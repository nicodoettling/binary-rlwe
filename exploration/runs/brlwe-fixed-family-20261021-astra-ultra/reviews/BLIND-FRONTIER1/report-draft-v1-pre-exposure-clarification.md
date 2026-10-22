# BLIND-FRONTIER1: independent statement-only mathematical report

This is an unsealed working report. The immutable final report and seal will be
separate files. The author proofs have not been accessed.

## 1. Scope, exposure, and disposition

I received the six original frozen claims, the supplied SV-SUBFIELD-v2 dependency,
and the four later frozen claims. Their exact inputs and hashes remain in
`allowed-input/`, the original manifest, and the two addendum manifests. The
assignment and both later task messages are preserved verbatim. The exposure
inventories separately identify packet, methodology, permitted external-source,
and operational scheduling exposure. No author proof, author verdict, other
review, coordinator mathematical summary, or outside experiment result was read.

I independently derive all ten statements below. I found no mathematical
counterexample under the stated hypotheses. The mathematical disposition is
**proved under the frozen hypotheses and the expressly imported standard
theorems**, subject to the two interpretation notes in section 14. This is a
blind referee's mathematical assessment, not final programme certification.
For the programme ledger, the claims remain **PROVISIONAL pending coordinator
reconciliation** with the exact current dependencies, author artifacts, and other
regressions. Same-model review is correlated and is not formal verification.

| Frozen claim | Independent result | Main obligations checked |
|---|---|---|
| GAUSS-AVG-v1 | Proved; the argument below gives a stronger constant | Singular Gaussian laws, means, uniform cube average, retained S |
| FRAC-INFO-v1 | Proved | Fractional identification, Poisson normalization, composite q, fixed S, ML exponent, uniformity in J |
| WEIGHT-COV-v1 | Proved | Interior slice faces, arbitrary finite-second-moment joint law, deterministic mean |
| WEIGHT-GAUSS-v1 | Proved with stated constant | Exact slice coverage, Gaussian TV conversion, singular covariance and varying target means |
| SV-PRIME-SUPPORT-v2 | Proved | Odd-prime descent, exponent versus support, ordinary-basis algorithm, existence family |
| SV-ALL-SUBFIELDS-v1 | Proved when the indicated minima exist | Field containment, extension norm, ramification, polynomial enumeration and invariant bases |
| SV-DENSE-SPLIT-v1 | Proved with construction parameters explicit | Exact contraction indices, odd-support stabilizer, exponential index, basis construction |
| SV-RS-DECODE-v1 | Proved | Recognition from A, inverse-ideal Fourier support, rounding errors, exact BW decoding, lifting |
| SV-GAP-DECODE-v1 | Proved | Containing code, cyclic gaps, primitive-root optimization, actual radius |
| SV-LIST-DECODE-v1 | Proved | List agreement, interpolation, polynomial coefficient recursion, exact lattice uniqueness, constants |

No extension to hidden-secret marginal TV, arbitrary non-Gaussian approximate
kernels, efficient ML recovery, general source hardness, or a new reduction is
inferred. The sufficient source conditions can fail while a different algorithm
works; the dense-support and RS/list statements themselves illustrate this.

## 2. Common Gaussian comparison and Fourier facts

Write V_s=Cov(W_s), and F=Cov(Z,Delta). Direct expansion gives

    V_s = B - F M_s^T - M_s F^T + M_s C M_s^T.                 (2.1)

No independence between Z and Delta is used. The two are jointly Gaussian only
where a Gaussian distribution comparison is asserted. For finite second moments,

    ||V_s||op <= tr(V_s) <= 2 tr(B) + 2 ||M_s||op^2 tr(C)
              <= 2 tr(B) + 2 n^2 tr(C),                       (2.2)

because each T^j is orthogonal and s is binary. Thus the supplied explicit L is
valid; if its maximum is zero, any positive L can be selected instead.

For two real Gaussian laws with covariances V,V_* bounded by L I and arbitrary
means, characteristic functions at u/sqrt(L), for a real unit u, satisfy

    2 TV >= |phi(u/sqrt(L))-phi_*(u/sqrt(L))|
         >= |exp(-u^T V u/(2L))-exp(-u^T V_* u/(2L))|
         >= exp(-1/2) |u^T(V-V_*)u|/(2L).

The first inequality follows by integrating a complex function of modulus one;
the second discards phases; the third is the mean value theorem on [0,1/2]. Hence

    TV >= exp(-1/2) ||V-V_*||op/(4L).                         (2.3)

This covers singular and point-mass Gaussians; no density or inverse covariance
is needed. Target means may vary with s. Since both joint laws have the same
finite S marginal,

    TV(Law(S,W_S),Law(S,W'_S)) = E_s TV(Law(W_s),Law(W'_s)).  (2.4)

It is essential that S is retained. This identity does not lower-bound the TV
after S is hidden.

The orthogonal negacyclic shift has an orthonormal complex eigenbasis u_k with
eigenvalues lambda_k=exp(i theta_k), theta_k=(2k+1)pi/n. Put
c_k=u_k^* C u_k. Positive semidefiniteness gives c_k>=0 and sum c_k=tr(C).
For a real symmetric matrix H, |u_k^* H u_k|<=||H||op even for these complex
vectors. Thus a lower bound on a Fourier diagonal can bound the real operator
norm without pretending that C is diagonal or circulant.

## 3. GAUSS-AVG-v1

For any fixed settings of coordinates 2,...,n-1, the alternating covariance sum
over the four choices of (s_0,s_1) is

    V_00 - V_10 - V_01 + V_11 = Q := C T^T + T C.           (3.1)

The constant, linear, and base-coordinate terms cancel. Replacing every V by
V-V_* leaves the same identity. The triangle inequality on each face, followed
by averaging all faces, gives

    E_s ||V_s-V_*||op >= ||Q||op/4.                         (3.2)

This uses faces covering the whole cube, not four rare individual secrets.
For n>=4 a power of two, |cos theta_k|>=sin(pi/n)>=2/n. Also

    u_k^* Q u_k = 2 cos(theta_k) c_k.

Choose k with c_k>=tr(C)/n. Then

    ||Q||op >= 4 tr(C)/n^2,
    E_s ||V_s-V_*||op >= tr(C)/n^2.

Combining with (2.3)-(2.4) proves the stronger bound

    joint TV >= exp(-1/2) tr(C)/(4 n^2 L),

and therefore the stated bound with denominator 16 n^2 L. No assumption about
Gaussian means, nonsingularity, or a sample-only distinguisher was introduced.

The degree exclusion is real. At n=2, let Delta be centered isotropic Gaussian
and Z=(I+T)Delta/2. For all four binary secrets, Z-M_s Delta has the same
isotropic covariance and zero mean: the four centered coefficient choices lie
on a circle. Here C is nonzero. The Fourier cosine used above vanishes.

The asymptotic conclusion follows only when tr(C) has an inverse-polynomial
lower bound and L has a polynomial upper bound in the fixed security parameter.
Changing another parameter while losing either scale is outside that conclusion.

## 4. WEIGHT-COV-v1 and WEIGHT-GAUSS-v1

Let A=I-T^2 and H=T-T^3. For any binary base z on coordinates 4,...,n-1 of
weight w-2, consider the four secrets obtained by choosing exactly one of
coordinates {0,2} and exactly one of {1,3}. The alternating covariance sum is

    Q_w = A C H^T + H C A^T,                               (4.1)

independently of z, B, F, and the target covariance. Every such base exists for
2<=w<=n-2. On a Fourier eigenvector,

    u_k^* Q_w u_k = 8 sin^2(theta_k) cos(theta_k) c_k.       (4.2)

None of the scalar factors vanishes at the odd n-th angles when n>=4 is a power
of two. Thus if every V_s is the same matrix, Q_w=0 implies every c_k=0 and
therefore C=0. This establishes the covariance part for any finite-second-moment
joint law.

If the full W_s laws agree, C=0 makes Delta a deterministic vector d. Equality
of the finite means then makes (M_s-M_t)d=0 for every pair of slice secrets.
Choose two secrets differing only by a swap of coordinates 0 and 1. Such a pair
exists throughout the interior range. This gives (I-T)d=0. Since 1 is not an
eigenvalue of T, d=0. Hence Delta=0 almost surely, as claimed.

For the quantitative statement, fold theta_k to an angle a in
[pi/n,pi/2-pi/n]. If a<=pi/4, sin^2(a)cos(a)>=4/(sqrt(2)n^2)>=2/n^2.
If a>=pi/4, the same product is at least (1/2)(2/n)=1/n>=2/n^2.
Consequently (4.2), with a k having c_k>=tr(C)/n, gives

    ||Q_w||op >= 16 tr(C)/n^3.                            (4.3)

The number of secrets covered by these four-pattern faces is exactly
4 binom(n-4,w-2). Their fraction in the slice is

    4 binom(n-4,w-2)/binom(n,w)
      = 4 w(w-1)(n-w)(n-w-1)/(n(n-1)(n-2)(n-3)) = p_w.    (4.4)

These faces are disjoint for the fixed coordinate pairing. On each face the
sum of four ||V_s-V_*||op is at least ||Q_w||op. The remaining secrets only
increase the nonnegative average, so

    E_{|s|=w} ||V_s-V_*||op >= (p_w/4)||Q_w||op
                              >= 4 p_w tr(C)/n^3.

Equation (2.3) now gives exactly the stated
exp(-1/2) p_w tr(C)/(n^3 L). V_* must be the same covariance throughout this
slice; target means need not be the same. Conditioning on w and then averaging
under binom(n,w)/2^n is justified by (2.4), without any product of marginal bounds.

At w=1, Z=0 and isotropic centered Gaussian Delta work because each M_s=T^j
is orthogonal. At w=n-1, Z=M_1 Delta gives W_s=T^j Delta. At w=0,n the slice is
a singleton. Thus the exclusions are substantive. A covariance lower bound
alone cannot give a non-Gaussian TV obstruction: take Delta=0 with probability
1-eta and Delta=+/-eta^(-1/2)u each with probability eta/2, and Z=0. Its covariance
is uu^T, but every residual law has TV at most eta from the point mass at zero.
This does not contradict the exact covariance theorem.

## 5. FRAC-INFO-v1

### 5.1 The fractional residue experiment

Write Lambda=J^-1 in the coefficient Euclidean coordinates. Since J is integral,
R=Z^n is contained in Lambda. Its Euclidean dual satisfies Lambda^* subset Z^n.
The quotient R/J has size D, so D belongs to J, and D Lambda subset R. Since
(D,q)=1, the stated map a=v/D -> v D^(-1) mod q is well-defined and has kernel
q Lambda. Equivalently R/qR -> Lambda/qLambda is an isomorphism because q acts
invertibly on Lambda/R. This is an algebraic identification, not an assumption
that fractional coefficients can be reduced by an arbitrary denominator.

For a nontrivial character h of R/qR, with h in Z^n nonzero modulo q, choose an
integer c with Dc=1 mod q. Its pullback to Lambda is the frequency

    u=(Dc/q)h,   q u in Lambda^*,   u mod Z^n = h/q mod Z^n.

Every point of Lambda^*+u has Euclidean distance at least 1/q from zero.
Poisson summation gives the exact, positive, real characteristic value

    E_{a~D_(Lambda,s)} exp(2pi i <u,a>)
       = sum_{v in Lambda^*} exp(-pi s^2 ||v+u||^2)
         / sum_{v in Lambda^*} exp(-pi s^2 ||v||^2).        (5.1)

The denominator is at least 1. Split the exponent in the numerator into equal
halves and use the distance lower bound. The remaining shifted-lattice sum is
at most the shifted Z^n sum, whose maximum occurs at the integer shift. This
last fact follows immediately from one-dimensional Poisson summation with
positive Fourier coefficients. Therefore (5.1) is at most

    exp(-pi s^2/(2q^2))
       (sum_{z in Z} exp(-pi s^2 z^2/2))^n = 1-mu          (5.2)

when mu>0. The bound is uniform in J and does not silently assume a scalar
ideal basis. Composite q causes no difficulty.

### 5.2 Pairwise separation

For distinct binary b,c, choose a nonzero coefficient of c-b, equal to +1 or -1.
The corresponding coefficient functional of A(c-b) is a nontrivial character
of A: on the input A=1 it already has value +1 or -1 modulo q. For this output
coordinate use the bounded complex test

    phi(A,B)=exp(2pi i [B-Ab]_j/q).

Under secret b its expectation is eta, the exact discrete-Gaussian error
characteristic value at 1/q. Under secret c it is eta times the source
characteristic value in (5.1). By one-dimensional Poisson summation,

    eta = sum_{z in Z} exp(-pi sigma^2(z+1/q)^2)
          / sum_{z in Z} exp(-pi sigma^2 z^2)
         >= gamma.

The source and error variables are independent, which justifies this single
product. Thus the test-expectation gap is at least gamma mu, and TV(P_b,P_c)
is at least gamma mu/2=delta. No conditioning on a selected successful prefix
has occurred, and no sequence of marginal lightness bounds is multiplied.

### 5.3 Fixed secret and many samples

Conditioned on S=b, all K physical samples have law P_b tensor K. The same b is
used in every sample. For any other c, the probability under b that c's
likelihood is at least b's is at most the K-th power of their affinity

    H(P_b,P_c)=sum_x sqrt(P_b(x)P_c(x)).

This follows by summing P_b^K on the likelihood-ratio event and bounding it
pointwise by sqrt(P_b^K P_c^K). The finite alphabet handles zero probabilities
without division. Cauchy-Schwarz gives H<=sqrt(1-TV^2)<=exp(-delta^2/2).
A union bound over c != b proves the stated ML conditional failure bound,
including arbitrary fixed tie-breaking and the cap at 1. The estimator is a
finite-alphabet statistical rule; no polynomial implementation or exact
transcendental comparison procedure has been asserted.

In fact the common source factor P_A(A_i) cancels when comparing secret
likelihoods. Thus the ML decision rule can be chosen independently of J for
fixed q and sigma, as well as having a performance bound uniform in J. It is
still a statistical estimator here, not an asserted efficient attack.

### 5.4 Asymptotic constants and quantifiers

For the stated fixed polynomial-value q family, ell=Theta_B(log n), s^2=2ell^4,
and a=pi ell^4/q^2 tends to zero. The theta tail in U is

    U-1 = O(n exp(-pi ell^4)),

using the elementary bound sum_{z>=1} exp(-u z^2)<=exp(-u)/(1-exp(-3u)).
Since q<=n^B, this error is o(a). Hence mu=Theta(a)>0 eventually. For
sigma=n^2 and q>=n^4, gamma tends to 1: its numerator is at least
exp(-pi/n^4), and its denominator is 1+O(exp(-pi n^4)). Thus
delta=Omega(ell^4/q^2)=Omega(s^2/q^2), with constants independent of J.

With K=n q^4, K delta^2=Omega(n ell^8). The extra factor 2^n is absorbed, giving
exp(-Omega(n(log n)^8)). This proves statistical recovery uniformly for each
eligible J coprime to q. It does not promise efficient recovery. Additional
revealed variables can be ignored by an estimator, so cannot restore an upper
bound against every estimator. It would be invalid to replace fixed S by fresh
S for each sample and reuse this tensor-product argument.

## 6. SV-SUBFIELD-v2 dependency and the inherited radius

The frozen dependency is expressly supplied as a theorem. I also checked its
mechanism because the later statements use its algorithm and its numeric
resource bound. The additive exponent e is the least positive integer with
e A^(-1) integral, hence the lcm of reduced entry denominators. This is computable
by exact rational linear algebra with polynomial bit complexity.

The unique prime above 2 has ramification degree n and norm 2. If its exponent
in J is b, eligibility gives b<=rho n<n; hence its additive exponent is 1 or 2.
Thus a in {1,2}. With m=e/a odd, J+mR removes the 2-primary component and keeps
the odd part. Multiplication by a sends J_o into J. This step does not treat
ramified powers as unramified contractions.

Exact integer normal forms compute each coefficient-embedded intersection
J_o intersect R_g and its index d_g. Since d_n=N(J_o)<=N(J)<2^n, at least one
choice is feasible. If d_g<2^g then k=ceil(log2(d_g+1))<=g. There are d_g+1
distinct binary vectors on these k basis positions, so two collide modulo J_o.
Their nonzero difference has coefficient norm at most sqrt(k)<=sqrt(g).
Multiplying by a produces 0!=f in J with ||f||_2<=2sqrt(g). Enumeration costs
polynomial in the numeric d_g, not its logarithm; the minimum-index choice has
the stated bound in numeric d_*.

For T=lambda+w, f lambda is integral. Parseval in the coefficient embedding is

    ||v||_2^2 = (1/n) sum_sigma |sigma(v)|^2.

It gives ||f w||_2<=r||f||_2<=2r sqrt(g). Under 16r^2g<1 every coefficient error
is strictly below 1/2, so rounding fT recovers f lambda and division by nonzero
f in the cyclotomic field recovers lambda. Input and output bit lengths are
charged; a nonscalar or badly conditioned integer basis is not replaced by a
short-basis oracle.

For the actual supplied radius, writing ell=ceil(log2(2nK)),

    Qmax >= n sigma_floor >= 8 n^3 sqrt(Kn) ell^4,
    r <= 1/(8192 n^4 K sqrt(Kn) ell^2) < 1/(4sqrt(n)).     (6.1)

Here epsilon<=1, chi>=1 and K>=1 were used, and ell>=1. This is a strict and
very conservative bound. Therefore 16r^2g<1 for every g<=n. Nothing here changes
the delivered radius or reverses a Gaussian-sampling implication.

At rho=0, N(J)<=1 forces J=R, e=a=1, J_o=R and d_*=1. The algorithm and radius
argument remain valid. Positive-rho existence examples below do not purport to
exist at rho=0.

## 7. SV-PRIME-SUPPORT-v2

For an odd p write f_g(p)=ord_(2g)(p). Odd primes are unramified throughout the
2-power cyclotomic tower. If P lies above p, then P^b intersect R_g is the b-th
power of its contracted prime. Several P_i may contract to the same prime;
their exponents then combine by a maximum, which is no larger than their sum.
Thus

    log2 d_g <= sum_i b_i f_g(p_i) log2 p_i.               (7.1)

For all allowed g, the elementary order formulas give

    f_g(p) <= (g/n) f_n(p) + 2.                           (7.2)

For completeness: if p=1 mod 4 and u=v_2(p-1)>=2, then
f_g=2^max(0,log2(2g)-u). If p=3 mod 4 and v=v_2(p+1)>=2, then
f_g=2^max(1,log2(2g)-v). These formulas follow by successively squaring an odd
integer and tracking the exact 2-adic valuation. The order either stays at 1
or 2 or doubles along the tower, immediately giving (7.2).

Since log2 N(J_o)=sum_i b_i f_n(p_i)log2 p_i<=rho n, equations (7.1)-(7.2) give
the claimed log2 d_g<=rho g+2 B(J_o). If B<=C log2 n, choose a power of two g
strictly above 2C log2 n/(1-rho), with a fixed extra margin. For all large n it
is at most n and is O(log n); then d_g<2^g=n^O(1). The supplied algorithm finds
a d_* no larger, without computing B or knowing C.

At an odd p, the p-primary part of the additive exponent is p^max_{i:p_i=p} b_i.
Therefore at most t prime ideals above each p implies

    B(J_o) <= t sum_p max_{i:p_i=p} b_i log2 p
             = t log2(m) <= t log2(e) <= t C log2 n.       (7.3)

This proves the broader family claim. It is a bound on numeric e, not merely
on the number of bits needed to write e. The number of different p need not be
bounded, and the algorithm still uses only the ordinary basis.

An explicit existence family can be specified as follows. Fix a large constant
j0>=2. For j>=j0 choose the least prime p_j=1+2^j mod 2^(j+1). Effective Linnik
with exponent 6 gives log2 p_j<=c+6(j+1), and v_2(p_j-1)=j exactly. Put
h=floor(sqrt(log2 n)) and take one prime ideal above each p_j, j0<=j<=h.
Also take one prime ideal above a completely split prime p_0(n)=1 mod 2n with
p_0(n)<=C_0(2n)^6. For large n these rational characteristics are distinct.

The additive exponent is their product, with logarithm O(h^2+log n)=O(log n).
For j<=h<log2(2n), f_n(p_j)=n/2^(j-1). The norm logarithm divided by n is
at most

    sum_{j>=j0} [c+6(j+1)]/2^(j-1) + O(log n/n).

Choose j0 so this tail is below rho/2. Eligibility then holds for all sufficiently
large n. The fixed first prime p_j0 contributes a positive constant times n to
log2 N(J), so the norm is exponential. The number of prime ideals tends to
infinity. A lone prime above the completely split p_0(n) has trivial decomposition
group; any automorphism stabilizing the whole ideal must fix that prime, because
it cannot change rational characteristic. Hence the full stabilizer is trivial.

This is a scope example, not an oracle for a hidden ideal. One may fix the least
irreducible factor at each p_j to make the prime choice definite. If constructive
basis generation is desired, squarefree finite-field factoring with numeric-p
cost can be implemented by Frobenius fixed-space linear algebra and gcd splits
over all field constants; it does not require an ideal-factorization oracle in
the decoder. The decoder's theorem begins with the ordinary basis supplied.

## 8. SV-ALL-SUBFIELDS-v1

For n>=4, the Galois group is C_2 x C_(n/2), with the cyclic factor generated by
5 modulo 2n. If H fixes L and [G:H]=g, then g is a power of two. The index of
H intersect <5> in <5> is at most g. It is a power of two dividing g, so
5^g belongs to H. When 2g<=n, the kernel of restriction from K_n to K_(2g)
is <5^g>; hence L is contained in K_(2g). When 2g>=n, containment in K_n is
automatic. This proves m=min(2g,n), L subset K_m, with [K_m:L]=m/g<=2.
The case n=2 is immediate; in particular L=Q maps to m=2, not to an absent
degree-one member of the standard chain.

Set I=J_o intersect O_L. Since J_o is an ideal,

    I O_(K_m) subset J_o intersect O_(K_m).

Taking indices and using the extension norm identity gives

    d_m <= [O_(K_m):I O_(K_m)] = [O_L:I]^[K_m:L]
         = d_L^[K_m:L] <= d_L^2.                          (8.1)

This argument is valid even at ramified primes. It does not assume equality
between contraction and extension, or the unramified prime-power formula used
in section 7. If d_L<2^g, (8.1) gives d_m<2^(g[K_m:L])=2^m. Thus every feasible
arbitrary subfield has a feasible standard one with index at most its square.
The standard chain is a subset of all subfields, proving

    d_all <= d_* <= d_all^2

whenever these minima exist. N(J_o)<2^n supplies a feasible choice K_n, so the
eligible setting of the dependency always has nonempty feasible sets.

Every subgroup of C_2 x C_(n/2) is generated by at most two elements: its
intersection with the cyclic factor is cyclic, and at most one additional
element lifts the other C_2 coordinate. Thus enumerating all pairs of the n
automorphisms, closing their generated groups, and deduplicating takes polynomial
time in n. Each automorphism acts by a signed coefficient permutation. The
integer kernel of the two corresponding fixed-point equations is exactly
R_n intersect L=O_L. Integer normal forms give its integral basis and compute
its intersection index with J_o in polynomial bit complexity. There is no
exponential number of unenumerated subfields in this rank-two group.

This proves equivalence of polynomial numeric contraction criteria; it does not
rule out different short-member constructions or other decoding algorithms.

## 9. SV-DENSE-SPLIT-v1

Let roots be beta_j=alpha^(2j+1), j modulo n. The split prime ideals are distinct
and pairwise coprime, of norm p. Their squarefree product over t roots has norm
p^t and additive exponent p. With ell=ceil(log2 p) and t the largest positive
odd integer at most floor(rho n/ell), eligibility is immediate. Because
log p=Theta(log n), t=rho n/ell+O(1), and

    log(p^t)=Theta(n).

For Y=X^(n/g), beta_j maps to alpha^((2j+1)n/g), and two roots give the same
restricted prime exactly when their j indices coincide modulo g. The consecutive
set {0,...,t-1} has min(t,g) distinct residues modulo g. Since p is unramified,

    d_g=p^min(t,g).                                       (9.1)

If g<=t, p^g>=2^g, so no such g is feasible. If g>t, the index equals p^t,
and feasibility is exactly g>t log2 p. Thus every feasible g has the same
index p^t and d_*=p^t. At least g=n is feasible by eligibility. Equation (8.1)
then implies d_all>=sqrt(d_*) when the all-subfields statement is used.

For the stabilizer, the odd residue classes modulo 2n form the Galois group
acting freely on itself by multiplication. If a subgroup preserves a set of
odd cardinality t, every orbit has size the subgroup's power-of-two order;
that order divides t and must be 1. This proves trivial full stabilizer and
does not rely on an informal assertion about interval asymmetry.

Given n and p, a primitive 2n-th root can be found by enumerating field elements
and testing alpha^n=-1. The evaluation equations at the chosen roots define a
linear kernel modulo p. Its inverse image in Z^n, generated by lifted kernel
vectors together with p I, gives an ordinary integer ideal basis after normal
form reduction. All this has polynomial cost in n, numeric p and the encodings.
The interpretation of obtaining a separately prescribed p(n) is discussed in
section 14; no claim about evaluating an arbitrary slow family generator is
needed for this construction from its parameter p.

The conclusion concerns failure of this sufficient collision criterion. It is
not a lower bound on decoding complexity, as the next sections demonstrate.

## 10. SV-RS-DECODE-v1

### 10.1 Recognition and coefficient code

Compute the additive exponent from the ordinary basis. In the promised class
it is p; primality can, if necessary, be checked by trial division in time
polynomial in numeric p. Check p=1 mod 2n. Enumerating alpha with alpha^n=-1
finds exactly the primitive 2n-th roots. For each alpha, evaluate the supplied
basis at beta_j=alpha^(2j+1) modulo p and record where every basis vector
vanishes. Since pR subset J, ideals in R/pR=F_p^n correspond exactly to subsets
of its CRT coordinates. Thus these evaluations recognize the support without
an ideal factorization. One checks whether it is a cyclic interval of size
1<=t<n, for some enumerated alpha. All computations use polynomial numeric-p
cost and charge the full basis encoding.

Let J_c be the product of complementary split primes. Since JJ_c=pR,

    p J^-1=J_c.

Thus a=p lambda is an integral coefficient vector whose finite-field evaluations
vanish outside the chosen support. Inverse negacyclic Fourier transformation
gives, for k=0,...,n-1,

    a_k mod p = (alpha^(-k)/n) sum_{j=0}^{t-1} z_j x_k^j,
    x_k=alpha^(-2k).                                      (10.1)

The x_k are distinct and all multipliers alpha^(-k)/n are nonzero. This is a
generalized Reed-Solomon code of dimension t and distance n-t+1, since a
nonzero polynomial of degree<t has at most t-1 roots. A cyclic support shift u
adds the nonzero multiplier x_k^u, including when the interval wraps around n.

### 10.2 Rounding, exact decoding and lifting

Let y=round(pT) coefficientwise with a fixed tie rule. Write a=p lambda. Every
coordinate where y differs from a as an integer has |p w_k|>=1/2. A coordinate
error modulo p is a subset of these integer differences. Parseval gives
sum_k |w_k|^2<=r^2, hence the received word has at most

    E=floor(4p^2r^2)

symbol errors. The guard 8p^2r^2<n-t+1 implies 2E<n-t+1.

Here is an explicit linear-algebra decoder. Divide out the GRS multipliers.
Let k=t and seek a monic locator E(X) of degree E and Q(X) of degree<k+E with

    Q(x_i)=y_i E(x_i) for all i.

These equations are linear in their unknown coefficients. A solution exists:
take the product of the actual error locators and multiply by a monic polynomial
to reach degree E, and multiply that locator by the true message polynomial.
For any solution, Q-E f_true vanishes at at least n-E positions while having
degree at most k+E-1. The strict guard makes n-E>k+E-1, so it is identically zero.
Polynomial division therefore recovers f_true from every solution, without
factoring the locator or guessing the errors.

The resulting residues specify each lambda_k modulo Z. Since |w_k|<=r<1/2,
there is a unique lift in that coset at distance less than 1/2 from T_k. Exact
rational rounding recovers it. Membership in J^-1 can also be checked exactly
by multiplying by every supplied basis element. There is no test of an
irrational canonical norm in the implementation.

Substituting the actual radius gives exactly

    8 p^2 epsilon^2 ell^4
      < (n-t+1)(1024 n K chi Qmax)^2.                     (10.2)

The existing guards imply r<1/2 by (6.1). Numeric p must be polynomial for this
to be a polynomial-time family. Merely having polynomial bit length of p is
not enough. At r=1/p, the guard is n-t+1>8 and the scalar guard 2pr<1 fails;
this is an illustrative radius, not an assertion about a particular DD input.

## 11. SV-GAP-DECODE-v1

The same recognition procedure handles every nonempty proper split-prime
support. Suppose consecutive selected indices have a cyclic gap g. The other
cyclic interval, including both selected endpoints, has length n-g+1 and contains
the entire support. The Fourier code in (10.1) is therefore contained in a GRS
code of dimension n-g+1 and distance g. Apply the exact decoder just proved
with E=floor(4p^2r^2). The guard 8p^2r^2<g makes 2E<g, so the true word is the
unique containing-code word within the error radius. Extra codewords in the
containing code cannot change that conclusion.

For any primitive root, the t positive cyclic gaps sum to n; their largest is
at least ceil(n/t). Enumerating all primitive roots and all their gaps computes
g_max and a maximizing interval in polynomial numeric-p cost. This optimization
depends on J only, not on the unknown target lambda. The singleton convention
g=n gives dimension 1, as it should.

If p^t<=2^(rho n), with rho>0, then n/t>=log2(p)/rho. Thus

    8p^2r^2<log2(p)/rho <= g_max

is sufficient. The exact inherited-radius condition is

    8 p^2 epsilon^2 ell^4
      < g_max (1024 n K chi Qmax)^2,                     (11.1)

or the same with log2(p)/rho as a sufficient right-hand factor. It is not an
automatic consequence of p having some unspecified polynomial upper bound.

## 12. SV-LIST-DECODE-v1

### 12.1 Lists and interpolation

Use the exact consecutive-support GRS description, with nonzero multipliers
c_i. Form the residue lists

    L_i = {c_i^(-1)(round(pT_i)+v) mod p : -B<=v<=B}.

They have exactly 2B+1 distinct entries because 2B+1<=p. If the true normalized
code symbol is absent, then |p w_i|>=B+1/2. (A large integer rounding difference
may wrap back into the list modulo p; that only reduces the number of bad
positions.) Thus at most

    h=floor(p^2r^2/(B+1/2)^2)

positions fail to contain the true value. The N(d,t) monomials X^i Y^j with
i+(t-1)j<=d span the specified interpolation space. There are n(2B+1) homogeneous
vanishing constraints, so the strict dimension inequality gives a nonzero Q.
For the true degree<t polynomial f, Q(X,f(X)) has degree at most d and at least
n-h distinct roots. Since d<n-h, it vanishes identically.

### 12.2 Polynomial root enumeration without a factorization oracle

The following coefficient recursion is sufficient and polynomial with numeric-p
cost. Initially divide Q by the largest common power of X among its monomials.
At a node with normalized nonzero Q_node, Q_node(0,Y) is a nonzero univariate
polynomial. Scan gamma in F_p for all its roots. Each root extends the current
coefficient prefix by gamma; substitute Y=gamma+X Y and again divide out the
largest common X power. Continue for t coefficient positions. At each leaf,
test the original identity Q(X,f(X))=0 exactly and keep precisely the roots.

Every polynomial root follows one of these branches by its successive
coefficients. To prove a polynomial tree bound, let gamma have multiplicity m
in Q_node(0,Y). After translation Y -> gamma+Y there is a nonzero X^0 Y^m term
and no smaller Y-degree term with X degree zero. After Y -> X Y, the smallest
X degree nu is at most m. The new normalized polynomial at X=0 has Y degree at
most nu<=m. Summing over distinct gamma, the children's leading Y degrees total
at most the parent's leading Y degree. The number of children is also at most
that degree. Therefore at every depth there are at most the original deg_Y Q
active prefixes (constant leading polynomials die immediately), including in
positive characteristic and for inseparable roots.

There are t levels. Before normalization, after h levels the polynomial has the
form Q(X,f_<h(X)+X^h Y), so its X degree is at most deg_X Q+h deg_Y Q. Both
degrees and the number of coefficients remain polynomial in d and t. Each
node scans at most p constants and uses exact polynomial arithmetic. The whole
procedure is polynomial in numeric p, d,t and the encodings. It does not expand
an uncontrolled p^t prefix tree or assume a bivariate factorization oracle.

### 12.3 Exact lattice selection

Each enumerated code polynomial specifies coefficient residues a_i mod p.
For each coordinate take its unique possible lift lambda_i near T_i; a tie at
distance 1/2 cannot pass a radius r<1/2 test. Check membership in J^-1 and the
rational squared Euclidean inequality ||T-lambda||_2^2<=r^2. The true lambda
passes, since canonical infinity error <=r implies coefficient Euclidean error
<=r by Parseval.

There can be at most one passing lattice point. If lambda and lambda' both
passed, their nonzero difference v belongs to J^-1 and satisfies ||v||_2<=2r.
The integral ideal vJ has positive integer norm, so

    |N(v)| D_J >= 1.

On the other hand, AM-GM and Parseval yield

    |N(v)| = product_sigma |sigma(v)|
            <= ((1/n)sum_sigma |sigma(v)|^2)^(n/2)
            = ||v||_2^n <= (2r)^n.

This contradicts the exact strict guard (2r)^n D_J<1. A small polynomial root
list alone would not supply this uniqueness; the membership and norm argument
are necessary parts of the algorithm.

### 12.4 Explicit regime and actual radius

Let x=n/(64t)>=1, B=floor x and d=n/2. Since n is a power of two and n>=64t,
d is integral. The first floor(d/(2(t-1)))+1 summands of N each exceed d/2,
so N>n^2/(16t). Meanwhile

    n(2B+1) <= n^2/(32t)+n <= 3n^2/(64t) < n^2/(16t).

Also B+1/2>=x/2 and the stated pr bound is pr<=sqrt(n)x/4. Consequently
h<=n/4, and d=n/2<n-h. The split-prime condition p>=2n+1 implies 2B+1<=p.
These conservative estimates verify every interpolation/list condition.

For eligible D_J<=2^(rho n) and the actual r<1/(4sqrt(n)),

    (2r)^n D_J < (2^(rho-1)/sqrt(n))^n < 1.

Thus the lattice uniqueness guard is indeed automatic at the delivered radius.
The separate sufficient list-radius condition substitutes to

    p epsilon ell^2/(1024 n K chi Qmax)
        <= n^(3/2)/(256t),                               (12.1)

along with n>=64t and the existing guards. For dense t=Theta(n/log p), the right
radius scale is Theta(sqrt(n) log(p)/p), and n>=64t eventually holds. This does
not assert that every arbitrary fixed polynomial p family satisfies (12.1) at
every delivered parameter choice.

## 13. Registered finite falsification and source checks

Both experimental jobs were registered before execution and each received an
explicit fresh LIGHT slot. Both ran under a 120-second timeout, a 512-MiB address
space limit, a 110-second CPU cap, and a five-second termination grace. Their
complete scripts, outputs, time metrics and execution records are preserved.
Each exited 0 in 0.33 seconds with maximum RSS 12,288 KiB. No background process
or unpreserved temporary experiment data remains.

The first job reconstructed CP-1 exactly: vk probability 10/11; posterior masses
21/2000, 1/20, 879/1000; incidences 1/10, 121/2000, 21/2000; two-hit probability
21/2000>1/100 despite residual posterior 21/221<1/10. The relevant first-stage
mass changes from 121/2000 to 221/2000 after the cached-prefix transfer. The test
correctly rejects the old sequential product claim. The mechanism is selected-support restriction
and Bayes normalization, not merely correlation of oracle values. None of the
proofs above branches on latent cache-hit status or multiplies such residual
marginals. The source-noise expectation and the affinity tensor power use
explicit independent variables under fixed S, and are different statements.

It also checked 1,088 exact covariance instances, 272 cube faces, 68 slice faces
and exact coverage counts; 270 small prime supports, 2,092 primitive-root support
changes, 273 GRS nonsingular minors and 571 Berlekamp-Welch received words; and
4,194 pairs of finite rational laws with one- and two-sample likelihood bounds.
Covariance examples included zero, rank-one, isotropic and other PSD matrices
with nonzero cross covariance. The finite-field cases used (n,p)=(2,5),(4,17),
(8,17). The finite probability vectors were normalized squares of entries
0,1,2,3 on alphabets of size 2 or 3, so the affinity inequalities could be tested
exactly after squaring. These are bounded regressions, not proofs of the
unrestricted statements.

The second job compared the complete root-recursion output with exhaustive
polynomial enumeration for 1,415 bivariate polynomials over F_2,F_3,F_5 plus
special repeated, inseparable, X-divisible, and spurious-prefix cases: 2,878
comparisons total. The child-degree budget was checked at every level. It also
checked 120 convenient-regime parameter choices for powers of two 128<=n<=4096
and all 2<=t<=n/64. Every exact check passed. No Gaussian or lattice tail was
truncated; no numerical evidence was used to certify an infinite law.

Only the three permitted external primary sources were accessed:

* [Milne, Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  version 3.08: the relevant ideal, norm and cyclotomic results were checked in
  sections 3, 4 and 6. Their applications above, including the maximum rule for
  merging contractions and the extension-index inequality, were derived here.
* [Kannan-Bachem, publisher abstract](https://epubs.siam.org/doi/abs/10.1137/0208040)
  expressly states polynomial binary complexity for normal forms and multiplier
  matrices. Only the abstract/metadata was accessed and read; this is not a
  claimed audit of the full paper's algorithm or proof.
* [Xylouris, Theorem 1.1](https://www.impan.pl/shop/en/publication/transaction/download/product/83078)
  gives the effective least-prime exponent 5.18, so the weaker exponent 6 used
  in the construction is justified. The theorem statement and introductory
  context were checked, not the whole analytic proof.

The imported standard results retain their normal mathematical role. This
report does not claim formal verification of those sources or their full proofs.

## 14. Interpretation notes, dependencies, and remaining certification work

Two wording points should remain explicit when these statements are integrated:

1. The minimum d_all and the minimum feasible standard-chain index are defined
   only when the feasible set is nonempty. The theorem's N(J_o)<2^n condition,
   automatically present for eligible source instances, supplies this. The
   comparison for an arbitrary nonzero ideal should be read conditionally on
   nonemptiness; no minimum of an empty set is silently assigned.
2. The dense-split basis construction is polynomial given its construction
   parameter p (and can find alpha itself). Merely calling an arbitrarily
   prescribed n -> p(n) family effective and polynomial-valued does not prove
   its generator is polynomial-time. No end-to-end promise for such a deliberately
   slow generator follows. A concrete least-prime progression construction with
   an effective polynomial bound, or p supplied as a parameter, removes this
   interpretation issue. The ordinary-basis decoding statements do not acquire
   a hidden basis and are unaffected.

The dependency chain in this report is explicit. Gaussian claims use (2.1)-(2.4)
and Fourier positivity; fractional information uses the exact source/error law,
Poisson, and affinity tensorization; prime-support classification uses the
supplied subfield decoder plus odd-prime orders; arbitrary-subfield comparison
uses only the Galois group and ideal extension norm; dense support uses that
comparison only for its optional d_all conclusion; RS decoding is proved from
CRT, Fourier inversion and polynomial interpolation; gap decoding uses the RS
linear decoder with a containing code; list decoding uses the same coefficient
code, its separately proved root recursion, and the exact norm uniqueness guard.

Changing any frozen hypothesis reopens the corresponding downstream use. In
particular, dropping coprimality with D, hiding S, refreshing S between physical
samples, allowing perturbations to depend on more than the weight, using ramified
prime-power descent without adjustment, substituting bit length for numeric p or
d_*, or replacing the actual radius by an illustrative radius is not certified.

No author proof has yet been compared with this independent argument. Completing
this referee report does not terminate the protected discovery programme. The
coordinator retains responsibility for the final ledger, repairs, artifact
reconciliation and programme verdict.
