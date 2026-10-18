# Exact Gaussian conditioning across ideal constraints

Status PROVISIONAL. This is an alternative constructive algorithm with an explicit acceptance cost. It does not assume independent selected stages. The finite CP-1 control is pending coordinator reservation.

Fix an integral overideal J of the target I (I subset J), with J eligible for the restricted DGS oracle. Suppose the oracle provides fresh centered D_(J,s) samples at a stated width s. Accept a sample exactly when it lies in I; if a nonzero short vector is required, also require x!=0. Every test is exact ordinary ideal membership. The complete single-attempt output law is

    Pr[output=x]=rho_s(x)/rho_s(J), x in I,
    Pr[FAIL]=1-rho_s(I)/rho_s(J).

Conditional on success it is EXACTLY D_(I,s). Excluding zero instead gives the exact nonzero-conditioned DGS with success mass

    p_nonzero=[rho_s(I)-1]/rho_s(J).                     (C1)

This avoids multiplying geometric approximation losses: the resulting Gaussian width remains s. It pays acceptance probability instead. In a smoothed regime s>=eta_epsilon(I), centered theta bounds imply

    rho_s(I)/rho_s(J) in
       [(1+epsilon)^-1 N(J)/N(I), (1+epsilon)N(J)/N(I)]. (C2)

Here the lower normalizer bounds use positive centered dual sums, so no artificial uniform-coset assumption is needed. At a width too small to produce nonzero points of I, the subtraction in (C1) is essential: a high zero acceptance probability is not a short-vector algorithm. Every nonzero x in I has ||x||_coef>=N(I)^(1/n), giving the separate upper bound

    p_nonzero <=Pr_(D_(J,s))[||x||>=N(I)^(1/n)]
               <=min(1,2n exp(-pi N(I)^(2/n)/(n s²))).   (C3)

An oracle call has not been made on I unless I itself is eligible. The only oracle input is the stated J. For T fresh exact attempts, success probability is 1-(1-p)^T. An approximate oracle with per-query conditional error epsilon_D gives at most T epsilon_D full-experiment error including failure; conditioning afterward on success requires its own division by the actual success mass. No exponentially small acceptance can be discarded from a polynomial-time claim.

For a chain J=I_0 superset I_1 superset ... superset I_r=I at a COMMON width s, exact fresh conditional rejection has

    p_j=rho_s(I_j)/rho_s(I_(j-1)),
    product_j p_j=rho_s(I)/rho_s(J).                    (C4)

Constructing each conditional sampler recursively therefore has the same expected number rho_s(J)/rho_s(I) of initial J draws. Splitting a large constraint into individually small-index constraints does not remove this cost. In the wide regime, the cost is approximately N(I)/N(J). A useful eligible prefix J can supply an exponential factor N(J), but a general input can still have a superpolynomial remaining ratio. For a large prime ideal I, the only eligible integral overideal is R, as already noted by C; this calculation adds the exact DGS output and nonzero normalizer rather than reopening that algebraic observation.

Cloning or resampling surviving particles does not create fresh independent draws from the next conditional Gaussian. Without an operation producing new points that preserve the earlier constraints, every final survivor belongs to the ORIGINAL finite particle set. With M initial iid points, probability of any nonzero point in I is at most M p_nonzero. This support argument is pointwise and does not depend on a fictitious product of selected-stage survival probabilities. A move that genuinely refreshes the distribution on I_j after the index exceeds the eligible budget is precisely an additional sampler/geometry operation that must be supplied.

Thus simultaneous-congruence rejection is a mathematically correct no-product-loss route to DGS on I, but its demonstrated running time is governed by (C1). The next repair would need a new conditional move preserving accumulated ideal constraints, or a coupling from several eligible composite-block oracle calls. Treating individual centered samplers as if they already provided that move would be an off-contract oracle use.
