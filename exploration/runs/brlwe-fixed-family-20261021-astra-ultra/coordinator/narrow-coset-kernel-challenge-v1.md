# Narrow-coset constructive challenge, first exact boundary

The concrete proposal is to retain the B-GP public map but replace its smoothing-width lower bound by a narrow width, compensating by taking the continuous source width smaller. The existing theorem does not license this replacement. A scalar/ideal coset calculation identifies the missing normalization.

Let J be the unique prime above2 in R=Z[X]/(X^n+1). In coefficient coordinates J={z in Z^n:sum z_i even}, hence Lambda=J^-1=Z^n union (Z^n+(1/2,...,1/2)). Its index is2, eligible for any fixed rho>0 for sufficiently large n. At input y=0, the exact uniform-coset bridge chooses either coset with probability1/2 and then samples the product discrete Gaussian within that coset at width r. Write A=rho_r(Z), B=rho_r(Z+1/2). Its unreduced law is therefore

    (1/2) D_(Z^n,r) +(1/2) D_(Z^n+(1/2)1,r),

whereas the desired D_(Lambda,r) has coset weights A^n/(A^n+B^n) and B^n/(A^n+B^n). Scalar covariance agreement cannot erase these weights.

The coset itself is not well-defined after reduction modulo qLambda when q is odd, so one may NOT simply carry the unreduced coset TV bound to the exposed experiment. A valid exposed test is the event that the quotient element equals0. Put A_q=rho_(r/q)(Z), B_q=rho_(r/q)(Z+1/2). The bridge and desired probabilities of this event are exactly

    p_bridge = (1/2)(A_q/A)^n +(1/2)(B_q/B)^n,
    p_DG = (A_q^n+B_q^n)/(A^n+B^n).

For r=n^-c with fixed c>0 and any odd q>=3, A,A_q tend to1 rapidly enough that A^n,A_q^n tend to1; B^n tends to0, and (B_q/B)^n tends to0. Thus p_bridge tends to1/2 and p_DG tends to1. This is an exact modulo-quotient normalization obstruction at the point input y=0. It does not assert that a continuous Gaussian source of positive width is a point mass, nor prove impossibility for all normalized kernels. A positive-width family claim would require a separately quantified continuity/conditional-kernel estimate.

A proposed repair is to choose the coset using its theta weight rather than uniformly. At y=0 this gives the desired Gaussian exactly. But the original proof that the uniform torus endpoint maps to a uniform public ring multiplier used a uniform quotient coset and translation-equivariant scalar kernel. Reweighting one endpoint is not a proof for the other. The new kernel would need to normalize the whole lattice theta sum at each y, preserve quotient equivariance, and charge an efficient sampler for exponentially many cosets from the ordinary ideal basis. Enumeration is available on numeric-polynomial index families already classified by the direct source algorithm; that does not solve the general source bridge.

A different nearest-lattice-cell rounding kernel is translation-equivariant and has the right uniform endpoint, but evaluating that partition from an arbitrary ordinary basis at a useful capture radius is a new algorithmic obligation. Assuming a BDD-quality rounding oracle would be circular. Coordinate rounding using a supplied ordinary basis can be implemented, but its capture radius must be computed from that actual basis and cannot be replaced by the existence of a short basis. No fixed-family reduction follows from this boundary calculation.
