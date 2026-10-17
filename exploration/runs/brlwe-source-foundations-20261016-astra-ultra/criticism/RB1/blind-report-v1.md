# RB1 theorem reconstruction v1 — exposed-context report

## 0. Input, isolation boundary, and disposition

The frozen scientific input is `input/theorem-only-v2.md`, SHA256
`44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51`.
The assignment was to prove, refute, or isolate missing hypotheses for EX-REG,
EX-REC, and their effective-family/implementation claims. I interpret
`epsilon_m` as the success probability of Q at recovering the actual sampled
binary secret in the target experiment stated in that input.

I reconstructed proofs of the displayed bounds, including their constants, and
found no additional mathematical source hypothesis necessary. These proofs do
not imply hardness of Base2, and do not establish standard-RLWE source hardness.

**This report cannot close the strict blind-referee gate.** During the review,
a call to `collaboration.list_agents`, intended to check operational progress,
returned another worker's completed scientific status summary. I immediately
informed the parent. The exact output is preserved in
`list-agents-exposure-exact.json`, and the exposure is described in
`isolation-incident.md`. No author proof or worker file was opened. The
pre-exposure reconstruction is preserved without alteration as
`pre-incident-checkpoint.md`, SHA256
`b878971539390d3033854f5f461fcca916e02938d44b24f57a86302ee11eb6c4`.
That checkpoint already contains the Fourier, Gaussian, entropy, and parameter
arguments used below. The exposed summary supplies no premise in this report.
The parent explicitly designated the completed work exposed-context review and
will commission another referee for the strict blind gate. This is also
correlated same-model scrutiny, not statistical independence.

Apart from the incident, mathematical input was limited to the frozen theorem
and the permitted primary result: Xylouris, *On the least prime in an arithmetic
progression and estimates for the zeros of Dirichlet L-functions*, Acta Arith.
150.1 (2011), Theorem 1.1, page 66,
https://www.impan.pl/shop/publication/transaction/download/product/83078.
The theorem states `P(a,Q) <= C Q^5.18` for coprime a,Q, with effectively
computable C. This directly supplies the exponent/effectiveness used below.
No other literature was consulted. Operational reads were the assignment,
audit skill/references, launcher metadata, and its cap-status file.

The independent mathematical disposition is **proved by reconstruction below**;
the audit-process disposition remains **strict blind gate OPEN** because of the
recorded exposure. No global ACCEPT is claimed.

## 1. Dependency map

| Claim | Dependencies | Result of this review |
|---|---|---|
| R1: rank, determinant, short-vector bound | Elementary cyclotomic algebra | Proved in Section 2 |
| R2: interval collision bound | Rank and injectivity of [0,L-1] mod q | Proved in Section 3 |
| EX-REG, including seed | R1, R2, Gaussian Fourier bound, Parseval | Proved in Section 3 |
| M1: source mask event and operator bound | Integer convolution and Gaussian tail | Proved in Section 4 |
| G1: rectangular discrete Gaussian convolution | Completion of squares and Poisson summation | Proved in Section 5 |
| I1: noisy-binary guessing and finite-range leakage | Exact joint probabilities | Proved in Section 6 |
| EX-REC | EX-REG, M1, G1, I1, one-call test | Proved in Section 7 |
| Finite implementation accounting | TV contraction and two local-kernel replacements | Proved in Section 8 |
| Effective family | Above, fixed h, Xylouris Theorem 1.1 | Proved in Section 9 |

The proof uses no claim that the expanded ideal parts are independent, no
Base_m oracle, and no witness available to B_Q beyond its own sampled secret.

## 2. Character rank and the cyclotomic norm estimate

Write a ring element in coefficient coordinates. Let M_v be the integer
negacyclic multiplication matrix for an integer coefficient vector v. Because
n is a power of two, X^n+1 is irreducible over Q: substituting X+1 gives an
Eisenstein polynomial at 2. Consequently M_v has nonzero integer determinant
for every nonzero integer polynomial v of degree less than n.

For a nonzero character vector alpha in F_q^n, choose its centered integer
coefficient lift v. Let r be the rank of M_v modulo q. Since the ring splits
into n distinct CRT coordinates, r is the number of nonzero CRT coordinates of
alpha. There are exactly binom(n,r)(q-1)^r characters of rank r.

Rank deficiency n-r modulo q implies q^(n-r) divides det(M_v). One elementary
way to see this is to lift invertible row operations modulo q to an integer
matrix whose determinant is coprime to q; the transformed product has n-r rows
divisible by q. Thus

    |det(M_v)| >= q^(n-r).

Let zeta range over the n complex roots of X^n+1. Their Fourier matrix is
unitary after division by sqrt(n), so

    sum_zeta |v(zeta)|^2 = n ||v||_2^2.

Applying arithmetic-geometric mean to these n squared magnitudes yields

    |det(M_v)| = product_zeta |v(zeta)| <= ||v||_2^n.

Therefore, for every such centered lift,

    ||v||_2 >= q^((n-r)/n).                         (2.1)

This includes every nonzero low-rank character, not just a typical one. No
nonzero scalar or unit assumption is imposed on a seed.

## 3. EX-REG as a full joint-law statement

First, L <= q: n sqrt(q) <= q, and q is an integer. Thus each interval
coefficient has L distinct residues modulo q.

For a character alpha of rank r, define g_alpha(A) to be the Fourier
coefficient of A R, where R has independent interval coefficients. If R,R'
are independent such draws, averaging over uniform A gives

    E_A |g_alpha(A)|^2
      = Pr[M_(R-R')^T alpha = 0] =: p_alpha.

The map D -> M_D^T alpha has rank r. Indeed the negacyclic coefficient
involution D -> bar(D), induced by X -> X^(-1), satisfies
M_D^T alpha = M_alpha bar(D); the involution is an invertible signed permutation.
For any fixed R', the rank-r constraint on R can be solved for r pivot
coordinates after choosing the other n-r coordinates. There are at most
L^(n-r) interval vectors in a fiber. Hence

    p_alpha <= L^(-r).                              (3.1)

The two seeds are independent, so their averaged squared Fourier factor is
p_alpha^2. This is a product justified by independence of A1 and A2, not an
inference from sequentially conditioned marginal bounds.

Let alpha/q be represented by its centered coefficient vector v/q. Poisson
summation gives the one-coordinate characteristic function of D_L as

    sum_k exp(-pi L^2(k+v_i/q)^2)
    --------------------------------.
             sum_k exp(-pi L^2 k^2)

For |u| <= 1/2 and L >= 1, the numerator is at most
4 exp(-pi L^2 u^2). For example, pair successive distances from u to the
integers and use

    sum_k exp(-pi L^2(k+u)^2)
      <= 2 exp(-pi L^2 u^2) sum_{j>=0} exp(-pi L^2 j^2)
      < 4 exp(-pi L^2 u^2).

The denominator is at least 1. Consequently

    |W_hat(alpha)|^2
       <= 16^n exp(-2 pi L^2 ||v||_2^2/q^2).         (3.2)

For 1 <= r <= n/2, (2.1) and L >= n sqrt(q) imply

    L^2 ||v||_2^2/q^2 >= n^2 q^(1-2r/n) >= n^2.

Bounding p_alpha by 1 and the number of these characters by q^n gives total
low-rank contribution at most 16^n q^n exp(-2 pi n^2).

For r > n/2, discard the W factor, use (3.1), and sum:

    sum_{r>n/2} binom(n,r)(q-1)^r L^(-2r)
      <= sum_{r>n/2} binom(n,r) n^(-2r)
      <= 2^n n^(-n) = (2/n)^n.                     (3.3)

For fixed A=(A1,A2), let P_A be the law of one expanded output. Parseval and
Cauchy-Schwarz give

    TV(P_A,Uniform(R)) <= (1/2) sqrt(sum_{alpha!=0}|P_A_hat(alpha)|^2).

Averaging over A and applying Cauchy-Schwarz again therefore gives

    E_A TV(P_A,Uniform(R))
      <= (1/2) sqrt(16^n q^n exp(-2 pi n^2)+(2/n)^n).

Given the actual seed pair A, all m expansion rows are independent with law
P_A. The elementary product hybrid gives
TV(P_A^m,Uniform(R)^m) <= m TV(P_A,Uniform(R)). Finally,

    TV((A,C1,...,Cm),(A,Z1,...,Zm))
      = E_A TV(P_A^m,Uniform(R)^m) <= delta_exp.

The equality explicitly retains the seed, and Z is independent of it. The
cap at 1 is legitimate. No good-seed conditioning, discarded exceptional seed,
or claim that unconditioned rows are independent is used.

## 4. Source masks, tail event, and the rectangular operator

On the planted source, retain the latent variables only for the analysis. Set

    V_j = U1 R_j1 + U2 R_j2 in I_T,
    G_j = F1 R_j1 + F2 R_j2 + W_j in Z[X]/(X^n+1).

Then C_j = V_j + G_j modulo q. The G_j are not assumed independent.

For t an integer and ell >= 1, Poisson summation gives
rho_t(Z) = sum_z exp(-pi z^2/t^2) >= t. Since t ell is an integer,

    Pr_{D_t}[|z|>t ell]
      <= (2/t) integral_{t ell}^infinity exp(-pi x^2/t^2) dx
      <= exp(-pi ell^2)/(pi ell).                  (4.1)

Let Good be the event that every coefficient of F1,F2 has magnitude at most
ell^2 and every coefficient of every W_j has magnitude at most L ell. A union
bound over (m+2)n coefficients gives Pr[not Good] <= delta_mask, with the
trivial probability cap if needed. This event depends exclusively on source
and expansion coins, not on S or the later auxiliary Gaussian.

On Good, coefficientwise integer negacyclic convolution gives

    ||G_j||_infinity
       <= 2n(L-1)ell^2 + L ell <= (2n+1)L ell^2 = b.

Let H be the mn-by-n integer matrix stacking multiplication by the G_j.
Each block is a sum of signed permutation matrices and therefore

    ||M_(G_j)||_op <= ||G_j||_1 <= n b,
    ||H||_op <= sqrt(m)n b.                        (4.2)

This pointwise estimate applies to all T,U1,U2,R and all masks in Good,
including zero seed components and arbitrary correlations between rows.

## 5. Exact Gaussian convolution calculation

The following lemma is used only for information-theoretic comparison; the
wrapper does not sample its dense Gaussian.

Fix any integer N-by-n matrix H with ||H||_op <= sigma/(2 ell), where N=mn.
Put s=ell and

    Omega = sigma^2 I_N - s^2 H H^T,
    B = (s^(-2)I_n + H^T Omega^(-1)H)^(-1)
      = s^2 I_n - (s^4/sigma^2) H^T H.

Both matrices are positive definite, and B >= (3s^2/4)I_n. Draw F0 with
independent D_s coordinates and draw E' independently from the discrete
elliptical Gaussian on Z^N proportional to exp(-pi e'^T Omega^(-1)e').
Set E=H F0+E'. Then

    TV(Law(E), D_sigma^N) <= eta.                   (5.1)

Here is the normalization calculation. Completing the square, with
mu_e = (s^2/sigma^2)H^T e, gives

    ||f||^2/s^2 + (e-Hf)^T Omega^(-1)(e-Hf)
      = ||e||^2/sigma^2 + (f-mu_e)^T B^(-1)(f-mu_e).

Thus the mass at e is proportional to exp(-pi||e||^2/sigma^2) theta_B(mu_e),
where

    theta_B(mu) = sum_{f in Z^n} exp(-pi(f-mu)^T B^(-1)(f-mu)).

Poisson summation expresses theta_B(mu)/sqrt(det B) as 1 plus nonzero Fourier
terms whose absolute sum is at most

    sum_{k != 0} exp(-pi k^T B k)
      <= sum_{k != 0} exp(-3 pi s^2 ||k||^2/4)
      = (1+kappa(3s^2/4))^n - 1 = Delta.

Write h(e)=theta_B(mu_e)/sqrt(det B). If Delta<1, then h(e) lies in
[1-Delta,1+Delta] for EVERY e. Since the probabilities sum to one, the exact
likelihood ratio against D_sigma^N is

    h(e) / E_{Y~D_sigma^N}[h(Y)].

Its distance from 1 is at most 2Delta/(1-Delta), so half its expected absolute
distance is at most Delta/(1-Delta). Intersecting with TV<=1 proves the
specified eta; when Delta>=1 the asserted eta=1 is trivially valid. There is
no untracked normalization factor or exceptional output branch.

For m=3 specifically, N=3n and

    H^T H <= 3n^2 b^2 I_n,
    sigma^2 = 12 n^2 b^2 ell^2,
    B >= (3ell^2/4)I_n.

The dimension in the theta error remains n, not 3n. Repeated rows or perfectly
correlated G_j are permitted: Omega is generally dense, but remains positive
definite. At H=0 the comparison is exact. None of this requires independently
sampled planted multipliers.

## 6. Actual-secret information bound

Let S be uniform in {0,1}^n and let F0 have iid D_ell coordinates independently
of S. Set Z=S+F0 as an integer vector, without reduction modulo q.

For any observation Z the optimal probability of recovering the actual S is

    P_guess(S|Z) = sum_z max_s Pr[S=s,Z=z].

Independence before conditioning gives the exact product identity

    P_guess(S|Z)
       = ( (1/2) sum_{z in Z} max(D_ell(z),D_ell(z-1)) )^n
       = ((1+D_ell(0))/2)^n.                       (6.1)

The last equality uses symmetry and unimodality: z<=0 selects D_ell(z),
and z>=1 selects D_ell(z-1), whose combined sum is 1+D_ell(0).

For ANY deterministic extra leakage Y=f(S) with at most M values,

    P_guess(S|Z,Y)
      = sum_{z,y} max_{s:f(s)=y} Pr[S=s,Z=z]
      <= M sum_z max_s Pr[S=s,Z=z].               (6.2)

Empty fibers have maximum zero. This uses joint masses, so zero-probability
observations cause no division problem. It does not assert that secret bits
remain independent after Y is disclosed. Randomized algorithms are mixtures
of deterministic decision rules and satisfy the same upper bound.

Now fix all planted-source and expansion variables D=(T,U1,U2,F1,F2,R,W)
on Good. This conditioning is independent of S,F0. Let Y be the CRT projection
of S onto T; its range has at most q^d values. All V_j S are determined by
(D,Y). Using the convolution experiment from Section 5,

    C_j S + E_j
      = V_j S + G_j(S+F0) + E'_j modulo q.

Thus the entire Q input is a randomized function of (D,Y,Z), with E' and Q's
coins fresh given D. Even giving D,Y,Z to an optimal unbounded decoder cannot
raise success above

    q^d ((1+D_ell(0))/2)^n.                        (6.3)

The same single projection Y determines the ideal contribution of EVERY row,
including three rows; the range is q^d, not q^(md). No assumption about the
joint law of the V_j is needed. If d=0, Y is constant. If d=n, the bound may
exceed 1 and is merely vacuous. Zero U_i, zero CRT coordinates, repeated rows,
and rare choices of T remain within the pointwise proof.

The actually sampled target errors are independent D_sigma coordinates. For
each fixed D on Good, (5.1) compares their full joint law with the convolved
error, jointly with the independent S. TV contracts under forming the
transcript and running Q, so actual planted acceptance is at most (6.3)+eta.
Averaging over D and paying Pr[not Good] gives

    p_planted <= q^d ((1+D_ell(0))/2)^n + eta + delta_mask.   (6.4)

No conditioning penalty 1/Pr[Good] appears: the pointwise bound is averaged,
and only the bad mass is paid. Good never conditions on S or a successful
recovery event.

## 7. EX-REC and the witness interface

Let p_uniform be B_Q's acceptance probability on the exact uniform pair,
and p_planted its acceptance probability on the exact Base2 pair. B_Q draws
only the stated local randomness, retains its own S, sends Q only
((C_j,C_j S+E_j))_j, and accepts exactly on equality of Q's output with that S.
It needs neither T,U,F nor a source oracle. It invokes Q once.

Under the uniform pair, EX-REG and independent sampling of S,E compare the
complete witness/transcript law with the target law at cost delta_exp. In
particular

    epsilon_m <= p_uniform + delta_exp
              <= |p_uniform-p_planted| + p_planted + delta_exp.

Substituting (6.4) proves exactly

    epsilon_m <= Adv_Base2(B_Q)
               + q^d ((1+D_ell(0))/2)^n
               + eta + delta_mask + delta_exp.

Because S is retained through the comparison, this is a statement about
recovering the actual sampled S, not choosing another compatible secret.

## 8. Finite implementation and exact operation count

Let K be the entire exact challenge-independent distribution of local
interval draws, W, S, and E; let K_tilde have TV at most xi_alg from K. This is
one FULL joint bound, so it permits whatever correlations the finite sampler
actually introduces as long as that bound holds. Applying any fixed input
pair and Q is a channel and changes acceptance by at most xi_alg.

For clarity, if the supplied planted pair law P_tilde is within xi_source of
P, denote the implemented acceptance probabilities by a_tilde(P_tilde) and
a_tilde(U), with U still EXACT uniform. Then

    p_uniform
      <= a_tilde(U)+xi_alg
      <= |a_tilde(U)-a_tilde(P_tilde)|
           + a_tilde(P_tilde)+xi_alg
      <= |a_tilde(U)-a_tilde(P_tilde)|
           + p_planted + xi_source + 2xi_alg.

If advantage instead remains defined on the exact P, the xi_source term can
be omitted; retaining it is conservative. A finite target whose COMPLETE
witness/transcript distribution is within xi_target changes recovery success
by at most xi_target. Thus the stated added loss
xi_source+2xi_alg+xi_target is valid. A marginal transcript-only TV estimate
would not justify the actual-secret success step.

For each row, forming C uses two ring multiplications and forming C S uses
one. There are therefore exactly 3m ring multiplications, O(m) additions
(three per row in the direct implementation), 2mn interval draws, mn D_L
draws, mn D_sigma draws, n secret bits, and one Q call. F0 and the elliptical
Gaussian in Section 5 are proof devices and add no sampler or multiplication
to the executable test. No q^d enumeration occurs in the algorithm.

For fixed h, the parameter bounds in Section 9 make both L and sigma
polynomial in n. A simple bounded implementation can tabulate a scalar D_t
on [-n ceil(t),n ceil(t)], compute its weights exp(-pi z^2/t^2) to polynomial
bit precision, and sample a dyadic approximation of the normalized table
with a fixed number of random bits. The omitted tail is exp(-Omega(n^2));
weights are uniformly computable to, for example, 2^(-n^2) absolute error in
polynomial time, and the polynomial number of table entries and draws still
gives negligible aggregate TV. For these parameters t^2 is an integer for
both L and sigma, so no noncomputable real parameter is involved. Pi and exp
can be approximated by ordinary convergent algorithms to the required
precision. The table method is slow but bounded polynomial time for fixed h.

Uniform interval draws can similarly be sampled by a fixed-bit dyadic
approximation, with error at most L/2^k for a k-bit draw, or bounded rejection
with an explicit negligible failure rule. Exact secret bits cost no error.
These constructions justify negligible xi_alg without assuming an exact
bounded-time sampler for infinite-support distributions.

## 9. Effective family and quantifiers

Fix h before adversaries; K=h+10 is then a constant. Put Q0=2n^K. The
specified prime is at least Q0+1. Xylouris applies to (1,Q0) and gives

    q <= C (2n^K)^5.18 <= n^(6K)

for all sufficiently large n. It is odd, 1 modulo 2n, and at least n^2.
The least prime can be found uniformly by enumerating the progression and
using even elementary trial division; its value and the search cost are
polynomial in n for fixed h. The effective absolute constant ensures a
polynomial global bound, with finitely many small n absorbed into its constant.
No source-hardness transfer to this new modulus follows from this search.

For the expansion error, its first squared term has logarithm

    n log(16)+n log(q)-2 pi n^2 = -Omega(n^2),

and (2/n)^n is negligible. Multiplication by m<=n^h preserves negligibility.
The mask error is at most polynomial(n) exp(-pi ell^2), also negligible.
Moreover

    kappa(t) <= 2 exp(-pi t)/(1-exp(-3 pi t)),

so n kappa(3ell^2/4) is negligible, Delta is negligible, and eventually
eta=Delta/(1-Delta) is negligible.

Poisson summation gives D_ell(0)=1/rho_ell(Z)<=1/ell. Hence, writing
p=(1+D_ell(0))/2,

    log(q^d p^n) <= d log(q) - n log(2) + n/ell.    (9.1)

For d=floor(sqrt(n)/ell^4), the first term is at most
6K sqrt(n) log(n)/ell^4=o(n), so (9.1) is -Omega(n).
For d=floor(n/(24K ell)),

    d log(q) <= n log(n)/(4ell) <= n log(2)/4,

and (9.1) is at most -3n log(2)/4+n/ell=-Omega(n).
The floor only improves these bounds.

Using L<=2n sqrt(q) and 2n+1<=3n gives

    sigma <= 12 sqrt(m)n^3 sqrt(q) ell^3,
    q/sigma >= sqrt(2) n^2/(12 ell^3) >= n

eventually, because K=h+10 and sqrt(m)<=n^(h/2). The upper bound q<=n^(6K)
also bounds every width, coefficient bit length, table, and ring operation by
polynomials in n for fixed h. A uniform PPT Q therefore gives a uniform PPT
implemented source test, with negligible xi_alg. Under the exact Base2
pseudorandomness hypothesis at this q,d family, its advantage is negligible;
EX-REC then makes actual-secret recovery negligible.

The ordering matters: each h determines its own prime/noise/source family.
The argument does not quantify over every polynomial sample exponent at one
fixed q family. For m=3, h>=1 covers the construction for sufficiently large
powers of two n. For h=0 the stipulated m range contains only m=1. These are
consistent with the frozen theorem. No September-modulus assumption is used.

## 10. Adversarial and finite controls

The single locally executed finite control was reserved with the parent and
released after completion. Files:

- `finite_control.py`: exact integer/Fraction code, deterministic, no seeds.
- `finite-control-command.txt`: the exact invocation.
- `finite-control-output.txt`: original stdout/stderr.

The command enforces a 120-second wall timeout; the code enforces 110 CPU
seconds and 128 MiB address space. It uses streaming enumeration of at most
83,521 character vectors, only short integer vectors/counters and a 64-by-8
likelihood table; estimated live data are well below 1 MiB beyond interpreter
memory. No floating-point probability calculation is used. Runtime was under
one second and the exit status was 0. No remote/detached compute, package
installation, or other experiment occurred.

Exact results:

| Control | Result |
|---|---|
| n=2,q=5 character ranks | Counts 1,8,16; minimum squared norms by nonzero rank 5,1; every determinant/norm inequality passed |
| n=4,q=17 character ranks | Counts 1,64,1536,16384,65536; minimum squared norms 85,17,5,1; every determinant/norm inequality passed |
| n=4,q=17 high-rank sum, L=q | 4800512/6975757441 <= 1/16 |
| n=2,q=13,L=8 interval collisions | All 168 nonzero characters checked; largest collision probability rank 1:79/1024<=1/8; rank 2:1/64 |
| Three secret bits with independent noise masses (1/4,1/2,1/4) on (-1,0,1) | Exact no-leak guessing probability 27/64=(3/4)^3 |
| All 256 deterministic one-bit leakage maps in that finite model | Largest guessing probability 5/8 <= 27/32, the cardinality bound |

The three-secret-bit experiment is an information-bound regression, not an
experimental verification of the m=3 theorem; m=3 is checked analytically in
Sections 5–7. These finite checks cannot prove the infinite Gaussian identities
or asymptotic claims. Those are justified only by the analytical arguments.
No numerical theta tail was truncated or treated as an exact Gaussian law.

Additional analytic edge checks:

1. The full seed-including expansion law is used, and conditional independence
   of rows is asserted only after the actual pair A is fixed.
2. The zero character is excluded from Parseval's nonuniformity sum; no nonzero
   character has rank zero in the split semisimple ring.
3. Nonunit/zero seeds and zero ideal coordinates are never conditioned away.
4. The bad-mask event is independent of S,F0, so no posterior renormalization
   can raise the claimed guessing bound without being paid for.
5. Dense rectangular Gaussian completion handles m=3 and arbitrary m. It does
   not create m independent noisy copies of the secret.
6. The leakage proof uses joint masses after projection, and never multiplies
   per-coordinate posterior maxima after the projection has coupled coordinates.
7. If Delta>=1, eta=1 gives a valid vacuous bound; likewise for clipped delta
   terms, d=n, and small n. At n=2,m=3 delta_exp is already 1, so no unjustified
   nonvacuous finite conclusion is drawn.
8. The cached-prefix product regression in the permitted audit reference does
   not arise in this proof: there is no adaptive exposure, selected survival
   event, cached answer, or sequential multiplication of conditioned hit
   probabilities. The only product laws are freshly independent seed averages
   and the unconditioned S+F0 coordinate calculation; (6.2) explicitly pays for
   subsequent support restrictions by the leakage cardinality.

## 11. Scope and remaining audit obligation

This report supplies an exact reconstruction of the finite and asymptotic
claims from the frozen theorem plus the stated primary prime theorem. It
finds no theorem-level counterexample or missing mathematical hypothesis.
It does not assess any unseen author proof, and cannot validate that a later
canonical artifact matches this reconstruction. The strict theorem-only blind
review must still be performed by another referee because of Section 0's
exposure. The theorem remains conditional on Base2 at the new parameter family;
no conventional RLWE assumption, target decision-hardness result, quantum or
nonuniform reduction, or practical security estimate is supplied here.
