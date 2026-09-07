#!/usr/bin/env python3
"""Use the bundled tmux helper, with a systemd cgroup deadline around Codex exec."""
import argparse
import datetime as dt
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
HELPER = Path('/home/nico/.codex/skills/codex-tmux-runner/scripts/codex_tmux.py')
CODEX = '/home/nico/.local/bin/codex'
SELF = str(Path(__file__).resolve())
sys.path.insert(0, str(Path(__file__).resolve().parent))
import resilience


def write_json(path, value):
    resilience.write_json(path, value)


def utc(t):
    return t.isoformat()


def require_execution_config(config):
    if config.get('launch_authorized') is not True:
        raise RuntimeError('User launch confirmation has not been recorded for this plan')
    if config.get('deadline_supervisor_verified') is not True:
        raise RuntimeError('Deadline verification is required before execution')
    duration = config.get('max_wall_seconds')
    if type(duration) is not int or not 20 <= duration <= 21600:
        raise RuntimeError('A valid finite deadline is required before execution')
    if config.get('goal_tools_allowed') or config.get('automatic_resume'):
        raise RuntimeError('Goal runs and automatic resumes are not supported')


def entry(manifest_path):
    manifest_path = Path(manifest_path)
    config = json.loads(manifest_path.read_text())
    require_execution_config(config)
    cgroup = Path('/proc/self/cgroup').read_text().strip()
    if config['systemd_unit'] not in cgroup.split('/'):
        raise RuntimeError('Codex entry must execute inside its run-owned timed service')
    start = dt.datetime.now(dt.timezone.utc)
    config.update(start_utc=utc(start), start_monotonic=time.monotonic(),
                  hard_deadline_utc=utc(start + dt.timedelta(seconds=config['max_wall_seconds'])),
                  phase_deadlines_utc={k: utc(start + dt.timedelta(seconds=v))
                      for k, v in config['phase_boundaries_seconds'].items()},
                  status='running', coordinator_pid=os.getpid(),
                  cgroup=cgroup)
    write_json(manifest_path, config)
    final_path = manifest_path.parent / 'final.md'
    if not final_path.exists():
        final_path.write_text('Run in progress. No findings recorded yet.\n')
    os.chdir(config['project_root'])
    os.execv(config['codex_command'][0], config['codex_command'])


def service(manifest_path):
    config = json.loads(Path(manifest_path).read_text())
    require_execution_config(config)
    unit = config['systemd_unit']
    # SIGINT and a five-second SIGKILL grace both fit inside the user cap.
    command = ['/usr/bin/systemd-run', '--user', '--pipe', '--wait',
               '--unit=' + unit, '--service-type=exec',
               '--property=RuntimeMaxSec=' + str(config['max_wall_seconds'] - 10),
               '--property=TimeoutStopSec=5', '--property=KillMode=control-group',
               '--property=SendSIGKILL=yes', '--property=KillSignal=SIGINT', '--property=Restart=no',
               '--property=WorkingDirectory=' + config['project_root']]
    for name in ('HOME', 'USER', 'LOGNAME', 'PATH', 'CODEX_HOME', 'XDG_RUNTIME_DIR', 'TMPDIR'):
        if name in os.environ:
            command.append('--setenv=' + name + '=' + os.environ[name])
    command += [sys.executable, SELF, '_entry', str(manifest_path)]
    write_json(Path(manifest_path).parent / 'deadline-status.json', {
        'state': 'starting', 'systemd_unit': unit, 'service_command': command})
    monitor = resilience.Monitor(manifest_path)
    process = None
    received_signal = None
    monitor_error = None
    returncode = 1
    fields = {}
    previous_handlers = {}

    def interrupted(signum, frame):
        nonlocal received_signal
        received_signal = signum

    def properties():
        try:
            result = subprocess.run(['/usr/bin/systemctl', '--user', 'show', unit,
                '--property=ActiveState,SubState,Result,ExecMainCode,ExecMainStatus,ControlGroup'],
                text=True, capture_output=True, timeout=5)
            values = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
            if result.returncode:
                values['ObservationError'] = result.stderr.strip()[:1000]
            return values
        except (OSError, subprocess.TimeoutExpired) as exc:
            return {'ObservationError': str(exc)}

    def stop_owned_service():
        try:
            stopped = subprocess.run(['/usr/bin/systemctl', '--user', 'stop', unit],
                                     capture_output=True, text=True, timeout=10)
            if stopped.returncode:
                monitor.alert('ordinary_failure', 'Service stop returned nonzero: ' + stopped.stderr[:1000],
                              source='systemd_stop')
        except (OSError, subprocess.TimeoutExpired) as exc:
            monitor.alert('ordinary_failure', 'Could not confirm service stop: ' + str(exc), source='systemd_stop')

    try:
        for signum in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            previous_handlers[signum] = signal.signal(signum, interrupted)
        process = subprocess.Popen(command)
        while True:
            fields = properties()
            monitor.tick(fields)
            if monitor.stop_reason:
                stop_owned_service()
                returncode = 1
                break
            if received_signal:
                stop_owned_service()
                returncode = 128 + received_signal
                break
            observed_code = process.poll()
            if observed_code is not None:
                returncode = observed_code
                break
            # The independent service timer remains authoritative; this only bounds
            # a stuck systemd-run client or failed external monitor observation.
            if time.monotonic() - monitor.started > config['max_wall_seconds'] + 30:
                raise RuntimeError('Service launcher remained live beyond deadline plus observation grace')
            time.sleep(monitor.settings['monitor_poll_seconds'])
    except (Exception, KeyboardInterrupt) as exc:
        monitor_error = type(exc).__name__ + ': ' + str(exc)
        stop_owned_service()
    finally:
        try:
            if process is not None and process.poll() is None:
                try:
                    process.wait(timeout=7)
                except subprocess.TimeoutExpired:
                    process.terminate()
                    try:
                        process.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=2)
        except (OSError, subprocess.TimeoutExpired) as exc:
            monitor_error = (monitor_error or '') + '\nClient cleanup failed: ' + str(exc)
        fields = properties()
        # A zero systemd-run exit is operational evidence only. The finalizer
        # explicitly leaves mathematical completeness for a human/coordinator audit.
        try:
            final = monitor.finalize(returncode, fields, received_signal, monitor_error)
            state = ('time_limit' if fields.get('Result') == 'timeout' else
                     'unverified' if final['process_outcome'] == 'unverified' else
                     'completed' if final['process_success'] else 'failed_or_interrupted')
            latest = json.loads(Path(manifest_path).read_text())
            latest.update(status=state, ended_at=final['ended_at'], service_exit_code=returncode,
                          failure_category=final['failure_category'],
                          scientific_completeness=final['scientific_completeness'])
            write_json(manifest_path, latest)
            write_json(Path(manifest_path).parent / 'deadline-status.json', {
                'state': state, 'systemd_unit': unit, 'exit_code': returncode,
                'ended_at': final['ended_at'], 'systemd': fields,
                'failure_category': final['failure_category'], 'exit_manifest': 'exit-manifest.json'})
        finally:
            for signum, handler in previous_handlers.items():
                signal.signal(signum, handler)
    return returncode


def load_plan(args):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,69}', args.run_id):
        raise ValueError('Run ID must be a safe, unique basename of at most 70 characters')
    plan_dir = Path(args.plan_dir).resolve()
    if not plan_dir.is_relative_to(ROOT):
        raise ValueError('The plan directory must be inside the project')
    config = json.loads((plan_dir / 'run-config.json').read_text())
    for name in ('PLAN.md', 'COORDINATOR_PROMPT.md', 'TASK_TEMPLATE.md'):
        if not (plan_dir / name).is_file():
            raise ValueError('Missing plan file: ' + name)
    if config.get('research_scope_file') is not None:
        scope_path = (plan_dir / config['research_scope_file']).resolve()
        if not scope_path.is_relative_to(plan_dir) or not scope_path.is_file():
            raise ValueError('Research scope must be a readable file inside the plan directory')
        scope_path.read_text()
    config.update(resilience.monitoring_config(config))
    base_duration = config['max_wall_seconds']
    duration = base_duration if args.seconds is None else args.seconds
    if not 20 <= duration <= min(21600, base_duration):
        raise ValueError('Duration must be between 20 seconds and the plan maximum')
    phases = config['phase_boundaries_seconds']
    values = list(phases.values())
    if values != sorted(values) or min(values) <= 0 or phases['hard_stop'] != base_duration:
        raise ValueError('Invalid phase boundaries')
    if phases['workers_stop'] >= base_duration:
        raise ValueError('Worker stop must leave shutdown time')
    if config.get('goal_tools_allowed') or config.get('automatic_resume'):
        raise ValueError('This launcher supports finite non-goal runs only')
    if config.get('model') != 'gpt-6-astra' or config.get('reasoning_effort') != 'ultra':
        raise ValueError('This launcher is configured for the user-requested Astra ultra')
    if duration != base_duration:
        phases = {k: round(v * duration / base_duration) for k, v in phases.items()}
    config.update(max_wall_seconds=duration, phase_boundaries_seconds=phases,
                  plan_directory=str(plan_dir))
    return plan_dir, config


def launch(args):
    plan_dir, config = load_plan(args)
    if args.validate_only:
        print(json.dumps({'validation': 'passed', 'creates_run': False,
            'plan_directory': str(plan_dir), 'max_wall_seconds': config['max_wall_seconds'],
            'launch_authorized': config.get('launch_authorized', False),
            'phase_boundaries_seconds': config['phase_boundaries_seconds'],
            'systemd_runtime_seconds': config['max_wall_seconds'] - 10,
            'systemd_stop_grace_seconds': 5}, indent=2))
        return 0
    require_execution_config(config)
    run_dir = ROOT / 'exploration' / 'runs' / args.run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    manifest_path = run_dir / 'run.json'
    config.update(run_id=args.run_id, project_root=str(ROOT), output_directory=str(run_dir),
        status='launching',
        systemd_unit=args.run_id + '.service', model='gpt-6-astra', reasoning_effort='ultra',
        deadline_supervisor_verified=True,
        run_kind='launch_smoke' if args.smoke else config['run_kind'],
        codex_home=os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    prompt = ('Active run manifest: ' + str(manifest_path) + '\n\n' +
              (Path(args.smoke).read_text() if args.smoke else
               (plan_dir / 'COORDINATOR_PROMPT.md').read_text()))
    if config.get('research_scope_file'):
        prompt += '\n\n' + (plan_dir / config['research_scope_file']).read_text() + '\n'
    prompt += ('\nExecution constraints: use local in-process collaboration only. '
        'Do not use remote execution environments, external worker services, tmux, systemd, '
        'nohup, or another Codex CLI to launch work. Every research worker must run '
        'gpt-6-astra with ultra reasoning: specify model="gpt-6-astra", '
        'reasoning_effort="ultra", fork_turns="none" when creating workers. '
        'Do not alter runner code, deadline metadata, or service settings. '
        'Record agent IDs and available session/thread UUIDs in agents.json; run.json is launcher-owned. '
        'After each worker result and every five minutes, update claims.json, reconciliation.md, '
        'progress.md, final.md and agents.json, then call python3 ' + SELF +
        ' checkpoint --run-file ' + str(manifest_path) +
        ' --reason "describe the checkpoint update". Runner snapshots do not establish mathematical progress. '
        'Read public sources with built-in web tools. No goal tools or automatic resume.\n')
    prompt_path = run_dir / 'prompt.md'
    prompt_path.write_text(prompt)
    spec = importlib.util.spec_from_file_location('tmux_runner', HELPER)
    runner = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runner)
    parsed = runner.make_parser().parse_args([
        'launch', '--root', str(ROOT), '--session', args.run_id,
        '--prompt', str(prompt_path), '--log', str(run_dir / 'run.log'),
        '--run-file', str(run_dir / 'tmux-run.json'),
        '--status-file', str(run_dir / 'tmux-status.json'),
        '--codex', CODEX, '--permission-profile', 'sandbox-only',
        '--search', '--model', 'gpt-6-astra', '--reasoning-effort', 'ultra',
        '--allow-non-git', '--startup-timeout', '20'])
    manifest = runner.prepare_run(parsed, 'launch')
    config['codex_command'] = manifest['codex_command']
    write_json(manifest_path, config)
    # Keep the helper's sandbox preflight, process/log supervision and status sidecars.
    manifest['inner_codex_command'] = manifest['codex_command']
    manifest['codex_command'] = [sys.executable, SELF, '_service', str(manifest_path)]
    manifest['deadline_manifest'] = str(manifest_path)
    return runner.launch_prepared(manifest, dry_run=False, startup_timeout=20)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '_entry':
        entry(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == '_service':
        raise SystemExit(service(sys.argv[2]))
    elif len(sys.argv) > 1 and sys.argv[1] in ('checkpoint', 'status'):
        parser = argparse.ArgumentParser(description='Local checkpoint and monitoring status; no launches')
        parser.add_argument('command', choices=['checkpoint', 'status'])
        parser.add_argument('--run-file', required=True)
        parser.add_argument('--reason', default='')
        args = parser.parse_args()
        result = (resilience.checkpoint(args.run_file, args.reason) if args.command == 'checkpoint'
                  else resilience.status(args.run_file))
        print(json.dumps(result, indent=2))
    else:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('--run-id', required=True)
        parser.add_argument('--plan-dir', default=str(ROOT / 'exploration'))
        parser.add_argument('--validate-only', action='store_true',
                            help='Check plan/config without preflight, files, services, or model calls')
        parser.add_argument('--seconds', type=int)
        parser.add_argument('--smoke', help='Use this bounded launch-test prompt instead of research')
        raise SystemExit(launch(parser.parse_args()))
