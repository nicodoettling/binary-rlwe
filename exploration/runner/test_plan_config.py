"""Pure tests: no model calls, service access, preflight, or background launch."""
import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

path = Path(__file__).with_name('bounded_run.py')
spec = importlib.util.spec_from_file_location('bounded_run', path)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class PlanConfigurationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        # Authorization in historical plans can legitimately change after launch.
        # Test the gate against an isolated, explicitly unconfirmed fixture.
        for relative in ('exploration', 'exploration/joint-ideal'):
            source = runner.ROOT / relative
            target = root / relative
            target.mkdir(parents=True, exist_ok=True)
            for name in ('PLAN.md', 'COORDINATOR_PROMPT.md', 'TASK_TEMPLATE.md'):
                (target / name).write_text((source / name).read_text())
            config = json.loads((source / 'run-config.json').read_text())
            config['launch_authorized'] = False
            (target / 'run-config.json').write_text(json.dumps(config))
        patcher = mock.patch.object(runner, 'ROOT', root)
        patcher.start()
        self.addCleanup(patcher.stop)

    def args(self, **overrides):
        values = dict(plan_dir=str(runner.ROOT / 'exploration/joint-ideal'),
                      run_id='test-not-launched', seconds=None,
                      smoke=None, validate_only=False)
        values.update(overrides)
        return argparse.Namespace(**values)

    def test_five_hour_configuration(self):
        _, config = runner.load_plan(self.args())
        self.assertEqual(config['max_wall_seconds'], 18000)
        self.assertEqual(config['phase_boundaries_seconds']['hard_stop'], 18000)
        self.assertFalse(config['launch_authorized'])
        self.assertEqual(config['run_kind'], 'finite_joint_ideal_investigation')

    def test_unconfirmed_launch_has_no_launch_side_effects(self):
        with mock.patch.object(Path, 'mkdir', side_effect=AssertionError('created directory')):
            with mock.patch.object(runner.subprocess, 'run', side_effect=AssertionError('ran process')):
                with self.assertRaisesRegex(RuntimeError, 'confirmation has not been recorded'):
                    runner.launch(self.args())

    def test_validation_never_launches(self):
        with mock.patch.object(Path, 'mkdir', side_effect=AssertionError('created directory')):
            with mock.patch.object(runner.subprocess, 'run', side_effect=AssertionError('ran process')):
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    self.assertEqual(runner.launch(self.args(validate_only=True)), 0)
                result = json.loads(out.getvalue())
                self.assertFalse(result['creates_run'])
                self.assertLessEqual(result['systemd_runtime_seconds'] +
                                     result['systemd_stop_grace_seconds'], 18000)

    def test_internal_entry_points_also_require_confirmation(self):
        config_path = runner.ROOT / 'exploration/joint-ideal/run-config.json'
        with mock.patch.object(runner, 'write_json', side_effect=AssertionError('wrote manifest')):
            with mock.patch.object(runner.subprocess, 'run', side_effect=AssertionError('ran process')):
                with mock.patch.object(runner.os, 'execv', side_effect=AssertionError('started Codex')):
                    for function in (runner.entry, runner.service):
                        with self.subTest(function=function.__name__):
                            with self.assertRaisesRegex(RuntimeError, 'confirmation has not been recorded'):
                                function(str(config_path))

    def test_execution_requires_verified_finite_deadline(self):
        for overrides in ({'deadline_supervisor_verified': False},
                          {'max_wall_seconds': 0}, {'max_wall_seconds': 21601}):
            config = dict(launch_authorized=True, deadline_supervisor_verified=True,
                          max_wall_seconds=18000, **{})
            config.update(overrides)
            with self.assertRaises(RuntimeError):
                runner.require_execution_config(config)

    def test_rescale_uses_selected_plan_duration(self):
        _, config = runner.load_plan(self.args(seconds=14400))
        self.assertEqual(config['phase_boundaries_seconds']['setup_end'], 720)
        self.assertEqual(config['phase_boundaries_seconds']['hard_stop'], 14400)

    def test_cannot_extend_plan(self):
        with self.assertRaises(ValueError):
            runner.load_plan(self.args(seconds=18001))

    def test_reject_path_escape(self):
        with self.assertRaises(ValueError):
            runner.load_plan(self.args(run_id='../unrelated'))

    def test_original_plan_still_validates(self):
        _, config = runner.load_plan(self.args(plan_dir=str(runner.ROOT / 'exploration')))
        self.assertEqual(config['max_wall_seconds'], 21600)
        self.assertEqual(config['phase_boundaries_seconds']['hard_stop'], 21600)

    def test_scope_file_must_stay_in_plan(self):
        path = runner.ROOT / 'exploration/joint-ideal/run-config.json'
        config = json.loads(path.read_text())
        config['research_scope_file'] = '../PLAN.md'
        path.write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, 'inside the plan'):
            runner.load_plan(self.args())

    def test_scope_file_and_monitoring_defaults(self):
        path = runner.ROOT / 'exploration/joint-ideal/run-config.json'
        config = json.loads(path.read_text())
        config['research_scope_file'] = 'RESEARCH_SCOPE.md'
        path.write_text(json.dumps(config))
        path.with_name('RESEARCH_SCOPE.md').write_text('Theoretical research scope.\n')
        _, config = runner.load_plan(self.args())
        self.assertEqual(config['snapshot_interval_seconds'], 300)
        self.assertEqual(config['coordinator_checkpoint_stale_seconds'], 600)


if __name__ == '__main__':
    unittest.main()
