# SV-SUBFIELD-v2: ordinary-basis decoding by a small subfield contraction

Author candidate, PROVISIONAL pending full and fresh blind review. This is an algorithmic source classification, not a hardness claim or a new decision reduction.

Let n>=2 be a power of two, R_n=Z[X]/(X^n+1), and J a nonzero integral ideal supplied by a nonsingular integer column basis A. Assume N(J)<=2^(rho n) with a fixed 0<=rho<1. All basis/target/rational input encodings and output costs are charged. Compute the additive exponent e of R_n/J by lcm of the reduced denominators of A^-1, and define a=2^{v_2(e)} to be the largest power of2 dividing e, with m=e/a odd. Eligibility implies a in{1,2}. Set J_o=J+mR_n.

For each power of two g with 2<=g<=n, define R_g inside R_n by Y=X^(n/g), so R_g=Z[Y]/(Y^g+1). Define

    d_g=[R_g:J_o intersect R_g].

These log2(n) integer indices are computable in polynomial bit complexity from A, by exact integer normal forms of the coefficient inclusion and congruence map. At least g=n satisfies d_g<2^g. Choose g_* minimizing d_g among the g with d_g<2^g, with deterministic ties. Let d_*=d_(g_*).

There is a deterministic algorithm from A that, with time and storage polynomial in the NUMERIC d_*, n and complete input lengths, outputs a nonzero member f of J of coefficient norm at most2sqrt(g_*). It enumerates d_*+1 binary vectors supported on the first ceil(log2(d_*+1)) basis elements 1,Y,...,Y^(g_*-1), reduces modulo J_o, subtracts a collision, and multiplies by a. No ideal factorization, short basis, subfield representation beyond this explicit coefficient embedding, or Gaussian oracle is supplied.

For every rational T=lambda+w, lambda in J^-1 and canonical infinity error at most rational r, the exact guard 16*r^2*g_*<1 suffices for coefficient rounding of fT followed by division by f to recover lambda. All such targets are solved pointwise and deterministically. The actual DD FIXED-MAIN-v2 radius, under all its guards, satisfies this sufficient inequality, since g_*<=n and that radius is less than1/(4sqrt(n)). This claim does not change that delivered radius.

A substantive family on which this algorithm has polynomial runtime is as follows. Fix constants rho<1, integer t>=1 and C>0. Suppose the odd ideal J_o is a product of at most t DISTINCT prime-ideal powers P_i^(b_i), b_i>=1, and the numeric exponent e<=n^C. Neither this factorization nor t,C need be supplied to the algorithm. For all sufficiently large n, some power-of-two g=O_(rho,t,C)(log n) satisfies

    d_g<2^g=n^O_(rho,t,C)(1).

Hence d_* is polynomial in n and the displayed decoder is polynomial time in n and the full supplied input lengths. The norm of J itself may be exponential in n and its full Galois stabilizer may be trivial. The finite algorithm and its numeric d_* bound apply at every n; the family assertion is asymptotic, so finitely many small n are absorbed into its runtime constant.

The bounded number of prime-ideal factors is load-bearing in this family guarantee. Polynomial exponent alone is not asserted to imply polynomial d_* for arbitrary prime support. The source is given as an ordinary ideal basis; effectively acquiring that basis is a separate obligation in any external reduction. Failure of these sufficient criteria is not source hardness. No efficient factoring or computation of a hidden ideal is assumed.
