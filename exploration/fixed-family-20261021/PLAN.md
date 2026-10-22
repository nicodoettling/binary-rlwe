# Fixed-family decision binary RLWE and source significance

Version 1, 21 October 2026. User authorization: “Sounds good. Can you go ahead and prepare the run and launch directly?” This approves the preceding five-hour native-goal run, three total Astra ultra agents, explicit Standard service, and protected first 3 h 30 min. This is a new investigation, not a continuation or relabeling of the completed direct-decision goal.

## Frozen objective and completion criteria

Two obligations must be addressed and reported separately.

**FF: fixed-family decision reduction.** Establish a decision reduction for a binary-RLWE parameter family fixed independently of the distinguisher's polynomial sample bound and inverse-polynomial advantage. Preserve the intended rank-one power-of-two cyclotomic setting, one uniform coefficient-binary secret shared across all samples of a target batch, independent uniform public multipliers, and independent coefficient discrete-Gaussian errors. Fix ring, degree sequence, polynomial-value modulus and polynomial noise parameters before quantifying over distinguishers. Reduction runtime, auxiliary parameters and source approximation may depend polynomially on the distinguisher's resources and inverse advantage, but the TARGET family must not change. State uniformity/nonuniformity, finite encodings, code/oracle access and effectiveness explicitly. If a proposed change of dimension changes the target family, audit its quantifiers rather than silently calling it fixed-family.

**SV: computational significance of the source.** Identify the exact decoding radius or sampling width delivered by the reduction and either (i) prove a quantitatively compatible connection to an independently established hardness assumption, or (ii) prove an algorithmic classification of explicit source regimes at those exact parameters, stating what remains unclassified. Classification must be a new, useful exact-parameter consequence or theorem, not merely restating the earlier source-hardness gap or the existence of an easy example. An honest algorithmic classification completes this diagnostic obligation but does not establish source hardness.

Positive completion requires FF plus SV, exact-version reviews, a nonempty useful parameter regime and completed mandatory post-success challenge. Distinguish final statuses “fixed-family reduction achieved”, “source diagnostic completed” and “hardness foundation established”; only the last requires a hardness connection. Better constants, smaller polynomial loss exponents, a distinguisher-dependent target family, unsupported newly named assumptions, or no attack found do not constitute positive completion. The original standard unrestricted hardness question can remain open after a restricted result; disclose this explicitly.

## Protected investigation and terminal rules

The hard runtime cap is external. The protected investigation and scientific stop criteria are cooperative, binding instructions; do not claim OS enforcement of productive research time.

- **No scientific termination before elapsed 210 minutes**, even if an intermediate theorem or an apparent FF/SV result has passed review. Continue meaningful work on the second obligation, scope strengthening, substantially different constructions, counterexamples, parameter analysis, or an adversarial challenge to apparent success. Do not fill time with artificial repetition, decorative documentation or long sleeps.
- Failed checkpoints redirect work. An initial obstruction closes only its exact mechanism. It must trigger a materially different alternative or an explicit reason that alternative is covered. Completion of workers, auxiliary lemmas, one referee wave, or inheritance of old theorems is not terminal.
- After 210 minutes, positive completion is permitted only when BOTH FF and SV meet the criteria above, all changed dependencies are reviewed, and the mandatory challenge below is resolved.
- After 210 minutes, early exhaustion requires substantive documented outcomes for all planned avenues, alternatives after initial failures, and a fresh nonauthor reviewer who actively challenges the exhaustion claim and proposes escapes. The coordinator must address every escape with evidence and remaining-resource estimates. No pending promising candidate, worker, review or repair may remain. Exhaustion leaves FF open and the mathematical goal unfinished unless actually achieved.
- An operational failure or user stop is a separate exception, never reported as scientific exhaustion or success. A detected content-policy termination is not authorization to retry, rephrase or route around it.
- At the hard deadline, preserve strongest results and exact gaps. A completed report is not an achieved mathematical objective. No automatic restart, extension or successor.

## Five-hour schedule

All offsets are from actual service activation and are immutable after launch.

| Elapsed | Activity |
| --- | --- |
| 0–45 min | Exact quantifier/interface reconstruction; first falsifiable tests; nonterminal allocation checkpoint |
| 45–210 min | Protected constructive exploration, source classification, alternatives and ongoing challenges; substantive allocation checks at 90 and 150 min |
| 210–270 min | Full and blind review, targeted repairs, exact parameter and source checks |
| 270–300 min | Final consolidation and delivery; workers/experiments stop by 285 min; final checkpoint by 295 min |

Checkpoints every ten minutes and after material events. Use Europe/Berlin in user-facing times; record exact UTC/monotonic origin and cap timestamps in receipts. The +210-minute boundary is both the protected-period end and discovery cutoff. Review may begin sooner on a candidate but does not replace meaningful protected investigation by the team.

## Team and scientific allocation

One coordinator plus at most two active workers/referees TOTAL. Every assignment uses `gpt-6-astra`, reasoning `ultra`, `service_tier="default"`; workers have fresh context and cannot spawn. Completed slots may be recycled for new assignments/referees. No extra CLI sessions to evade the ceiling.

### Worker A: FF1 — joint-law transfer and fixed-family quantifiers

Begin with the accepted MR-v1/FIXED-MAIN-v2 restriction

    sigma0 >= 8*k0*n*(n/2+2)/epsilon_*.

Freeze exactly where sample count and inverse advantage enter, and separate avoidable TV estimates from actual distribution mismatch. Investigate randomized rounding, discrete Gaussian correction, normalized joint-law methods or a different modulus-transfer kernel. A scalar variance match or marginal approximation is not a joint product-error theorem. A square-root improvement that retains adversary-dependent fixed-noise exponents is partial progress only. Aim for negligible full-batch transfer error for every polynomial sample bound at one fixed target family, or a different argument that avoids needing that statistical guarantee.

First test: an explicit channel with exact planted/comparator laws, or a quantitative witness against a specified channel. Preserve all shared-secret correlations. Any lower bound refutes only its stated class of transformations. If this avenue fails, pursue a materially different construction and send the obstruction to the coordinator's FF2 search.

### Worker B: SV — exact source usefulness and foundation

Reconstruct the current BDD radius in J^-1, with all auxiliary-prime and advantage losses. Compare it directly to justified classical decoding algorithms. If using DGS comparisons, first prove/check the exact BDD-to-DGS composition at the new radius, error and code-access model; an easy wide DGS sampler does not automatically yield a BDD algorithm or reverse the existing implication.

Start with explicit source families and ordinary input bases; compare HNF/quotient-exponent criteria, polynomial numeric index, known short generators and large-characteristic candidates. Polynomial encoding length is not polynomial value. A short vector existing by Minkowski is not a supplied algorithm. Relate meaningful remaining families to established assumptions only through effective maps with exact resources and both endpoints. Retain the earlier short-complementary-multiplier and integral-map obstructions.

First deliverable: a parameter table comparing new output radius/derived width to algorithmic regimes, with proofs or exact imported hypotheses for each comparison, and a nontrivial family classification or a precise unmet implication. Then seek either an effective new hardness connection or a stronger delimitation, not another unstructured search for arbitrary ideal transfer.

### Coordinator: FF2 — alternatives, synthesis, and challenge

Investigate avoiding the present modulus-transfer edge: fixed-modulus selected-functional/fiber bounds, alternative selected information, controlled hybrids, or amplification whose exact shared-secret experiment is justified. For amplification, fresh decision coins or multiple blocks do not automatically repair a distinguisher that succeeds only on a small fraction of secrets. For fixed-modulus bounds, the existing norm-divisor argument averages over DISTINCT primes and one COMMON partition; neither condition can be dropped silently.

Maintain the global quantifier table and dependency graph, ensure both FF and SV remain substantive, and incorporate failed attempts into new assignments. Quantum sampling composition is a bounded companion only where needed to assess SV, not a substitute for FF. Existing PRS17/OHCP and Regev machinery should be reused at exact scope rather than rebuilt.

## Evidence, reading order and regressions

Alias roots, relative to project:

- DD = exploration/runs/brlwe-direct-decision-20261021-astra-ultra
- RH = exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra
- OLD = exploration/runs/brlwe-standard-hardness-20261017-astra-ultra

Read DD/final.md, DD/programme-decisions.md, DD/reconciliation.md and DD/coordinator/acceptance-v1.json, then the exact FIXED-MAIN-v2 statement/proof, MR-v1 statement/proof, AM-MAIN-v3 statement/proof and source/complexity reports as relevant. Frozen PROVISIONAL banners do not override later exact-hash acceptance records. This intake is not re-certification of inherited results.

Load-bearing pointers:

- DD/coordinator/fixed-main-statement-v2.md and fixed-main-proof-v2.md.
- DD/coordinator/modround-statement-v1.md and modround-proof-v1.md.
- DD/coordinator/am-main-theorem-v3.md and am-main-proof-v3.md.
- DD/coordinator/selected-functional-statement-v2.md and selected-functional-proof-v2.md.
- DD/workers/DD2/am1-strengthened-theorem-v1.md and am1-strengthened-proof-v1.md.
- DD/reviews/FULL2/source-complexity-report-v1.md and exact-v2-recheck.md; DD/reviews/BLIND2/followup-v2-report.md.
- RH/coordinator/M1/theorem-only-v2.md, proof-v3.md, remaining-family-v2.md and RH/coordinator/m1-acceptance-v2.md.
- RH/workers/A/linear-transfer-theorem-v1.md and RH/coordinator/ab-acceptance-v1.md.
- OLD/workers/RF4/same-j-composition/interface-statements-v1.md and OLD/coordinator/samej-acceptance-v1.md; OLD/workers/F/finite-quantum-integration/ for any new coherent composition.
- DD/regressions.json contains 203 scoped entries. Retain every ID and exact provenance by reference; reconcile applicability to changed claims without bulk duplication. Add new counterexamples before repairs. Preserve CP-1 against unsupported adaptive product reasoning.
- literature/2017-258.pdf (PRS17), literature/2020-119.pdf and 2020-1185.pdf, literature/2026-2443.pdf, and DD's exact primary-source references. Existing extraction: exploration/direct-decision-20261021/inputs/PRS17.txt. The PDF is authoritative. Primary-source web reading is allowed for a concrete needed theorem, not a repetitive broad survey.

The base HANDOFF.md describes older work and is stale; the exact October statements, verdicts and final receipts take precedence. Historical native goals, manifests and hashes are read-only.

## Mandatory mathematical challenge and review

For each new main candidate, freeze a theorem-only version with all quantifiers, models, source/target parameters, output laws and costs. Obtain nonauthor full-proof/source/complexity review and a fresh statement-only blind review, both on exact bytes. Withhold author proofs, statuses, suspected bugs and coordinator conclusions from the blind packet. Preserve complete assignments, allowed-source lists, exposures, reports and seals. Repairs reopen dependencies and require fresh checks; same-model agreement is correlated scrutiny, not formal verification.

The reviewers must explicitly challenge: (a) whether target parameters really precede all adversaries; (b) the shared binary secret and full conditional error law; (c) small distinguishing advantages and arbitrarily high fixed polynomial sample exponents; (d) numeric versus bit complexity; (e) source classical simulation at the ACTUAL new radius/width; (f) effective source transfer versus existence of short objects. A source hardness claim additionally needs independent established premises, not merely absence of a known efficient algorithm.

An apparent early success is a signal to intensify these challenges and investigate scope during the protected period, not to invoke the previous run's early-achievement certificate. The old certificate is not authority for this run.

## Execution, experiment and delivery contract

New output: exploration/runs/brlwe-fixed-family-20261021-astra-ultra. Research writes only there, temporary /tmp files allowed with evidence retained. Package, literature, historical runs, user/project settings and Git remain read-only. No commit/push, publication, outside messages, installation, remote solver jobs, detached computations, nested Codex sessions or extra services. Use sandbox-only workspace-write with approval_policy=never.

Use the v3 external time-cap helper. No aggregate memory containment is claimed. Local jobs have enforced wall limits (120 seconds default, 300 seconds maximum, always within remaining experiment window) and <=16 GiB address space per job, normally much smaller; at most two jobs and one heavy concurrently. Register hypothesis, code/input/seed, exact command, dimensions/bit sizes, resource estimates and expected outcome before executing. Preserve full failures, outputs, timings, peak memory and precision/tail treatment. Bounded tests do not prove asymptotic statements.

Deliver final.md, claims.json, reconciliation.md, regressions.json, reduction-attempts.md, parameter-table.md, source-comparison.md, progress.md, resume.md, programme-decisions.md, checkpoint/phase records, full review and experiment evidence, runtime/goal/usage/shutdown receipts. The final report MUST have separate FF, SV-diagnostic and hardness-foundation statuses, explain what changed versus the accepted predecessor, and name exact next tests. Save a protected-period compliance record and any post-210-minute termination certificate. Report incomplete gates as provisional. No automatic successor.
