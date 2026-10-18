# B-IDEN-GP v1: explicit periodic-Gaussian to fractional-ideal source reduction

Status: PROVISIONAL author proof, not certified. This is a constructive endpoint bridge. A standard hardness theorem for its required low-index ideal family is still missing. C is checking primary periodic-lattice hardness sources independently.

## Frozen experiments and direction

Use coefficient Euclidean space R^n. Let Gen sample one integral ideal J with D=[R:J], gcd(D,q)=1, and let Lambda=J^-1. Its coefficient determinant is1/D and Z^n is contained in Lambda. Publish an ordinary rational basis of J (HNF is sufficient), not a short basis or Gaussian trapdoor. All sample counts below refer to the same sampled J.

The periodic-Gaussian input experiment GP(Gen,q,w,k) is

    planted: (J, Y_1,...,Y_k), Y_i=G_i mod qLambda,
             independent G_i~continuous D_w on R^n conditional on J;
    comparator: same J, independent Haar-uniform Y_i in R^n/qLambda.

The fractional-ideal source FG(Gen,q,s,k) is

    planted: (J, A_1,...,A_k), independent a_i~D_(Lambda,s),
             A_i=a_i mod qLambda, identified with R_q;
    comparator: same J, independent uniform A_i in R_q.

This is a known-ideal decision problem with centered spherical coefficient Gaussians. It is not search BDD with arbitrary promised targets, nor standard RLWE. A hidden-J FG distinguisher can be used by discarding J from these outputs; hardness of known-J GP under the same Gen would then suffice in the correct direction. Revealing a short basis of J would invoke the separate public-basis obstruction.

Let r>=eta_epsilon(Z^n), w>0, and s=sqrt(w^2+r^2). The public reduction below turns an FG distinguisher of advantage delta into a GP distinguisher with advantage at least

    delta - 2k epsilon/(1-epsilon) - delta_num,

where delta_num is the total implementation distance of the one-dimensional Gaussian samplers and continuous-input representation. Sample count k is unchanged. No ideal-family randomization is performed by the reduction.

## Public sampler

Compute the finite group Lambda/Z^n (order D) by rational ideal arithmetic. Given any representative y of Y in R^n/qLambda:

1. Sample u uniformly from Lambda/Z^n and use its coefficient representative in [-1/2,1/2)^n.
2. Sample E from the product integer Gaussian D_(Z^n,r,y-u), and set a=u+E.
3. Output a mod qLambda, using the canonical isomorphism to R_q induced by inclusion R subset Lambda and gcd(D,q)=1.

This uses only independent scalar Gaussian samplers and ordinary ideal arithmetic. D may be exponentially large: sampling uniform invariant factors uses O(log D) random bits and does not enumerate the quotient. There is no short basis of J in the implementation. Bit complexity is polynomial in the input basis, n,k,log q,log D and numerical precision, provided the input torus coordinates have the corresponding bounded finite representation. The mathematical ideal-real-input model and its finite-precision implementation are distinguished by delta_num; no exact real Gaussian is claimed to run on a finite machine.

## Exact comparator, including the actual coset sampler

The actual kernel Q_y in steps1–2 is Lambda-translation equivariant. For lambda in Lambda, translation permutes the quotient cosets u. The change between chosen representatives is an integer vector, and the conditional product integer Gaussian translates by that vector. Therefore

    Q_(y+lambda)(a+lambda)=Q_y(a).

In particular the output class modulo qLambda is independent of which representative y was chosen. Haar measure on R^n/qLambda is invariant under the transitive translation action of Lambda/qLambda. The output law must therefore be exactly uniform on that finite quotient. This argument applies to the actual uniform-coset sampler, not just an ideal Gaussian kernel. Conditional on J, independent comparator inputs and local coins give independent uniform outputs. The full joint comparator with J is exact; finite-precision departures are charged separately by delta_num.

## Two normalizers in the planted comparison

Write rho_r(x)=exp(-pi||x||^2/r^2). Poisson summation at r>=eta_epsilon(Z^n) gives, for every c and every coset u,

    rho_r(Z^n+u-c)/r^n in [1-epsilon,1+epsilon].

Let P_y=D_(Lambda,r,y) be the ideal lattice-Gaussian kernel. Its coset probabilities are proportional to these theta values. Relative to the uniform distribution on the D cosets, this is a reweighting by factors in [1-epsilon,1+epsilon], divided by their ACTUAL expectation. Conditional within a coset, P_y and Q_y agree. The elementary reweighting bound therefore gives

    TV(P_y,Q_y)<=epsilon/(1-epsilon), uniformly in y,J.

Now start with unwrapped G~continuous D_w and use the ideal kernel P_G. Its joint density/mass is

    rho_w(y) rho_r(a-y) / [w^n rho_r(Lambda-y)].

Consider instead the normalized joint law proportional to rho_w(y)rho_r(a-y), for a in Lambda and y in R^n. Integrating y gives a marginal exactly D_(Lambda,s), s=sqrt(w^2+r^2), by completing the square. Its Y marginal is continuous D_w reweighted by rho_r(Lambda-y), divided by the ACTUAL continuous-Gaussian expectation of that theta function. Because Lambda contains Z^n, Lambda^* is a sublattice of Z^n and r>=eta_epsilon(Z^n) implies

    rho_r(Lambda-y)/(r^n/det Lambda) in [1-epsilon,1+epsilon]

uniformly in y. Thus the second reweighting changes the full joint law by at most epsilon/(1-epsilon). The conditional a|y is exactly P_y in both joint laws. Combining the two steps and then reducing modulo qLambda gives the claimed per-sample planted distance 2epsilon/(1-epsilon). This proof does not drop any center-dependent theta normalizer. Conditional-on-J product coupling gives the stated k-sample loss; averaging over the actual Gen law preserves it.

## Scales and the remaining foundation

After dividing torus representatives by q, GP is continuous D_(w/q) modulo Lambda=J^-1. Canonical widths are sqrt(n) times coefficient widths. Thus an imported theorem in the canonical embedding must be evaluated at normalized radius sqrt(n)w/q, with the actual inverse-ideal family and its public ordinary basis.

For D<=2^(rho n), every nonzero a in J^-1 has coefficient norm at least D^(-1/n)>=2^(-rho): the ideal containment (a) subset J^-1 implies |N(a)|>=1/D, and AM–GM gives ||a||_coef>=|N(a)|^(1/n). This is a geometric observation, not an efficient decoding algorithm. An ordinary HNF basis does not automatically give a good decoding basis.

A possible algebraic width window is w and r polynomially small compared with q, while r exceeds eta(Z^n). The resulting source Gaussian width s is correspondingly small enough for a polynomial target-noise ratio if a suitable proof-only denominator basis has controlled norm. The hard missing premise is a verified standard reduction to GP for a Gen with low D at that normalized width. A worst-case BDD solver for arbitrary nearby targets does not follow merely from a Gaussian-versus-Haar distinguisher. Conversely a standard theorem with public short-basis advice would be incompatible with the needed FG pseudorandomness in the useful-width regime. No such theorem is asserted here.

This packet gives both full endpoints and a polynomial public channel. It does not certify the Gaussian source, an ideal-family distribution, or the binary completion theorem.
