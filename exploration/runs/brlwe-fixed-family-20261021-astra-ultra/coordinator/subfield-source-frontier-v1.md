# New source construction to test: contract to a small cyclotomic subfield

2026-10-21T18:42:36Z discovery note. Not yet a theorem or accepted source classification. This is a new extension beyond the full-stabilizer descent candidate; do not send it to the ongoing blind reviewer until that review is sealed.

The full Galois stabilizer of a composite ideal can be trivial even when its prime components separately have large decomposition groups. Instead fix the standard subfield R_g=Z[X^(n/g)] for every power-of-two g dividing n, g>=2. Compute d_g=[R_g:J_o intersect R_g] directly from the supplied ordinary basis by the same integer congruence/SNF image-index calculation. No invariance of J_o is needed to define this index. If d_g<2^g, enumerate d_g+1 binary vectors on these g sparse coefficients, find a collision, and obtain v in J_o of norm at most sqrt(g). Multiplying by the eligible 2-primary scalar a<=2 puts it in J, so the actual inherited radius is covered. Compute every d_g first and enumerate only for the least feasible numeric d_g. This is effective without factoring.

Potential broad family theorem: suppose the odd ideal is a product of at most t prime-ideal powers, t fixed, and its additive exponent e<=n^C for fixed C, while N(J)<=2^(rho n), rho<1 fixed. Let its factors be P_i^(b_i) above p_i, residue degrees f_i at degree n and f_i' at degree g. Cyclotomic order formulas suggest

    f_i' <= (g/n) f_i +2.

Contraction exponent is unchanged at odd unramified primes; merged contractions use maximum exponents. Therefore

    log2 d_g <= (g/n) log2 N(J_o) +2 sum_i b_i log2 p_i
             <= rho g +2t log2 e.

Choose a power-of-two g=O(log n) with 2t log2 e < (1-rho)g. Then d_g<2^g=n^O(1), proving a whole composite ordinary-basis family classically decodable even with trivial full stabilizer and exponential norm. The algorithm need not know the factorization/t,C,rho; those prove its polynomial numeric enumeration on the family. Strictness, exact 2-primary stripping, normal forms and n=2/small-n cases need review.

Example shape that should witness added scope: one high-residue-degree prime ideal over3, times one split prime ideal over a polynomial-value prime q. The latter forces the full stabilizer to be trivial; D can remain exponentially large below2^(rho n). A subfield of degree g=C0 log n has contraction index at most3^(g/2)q, below2^g if C0 exceeds the modulus exponent divided by1-log2(3)/2. This is only a family construction candidate until primality/root effectiveness, norm eligibility and exact contraction have been checked. It makes no hardness assertion and leaves many-prime-support ideals outside its sufficient scope.
