# Launch receipt and monitoring

The user authorized immediate launch of this five-hour, four-agent Astra ultra native-goal run. Host and in-service sandbox preflights passed. Startup observations confirm `gpt-6-astra`, `ultra`, workspace-write and approval never. See [launch-receipt.json](launch-receipt.json) and [startup-service-check.json](startup-service-check.json).

| Event | Europe/Berlin | UTC |
| --- | --- | --- |
| Service start | 16 October 2026, 23:13:31 | 16 October, 21:13:31 |
| Wrap-up begins | 17 October 2026, 03:53:31 | 17 October, 01:53:31 |
| Five-hour deadline | 17 October 2026, 04:13:31 | 17 October, 02:13:31 |

Session: `brlwe-source-foundations-20261016-astra-ultra`.
Codex thread: `01a14690-1afb-7b03-a01d-09c842692662`.
Service: `codex-cap-brlwe-source-foundations-20261016-astra--72240bce8837.service`.

The requested and configured team is one coordinator plus three workers. Native goal creation is recorded in the output's goal-created.json; actual worker startup is separate runtime evidence. The generic launcher's agent-capacity field remains unverified by that helper even when subsequent direct evidence becomes available.

Verified service properties: RuntimeMaxSec=17935, TimeoutStopSec=60, scheduling reserve=5 seconds, KillMode=control-group, SendSIGKILL=yes, Restart=no. The supervisor and Codex child were both observed inside the exact service cgroup. The cap covers initialization, research, review and shutdown; achievement can end the goal earlier. It is a local monotonic runtime cap, not an exact billing cutoff or aggregate memory limit. No token budget or automatic service restart was requested.

Read live status without launching work:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v2/capped_codex_tmux.py status --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-source-foundations-20261016-astra-ultra/launcher-run.json --tail 0
```

Attach to the durable tmux session:

```sh
tmux attach-session -t brlwe-source-foundations-20261016-astra-ultra
```

The run manifest preserves the exact command, helper and prompt hashes, initial worktree state and concurrency overrides. The cap sidecar is runtime authority. Scientific checkpoints, native goal status and process health are distinct records. Root HANDOFF.md still contains an older startup snapshot; use the current launch receipts and run artifacts instead.
