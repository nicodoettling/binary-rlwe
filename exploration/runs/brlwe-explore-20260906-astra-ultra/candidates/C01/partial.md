# C01 investigation notes

Started 2026-09-06 10:12:55 UTC; bounded investigator deadline 10:47 UTC. No experiments requested or run. Only assigned primary-source checks and hand calculations.

The scout's exact conditional collision identity checks algebraically. The conditional bit probability is based on wrapped coefficient noise. Averaging its squared characteristic function yields `1-beta sin^2`, with beta equal to four times the averaged posterior bit variance. For the prescribed binomial quotient the coefficient blocks remain independent, giving an exact d-th power of the scalar Fourier sum. This is a joint averaged collision statement about `(S mod J, Y)`, not a pointwise guarantee for every leakage y and not an RLWE transcript result.

Primary source opened directly: Breuillard–Varju arXiv:1909.09053v2, printed pp.7–9, https://arxiv.org/pdf/1909.09053 . Theorem 5 is unconditional and uniform in every prime, every two-or-more-point step law on that prime field, and every multiplier meeting its order threshold. It explicitly allows the step law to vary with the prime; the fixed-integer-law restrictions belong to other theorems. Accuracy parameter is delta in (0,1/2). The time bound contains `(1-||mu||_2^2)^(-1) log(q/delta) log q (log log q)^5`; order threshold is `C log q log log log q`. Lemma 6 and the proof on pp.8–9 explain the orbit energy and Parseval step; no GRH or typical-multiplier restriction is used here.

Independent width observation: beta >= 1-TV(W_tau,q, shifted W_tau,q) >= 1-D_tau(0). The first inequality uses `2xy/(x+y) >= min(x,y)` and the second uses contraction under wrapping plus telescoping of the symmetric unimodal discrete Gaussian. Thus every fixed tau_0>0 gives a uniform positive beta lower bound for all tau>=tau_0 and all odd q. This strengthens the scout's constant-width witness without changing target sigma.

The public ideal `I=(g)`, where `g=(X^n+1)/(X^d-a)`, has d-dimensional coefficient blocks of geometric codewords. For a public mask `A=gP+F` with coefficient-small F, enumerate each possible scalar P_j in F_q and check the block. Complexity O(nq), so polynomial q makes the naive source assumption false in the small-noise regime. The obstruction persists if a is hidden within the polynomial-size family. It does not rule out all public samplers.

Remaining checks: formal asymptotic quantifiers and finite-sample distances; exact Order-LWE/HLBDD source definition, noise hypotheses, and family mismatch; identify a next lemma that tests the bridge instead of repeating a favorable mixing calculation.

## Completed dossier, 10:26 UTC

The remaining checks above are now written in [../C01.md](../C01.md), with [calculations.md](calculations.md) and [source-checks.md](source-checks.md). Main finding retained as extraction only. The exact asymptotic is uniform over qualifying q,a,L and every tau>=tau_0; the finite beta-dependent mixing criterion is retained for shrinking tau. The sampler attack allows arbitrary P and correlated errors whenever a coefficient-small box holds with high probability, and handles hidden a by polynomial enumeration.

Additional source check: Order-LWE Definition 2.13 requires a negligible swallowing ratio, and Lemma 7.7 hybrid H3 explicitly relies on superpolynomial q. Active-coordinate failure for uniform masks is exactly `1-(1-1/q)^d`; polynomial q does not make it negligible automatically. These are recorded as composition gaps, without auditing the older proof.

One future lemma is stated for the wrapped discrete additive completion `US+FY+H`, asking whether independent H and a narrow target noise law force F back into the coefficient-small neighborhood already attacked. No effort to prove that further lemma, no experiment, and no broad search were undertaken. Dossier spelling, notation, formula signs, sample accounting and local links checked by inspection.
