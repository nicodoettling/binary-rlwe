# Binary-secret RLWE: capped native-goal coordinator

The user has approved this new four-agent Astra ultra goal run with a revised three-hour cap. **Execute this prompt only after launch-specific user approval is recorded in this package's `run-config.json`.** Earlier approvals in other plan directories do not authorize this run.

Project root: `/home/nico/projects/research_projects/binaryRLWE`.
Plan directory: `/home/nico/projects/research_projects/binaryRLWE/exploration/goal-routes-20260907`.
New output directory: `/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra`.
The capped launcher manifest is `launcher-run.json` in that output directory. Read its exact `cap.status_file` to find the authoritative cap sidecar. Do not infer deadlines from this filename or reset them from your first model response.

## Entry and native goal

Read `run-config.json`, `PLAN.md`, `RESEARCH_SCOPE.md`, and `TASK_TEMPLATE.md` in the plan directory. Verify the specific approval, output path, model, limits, and live cap evidence before research. Read the current versions of both skills and the required proof-audit references. This prompt and the user's new goal request supersede historical instructions that prohibited goal mode for earlier finite runs; do not run the legacy project launcher.

Verify that native goal tools are available. If not, save a configuration-error checkpoint and terminate; do not silently perform a non-goal substitute. Inspect existing goal state before creating exactly one coordinator goal. Do not overwrite a pre-existing unfinished goal. On a fresh service, create the exact `goal_objective` in run-config without `token_budget`; no token budget was requested. Save the returned goal identity and exact objective. Workers create no goals. On every continuation, read the goal, cap sidecar, saved ledger, and resume checkpoint before scheduling work.

The goal is to establish a new quantitatively meaningful hardness implication for coefficient-binary rank-one RLWE from an independently specified, motivated nonbinary source assumption. The search, algebra, and computational-transfer tracks in PLAN.md are candidate mechanisms, not established statements. Apply PLAN.md's endpoint rule: polynomial target modulus is preferred; a new fully checked asymptotic PPT-hardness result at a larger modulus with polynomial input bit length may achieve the goal in its explicitly limited scope. Fixed promised-advantage bounds, obstructions, and unresolved analytic-premise implications remain partial results. One- or two-sample results must not be called the original multiple-sample theorem. The user accepts that the capped run may fail to achieve the goal.

Initialize nonempty `final.md`, `resume.md`, `progress.md`, `claims.json`, `claim-history.jsonl`, `reconciliation.md`, `agents.json`, `regressions.json`, `parameter-table.md`, `source-comparison.md`, and `experiments/registry.json`. Record service start, wrap-up, shutdown and deadline UTC values, exact prior Git revision/worktree state, imported claim versions, and the new goal state. Write research only in the designated new output directory. Old literature, runs, plans, runner code, and Git history remain unchanged; do not commit, push, publish, install packages, or contact others during this run.

## Read-only scientific inputs

Read the root HANDOFF and discussion note for orientation, then treat current claims and reconciliations as authoritative over frozen author headers:

- Latest run `exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/`: `final.md`, `claims.json`, `reconciliation.md`, `dependencies.md`, `regressions.json`, `target.md`, `parameter-table.md`, `source-comparison.md`.
- Its `candidates/observable/statement-and-proof-v2.md`, `criticism/N02/review-v1.md`, and frozen W1/W2 notes with their N01/N03 reviews when used.
- `exploration/consolidated/joint-ideal-20260906/`: current consolidated report, ledger, reconciliation, and referenced corrections.
- The original PDFs and `literature/reading-notes-2026-09-05.md`; verify load-bearing imports in primary sources.

Import the complete historical regression records and provenance by reference/hash or frozen copy, including rejected probability statements. Preserve the distinction between W3-OBS coordinator v3 / author v2 and its stale historical header. Imported analytic statements remain provisional until their use is justified at the claimed level. Do not start by rewriting historical files or reproducing unrelated large experiments.

## Work and review

Follow the three tracks and latest phase boundaries in PLAN.md. You and at most three active workers form the entire team. Every new worker uses `gpt-6-astra`, `reasoning_effort=ultra`, and a fresh bounded assignment; use an appropriate non-full fork when setting explicit model overrides. No worker grandchildren. Recycle completed slots for fresh review; thread-capacity limits are handled by integration/local work, not by declaring success.

Paste the full academic scope from RESEARCH_SCOPE.md into every assignment and preserve its exact text. Include precise task, output ownership, absolute UTC deadlines, allowed sources, forbidden dependencies, and the required first falsification test. Keep statements, derived results, hypotheses, source claims, and finite experiments distinct. Each probabilistic lemma names all variables and their joint law, available versus latent information, conditioning and normalization, and every runtime/query/sample cost.

By elapsed 50 minutes, choose at most two candidates for detailed development based on actual proof attempts or counterexamples. Record why remaining routes are deferred and when they would be reopened. The search route deserves priority because it targets the original recovery task and may avoid the uniform-quotient step; this is a reason to investigate, not a desired verdict.

Begin criticism as statements stabilize. Before retaining a new theorem, obtain nonauthor reviews of the exact statement, proof, imported sources, constants, parameters, and complexity. Give at least one fresh blind referee only the frozen theorem, definitions, explicit hypotheses, and permitted sources, without the proof, status, coordinator assessment, or suspected flaw. Use `fork_turns="none"` for that blind referee so no prior proof context is inherited. Do not give that referee the general reading list if it would reveal the candidate argument. Freeze the complete blind report before revealing prior objections or proof bytes.

A flaw rejects the exact version and reopens all downstream claims. Save the counterexample before repairing. Repaired claims remain `REPAIRED-PENDING-RECHECK` until a fresh nonauthor checks the edited bytes against old regressions and a newly targeted search. Use exact finite probability models where feasible, including the cached-prefix regression if a sequential product or restored-independence claim arises. Final ACCEPTED requires the complete claim graph and applicable audit gates to close; a conditional implication may explicitly take an analytic statement as a premise, but that does not certify its instantiation or count as a completed hardness result if that premise remains the load-bearing gap.

Keep experiments within the PLAN limits. Save code and results before editing either; each correction gets a new version. Never reconstruct a missing original artifact as if it were contemporaneously preserved.

## Durability and cap behavior

Update the five core research files (`claims.json`, `reconciliation.md`, `progress.md`, `final.md`, `agents.json`) and `resume.md` at least every five minutes and after each material worker result. Workers save a useful partial note before long tools. Use temporary files and atomic replacement for complete versions. Maintain a short frontier: attempted mechanisms, the exact sticking point, new evidence, invalidated claims, and next tests.

For immutable core snapshots, the old module's standalone capture function is compatible without its legacy run manifest. Mirror the goal/session identity, deadlines, open claims and next-step frontier from `resume.md` into `progress.md` or `final.md` before capture: only the five legacy core files are included, not `resume.md` or the append-only claim history. Preserve those additional files durably in the run directory. After completing the core writes, execute the following with `python3 -B` from the project root and a truthful, specific reason:

```python
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from exploration.runner.resilience import snapshot, write_json
run_dir = Path("/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-goal-routes-20260907-astra-ultra")
capture = snapshot(run_dir, kind="capped-goal-coordinator", reason="REPLACE WITH THE ACTUAL UPDATE", core_only=True)
if capture["missing_core_artifacts"]:
    raise RuntimeError(capture["missing_core_artifacts"])
write_json(run_dir / "coordinator-checkpoint.json", {
    "created_at": capture["created_at"],
    "snapshot_directory": capture["directory"],
    "reason": capture["reason"],
    "scientific_progress_verified": False,
})
```

This uses only standalone snapshot/write functions; do not call `bounded_run.py checkpoint`, `resilience.checkpoint`, or the legacy Monitor with the new manifest. The bundled cap helper independently records process outcome but does not provide the old policy/staleness observer or guarantee mathematical checkpoint cadence. Record missing snapshots or late updates honestly.

Read the cap clock before every assignment and long tool. At the sidecar wrap-up time, stop new discovery and devote the remaining time to reconciliation, proportionate checks, final report, and resume checkpoint. By elapsed 175 minutes, finish or interrupt all workers and experiments and record their states. Do not launch any tool whose timeout reaches the graceful-shutdown boundary.

The cap applies to this whole service and its ordinary local descendants. Never start another service, tmux coordinator, detached external job, remote environment, or second clock. Use the tools' interrupt/cancel facilities for owned workers and experiments; the external helper owns service enforcement. No broad process killing or stopping a shared tmux server.

If the goal is actually achieved, verify the delivered artifacts against current accepted claims, record remaining scope exclusions, mark that goal complete, and finish early. A report, successful referee wave, improved candidate, scoped obstruction, or repeated old result is not by itself achievement. If the goal remains open, continue in-scope work until wrap-up. Do not mark it blocked merely because a proof is difficult, a thread limit is reached, or time expires; follow the actual tool's blocking rules if an external impediment persists.

At or after wrap-up, native continuations are limited to checkpoint, reconciliation, and shutdown work within the still-live cap. At an expired cap, do no research and do not restart. Leave unfinished goal state unfinished; the timer does not pause or complete a goal. Any future resume requires a new user decision and explicit new duration.

On a content-policy interruption, record the actual error if available, preserve existing work, stop further research and owned workers, and do not retry, rephrase, reroute, or restart. Do not confuse it with a tool-permission review rejection. The full research scope is context, not a promise of classifier behavior.

## Final deliverables

The final report begins with the strongest new claim or the absence of one. State exact source/target experiments, parameter and sample range, computational assumptions, finite losses, algorithm costs, review disposition, and the relationship to the original multi-sample search question. Preserve full proofs, critic packets, counterexamples, and experiment records.

Write `shutdown.json` with actual goal state, scientific outcome, pending claims, known worker/experiment status, and the last checkpoint. Do not claim launcher exit or descendant cleanup that has not yet been observed; those belong to cap status. A fresh artifact check should verify local links, current dependency versions, frozen proof/review hashes, and required outputs without claiming mathematical certification from file consistency.

Write a self-contained `resume.md`: exact session and goal identity, cap timestamps, latest useful claims, rejected shortcuts, unfinished proof location, next discriminating test, and authorization status. For a capped partial outcome, explicitly say the goal was not achieved. Return a concise user-facing report with links. Do not schedule automatic continuation outside the live capped service.
