This launcher runs finite exploration through the installed codex-tmux-runner helper and a run-owned systemd user service. It does not use goal tools, automatic resumes, recurring tasks, or external notifications.

The actual Codex command remains sandbox-only: `--sandbox workspace-write -c approval_policy="never"`. All research agents use `gpt-6-astra` with `ultra` reasoning. The installed helper retains its Bubblewrap, tmux group, CLI option, startup banner, process and heartbeat checks. Launch requires the selected plan's applicable authorization and verified finite deadline; configuration validation never records authorization.

The service retains `RuntimeMaxSec=max_wall_seconds-10`, `TimeoutStopSec=5`, `KillSignal=SIGINT`, `KillMode=control-group`, `SendSIGKILL=yes`, and `Restart=no`. Its timer starts before initialization, survives the monitor/client, and covers research descendants. Neither snapshots nor monitoring extend the research service's deadline. Finishing local bookkeeping can take a few seconds after the service stops. Remote execution environments and independent worker services remain forbidden.

Launch from a host context with the user's tmux server and systemd bus, after the plan's launch is authorized:

```sh
python3 exploration/runner/bounded_run.py --plan-dir exploration/joint-ideal-next --run-id UNIQUE_RUN_NAME
```

Use a new run name each time. Existing runs, logs, and snapshots are preserved. `--plan-dir` selects a prepared in-project directory with `PLAN.md`, `COORDINATOR_PROMPT.md`, `TASK_TEMPLATE.md`, and `run-config.json`. Optional `research_scope_file` must resolve to a readable file inside that directory; its entire text is included verbatim in the generated coordinator prompt. The plan must require that full scope in worker assignments too.

`--seconds` may shorten the selected plan's maximum and rescales its phases; it cannot extend the maximum. Validate a plan without preflight, files, service access, or model calls:

```sh
python3 exploration/runner/bounded_run.py --plan-dir exploration/joint-ideal-next --run-id PENDING --validate-only
```

During an authorized run, `_service` is an ordinary Python supervisor outside the timed research service. It polls the service, reads newly persisted session events and log lines, publishes a heartbeat, and preserves artifacts. These operations do not require model participation. The default configuration is:

| Plan configuration | Default | Purpose |
| --- | ---: | --- |
| `monitor_poll_seconds` | 5 | Observe errors and service state |
| `snapshot_interval_seconds` | 300 | Preserve a filesystem artifact snapshot |
| `coordinator_checkpoint_stale_seconds` | 600 | Warn that changed coordinator documents are overdue |

Each value must be an integer from 1 to 3600, with polling at least as frequent as the other intervals. Snapshots follow the scheduled cadence, with missed intervals coalesced; they are also attempted on startup and exit. Detection latency is the polling interval plus log persistence, service-query, and filesystem work. It is not an instantaneous notification guarantee.

Structured current-session error events distinguish `cyber_policy`, `permission_denial`, `timeout`, and `ordinary_failure`. Supported records include `event_msg/error`, `event_msg/task_complete.error`, and `turn.failed`; the previous run's actual `task_complete.error.codex_error_info=cyber_policy` shape is covered by a fixture. The supervisor watches the coordinator UUID from `tmux-status.json` and explicit `session_id`, `codex_session_id`, or `thread_id` UUIDs in `agents.json`. Worker names such as `/root/reviewer` are not session UUIDs; worker sessions not identified there are outside this observation scope.

A confirmed structured `cyber_policy` event stops only this run's service and records `stop_reason`. The runner does not rephrase, retry, resume, or weaken permissions. Plain `ERROR: ` log lines produce an `unconfirmed_log_error` notice and candidate classification: tool output can quote old errors, so text alone never confirms a policy failure or triggers the policy-stop path. A systemd `Result=timeout` supplies independent timeout evidence. Error events and overall process exit are recorded separately, since a tool error can occur during a run that later exits normally.

Every notice is written atomically to `alerts/` and printed to stderr, which the tmux helper records in its transcript. The current observations are in `monitor-status.json`. These are local notices: they do not send a chat message when the conversation is closed, email anyone, or contact an external service. Inspect them with the read-only command:

```sh
python3 exploration/runner/bounded_run.py status --run-file /absolute/path/to/run/run.json
```

The status command reports persisted evidence and whether the monitor heartbeat is stale. It does not query live processes or certify current service health. Use the installed helper's emitted status command and `systemctl --user show RUN_NAME.service` for live process/service evidence. Stop only this run with `systemctl --user stop RUN_NAME.service`; do not stop a shared tmux server or unrelated Codex daemon.

The coordinator must update `claims.json`, `reconciliation.md`, `progress.md`, `final.md`, and `agents.json` every five minutes and after every worker result, then publish a checkpoint:

```sh
python3 exploration/runner/bounded_run.py checkpoint \
  --run-file /absolute/path/to/run/run.json \
  --reason 'Recorded the review result, open objections, and next steps'
```

The checkpoint helper requires a running manifest, all five nonempty artifacts, and syntactically valid JSON. It preserves the supplied files in `coordinator-checkpoints/`, then atomically updates `coordinator-checkpoint.json`. Updating only the agent registry or repeating the helper with unchanged documents does not reset the content-change timestamp. A stale warning therefore cannot be cleared merely by a periodic filesystem copy. Changed text is an observable checkpoint signal, not proof of meaningful mathematical progress; the coordinator remains responsible for its content.

Periodic and exit captures go into `runner-snapshots/`. Each published directory contains copied artifact bytes and an atomic manifest with SHA-256 hashes. A stable file set is checked before and after copying; detected concurrent edits cause bounded retries and then a durable warning. Staging directories remain unpublished and are cleaned up on handled failures; earlier snapshots are preserved. Files and directories are fsynced before publication. This supplies an internally hash-consistent copy of a filesystem state, not a transaction across the coordinator's scientific reasoning. Workers and the coordinator should publish completed documents atomically and avoid updating the core checkpoint documents during the checkpoint command.

Captures exclude logs, hidden paths, runner metadata, and the two capture stores; research-created `snapshots/` directories remain included. Symlink/special-file artifacts and captures above 256 MiB fail explicitly rather than being followed or silently omitted. There is no deletion/rotation of previous snapshots. A failed capture retains the last successful snapshot and reports the failure; available disk space limits durability.

Every handled service exit, startup exception, SIGINT, SIGTERM, or SIGHUP attempts a final capture and writes `exit-manifest.json` plus `artifact-index.json`. The finalizer preserves partial reports and reconciliation exactly as found, lists missing core artifacts and unfinished agents as recorded, and never writes mathematical conclusions. If the final capture fails, the manifest explicitly identifies its fallback to an earlier snapshot. `run.json` and `deadline-status.json` also receive the execution outcome.

`process_success` requires exit code zero and observed inactive/success service state. `scientific_completeness` always remains `not_verified_by_runner`. The presence of a reconciliation file means only `present_unverified`; it does not establish that all objections were resolved. `service_inactive_observed` records the service state; descendant shutdown is explicitly not independently verified by this finalizer. Missing service evidence yields an unverified outcome. The generic tmux helper can still report failure for an expected forced timeout; consult the deadline and exit manifests.

A hard kill of the supervisor, host loss, full/unwritable disk, or filesystem failure can prevent finalization. The independent research deadline still applies if systemd remains available, and prior snapshots remain the recovery basis. The log reader processes bounded chunks, skips oversized records with an `observation_gap` notice, and may lag behind very large bursts. The watcher cannot prevent upstream screening, certify why screening occurred, guarantee model-generated checkpoints, or certify a mathematical result.

Pure local verification is safe to discover and does not launch a model, tmux, service, or external notification:

```sh
python3 -m unittest discover -s exploration/runner -v
```

The tests cover real-format structured error fixtures, quoted historical errors, exact-session selection, partial/rotated logs, policy-stop scope, timeout and signal finalization with fake processes/systemctl, immutable hash manifests, interrupted captures, stale checkpoint behavior, malformed agent metadata, authorization gates, and preserved timer properties. `test_deadline.py` is an explicitly invoked integration script guarded by `__main__`; importing it during unit discovery has no service side effects.

Historical live deadline and managed-agent evidence remains in `verification/`. It predates this monitoring implementation and is not a live integration test of the new watcher. No new model or service run was used to verify these changes. The earlier architecture investigation used the official [Codex exec implementation](https://github.com/openai/codex/blob/main/codex-rs/exec/src/lib.rs) and [in-process app server](https://github.com/openai/codex/blob/main/codex-rs/app-server/src/in_process.rs), plus installed CLI 0.153.0 and the historical managed smoke.
