# Proof of SV-BDD-CLASS v1

Frozen author proof. PROVISIONAL. All new claims are deterministic; there is no new conditional-probability lemma.

## 1. Computation, HNF and scalar rounding

For any positive integer m, mZ^n is contained in AZ^n exactly when every entry of mA^-1 is an integer. The least such m is the least common multiple of all reduced denominators of A^-1. Exact inversion and gcd/lcm arithmetic have polynomial bit complexity in the supplied nonsingular integer matrix; determinant/cofactor bounds control all intermediate and output bit lengths. Thus e is computed without integer factorization.

Since J is an ideal, m belongs to J if and only if mR is contained in J: the forward direction multiplies by every monomial, and the reverse direction takes 1. In upper-column HNF, the first column generates J intersect Q*1 and is H11*1. Thus H11=e. For every j, eX^(j-1) belongs to J intersect span(1,...,X^(j-1)); its last coordinate is an integer multiple of Hjj. Hence Hjj divides e. This proves max Hii=e. This equality specializes the older valid general-lattice inequality h<=e; it does not reject that inequality.

Since e is in J and lambda is in J^-1, e lambda is integral. Parseval in this power basis gives ||v||_coef,2<=||v||_canonical,infinity<=r, hence each coefficient of ev has absolute value <=er<1/2. Translation-equivariant nearest-integer rounding therefore returns exactly e lambda, including at every valid input. Division by e recovers lambda. Rational arithmetic and output lengths are polynomial in full input bits. The strict margin avoids tie ambiguity.

## 2. A nonzero ideal member

The product f lambda belongs to R. Each coefficient of the negacyclic product fv is the inner product of the coefficient vector of v with a signed permutation of the coefficient vector of f. Cauchy–Schwarz gives absolute value at most ||f||_coef,2 ||v||_coef,2<=||f||_coef,2 r<1/2. Rounding fT therefore returns f lambda exactly. Since X^n+1 is irreducible over Q for power-of-two n, nonzero f is invertible in K, and dividing by it gives lambda.

Multiplication uses integer/rational convolution, and inversion of f uses a nonsingular n by n multiplication matrix. Gaussian elimination with determinant bounds gives polynomial bit complexity in n and encoded f. No oracle, short-basis advice, ideal factorization or Gaussian distribution is used. The squared guard is rational and exactly testable. The proof does not compute f merely because a short one exists.

## 3. Numeric-index enumeration

Because D<2^n, h0=ceil(log2(D+1))<=n and there are at least D+1 binary vectors in those coordinates. The quotient R/J has exactly D elements. Two enumerated vectors b,b' have the same residue, and f=b-b' is a nonzero ternary element of J with at most h0 nonzero coefficients. Thus ||f||²<=h0.

An exact residue key is A^-1 b reduced coordinatewise modulo Z. Two keys agree if and only if b-b' belongs to J. Keys use rationals of polynomial bit length; sorting or dictionary lookup can be performed with polynomial bit comparisons and O(D) storage. This provides the claimed O(D+1) residue computations and polynomial-in-D total complexity. It does not run in polynomial logD time. The resulting f is effective and part 2 applies whenever 4r²h0<1.

## 4. The actual radius

Substituting epsilon0=epsilon_*/2, epsilon=epsilon_*/4 and delta=epsilon_*/16 into DD AM-MAIN-v3 gives d0=epsilon_* ell²/(1024 n K chi), then r=d0/Qmax. In particular neither K nor Qmax can be dropped. The accepted guards imply

    Qmax>=Qmin>=n sigma_floor
         =8n³ ceil(sqrt(Kn))ell⁴.

As 0<epsilon_*<1, chi>=1 and K>=1,

    r < 1/(8192 n⁴ K ceil(sqrt(Kn))ell²)
      < 1/(2sqrt(n))

for n>=2 and ell=ceil(log2(2nK))>=2. Hence 4r²h0<1 for every h0<=n. This proves the polynomial-index application and the exact threshold B for all other cases. It is not an asymptotic substitution and remains true for conservative large auxiliary-prime choices.

## 5. Prime and supported-family arithmetic

For prime J above p, R/J has characteristic p, so its additive group has exponent p. Its field size is p^f. The exponent test gives p<B. If it fails, p>=B; combining p^f<=2^(rho n) with logarithms yields f<=rho n/log2 B. B>1 follows from the radius bound. The implication remains a necessary condition for being unclassified by this particular test, never a hardness statement.

For the composite statement, power-of-two cyclotomic R is the full ring of integers. The prime 2 is totally ramified: 2R=mathfrak{p}_2^n and N(mathfrak{p}_2)=2. If the 2-part of J is mathfrak{p}_2^a, eligibility gives 0<=a<=log2D<=rho n<n. Its quotient exponent is 1 if a=0 and 2 otherwise. Every odd p is unramified, and all prime ideals above p have common residue degree f_p=ord_(2n)(p). Write its component as product_j mathfrak{p}_{pj}^{a_pj}. Its norm is D_p=p^(f_p sum_j a_pj), and its additive exponent is p^(max_j a_pj), because p^tR has valuation t at every prime above p. Therefore if f_p>=F,

    e_p=p^(max_j a_pj)<=p^(sum_j a_pj)<=D_p^(1/F).

The exponents at different rational primes are coprime and multiply. Multiplying the displayed inequalities and the 2-part bound gives e<=2 D^(1/F). Eligibility yields e<=2^(1+rho n/F), and the strict structural condition implies e<B. This arithmetic is used only to describe the family; the actual decoder computes e by exact inversion and does not request a factorization.

The classical power-of-two cyclotomic splitting and ramification identities in this final section are elementary algebraic-number-theory inputs, to be verified against a primary source during review. No computational hardness theorem is imported through them. Parts 1–4 and the characteristic-p assertion in part 5 need none of the splitting-order formula.

## Scope and challenge points

The multiplier algorithm overlaps the older supplied-element integral-cancellation observation; the new content is its direct exact-radius family classification, effective ordinary-basis acquisition at polynomial numeric index, the HNF equality, and the supported-family restriction. The theorem does not claim that the elementary rounding idea is novel. It neither simulates a coherent DGS oracle nor derives a decoder from wide DGS. Supplied short integral transfer maps still encode the short-object obstruction of RH M2; no acquisition mechanism has been added there.

No acceptance can be inferred from this author proof. Needed review challenges include strict endpoints, exact radius substitution, ordinary basis and bit complexity, distinction between e and D, and residual families having polynomial encodings but superpolynomial numeric characteristic/index.
