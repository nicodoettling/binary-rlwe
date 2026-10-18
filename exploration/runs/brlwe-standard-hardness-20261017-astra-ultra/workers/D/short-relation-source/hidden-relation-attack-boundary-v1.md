# D-SREL-ATTACK-1: what hiding a logarithmic-weight relation does and does not buy

Status: provisional elementary algorithm and scope boundary. No experiment or standard-hardness claim. Coordinates use the coefficient Euclidean norm throughout.

Let J be a public integral ideal in R=Z[X]/(X^n+1), n power of two, and let q be an odd prime coprime to [R:J]. Assume J contains a nonzero coefficient-ternary v of weight <=w, without assuming that J is principal or that v generates J. The two full experiments have the SAME J marginal:
  P: a~D_(J^-1,s), A=pi_q(a);
  Q: A~U(R_q).
Any randomness used to choose J is fixed before the following algorithm; conditional statements are pointwise in J. The hidden relation need not be supplied to the algorithm.

## Executable algorithm and exact comparator

Enumerate all ternary coefficient vectors of weights1,...,w. Test membership in J using its integer HNF. Stop at the first member v. This is a deterministic function of public J, and does not depend on A or the challenge bit. There are at most
  N_w=sum_(j=1)^w 2^j binom(n,j)
trials, each using polynomial-time exact arithmetic in the input size. Existence guarantees termination within this bound. This is an explicit finite algorithm; it has not been run as a computational experiment.

Let L_v(A) be the constant coefficient of vA modulo q. Because v is nonzero ternary and q is odd, L_v is a nonzero F_q-linear functional on R_q. Thus in Q, L_v(A) is EXACT uniform in F_q, even if v is a zero divisor modulo q. We do not require gcd(N(v),q)=1.

For integer B>=0, accept planted precisely when the centered residue of L_v(A) has absolute value at most B. The comparator probability is exactly min(1,(2B+1)/q).

In P, v a lies in R because v in J and a in J^-1. The constant coefficient is a real linear functional of a whose coefficient vector has Euclidean norm sqrt(j), where j=wt(v)<=w. The shifted-Gaussian mass inequality rho_s(L-c)<=rho_s(L), applied after completing the square in the moment-generating function, gives
  Pr[|coeff_0(v a)|>s sqrt(w) U] <=2 exp(-pi U²)
for every U>0. Therefore B=ceil(s sqrt(w)U) yields distinguishing advantage at least
  1-2exp(-pi U²)-min(1,(2B+1)/q).
This lower bound holds conditional every public J satisfying the promise, hence after averaging J, and it does not use a product of marginal probabilities. Modular wrapping cannot create a false negative on the bounded integer event.

## Complexity and implications

For constant w this is a polynomial-time source distinguisher in a useful narrow regime. For w=O(log n), the enumeration is exp(O(log² n)) times a polynomial in the input encoding lengths. The proposed sparse-relation source is therefore at most quasipolynomially hard in this regime. This is not a polynomial-time attack for growing w, and does not refute a computational hardness premise.

If a polynomial-time reduction from a standard n-dimensional RLWE/ideal-lattice problem to this source has polynomial dimension/encoding blowup and polynomial inverse advantage, then composing it with the displayed algorithm yields a quasipolynomial algorithm for that standard problem in the same classical/quantum model as the reduction. This is a concrete consequence that any claimed source foundation must accept; no theorem here excludes such an algorithm.

For general logarithmic-weight sparse f, no polynomial-time extraction from HNF(J) was established. CDPR's typical-generator recovery theorem has additional log-embedding and unit-coset hypotheses; failure to verify them is not security evidence. Known-generator examples remain polynomially distinguishable, and hiding f only removes that immediate input, not the finite enumeration bound.

## Hand controls

For J=R and v=1 the test reduces exactly to testing one coefficient of D_(Z^n,s) modulo q; the uniform comparator is1/q per residue. For a nonunit v modulo q, the same single-coordinate comparator remains uniform because one nonzero coefficient of v multiplies a uniform coordinate of A, conditional on all other coordinates. This control prevents incorrectly requiring multiplication by v to be a ring automorphism.
