# ENT1: binary RLWE with high joint min-entropy

Version 1, 21 October 2026. **Planning status: proposed successor, not launched. Mathematical status: candidate extension, not an accepted theorem.** Origin: the collaborator's question and the subsequent discussion of weighted selected-functional bounds. This package records that proposal and the investigations needed to establish or delimit it; it is not a new proof or audit.

## Target and scope

Work over the existing power-of-two cyclotomic ring R = Z[X]/(Xⁿ+1). Replace the uniform secret by S sampled from a distribution μ supported on {0,1}ⁿ with joint min-entropy

$$
H_\infty(S)=-\log_2\max_s\mu(s)\ge h.
$$

The bits may be correlated. Retain one secret shared across a batch, independent uniform public multipliers, and independent coefficient Gaussian errors. Begin with a fixed public distribution family and an efficient sampler, with all sampling costs charged. The computational wrapper must be able to draw fresh secrets from μ and check its predictions; a promise of entropy without sampling access is not yet a computational theorem. Do not require evaluating μ(s) merely to implement the wrapper. Approximate sampling needs an explicit total error budget over all calls.

The first target is an entropic analogue of the accepted restricted decision reduction. For a nonzero integral ideal J with D=N(J), investigate replacing the uniform-secret index restriction by a quantitative entropy surplus h−log₂ D. A candidate useful regime is h≥ηn and D≤2^(ρn), for fixed 0<ρ<η≤1. Merely requiring log₂ D<h is not enough: derive the slack needed for the actual distinguishing advantage and all accumulated errors.

Keep μ and the residue partition fixed across auxiliary primes. Specify all quantifier order, especially whether the target distribution is fixed before the source ideal and the distinguisher. The initial theorem should use a fixed public μ-family rather than silently allow ideal-dependent or prime-dependent targets. Retain the existing sample, noise, advantage, finite-input and source-geometry restrictions unless separately improved. Neither unrestricted worst-case hardness nor a fixed target family for every PPT exponent follows just from ENT1.

## Proposed mechanism — obligations, not certified inequalities

For an auxiliary split prime q with CRT roots ζ(q,j), define

$$
W_q(c,j,v)=\Pr[S\bmod J=c,\ S(\zeta(q,j))=v],\qquad
K_q(\mu)=\sum_c\max_{j,v}W_q(c,j,v).
$$

Let Cμ be the number of residue classes occupied by the support of μ, so Cμ≤D. The first candidate bound concerns optimal prediction of a selected root value from Y=S+G, with independent G sampled from D(J,t). Subject to the exact hypotheses of the inherited Gaussian envelope, investigate

$$
p_{\mathrm{selected},q}(S\mid Y)
\le \min\{1,\Gamma(t,r_0)K_q(\mu)\},\qquad
\Gamma(t,r_0)=\exp\!\left(\frac{\pi n}{4r_0}\right)
\left(1+\frac{r_0}{t^2}\right)^{n/2}.
$$

For M distinct split primes q≥Qmin and uniform averaging over the list, the proposed weighted collision bound is

$$
\mathbb E_q K_q(\mu)
\le \min\left\{1,\sqrt{C_\mu\,2^{-h}}+\sqrt\nu\right\},
\qquad \nu=\frac{n\log n}{2M\log Q_{\min}}.
$$

The intended proof route weights the existing collision argument: for each residue fiber of mass w_c, bound the collision diagonal by 2⁻ʰw_c and the averaged off-diagonal term by νw_c², then apply the appropriate square-root and summation inequalities. Audit the selected-root maximum, all averaging orders, normalizers and common-partition hypotheses. Do not simply multiply the entire uniform-secret estimate by 2^(n−h), which would also worsen the prime-collision term.

The computational application must compare Γ(√(D2⁻ʰ)+√ν), with all truncation, approximation and simulation errors, against the extractor's actual success lower bound. Derive finite constants and a nonempty parameter regime. Recovery of the uniform case μ(s)=2⁻ⁿ is a necessary consistency check, not proof of the weighted case.

## Dependencies and first discriminating checks

Paths below point to frozen predecessor versions. Their [exact acceptance record](../runs/brlwe-direct-decision-20261021-astra-ultra/coordinator/acceptance-v1.json) governs inherited status only. Changed secret laws reopen the relevant dependencies.

| Obligation | Nearest evidence | First check and possible obstruction |
| --- | --- | --- |
| ENT1-A: weighted Gaussian envelope | [SFUNC-v2 proof](../runs/brlwe-direct-decision-20261021-astra-ultra/coordinator/selected-functional-proof-v2.md) | Replace uniform mass by μ(s) without dropping posterior normalizers or occupied fibers. Verify the exact selected-functional experiment. |
| ENT1-B: weighted prime averaging | [DD2-AM1-SNF-v1 proof](../runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/am1-strengthened-proof-v1.md) | Check the diagonal/off-diagonal calculation for correlated distributions, one common partition and distinct primes. Identify which steps fail for q-dependent weights. |
| ENT1-C: executable decision extraction | [DD1-EXTRACT-v1 proof](../runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD1/extraction-proof-v1.md) | Audit fixed-secret reasoning and subsequent averaging under μ, including concentration of distinguishing advantage on rare secrets, calibration/test-bank conditioning, sampler access and runtime. |
| ENT1-D: completion and modulus transfer | [A-FRAC-v1 proof](../runs/brlwe-standard-hardness-20261017-astra-ultra/workers/A/fractional-composition/proof-v1.md), [MR-v1 proof](../runs/brlwe-direct-decision-20261021-astra-ultra/coordinator/modround-proof-v1.md) | Verify that the completion's product law survives and rounding needs only binary support. Independence of S from the Gaussian/source variables must be stated, not inferred from high entropy. |
| ENT1-E: composed computational theorem | [FIXED-MAIN-v2 statement](../runs/brlwe-direct-decision-20261021-astra-ultra/coordinator/fixed-main-statement-v2.md), [proof](../runs/brlwe-direct-decision-20261021-astra-ultra/coordinator/fixed-main-proof-v2.md) | Propagate the new losses through the full reduction; give a finite parameter table, actual output radius, quantifier order and total cost. Source-hardness status stays separate. |

The original [Entropic LWE paper](../../literature/2020-119.pdf) and [entropic Ring-LWE paper](../../literature/2020-1185.pdf) are the comparison baseline. Before a novelty claim, compare exact source models and quantitative guarantees with their statements. This proposal is an extension of the project's present mechanism, not a claim that entropic RLWE is a new research question.

## Milestones, outcomes and review

1. **Model and falsification gate.** Freeze the μ-family, sampler/access model and quantifiers. Check biased product distributions, flat correlated subsets, mixtures and heavy atoms, singleton residue fibers, and entropy near log₂ D. Include a high-Shannon-entropy/heavy-atom control to prevent replacing joint min-entropy by Shannon entropy or a sum of marginal entropies. Any finite enumeration is diagnostic only.
2. **Weighted analytic result.** Prove or correct ENT1-A/B with exact constants. If only a restricted class of μ works, identify its substantive additional property; do not silently redefine “high entropy” to include it.
3. **Computational composition.** Establish ENT1-C/D/E, including sampling, finite precision, call counts and actual source parameters. A weighted information-theoretic lemma alone is useful partial progress, not entropic computational hardness.
4. **Adversarial review.** Freeze exact theorem and proof versions. Require nonauthor full-proof/dependency review and a fresh statement-only review before acceptance; changed dependencies need rechecks. Same-model agreement is correlated scrutiny, not formal verification. Explicitly challenge rare-secret advantage concentration, adaptive conditioning, q-dependent laws, and the separation between a reduction and a hard source assumption.

Suggested effort for a later authorized investigation: a bounded 3–5-hour package with a substantial composition/review reserve, calibrated after the ongoing run's outcome. Agent count, models, cap and any protected exploration period remain to be selected; this is not a launch brief.

**Positive outcome:** a reviewed entropic decision-reduction theorem with explicit surplus h−log₂ D, a nonempty useful parameter window, an executable sampler-based wrapper and honest source-hardness scope. This broadens the supported secret class. Compose with any FF improvement only after checking the changed interfaces.

**Partial outcome:** a reviewed weighted selected-functional/averaging theorem with a precisely located computational gap. Preserve it as an auxiliary result and prioritize that gap; do not promote it to a computational theorem.

**Negative outcome:** a counterexample or quantified obstruction to a specified weighted bound or interface. Record its exact scope, then consider one justified restricted-source alternative, such as flat or explicitly structured sources. Failure of this mechanism does not disprove entropic binary-RLWE hardness.

**Inconclusive outcome:** preserve exact candidate versions and the first unresolved obligation. No automatic extension, restart or claim of success. Close a subtask only at its stated scope; an easy weighted lemma is not completion of the whole package.

## Reserved extensions and relationship to the live programme

Public auxiliary information is a later extension. Start, if needed, with an explicit pointwise conditional min-entropy guarantee and suitable conditional product laws. Average conditional min-entropy, smooth entropy and computational entropy require separate statements and loss accounting. Arbitrary prime-dependent source laws are outside the first target. A quantum DGS composition or a search analogue also needs its own scope check.

ENT1 neither interrupts nor enlarges the active FF/SV run. Its current objectives, assignments, protected period and deadline remain unchanged. Reconcile that run's final accepted evidence before scheduling ENT1; improvements may change its best starting theorem, while unresolved FF and source-hardness questions remain visible. See the [programme entry point](../PROGRAMME.md).
