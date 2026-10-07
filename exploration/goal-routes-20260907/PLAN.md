# Capped goal proposal: new hardness routes for binary-secret RLWE

Status: **launch authorized with a three-hour cap**. The user approved this package with “go ahead and start, but please with a 3h time limit instead of 3.5h”. The run started on 7 September at 21:34:27 UTC and was verified healthy, with a native goal active. The three-hour cap ends on 8 September at 00:34:27 UTC; see launch-receipt.json. The user now requests a goal run; the older non-goal restrictions describe previous runs and do not apply to this proposal.

## Scientific goal

**Establish a new, quantitatively meaningful hardness implication for coefficient-binary, rank-one RLWE from an independently specified and motivated nonbinary source assumption, by changing the proof target, quotient geometry, or computational reduction.**

The original search question takes priority. A decisional result also qualifies if it improves the current negligible-loss gap. The run has a 180-minute maximum and may instead end with reviewed partial results, a scoped obstruction, or a precise unresolved lemma. A written report or a list of disposed workstreams does not achieve the hardness goal.

This is broader than proving active-point inheritance. The three initial mechanisms are deliberately different: avoid the decision requirement, change the algebra responsible for the defect, or handle the defect computationally. At most two routes proceed to full development after the initial comparison. Existing results are a starting point, not a quota of outcomes to reproduce.

## Fixed target and permitted movement

Keep rank one, growing power-of-two degree, independent uniform coefficient-binary secrets, and explicitly independent coefficient Gaussian target errors. Distinguish source pseudorandomness, target search success, and target decision advantage. Preserve the actual number of challenges and samples in every implication.

The preferred target has polynomial integer modulus and $q/\sigma\ge n^c$ for fixed positive $c$. Start from the last run's common parameter table, but allow changes in quotient dimension, splitting degree, ideal support law, Gaussian widths, and the explicitly stated source-sample budget. An assumption is not independently justified merely because its definition omits a binary secret. Identify its relationship to public literature and the changes needed at our parameters.

A clearly labelled larger-modulus or weaker-security result may be useful. A genuinely new, fully checked asymptotic PPT-hardness implication at superpolynomial target modulus **can qualify as a scoped goal achievement**, provided inputs still have polynomial bit length, the target noise ratio is nontrivial, and all bit-complexity and source assumptions are explicit. It does not satisfy the preferred polynomial-modulus endpoint. A fixed promised-advantage theorem or an implication with unresolved load-bearing analytic premises is only partial progress. Any claimed return to polynomial target modulus requires an actual ring-preserving modulus/noise reduction. Do not change the coefficient field to an extension field and call it the same RLWE problem; residue extensions must arise from factorization of the original ring modulo the integer prime.

## Four-agent organization

The ceiling is **four active agents total: one coordinator and three workers**, all `gpt-6-astra` with `ultra` reasoning. This is a concurrency limit, not a total-thread budget. Recycle slots for fresh nonauthor and blind review; workers cannot spawn agents or create goals.

The coordinator owns the native goal, exact theorem statements, shared parameter comparison, claim graph, source interfaces, and integration. The coordinator also works on the shared source-budget question locally instead of merely scheduling workers.

### A. Direct search hardness through lossiness

**Priority:** revisit the user's original recovery problem. The current active-coordinate defect entered a decision hybrid that replaces $UZ$ by a uniform ideal point. Bounding recovery may need neither that replacement nor uniformity of the secret quotient.

Candidate to prove or refute, not an established result of this planning pass:

$$
P_{\rm guess}(S\mid\text{planted transcript})
\ \le\ |R_q/J|\,P_{\rm guess}(S\mid S+G)+\eta_N.
$$

Noise completion formally suggests the transcript $US+F(S+G)+H$. If its witness-retaining joint law is correct, revealing the quotient of $S$ and the noisy observation might suffice to bound guessing without assuming that $U$ is invertible on its support. The source distinguisher can sample its own secret and errors and check whether a recovery solver returns that exact secret.

First obligations:

1. Freeze the full joint law and prove or falsify the witness-retaining noise comparison. Verify that revealing source coins and the completion kernel does not invalidate the proposed guessing bound.
2. Derive the exact binary/noisy-bit guessing probability and the quotient leakage cost. One candidate bound for independent auxiliary $D_\ell$ coordinates is $[(1+D_\ell(0))/2]^n$; check the unwrapped identity and wrapped comparison rather than assuming them.
3. State the resulting finite search-success inequality and a simultaneous parameter range. Test whether only an entropy budget is needed, potentially allowing a larger quotient than the existing extractor does.
4. First establish one target sample. Then test **two target samples from the source's actual two noisy ideal points**, generating both responses locally under one secret and using the full stacked completion. Account for both source noise laws. More target samples require an explicitly available source budget or a separately proved expansion.

This revisits noise lossiness from the [original ordinary-LWE paper](https://eprint.iacr.org/2020/119.pdf), with a different ring source interface. It is not a claim that the paper already proves the proposed ring statement. The two-sample search direction is potentially useful even if full decisional pseudorandomness remains out of reach.

### B. Partial splitting and larger residue fields

**Priority:** change the algebra that makes a uniform ideal point rank-deficient too often.

Suppose selected CRT factors have residue fields of order $Q=q^f$, with $k$ selected factors and total quotient dimension $D=kf$. Recheck the finite product-ring calculation

$$
\eta_{\rm iso}=1-(1-Q^{-1}+Q^{-2})^k\le k/Q.
$$

Growing residue degree could make the bad mass negligible while the integer modulus stays polynomial. This is an algebraic candidate, not a transferred extraction or hardness theorem.

First obligations:

1. Exhibit a nonempty asymptotic prime/factor-degree family for $X^n+1$, with polynomial representation, sampling, and public arithmetic. Require $f=\operatorname{ord}_{2n}(q)$, $1\le k\le n/f$, and $D=kf$, simultaneously with an output-entropy budget compatible with the remaining binary-secret entropy. A large residue degree can remove the rank defect while making $D\log q$ too large for the proposed extraction. Freeze $f,k,D$ separately; do not reuse $d$ ambiguously.
2. Determine whether conditional binary extraction holds for these quotients, using applicable joint random-walk or ideal-sensitive leftover-hash results. The existing fully split theorem does not automatically apply. Keep posterior replicas conditioned on the same observation.
3. Check noise completion, source motivation, and simple algebraic decoding in that same regime. A large field alone supplies none of these.
4. If extraction is the obstacle, compare a precisely stated search-only version with A before abandoning the algebraic family.

The [ring leftover-hash manuscript](https://eprint.iacr.org/2025/1080) is a source of tools to inspect, not an assertion that it already handles this conditional binary distribution. A useful negative result identifies which requirement conflicts with the candidate splitting regime and under what hypotheses.

### C. Computational source transfer and advantage accounting

**Priority:** examine transformations and computational comparisons outside the previous exact-statistical obstructions.

Investigate active-point inheritance, transformations using both public components, equal-small-noise source inputs, source symmetries, and controlled approximate preservation of the uniform comparator. Freeze each pair of challenge worlds and the public algorithm before analyzing noise or entropy.

Aim for an implication of the form

$$
\operatorname{Adv}_{\rm source}(B)
\ge \operatorname{poly}(\varepsilon,1/n)-\operatorname{negl}(n),
$$

for target advantage $\varepsilon$, with an explicitly positive inverse-polynomial bound for every inverse-polynomial $\varepsilon$, and polynomial runtime/query cost. Merely restating an additive $d/q$ loss does not qualify.

First obligations:

1. Use finite exact mixture models to test concentration of distinguishing advantage on the deficient branches and signed-advantage cancellation.
2. Distinguish repeated evaluations on one challenge from independent fresh source samples. Any amplification or rejection procedure must account for observable events, normalization, runtime, and its actual oracle budget.
3. Check planted and uniform endpoints together. Correct posterior simulation on the planted input does not imply correctness on uniform input.
4. Maintain an assumption comparison with the explicitly defined same-ideal [HLBDD source](https://eprint.iacr.org/2018/494.pdf). A changed source law, query budget, or security strength must remain visible.

A fixed promised-advantage threshold can be a qualified fallback, with its exponent chosen before parameters. It is not full negligible-advantage hardness. A scoped impossibility for a genuinely new transformation class is a useful partial outcome.

## Schedule and selection gates

Times are elapsed from capped-service activation and are latest boundaries. Read the actual UTC timestamps from the cap sidecar; initialization consumes part of the same envelope.

| Elapsed | Work and gate |
|---|---|
| 0–15 minutes | Read the cap, create the one native goal, import current claims/regressions, freeze target and source conventions, and write a partial report. |
| 15–50 minutes | Three distinct initial mechanisms. Each returns an actual finite statement or public map, its first attempted proof/falsification, and the limiting condition. |
| 50–100 minutes | Develop at most two routes using one parameter/sample/assumption comparison. Assign the third slot to breaking those routes or closing a specific shared dependency. |
| 100–140 minutes | Freeze candidates for fresh nonauthor review, including at least one blind theorem-only review. Review imports, probability laws, advantage, and complexity. |
| 140–160 minutes | Repair, invalidate downstream claims, and freshly recheck exact edited versions. If an early review frees time, test the next concrete in-scope mechanism. |
| 160–175 minutes | Wrap-up only: reconcile, perform proportionate artifact/regression verification, write the result and resume checkpoint, and finish workers/experiments. |
| 175–180 minutes | Coordinator shutdown/checkpoint reserve. No new research or experiments. External termination enforces the cap. |

Early scientific achievement requires a new checked implication with an explicit source premise, one coherent parameter regime, exact task/sample scope, and no unresolved load-bearing defect. A modest correctly scoped theorem can qualify; it must state whether the original multiple-sample objective remains open. A result already in the repository, or a theorem conditional on a newly renamed version of the desired binary problem, does not qualify.

A new obstruction or precise open lemma is valuable but does not by itself complete this hardness goal. Keep exploring available in-scope routes until wrap-up, unless the actual goal is achieved or a genuine blocking condition meets the platform's goal-status rules. A temporary lack of free agent slots is not a scientific stopping criterion.

## Review, evidence, and expected delivery

Use the mathematical-proof-audit protocol. Import historical counterexamples and their source records without spending the discovery phase redoing unrelated large computations. Run every regression applicable to a current claim, plus a new targeted finite search before accepting a repair. Preserve original proof versions and complete referee packets. Blind review receives only the frozen statement, definitions, explicit assumptions, and permitted primary sources; disclose the proposed proof and earlier objections only after its report is frozen.

Source verification is targeted to load-bearing claims. Use primary literature and installed local tools. No package-installation project, GPU work, external compute, or unbounded parameter sweep. Default experiment timeout is 120 seconds, maximum 300 seconds, at most two concurrently, always truncated by the task deadline. Record code, exact inputs, seeds, precision/tail qualifications, outputs, failures, and elapsed time. Finite examples and same-model reviewer agreement do not establish asymptotic hardness.

Write a continuously useful `final.md`, `claims.json`, `claim-history.jsonl`, `reconciliation.md`, `progress.md`, `agents.json`, `parameter-table.md`, `source-comparison.md`, and `resume.md`. Include complete candidate proofs, referee packets, `regressions.json`, and `experiments/registry.json`. The final report should lead with any genuinely new theorem or obstruction and its practical mathematical implication, not the number of agent tasks completed.

The minimum honest capped delivery explains what was attempted, what was newly learned, exact surviving claims, where an argument fails, and the next discriminating test. It may explicitly report **no new validated implication**. Do not manufacture progress to meet an output quota.

## Execution and authorization

Use the updated skill's `capped_codex_tmux.py`, **not** the legacy project `bounded_run.py`, which forbids goals. The request is one native goal with no token budget, Astra ultra, four active agents total, `--max-runtime 180m`, and `--wrapup-before 20m`. The cap includes the whole team. Native continuation inside the live capped service is intended; restarting a terminated service is not authorized.

The helper independently enforces service shutdown and writes cap status. It does not replicate the old project's continuous policy/staleness observer. Preserve atomic five-minute coordinator updates and use the existing standalone snapshot function as documented in the prompt; do not call the old manifest-dependent checkpoint command. This is cooperative scientific checkpointing plus independent process containment, not a promise that the model will always checkpoint before a forced stop.

At timeout, leave an unfinished native goal unfinished and record a time-limited checkpoint. Do not call it completed, blocked merely because time expired, or paused by the timer. No automatic service restart, retry after content-policy failure, or post-deadline research is permitted. Later resume requires new user authorization and a fresh explicit budget.

See [LAUNCH.md](LAUNCH.md) for the exact proposed invocation and health checks, [COORDINATOR_PROMPT.md](COORDINATOR_PROMPT.md) for the durable task, and [run-config.json](run-config.json) for the declarative limits. This specific launch is approved; subsequent resumes remain separately authorized.
