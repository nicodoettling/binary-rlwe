# SV-PRIME-SUPPORT-v2: a wider subfield classification

Use exactly the ordinary-basis input, unique2-primary factor a, odd ideal J_o, computable indices d_g and decoder of SV-SUBFIELD-v2. Assume N(J)<=2^(rho*n), fixed 0<=rho<1. In the mathematical factorization J_o=product_i P_i^b_i over odd rational characteristics p_i, define

    B(J_o)=sum_i b_i*log2(p_i).

The sum counts distinct prime ideals, not just rational primes; B need not be computed by the algorithm. For every allowed g,

    log2(d_g) <= rho*g+2*B(J_o).

Consequently, if B(J_o)<=C*log2(n) for fixed C, the SAME factorization-free algorithm runs in polynomial time and decodes all rational targets at the actual inherited DD radius. More generally it suffices that e<=n^C and, for each rational odd prime p, at most t distinct prime ideals above p occur in J_o, where t is fixed. The total number of prime ideals, and the number of different rational characteristics, need not be bounded. The algorithm does not receive the factorization, B, t or C.

For every fixed 0<rho<1, this family contains eligible exponential-index ideals with unbounded prime-ideal support and trivial full Galois stabilizer. An explicit asymptotic family can be built using split primes and primes with successively increasing exact2-adic valuations of p-1, with a polynomial numeric exponent. It is an existence/scope example, not an additional input oracle or a source hardness claim.

No implication is asserted from polynomial exponent alone when arbitrarily many primes ABOVE ONE rational characteristic occur. This theorem supplies a sufficient classical decoding criterion, not hardness of its complement. It changes no target family and establishes no new FF reduction.
