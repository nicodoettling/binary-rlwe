# Launch record and monitoring

## Current continuation: Standard speed and three agents

On 18 October 2026 (Berlin), the user requested a restart at Standard speed and **three agents total**. The foreground checkpointed the research, stopped the preceding service, verified its cgroup was empty, and resumed the same native goal thread. Astra ultra reasoning and sandbox-only permissions are unchanged. A run-local wrapper explicitly passes `service_tier="default"`; the actual host process arguments confirm this override and the two-worker ceiling. This is verified client configuration, not a claim to have inspected backend billing telemetry. No user-wide configuration was edited.

The new service started at **00:39:22 Berlin**. Discovery stops at **03:36:14 Berlin** and the hard deadline is **04:06:14 Berlin on 18 October**, within the previously authorized envelope. The research clock was not reset. The previous two-agent records below are historical.

- Current tmux: `brlwe-standard-hardness-20261017-standard3`.
- Current service: `codex-cap-brlwe-standard-hardness-20261017-standar-fd6a991cdd92.service`.
- Current manifest: `../runs/brlwe-standard-hardness-20261017-astra-ultra/standard3-launcher-run.json`.
- [Launch command](standard3-resume-command.json), [runtime verification](standard3-resume-verification.json), and [speed wrapper](codex-standard-speed.sh).

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py status --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/standard3-launcher-run.json --tail 0
```

Attach with `tmux attach-session -t brlwe-standard-hardness-20261017-standard3`.

At 00:42:30 Berlin, actual collaboration evidence showed all three agents running: the coordinator, `bt13_blind`, and `e_fractional`. Both worker starts explicitly selected Astra ultra with fresh histories. The coordinator acknowledged three available slots and the unchanged active native goal. Exact receipts are recorded in the runtime verification linked above.

## Earlier continuation: two agents after user-requested throttle (historical)

On 17 October 2026, the user reduced the active team to **two agents total**, retaining Astra ultra. File-based steering did not receive a timely acknowledgment, so the foreground saved a checkpoint, stopped the original service, verified it was no longer running, and resumed the **same native goal thread** with two runtime slots. The coordinator acknowledged the new ceiling and observed no inherited live workers. The goal remains active and unfinished; research and review now proceed with at most one worker alongside the coordinator. The original launch record below is historical.

The resumed service started at **22:08:21 UTC on 17 October** (00:08:21 Berlin on 18 October). Discovery stops at **01:37:14 UTC on 18 October**; the hard deadline is **02:07:14 UTC / 04:07:14 Berlin**, two minutes earlier than the original cap. No fresh six-hour window or token budget was created. The old service's interrupted status records this deliberate operational change, not a policy interruption or a scientific result.

- Current tmux: `brlwe-standard-hardness-20261017-throttle2`.
- Current service: `codex-cap-brlwe-standard-hardness-20261017-throttl-a1f12347731a.service`.
- Current manifest: `../runs/brlwe-standard-hardness-20261017-astra-ultra/throttle-resume-launcher-run.json`.
- [Applied throttle receipt](throttle-two-agents-receipt.json) and [host/runtime verification](throttle-resume-verification.json).
- [Coordinator acknowledgment](../runs/brlwe-standard-hardness-20261017-astra-ultra/foreground-inputs/throttle-two-agents-ack.md).

Check current status:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py status --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/throttle-resume-launcher-run.json --tail 0
```

Attach with `tmux attach-session -t brlwe-standard-hardness-20261017-throttle2`. Lower concurrency reduces simultaneous model work; no exact weekly-quota saving has been measured or guaranteed. Raw native-goal token counts are not account-wide quota accounting.

## Original launch (historical)

Immediate launch was authorized by the user for six hours and five agents total. Astra ultra retains the explicit model preference from the preceding research runs. The installed v2 helper passed host and in-service sandbox preflight, created a dedicated capped user service, and observed a live Codex process with a fresh heartbeat. [Launch receipt](launch-receipt.json) records the actual settings, containment and timestamps.

| Event | Europe/Berlin | UTC |
| --- | --- | --- |
| Service start | 17 October 2026, 22:09:14 | 17 October, 20:09:14 |
| Wrap-up begins | 18 October 2026, 03:39:14 | 18 October, 01:39:14 |
| Six-hour deadline | 18 October 2026, 04:09:14 | 18 October, 02:09:14 |

- tmux session: `brlwe-standard-hardness-20261017-astra-ultra`
- Codex thread: `01a14b7b-9e45-7b70-b46d-0bf70e17f2e2`
- service: `codex-cap-brlwe-standard-hardness-20261017-astra-u-0d13c36f8a40.service`
- requested total: five, including the coordinator; configured spawned-worker ceiling: four.
- observed coordinator: `gpt-6-astra`, `ultra`, workspace-write, approval never.
- verified RuntimeMaxSec=21535, TimeoutStopSec=60, scheduling reserve=5 seconds, KillMode=control-group, SendSIGKILL=yes, Restart=no.

Both supervisor and Codex child were observed inside the expected service cgroup. The generic helper does not itself verify effective agent capacity; native goal and four useful worker starts were separately verified and recorded in [runtime-startup-verification.json](runtime-startup-verification.json). All five agents were observed running with Astra ultra assignments. A subsequent host status check confirmed the service and cap remained healthy. No token budget or automatic restart is authorized. The cap is local monotonic runtime enforcement, not an exact billing cutoff or aggregate memory cap. Initialization, research, reviews and shutdown share the same six-hour envelope.

Check live status:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py status --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/launcher-run.json --tail 0
```

Attach:

```sh
tmux attach-session -t brlwe-standard-hardness-20261017-astra-ultra
```

The run manifest preserves the exact command, permission profile, configuration overrides, prompt/helper hashes and initial Git state. The cap sidecar controls runtime status. Scientific progress, native goal completion and process cleanup remain distinct records. This run may finish early only if the computational-foundation goal and its review gates are actually satisfied; accepted auxiliary results alone do not satisfy it.
