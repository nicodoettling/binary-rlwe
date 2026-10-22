# OPERATIONS-AUDIT1 — documentary operational audit

The observed configuration and history support one native goal, an unchanged five-hour service clock, the three-agent ceiling, and continued nonterminal work through the protected interval. FF remains open, the source diagnostic concerns the inherited radius, and no hardness foundation or scientific exhaustion is established. This is an operational evidence audit, not mathematical acceptance or a final shutdown certificate.

The principal snapshot was taken at **2026-10-21T21:53:49.048436+00:00**. Supplementary configuration/resource evidence was read at 21:57:37 UTC; the final input manifest binds the coordinator's 21:58:46 runtime refresh and checkpoint 025. All findings refer to those saved bytes. Future delivery, usage and shutdown receipts are **pending, not overdue** at this audit.

## Findings requiring exact reporting

| ID | Finding | Disposition |
|---|---|---|
| OA-01 | Ten-minute recording cadence was approximate, not exact. Checkpoint 019 was 251.526828 seconds late; the largest adjacent interval was 819.512951 seconds. Checkpoints 023 and 024 were 1.969241 and 10.248407 seconds early. | Historical cadence deviation. Preserve actual times and disclose it; do not backdate or call the cadence exact. No clock reset is indicated. |
| OA-02 | `reviews/BLIND-SV1/experiment-01-execution.json` explicitly says peak memory was not separately measured. Its script enforces 512 MiB address space, 115 CPU seconds and a 120-second alarm; its internal elapsed time is 19.156426609 seconds. | Historical evidence gap against the request to preserve per-job peak memory. The address-space limit is not a measured peak. No rerun is needed merely to replace a missing historical measurement. |
| OA-03 | `SYM-RANK-FV2` has registry `wall_seconds=26.47`, matching script-internal `seconds=26.469174596946687`, while its GNU-time resource file records total wall `0:26.69`. | Small measurement-scope ambiguity. Label the first as script time or use 26.69 seconds for process wall time. Neither value approaches the limit. |
| OA-04 | The 21:39:02 `experiments/evidence-index-v1.json` has one changed path among 354 indexed artifacts: `reviews/BLIND-RESOURCE3/complete-report.md`, 37486 to 37687 bytes, hash `17edcf23aa62b7186d68338e6e8a750444fe72366975afcea058a99ad7b86b7f` to `774e5020cc3593ce2e8dab4adc208d6400b6e4ffc7dece8635f53a40a6b0a2c8`. All 354 paths exist. | Expected working-index staleness before that review's final seal. Coordinator acknowledged it and will preserve v1 while creating a new final index after all audit seals. Do not present v1 as a current exact index. |
| OA-05 | The first runtime snapshot's top-level `latest_actual_spawn_receipts` pointed to v2 despite a v5 metadata refresh. | **Resolved in observed bytes:** runtime verification at 21:58:46.673190 UTC points to `spawn-receipts-all-v6.json`. That file has 19 spawn attempts plus one separate failed-message receipt, and metadata for 18 threads including root. Historical completed threads are not concurrent workers. |
| OA-06 | The cap-status file's `updated_at` remains 17:48:10.733979 UTC. Its `state=running` and service properties are launch-time observations. | Evidence limitation, not a deadline violation. A later worker-status heartbeat shows activity, but neither record certifies future shutdown or absence of experiments. Final cleanup must distinguish actual observations from scheduled signals and cached state. |
| OA-07 | This auditor's supplementary extractor initially printed five short encrypted assignment prefixes by treating stored tool message arguments as plaintext. | Auditor process lapse, immediately disclosed to the coordinator. Prefixes were removed from persisted metadata and the script corrected to omit every message body. No decryption was attempted; the prior tool result cannot be withdrawn. `audit-extraction-lapse.json` preserves the limitation without retaining ciphertext. This is not a finding about mathematical correctness or billing. |

The first commentary imprecisely attributed the index change to the registry; a subsequent commentary corrected it to the BLIND-RESOURCE3 report. The exact saved hash comparison above controls.

## Goal and honest terminal status

Selected actual root and child session records contain exactly **one** `tools.create_goal` call, at 17:48:48.580 UTC. Its call has no `token_budget` field. No `update_goal` call was observed in the sampled history, and no child goal creation or child spawn call was observed. The saved initial receipt is null; the creation receipt starts at zero tokens/time; all checkpoint receipts preserve the same root thread and creation epoch, remain active, and have nondecreasing native counters.

At checkpoint 024 the native counters are 5,048,537 tokens and 14,332 seconds. Checkpoint 025 subsequently records 5,352,964 tokens and remains active. These are native goal counters, not weekly-quota, price, cost or backend billing measurements. `native-usage-delta.json` is still a 210-minute snapshot; it is not the final counter receipt. Native goal creation is about 38 seconds after service activation, so native time and service elapsed time must not be silently identified.

The 45-, 90-, 150- and 210-minute records all reject scientific termination. Their programme decisions record redirected alternatives after scoped failures. The fresh nonauthor `frontier-challenge-report-v1.md` explicitly rejects scientific exhaustion and FF completion, and the coordinator's replies agree. The currently documented open routes prevent an exhaustion or positive-achievement certificate on the existing record. A completed bounded report must leave the mathematical objective unresolved; cap expiry is a separate operational end. No terminal certificate is missing merely because none is justified.

This audit accepts the separation of FF, inherited-radius source diagnosis and hardness as reporting discipline. It does not re-prove or re-certify the source theorems, the mathematical challenge, or the full/blind dependency graph. The separate delivery auditor handles those exact mathematical dependencies. The coordinator reported acceptance-v7 during this audit; that is not mathematical acceptance by OPERATIONS-AUDIT1.

## Clock and schedule evidence

Activation is consistently **17:48:10.636448 UTC**, monotonic **699808.034735**. The launcher, cap and deadline record use the same origin. Across saved checkpoints 000–024 the largest difference between UTC-derived and recorded monotonic elapsed time is 0.052199 seconds, at startup. There is no detected reset, relabelled origin or five-hour extension.

| Gate | Scheduled UTC | Actual recorded UTC | Delay |
|---|---|---|---:|
| 45 minutes | 18:33:10.636448 | 18:33:18.441902 | 7.805454 s |
| 90 minutes | 19:18:10.636448 | 19:18:50.761976 | 40.125528 s |
| 150 minutes | 20:18:10.636448 | 20:19:42.431138 | 91.794690 s |
| Protected end / discovery cutoff | 21:18:10.636448 | 21:18:45.061895 | 34.425447 s |
| Checkpoint 025 | 21:58:10.636448 | 21:58:22.473661 | 11.837213 s |

Checkpoints 000–025 are present. The full 000–024 timing table is in `clock-and-goal-checks.json`; checkpoint 025's original bytes are in `final-inputs`. The 190-minute record acknowledges compaction/continuation lateness. Evidence of substantive protected activity is documentary/cooperative; this audit makes no claim that an OS mechanism enforced productive research.

Post-cutoff actual assignment metadata identifies BLIND-RESOURCE3, the compact-v3 challenge addendum, BLIND-RESOURCE4, DELIVERY-AUDIT1 and this operations audit. Their preserved plaintext assignment files limit them to review, targeted repairs or audit. Programme/checkpoint records likewise switch to review and repair. No new discovery assignment was identified. This is a scoped documentary conclusion, not continuous surveillance of every thought or process.

The still-future binding times are consolidation at **22:18:10.636448 UTC**, workers/experiments stopped by **22:33:10.636448**, final checkpoint by **22:43:10.636448**, graceful shutdown scheduled **22:47:05.636448**, scheduled kill **22:48:05.636448**, hard deadline **22:48:10.636448**. The service configuration has RuntimeMax 17,935 seconds, 60 seconds stop grace, a five-second scheduling reserve, control-group kill and no restart. Those parameters sum to the original 18,000-second cap. They are configuration evidence, not evidence that a future signal or cleanup has already occurred. The final three shutdown times are 00:47:05, 00:48:05 and 00:48:10 Berlin time on 22 October.

## Agent/model/tier evidence

The launcher explicitly requests `gpt-6-astra`, `model_reasoning_effort="ultra"`, `service_tier="default"`, sandbox `workspace-write`, approval `never`, and at most two spawned threads. The argv also contains `features.fast_mode=true`; that literal feature flag must not be hidden. The selected service-tier argument is nevertheless `default`; this audit does not infer price or request routing from a feature flag.

At the primary snapshot, all observed turn configurations across 18 root/child sessions report Astra, ultra and never. The actual spawn calls request the same model/effort and fresh context; their schema has no service-tier field. Two fresh-spawn requests failed at the thread limit, and a later message attempt also failed; those errors were preserved rather than bypassed by another CLI/session.

An independent lifecycle reconstruction from selected child `task_started`, `task_complete` and `turn_aborted` metadata found a maximum of **two active children**, with no unmatched repeated start anomaly. At that snapshot the children were DELIVERY-AUDIT1 and OPERATIONS-AUDIT1. This is stronger than counting cumulative child files, but remains local lifecycle evidence rather than a backend scheduler or process census.

Actual `thread_settings_applied` events provide explicit `service_tier="default"` in six root events and one event each for **ff1, sv, ff3_kernel, full_frontier1, full_source3 and delivery_audit1**. Those twelve events also report Astra/ultra/never. The selected records and source-prefix hashes are preserved in `selected-thread-settings.json` and `supplement-manifest.json`. Other child turn contexts lack a tier field; inheritance is the available evidence for those children. Neither local settings nor spawn receipts establish backend billing.

## Experiment resource evidence and limits of this audit

The root registry explicitly disclaims aggregate memory containment and sets 120 seconds default/300 seconds maximum, at most 16 GiB per job, two simultaneous jobs and one heavy job. Saved job registrations, timeout/`prlimit`/`RLIMIT_AS` configurations, output receipts and retained failures support bounded local jobs. In the 49 JSON registration records inspected, declared wall limits are 120 seconds and address-space limits are at most 2 GiB; supplementary Markdown registrations and execution receipts cover additional review/source jobs. This is a registration/artifact count, not an experiment count.

The saved timing artifacts include successful runs, the SV-FV3 timeout (120.03 seconds, exit 124), CRT-FV1 exit 1, and the FF3-LP-FV1 abort (signal 6, actual receipt exit 134). GNU time's `Exit status: 0` on that signal-terminated FF3 file must not be read as success; the separate receipt correctly says `ABORTED_NO_MATHEMATICAL_RESULT`. Failures and separately registered repairs remain visible. The largest peak RSS found in inspected timing records is **964,724 KiB** for FF3 n4 geometry FV12, beneath its 2 GiB address-space cap. This is one process/job peak, not an aggregate memory bound. OA-02 prevents a claim that every job has measured peak memory.

Some limits are enforced by the Python script itself rather than appearing in its outer command; for example BLIND-SV1 sets address/CPU limits and an alarm in code. This audit read that code only to verify the operational limit setup, without rerunning the mathematics. Exact preregistration chronology and simultaneous-job occupancy were not independently reconstructed for every job. Coordinator slot grants and saved execution records are evidence, not OS-enforced global two-job/one-heavy containment. No numerical experiment, solver, installation, service or detached job was launched by this auditor.

## Final delivery items still pending at the audit

At the delivery-presence snapshot, `claims.json`, reconciliation, regressions, reduction attempts, parameter table, source comparison, progress, resume and programme decisions exist. `final.md` is still absent while immutable drafts exist. This is normal before consolidation, and presence is not content approval.

Before the cap, the coordinator should bind a final evidence index after all audit seals, resolve or explicitly disclose OA-01 through OA-03, and preserve the final active-goal/native-counter receipt with its baseline/delta interpretation. It should record the workers/experiments stop and final checkpoint using actual times, and report only observed cleanup/process status. Cached cap state and future scheduled shutdown must remain labelled as such. Any inability to observe an enclosing process or the post-exit service must be stated instead of inventing an observation. These items are not certified by this pre-consolidation audit and are not late yet.

## Scope, exposure and seal

This auditor had full operational exposure, including programme summaries and existing status conclusions; it was not blind. Inputs include PLAN, launch/cap/deadline/configuration records, goal/checkpoint receipts, experiment inventories/limits/resources, selected actual session metadata, and the final challenge's status language. No author mathematical proof was reviewed for correctness. Copies and hashes are in the three input manifests; raw sessions, instructions, secret values and ciphertext are not retained in the final audit artifact set. The extraction lapse and two failed guessed-path reads are disclosed rather than treated as successful reads: the checkpoint directory is `coordinator/checkpoints`, and the challenge report's actual filename is `frontier-challenge-report-v1.md`.

No root or historical artifact was edited. Audit writes are confined to this directory. No agents, goals, Codex sessions, services, detached computations, installations, Git operations or external messages were created by this auditor. Coordinator collaboration messages are internal audit communication. No final process cleanup or backend billing observation is claimed. The exact seal binds this report, scripts, manifests, selected metadata, retained documentary inputs and the auditor-lapse record.
