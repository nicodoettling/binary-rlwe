# A nontrivial restricted ideal-SuperSVP consequence of the fractional route

PROVISIONAL v2. V1 parameter example is rejected as written; see restricted-supersvp-v1-parameter-correction.md. This is a conditional consequence of A-FRAC, B-GP finite bridge, and C-OHCP-v4, plus a primary quantum BDD-to-DGS theorem. It is not a claim that this restricted SuperSVP family is standard-hard. All source-composition dependencies need their own review.

## 1. Uniform input family and direction

Let R=Z[X]/(X^n+1), n a power of two, and fix rho<1. Let J range over EVERY integral ideal with D=N(J)<=2^(rho n) and gcd(D,q)=1. Give J by an ordinary basis, with no short ideal basis, trapdoor, preprocessing advice, or distribution on J. Assume a fixed binary-recovery algorithm gives, through A/B's exact pointwise composition, a distinguisher of advantage delta for the finite periodic Gaussian experiment of C-OHCP-v4 for every such J. This pointwise qualification is essential.

The reduction direction is

    restricted ideal short-vector problem
      <= quantum DGS on the same J
      <= quantum BDD on qJ^-1
      <= classical finite Gaussian-periodic decision
      <= classical original binary recovery.

The first two arrows below concern exact widths and the SAME ideal family. They do not import a reduction from arbitrary ideals to bounded-index ideals.

## 2. Primary quantum import and exact scales

BRST, Continuous LWE, Lemma3.4 (citing Regev Lemma3.14), states that BDD on L* within Euclidean radius d<lambda1(L*)/2 gives a quantum sample from D_(L,sqrt(n)/(sqrt(2)d)). We use the full canonical embedding. C-OHCP provides a stronger infinity-radius promise; it in particular solves the Euclidean radius d0 problem on L0=qJ^-1.

The canonical Euclidean dual is L0*=conjugate(J)/(nq). Scaling its Gaussian output by nq and conjugating therefore gives D_J at canonical width

    s_can = nq sqrt(n)/(sqrt(2)d0).

The coefficient width and a convenient output radius are

    s_J = nq/(sqrt(2)d0),
    R_out = sqrt(n) s_J = n^(3/2)q/(sqrt(2)d0).

There is no missing n factor: sigma(R)=sqrt(n) times an orthogonal copy of Z^n, and L0*=conjugate(J)/(nq). For canonical benchmark width w=sqrt(n) w_B and v0=2sqrt(n)a, C's radius is

    d0=delta*w_B/(64nka),
    R_out=(64/sqrt(2))*n^(5/2)*k*a*q/(delta*w_B).

These equalities assume the minimal v0 choice meets uniqueness; otherwise use the actual v0 and d0. The polynomial windows below make uniqueness automatic.

The quantum lemma requires coherent access to the BDD algorithm. Given the actual finite recovery/distinguisher circuit, C's bounded finite procedure can be reversibly simulated and uncomputed, with coins retained. It is not enough to have an opaque classical-only remote oracle. Set C's pointwise failure exponentially small before this invocation. Standard coherent purification bounds charge O(sqrt(epsilon_BDD)) per oracle use; the primary quantum circuit has polynomially many uses, so the resulting output loss is negligible. No quantum assumption is hidden in the preceding classical GP-to-BDD edge.

Primary source: https://arxiv.org/pdf/2005.09595, Lemma3.4, printed p11 (PDF page10). The paper's exact statement was reread directly for this calculation.

## 3. Nonzero output and smoothing requirement

A sufficient explicit coefficient smoothing bound for integral ideal J is

    eta_(exp(-n))(J)<=sqrt(n) D^(1/n).

It follows from the ideal-dual algebraic norm and the independent theta packing estimate. Hence s_J>=2sqrt(n)D^(1/n) implies s_J>=2eta_(exp(-n))(J). Under this condition the Gaussian mass at zero is at most 2^-n(1+exp(-n))/(1-exp(-n)). For the norm tail, exponential Markov gives

    Pr[||X||coef>s_J sqrt(n)]
      <= exp(-pi n/2) rho_(sqrt(2)s_J)(J)/rho_(s_J)(J)
      <= [(1+exp(-n))/(1-exp(-n))]*(sqrt(2)exp(-pi/2))^n.

Both are exponentially small. Test zero and the displayed norm bound explicitly, and repeat a polynomial number of times if desired. The output is then a nonzero element of J of coefficient norm at most R_out, except with the negligible imported sampling error. The quantum sampling law is retained rather than replacing it by an arbitrary short-vector oracle.

C's uniqueness bound d0<q/(4D^(1/n)) itself gives s_J>2sqrt(2)nD^(1/n), which dominates the above sufficient smoothing bound for n>=2. Thus there is no incompatible smoothing requirement in this restricted consequence.

## 4. Instantiation as the q0-ary ideal SuperSVP pair

Take a different split prime q0 coprime to q. For any d-subset T of roots modulo q0, define K_T=q0 preimage(I_T)^{*coef}, as in partial-v1. It is an integral ideal of norm q0^d. With J=K_T and q0^d<=2^(rho n), the preceding reduction solves the restricted SuperSVP pair

    (K_T subset Z^n, r=1, beta=1, quotient index q0^d)

at absolute output radius R_out. Its public exponent-q0 solution has norm q0, so the result is genuinely below that trivial guarantee whenever

    q0 > (64/sqrt(2))*n^(5/2)*k*a*q/(delta*w_B).

This is a simultaneous inequality, not a new hardness claim. For fixed k and constant delta, w_B=ell² with ell=ceil(log2(2nk)), choose kappa=Theta(n log(nq)) with kappa>=2log(8n), and zeta=exp(-kappa/2). This satisfies C's constraint kappa>=log(8n/zeta); the v1 choice zeta=exp(-kappa) did not. The symbolic primary polynomial Q_* contributes only O(log kappa) to log(1/epsilon0), hence a=O(sqrt(n log(nq))). Therefore

    R_out=O(n^3 q sqrt(log(nq))/ell²).

A's proposed binary target has sigma_target=8n²ceil(sqrt(kn))ell^4 and can use a split q>=n^c sigma_target of polynomial size. Choose an auxiliary split prime q0 of polynomial size satisfying q0/R_out -> infinity, and

    d=floor(rho*n/log2 q0).

For all sufficiently large n this has d>=1 and satisfies q0^d<=2^(rho n). The prime choices are supplied public parameters here; this calculation does not assert a prime-finding theorem in a prescribed interval without checking it. Both q and q0 may be selected from the permitted split-prime parameter families, with q0 larger and distinct. The bound is uniform in T, so no random-T averaging or hidden-ideal assumption is used.

When delta is merely inverse polynomial, enlarge kappa and q0 by the corresponding polynomial factors, and record the resulting approximation regime. One cannot silently claim the constant-delta polynomial exponent for all adversaries.

## 5. What 2026/2443 contributes and what it does not

The supplied paper makes it natural to report the public Z^n superlattice basis and the quotient exponent alongside an absolute output radius. That exposes a nonempty and nontrivial restricted ideal regime of our separate Gaussian-periodic chain. The paper's own dense hinted-SIS/LWE endpoints are not used in the above implication.

Neither its general-lattice SuperSVP theorem nor its reverse reduction proves hardness for the restricted ideal pairs K_T subset Z^n. The standard-family normalization edge remains open, as recorded in periodic-hardness/standard-family-boundary-v1.md. This packet is a meaningful nonstandard worst-case consequence if its dependencies pass review; it cannot complete the running standard-hardness goal by renaming the restricted family.
