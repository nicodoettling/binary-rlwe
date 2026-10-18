# A-HOM-END v1: a precise alternative oracle endpoint

PROVISIONAL. This note records a constructive reduction endpoint, not an algorithm for obtaining its missing relation. It arose in coordination with D's anisotropic R1 investigation. No experiment was run.

Take ordinary RLWE samples (a_0,b_0),(a_i,b_i) for i=1,...,m, with common uniform secret s and independent coefficient errors e_i of width tau. Conditional on a_0 being a unit, define R_i=a_i a_0^(-1) in R_q. Each R_i is uniform and independent across i conditional on a_0. Fix integer negacyclic lifts of the R_i.

Suppose a polynomial-time algorithm, possibly using the ASSUMED binary recovery algorithm, receives only the public multipliers and its own independent coins and returns a p-by-m matrix K over Z[X]/(X^n+1) with p>=1 such that:

1. K R=0 modulo q (an exact integer relation is stronger and also suffices);
2. K:R_q^m->R_q^p is surjective, equivalently every CRT evaluation has row rank p;
3. every row obeys sum_i ||K_ji||_1<=L for a declared deterministic L;
4. all checks succeed except with probability rho.

On success output C=K(b_1,...,b_m); on failure output uniform R_q^p. The unit check for a_0 is also public and may be included in the failure probability. No ideal offset or hint simulator is needed for this endpoint.

The planted identity is exact:

    K a = K R a_0 = 0 mod q,
    C=K e mod q.

The comparator is exactly iid uniform R_q^p conditional on K and all multiplier data, because the m designated responses are independent uniform and K is surjective. This requires K to be computed without reading the ordinary responses. Oracle queries constructed solely from multiplier data are permitted here; their own promised-law correctness is the separate missing obligation.

If every ordinary input error coefficient has absolute value at most E, then every output coefficient has absolute value at most W=E L. With error-tail failure delta_e and W<(q-1)/2, the test accepting iff all centered output coefficients lie in [-floor W,floor W] has advantage at least

    1-rho-delta_e-((2 floor W+1)/q)^(pn).

This statement counts every output coordinate and retains no hidden Gaussian augmentation. For a genuinely standalone public short-K algorithm, useful parameters would make the ordinary source easy, so that algorithm cannot be assumed as a hardness foundation. If the short-K algorithm USES the assumed binary recovery oracle with justified query laws, the very same identity is instead a legitimate hardness-reduction endpoint. That distinction is essential.

The relation sought by D's covariance cancellation satisfies K R=0 as an integer identity, which implies the modular condition above. D separately requires ring-linearity and active-coordinate surjectivity to preserve ideal points in its hint route. The direct ordinary-source test here needs full-coordinate surjectivity; it does not infer it from real full row rank.

What remains missing: a concrete way to obtain such K from the original single-ring binary recovery oracle. A high-density homogeneous relation may involve m independent ring-binary coefficient blocks (mn bits), while that oracle has only n binary secret bits. Sampling all but one block and asking it to solve the last reproduces the sparse fixed-multiplier event in A-ORACLE. Valid known-secret oracle queries supply a secret already available to the reduction. These observations do not exclude a different adaptive construction, but no such construction has been established here.
