"""Unit tests only: fake service processes and local fixture logs; no model/service calls."""
import contextlib
import ast
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import signal
import subprocess
import tempfile
import unittest
from unittest import mock

import bounded_run as runner
import resilience as r


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.run = self.directory / 'run'
        self.run.mkdir()
        self.manifest = self.run / 'run.json'
        self.config = {'status': 'running', 'max_wall_seconds': 1200,
                       'launch_authorized': True, 'deadline_supervisor_verified': True,
                       'systemd_unit': 'fixture-owned.service', 'project_root': str(self.directory),
                       'codex_home': str(self.directory / 'codex')}
        r.write_json(self.manifest, self.config)
        self.stderr = io.StringIO()
        self.redirect = contextlib.redirect_stderr(self.stderr)
        self.redirect.__enter__()
        self.addCleanup(self.redirect.__exit__, None, None, None)

    def artifacts(self):
        for name in r.CORE_ARTIFACTS:
            (self.run / name).write_text('{}\n' if name.endswith('.json') else 'Partial, unverified work.\n')

    def session(self, session_id='01a07718-4189-7492-9b02-8b3ae06ab59d'):
        r.write_json(self.run / 'tmux-status.json', {'codex_session_id': session_id})
        path = Path(self.config['codex_home']) / 'sessions/2026/09/06' / ('rollout-' + session_id + '.jsonl')
        path.parent.mkdir(parents=True, exist_ok=True)
        return path


class ErrorTests(Fixture):
    def test_structured_actual_terminal_record(self):
        path = self.session()
        path.write_text(json.dumps({'timestamp': '2026-09-06T15:59:47Z', 'type': 'event_msg',
            'payload': {'type': 'task_complete', 'error': {'message': 'Content flagged.',
                                                       'codex_error_info': 'cyber_policy'}}}) + '\n')
        monitor = r.Monitor(self.manifest)
        monitor.tick()
        self.assertEqual(monitor.alerts[0]['category'], 'cyber_policy')
        self.assertEqual(monitor.alerts[0]['source'], 'persisted_session_error')
        self.assertIn('cyber_policy', self.stderr.getvalue())
        self.assertEqual(len(list((self.run / 'alerts').glob('*.json'))), 1)
        monitor.tick()
        self.assertEqual(len(monitor.alerts), 1)

    def test_quotes_and_other_sessions_do_not_classify(self):
        path = self.session()
        path.write_text(json.dumps({'type': 'response_item', 'payload': {'type': 'message',
            'role': 'assistant', 'content': 'ERROR: historical cyber_policy'}}) + '\n')
        other = path.with_name('rollout-01a07718-4189-7492-9b02-8b3ae06ab500.jsonl')
        other.write_text(json.dumps({'type': 'error', 'message': 'permission denied'}) + '\n')
        (self.run / 'run.log').write_text('Research discussion of cyber_policy and permission denied.\n')
        monitor = r.Monitor(self.manifest)
        monitor.tick()
        self.assertEqual(monitor.alerts, [])

    def test_partial_record_then_completed_line(self):
        path = self.session()
        line = json.dumps({'type': 'error', 'error': {'codex_error_info': 'permission_denied', 'message': 'Denied'}})
        path.write_text(line[:-1])
        monitor = r.Monitor(self.manifest)
        monitor.tick()
        self.assertFalse(monitor.alerts)
        with path.open('a') as handle:
            handle.write('}\n')
        monitor.tick()
        self.assertEqual(monitor.alerts[0]['category'], 'permission_denial')

    def test_categories_are_distinct(self):
        for code, expected in [('cyber_policy', 'cyber_policy'), ('permission_denied', 'permission_denial'),
                               ('request_timeout', 'timeout'), ('server_error', 'ordinary_failure')]:
            self.assertEqual(r.classify_error({'codex_error_info': code})['category'], expected)

    def test_current_cli_log_fallback(self):
        (self.run / 'run.log').write_text('ERROR: This content was flagged for possible cybersecurity risk.\n')
        monitor = r.Monitor(self.manifest)
        monitor.tick()
        self.assertEqual(monitor.alerts[0]['category'], 'unconfirmed_log_error')
        self.assertEqual(monitor.alerts[0]['candidate_category'], 'cyber_policy')
        self.assertEqual(monitor.alerts[0]['source'], 'current_log_error_line')
        self.assertIsNone(monitor.stop_reason)

    def test_historical_error_in_fenced_output_is_not_a_confirmed_failure(self):
        (self.run / 'run.log').write_text('assistant\nPrevious run said:\n```\n'
            'ERROR: This content was flagged for possible cybersecurity risk.\n```\n')
        final = r.Monitor(self.manifest).finalize(0, {'ActiveState': 'inactive', 'Result': 'success'})
        self.assertIsNone(final['failure_category'])
        self.assertIsNone(final['stop_reason'])
        self.assertTrue(final['process_success'])

    def test_oversized_line_reader_is_bounded_and_recovers(self):
        path = self.run / 'run.log'
        path.write_bytes(b'x' * (5 * 1024 * 1024) + b'\nERROR: later\n')
        reader = r.IncrementalLines()
        self.assertEqual(reader.read(path), [])
        self.assertEqual(reader.read(path), ['ERROR: later'])
        self.assertEqual(reader.oversized_lines_skipped, 1)

    def test_truncated_log_restarts_reader(self):
        path = self.run / 'run.log'
        path.write_text('A fairly long prior log message\n')
        reader = r.IncrementalLines()
        self.assertEqual(len(reader.read(path)), 1)
        path.write_text('ERROR: x\n')
        self.assertEqual(reader.read(path), ['ERROR: x'])


class SnapshotTests(Fixture):
    def test_copies_hashed_contents_preserves_previous_and_excludes_store(self):
        self.artifacts()
        first = r.snapshot(self.run)
        (self.run / 'final.md').write_text('New partial report\n')
        second = r.snapshot(self.run)
        self.assertNotEqual(first['directory'], second['directory'])
        self.assertEqual((self.run / first['directory'] / 'artifacts/final.md').read_text(), 'Partial, unverified work.\n')
        for entry in second['artifacts']:
            self.assertEqual(entry['sha256'], hashlib.sha256(
                (self.run / second['directory'] / 'artifacts' / entry['path']).read_bytes()).hexdigest())
        self.assertEqual(len(second['artifacts']), 5)
        self.assertFalse(second['scientific_progress_verified'])

    def test_failure_keeps_previous_snapshot_and_cleans_staging(self):
        self.artifacts()
        first = r.snapshot(self.run)
        with mock.patch.object(r, 'signature', side_effect=OSError('Concurrent mutation')):
            with self.assertRaises(OSError):
                r.snapshot(self.run)
        self.assertTrue((self.run / first['directory'] / 'manifest.json').is_file())
        self.assertFalse(list((self.run / 'runner-snapshots').glob('.staging-*')))

    def test_refuses_symlink_artifact(self):
        (self.directory / 'secret').write_text('outside')
        (self.run / 'final.md').symlink_to(self.directory / 'secret')
        with self.assertRaises(ValueError):
            r.snapshot(self.run)

    def test_checkpoint_requires_complete_nonempty_valid_artifacts(self):
        self.artifacts()
        (self.run / 'claims.json').write_text('{')
        with self.assertRaises(ValueError):
            r.checkpoint(self.manifest, 'checkpoint')
        self.assertFalse((self.run / 'coordinator-checkpoint.json').exists())

    def test_unchanged_checkpoint_does_not_reset_change_time(self):
        self.artifacts()
        first = r.checkpoint(self.manifest, 'Initial ledger')
        second = r.checkpoint(self.manifest, 'No new result')
        self.assertFalse(second['content_changed'])
        self.assertEqual(first['last_content_change_at'], second['last_content_change_at'])
        (self.run / 'agents.json').write_text('{"agents": []}\n')
        self.assertFalse(r.checkpoint(self.manifest, 'Agent status only')['content_changed'])
        (self.run / 'progress.md').write_text('Explicit unresolved next step\n')
        self.assertTrue(r.checkpoint(self.manifest, 'Recorded a result')['content_changed'])

    def test_fixed_snapshot_cadence(self):
        with mock.patch.object(r.time, 'monotonic', return_value=100):
            monitor = r.Monitor(self.manifest)
        with mock.patch.object(monitor, 'capture') as capture:
            for instant in (100, 200, 399, 400, 401, 710):
                with mock.patch.object(r.time, 'monotonic', return_value=instant):
                    monitor.tick()
            self.assertEqual(capture.call_count, 3)
            self.assertEqual(monitor.next_snapshot, 1000)

    def test_filesystem_snapshots_do_not_clear_staleness(self):
        self.config['start_utc'] = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(seconds=700)).isoformat()
        r.write_json(self.manifest, self.config)
        monitor = r.Monitor(self.manifest)
        monitor.tick()
        self.assertTrue(monitor.checkpoint_health()['stale'])
        self.assertEqual([a['category'] for a in monitor.alerts], ['stale_coordinator_checkpoint'])


class FinalizationTests(Fixture):
    def test_zero_exit_is_not_scientific_completion(self):
        self.artifacts()
        monitor = r.Monitor(self.manifest)
        final = monitor.finalize(0, {'ActiveState': 'inactive', 'Result': 'success'})
        self.assertTrue(final['process_success'])
        self.assertEqual(final['scientific_completeness'], 'not_verified_by_runner')
        self.assertEqual(final['reconciliation_state'], 'present_unverified')
        self.assertEqual((self.run / 'final.md').read_text(), 'Partial, unverified work.\n')
        self.assertTrue((self.run / 'artifact-index.json').is_file())
        self.assertTrue((self.run / 'exit-manifest.json').is_file())

    def test_timeout_missing_reconciliation_and_no_retry(self):
        final = r.Monitor(self.manifest).finalize(1, {'ActiveState': 'failed', 'Result': 'timeout'})
        self.assertEqual(final['failure_category'], 'timeout')
        self.assertEqual(final['reconciliation_state'], 'missing')
        self.assertFalse(final['automatic_resume'])
        self.assertFalse((self.run / 'final.md').exists())

    def test_finalizer_survives_observation_and_snapshot_failure(self):
        monitor = r.Monitor(self.manifest)
        with mock.patch.object(monitor, 'tick', side_effect=RuntimeError('bad observation')):
            with mock.patch.object(r, 'snapshot', side_effect=OSError('capture failed')):
                final = monitor.finalize(1, {})
        self.assertFalse(final['exit_snapshot_succeeded'])
        self.assertTrue((self.run / 'artifact-index.json').is_file())
        self.assertTrue((self.run / 'exit-manifest.json').is_file())

    def test_malformed_agent_registry_does_not_prevent_finalization(self):
        (self.run / 'agents.json').write_text('{"agents": null}')
        final = r.Monitor(self.manifest).finalize(1, {'ActiveState': 'failed'})
        self.assertEqual(final['agent_registry_state'], 'missing_or_invalid')
        self.assertTrue((self.run / 'exit-manifest.json').is_file())

    def test_unknown_service_state_does_not_claim_success(self):
        final = r.Monitor(self.manifest).finalize(0, {'ObservationError': 'No bus'})
        self.assertFalse(final['process_success'])
        self.assertEqual(final['process_outcome'], 'unverified')
        self.assertFalse(final['service_inactive_observed'])


class ServiceTests(Fixture):
    def systemctl(self, command, **kwargs):
        self.assertEqual(command[:2], ['/usr/bin/systemctl', '--user'])
        if command[2] == 'show':
            return subprocess.CompletedProcess(command, 0,
                'ActiveState=failed\nSubState=failed\nResult=timeout\nExecMainStatus=9\n', '')
        self.assertEqual(command[2:], ['stop', 'fixture-owned.service'])
        return subprocess.CompletedProcess(command, 0, '', '')

    def test_mock_service_is_monitored_and_finalized_with_timer_unchanged(self):
        process = mock.Mock()
        process.poll.side_effect = [None, 1, 1]
        with mock.patch.object(runner.subprocess, 'Popen', return_value=process) as launch:
            with mock.patch.object(runner.subprocess, 'run', side_effect=self.systemctl):
                with mock.patch.object(runner.time, 'sleep'):
                    self.assertEqual(runner.service(self.manifest), 1)
        command = launch.call_args.args[0]
        for option in ('--property=RuntimeMaxSec=1190', '--property=TimeoutStopSec=5',
                       '--property=KillMode=control-group', '--property=KillSignal=SIGINT',
                       '--property=SendSIGKILL=yes', '--property=Restart=no'):
            self.assertIn(option, command)
        final = r.read_json(self.run / 'exit-manifest.json')
        self.assertEqual(final['failure_category'], 'timeout')
        self.assertEqual(r.read_json(self.run / 'monitor-status.json')['state'], 'finalized')
        self.assertEqual(launch.call_count, 1)

    def test_launch_exception_still_finalizes(self):
        with mock.patch.object(runner.subprocess, 'Popen', side_effect=OSError('mock start failure')):
            with mock.patch.object(runner.subprocess, 'run', side_effect=self.systemctl):
                self.assertEqual(runner.service(self.manifest), 1)
        final = r.read_json(self.run / 'exit-manifest.json')
        self.assertIn('ordinary_failure', final['observed_categories'])
        self.assertFalse(final['process_success'])

    def test_confirmed_policy_error_stops_only_own_service(self):
        path = self.session()
        path.write_text(json.dumps({'type': 'event_msg', 'payload': {'type': 'task_complete',
            'error': {'message': 'Policy block', 'codex_error_info': 'cyber_policy'}}}) + '\n')
        process = mock.Mock()
        process.poll.return_value = 1
        with mock.patch.object(runner.subprocess, 'Popen', return_value=process) as launch:
            with mock.patch.object(runner.subprocess, 'run', side_effect=self.systemctl) as commands:
                self.assertEqual(runner.service(self.manifest), 1)
        stops = [c.args[0] for c in commands.call_args_list if c.args[0][2] == 'stop']
        self.assertEqual(stops, [['/usr/bin/systemctl', '--user', 'stop', 'fixture-owned.service']])
        final = r.read_json(self.run / 'exit-manifest.json')
        self.assertEqual(final['stop_reason']['category'], 'cyber_policy')
        self.assertEqual(launch.call_count, 1)

    def test_catchable_signal_stops_owned_service_and_finalizes(self):
        process = mock.Mock()
        process.poll.return_value = 1
        real_tick = r.Monitor.tick
        def tick(monitor, *args, **kwargs):
            real_tick(monitor, *args, **kwargs)
            signal.getsignal(signal.SIGTERM)(signal.SIGTERM, None)
        with mock.patch.object(runner.subprocess, 'Popen', return_value=process):
            with mock.patch.object(runner.subprocess, 'run', side_effect=self.systemctl):
                with mock.patch.object(r.Monitor, 'tick', tick):
                    self.assertEqual(runner.service(self.manifest), 128 + signal.SIGTERM)
        final = r.read_json(self.run / 'exit-manifest.json')
        self.assertEqual(final['signal'], signal.SIGTERM)
        self.assertEqual(final['process_outcome'], 'interrupted')

    def test_deadline_test_module_import_has_no_live_side_effects(self):
        import importlib.util
        path = Path(__file__).with_name('test_deadline.py')
        spec = importlib.util.spec_from_file_location('safe_deadline_import', path)
        module = importlib.util.module_from_spec(spec)
        with mock.patch.object(subprocess, 'run', side_effect=AssertionError('Launched a service')):
            with mock.patch.object(Path, 'mkdir', side_effect=AssertionError('Created a directory')):
                spec.loader.exec_module(module)

    def test_deadline_embedded_program_compiles_without_execution(self):
        tree = ast.parse(Path(__file__).with_name('test_deadline.py').read_text())
        programs = [node.value.value for node in ast.walk(tree) if isinstance(node, ast.Assign)
                    and any(isinstance(target, ast.Name) and target.id == 'program' for target in node.targets)]
        self.assertEqual(len(programs), 1)
        compile(programs[0], '<deadline-fixture-compile-only>', 'exec')


if __name__ == '__main__':
    unittest.main()
