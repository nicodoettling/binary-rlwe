# Direct decision binary RLWE — run report

**Positive result: FIXED-MAIN-v2 is accepted within its explicit scope.** The [exact-version acceptance](coordinator/acceptance-v1.json) binds the statements, proofs, dependencies, full and blind reports, repairs and regression checks. The bounded package is delivered and the new native mathematical goal is COMPLETE. The source-family and parameter restrictions below remain binding.

## Result and its exact scope

The accepted theorem gives a classical bounded-distance decoder for J^-1 from a decision binary-secret rank-one RLWE distinguisher at ONE prescribed target modulus q0. Here R=Z[X]/(X^n+1), n is a power of two, and the supplied ordinary integral ideal satisfies N(J)<=2^(rho*n) for fixed rho<1. The source family restriction is retained. No short basis, trapdoor, or ideal Gaussian sampler is supplied.

The target has one uniform coefficient-binary secret shared across k0 samples, independent uniform public multipliers, and independent coefficient D_(Z,sigma0) errors. The comparator keeps the same public multiplier and metadata law and replaces only responses by independent uniform elements. D0 is bounded on every valid input and every random tape. Its promised absolute advantage is epsilon_*; if it receives J as metadata, the premise is pointwise for that same J.

The exact statement and proof are [FIXED-MAIN-v2](coordinator/fixed-main-statement-v2.md) and [its proof](coordinator/fixed-main-proof-v2.md). Its finite guards include

    sigma0 >= 8*k0*n*(n/2+2)/epsilon_*,   q0 >= n*sigma0.

Together with the specified auxiliary-prime, completion and implementation guards, the decoder has inverse-polynomial radius in a nonempty asymptotic regime and success at least1-17*zeta/16. It makes at most

    M*Q_* * ((n+1)*Ncal + Qmax*Ntest)

calls to D0. The exact definitions, all physical sample counts, finite sampling caps and full input/evaluation/oracle costs are in the statement and its AM-MAIN-v3 dependency. Enumeration costs are charged in auxiliary moduli in VALUE; the fine-grid parameter P is charged in bit length. Neither a huge numeric P nor an arbitrary enormous kappa is described as polynomial value.

For fixed integers b>=0,c>=1, one compatible family has k0<=n^b, epsilon_*=n^-c, sigma0=n^(b+c+4), and polynomial-value q0>=n*sigma0; q0=n^(b+c+6) is an example. Auxiliary list size and lower bound are M=ceil(2^24*n^(2c+4)) and Qmin=ceil(q0*n^(b+2c+12)). Construct the list before deriving the extractor's sample count. All numerical guards hold for sufficiently large powers-of-two n, uniformly over the eligible ideals, with an explicitly polynomial choice of kappa. The fixed target may be composite; the auxiliary moduli are distinct split primes.

The separately reviewed [nonvacuity and radius note](coordinator/nonvacuity-and-radius-note-v1.md) shows that the finite oracle premise is nonempty using an explicitly exponential-time test; that cost is charged. It also shows the shortest nonzero canonical-infinity length of J^-1 lies in (1/2,1], so the inverse-polynomial radius is an inverse-polynomial fraction of the source separation. Neither observation establishes efficient distinguishing or source hardness.

This covers the stated sample/advantage/noise window. It does not assert that one fixed noise exponent handles every polynomial sample count and every inverse-polynomial advantage. It also does not prove that an efficient promised distinguisher exists, that the restricted ideal family is hard, standard unrestricted worst-case hardness, practical parameters, or a quantum sampling composition.

## How the bridge works

1. **Extract one selected CRT value.** An ordinary decision distinguisher is converted into an extractor returning one correct root/value pair with controlled success. Calibration and test banks are disjoint; reuse within each bank is handled by simultaneous concentration and union bounds. Every raw sample in the complete bank retains the same binary secret. The number of raw samples and the larger number of distinguisher executions are counted separately.
2. **Bound selected-value guessing on the fractional source.** A full-observation Gaussian envelope gives a selected-functional guessing bound with both normalizers retained. Across distinct auxiliary split primes, every root collision of a nonzero binary difference consumes a prime factor of its nonzero algebraic norm. This bounds average selected-value success without assuming uniform binary cube fibers or independent CRT error coordinates.
3. **Use the inherited finite decoding machinery.** A-FRAC's complete joint-law completion, B-GP's finite source bridge and the exact C8 hidden-center decoder yield a favorable auxiliary modulus. The algorithm runs the full bounded schedule at every retained modulus and verifies candidates by exact ideal membership and rational coefficient distance. A wrong-modulus call cannot pass with a wrong candidate. The inherited PRS17-inspired machinery is reused, not claimed as new.
4. **Transfer one fixed target to the auxiliary list.** MR-v1 scales coefficient representatives and uses translation-equivariant rounding. Conditional on the entire public bank and the shared secret, it controls the rounding shift and explicitly compares discrete Gaussian laws. The two-endpoint signed-gap loss is at most k0*n*(7*q0/q+(n/2+2)/sigma0). With the guards, every auxiliary modulus retains the same gap orientation. AM-MAIN-v3 explicitly permits the required widths sigma_q=(q/q0)*sigma0 and charges their finite sampler bit costs.

Every D0 execution uses q0. Its actual inputs include transformed and hybrid samples; the advantage promise is invoked only for the exact target experiments, after paying the stated statistical transfer loss. There is no claim that every execution receives exact planted Gaussian samples.

Scaling and rounding are established modulus-switching techniques; the present contribution is their explicitly bounded use in this particular ring/shared-secret/source composition. The primary [BLP+2013 paper](https://arxiv.org/pdf/1306.0281) also explains why output distributions and resource-dependent parameter regimes require care. The auxiliary-prime construction uses the effective least-prime theorem from [Xylouris, Theorem1.1](https://www.impan.pl/shop/en/publication/transaction/download/product/83078); it does not use a factorial modulus with merely polynomial encoding length.

## Other routes and preserved failures

DD1 found an explicit J=R response witness against a blanket small fractional decision-gap statement. Conditional centering leaves that gap unchanged; broad response masks scale both gaps; a large-q lattice-tube alternative has a restricted exponential-value-q scope. Those calculations do not prove that all direct-decision reductions fail. The accepted construction instead tests extracted actual-secret information through a selected functional.

DD2 checked PRS17's uniform secret randomization against the binary promise and explored integral cancellation, affine cube symmetries, CRT projection and digit alternatives. The integral-cancellation construction requires an ideal sample that already enables a stronger elementary decoder. Unknown cube translates and a scalar variance argument do not establish the required full binary/discrete ring law. These are scoped mechanism outcomes, not an exhaustion certificate.

The [attempt ledger](reduction-attempts.md), worker reports and [programme decisions](programme-decisions.md) preserve the constructions, alternatives and source overlap. The separate arbitrary-ideal foundation remains open.

## Review and evidence status

FULL1 and BLIND1 sealed complete reviews of the earlier AM-MAIN-v2. They supported the finite core but rejected its literal all-parameters-polynomial-value sentence. They also required an explicit optimal-success definition, a polynomial kappa choice, complete input/oracle costs, and correct treatment of the impossible exact advantage1 endpoint. AM-MAIN-v3 and SFUNC-v2 repair those points.

FULL2 completed the full proof, primary-source and complexity audit; BLIND2 independently reconstructed the result from a clean statement/definition/source packet. Both sealed their reports before the repair recheck. The coordinator and both reviewers rejected FIXED-MAIN-v1's final execution-law sentence. Version 2 preserves the numerical proof and distinguishes the exact target promise from actual transformed/hybrid calls. Both reviewers separately checked the exact revised bytes and sealed their acceptance. The original rejected versions and reports remain unchanged. Same-model agreement is correlated scrutiny, not formal verification.

All 164 inherited regression IDs, source pointers, entry hashes and verdict provenance are retained and reconciled for the accepted construction, along with 39 new entries. Root integrity checks verified all six review seals and the accepted dependency bytes. Historical counterexamples remain valid in their original scopes; unrelated rejected mechanisms are not revived. Twelve local experiment jobs were preregistered: eleven completed successfully; MR-FV1 failed only while formatting a large rational for logging, and its code/output/failure were retained before the separately registered MR-FV2 repair. The longest job took 52.0 seconds with 48 MiB observed maximum RSS. All jobs had 120-second limits and 512 MiB address-space caps; no aggregate memory cap is claimed. These are finite falsification checks, not executions of the full conservative decoder or proofs of asymptotic claims. See [experiment registry](experiments/registry.json) and [reconciliation](reconciliation.md).

## Run, goal and cleanup status

The service clock began2026-10-21 at12:19:00.281989UTC. The45-minute gate was nonterminal and was recorded late at13:08:42UTC; original deadlines were retained. The configured team used Astra ultra with explicit default service tier, root plus at most two active children, recycling completed slots. Configuration evidence is not backend billing telemetry.

The mathematical objective is achieved by the accepted restricted-family reduction, rather than by a negative investigation or an auxiliary theorem alone. The PLAN permits an early finish for reviewed achievement; no branch-exhaustion claim is made. The [native completion receipt](coordinator/goal-completion-receipt.json) reports COMPLETE, 1,715,836 tokens and 6,007 seconds (1 h 40 min 7 s). The [run-relative delta](coordinator/native-usage-delta.json) uses the new goal's zero baseline; these counters are not a quota percentage or backend billing telemetry. The [early-achievement certificate](coordinator/early-achievement-certificate.md) records the positive termination condition at 100.26 service minutes.

All child assignments and twelve experiments have finished. The [process observation](coordinator/shutdown-observation.json) found no registered experiment process in the visible namespace. The cap sidecar still reported the enclosing service running while the coordinator recorded delivery; the cgroup contains entries not mapped into this sandbox PID namespace. Post-exit service cleanup has not been observed. Mathematical achievement, package delivery, native goal completion and process cleanup are therefore recorded separately. No successor or automatic extension is authorized.
