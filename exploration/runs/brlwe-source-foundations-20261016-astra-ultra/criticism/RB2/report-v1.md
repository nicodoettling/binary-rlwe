# RB2 independent blind report, version 1

## Identity, frozen input, and verdict

Reviewer: RB2, gpt-6-astra with ultra reasoning. This review was conducted
from the frozen theorem statement, without an author proof or another
reviewer's scientific report. The assignment is preserved in `assignment.md`.

Frozen scientific statement: `input/theorem-only-v2.md`.

SHA256:
`44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51`.

**Independent review verdict: PASS for EX-REG, EX-REC, the stated effective
families, and the finite-implementation error accounting.** I reconstruct
proofs below. I find no counterexample and no additional source assumption
needed for these statements. This is a blind referee's mathematical verdict,
not a claim to have completed the coordinator's project-wide certification
gates or checked any author artifact I was not given.

The exponent-5.18 least-prime theorem was checked at the exact permitted
primary URL. The only imported scientific theorem is that stated result;
its proof was not reaudited. All remaining arguments below are independent
derivations. The exact consulted-source manifest is `sources-consulted.md`.
No other project research, proof, history, status, log, or agent-registry file
was read. No accidental scientific exposure occurred. No executable
mathematical experiment was run. The finite controls below are exact hand
calculations, including optimization over all deterministic guessers in the
small posterior example. They do not constitute an asymptotic experiment.

## 1. Model and the claims being checked

Let n >= 2 be a power of two, q >= n^2 an odd prime with q = 1 mod 2n, and
R = F_q[X]/(X^n+1), represented by its n coefficients. The n distinct CRT
roots identify R with F_q^n. For a d-subset T of these roots, I_T is the ideal
of CRT vectors supported on T; coordinates on T may also be zero.

Write ell = ceil(log_2 n), L = ceil(n sqrt(q)),
b = (2n+1)L ell^2, and sigma = 2 sqrt(m)n b ell. For t > 0,
D_t(z) = exp(-pi z^2/t^2)/rho_t on Z, where rho_t is the corresponding sum.

An input pair (A_1,A_2) is expanded using independent rows of fresh private
coins:

    C_j = A_1 R_j1 + A_2 R_j2 + W_j mod q,

where all coefficients of R_ji are uniform on {0,...,L-1}, and those of W_j
are independent D_L. The map and its algorithm are public; neither its
input pair nor its local random tape is supplied to the target solver.

EX-REG claims the joint comparison including the original pair, for uniform
independent A_1,A_2, against m independent uniform outputs independent of
that pair, with error

    delta_exp = min(1, (m/2) sqrt(B)),
    B = 16^n q^n exp(-2 pi n^2) + (2/n)^n.

For the planted pair, T is a uniform d-subset, U_1,U_2 are independent
uniform elements of I_T conditional on T, and A_i = U_i + F_i mod q.
The 2n coefficients of F_1,F_2 are independent D_ell and independent of the
ideal data. This exact pair law, and only this pair, defines Base2.

The target has independent uniform multipliers a_j, one coefficient-binary
uniform S, and independent coefficient D_sigma errors E_j jointly
independent of S and the multipliers. Success means Q returns that actual S.
The wrapper samples the expansion, its own actual S and errors, calls Q on
(C_j,C_j S+E_j)_j, and tests equality to its actual sampled S.

EX-REC states

    epsilon_m <= Adv_Base2(B_Q) + beta + eta + delta_mask + delta_exp,
    beta = q^d ((1+D_ell(0))/2)^n,
    delta_mask = min(1,(m+2)n exp(-pi ell^2)/(pi ell)),

where kappa(t) = 2 sum_{j>=1} exp(-pi t j^2),
Delta = (1+kappa(3ell^2/4))^n-1, and eta is
min(1,Delta/(1-Delta)) when Delta < 1, otherwise 1.

## 2. First discriminating check: the complete m=3 uniform law

### 2.1 Conditional law and the two-seed second moment

For each fixed pair a=(a_1,a_2), let P_a be the distribution of a single
expanded output. Fresh row coins give the exact conditional law

    Law(C_1,C_2,C_3 | A=a) = P_a tensor P_a tensor P_a.

This is an equality on every seed value, including a_1=a_2=0. It does not
assert that P_a itself is always close to uniform. Since the comparison has
the same uniform seed distribution on both sides,

    TV((A,C_1,C_2,C_3),(A,Z_1,Z_2,Z_3))
      = E_A TV(P_A^tensor3,U^tensor3)
      <= 3 E_A TV(P_A,U).

The same formula with m in place of 3 follows from a product telescoping
inequality. Thus no marginal-to-joint inference is needed.

Here is a bound for the expectation on the right. Index additive characters
by coefficient vectors t in F_q^n, using chi_t(x)=exp(2 pi i <t,x>/q).
Let r(t) be the rank of multiplication by t in R. Because the ring splits,
r(t) is exactly the number of nonzero CRT coordinates of t, and there are
binom(n,r)(q-1)^r vectors of rank r.

The involution bar(f)=f(X^-1) is a signed coefficient permutation and
the adjoint of multiplication by f is multiplication by bar(f). For an
interval vector V, averaging over one uniform ring element A gives

    E_A |E_V chi_t(A V)|^2
      = Pr[t bar(V-V') = 0],

where V' is an independent copy of V. The relevant linear map has rank r.
We have L <= q because n sqrt(q) <= q and q is an integer. Choose r pivot
coordinates of a rank-r submatrix. Conditional on the other coordinates,
at most one choice of the pivot vector in {0,...,L-1}^r can produce a
specified image modulo q. Every atom of the image therefore has mass at
most L^-r; its collision probability is at most L^-r. The two independent
uniform seeds give the square L^-2r, with no third seed or oracle call.

Writing g_t for the Fourier transform of W, this proves

    E_A |hat(P_A)(t)|^2 <= |g_t|^2 L^-2r(t).

The proof also applies when multiplication is singular; it never divides by
a CRT coordinate and never removes a seed branch.

### 2.2 The small-rank Fourier contribution

Take the centered integer coefficient lift of a nonzero t. Its integer
negacyclic multiplication matrix M_t has nonzero determinant: X^n+1 is
irreducible over Q for n a power of two. For example, substitution X+1
gives an Eisenstein polynomial at 2. Reduction modulo q has rank r, so
q^(n-r) divides det(M_t), as is immediate from integer Smith normal form.
Each column is a signed permutation of t. Hadamard's inequality gives

    q^(n-r) <= |det(M_t)| <= ||t||_2^n.

Consequently r <= n/2 implies ||t||_2 >= sqrt(q).

Poisson summation for a one-dimensional discrete Gaussian gives, for
alpha in [-1/2,1/2],

    E_{W~D_L} exp(2 pi i alpha W)
      = sum_k exp(-pi L^2(k-alpha)^2)
        / sum_k exp(-pi L^2 k^2).

For L >= 1 this is at most 4 exp(-pi L^2 alpha^2). Indeed the denominator
is at least 1, and after factoring out the displayed exponential the
numerator is at most

    1 + 2 sum_{k>=1} exp(-pi L^2 k(k-1)) < 4.

Taking the product over coefficients and squaring yields

    |g_t|^2 <= 16^n exp(-2 pi L^2 ||t||_2^2/q^2).

For nonzero t of rank at most n/2, L^2 >= n^2 q makes this at most
16^n exp(-2 pi n^2). There are fewer than q^n such t. Dropping the
additional collision factor gives their total contribution at most

    16^n q^n exp(-2 pi n^2).

### 2.3 The large-rank contribution and the full conclusion

For r > n/2, use |g_t| <= 1. Then

    sum_{r>n/2} binom(n,r)(q-1)^r L^-2r
      <= sum_{r>n/2} binom(n,r)n^-2r
      <= 2^n n^-n = (2/n)^n.

Parseval, with this character normalization, gives

    chi^2(P_A || U) = sum_{t != 0} |hat(P_A)(t)|^2.

Thus E_A chi^2(P_A||U) <= B. Cauchy-Schwarz for total variation and
Jensen give

    E_A TV(P_A,U) <= (1/2) sqrt(B).

The exact conditional product law above proves EX-REG for every m,
including m=3. Truncating the resulting bound at 1 is valid. This is a
full joint law with the seed present, not just uniform-looking marginals.

### 2.4 Exact finite branch control: n=2, q=5, m=3

Here ell=1 and L=5=q. Each interval polynomial is exactly uniform in R.
The two CRT roots are 2 and -2. At either root, the two seed evaluations
are simultaneously zero with probability 1/25; these events are independent
between the two roots. The complete branch weights are:

| Common zero roots of A_1,A_2 | Probability | Single-output law |
|---|---:|---|
| None | 576/625 | Uniform R |
| Only 2 | 24/625 | Uniform at -2, Gaussian projection at 2 |
| Only -2 | 24/625 | Uniform at 2, Gaussian projection at -2 |
| Both | 1/625 | W mod 5 |

For an exact formula, let

    p(x) = rho_5^-1 sum_{k in Z} exp(-pi(x+5k)^2/25), x in F_5,
    nu(z) = sum_{x in F_5} p(x)p(3(z-x)).

The latter is the law of W_0+2W_1 mod 5. Symmetry of p gives the same
law for W_0-2W_1. In each one-zero-root branch, the other coordinate is
uniform and independent of this projection. In the all-zero branch,
the coefficient law is p tensor p. Taking three independent row draws
within every fixed seed gives the exact seed-inclusive total variation

    (48/625) TV(nu^tensor3,U_5^tensor3)
      + (1/625) TV(p^tensor6,U_5^tensor6).

There is no omitted rare branch and no finite truncation of a Gaussian
series in this expression. For these parameters the displayed delta_exp
is 1, so its vacuity is explicitly permitted. This finite control is useful
because it would falsify any proof claiming each conditional law is uniform,
or treating the common seed's bad branches as independent between rows.

For comparison of recovery events, append the actual sampled S and all
fresh target noise as part of the comparison kernel. Total variation cannot
increase, and the event is Q(transcript)=S with that same S. No arbitrary
preimage or newly sampled posterior witness is substituted.

## 3. Independent planted recovery proof

### 3.1 Tail event and the integer mask matrices

For t>=1 with t ell an integer, Poisson summation gives rho_t >= t, and
monotonicity plus a Gaussian integral bound gives

    Pr_{Z~D_t}[|Z| > t ell]
      <= 2 integral_ell^infinity exp(-pi u^2) du
      <= exp(-pi ell^2)/(pi ell).

Use the good event that all 2n coefficients of F_1,F_2 satisfy
|F_i,k| <= ell^2, and all mn coefficients of W_j satisfy
|W_j,k| <= L ell. Its complement has probability at most delta_mask,
by a union bound and the trivial bound 1. This event involves no S or
target noise.

With integer negacyclic products, put

    G_j = F_1 R_j1 + F_2 R_j2 + W_j,
    V_j = U_1 R_j1 + U_2 R_j2 in I_T.

Then C_j = V_j+G_j mod q. On the good event,

    ||G_j||_infinity
      <= 2n(L-1)ell^2 + L ell
      <= (2n+1)L ell^2 = b.

Let A be the mn-by-n integer matrix obtained by stacking multiplication
by the G_j. Each block has Frobenius norm at most n b, hence

    ||A||_op <= sqrt(m)n b.

This notation A denotes an integer matrix only in this section, not the
original pair of ring seeds.

### 3.2 A full discrete Gaussian law, with its normalizer

Fix any good planted state. Define the positive definite scale matrix

    Sigma = sigma^2 I_mn - ell^2 A A^T.

It satisfies Sigma >= (3/4)sigma^2 I. These are Gaussian *scale*
matrices in exponent formulas, not assertions about exact discrete
covariance matrices.

Independently sample Z with n iid D_ell coefficients, and E' on Z^(mn)
with mass proportional to

    exp(-pi E'^T Sigma^-1 E').

Set E=AZ+E'. I claim its entire mn-dimensional law is within eta of
the product law D_sigma^(mn). This construction is an analysis device;
the public wrapper need not sample E' or know A.

The change of integer variables (z,e') -> (z,e=Az+e') is a bijection.
Completing the square gives

    ||z||^2/ell^2 + (e-Az)^T Sigma^-1(e-Az)
      = ||e||^2/sigma^2 + (z-mu(e))^T H^-1(z-mu(e)),

where

    H = ell^2 I_n - ell^4 A^T A/sigma^2 >= (3/4)ell^2 I_n,
    mu(e) = ell^2 A^T e/sigma^2.

Thus the marginal mass of E is proportional to

    exp(-pi ||e||^2/sigma^2) f(e),
    f(e) = sum_{z in Z^n} exp(-pi(z-mu(e))^T H^-1(z-mu(e))).

Poisson summation yields, uniformly in every real shift c,

    rho_H(c) / sqrt(det H)
      = sum_{k in Z^n} exp(-pi k^T H k) exp(2 pi i <k,c>).

Its deviation from 1 has absolute value at most

    sum_{k != 0} exp(-pi k^T H k)
      <= (1+kappa(3ell^2/4))^n-1 = Delta.

If Delta<1, write f(e)=sqrt(det H)(1+u(e)), where |u(e)|<=Delta.
Relative to p(e)=D_sigma^(mn)(e), the *normalized* marginal density is

    p(e)(1+u(e))/(1+E_p u).

The normalization is positive and at least 1-Delta. Consequently its TV
distance from p is at most Delta/(1-Delta); use the trivial bound 1 as
needed. This is exactly eta. In particular, the bound concerns the whole
vector E, not only its coordinate marginals or its quadratic scale.

Since this holds for every good planted state and S stays independent,
it also compares the full joint state/S/error distribution on that event.
No uniformity or independence among the G_j is needed.

### 3.3 What the alternate transcript reveals about the actual S

Under the alternate error law,

    C_j S + E_j = V_j S + G_j(S+Z) + E'_j mod q.

Give a hypothetical decoder all of the planted state
(T,U_1,U_2,F_1,F_2,(R_ji)_ji,(W_j)_j), all of E', the integer vector
H_secret=S+Z, and the d CRT evaluations pi_T(S) of the actual secret on T.
These data determine the whole target transcript. In fact V_j lies in
I_T, so V_j S depends only on pi_T(S). This remains true if some or all
CRT coordinates of U_1,U_2, or of every V_j, are zero. No coordinate
division or full-support hypothesis is used.

The revealed planted state and E' are jointly independent of (S,Z),
including after conditioning on the good event. Conditional on that state,
pi_T(S) has at most q^d possible values. For any joint pair (S,H) and
any deterministic K-valued leakage L(S), pointwise maximization gives

    P_guess(S | H,L)
      = sum_h sum_l max_{s:L(s)=l} Pr[S=s,H=h]
      <= K sum_h max_s Pr[S=s,H=h].

Apply this with K=q^d. To evaluate the remaining quantity, put p=D_ell.
The *joint* mass of S=s and H_secret=h is

    2^-n product_i p(h_i-s_i).

Maximization over the full binary vector separates in this product before
any additional leakage is conditioned upon. For a single coefficient,

    sum_{h in Z} max(p(h),p(h-1)) = 1+p(0),

since the first term wins for h<=0 and the second for h>=1. Therefore

    P_guess(S | S+Z) = ((1+D_ell(0))/2)^n,

and every decoder of the alternate transcript has actual-secret success
at most beta. This is an average guessing-probability calculation from
the full joint law; it is not a product of posterior success probabilities
after exposing CRT coordinates.

Returning to the genuine errors costs eta on the good event and at most
delta_mask on its complement. Thus the exact planted wrapper acceptance
probability is at most beta+eta+delta_mask.

### 3.4 Reduction to the sole Base2 challenge

Let a_U and a_P be the wrapper's acceptance probabilities on the uniform
pair and the planted pair. EX-REG, with the actual S and fresh errors
appended, implies

    epsilon_m <= a_U + delta_exp.

The exact definition of pair advantage gives

    a_U <= a_P + Adv_Base2(B_Q).

Substituting the preceding planted bound proves EX-REC. The wrapper uses
the one supplied pair, fresh local coins, and one Q call. It neither asks
for a source oracle nor assumes the expanded planted rows have a Base_m
distribution. Their shared masks and ideal correlations are admitted
throughout the proof.

## 4. Further exact finite controls and probability regressions

### 4.1 Gaussian scale does not imply an exact discrete convolution law

As a scalar control for the Gaussian sublemma, take ell=1, A=[1], sigma=2.
Then Sigma=3, H=3/4, and mu(e)=e/4. Independent Z~D_1 and E'~D_sqrt(3)
give E=Z+E' with marginal proportional to

    exp(-pi e^2/4) rho_{H}(e/4).

The theta factors for e=0 and e=2 differ. Poisson summation gives

    rho_H(0)-rho_H(1/2)
      = 2 sqrt(H) sum_{k odd} exp(-pi H k^2) > 0.

Thus replacing this convolution by an *exact* D_2 law would be wrong.
The normalized theta comparison in Section 3.2 pays precisely for this
effect. This is a structural sublemma control, not an assertion that these
scalar parameters are an entire n>=2 ring instance.

### 4.2 Exact two-bit leakage enumeration

Use two independent uniform bits and, as a finite structural control, two
independent noises uniform on {-1,0,1}. All 36 elementary pairs (S,Z)
have weight 1/36. For each coordinate of H=S+Z, values -1 and 2 identify
the bit, whereas 0 and 1 leave two equiprobable possibilities.

Without leakage, pointwise optimal guessing has probability 4/9. Add
the parity S_1 xor S_2, a two-valued leakage. Among H pairs there are:

* four pairs with both bits ambiguous, each contributing 2/36 after parity;
* eight with one ambiguous bit, each contributing 2/36;
* four with neither ambiguous, each contributing 1/36.

The optimal success is therefore 28/36=7/9, below the cardinality bound
2*(4/9)=8/9. This calculation explicitly maximizes over all deterministic
guessers; randomized guessers cannot improve it. It checks the averaging
and leakage step without assuming posterior-coordinate independence.

### 4.3 Cached-prefix regression CP-1

The required operational regression has Pr[vk=1]=10/11 and posterior
weights Pr[A_b]=21/2000, Pr[C_b]=1/20, Pr[D]=879/1000. Its initial
incidences are p(x)=1/10, p(e_b)=121/2000=0.0605, and
p(f_b)=21/2000=0.0105, all at most the strict threshold 1/10.
The two selected hits occur with total probability

    sum_b (21/2000)/2 = 21/2000 > 1/100.

After the first hit and the cached-prefix transfer, the second incidence
is 21/221 < 1/10. Hence the tempting product bound is false. The cause
is support restriction and posterior renormalization, even though the
remaining incidence is still below threshold.

The present proof does not invoke that product rule. Its row product is
an exact conditional independence statement before selection, with the
entire seed retained and then averaged. Its secret-bit product is an
explicit sum of maxima of a factorized joint mass before leakage. Extra
leakage is handled by a pointwise cardinality inequality, not a posterior
product. No proof branch exposes latent cache-hit information. Thus CP-1
rejects the invalid inference while leaving these replacement arguments
intact.

These hand controls do not search all parameter values numerically. The
general results rest on the analytic arguments above, including exact
normalizers and bounds on every branch.

## 5. Effective family and source scope

Fix h>=0 before the adversary, take polynomial-time computable
1<=m(n)<=n^h, set K=h+10, and let q be the least prime 1 mod 2n^K.

The permitted primary source is Triantafyllos Xylouris, *On the least prime
in an arithmetic progression and estimates for the zeros of Dirichlet
L-functions*, Acta Arithmetica 150.1 (2011), Theorem 1.1, printed page 66
(PDF page 2):
https://www.impan.pl/shop/publication/transaction/download/product/83078.
It supplies P(a,M)<=C M^5.18 for coprime positive a,M with an effectively
computable constant. Applying it to a=1, M=2n^K gives

    2n^K+1 <= q <= C 2^5.18 n^(5.18K) <= n^(6K)

eventually for each fixed K. The eventual upper bound absorbs a fixed
constant using the positive exponent gap 0.82K. No assumption about an
unpublished exponent or a conjectural prime-search bound is involved.

This q is odd and 1 mod 2n, and q>=n^2. A uniform algorithm can find it
by scanning the progression and testing primality by trial division if
desired. Since the numerical value q is polynomial in n for fixed h,
even that inefficient elementary method has polynomial runtime in n.
The theorem needs polynomial dependence on n, not polynomial dependence
only on log q.

For n>=2 and q>=n^2, L <= (5/4)n sqrt(q), and 2n+1 <= (5/2)n.
Therefore

    sigma <= (25/4) n^(h/2+3) sqrt(q) ell^3,
    q/sigma >= (4 sqrt(2)/25) n^2/ell^3 >= n

eventually. The q/sigma assertion has the claimed direction and enough
slack despite increasing m.

All statistical error terms are negligible for fixed h and K:

* The first term in B is at most
  exp(-2 pi n^2+6K n log n+n log 16), hence exp(-Omega(n^2)).
  The other term is (2/n)^n. Multiplication by m<=n^h does not change
  negligibility of delta_exp.
* kappa(3ell^2/4)=O(exp(-3 pi ell^2/4)); consequently Delta, and then
  eta, are n times exp(-Theta(log^2 n)) up to constant factors eventually.
* delta_mask is bounded by a polynomial times exp(-pi ell^2)/ell.

For beta, rho_ell>=ell gives D_ell(0)<=1/ell. Since ell=log_2 n on the
power-of-two subsequence,

    log_2 beta <= 6K d ell - n + n log_2(1+1/ell).

If d=floor(sqrt(n)/ell^4), the first term is at most
6K sqrt(n)/ell^3=o(n), so beta<=2^(-n+o(n)). If
d=floor(n/(24K ell)), that term is at most n/4, so
beta<=2^(-3n/4+o(n)). Both are negligible.

With a bounded polynomial implementation of the wrapper, a nonnegligible
actual-secret recovery probability would therefore give a nonnegligible
uniform-PPT Base2 distinguisher at this exact q,d family. The Base2
hypothesis remains a separate premise for each choice of h and each d
family. The result does not supply all polynomial sample exponents at
one fixed modulus family, or transport a source premise from a different
September modulus family. It says nothing about standard-RLWE source
hardness, target decision hardness, nonuniform/quantum adversaries, or
practical parameter security.

## 6. Finite implementation and costs

Let B be the ideal wrapper and B_hat the wrapper using an approximate
challenge-independent joint local sampler at TV distance at most xi_alg.
Let P and P_hat be the exact and implemented planted *pair* distributions,
at TV distance at most xi_source. The uniform pair comparator U stays
exact. Data processing gives

    |Pr_P[B=1]-Pr_P_hat[B_hat=1]| <= xi_source+xi_alg,
    |Pr_U[B=1]-Pr_U[B_hat=1]| <= xi_alg.

The triangle inequality for the difference of the two acceptance
probabilities therefore gives

    Adv_P(B) <= Adv_P_hat(B_hat)+xi_source+2xi_alg.

A complete target *witness/transcript* comparison of TV xi_target changes
the actual-secret success probability by at most xi_target. Substitution
in EX-REC yields exactly the advertised extra

    xi_source + 2xi_alg + xi_target.

The need to include the actual witness in xi_target is real: transcript
TV alone does not control which latent secret the solver must recover.
Conversely, xi_source need only control the pair law, since the test
receives only that pair and its local coins are independent of it.

For completeness, bounded polynomial local sampling can be implemented
without an ideal real-number operation. In the effective family, L and
sigma are polynomially bounded in n, and sigma^2=4mn^2b^2ell^2 is an
integer. A simple, inefficient construction suffices:

1. Generate the n secret bits exactly. For each interval draw, use the
   usual binary rejection method, cap it at n attempts, and output a fixed
   fallback on failure. The failure probability is at most 2^-n per draw.
2. For each Gaussian parameter t in {L,sigma}, restrict to
   |z|<=ceil(t n). The omitted mass is exponentially small in n^2, by
   the same Gaussian tail integral. The cutoff can be computed with
   integer square roots because t^2 is an integer.
3. Tabulate the finitely many weights exp(-pi z^2/t^2), normalize to
   rational/dyadic probabilities, and inverse-sample using a fixed number
   of random bits. Certified approximations to pi and exp to
   O(n^2+log(mnt)) bits suffice. For example, the arctangent series in
   pi=16 arctan(1/5)-4 arctan(1/239) converge geometrically; exponential
   Taylor series after range reduction also give certified bounded
   polynomial bit complexity.
   The support contains only polynomially many integers for fixed h, so
   rounding error summed over the entire table remains negligible.

There are polynomially many draws, so a coupling/union bound makes the
TV error of the *entire* local sampler negligible. This proves existence
of a bounded polynomial implementation; it is not a practical runtime
claim. In the reduction from the exact theoretical target, one can set
xi_source=xi_target=0 and use only the negligible xi_alg approximation
to obtain a genuine bounded-PPT distinguisher.

The advertised high-level operation counts are correct: 2mn interval
draws, mn D_L draws, mn D_sigma draws, and n secret bits. Forming the C_j
uses 2m ring multiplications; forming C_j S uses m more. There are O(m)
ring additions and one Q call. All integer bit lengths and all ring
arithmetic costs are polynomial in n for fixed h. The multivariate E'
used in the proof is never required by this implementation.

## 7. Final scope of this blind verdict

Every displayed finite error term has an independent derivation above.
The three-output comparator check retains the complete seed mixture and
zero branches. The planted analysis retains the shared masks, the full
mn-dimensional error law, the normalizing theta factor, and the actual
sampled binary witness. The effective family uses only the permitted
published least-prime statement and its stated effectiveness.

No missing hypothesis or counterexample was found. The result remains
conditional on the exact new-family Base2 premise. Numerical testing was
not used to certify an asymptotic conclusion, and no claim is made about
unseen author proofs, project regressions beyond the supplied operational
ones, or later revisions of the frozen statement.

This version is to be frozen and accompanied by a separate SHA256 receipt
before its path and digest are disclosed. Subsequent corrections, if any,
must use a new report version.
