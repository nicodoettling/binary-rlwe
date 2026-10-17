# RF1 full-proof referee report v1

## 1. Exact disposition and review boundary

**PASS for the mathematical, parameter, source-interface, and uniform-PPT
implementation claims of theorem-only-v2, supported by the exact proof-v1
identified below. No mathematical repair or additional source hypothesis was
found necessary.** This is a version-specific nonauthor review, not a global
certification, proof of the Base2 assumption, or independent statistical
confirmation. A fresh blind referee and coordinator reconciliation are separate
gates. I did not read or contact RB2.

| Frozen scientific input | Verified SHA256 |
|---|---|
| `input/theorem-only-v2.md` | `44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51` |
| `input/proof-v1.md` | `38c43826a936f69a775a97f19dfb3aeb90256cd03d8953d47fd54f82da27c8ae` |

The input manifest was frozen at 2026-10-16T21:31:34.839246Z. Its v2 theorem
is authoritative. The proof's first paragraph still names theorem-v1; this is
an administrative cross-reference cleanup for the canonical artifact, not a
scientific premise of this review. Every additional v2 clause was checked,
including the exact uniform comparator, clipped finite errors, actual-witness
TV accounting, bounded samplers, fixed-h quantifiers, and operation count.
The finite construction is read with a positive integer sample count m.

This role deliberately reused the agent whose earlier theorem reconstruction
was frozen in RB1. Consequently it is explicitly NONBLIND, and is not counted
as an independent referee lineage. No RB1 bytes were changed. The proof here
was audited equation by equation, including its own difference-coordinate
collision argument, normalized rectangular convolution, modular observation,
and finite table sampler; prior reconstruction agreement is not used as proof.

I read SC-v1, the current 43-entry regression inventory (preserved as
`input/regressions-read-snapshot.json`), all 19 imported regression packets,
and the applicable linked historical N02/B01/N03, source-small-d, rectangular,
and ledger-scope evidence. The audit skill and its probability reference were
already read in the prior role. This report does not recertify the entire
historical project, source-hardness literature, or old attack theorems.

The only load-bearing external mathematical theorem is Xylouris, Acta Arith.
150.1 (2011), Theorem 1.1, printed page 66. I reopened the primary PDF and
checked `P(a,Q) <= C Q^5.18`, with effectively computable C, for coprime a,Q.
The substitution here is a=1, Q=2n^K. No stronger least-prime exponent is used.
[Primary source](https://www.impan.pl/shop/publication/transaction/download/product/83078#page=2).

## 2. First falsification target: three samples and cross-blocks

The proof's most consequential three-sample step is the 3n-by-n matrix M
stacking the three integer mask-multiplication matrices. The proposed full
complement is

    B = sigma^2 I_(3n) - ell^2 M M^T,

so its off-diagonal sample blocks are `-ell^2 M_i M_j^T`. The proof retains
all of them and uses one shared n-dimensional G. It does not replace B by
separate marginal complements or assume independent planted masks.

I first checked an exact negative control. Let n=4, m=3, ell^2=4, all three
blocks M_j=I_4, and sigma^2=8. Every marginal complement is 4I_4>0, but for
x=(e_1,e_1,e_1),

    x^T B x = 8*3 - 4*9 = -12.

Thus positive individual completions cannot justify the full law. This does
not refute the actual proof: its stacked bound and width enforce
`ell^2 ||M||^2 <= sigma^2/4`, not merely blockwise positivity.

A reserved exact-rational control then used n=4, m=3, ell^2=4, b=1,
sigma^2=768, and distinct negacyclic blocks for

    1+X,  1+X^2,  1+X-X^3.

The resulting 12-by-4 M gives 88 nonzero cross-block entries in B. Independent
Gauss–Jordan inversion reproduced the Schur-complement expression for Theta;
105 direct quadratic-form evaluations agreed exactly; exact LDL pivots
verified positivity of B and of `Theta-3I_4`. The calculated Theta is

    [[185/48, -1/16,      0,  1/16],
     [ -1/16,185/48,  -1/16,     0],
     [      0, -1/16,185/48, -1/16],
     [  1/16,     0,  -1/16,185/48]].

Dropping cross-blocks at the valid width leaves, for example, entry (0,4)=4
in `ell^2 MM^T+B_diag`; hence the isotropic exponent identity fails. The
actual proof passes both negative controls. These are parameter-matrix
identities, not assertions that a discrete Gaussian's actual covariance is
its exponent matrix divided by 2pi.

Files: `rectangular_control.py`, `rectangular-command.txt`,
`rectangular-output.txt`, and `experiment-cap-preflight.json`. The parent
reserved and subsequently released this one light experiment. Limits were
120 s wall, 110 s CPU, and 128 MiB address space, all enforced. Runtime was
0.039082 s, exit status 0, and maximum observed rational size was 25 bits.
Live matrices are at most 12-by-24 during inversion, with negligible data
memory beyond the Python interpreter. There was no randomness, numerical
Gaussian summation, tail truncation, package installation, or remote compute.
No other RF1 experiment was run. Finite matrix checks do not prove asymptotic
or infinite-support probability claims; the latter are checked analytically.

## 3. Algebra, Fourier aliases, and full retained-seed regularity

### 3.1 Rank and determinant

For the negacyclic signed shift J, J^T=J^(-1), so
`M_a^T=M_(a*)`. The involution is an invertible signed permutation of
coefficient vectors and permutes CRT roots. Consequently for fixed z of CRT
support k, `A* z` for uniform A is uniform on the k-dimensional supported
ideal. This statement includes nonunits and zero coordinates.

For a nonzero centered integer lift z, irreducibility of X^n+1 over Q makes
its multiplication determinant nonzero. The Eisenstein argument uses the
shifted polynomial's even intermediate coefficients and constant term 2.
Modulo q the multiplication rank is k, so q^(n-k) divides the determinant.
The complex-root evaluation matrix satisfies V*V=nI, and AM–GM therefore
gives `|det M_z| <= ||z||_2^n`. The asserted

    ||z||_2 >= q^(1-k/n)

has no missing sqrt(n) factor. No nonzero character can have k=0; that would
be the zero ring element because CRT is an isomorphism. The zero character
is correctly excluded from the chi-square sum.

### 3.2 Difference-coordinate collision law

The interval injects modulo q since `L=ceil(n sqrt(q))<=q`. For independent
R,R', each coefficient of D=R-R' has maximum residue mass at most 1/L:
its numerator counts an intersection of two length-L subsets of F_q. The
D coefficients remain independent, including when integer differences wrap.
For a rank-k linear system, condition on all nonpivot coefficients. There is
at most one admissible pivot tuple, whose conditional probability is at most
L^(-k), since the pivot coordinates retain their independent original laws.
Every positive-mass conditioning branch satisfies the same bound; impossible
branches contribute zero.

Thus `E_(Y uniform V)|phi_R(Y)|^2<=L^(-k)` by character orthogonality.
Independence of the two original uniform seeds, not any output independence,
then gives L^(-2k) for their averaged squared factor. This closes the exact
source budget: only A1,A2 are used.

### 3.3 All aliases and all characters

Poisson summation includes the exact ratio of alias sums. For |t|<=1/2,
`(a+t)^2-t^2>=a^2-|a|`. The author's numerator bound is valid:

    1+2 sum_(a>=1) exp(-pi L^2(a^2-a)) < 4,

since the a=1 contribution is 2 and the remainder is at most
`2e^(-2pi)/(1-e^(-pi))<1`. The denominator is at least 1. Squaring and taking
the n-coordinate product gives exactly the factor 16^n.

For 1<=k<=n/2, the determinant bound and L^2>=n^2q give Gaussian exponent
at least 2pi n^2. Counting at most q^n such characters gives the first
B_exp term. For k>n/2, the exact number is binom(n,k)(q-1)^k, and

    sum_(k>n/2) binom(n,k)(q-1)^k L^(-2k)
      <=2^n (q/L^2)^(n/2) <=(2/n)^n.

The exponent n/2 is a deliberate weakening of the strict k>n/2 condition.
Because q/L^2<=1/n^2<=1, the inequality has the stated direction.

Parseval now controls the SUM of every nontrivial squared character, not
just individual small biases. Conditional TV is at most half the square
root of chi-square, and averaging uses Jensen in the correct direction.
Given the actual seed A, all fresh expansion rows have kernel K_A^m;
telescoping product TV costs m. Averaging over the retained seed gives exactly

    TV((A,C_1,...,C_m),(A,Z_1,...,Z_m)) <= delta_exp.

This is valid at m=3 and for every positive integer m. Unconditioned rows
are never declared independent. A bad seed is not discarded, and no unit
probability is omitted. A finite bound exceeding 1 is clipped legitimately.

An additional hand control establishes the interface boundary: if expansion
coins R,W were also appended, C would be deterministic given (A,R,W), and
TV from independent uniform Z would be exactly 1-q^(-mn). The frozen theorem
retains A but not R,W, and the solver does not receive those coins. The
planted-world reveal later in the proof is a different upper-bound argument,
not an illicit strengthening of EX-REG. See `negative-controls-v1.md`.

The author's comment about omitting W is also sound in its stated scope:
a fixed root where both uniform seeds vanish has probability q^(-2), and
then every pure ideal-preserving output vanishes there. Independent uniform
m-tuples have all-zero probability q^(-m). For m>=3 and polynomial q this
leaves an inverse-polynomial gap. Adding W is therefore substantive.

## 4. Planted source, tails, and conditioning

SC-v1 and theorem-v2 agree on one uniform support T, independent uniform
U1,U2 in I_T INCLUDING zeros, iid coefficient D_ell masks independent of the
entire ideal tuple, and an exact product-uniform comparator. The expanded
planted points need not be Base_m. Their only required property is the exact
decomposition `C_j=U'_j+F'_j`, where every U'_j lies in the same I_T.

For integer t=ell or L and integer cutoff t ell, decreasing-tail integration
and `rho_t(Z)>=t` give

    Pr[|D_t|>t ell] <= exp(-pi ell^2)/(pi ell).

There are precisely 2n original mask coefficients and mn W coefficients.
The union bound is delta_mask. On Good,

    |F'_j,i| <= 2n ell^2(L-1)+L ell <= b.

The signed-shift representation gives each block norm <=nb and the stacked
norm squared <=mn^2b^2. At the specified sigma this yields

    B >= (3sigma^2/4)I_(mn),
    Theta >= (3ell^2/4)I_n.

The analysis variable C_lat contains source and expansion randomness only.
It is independent of the fresh S,G. Conditioning on Good changes C_lat but
preserves the full product law of S,G. Conditioning further on a positive-mass
C_lat=c fixes the masks; no posterior law of ratios or secret bits is assumed.
The proof bounds success pointwise on each such c and pays the total bad mass
additively. It never multiplies success by a good-event probability on the
unsupported assumption that those events are independent.

## 5. Full rectangular completion and theta normalization

For each fixed good C_lat, the proof draws the ENTIRE H from the lattice law
proportional to `exp(-pi h^T B^(-1)h)`, independently of (S,G) conditional on
C_lat. This is a genuine probability distribution because B>0. It is not a
sequential sampler with omitted center-dependent normalizers, and it is not
an algorithm B_Q must execute.

Direct matrix inversion gives

    Theta = (ell^(-2)I + M^T B^(-1)M)^(-1)
          = ell^2 I - ell^4 M^T M/sigma^2.

The coefficient of the completed-square center is exactly
`mu_z=(ell^2/sigma^2)M^T z`. Expanding both quadratics gives the claimed
identity with residual term `||z||^2/sigma^2`; the rectangular dimensions
match. This holds even for M=0 or deficient-rank M. No inverse of M is used.

Let theta_z be the translated lattice sum in the n-dimensional input space,
and `r_z=theta_z/sqrt(det Theta)`. Poisson summation bounds all nonzero dual
terms uniformly in the center:

    |r_z-1| <= sum_(k!=0) exp(-pi k^T Theta k)
             <=(1+kappa(3ell^2/4))^n-1=Delta.

If P=D_sigma^(mn), exact normalization is

    Q(z)=P(z) r_z / E_P[r].

For Delta<1 the denominator is >=1-Delta, and
`|r_z-E_P r|<=2Delta`. Thus TV<=Delta/(1-Delta); the cap at 1 and the explicit
Delta>=1 branch cover every finite parameter. The historical negative-bound
counterexample is excluded by this guard, not by an asymptotic assertion.

This comparison retains C_lat and independently sampled S. It does NOT
retain H as a separate coordinate at the independent-noise endpoint. Only
after the noise comparison does the proof reveal H in the completed world to
upper-bound guessing. This order is necessary: the finite diagnostic H uniform
F_3, G=0, M=0 has E=H marginally uniform, yet (H,E) is at TV 2/3 from (H,U)
with independent uniform U. The author's explicit order avoids this invalid
extension. This diagnostic is a check of the inference, not a Gaussian
reference instance.

No continuous-covariance approximation, claim that positive Fourier ratios
imply a probability kernel, or exact wrapped deconvolution theorem is used.
The error eta depends on input dimension n, even for m=3 and growing m;
the output dimension mn is fully present in B and H.

## 6. Leakage, posterior branches, and the actual witness

In the completed world the transcript is determined by

    (C_lat, H, Y=S+G mod q, pi_T(S)).

Indeed every U'_j S depends only on the SAME pi_T(S), and F'_j Y+H_j is
known. For fixed positive-mass (C_lat,H), S,G have their original independent
product law. The projection has at most q^d possible values; no uniformity
or independence of its coordinates or posterior fibers is asserted.

For arbitrary observation Y and deterministic leakage f with at most D values,

    sum_(y,t) max_(s:f(s)=t) Pr[S=s,Y=y]
       <= D sum_y max_s Pr[S=s,Y=y].

This is an inequality of joint masses, so empty fibers and zero-probability
y need no division convention beyond assigning zero mass. In particular it
remains true after Y has produced highly nonuniform posterior secret bits.

For the stronger INTEGER observation Z=S+G, independence before observing Z
gives the exact identity

    P_guess(S|Z)
       = [ (1/2) sum_z max(D_ell(z),D_ell(z-1)) ]^n
       = ((1+D_ell(0))/2)^n.

Symmetry and unimodality give the last equality by splitting the integer
sum at z=0/1. Reduction modulo q is postprocessing and can only decrease
guessing. The projection then costs q^d once, not q^(md); this is unaffected
by correlations among expanded rows. Revealing C_lat,H serves only this
upper bound and is not a public decoding capability.

For d=0 the projection is constant; for d=n the bound can be vacuous.
Both zero ideal points, zero active coordinates, repeated expanded ideal
points, and rank loss all survive the argument. No eta_iso or active-unit
conditioning loss is silently removed. There is no old-secret replacement or
posterior resampling: success always refers to the originally sampled S.

Adding the pointwise eta comparison and the bad-mask mass yields exactly

    p_planted <= q^d ((1+D_ell(0))/2)^n + eta + delta_mask.

EX-REG permits independently adjoining S and the complete iid E vector and
forming responses, so the uniform-source endpoint is within delta_exp of the
FULL target witness/transcript law. Therefore

    epsilon_m <= p_uniform+delta_exp
              <= Adv_Base2(B_Q)+p_planted+delta_exp.

The test knows its own sampled S and can evaluate exact equality with Q's
output. It does not check only a residual or another valid preimage. It has
one pair as input, one Q call, and no hidden support, source oracle, posterior
sampler, or additional target responses. This proves the claimed EX-REC.

## 7. Parameters, effectivity, and finite implementation

Fix h first, put K=h+10, and choose polynomial-time computable 1<=m<=n^h.
The primary theorem gives

    2n^K+1 <= q <= C(2n^K)^5.18 <= n^(6K)

for sufficiently large n. Its constant is absolute/effective. Trial division
while enumerating progression candidates already costs polynomial time in
unary n for fixed K; the finite prefix is absorbed by a constant. Root
enumeration is also polynomial in n here, though B_Q does not need roots.
This does not assert polynomial time in log n alone.

Using L<=2n sqrt(q) and 2n+1<=3n,

    sigma <=12 sqrt(m)n^3 sqrt(q)ell^3,
    q/(n sigma)>=sqrt(2)n/(12ell^3) -> infinity.

Thus q/sigma>=n eventually. For the larger d,

    log_2(q^d)<=6K ell * n/(24K ell)=n/4.

The smaller floor(sqrt(n)/ell^4) is eventually no larger, because the ratio
of the unfloored quantities is 24K/(sqrt(n)ell^3)->0. Since
D_ell(0)<=1/ell,

    q^d ((1+D_ell(0))/2)^n
      <=2^(-3n/4+n/(ell ln 2)) <=2^(-n/2)

eventually. Floors only improve these upper bounds. The first B_exp term is
exp(-Omega(n^2)); the second is exp(-Omega(n log n)). Their square root times
m is negligible. Both n kappa(3ell^2/4) and (m+2)n exp(-pi ell^2)/(pi ell)
are negligible; hence Delta and eta are negligible as well.

These estimates use the explicit NEW q family. They do not import hardness
from the September modulus, or make the error negligible for arbitrary
polynomial q at an unchanged d. Each h fixes its own family before the solver
and its success exponent. m=3 is covered eventually with h=1, n>=4; h=0
restricts m to 1. This does not establish all polynomial sample exponents at
one fixed modulus family.

The exact sampler counts in theorem-v2 match the public code path: n secret
bits, 2mn interval draws, mn D_L draws, mn D_sigma draws, 3m ring
multiplications, O(m) additions, and one Q call. Integer masks, M, B, Theta,
H, CRT projection and q^d exhaustive search are never computed by B_Q.
Schoolbook ring arithmetic costs O(mn^2) modular operations. Finite exact
Gaussian draws are idealized laws; the bounded implementation is separate.

The proposed bounded table construction is sound. sigma^2 and L^2 are
integers, tau_max=ceil(sigma) can be computed by integer square root, and all
widths are <=tau_max. The cutoff

    B_cut=(n+ceil(log_2(mn+2))+2)tau_max

is an integer and exceeds n times every width. Tail integration gives
exp(-Omega(n^2)) error per coefficient. B_cut and the table length are
polynomial in n for fixed h,K. Rational approximations to the weights with
absolute error 2^(-n^2)/poly(mn B_cut), clipped nonnegative if necessary and
with the zero weight exactly 1, have polynomial aggregate L1 error. The
normalizer is >=1, so normalization increases that error by only a constant
factor. Rounding a finite normalized law to nonnegative dyadic masses summing
to 1 costs at most a table-length factor times the dyadic precision. Fixed
independent bit blocks sample that dyadic law in worst-case polynomial time.
The pi/exp approximations require polynomial precision and polynomial argument
length here. No exact finite-bit implementation of an infinite-support law
is asserted.

Similarly, r random bits mapped to a length-L interval have TV at most L2^(-r);
the displayed r is enough after the 2mn draws. Total xi_alg can therefore be
negligible independently of Q. The proof's table procedure is inefficient in
practice, but that is outside the claim.

For explicit TV accounting, let P be exact Base2, P_tilde an implemented
source within xi_source, U exact uniform, K the exact whole local kernel,
and K_tilde its approximation. With a_K denoting acceptance under K,

    a_K(U) <= a_Ktilde(U)+xi_alg
      <= |a_Ktilde(U)-a_Ktilde(P_tilde)|
          +a_Ktilde(P_tilde)+xi_alg
      <= |a_Ktilde(U)-a_Ktilde(P_tilde)|
          +a_K(P)+xi_source+2xi_alg.

A complete target witness/transcript perturbation adds xi_target. This proves
the claimed implementation loss. If advantage is kept against exact P, the
xi_source term is unnecessary but conservative. An approximate uniform
comparator would require its own error, as the proof says. Marginal sampler
or transcript-only bounds would not suffice; the frozen theorem requires
the full laws.

## 8. Complete historical regression applicability

The following table covers all 43 IDs in the preserved current inventory.
PASS means the current argument was checked against the indicated failure;
OUTSIDE means the old rejected mechanism is not a dependency, with the reason
stated. It is not a new proof of every historical theorem. Evidence includes
`imports/regressions/00`–`18`, the linked historical exact hand controls,
source-scope and ledger-defect reports, and the new RF1 controls above.

| IDs | Application and outcome |
|---|---|
| R01 | OUTSIDE the proof: the retired binomial-support code family is not uniform d-subset Base2. Its block enumeration attack remains a source-premise warning; no hardness of that family is revived. |
| R02 | PASS: the C=G, H=E-FG trick destroys G's conditional product law. Here C_lat precedes and is independent of G; H is independently sampled conditional C_lat. |
| R03, R04, R05, C03-HC5, SE-CORRELATION-F3, PAIRWISE-SE-F3 | PASS: diagonal uniform pairs, sign-correlated Gaussian marginals, binary XOR, E=-S, and E=-F-S refute marginal/pairwise shortcuts. Their exact gaps include common-K TV2/3 and secret-correlated target TV2/9. The current target specifies full joint independence, and the completion compares one full mn-dimensional law. |
| R06, R07 | PASS: q=3 quotient extraction can miss residues, and a large field kernel can have singleton Boolean fibers. The current proof neither claims extraction nor infers Boolean ambiguity from field rank; it computes noisy-bit guessing directly and pays cardinality q^d for arbitrary fibers. |
| R08, C02-LATENT-PUBLIC, PUBLIC-ENCODED-F | PASS: latent TV1/2 can project to public TV0 in the F5 control, or remain 1/2 if encoded. This proof uses latent information solely for a guessing UPPER bound and a valid forward channel. It does not infer a public lower bound from latent distance. |
| R09 | OUTSIDE: strict injection thresholds and Lucas full-occupancy claims are unused. The (2,1) missing class at n=4,8,16 remains a counterexample to full occupancy, not to the cardinality leakage inequality. |
| R10, C01-ATT | OUTSIDE: no residual-box distinguisher, dual rounding, norm uniqueness, or claimed optimized attack runtime occurs. The wrapper needs no roots; the restricted effective family's optional root enumeration is polynomial in n, not an unjustified generic poly(log q) setup. |
| R11 | PASS: sometimes-lossy examples may retain average recovery near 1/2. The present planted bound is pointwise on every Good source/coin value, with the entire bad probability paid, so it gives the required average bound. |
| R12 | PASS: the two verified preimages in F3 show residual validity does not identify the original secret. B_Q tests equality with its own actual S; the success event is retained in every TV comparison. |
| R13, N03-PV-CONDITIONING | PASS / unused transfer mechanism: signed gaps can cancel in mixtures, and Renyi orientation matters. No Renyi or active-search-to-decision transfer is used; the final inequality is the elementary absolute acceptance-probability difference plus additive losses. |
| R14, N02-DUAL-NUMBER | PASS for zero-fiber warning: uniform ideal points include zeros; active-conditioning TV differs from image deficiency. The dual-number model's TV9/32 is retained as a diagnostic, not generalized to the split ring. The current proof includes zero multipliers and never needs a quotient-to-ideal isomorphism. |
| R15 | PASS: repeated noise, rotations, and common K do not supply independent target samples by themselves. The new EX-REG proves the full retained-seed law with fresh R,W. Planted rows are explicitly allowed to remain correlated. |
| R16 | PASS: no statistical closeness of planted RLWE transcripts to uniform response pairs is claimed. Only uniform SEED expansion is statistically regular. No posterior sampler or unavailable packed responses are assumed. |
| R17 | PASS / scope excluded: no independent-matrix three-point moment transfer, small symmetry orbit mixing, QCSD carry conversion, or quantum Fourier speedup is used. Ring multiplication is analyzed directly by rank and determinant, including three samples. |
| R18, CP-1, C03-HC6 | PASS: see the explicit CP-1 calculation below. Fixed independent difference coordinates and seed factors are multiplied only under declared product laws. Success and Good are combined by additive bad-mass loss. No adaptive cached-prefix stage product occurs. |
| C03-HC1, NC1-v1 | PASS: when Delta>=1 the old ratio could be negative, even for M=0 and true TV0. The current piecewise eta returns 1 on that branch. |
| C03-HC2, RECT-ALG-1 | PASS: H_seq has parity-dependent normalizers and is not D_B; positive marginal complements need not make full B positive. Current H is the full normalized lattice Gaussian, only proof-side. New three-block controls explicitly reject the marginal-only substitution. |
| C03-HC3 | PASS for the distinction: exponent parameters are never identified with exact discrete variance. The variance/monotonicity obstruction itself is OUTSIDE the proof. |
| C03-HC4 | PASS: signed Fourier inverses and fixed-width wrapped noncompletion do not contradict this positive full-lattice kernel with paid eta. No positive-ratio-implies-probability inference is used. The Renyi subcontrol is outside the TV proof. |
| C03-HC7 | OUTSIDE: the old repeated noisy-observation A1/A2 entropy thresholds are not used. The proof has one shared G and the exact one-observation bit-guessing identity. |
| C02-CHAR | PASS: negligible fixed-character bias does not imply general TV. Here Parseval sums all nontrivial squared biases, with q^n explicitly paid in the low-rank part; this closes that gap. |
| S0-dependency | PASS: no historical status is inherited. EX-REC depends explicitly on the newly checked regularity, completion, guessing and mask bounds; the asymptotic consequence additionally depends on the primary prime theorem and the new parameter substitution. |
| W2-SUBGROUP-BOUNDARY, W2-CONSTANT-COMPARISON | OUTSIDE: no all-subgroup negligible-coverage assertion or attack constant improvement is made. The n=8,d=2 coverage-one example and optimized-constant qualifications remain in force. |
| UNIFORM-APPROX-COLLAPSE | PASS / invalid no-go excluded: exact-uniform entropy obstructions cannot be extended to approximate comparator preservation. EX-REG directly proves approximate preservation; no exact-uniform entropy monotonicity inference is invoked. |
| N03-SCAL-POSTERIOR | PASS: conditioning on the public pair can fix formerly iid ratios. This proof uses no conditional ratio claim; its conditioning fixes C_lat independent of S,G, and after Y it uses joint-mass maxima rather than prior independence. |
| SOURCE-SMALL-D | PREMISE LIMITATION RETAINED: d=0 and d=1 can be easy sources; for d=1 enumerate n q ideal points and verify a small coefficient box. The finite implication is still valid, while asymptotic hardness is explicitly assumed only at each specified growing d family. No all-d plausibility claim is made. |
| A-PPT-LEDGER-SCOPE | PASS: the old arbitrary-polynomial-q reading made q^d2^(-n) enormous at q>=n^128 with d=n/(64ell). This theorem fixes q least 1 mod 2n^K and d<=n/(24Kell), explicitly recalculating log_2 q^d<=n/4. |

For CP-1, the conditioning normalizer is 10/11, yielding
A_b=21/2000, C_b=1/20, D=879/1000. The incidences are 1/10,
121/2000, and 21/2000. The selected two-hit probability is
`2*(21/2000)*(1/2)=21/2000>1/100`; the later incidence 21/221<1/10 does
not cure the false product. Support restriction and posterior normalization,
not merely failure of fresh-value independence, cause the inflation. This
proof never exposes latent cache status or uses the rejected selected-stage
product. Its pivot-coordinate bound conditions only on disjoint coordinates
of an actual product law, and its multirow TV estimate is telescoping,
not a product of conditional success probabilities.

## 9. Closed dependencies, limitations, and deliverable scope

| Current claim | Referee disposition |
|---|---|
| EX-REG, exact finite retained-seed law | PASS, including m=3, zero seeds, low-rank characters, and vacuous small parameters |
| EX-REC, actual-secret finite inequality | PASS with precisely the stated Base2 comparator and public interface |
| Full rectangular completion / guarded eta | PASS; normalized proof kernel, full cross-blocks, no covariance shortcut |
| Effective q,d,m,sigma family | PASS from the stated prime theorem and checked substitutions |
| Bounded uniform-PPT wrapper / TV accounting | PASS for fixed h, with the specified complete-law approximation errors |
| Source pseudorandomness at each new family | ASSUMED, not proved or inherited from September |
| IID planted Base_m production | NOT CLAIMED and not supplied |
| Arbitrary polynomial m at one fixed q family | NOT CLAIMED and not supplied |
| Target decision, quantum/nonuniform hardness, practical security, priority | OUTSIDE this theorem and review |
| Fresh blind and final integration gates | Separate coordinator obligations; this report does not replace them |

The mathematical dependencies of the reviewed claim close in the exact
statement's conditional scope. No author-proof counterexample or unresolved
analytic/algorithmic lemma remains from this referee. The stale theorem-v1
header should be corrected in the canonical publication artifact; any
scientific edit needs a versioned recheck. Complete code/output and negative
controls are preserved, and the report/hash receipt names the exact input
hashes. All RF1 work stayed in its owned directory, all RB1 artifacts stayed
unchanged, and RB2 isolation was respected.
