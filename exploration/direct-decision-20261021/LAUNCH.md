# Direct decision binary RLWE: launch receipt

User-authorized new four-hour native-goal run, three total agents, Astra ultra, explicit Standard service. Startup process and external time cap verified; worker startup is recorded separately. Configuration evidence is not backend billing telemetry.

| Phase, 21 October 2026 | Europe/Berlin | UTC |
| --- | --- | --- |
| start | 14:19:00 CEST | 12:19:00 UTC |
| nonterminal_gate | 15:04:00 CEST | 13:04:00 UTC |
| review_start | 17:04:00 CEST | 15:04:00 UTC |
| delivery_start | 17:54:00 CEST | 15:54:00 UTC |
| workers_stop | 18:04:00 CEST | 16:04:00 UTC |
| final_checkpoint | 18:14:00 CEST | 16:14:00 UTC |
| hard_deadline | 18:19:00 CEST | 16:19:00 UTC |

Session: `01a15e66-88ee-7da3-b484-747bf9751c67`.

Tmux: `brlwe-direct-decision-20261021-astra-ultra`.

Service: `codex-cap-brlwe-direct-decision-20261021-astra-ult-dacbe2c5899c.service`.

Monitor:

```bash
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/v3/capped_codex_tmux.py status --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-direct-decision-20261021-astra-ultra/launcher-run.json --tail 0
```

See [plan](PLAN.md), [configuration](launch-config.json), [host verification](host-runtime-verification.json), and live output sidecars. The 45-minute checkpoint is nonterminal. The clock and cap are immutable; no automatic successor is authorized.

Native goal active; coordinator reports three total slots and successful DD1/DD2 worker starts, both Astra ultra with fresh context. See [team startup verification](team-startup-verification.json).
