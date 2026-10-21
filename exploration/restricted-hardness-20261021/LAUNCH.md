# Launch and monitoring: restricted ideal hardness, 21 October 2026

User-authorized three-hour continuation of native goal thread `01a14b7b-9e45-7b70-b46d-0bf70e17f2e2`. Three total agents, Astra ultra, Standard service tier. Root actual argv and external time enforcement passed the host startup check in `host-runtime-verification.json`; worker startup verification is recorded separately. No backend billing telemetry is inferred.

| Phase | Europe/Berlin | UTC |
|---|---|---|
| start | 2026-10-21 07:34:44 CEST | 05:34:44 UTC |
| decision | 2026-10-21 08:19:44 CEST | 06:19:44 UTC |
| review_start | 2026-10-21 09:49:44 CEST | 07:49:44 UTC |
| workers_stop | 2026-10-21 10:19:44 CEST | 08:19:44 UTC |
| final_checkpoint | 2026-10-21 10:29:44 CEST | 08:29:44 UTC |
| graceful_shutdown | 2026-10-21 10:33:39 CEST | 08:33:39 UTC |
| hard_deadline | 2026-10-21 10:34:44 CEST | 08:34:44 UTC |

Tmux: `brlwe-restricted-hardness-20261021-astra-ultra`.
Service: `codex-cap-brlwe-restricted-hardness-20261021-astra-05b9ab067e48.service`.

Monitor:

```bash
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v3/capped_codex_tmux.py status --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/launcher-run.json --tail 0
```

The manifest, heartbeat and cap sidecar under the output directory are authoritative for current process state. This document is a startup receipt. The previous service was verified inactive with no live descendants before resume. No restart, extension, new native goal or automatic successor is authorized.

Actual coordinator and both workers were observed running at 2026-10-21T05:39:44.985226+00:00. The runtime advertised three total slots. Both worker spawn requests specified Astra ultra with fresh context. See `team-startup-verification.json` and the source runtime receipt.
