# Restricted ideal sampling: final work-package report

**The computational-hardness foundation was not achieved.** This bounded package is complete, with three internally reviewed auxiliary results. The original native goal remains **active and unfinished**. After the first tests and the45-minute decision, the tested constructive routes had no effective standard-hardness bridge; proportionate reviews and repairs were completed, and the package closes early. No successor is scheduled.

## Accepted results and exact scope

1. **M1-USEFUL-v2: constructive classical sampling criterion.** From a represented rational basis with maximum Gram–Schmidt length at most s/u, where4exp(-piu²)<=eta/(32n), an all-input bounded classical bit algorithm samples within TV eta of ordinary D_(J,s). Conditional scalar normalizers, finite precision, capped draws and global-zero failures are charged. Upper-column HNF diagonal h and additive quotient exponent e give effective criteria s>=hu and s>=eu. Polynomial numeric index D permits a charged O(D) collision search and an effective short-GS basis; polynomial encoding of D alone does not.

At the **actual inherited width**

    W=nq/(sqrt(2)d0)=32sqrt(2)n²k chi q/(delta ell²),
    d0=delta ell²/(64nk chi), ell=ceil(log2(2nk)),
    sigma=8n²ceil(sqrt(kn))ell⁴, q>=n sigma,

with the explicit inherited odd-prime q congruent1 modulo2n, eta=2^(-4n),u=4n works. This simulates all polynomial-index eligible calls and every ordinary-basis call with h<=W/(4n), including e<=W/(4n). The explicit exponential-index family J=(3,X^(n/2)+X^(n/4)-1) has norm3^(n/2)<=2^(4n/5), exponent3, and is covered. Adaptive **classical** transcript losses add conditional eta_j, or eta_j+alpha_j against another sampler's error alpha_j. Arbitrary coherent access and arbitrary precision at fixed width are excluded. This constructive theorem was reviewed; the experiments are finite controls, not a complete software implementation of the sampler.

[Statement](coordinator/M1/theorem-only-v2.md), [proof](coordinator/M1/proof-v3.md), [full recheck](criticism/RFR2/report-v1.md), [source/complexity](criticism/RFR2/source-complexity-v1.md), [fresh blind report](criticism/FBR2/report-v1.txt), [seal](criticism/FBR2/seal-v1.json), [acceptance](coordinator/m1-acceptance-v2.md).

2. **M2-TRANSFER-v1: an integral linear map already contains a short object.** For the power-two tower R subset S, prime I and prime J above I, any supplied nonzero integral linear T:S->R with T(J) subset I can be decomposed in polynomial bit time to obtain either nonzero a in ISJ^-1 or nonzero y in I, with norm at most min(n||T||op,sqrt(n)||T||F). This is a precise restriction on a proposed map-based route. It supplies no algorithm finding T and excludes rational, nonlinear and merely probabilistic containment.

[Statement](workers/A/linear-transfer-theorem-v1.md), [proof](workers/A/linear-transfer-proof-v1.md), [nonauthor full review](coordinator/reviews-A/full-proof-review-v1.md), [source/complexity](coordinator/reviews-A/source-complexity-review-v1.md), [fresh blind report](criticism/FBR1/report-v1.md), [seal](criticism/FBR1/seal-v1.json), [acceptance](coordinator/ab-acceptance-v1.md).

3. **M3-ENTROPY-v1: full-observation guessing controlled by the exact cube image.** For fixed full-rank J subset Z^n, uniform binary S independent of exact G~D_(J,t), let C_J be the number of occupied binary residue classes. For every r>0,

    C_J/2^n <= p_guess(S | S+G)
      <= min(1,(C_J/2^n) exp(pi n/(4r))(1+r/t²)^(n/2)).

Taking r=t gives overhead exp((pi/4+1/2)n/t), and t=2n²ell gives exp((pi/8+1/4)/(n ell)). This controls the entire unwrapped observation, which can reveal more than the residue. Metadata is allowed only if the full conditional product law survives. For a power-two cyclotomic integral ideal, C_J<2^n implies a ternary collision, N(J)<=n^(n/2), and a basis of operator norm<=n², **as existence statements**. No efficient collision search, source hardness, or changed-premise composition follows automatically.

[Statement](workers/B/theorem-only-v1.md), [proof](workers/B/proof-v1.md), [nonauthor full review](workers/A/b-review/full-report-v1.md), [source/complexity](workers/A/b-review/source-complexity-v1.md), [fresh blind report](criticism/FBR1/report-v1.md), [acceptance](coordinator/ab-acceptance-v1.md).

## Computational direction, failed routes and remaining gap

The inherited accepted conditional direction remains

    bounded binary-recovery code -> fractional-source decision
    -> finite periodic-Gaussian decision -> BDD(qJ^-1)
    -> finite quantum ordinary DGS(J,W), on the SAME eligible J.

The original source uses a fresh uniform coefficient-binary secret shared across k samples and independent coefficient discrete-Gaussian integer errors of width sigma; metadata is fixed in both worlds. Eligible J is integral in the power-two ring, N(J)<=2^(rho n),rho<1, gcd(N(J),q)=1. The full positive delta formula and representation promises remain exactly those of the [historical same-J theorem](../brlwe-standard-hardness-20261017-astra-ultra/workers/RF4/same-j-composition/same-j-theorem-only-v1.md). The two complete GP endpoint charges are Delta_B+kn nu+eta_cap and kn nu+eta_cap; the implemented gap charges3kn nu+2eta_cap once. The final ordinary-DGS error is at most min(1,epsilon+2sqrt(p)+E_n), with p=(n/2)exp(-kappa)+zeta and all finite parameters as frozen there. Each output uses at most2Q_* coherent executions of the supplied bounded recovery code, plus actual compilation, setup, arithmetic and serialization costs. A classical answer service does not supply that code. No source sample budget is silently equated with the recovery or quantum query budget.

M1 supplies classical samples in its sufficient regime; it does not reverse that implication into a binary recovery algorithm. For prime J above p, h=e=p. Hence any still-unclassified eligible prime case must have p>W/(4n) and f log2(p)<=rho n when N(J)=p^f. Such a case may still have another efficiently found short basis. Large characteristic is not hardness evidence. See the separately reviewed [remaining-family audit](coordinator/M1/remaining-family-v2.md) and its [version reconciliation](coordinator/M1/remaining-family-version-reconciliation-v1.json).

For M2, the explicit LLL complementary-multiplier construction yields only the general certificate with factor2^((m-1)/4); after the actual W_m and eligibility D^(1/m)<2 are charged, it does not certify the desired polynomial approximation. This is a limitation of that certificate, not a lower bound on actual LLL output. The planted mapped law is a normalized fiber sum on the actual image, while the uniform comparator is uniform only on the actual image quotient, which may be proper. A supplied short multiplier, Minkowski existence, or zero/nonzero projection shortcut does not create the missing algorithm. [First-test report](workers/A/report-v1.md).

The **provisional companion** norm289 family has D=289^(n/8)>2^n and C_J=176^(n/8), so its residue guessing is(11/16)^(n/8), with the accepted full-law overhead above. Its explicit five-term generator F and exponent17 also make it an easy public-source control. Multiplying by F before centered lifting gives planted acceptance at least1-2n exp(-pi ell²), whereas the full uniform comparator accepts with probability[min(q,2floor(sqrt(10)ell³)+1)/q]^n. This companion has favorable nonauthor review and exact arithmetic controls; it has not been promoted to a separately blind-certified hardness theorem. The [changed-premise composition audit](workers/B/downstream-compatibility-v1.md) also remains provisional. [Family and source test](workers/B/concrete-family-v1.md).

No established standard-RLWE/Order-LWE or arbitrary worst-case ideal-family connection with compatible parameters was obtained. No practical security level, absence-of-attacks claim, or literature-priority claim is established. Exact directions and both endpoints are recorded in [reduction-attempts.md](reduction-attempts.md); source imports and representation limits are in [source-comparison.md](source-comparison.md) and [parameter-table.md](parameter-table.md).

## Audit and experiments

Two specification defects were preserved before repair: the scalar-versus-global fallback branch, and the omitted explicit prime-q prerequisite. The latter permits composite q82944 under the old displayed numbers; it does not satisfy the inherited same-J prime premise. Theorem-v1 remains rejected as a standalone packet; theorem-v2/proof-v3 received fresh full/source and fresh blind gates. FBR2 also checked that the strong W lower bound, rather than only W>4n sqrt(n), covers the exponent3 family at n4.

All151 inherited regression IDs retain exact provenance;13 new entries bring the current registry to164. CP-1 was reconstructed on all160 original atoms, retaining21/2000>1/100. [Current regression gate](coordinator/regression-gate-v3.json). Structural hashes and links are checked separately from proof certification. Same-model role diversity is correlated scrutiny, not statistical independence or formal verification.

| Bounded local job | Exact scope | Wall / peak RSS |
|---|---|---|
| M1-FV1 |80 finite Gaussian laws, HNF family controls, full CP-1 |0.20s /13312KiB |
| B-FV1 |40 exact Gaussian guessing cases with rigorous tail bound;304 degree8 representatives |0.49s /19456KiB |
| A-LIN-FV1 |86 maps,240 components,13747 quotient inputs |0.18s /12288KiB |
| B-M1-FV1 |2048 adaptive fallback tapes, HNF-order/collision controls |0.05s /21504KiB |
| A-BFAM-FV1 |Independent256-vertex family enumeration |0.02s /10240KiB |
| M1-Q-FV1 |Preserved composite counterexample and four prime/width cases |0.02s /12288KiB |

All six exited0, including their expected negative controls. They are falsification/arithmetic evidence, not asymptotic-hardness experiments. Code, exact inputs, deterministic seeds, commands, complete outputs, tails, limits and resource receipts are in the [experiment registry](experiments/registry.json). No job exceeded512MiB address-space allowance or120s wall allowance; no aggregate memory containment is claimed.

## Programme and operational close

**HOLD further autonomous construction until a concrete new ingredient is available.** Ranked next targets: (1) an established hard family in the remaining large-characteristic regime with an effective map and both endpoints; (2) an effective complementary multiplier or a quantified non-integral/nonlinear route outside the integral-map scope; (3) an entropy-compatible family with established computational hardness that survives the public short-witness test. A hidden-relation assumption by itself is not the required standard foundation. The [45-minute decision](gate-45m.md) and [programme ledger](programme-decisions.md) preserve the reasons.

The service began2026-10-21T05:34:44.878177Z; discovery cutoff07:49:44.878177Z, workers/experiments stop08:19:44.878177Z, final checkpoint08:29:44.878177Z, graceful08:33:39.878177Z and hard08:34:44.878177Z were never reset. Peak observed concurrency was3 total; five worker/referee threads were used sequentially, all reporting Astra ultra. Standard/default is supported by launch configuration, not server billing telemetry. All workers have completed and no experiment remains. External service/process cleanup has not been observed; the cap sidecar still reports running with its original update timestamp.

The45-minute gate was durably issued about46s late. One core interval was about11m13s, exceeding the ten-minute target by73s; this is recorded, not reconstructed as on time. Frozen evidence and historical files are preserved. No new goal, goal pause/completion, service restart, external message, installation, commit/push or successor launch was made.

The saved final native receipt records active goal01a14b7b-9e45-7b70-b46d-0bf70e17f2e2 with unchanged objective. Native usage at that receipt increased by958817 tokens and4452 seconds from this package's baseline; these are native counters, not weekly quota percentages or billing estimates, and later finalization may not be included. [Usage receipt/delta](coordinator/goal-usage-delta.json). Scientific foundation, bounded-package delivery, process exit and native-goal status are separate facts; [shutdown.json](shutdown.json) and [resume.md](resume.md) record them explicitly.
