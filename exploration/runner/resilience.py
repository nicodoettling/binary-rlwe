"""Local observation and artifact preservation. No model calls or restart logic."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import time
import uuid

CORE_ARTIFACTS = ('claims.json', 'reconciliation.md', 'progress.md', 'final.md', 'agents.json')
MONITOR_DEFAULTS = {'monitor_poll_seconds': 5, 'snapshot_interval_seconds': 300,
                    'coordinator_checkpoint_stale_seconds': 600}
EXCLUDED = {'runner-snapshots', 'coordinator-checkpoints', 'alerts', '__pycache__',
            'run.json', 'prompt.md', 'tmux-run.json', 'tmux-status.json',
            'deadline-status.json', 'monitor-status.json', 'coordinator-checkpoint.json',
            'artifact-index.json', 'exit-manifest.json', 'interruption.md'}
UUID = re.compile(r'^[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$', re.I)


def now_utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sync_directory(path):
    descriptor = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def write_json(path, value):
    """Concurrent writers use unique temporary files; readers see one complete value."""
    path = Path(path)
    descriptor, temporary = tempfile.mkstemp(prefix='.' + path.name + '-', dir=path.parent)
    try:
        with os.fdopen(descriptor, 'w') as handle:
            json.dump(value, handle, indent=2)
            handle.write('\n')
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        sync_directory(path.parent)
    finally:
        Path(temporary).unlink(missing_ok=True)


def read_json(path, default=None):
    try:
        value = json.loads(Path(path).read_text())
        return value if isinstance(value, dict) else ({} if default is None else default)
    except (OSError, ValueError):
        return {} if default is None else default


def monitoring_config(config):
    result = {}
    for key, default in MONITOR_DEFAULTS.items():
        value = config.get(key, default)
        if type(value) is not int or not 1 <= value <= 3600:
            raise ValueError(key + ' must be an integer between 1 and 3600')
        result[key] = value
    if result['monitor_poll_seconds'] > min(result['snapshot_interval_seconds'],
                                            result['coordinator_checkpoint_stale_seconds']):
        raise ValueError('Monitor polling must be at least as frequent as checkpoints')
    return result


def artifact_files(run_dir, core_only=False):
    if core_only:
        return [run_dir / name for name in CORE_ARTIFACTS if (run_dir / name).exists()]
    paths = []
    for parent, directories, files in os.walk(run_dir, followlinks=False):
        directories[:] = sorted(d for d in directories if d not in EXCLUDED and
                                 not d.startswith('.') and not (Path(parent) / d).is_symlink())
        for name in sorted(files):
            if name not in EXCLUDED and not name.startswith('.') and not name.endswith(('.log', '.tmp')):
                paths.append(Path(parent) / name)
    return sorted(paths)


def signature(path):
    s = path.lstat()
    if not stat.S_ISREG(s.st_mode):
        raise ValueError('Artifact is not a regular file: ' + str(path))
    return (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)


def snapshot(run_dir, kind='periodic', reason='', core_only=False):
    """Publish a stable file set by rename, with hashes of the exact copied bytes.

    This is a bounded optimistic filesystem capture, not a transactional scientific
    checkpoint. Concurrent modification aborts and preserves all earlier snapshots.
    """
    run_dir = Path(run_dir)
    store = run_dir / ('coordinator-checkpoints' if core_only else 'runner-snapshots')
    store.mkdir(exist_ok=True)
    for attempt in range(3):
        staging = Path(tempfile.mkdtemp(prefix='.staging-', dir=store))
        try:
            paths = artifact_files(run_dir, core_only)
            before = {p: signature(p) for p in paths}
            if sum(s[2] for s in before.values()) > 256 * 1024 * 1024:
                raise ValueError('Artifact snapshot exceeds the 256 MiB capture limit')
            entries = []
            for path in paths:
                relative = path.relative_to(run_dir)
                destination = staging / 'artifacts' / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                digest = hashlib.sha256()
                # O_NOFOLLOW prevents following a file replaced by a symlink after enumeration.
                descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
                with os.fdopen(descriptor, 'rb') as source, destination.open('wb') as target:
                    if not stat.S_ISREG(os.fstat(source.fileno()).st_mode):
                        raise ValueError('Artifact changed into a special file')
                    copied = 0
                    while True:
                        block = source.read(1024 * 1024)
                        if not block:
                            break
                        copied += len(block)
                        if copied > before[path][2]:
                            raise OSError('Artifact grew during capture')
                        digest.update(block)
                        target.write(block)
                    target.flush()
                    os.fsync(target.fileno())
                entries.append({'path': str(relative), 'bytes': copied,
                                'sha256': digest.hexdigest()})
            if paths != artifact_files(run_dir, core_only) or any(signature(p) != s for p, s in before.items()):
                raise OSError('Artifacts changed during capture')
            identity = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ-') + uuid.uuid4().hex[:8]
            manifest = {'schema_version': 1, 'snapshot_id': identity, 'kind': kind,
                        'created_at': now_utc(), 'reason': reason, 'artifacts': entries,
                        'missing_core_artifacts': [name for name in CORE_ARTIFACTS
                                                   if name not in {e['path'] for e in entries}],
                        'consistency': 'stable_file_set_during_copy; scientific_coherence_not_verified',
                        'scientific_progress_verified': False}
            write_json(staging / 'manifest.json', manifest)
            for directory, _, _ in os.walk(staging, topdown=False):
                sync_directory(directory)
            destination = store / identity
            staging.rename(destination)
            sync_directory(store)
            return {'directory': str(destination.relative_to(run_dir)), **manifest}
        except (OSError, ValueError):
            shutil.rmtree(staging, ignore_errors=True)
            if attempt == 2:
                raise
    raise AssertionError('unreachable')


def checkpoint(manifest_path, reason):
    run_dir = Path(manifest_path).resolve().parent
    config = read_json(manifest_path)
    if config.get('status') != 'running':
        raise ValueError('Coordinator checkpoints require a running manifest')
    if not reason.strip():
        raise ValueError('Checkpoint reason must describe the update')
    capture = snapshot(run_dir, 'coordinator', reason, core_only=True)
    if capture['missing_core_artifacts']:
        raise ValueError('Checkpoint missing required artifacts: ' + ', '.join(capture['missing_core_artifacts']))
    for name in CORE_ARTIFACTS:
        copied = run_dir / capture['directory'] / 'artifacts' / name
        if not copied.read_text().strip():
            raise ValueError('Checkpoint artifact is empty: ' + name)
        if name.endswith('.json'):
            json.loads(copied.read_text())
    # A repeated command without changed scientific artifacts cannot clear a stale warning.
    substantive = [a for a in capture['artifacts'] if a['path'] != 'agents.json']
    fingerprint = hashlib.sha256(json.dumps(substantive, sort_keys=True).encode()).hexdigest()
    previous = read_json(run_dir / 'coordinator-checkpoint.json')
    changed = previous.get('content_sha256') != fingerprint
    receipt = {'schema_version': 1, 'created_at': now_utc(), 'reason': reason,
               'snapshot_directory': capture['directory'], 'content_sha256': fingerprint,
               'last_content_change_at': now_utc() if changed else previous.get('last_content_change_at'),
               'content_changed': changed, 'scientific_progress_verified': False,
               'meaning': 'Coordinator supplied an updated artifact set; mathematical progress is not inferred'}
    write_json(run_dir / 'coordinator-checkpoint.json', receipt)
    return receipt


def classify_error(error):
    if not isinstance(error, dict):
        error = {'message': str(error)}
    code = error.get('codex_error_info', error.get('code', ''))
    code_text = json.dumps(code).lower()
    message = str(error.get('message', ''))
    lowered = message.lower()
    if 'cyber_policy' in code_text or 'flagged for possible cybersecurity risk' in lowered:
        category = 'cyber_policy'
    elif any(s in code_text for s in ('permission_denied', 'permission_denial', 'approval_denied', 'sandbox_denied')) or any(
            s in lowered for s in ('permission denied', 'approval request denied', 'approval request rejected',
                                   'automatic approval review rejected', 'sandbox denied')):
        category = 'permission_denial'
    elif any(s in code_text for s in ('timeout', 'timed_out')):
        category = 'timeout'
    else:
        category = 'ordinary_failure'
    return {'category': category, 'code': code, 'message': message[:4000]}


def structured_error(record):
    if not isinstance(record, dict):
        return None
    if record.get('type') == 'event_msg':
        payload = record.get('payload', {})
        if not isinstance(payload, dict):
            return None
        if payload.get('type') == 'error':
            return payload.get('error', payload)
        if payload.get('type') in ('task_complete', 'turn_complete', 'turn_aborted') and payload.get('error'):
            return payload['error']
    if record.get('type') in ('error', 'turn.failed'):
        return record.get('error', record)
    return None


class IncrementalLines:
    """Read only complete lines and tolerate truncation/rotation without unbounded reads."""
    def __init__(self):
        self.positions = {}
        self.oversized_lines_skipped = 0

    def read(self, path):
        path = Path(path)
        try:
            s = path.stat()
            offset, inode, skipping = self.positions.get(str(path), (0, s.st_ino, False))
            if inode != s.st_ino or s.st_size < offset:
                offset = 0
                skipping = False
            with path.open('rb') as handle:
                handle.seek(offset)
                data = handle.read(4 * 1024 * 1024)
            if skipping:
                boundary = data.find(b'\n') + 1
                if not boundary:
                    self.positions[str(path)] = (offset + len(data), s.st_ino, True)
                    return []
                offset += boundary
                data = data[boundary:]
                skipping = False
            end = data.rfind(b'\n') + 1
            if not end and len(data) == 4 * 1024 * 1024:
                self.oversized_lines_skipped += 1
                self.positions[str(path)] = (offset + len(data), s.st_ino, True)
                return []
            self.positions[str(path)] = (offset + end, s.st_ino, skipping)
            return data[:end].decode('utf-8', errors='replace').splitlines()
        except OSError:
            return []


class Monitor:
    def __init__(self, manifest_path):
        self.manifest_path = Path(manifest_path)
        self.run_dir = self.manifest_path.parent
        self.config = read_json(self.manifest_path)
        self.settings = monitoring_config(self.config)
        self.started = time.monotonic()
        self.started_at = now_utc()
        self.next_snapshot = self.started
        self.lines = IncrementalLines()
        self.alerts = []
        self.seen = set()
        self.latest_snapshot = None
        self.session_paths = {}
        self.session_root = Path(self.config.get('codex_home', os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))) / 'sessions'
        self.last_discovery = -1e10
        self.stale_key = None
        self.systemd = {}
        self.stop_reason = None

    def alert(self, category, message, **evidence):
        key = json.dumps([category, message, evidence], sort_keys=True)
        if key in self.seen:
            return
        self.seen.add(key)
        record = {'observed_at': now_utc(), 'category': category, 'message': message,
                  'automatic_action': 'no retry or resume; confirmed policy block stops owning service', **evidence}
        directory = self.run_dir / 'alerts'
        directory.mkdir(exist_ok=True)
        write_json(directory / (uuid.uuid4().hex + '.json'), record)
        self.alerts.append(record)
        try:
            print('[bounded-run local alert] ' + category + ': ' + message, file=sys.stderr, flush=True)
        except (BrokenPipeError, OSError):
            pass

    def discover_sessions(self, monotonic):
        status = read_json(self.run_dir / 'tmux-status.json')
        ids = {status.get('codex_session_id', '')}
        def collect(value):
            if isinstance(value, dict):
                for key, item in value.items():
                    if key in ('session_id', 'codex_session_id', 'thread_id') and isinstance(item, str):
                        ids.add(item)
                    elif isinstance(item, (dict, list)):
                        collect(item)
            elif isinstance(value, list):
                for item in value:
                    collect(item)
        collect(read_json(self.run_dir / 'agents.json'))
        if monotonic - self.last_discovery < 30 and ids.issubset(self.session_paths):
            return
        self.last_discovery = monotonic
        for session_id in ids:
            if isinstance(session_id, str) and UUID.fullmatch(session_id) and session_id not in self.session_paths:
                matches = list(self.session_root.glob('*/*/*/*' + session_id + '.jsonl'))
                if len(matches) == 1:
                    self.session_paths[session_id] = matches[0]

    def scan_errors(self, monotonic):
        self.discover_sessions(monotonic)
        for session_id, path in self.session_paths.items():
            for line in self.lines.read(path):
                try:
                    record = json.loads(line)
                except ValueError:
                    continue
                error = structured_error(record)
                if error:
                    classified = classify_error(error)
                    if classified['category'] == 'cyber_policy':
                        self.stop_reason = {'category': 'cyber_policy', 'source': 'persisted_session_error',
                                            'session_id': session_id, 'event_timestamp': record.get('timestamp')}
                    self.alert(classified.pop('category'), classified.pop('message'),
                               source='persisted_session_error', session_id=session_id,
                               event_timestamp=record.get('timestamp'), **classified)
        for line in self.lines.read(self.run_dir / 'run.log'):
            if line.startswith('ERROR: '):
                classified = classify_error({'message': line[7:]})
                candidate = classified.pop('category')
                self.alert('unconfirmed_log_error', classified.pop('message'),
                           source='current_log_error_line', candidate_category=candidate,
                           reason='Text log may contain quoted/tool output; structured provenance required', **classified)
        if self.lines.oversized_lines_skipped:
            self.alert('observation_gap', 'Oversized records were skipped by the bounded log reader',
                       source='log_reader', skipped_records=self.lines.oversized_lines_skipped)

    def capture(self, kind):
        try:
            self.latest_snapshot = snapshot(self.run_dir, kind)
            write_json(self.run_dir / 'artifact-index.json', self.latest_snapshot)
        except (OSError, ValueError) as exc:
            self.alert('snapshot_failure', str(exc), source='filesystem_capture')

    def checkpoint_health(self):
        receipt = read_json(self.run_dir / 'coordinator-checkpoint.json')
        last = receipt.get('last_content_change_at') or self.config.get('start_utc') or self.started_at
        try:
            age = max(0, (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(last)).total_seconds())
        except (TypeError, ValueError):
            age = (time.monotonic() - self.started)
        stale = age >= self.settings['coordinator_checkpoint_stale_seconds']
        if stale and self.stale_key != last:
            self.stale_key = last
            self.alert('stale_coordinator_checkpoint', 'No changed coordinator checkpoint within the configured threshold',
                       last_content_change_at=last, source='checkpoint_receipt')
        return {'stale': stale, 'age_seconds': round(age, 1), 'last_content_change_at': last,
                'receipt_present': bool(receipt), 'scientific_progress_verified': False}

    def tick(self, systemd=None, allow_snapshot=True):
        monotonic = time.monotonic()
        if systemd is not None:
            self.systemd = systemd
        self.scan_errors(monotonic)
        if self.systemd.get('Result') == 'timeout':
            self.alert('timeout', 'Timed service reached its runtime limit', source='systemd')
        if allow_snapshot and not self.stop_reason and monotonic >= self.next_snapshot:
            self.capture('periodic')
            interval = self.settings['snapshot_interval_seconds']
            self.next_snapshot += (int((monotonic - self.next_snapshot) // interval) + 1) * interval
        checkpoint_state = self.checkpoint_health()
        write_json(self.run_dir / 'monitor-status.json', {
            'state': 'monitoring', 'heartbeat_at': now_utc(), 'monitor_pid': os.getpid(),
            'settings': self.settings, 'systemd': self.systemd,
            'observed_session_ids': list(self.session_paths),
            'error_observation_scope': 'coordinator and explicit session/thread UUIDs in agents.json',
            'alerts': self.alerts, 'checkpoint': checkpoint_state,
            'latest_snapshot': self.latest_snapshot and self.latest_snapshot['directory'],
            'stop_reason': self.stop_reason,
            'automatic_resume': False})

    def finalize(self, exit_code, systemd, signal_number=None, monitor_error=None):
        try:
            self.tick(systemd, allow_snapshot=False)
        except Exception as exc:
            self.alert('ordinary_failure', 'Final observation failed: ' + str(exc), source='external_monitor')
        if monitor_error:
            self.alert('ordinary_failure', monitor_error, source='external_monitor')
        elif signal_number:
            self.alert('ordinary_failure', 'External monitor received signal ' + str(signal_number), source='signal')
        elif exit_code != 0 and not any(a['category'] in ('cyber_policy', 'permission_denial', 'timeout', 'ordinary_failure') for a in self.alerts):
            self.alert('ordinary_failure', 'Service launcher exited with code ' + str(exit_code), source='process_exit')
        self.capture('exit')
        if self.latest_snapshot is None:
            write_json(self.run_dir / 'artifact-index.json', {
                'artifacts': [], 'capture_state': 'unavailable', 'scientific_progress_verified': False})
        categories = list(dict.fromkeys(a['category'] for a in self.alerts))
        primary = next((c for c in ('cyber_policy', 'permission_denial', 'timeout', 'ordinary_failure') if c in categories), None)
        process_success = (exit_code == 0 and systemd.get('Result') == 'success' and
                           systemd.get('ActiveState') == 'inactive' and
                           not systemd.get('ObservationError') and not signal_number and not monitor_error and
                           not self.stop_reason)
        saved = {a['path']: a for a in (self.latest_snapshot or {}).get('artifacts', [])}
        artifact_state = {name: {'present': name in saved, 'empty': saved[name]['bytes'] == 0 if name in saved else None}
                          for name in CORE_ARTIFACTS}
        agents = read_json(self.run_dir / 'agents.json')
        entries = agents.get('agents', [])
        agents_valid = isinstance(entries, list) and all(isinstance(a, dict) for a in entries)
        unfinished = [a for a in entries if a.get('status') not in ('completed', 'closed', 'cancelled')] if agents_valid else []
        manifest = {'schema_version': 1, 'ended_at': now_utc(),
                    'process_outcome': ('succeeded' if process_success else 'interrupted' if signal_number or self.stop_reason
                                        else 'unverified' if exit_code == 0 else 'failed'),
                    'process_success': process_success, 'exit_code': exit_code, 'signal': signal_number,
                    'failure_category': primary, 'observed_categories': categories,
                    'systemd': systemd, 'service_inactive_observed': systemd.get('ActiveState') in ('inactive', 'failed'),
                    'descendant_shutdown': 'not_independently_verified_by_finalizer',
                    'scientific_completeness': 'not_verified_by_runner',
                    'reconciliation_state': 'present_unverified' if 'reconciliation.md' in saved else 'missing',
                    'artifact_state': artifact_state, 'unfinished_agents_as_recorded': unfinished,
                    'agent_registry_state': 'readable_list' if agents_valid and agents else 'missing_or_invalid',
                    'artifact_state_basis': 'latest successfully captured snapshot; live files may differ if exit capture failed',
                    'review_reconciliation': 'Read preserved claims.json and reconciliation.md; runner does not resolve objections',
                    'latest_snapshot': self.latest_snapshot and self.latest_snapshot['directory'],
                    'exit_snapshot_succeeded': bool(self.latest_snapshot and self.latest_snapshot['kind'] == 'exit'),
                    'coordinator_checkpoint': read_json(self.run_dir / 'coordinator-checkpoint.json'),
                    'stop_reason': self.stop_reason,
                    'alerts': self.alerts, 'automatic_resume': False}
        write_json(self.run_dir / 'exit-manifest.json', manifest)
        status = read_json(self.run_dir / 'monitor-status.json')
        status.update(state='finalized', heartbeat_at=now_utc(), alerts=self.alerts,
                      latest_snapshot=manifest['latest_snapshot'], exit_manifest='exit-manifest.json')
        write_json(self.run_dir / 'monitor-status.json', status)
        return manifest


def status(manifest_path):
    run_dir = Path(manifest_path).resolve().parent
    result = {'run': read_json(manifest_path), 'monitor': read_json(run_dir / 'monitor-status.json'),
              'exit': read_json(run_dir / 'exit-manifest.json'),
              'coordinator_checkpoint': read_json(run_dir / 'coordinator-checkpoint.json')}
    monitor = result['monitor']
    try:
        age = (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(monitor['heartbeat_at'])).total_seconds()
        result['monitor_heartbeat_stale'] = monitor.get('state') != 'finalized' and age > max(
            30, 3 * monitor.get('settings', MONITOR_DEFAULTS)['monitor_poll_seconds'])
    except (KeyError, TypeError, ValueError):
        result['monitor_heartbeat_stale'] = True
    result['interpretation'] = 'Persisted observation only; process success does not establish scientific completeness'
    return result
