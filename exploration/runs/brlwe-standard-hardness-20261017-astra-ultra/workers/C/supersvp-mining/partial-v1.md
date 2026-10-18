# SuperSVP mining: exact first partial

PROVISIONAL. Read the user-supplied primary 2026/2443 §§3.5,4.1–4.2,4.4,6.1,7.1 directly from the supplied extraction. This is a restricted-family calculation, not a standard-hardness theorem. No experiment was run.

## 1. Three moduli must be distinguished

Let q0 be the split prime defining the CRT ideal I_T of dimension d. Set J_T=preimage(I_T) in R=Z[X]/(X^n+1). The coefficient Euclidean dual satisfies J_T^{*coef}=conjugate(J_T)^-1, since coefficient dot product is Tr(x conjugate(y))/n. Therefore

    K_T=q0 J_T^{*coef}=q0 conjugate(J_T)^-1,
    q0 R subset K_T subset R,
    N(K_T)=q0^d,
    K_T/q0R=I_T^perp.

In the full canonical embedding, the conversion is

    sigma(K_T)=n q0 sigma(J_T)^*.

The factor n cannot be omitted. The perpendicular ideal has CRT support given by the complement composed with the inversion/conjugation involution.

The pair K_T subset Z^n with P=I_n is exactly an r=1 SuperSVP instance: beta=1, quotient cardinality q0^d, invariant factors q0 repeated d times, and quotient gadget width g=d ceil(log2 q0). For d>0 the quotient exponent is q0; q0 e_i is a public nonzero vector in K_T. Thus any absolute output promise gamma_prime>=q0 is trivial. For d=0 the target lattice is R and e_i is already a solution at radius1.

Let Q denote the *different* modulus introduced by the paper's dense succinct-SIS/LWE reduction. Let q denote the target modulus in our fractional Gaussian/binary chain. The paper does not identify these three moduli. In particular, using denominator J=K_T in B's fractional bridge requires gcd(q0^d,q)=1. Setting q=q0 fails for every d>0. A coprime q is permitted by the pointwise A/B route, but it is a different full source law from SC-v1.

## 2. Complete endpoints of the imported paper edge

For input basis B_K of K_T, hint P=I, and sigma0>=2 eta_(2^-(lambda+2))(K_T), primary Theorem4.2 constructs a dense public triple

    A uniform full-row-rank in F_Q^(n by m),
    W uniform in F_Q^(r n by g), independent of A,
    T columns independently D_[I_r tensor A | W]^-1(G_(r n,Q), s).

The generated triple is statistically close to this joint law. The actual construction retains correlated Gaussian columns V, sign masks, and a lifting matrix M_lift satisfying Q B_K^-1 M_lift=A mod Q. They are not all public. A succinct-SIS solution x in Z^m, 0<||x||<=gamma and Ax=0, yields a nonzero vector in K_T of norm at most

    gamma_prime=4 gamma gamma_det sigma0,
    gamma_det=2 m0 n sqrt(r_M).

Its uniform-matrix endpoint is not a pair of ring elements; its conditional Gaussian public hint cannot be dropped from a claimed solver input without specifying the direction of the reduction.

Theorem7.1 turns a SEARCH succinct-LWE solver on the SAME public triple, secret uniform in F_Q^n and error D_(Z^m,chi), into a QUANTUM succinct-SIS solver, using the solver circuit coherently and in reverse. Write H=lambda+ceil(log2(m+1)). It requires

    4 sqrt(H)<=chi<=Q/(8 sqrt(H)),
    gamma>=Q sqrt(m)/(2chi).

Thus the smallest certified combined output radius is

    gamma_prime=2 (Q/chi) sqrt(m) gamma_det sigma0.

A nontrivial q0-ary result requires simultaneously

    chi/Q > 2 sqrt(m) gamma_det sigma0/q0,
    chi/Q <= 1/(8 sqrt(H)),

so necessarily q0>16 sqrt(mH) gamma_det sigma0. This is a quantitative test, not automatically a contradiction.

Theorem6.1's decision-to-search edge separately assumes ordinary decisional LWE. It requires hint width at least6n ceil(log2 Q)^2 and increases decomposition degree r to L=r ceil(32(lambda+2)ln2/adv^2). The exact quotient gadget g<=O(n) in the binary entropy regime does not meet this hint-width inequality. Section4.2 explicitly permits padding quotient gadgets with zero columns, which can raise the public hint dimension but changes the parameters and full public tuple. Likewise, r=1 alone cannot be silently retained through the decision-to-search degree increase.

## 3. Geometry does not by itself force the trivial output regime

If D=N(K_T)<=2^(rho n), rho<1, the algebraic norm and ideal-dual packing bound give the explicit coefficient smoothing upper bound

    eta_(2^-(lambda+2))(K_T)
       <= D^(1/n) max(sqrt(n),sqrt((lambda+2)ln2)).

This uses the correctly normalized canonical dual and then divides canonical width by sqrt(n). It is a new application of the independently checked ideal theta estimate, not a bound obtained by treating an arbitrary integer lattice as an ideal. With lambda=n and D^(1/n)<2, a supplied sigma0=O(sqrt(n)) is enough. The remaining gamma_det and sqrt(mH) costs are polynomial for polynomial q0,Q, so q0 can formally exceed the lower output bound by choosing its polynomial degree sufficiently large. The first-pass conclusion is therefore NOT an unconditional norm obstruction.

An explicit ordinary basis can be obtained from a systematic parity check of K_T modq0. Up to a coefficient permutation it has block form

    B_K=[[q0 I_d,C],[0,I_(n-d)]],

with balanced C entries at mostq0/2. Hence ||B_K||<=nq0 and ||B_K^-1||<=n, while its first d columns have lengthq0. The paper's Equation11 demands Q>=17 k_paper ||B_K||. For this basis Q=q0 is impossible when d>0. A different substantially shorter basis would be additional work, not a free consequence of the unit superlattice hint. Choosing Q polynomially larger is allowed by the paper, with parameter and endpoint changes recorded.

## 4. Exact comparison with the fractional-Gaussian chain

For J=K_T and a coprime q, our source decision law is

    (J, Q_(1/(DP))(G_w) mod qJ^-1)^k
        versus (same J, uniform((DP)^-1 Z^n/qJ^-1))^k,

where w is canonical width. B maps this to the exact planted fractional Gaussian D_(J^-1,s) modqJ^-1 (s in coefficient coordinates) and exactly uniform R/qR, paying the displayed finite bridge errors. A's composition uses the finite quotient J^-1/R of sizeD, independent of the superficial number of gadget columns. C-OHCP would turn any pointwise distinguisher for that finite periodic law into BDD on qJ^-1 without a short basis. These are precise conditional edges; the present primary SuperSVP theorem supplies no map from its dense (A,W,T) distribution to this known-ideal periodic law.

The missing bridge is therefore not merely a short quotient encoding. One must transform a standard-hard input, or a verified hard restricted SuperSVP input, into this exact ideal Gaussian decision family, preserving both comparator law and public metadata, or transform its dense hinted average case into our ring/binary target with quantified loss. Neither is supplied by identifying K_T subset Z^n. The random-T family is a strict special family; worst-case hardness for general SuperSVP pairs does not establish its hardness.

Next test: inspect whether the short quotient encoder itself yields an R-linear response map with short inverse and controlled coefficient noise. The general dense-matrix extraction step cannot be replaced by ring multiplication by notation alone.
