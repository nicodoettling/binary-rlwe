# Hidden-ideal hardness: computational foundations and sample dependence

Prepared 16 October 2026 (Europe/Berlin). **Launch authorized immediately** by the user's request: “Can you prepare an launch a 5h 4 agent astra ultra tmux goal run along these line? Please launch immediately”. This authorizes one new five-hour capped native-goal run, with four active agents total, all `gpt-6-astra` / `ultra`. No further confirmation is required for this launch.

## Goal and useful outcomes

Establish and critically validate a quantitatively substantive new result about the noisy hidden-ideal source underpinning binary-secret RLWE: a computational hardness connection, an improved distinguishing algorithm or useful parameter obstruction, or a many-sample binary-secret recovery implication with explicit source-strength and sample accounting. Every qualifying result must improve on the accepted September baseline, specify a nonempty effective asymptotic regime, and close its load-bearing proof and review obligations.

A successful connection must relate independently specified source problems by an actual algorithm with checked endpoint laws and loss, rather than rename Base2 or assume the desired binary problem. A distinguishing result must improve the existing exp(O(d)) method, use genuinely additional joint information with a quantified algorithmic benefit, or eliminate a previously live useful regime. A sample-extension result must prove its full joint-law, noise, entropy and effective-parameter obligations beyond the accepted one/two-sample theorem. Its primary success criterion is to preserve the two-point source budget or justify the stronger source through a separate computational connection. Merely defining Base_m or restacking the accepted completion under an assumed Base_m is supporting work, not goal achievement. A genuinely new quantitative structural tradeoff under Base_m may qualify, but its additional ingredient and stronger premise must be explicit; it is not justification of Base_m or a consequence of Base2 without a separate reduction.

The cap can expire with no qualifying result. Preserve precise open lemmas, failed attempts, scoped obstructions, and useful partials without claiming goal completion. The run may end early when the substantive goal and all review gates are actually satisfied.

## Authoritative baseline and scope

Use `exploration/runs/brlwe-goal-routes-20260907-astra-ultra/{final.md,claims.json,reconciliation.md}` and `candidates/search/theorem-only-v2.md`, `proof-v1.md`, `supplement-v1.md` as the accepted current baseline. Inherited review is not a fresh proof audit. Root HANDOFF.md contains a stale startup snapshot and an older strongest-result description; it does not override the completed September run.

For powers of two n, let ell=ceil(log2 n), R_q=F_q[X]/(X^n+1), with q splitting completely. Base2 chooses one uniform d-subset T of CRT roots; conditional on T, U_1,U_2 are independent uniform elements of I_T, with zeros allowed. F_1,F_2 have mutually independent coefficient D_ell errors, independent of T,U_1,U_2, with D_t(z) proportional to exp(-pi z^2/t^2). Only (U_1+F_1,U_2+F_2) is published, against two independent uniform ring elements. There is no source oracle, hidden ideal basis, target response or binary secret in the challenge. Noise is small in coefficients, not in finite-field CRT coordinates.

The accepted result concerns uniform classical PPT exact recovery of one coefficient-binary secret from one or two target samples with independent Gaussian errors. It uses sigma_m=2sqrt(m)n ell^3 and q the least prime 1 modulo 2n^3, eventually 2n^3+1<=q<=n^16. Its two concrete source dimensions are floor(sqrt(n)/ell^4) and floor(n/(64ell)), each under a separate Base2 assumption. Base2 hardness remains assumed. The existing reviewed ATT method uses only the first source component and has exp(O(d)) polynomial-overhead runtime under its strict gates. Small d, including O(log n) in this regime, is insecure. Neither an absence of a found attack nor finite examples establish hardness.

The desired application remains rank-one coefficient-binary RLWE at polynomial integer modulus with a nontrivial q/noise ratio, ultimately polynomially many samples. Distinguish search from decision, one challenge from an oracle, marginal from joint pseudorandomness, and statistical from computational comparisons. Alternative parameter families can be investigated with explicit scope; changing residue geometry or noise does not silently preserve the source assumption.

## Initial team and first tests

The team ceiling is one coordinator plus three workers, not four workers. Workers cannot spawn agents, create goals, launch external runs, or change models. Use fresh Astra ultra assignments and recycle slots for nonauthor review.

**A — Computational foundations.** Verify the precise relationship to Order-LWE §7 HLBDD and relevant primary literature, then attempt a concrete hardness connection to standard RLWE or another independently motivated source. First deliver a table of exact experiments and reduction directions, and at least one explicit public map with planted/uniform endpoint calculations or the exact reason it fails. Distinguish hidden from known lattice, Gaussian width conventions, support distribution, source sample budget, and polynomial from superpolynomial modulus. Existing worst-case results for Order-LWE do not automatically prove HLBDD. Information-theoretic smoothing alone does not justify computational hardness in our statistically distinguishable regime.

**B — Joint distinguishing and structure.** Investigate information available from two noisy points sharing T beyond the archived first-marginal attack. First reconstruct the exact scope and cost of ATT v3 from its reviewed version, then test a genuinely joint mechanism (for example cancellation, joint lattice constraints, or algebraic relations) against both full source laws. Small exact models must retain coefficient noise, zero active coordinates, and same-T versus independently redrawn T. Track success, uniform false positives, bit complexity, memory and noise tails. Do not rerun solved singleton/special-binomial failures as purported discoveries. A failed mechanism should identify an actual obstruction and its hypotheses.

**C — Sample dependence and binary-secret transfer.** Define Base_m using m independent ideal points and independent coefficient errors conditional on one T. First separate (i) extending the lossy recovery theorem assuming Base_m, (ii) deriving Base_m pseudorandomness from Base2 or another source, and (iii) new distinguishing power from m observations. Use m=3 as the first decisive gate for a public expansion of Base2 or a target-level sample extension: write the full joint law of all three multipliers and errors on the uniform comparator before proceeding. Extra samples from the same unknown T are not freely available; rotations and correct marginals do not supply independence. Investigate the stacked Gaussian proof as a baseline, the common quotient entropy cost, noise growth, and nonempty polynomial-q regimes. Record fixed m, growing m, and any fixed polynomial exponent separately. Any stronger source premise must remain explicit in the conclusion; a routine stronger-assumption restacking alone is not goal achievement.

**Coordinator — Integration and adversarial selection.** Own the native goal, shared definitions, source/target and parameter comparisons, dependency graph, and reconciliation. Work locally on interactions between A/B/C and cheap counterexamples. After the first comparison, focus on at most two candidates and use released slots for constructive repair, source review, full proof review, and blind review. Do not use a worker shortage or a completed first wave as a reason to declare success.

## Five-hour schedule

The actual cap sidecar timestamps, measured from service activation, control all deadlines.

| Elapsed | Latest phase boundary |
| --- | --- |
| 0–15 minutes | Verify runtime, create one native goal, initialize useful partial files, freeze baseline and initial source contracts, start three workers. |
| 15–65 minutes | Distinct first tests and targeted primary-source checks; save negative evidence and preliminary finite statements. |
| 65–150 minutes | Select at most two promising candidates; develop exact statements/proofs and actively seek counterexamples. |
| 150–220 minutes | Freeze candidates for nonauthor, source/complexity, and blind reviews; recycle slots as needed. |
| 220–260 minutes | Repairs, downstream invalidation, fresh rechecks, or a further focused attempt if no candidate survives. |
| 260–280 minutes | Complete review and delivery checks. Do not begin a large new proof obligation. |
| 280–295 minutes | Wrap-up only: reconcile, save final report and resume checkpoint, stop workers and experiments. |
| 295–300 minutes | Coordinator shutdown reserve; external cap ends remaining local descendants. |

## Review and preservation

Apply the installed mathematical-proof-audit skill and both required references. Freeze exact statements and full joint probability laws before auditing. Import historical regressions by provenance, including the failed independence models, active/uniform-point rank losses, unsupported correlated completion, conditional-sampler obstructions, strict norm/root gates, and the repaired A-PPT modulus clause. Run applicable regressions and targeted finite falsification for new probabilistic claims. CP-1 is mandatory when a sequential product/restored-independence argument is used.

At least one fresh blind reviewer sees only the exact theorem, definitions, explicit assumptions and permitted sources. Preserve full assignments, report bytes, versions and hashes. A changed proof reopens dependent claims and needs a fresh recheck. Same-model review is correlated scrutiny, not statistical independence or formal verification. Final acceptance requires closed current dependencies, valid parameters/quantifiers, source verification, and artifact consistency.

All research writes belong in the new run directory. Old runs, literature, frozen proofs and reviews, project instructions, runner code and Git history remain unchanged. No commits, pushes, external messages, package installs, or publication are authorized by this run. Web searches and primary-source retrieval are allowed and required where appropriate.

Experiments must be bounded, local, and proportionate: default wall time 120 seconds, hard maximum 300 seconds per job, at most two jobs concurrently and one heavy job. Enforce timeouts and an address-space limit no larger than 16 GiB per job; estimate sizes before execution and preserve code, seeds, commands, output, tails and precision qualifications. No detached or remote compute jobs. The generic launcher enforces time, not a 128 GiB aggregate memory cap; do not claim memory containment that has not been installed and verified.

Maintain nonempty final.md and resume.md from the start, plus claims.json, claim-history.jsonl, reconciliation.md, progress.md, agents.json, regressions.json, parameter-table.md, source-comparison.md and experiments/registry.json. Checkpoint core state at least every five minutes and on material results. Save immutable versions; never reconstruct lost historical bytes.

Use sandbox-only workspace-write with approval_policy=never and enabled web search. A policy interruption is preserved and stops research; no automatic retry, rephrasing, rerouting or service restart. The user-requested goal is not completed, paused or blocked merely by timeout. Native continuations are allowed only inside this live five-hour service. Any later service resume requires a new user decision and fresh duration.
