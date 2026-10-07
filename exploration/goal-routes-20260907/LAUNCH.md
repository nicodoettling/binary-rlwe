# Launch contract — approved three-hour run

The user approved this package with a revised three-hour maximum. No native goal or research service was started during the design phase; actual launch evidence will be saved separately. `run-config.json` is a declarative planning record, not input consumed by the capped helper.

The actual user approval and timestamp are recorded in run-config.json. Verify a fresh session name and unused output path, preserve the initial Git state and skill/helper versions, and create the designated new output directory. If the name is already in use, choose a fresh name and update every corresponding prompt/config path before launch; do not append to a different run.

Use the installed updated helper with the exact options below. Use the approved integer duration `180m` (10,800 seconds), reduced from the original 210-minute proposal.

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/capped_codex_tmux.py launch \
  --root /home/nico/projects/research_projects/binaryRLWE \
  --session brlwe-goal-routes-20260907-astra-ultra \
  --prompt /home/nico/projects/research_projects/binaryRLWE/exploration/goal-routes-20260907/COORDINATOR_PROMPT.md \
  --log /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra/run.log \
  --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra/launcher-run.json \
  --status-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra/worker-status.json \
  --codex /home/nico/.local/bin/codex \
  --permission-profile sandbox-only \
  --model gpt-6-astra --reasoning-effort ultra --search \
  --max-runtime 180m --wrapup-before 20m \
  --stop-grace-seconds 60 --scheduling-reserve-seconds 5 \
  --startup-timeout 20
```

There is no CLI goal or agent-count flag. The prompt instructs the coordinator to verify native goal support and create one goal, without a token budget, and limits active concurrency to four including itself. The latest user request permits native goal continuations during the live capped service; it does not authorize automatic service resumes after termination.

The helper's actual host preflights are mandatory at launch: CLI options, sandbox no-op, Bubblewrap/group inheritance, cgroup v2, user-systemd availability, and repeated in-service sandbox preflight. Do not weaken the sandbox or silently fall back to an uncapped run if they fail. `--dry-run` performs real host prerequisites, so it was not run as a documentation check.

## Expected envelope and immediate verification

From service activation, before inner sandbox/model startup:

| Event | Offset |
|---|---:|
| Scientific wrap-up begins | 2:40:00 |
| Cooperative workers/experiments stopped | 2:55:00 |
| SIGTERM initiation | 2:58:55 |
| Scheduled forced cleanup | 2:59:55 |
| Requested cap envelope | 3:00:00 |

Use actual timestamps from `launcher-run.json` and its `cap.status_file`, not the planning table, as runtime authority. The cap is a local monotonic runtime limit with scheduling reserve, not a hard real-time or billing cutoff; it cannot retract remote requests already accepted.

Immediately run:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/capped_codex_tmux.py status \
  --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra/launcher-run.json \
  --tail 0
```

Verify the observed model and effort, workspace-write plus approval `never`, live process and fresh heartbeat, named service and expected cgroup membership, RuntimeMaxSec/TimeoutStopSec, KillMode=control-group, SendSIGKILL=yes, and Restart=no. Save the startup evidence. Check that the native goal was actually created; unavailable goal tools must produce a configuration-error checkpoint instead of a silent finite-run substitute.

The cap sidecar's terminal result takes precedence over an old worker status. Missing or inconsistent evidence means stale/unknown. The helper provides no `stop` subcommand: an authorized early host stop uses `systemctl --user stop` with only the exact validated `manifest.cap.service`, followed by capped status. Never kill unrelated services or a shared tmux server.

## Preservation limits

Keep the manifest, original log, worker status, cap sidecar, prompt/helper hashes, scientific checkpoints and referee records. Use the existing pure snapshot function as specified in COORDINATOR_PROMPT.md, not the legacy manifest-dependent launcher/checkpoint interface.

The installed capped helper supplies heartbeat, descendant containment and terminal cap status. It does not supply the old project's continuous structured-policy observer, five-minute autonomous filesystem capture, or stale-content alerts. This design uses explicit cooperative scientific checkpoints and their immutable snapshots; it does not claim those additional monitors are installed for this new run.

The expired run cannot restart itself. A future exact-session resume needs new user approval, a fresh duration and sidecars, and confirmation that the old service/cgroup is stopped. Timeout neither completes nor pauses an unresolved native goal.
