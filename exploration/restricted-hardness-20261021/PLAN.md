# Restricted ideal sampling: computational value and hardness transfer

Version 1, 21 October 2026. Launch authorized by the user: “sounds good. Please prepare and directly launch the run.” This approves the preceding three-hour, three-agent Astra ultra proposal. This package is a new bounded work package continuing the existing unfinished native research goal, not a claim that the earlier goal was achieved.

## Objective and success criteria

Assess and advance the computational-hardness connection for the restricted ideal Gaussian sampler obtained from binary-secret RLWE recovery. Determine where its delivered distribution and width provide computational power, test an effective transfer from established hard ideal families, and investigate whether sharper guessing bounds can enlarge the useful ideal family.

Useful outcomes include an internally reviewed algorithm delimiting the proposed assumption, a noncircular reduction with a nonempty parameter regime, or a precisely isolated unresolved obligation with failed routes and evidence preserved. None of these automatically completes the existing broader native goal of establishing a standard computational foundation for binary-secret rank-one RLWE.

## Authorized execution

- Three active agents TOTAL: coordinator and at most two workers, all `gpt-6-astra`, reasoning `ultra`.
- Explicit Standard `service_tier="default"` for root and all workers. Use the current v3 capped runner; its `features.fast_mode=true` capability flag enables explicit tier serialization and does not select Fast.
- Three-hour externally enforced cap from service activation; no automatic extension or restart.
- Decision at elapsed 45 minutes. Discovery stops at elapsed 135 minutes; the last 45 minutes are for adversarial review, reconciliation and delivery. Workers/experiments stop by elapsed 165 minutes. Final checkpoint by elapsed 175 minutes.
- Sandbox-only permissions, local experiments and primary-source web research. No installation, remote computation, Git changes, external messages or publication during the autonomous run.
- Local experiments: 120-second default wall timeout, 300-second maximum; at most two simultaneous jobs, one heavy; at most 16 GiB address space per job, smaller where appropriate. Explicitly enforce limits before each experiment. The generic runner enforces time, not an aggregate memory cap.
- Continue native thread `01a14b7b-9e45-7b70-b46d-0bf70e17f2e2`. Preserve its objective and unfinished status unless the actual original objective is achieved. No token budget was requested. Record fresh usage relative to the launch baseline; accumulated native tokens are not weekly quota accounting.

## Evidence and frontier

Historical run root: `exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/`.

Read its final report, reconciliation and claims alongside exact statements and acceptance records. Historical frozen banners are not current verdicts. The complete same-J composition RF4-SAMEJ-v1 and conditional weighted-trace RT1-WEIGHTED-v2 have internal scoped acceptance; this launch does not re-certify them. The Regev-style BDD-to-dual-DGS quantum mechanism is an established component. Its finite implementation is not the new research target.

Key links relative to the historical root:

- `workers/RF4/same-j-composition/same-j-theorem-only-v1.md`, its proof and interfaces; `coordinator/samej-acceptance-v1.md`.
- `workers/A/class-changing/small-index-simulation-v1.md`: provisional classical simulation at the delivered width for polynomial-index ideals. Its proof and exact scope must be checked before using it as a new accepted baseline.
- `coordinator/tower-lift/weighted-v2/theorem-only-v2.md` and `coordinator/tower-lift/weighted-acceptance-v2.md`: supplied short complementary multiplier, not an algorithm obtaining it.
- `workers/D/relaxed-guessing/`: prior provisional high-index lossiness example, with an easy public source; avoid rediscovering it as hardness progress.
- `workers/A/fractional-composition/proof-v1.md`, section 4: exact bound `p_guess(S | S+G_J) <= min(1, D * ((1+D_Z,t(0))/2)^n)`. Neither uniform coset weights nor a public sampler for proof-only G is assumed.
- `workers/A/class-changing/`, `coordinator/tower-lift/`, `reduction-attempts.md`, `regressions.json`: earlier transfers, obstructions, and 151 regression IDs.

## Programme and assignment

### M1: Establish the useful sampling regime — coordinator

Freeze the actual full output law, width, accuracy and cost. Verify the provisional polynomial-index simulation, then identify which superpolynomial or exponential indices leave an unresolved computational problem. Compare genuine algorithms with the exact delivered width and ordinary basis input; a short-basis existence theorem is not an algorithm. First test: can the baseline sampler already supply every oracle call used by a proposed transfer? Positive outcome: a reviewed simulation delimiting the family. Negative or inconclusive outcome: a precise unmet sampler requirement, not evidence of hardness.

### M2: Effective hard-family transfer — worker A

Start with weighted trace and the short complementary multiplier in `I S J^{-1}`, with extension ring S and target ideal I. Test whether a compatible multiplier can be found efficiently using only available inputs and allowed oracle queries. Charge degree growth, norms, output radius, success, representations and the exact source/comparator laws. Check whether obtaining the multiplier is already a comparable short-vector task. First test: an explicit candidate construction with a full parameter inequality, or a scoped obstruction to that construction. If the inherited route has no new effective ingredient, stop that branch rather than restating the conditional theorem. Alternative class-changing or correlated-query constructions are in scope only if they offer a concrete new test and survive the historical obstructions.

### M3: Entropy-sensitive family enlargement — worker B

Investigate actual binary guessing probability, cube fibers and Gaussian mass rather than index alone. Distinguish residue-only leakage from the full observation S+G_J. Prioritize candidates for which an enlarged useful ideal family could matter computationally. First test: a sharpened, exact bound or family beyond the existing index criterion, together with a public-source distinguishing check and noise/geometry compatibility. Reconcile the prior high-index/easy-source examples before proposing novelty. Pure information-theoretic enlargement without computational viability remains an auxiliary result.

### Decision gate and allocation

By elapsed 45 minutes, record for M1–M3: nearest predecessor, whether it already covers the proposed result, full-law and parameter compatibility, one concrete new test, and the next allocation. Select at most two substantive unresolved directions. Shift a worker to falsification if needed. A failed bound is not an impossibility theorem; unsuccessful attacks are not hardness evidence. If all branches are exhausted, review the scoped outcome and finish early with the native goal honestly unfinished.

## Review and delivery

Reserve the final 45 minutes. Freeze candidate statements before review; use a nonauthor full-proof/source/complexity reviewer and at least one fresh blind referee receiving only the theorem, definitions, assumptions and allowed sources. Recycle slots without exceeding three total. New mathematical acceptance requires closed dependencies, historical regression dispositions, targeted finite checks for probability claims, exact-version rechecks after repair, and clean artifact verification. Incomplete gates leave claims provisional. Same-model agreement is correlated scrutiny, not formal verification.

Coordinator owns shared integration. Workers write only their assigned directories. Preserve failed versions before repair. Maintain concise checkpoints every ten minutes and after material events, plus the 45-minute gate receipt. Avoid repeated archive copying, open-ended literature surveys, and large benchmark sweeps.

Output root: `exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/`. Deliver `final.md`, `claims.json`, `reconciliation.md`, `regressions.json`, `reduction-attempts.md`, `progress.md`, `resume.md`, `programme-decisions.md`, experiment provenance, complete review inputs/reports, startup/runtime evidence, usage baseline/final receipts and honest shutdown status. Clearly state which result would justify another run. No successor is scheduled by this plan.
