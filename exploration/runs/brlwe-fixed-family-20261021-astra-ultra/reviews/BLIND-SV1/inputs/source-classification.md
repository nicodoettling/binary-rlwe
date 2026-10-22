# SV-BDD-CLASS v1: direct classification of the actual source radius


Let n>=2 be a power of two, R=Z[X]/(X^n+1), K=Q[X]/(X^n+1). Coefficient norm is ordinary Euclidean norm. Canonical infinity norm is the maximum complex absolute value over the n embeddings. Supply a nonsingular integer column basis A of a nonzero integral ideal J, and let D=|det A|. An ordinary basis is the only ideal input. All integer/rational encodings and output costs are charged. Let r>0 be rational, and let T be a rational coefficient vector promised to equal lambda+v with lambda in J^-1 and ||v||_canonical,infinity<=r. The statements below are deterministic, pointwise in T, and use no oracle.

1. Let e be the least positive integer with eR contained in J. Compute e in polynomial bit complexity as the least common multiple of the reduced denominators of entries of A^-1. If 2er<1, coefficientwise round eT by floor(x+1/2) and divide by e. This returns lambda exactly, in polynomial bit complexity. For an upper-triangular column HNF H of J in the fixed power-basis ordering,

       H11=e=max_i Hii,

   and every Hii divides e. Thus the maximum-HNF-diagonal and quotient-exponent tests coincide for these ideals.

2. If a nonzero integral f in J has been computed or supplied and satisfies 4r²||f||_coef,2²<1, coefficientwise round fT and divide by f in K. This returns lambda exactly, in polynomial bit complexity in n and the complete A,T,f,r encodings. Testing the displayed guard is exact rational arithmetic. The cost of acquiring f is additional and may not be inferred from its existence. The result applies to any nonzero member, not only a generator of J.

3. Suppose D<2^n and h0=ceil(log2(D+1)). From A alone, enumerate D+1 distinct binary vectors supported on the first h0 coordinates. This uses O(D+1) ideal-residue computations and polynomial auxiliary work per vector and returns a nonzero ternary f in J of norm at most sqrt(h0). If 4r² h0<1, combining with part 2 solves the promised BDD instance deterministically. Its runtime and storage are polynomial in the NUMERIC D and the full input lengths. Therefore it is polynomial time on every family D<=n^C for fixed C, even when D exceeds 1/(2r).

4. Instantiate r at the accepted DD FIXED-MAIN-v2 radius, with all of that theorem's exact parameter guards:

       r = epsilon_* ell²/(1024 n K chi Qmax),
       B = 1/(2r) = 512 n K chi Qmax/(epsilon_* ell²),
       K=k0(Ncal+Ntest), ell=ceil(log2(2nK)).

   Here K is the physical source sample count and Qmax is the largest auxiliary prime; all other parameters retain their exact DD meanings. Then r<1/(2sqrt(n)). Parts 1–3 classify every eligible ideal with e<B, every ideal with effectively acquired nonzero f of norm<B, and every polynomial-NUMERIC-index family D<=n^C. These are direct classical decoders for J^-1 at the ACTUAL radius. They do not depend on a Gaussian-sampling comparison, a distinguisher, or a short basis being supplied.

5. For an eligible nonzero prime ideal J above an odd rational prime p with residue degree f, e=p and D=p^f. Hence p<B is sufficient for direct classical decoding, independently of f. Any prime ideal not classified by this exponent test has

       p>=B,    f<=rho n/log2 B

   when D<=2^(rho n), 0<=rho<1. This necessary condition does not establish hardness and does not rule out part 2 or part 3.

6. More generally factor an eligible J mathematically into prime-ideal powers. Suppose every odd rational prime p dividing D has residue degree f_p=ord_(2n)(p)>=F, for an integer F>=1. Then

       e <= 2 D^(1/F) <= 2^(1+rho n/F).

   Thus 2^(1+rho n/F)<B is a sufficient structural condition for direct decoding of the whole family, including composite and exponential-index ideals. Factoring D is not required by the decoder: it computes and tests e directly. Failure of this condition is only failure of a sufficient classification. In particular an eligible ideal with e>=B must contain an odd prime of residue degree below every F satisfying the displayed strict bound. The ramified 2-primary part alone is always covered.

The inherited same-J DGS theorem, M1 classical wide-sampling criterion, short-complementary-multiplier transfer obstruction and integral-map decomposition retain their old scopes. None is reversed or generalized by this statement. No independently established hard source is claimed. All strict inequalities are intentional, and output on an unpromised input may be any rational vector or a distinguished FAIL symbol.
