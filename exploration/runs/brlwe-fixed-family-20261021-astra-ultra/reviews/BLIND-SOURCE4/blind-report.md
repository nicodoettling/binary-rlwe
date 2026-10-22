# BLIND-SOURCE4: frozen-statement mathematical review

Review date: 2026-10-21. Inputs are the exact statement packet authorized by allowed-read-manifest-v2.json and the definition-only addition authorized by allowed-read-addendum-v3.json. The original five target versions remain frozen throughout this review. No author proof, other review, repaired statement, or author experiment was read. See assignment-verbatim.txt, exposure-notes.md, and input-hashes.json for the full provenance. A seal manifest is supplied separately.

## 1. Verdict and exact scope

| Frozen target | Local mathematical conclusion |
|---|---|
| SV-DENSE-SPLIT-v1 | Proved under its stated effective polynomial-value split-prime-family assumption. |
| SV-RS-DECODE-v1 | The pointwise algorithm and its finite decoding bound are proved. The paragraph identifying/substituting the **actual inherited radius is false as written**, because epsilon differs from epsilon_* by a factor of four in the supplied definitions. The exact complete version therefore needs correction. |
| SV-GAP-DECODE-v1 | Proved; it uses the valid pointwise decoding argument, not the defective inherited-radius identification in RS-v1. |
| SV-LIST-DECODE-v1 | Proved, including deterministic root enumeration with a multiplicity budget, exact lift selection, and the displayed explicit regime. |
| SV-RS-ACTUAL-v3 | Proved conditional on the explicitly assumed inherited interface/guards, using its own correct epsilon_* radius and the supplied K/ell definitions. This does not certify the inherited reduction itself or a minimal-chi witness. |

These are local conclusions from independent reconstruction. They are not a claim that the coordinator's global historical-regression, dependency, or delivery gates have closed. No hardness conclusion follows from any failed sufficient condition.

The mathematical dependency graph used here is:

1. Coefficient Parseval identity and prime-exponent annihilator description -> Fourier/GRS representation.
2. Fourier/GRS representation plus explicit linear-system decoding -> RS pointwise algorithm -> GAP and the decoder portion of ACTUAL-v3.
3. Fourier/GRS representation plus interpolation, multiplicity-controlled recursion, and the determinant/norm uniqueness bound -> LIST.
4. Explicit support construction plus ordinary contraction computation -> DENSE.
5. Cyclotomic subfield containment plus ideal-extension index bound -> ALL-SUBFIELDS -> arbitrary-subfield conclusion in DENSE and ACTUAL-v3.
6. Exact batch/C8 definitions plus an effective split-prime construction and the permitted chi>=a interface -> ACTUAL-v3's delivered-radius witness.

The rejected epsilon identification is a separate leaf. Rejecting it invalidates any use of its displayed inequality as the exact inherited substitution. It does not invalidate the separately reconstructed pointwise decoder or ACTUAL-v3's correctly defined radius.

## 2. Frozen model, quantifiers, and representations

R=Z[X]/(X^n+1), n>=2 a power of two; K=Q(zeta_(2n)) when a field is needed. An ideal is supplied by a nonsingular n-by-n integer column basis A in the coefficient basis 1,X,...,X^(n-1). Targets and claimed radii are rational and have their entire encodings charged. Coefficient norm is Euclidean; canonical infinity norm is max over all n embeddings. No scaled real embedding convention is substituted.

All decoding statements are pointwise promises: for each supplied valid ideal, rational T, rational r, and decomposition T=lambda+w with lambda in J^-1 and the stated canonical bound, the algorithm returns lambda. Root choice and spectral interval may depend on J; their deterministic computation does not depend on knowing lambda. No factorization, short vector, Gaussian samples, or Gaussian oracle is provided or assumed.

For ACTUAL-v3 the quantifier order is: fix rho and an admissible inherited polynomial-value parameter family; fix its master auxiliary list and thereby K,ell,Qmin,Qmax; choose a common kappa valid over the entire eligible D range; compute common Q_*,epsilon_C,a; then construct p,J and chi; then the deterministic decoder works for every promised target at the resulting radius. This is not one source family uniform over all possible adversaries' polynomial exponents, nor a claim about chi=a.

## 3. Common norm, exponent, and recognition facts

Let z=sum_i z_i X^i, and let the complex embedding roots be omega_j=exp(pi*i*(2j+1)/n). The matrix (omega_j^i) has pairwise orthogonal columns of squared norm n. Therefore

    ||z||_coef^2 = (1/n) sum_j |sigma_j(z)|^2 <= ||z||_can,infinity^2.

Also

    ||uv||_coef <= ||u||_coef ||v||_can,infinity.

Both inequalities have exactly the constants used below; no extra sqrt(n) is needed.

The additive quotient exponent e is the least positive integer with eR subset J. Equivalently eA^-1 is integral, so e is the lcm of reduced denominators of the entries of A^-1. Exact rational linear algebra computes this with polynomial bit complexity in the complete A encoding. If desired, the ideal promise itself can be checked by testing that A^-1 M_X A is integral, where M_X is the signed cyclic multiplication matrix for X.

For e=p prime, pR subset J subset R. If p=1 mod 2n, the roots beta_j=alpha^(2j+1) are distinct and

    R/pR -> F_p^n,  u |-> (u(beta_j))_j

is an algebra isomorphism. Every ideal of this product algebra is zero in a set of coordinates and unrestricted in the others. Thus evaluating all columns of A identifies exactly the set S of roots at which all elements of J vanish. This proves the support description without a supplied factorization. Its cardinality t satisfies |det A|=p^t. Excluding R and pR is precisely excluding t=0 and t=n.

Deterministic recognition can use trial division for primality, enumerate field elements alpha until alpha^n=-1, and evaluate A at the resulting roots. Because n is a power of two, alpha^n=-1 is equivalent to order 2n. There are exactly n such roots. To recognize an unspecified consecutive-support presentation, enumerate these primitive roots and scan all cyclic starts. To maximize a gap, scan the support in each such ordering. These operations are polynomial in n, the **numeric p**, and the full input bit lengths. No polynomial-in-log(p) primality/root-search/factorization claim is needed. On arbitrary inputs the same elementary recognition has a bound in numeric e; on the promised inputs e=p.

## 4. The exact inverse Fourier orientation

If lambda in J^-1, then a=p lambda is in R since p in J. Conversely, for a in R,

    a/p in J^-1  iff  a J subset pR.

In the product algebra, J is arbitrary on the complement of S and zero on S. Its annihilator is therefore supported **on S**, not on its complement. Writing v_j=a(beta_j), we have v_j=0 for j outside S, and the inverse transform gives

    a_i = n^-1 sum_(j in S) v_j alpha^(-(2j+1)i)  in F_p.

Suppose S lies in the cyclic interval s,s+1,...,s+k-1. Put

    x_i = alpha^(-2i),
    m_i = alpha^(-(2s+1)i),
    f(Z) = n^-1 sum_(h=0,...,k-1) v_(s+h mod n) Z^h,

with zero coefficients for positions outside S. Then

    a_i = m_i f(x_i),   0<=i<n,   deg f<k.

The x_i are pairwise distinct, and all m_i are nonzero. This is the claimed generalized Reed--Solomon code, with dimension k and distance n-k+1. The cyclic wrap causes no change: alpha^(-2ni)=1. For S={0,...,t-1}, k=t and m_i=alpha^-i. The negative exponents and the support orientation are load-bearing.

The finite control independently checked this identity on every spectral unit vector for all 270 nonempty proper supports at (n,p)=(2,5),(4,17),(8,17), and checked multiplication annihilation against explicit integer ideal bases. This is a bounded regression, not the proof of the identity.

## 5. RS pointwise decoding, including the exact linear system

Let z_i be deterministic nearest-integer rounding of pT_i, with any fixed rule for ties. Since a_i=p lambda_i is an integer, a coordinate where z_i differs from a_i must have |p w_i|>=1/2. Hence the number e of such coordinates satisfies

    e <= 4p^2 ||w||_coef^2 <= 4p^2 r^2,
    e <= E := floor(4p^2 r^2).

Reduction modulo p can only reduce the number of erroneous symbols. Divide z_i mod p by m_i to get received values y_i. Under 8p^2r^2<n-k+1, we have 2E<n-k+1 and therefore k+2E<=n.

For a fully explicit decoder, find polynomials L,P over F_p with L monic of degree E, deg P<k+E, and

    P(x_i)=y_i L(x_i)   for all i.

This is a finite-field linear system in k+2E unknown coefficients. A solution exists: take an error locator of actual degree e, multiply by any monic polynomial of degree E-e, and multiply the result by the true message f to obtain P. For any solution, P-Lf vanishes at all n-e correct locations; its degree is at most k+E-1, while n-e>=n-E>=k+E. Thus P=Lf identically. Polynomial division recovers the exact f, even when the actual number of errors is less than E. No bivariate factorization is involved here.

The decoded a_i mod p determines lambda_i modulo Z. For each coordinate choose the unique lift a_i/p+z, z in Z, with distance less than 1/2 from T_i. Such a lift exists for the promised lambda because |w_i|<=||w||_coef<=r<1/2; uniqueness follows because two such lifts differ by an integer. This yields lambda exactly. The output numerator sizes are bounded in terms of the full T encoding and log p, both charged.

This proves the core RS theorem and, by taking k=n-g_max+1, the core GAP theorem. Strict inequalities matter: the proof does not accept equality at the Hamming unique-decoding threshold or r=1/2. Rounding ties are already paid for by the non-strict per-coordinate error bound.

The illustrative r=1/p has pr=1 and satisfies the RS bound exactly when n-t+1>8. It also satisfies r<1/2 because every allowed p is at least 5. The scalar sufficient condition 2pr<1 fails there. No assertion that this illustrative r is an inherited instance is required.

## 6. The literal defect in RS-v1's inherited-radius paragraph

The supplied parameter definitions and the later definition-only batch excerpt say

    epsilon = epsilon_*/4,
    r_actual = epsilon_* ell^2/(1024 n K chi Qmax).

RS-v1 instead identifies the actual inherited radius as

    epsilon ell^2/(1024 n K chi Qmax).

All displayed factors are positive on a valid input, so the latter is exactly r_actual/4 and cannot equal r_actual. Consequently the displayed RS-v1 inequality with coefficient 8 and epsilon^2 is not the exact sufficient substitution at the inherited radius. The correct substitution is

    8 p^2 epsilon_*^2 ell^4
       < (n-t+1) (1024 n K chi Qmax)^2.

If expressed using the inherited epsilon, its left side is

    128 p^2 epsilon^2 ell^4.

Thus the printed epsilon-based inequality is weaker by a factor of 16. This is a direct algebraic contradiction between frozen definitions, requiring no numerical experiment. It is a rejection of the exact inherited-radius assertion, not a counterexample to the separately proved pointwise decoder. No repaired packet was read to reach this conclusion. ACTUAL-v3 explicitly uses epsilon_* and is unaffected by this mismatch.

## 7. GAP: interval dimension, optimization, and eligible norm

List the t support positions cyclically. The t positive gaps between successive positions sum to n, so their maximum is at least ceil(n/t). A gap of size g leaves g-1 unsupported consecutive positions. The complementary cyclic interval has length n-g+1 and contains every supported position. Section 4 therefore puts pJ^-1 modulo p inside a GRS code of dimension n-g+1 and distance g.

For a singleton, the single gap is n; the containing code has dimension 1 and distance n. For t=n-1, the maximum gap is 2. These cases obey the same argument. Maximizing over primitive roots is a deterministic finite search based on J alone; no hidden-target advice is used.

Eligibility gives t log2(p)<=rho n with rho>0, hence

    g_max >= ceil(n/t) >= n/t >= log2(p)/rho.

Thus 8p^2r^2<log2(p)/rho implies the claimed strict decoding condition. No conclusion is drawn when that sufficient bound fails. Optimizing the root can help but is not needed for this lower bound.

## 8. LIST: interpolation, all roots, and exact selection

Let z_i again be nearest-integer rounding of pT_i. The unscaled list is z_i-B,...,z_i+B modulo p. The requirement 2B+1<=p makes its entries distinct. For the interpolation code, divide each entry by the known multiplier m_i; it remains a list of the same cardinality, although it need not be an interval after scaling.

If the true symbol is absent from the list, then the integer z_i-a_i is outside [-B,B], so |p w_i|>=B+1/2. Therefore at most

    h=floor(p^2 r^2/(B+1/2)^2)

coordinates fail to contain the true symbol. Possible wraparound congruences can only improve this count. No independence between errors is assumed.

There are exactly N(d,t) monomials X^iY^j with i+(t-1)j<=d. The n(2B+1) homogeneous evaluation constraints have a nonzero solution Q when N(d,t)>n(2B+1). For the true polynomial f, deg Q(X,f(X))<=d, and it has at least n-h distinct roots x_i. Since d<n-h, it vanishes identically.

### Polynomial-root enumeration with multiplicities

The following gives an explicit algorithm and proves the required polynomial-size recursion without assuming a general factorization oracle.

At every node, divide the current nonzero Q by its maximal power of X, so q(Y)=Q(0,Y) is a nonzero polynomial. Enumerate each a in F_p with q(a)=0 by exhaustive field enumeration; numeric p is an allowed resource. Substitute Y=a+XY, remove the new maximal power of X, and recurse to determine the next coefficient. After t levels, verify Q_original(X,f(X))=0 and retain only actual polynomial roots of degree<t.

To bound branching, suppose a is a root of q of multiplicity m. Expand

    Q(X,a+Z)=sum c_ij X^i Z^j.

For i=0, all j<m terms vanish and the j=m coefficient is nonzero. After Z=XY, the minimal X exponent s=min{i+j:c_ij!=0} is at most m. Removing X^s and setting X=0 gives a polynomial in Y of degree at most s, hence at most m. Thus the sum of the children’s reduced Y-degrees is at most the sum of multiplicities of q's roots, which is at most deg q. This is the exact invariant that a naive p-ary tree argument would miss.

At each positive depth there are at most deg_Y(Q_original) nodes, and the sum of their reduced Y-degrees is at most that same number. Zero-degree nodes terminate. There are t levels, so there are O(1+t deg_Y Q) nodes, including the initial node. Each substitution increases X-degree by at most deg_Y Q; after t levels all degrees are bounded by d+t deg_Y Q. The arithmetic, scanning p possible roots, and final polynomial identity tests therefore have polynomial cost in n,p,d and input length. The argument uses multiplicity, not a nonzero derivative, so it remains valid for inseparable characteristic-p roots. Nonzero Q remains nonzero under the substitution, and removing X-content is always defined.

The exact regression included a characteristic-5 fifth power, two roots with a shared coefficient prefix, a factor X^7, a formal power-series root whose degree is too large, all five constant roots, and a no-root example. All enumerated roots matched exhaustive testing of all 125 degree<3 polynomials in each case.

### Lifting and uniqueness

For each root f, compute its GRS word and lift each coordinate divided by p to within <1/2 of T. Discard absent lifts, test ideal-inverse membership exactly, and test the squared coefficient distance <=r^2 with rational arithmetic.

For any nonzero x in J^-1, the multiplication matrix M_x satisfies M_x A integral. Its determinant is a nonzero integer, giving

    |N_(K/Q)(x)| D_J >=1.

On the other hand, the arithmetic-geometric mean inequality and Parseval give

    |N_(K/Q)(x)| = product_sigma |sigma(x)| <= ||x||_coef^n.

Hence every nonzero member of J^-1 has coefficient norm at least D_J^(-1/n). Two candidates within Euclidean distance r of T would differ by an element of J^-1 of norm at most 2r. The strict guard (2r)^n D_J<1 rules this out. The true lambda is retained because ||w||_coef<=r. Thus exactly one accepted candidate exists. This is why a polynomial list by itself is insufficient, and why both membership and the uniqueness guard are retained.

### The displayed convenient regime

Write s=t-1>=1. A decreasing-sum/integral comparison yields

    N(d,t)>=d^2/(2s).

For d=n/2, this is greater than n^2/(8t). If n>=64t and B=floor(n/(64t)), then

    n(2B+1)<=n^2/(32t)+n<=3n^2/(64t)<n^2/(8t).

Also B+1/2>=n/(128t). The stated pr bound therefore implies h<=n/4, and d=n/2<n-h. The list-size constraint follows automatically from p>=2n+1. Because n is an even power of two, d=n/2 is integral.

For an eligible ideal and the supplied inherited guarantee r<1/(4sqrt(n)),

    (2r)^n D_J < (2^(rho-1)/sqrt(n))^n <1.

Thus the stated uniqueness implication is valid. For dense support t=Theta(n/log p), the explicit permitted pr is Theta(sqrt(n) log p), and n>=64t holds for all sufficiently large n. This is a sufficient radius; it is not a hardness boundary.

## 9. DENSE: construction, stabilizer, contractions, and growth

Let ell_p=ceil(log2 p). For rational fixed rho, t is computed using exact rational/integer arithmetic as the greatest positive odd integer <=floor(rho n/ell_p), when one exists. Under p>=n^4 and p<=n^A for a fixed A, t=Theta(n/log n), so it exists and grows unboundedly for sufficiently large n, while t<n.

The p-prime factors are distinct, their quotient fields are F_p, and CRT gives R/J=F_p^t as an additive group. Thus the exponent is p and N(J)=p^t. Since t ell_p<=rho n and log2 p<=ell_p, N(J)<=2^(rho n). For the lower bound,

    t >= rho n/ell_p-2,
    t log2 p >= rho n (log2 p/ell_p)-2 log2 p = Omega(n),

where polynomial-value p bounds the subtractive term by O(log n). The upper bound is rho n. Thus N(J)=exp(Theta(n)). Numeric p and the number of characteristic primes must not be confused: there is one rational characteristic and t unbounded prime ideals above it.

An explicit ordinary integer basis can be constructed without short-vector search. Let G(X) be the monic degree-t polynomial product of the selected linear factors modulo p, with ordinary residue representatives. Use columns

    p, pX, ..., pX^(t-1), G, XG, ..., X^(n-t-1)G.

They all vanish at the selected roots modulo p, and the triangular coefficient matrix has determinant p^t. The resulting lattice equals J by its index. Entries have O(log p) bits; the basis has O(n^2 log p) encoding size. Finding alpha by enumeration and forming G is polynomial in numeric p and n.

For the full Galois stabilizer, write the supported exponent set as S={1,3,...,2t-1} in Z/(2n). If an odd unit u stabilizes the ideal, it permutes this set (the possible inverse action gives the same stabilizer). Summing gives

    u t^2 = t^2 mod 2n.

Since t is odd and 2n is a power of two, t^2 is invertible modulo 2n; hence u=1 mod 2n. This proves triviality and explains the oddness requirement.

On the standard subfield generated by Y=X^(n/g), the selected roots restrict according to their indices modulo g. Consecutive t indices yield exactly min(t,g) distinct restricted roots. The contraction therefore has index

    d_g=p^min(t,g).

If g<=t, d_g=p^g>=2^g, so g is infeasible. If g>t, feasibility is exactly t log2 p<g and d_g=p^t. The feasible set is nonempty: g=n works because p^t<=2^(rho n)<2^n. Thus its minimum is exactly p^t and is exponential. This uses the strict feasibility condition, not a rounded logarithmic substitute.

## 10. ALL-SUBFIELDS and the subfield dependency

The cyclotomic integer-ring and ramification facts used here match [Milne, Proposition 6.2](https://www.jmilne.org/math/CourseNotes/ANT.pdf). The ideal-extension norm identities match his Propositions 4.1–4.2. The residue-degree description agrees with Example 8.18. The specialized containment and algorithmic arguments below are reconstructed directly.

For n>=4, Gal(K_n/Q) is C_2 times a cyclic group C of order n/2, where C consists of units congruent to 1 modulo 4. Cyclicity can be checked directly: 5 has order n/2 modulo 2n because v_2(5^(2^h)-1)=h+2, by induction. The n=2 case is immediate.

Let L have degree g and H=Gal(K_n/L). If m=min(2g,n)=n, containment in K_m is automatic. Otherwise |H intersect C|>=|H|/2=n/(2g). Since C is cyclic, H contains its unique subgroup of order n/(2g), which is Gal(K_n/K_(2g)). Therefore L subset K_m, with [K_m:L]<=2.

Let I=J_o intersect O_L. Then I O_(K_m) subset J_o intersect O_(K_m). The extension has index N(I)^[K_m:L], so

    d_m <= d_L^[K_m:L] <= d_L^2.

If d_L<2^g, the sharper exponent [K_m:L]=m/g gives d_m<2^m. Taking minima gives d_all<=d_*<=d_all^2. All feasible sets are nonempty when N(J_o)<2^n, because the full field is feasible. This includes g=1 for arbitrary subfields and n=2 for the standard chain; no missing minimum is hidden at either endpoint.

Every subgroup of C_2 times a cyclic group has at most two generators: project to the cyclic factor, lift one generator of the image, and add a generator of the kernel, whose order is at most two. Hence at most n^2 ordered generator pairs suffice to enumerate every subgroup, with polynomial-size group closure/deduplication. Automorphisms act on the coefficient basis by signed permutations. Their invariant integer lattices can be obtained by solving the resulting signed-coordinate equalities; inconsistent signed cycles force zero, and each remaining component gives an integral generator. Contractions with the input ideal are computable by exact integer normal forms. Thus the larger enumeration has polynomial bit complexity in n and the complete A encoding, as claimed.

For completeness, the needed SV-SUBFIELD-v2 mechanism also reconstructs correctly. The prime 2 is totally ramified with (2)=P^n. If the 2-primary exponent of J is P^b, eligibility forces b<n, so the 2-primary additive exponent a is 1 or 2. With e=am and J_o=J+mR, the finite quotient decomposition gives a J_o subset J. The odd part has norm at most N(J), so g=n is feasible.

For a feasible g, s=ceil(log2(d_g+1))<=g. Enumerate d_g+1 distinct binary coefficient vectors in the first s standard subfield basis positions. Their reductions modulo J_o collide; the nonzero difference has coefficient norm at most sqrt(s), and multiplication by a gives a nonzero f in J with norm at most 2sqrt(g). Exact normal-form residues suffice and numeric d_g, not log d_g, pays for enumeration and storage. Since ||fw||_coef<=2sqrt(g)r, the strict guard 16r^2g<1 makes coefficient rounding of fT recover f lambda, followed by exact division by nonzero f in K.

The bounded-factor family in that dependency has a direct quantitative proof. For an odd prime p let f_g(p)=ord_(2g)(p). The elementary order formula for powers of two gives

    f_g(p)<=2+(g/n) f_n(p).

Indeed below the eventual doubling range the order is at most 2; in the doubling range it scales by g/n. Odd primes are unramified throughout this tower. If J_o is a product of at most t distinct P_i^(b_i), contractions can merge, which only decreases their norm relative to the product bound. Therefore

    log2 d_g
      <= sum_i b_i f_g(p_i) log2 p_i
      <= rho g + 2 sum_i b_i log2 p_i
      <= rho g + 2t log2 e.

The last inequality uses p_i^(b_i)<=e. With e<=n^C, take a power of two g>2tC log2(n)/(1-rho), still O(log n) and <=n for sufficiently large n. Then d_g<2^g is polynomial in n. The t bound is essential. This dependency therefore does not contradict DENSE's unbounded support example.

Combining ALL-SUBFIELDS with the exact dense contraction value gives d_all>=sqrt(p^t)=exp(Omega(n)). This concerns only the stated collision criterion.

## 11. ACTUAL-v3: uniform parameters, effective prime, and delivered radius

The authorized additional batch definitions give, with fixed b,c and positive valid input parameters,

    Ncal,Ntest = n^{O(1)},   K=k0(Ncal+Ntest)=n^{O(1)},
    ell=ceil(log2(2nK))=O(log n).

Their finite inputs include k0 and the represented routine costs; positivity of K is part of the valid domain because the formula for ell and the explicitly positive C require it. In particular this proof does not silently allow k0=0 and then evaluate log(0).

The common kappa can be chosen with polynomial value uniformly for 1<=D<=2^(rho n). In fact, a0,max(D) increases with D, so Smax(D) is largest at D=1. Substituting h0=delta w/(32nK),

    log a0,max(D)
      = log w +(log D)/n +(2/n)log(delta/(32nK))-log(nQmax).

Consequently Smax(1)=O(n log n). The tail inequality 3w exp(-kappa)<Qmin/(8D) is strongest at the largest D. One may conservatively use the exact integer 2^n in place of 2^(rho n), and add a fixed strict margin when taking a certified logarithmic ceiling. The other displayed lower bounds for kappa are polynomial: K,1/delta and log(1/zeta) are polynomial or logarithmic under the specified families. Thus kappa=n^{O(1)} is effective, with all bit costs charged.

Every displayed C8 loop expression is a fixed polynomial and logarithmic expression in kappa+200, so Q_*=n^{O(1)}. Thus epsilon_C is inverse polynomial and a=O(sqrt(log n))+O(1). The Up rule uses a certified rational approximation with fixed error, then an exact rational ceiling; it need not decide whether a transcendental quantity is an exact integer. This removes a potential precision ambiguity. The resulting a is determined before p and J.

Now

    C=epsilon_* ell^2/(1024 n K Qmax)

is positive represented rational with polynomial bit length and inverse-polynomial lower bound. Let H be a rational upper threshold exceeding Qmax, n^4-1, and (a+1)/C. Choose a power-of-two modulus q divisible by 2n and greater than H. Then q has polynomial value. By [Xylouris, Theorem 1.1](https://www.impan.pl/shop/en/publication/transaction/download/product/83078), the least prime p=1 mod q is at most a fixed effective constant times q^5.18. Thus p has polynomial value and p>=q+1>H. Exhaustive progression search with elementary deterministic primality testing is effective in polynomial numeric p; no efficient factoring assumption is required. Since q is divisible by 2n, p is completely split. This construction explicitly forces a lower threshold; the least split prime modulo only 2n would not do that.

Construct J from this p as in Section 9. This is now an effective family, with exponential norm but polynomial ordinary-basis encoding and polynomial numeric p. Set u=Cp and chi=ceil u. Since u>a+1>1,

    u<=chi<u+1,
    1/2 < u/(u+1) < u/chi <=1.

With the **actual** delivered radius r=C/chi, this is exactly

    1/2 < pr <=1.

There is no replacement by an illustrative radius. In particular 2pr>1, so the scalar-rounding sufficient guard fails. At the same time 8p^2r^2<=8, and t=Theta(n/log p)=o(n), so 8<n-t+1 for all sufficiently large n. Also r<=1/p<=n^-4<1/2, so the pointwise RS algorithm applies directly.

The new chi is an explicitly charged polynomial-value integer and satisfies chi>=a. The provided interface expressly permits this. Guards containing d0 or r only improve when chi increases. The supplied lower bound Qmin>=n sigma_floor and D^(1/n)<=2^rho also make the displayed d0 upper guard uniform in eligible D for sufficiently large n; in any case the inherited guards are explicit hypotheses of this corollary, not re-proved reduction claims. Common kappa and a were chosen before J, so no fixed-point dependence on D=N(J) occurs.

This proves the claimed witness at its delivered radius, including exponent p, trivial stabilizer, exponential norm, and exponential feasible collision indices. It says nothing comparable about the larger minimal-chi radius. The computational polynomial exponents may depend on the fixed family parameters; this is consistent with the stated quantifier order.

## 12. Complete resource accounting

Let L_A,L_T,L_r be the total bit lengths of the basis, target, and rational radius; charge every other supplied represented routine and parameter encoding as stated. Rational inversion, determinant/membership checks, exact rounding, and output construction have polynomial bit cost in these lengths and n. Exact integer normal forms are needed only for generic contractions; they are not ideal-factorization oracles.

Recognition and primitive-root searches are polynomial in numeric p, not claimed polynomial in log p. The same distinction applies to scanning F_p in the root recursion and to the effective split-prime construction. Once a polynomial-value p family is established, these become polynomial in n with constants/exponents depending on that family.

RS/GAP decoding uses a linear system of size at most n and polynomial-degree univariate arithmetic. LIST uses a linear system with N(d,t)=O((d+1)^2) columns and n(2B+1) rows, followed by O(t deg_Y Q) recursion nodes; each scans p field elements and handles degrees at most d+t deg_Y Q. Hence its stated polynomial dependence on n,p,d,B and the full encodings is valid. On valid instances d<n follows already from d<n-h and h>=0.

The generic subfield collision algorithm's resource is the numeric d_*. Dense d_*=p^t has O(n) bits but exponential value, so its failure to have a polynomial numeric enumeration bound is real. This does not make the ordinary ideal basis exponentially large: the explicit dense basis has polynomial size. Nor does it rule out RS, LIST, other short-member algorithms, lattice reduction, or direct BDD methods.

## 13. Conditional laws, CP-1, and probabilistic scope

The new decoder and family claims are deterministic. Error coordinates can be arbitrarily correlated or chosen adversarially: the only counting bound is the pointwise sum of squared coefficient errors. There is no multiplication of marginal success probabilities, posterior sample reuse, cache assumption, randomized prime search, or uncharged probabilistic factorization.

If a probability distribution is placed on valid inputs, conditioning on any positive-probability event that preserves the promises leaves the conditional failure probability exactly zero, because correctness holds separately on every remaining input. No independence statement is needed for that inference. Root maximization and list filtering are deterministic functions of exposed input data.

The inherited DD/FF interface may contain probabilistic arguments, but they are not present as proofs in this permitted packet; their validity is an explicit external assumption of ACTUAL-v3. This review certifies the stated parameter manipulation and source decoder conditional on that interface, not any unsupplied sampler law, adaptive composition, or sequential estimate.

The mandatory CP-1 regression was independently recomputed with exact Fractions. The preconditioning normalizer is 10/11. Posterior masses are A_b=21/2000, C_b=1/20, D=879/1000. Initial incidences are p(x)=1/10, p(e_b)=121/2000, p(f_b)=21/2000; none exceeds gamma=1/10. The selected two-hit event has probability

    21/2000 = 0.0105 > 1/100 = gamma^2.

After the selected first hit, the matching f incidence is

    (21/4000)/(21/4000+1/20)=21/221<1/10.

The matching adaptive first-hit mass is 2(A_b/2+C_b)=221/2000=0.1105, while the raw fixed-address incidence is 121/2000=0.0605. Thus local residual lightness does not restore the false product estimate. Support removal and Bayes normalization inflate the relevant first-stage mass; a latent cache-hit flag cannot be added to the algorithm's filtration. The present deterministic energy-counting proofs never use that rejected implication and need no substitute product bound.

## 14. Boundary and regression audit

Checked analytically: rational rho is handled by exact integer comparisons; t positivity is only asserted for sufficiently large n; odd t gives the stabilizer proof; t=1 is valid for RS/GAP and deliberately excluded from LIST's t-1 weights; t near n correctly shrinks the distance; split p ensures p does not divide n and all Fourier inverses exist; every strict radius/feasibility inequality remains strict; standard and arbitrary feasible minima are nonempty through the full field; n=2 and arbitrary degree-one subfields are covered; rounding ties are included in the error counts; list residues are distinct under 2B+1<=p; repeated and inseparable polynomial roots retain multiplicity in the recursion; candidate membership and lattice uniqueness are separate checks; p versus log p is explicit; ordinary-basis acquisition is constructive only for the displayed family and is otherwise supplied as input.

Executed exact regression: exit 0, 0.09 seconds wall time, peak RSS 12,288 KiB, within the granted 120-second/512-MiB limits. It checked 270 supports, 1,046 spectral basis vectors, 8,244 annihilator products, six root-recursion examples against 750 exhaustive candidate polynomials, and CP-1. These finite controls passed, including rejection of CP-1's old product claim. They do not constitute infinite verification. The epsilon mismatch was established algebraically and remains an exact-statement rejection despite all finite controls passing.

## 15. What remains outside this blind certificate

The original RS-v1 inherited-radius paragraph requires correction and fresh review of the changed text. No such repair has been read here. The inherited reduction's own theorem, success probabilities, external source acquisition in another reduction, and historical project regressions were not made available as mathematical input and are not certified. The local proofs above do not infer hardness or a complete source classification from their sufficient decoding criteria.

This report is sealed against the original allowed inputs and the definition-only addition. Later full-proof or repair review must be a separate artifact with its expanded exposure recorded.
