# C finite OHCP v3 exact-version review

2026-10-17T21:11:48Z tool clock at start of final pass. PROVISIONAL nonblind adversarial review; no acceptance authority. No experiment.

Exact theorem SHA256 fae38a0173476c66321858b1e32a84551b0aaa1d028a4fb65924d9c37b01402e; proof SHA256 a34b4993783eea39d1eadfd08a47ef6ba06277f257607b5fb9957329455a8beb. Earlier v1 remains rejected by the immutable logarithmic-scale countercontrol; no acceptance transfers between versions.

## Disposition

The analytic reduction and adaptive error accounting survive this review, but the exact v3 finite worst-case polynomial-runtime claim is not yet justified. Section7.3 imports exact uniform-integer binary rejection, whose retry count is unbounded. Its expected polynomial runtime is insufficient for the stated worst-case bound. This is a local implementation correction, not an endpoint counterexample.

For each sample j, at most n*L_j scalar proposals are needed, where L_j=ceil(40 K_j log(16/nu_j)). Each uniform integer draw has acceptance probability greater than1/2. Cap its binary rejection at R_j=ceil(log2(16 n L_j/tau_j)), with a fixed fallback. The conditional union bound adds at most tau_j/16. This fits the existing numerical slack and preserves exact integral multipliers. No scalar sampler claims exact Gaussian output; the fallback belongs to its charged approximation. Both global orientations should also enforce the published time and query-description cap, since the incorrect orientation need not satisfy the oracle promise. Basic domains and efficient parameter representations must be explicit.

## Analytic checks performed independently

1. Full discrete/continuous completion retains rho_P and rho_V, with normalized density ratio equal to their ratio. P>=2 eta^2 I under the stated residual guard. The per-sample TV bound epsilon/(1-epsilon) is valid.
2. Multiplication cancellation is exact for every sampled integral multiplier. Fixed widths on nuisance coordinates do not alter radiality in the selected complex pair. Same finite rounding kernel may follow all continuous comparisons.
3. The shifted center2+e_j/d0 has norm in[1,3], including zero coordinates. Starting-gap loss is below delta/16; the single common orientation works for all pairs. The independent algebraic-norm/packing proof in independent-smoothing-control-v1.md gives the asserted full-Haar smoothing bound.
4. Parameters are chosen without a v0/kappa cycle: v0*d0=h0 is fixed before Q_* and epsilon0. Confidence kappa+log4 weakens the verified profile conditions; Q_*=n ceil(T_H) covers two orientations times n/2 pairs. Exact finite scalar and grid errors use a single global sample counter and conditional coupling, not an unjustified product of marginal success probabilities.
5. The local comparison oracle is continuous only within |h_j|<=8d0 and agrees with the actual exact-multiplier oracle elsewhere. It has a uniformly bounded error at every possible query and needs no query-confinement assertion. The center ball and origin Lipschitz ball are contained in this guard.
6. The Gaussian grid sampler is compared to the exact rounded law by a common uniform-variable coupling. Finite output is never asserted TV-close to an unrounded continuous Gaussian. Mean precision is scaled to actual multiplier size. Canonical/coefficient widths differ by sqrt(n); exact rational membership and rounding recover the point, not merely an embedding approximation.
7. Both-sign failures and numerical errors are summed over conditional kernels. No average-J advantage is promoted to every-J decoding; the restricted-family-to-standard-worst-case edge remains OPEN.

## Primary-source verification

Indexed primary author PDF, https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf, retrieved independently through web search on2026-10-17 (tool reference turn242search12), gives Definition4.3 and Proposition4.4. The radial promise is restricted to the center neighborhood. The profile requirements are an excursion at a nonnegative scale, global exponential decay, and a Lipschitz bound. These support the local extension and shifted-center proof. The published polynomial runtime is imported symbolically; no explicit exponent or separate implementation theorem has been inferred.

Await coherent immutable v4 for fresh exact-byte review of the finite repair. This report does not certify v3 as written.
