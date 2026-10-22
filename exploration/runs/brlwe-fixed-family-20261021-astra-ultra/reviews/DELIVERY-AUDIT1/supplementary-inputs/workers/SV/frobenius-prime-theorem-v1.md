# SV-FROB-PRIME v1

Frozen author theorem, PROVISIONAL pending exact-version review.

Let n>=2 be a power of two, R=Z[X]/(X^n+1). Supply an ordinary nonsingular integer column basis A of a nonzero PRIME ideal J of odd rational characteristic p, and promise D=N(J)<=2^(rho n) for fixed 0<=rho<1. No short vector, short basis, finite-field representation or Gaussian sampler is supplied. The prime p can be recovered as the additive exponent e of R/J using the exact denominator algorithm of SV-BDD-CLASS v1 part1.

There is a deterministic algorithm, polynomial in the NUMERIC p, n and the full basis encoding, that outputs a nonzero ternary f in J, with coefficient Euclidean norm <=sqrt(n). Consequently, for every rational target T=lambda+v with lambda in J^-1 and canonical infinity error <=r<1/(2sqrt(n)), the algorithm followed by coefficient rounding of fT and division by f recovers lambda exactly. It is all-input bounded on the stated promised inputs, pointwise and deterministic. Testing the ideal/primality promise is not required; the runtime charged here is polynomial in p, not logp.

In particular every such family with p<=n^C for any fixed C is classically polynomial-time decodable at the EXACT DD FIXED-MAIN-v2 radius r=epsilon_*ell²/(1024 nKchi Qmax), including cases D=p^f_res is exponential in n and p>=1/(2r). For p=2, scalar multiplication by2 already gives direct decoding whenever r<1/4, which also covers that radius.

The algorithm computes sigma_p:X→X^p. On power-basis coefficients this is a signed permutation. For every cycle with sign product +1, form its unique invariant vector whose initial nonzero coordinate is+1 and whose other coordinates follow the cycle signs. Omit cycles with sign product−1, whose fixed coefficients must vanish. These disjoint-support vectors b_1,...,b_g are an integral basis of the fixed coefficient lattice. Here f_res=ord_(2n)(p) and g=n/f_res. Put h=ceil(log2(p+1))<=g. Enumerate p+1 distinct binary sums of b_1,...,b_h, reducing each modulo the ordinary supplied J. Subtract a colliding pair. All arithmetic, including residue keys A^-1x mod Z^n, is exact.

This is an ordinary-input family classification. It does not establish hardness of the remaining superpolynomial-characteristic ideals, does not certify FF, and does not turn a DGS simulation into a decoder. It strengthens the source diagnosis beyond the earlier polynomial-index and e<1/(2r) tests. Failure of its numeric polynomial-time condition is not a lower bound.
