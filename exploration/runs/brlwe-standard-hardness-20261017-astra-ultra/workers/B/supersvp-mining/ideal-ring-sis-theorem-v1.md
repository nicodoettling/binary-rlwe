# B-SUP-IR-T v1 — natural-inclusion ideal to ring succinct-SIS map

Status: PROVISIONAL new theorem, not accepted. This is a one-vector reduction for a restricted ideal/SuperSVP input, with explicit sampling dependencies. It is NOT a consequence of the general-matrix hardness theorem by substitution, NOT a standard worst-case hardness theorem for the low-index family, and NOT a binary-secret reduction. Proof: ideal-ring-sis-proof-v1.md.

## Input, conventions, and parameters

Let R=Z[X]/(X^n+1), n>=2 a power of two; all norms are coefficient Euclidean norms. Let q be an odd prime splitting R, J an integral ideal with ordinary integer COLUMN basis B and D=[R:J] coprime to q. The reduction receives B. No basis of J is published. Its superlattice is the known R, with index D and basis norm 1. This is only the restricted ideal family of SuperSVP, with one copy.

Compute the invariant-factor quotient R/J. Let k be its binary gadget length, k<=2log_2 D. Let g_1,...,g_k in R be its bit-generator columns. Nearest-plane round g_l to b'_l in J/q using B/q. Put C_l=q b'_l in J. For k=0 these blocks are empty.

Fix rational p>=1 and define K=round((q/p)B^-1) entrywise. Let

  R0 = sqrt(n)/2 + k sqrt(n)||B||op/(2q),
  Z1 = p R0 + sqrt(n)/2,
  Zrem = (q/p)||B^-1||op sqrt(n)/2 + (n/2)Z1.

Choose integer r>=1 with 2^r-1>=Zrem and let G be the n by nr signed-binary gadget with columns 2^j e_i, 0<=j<r. Write b=nr, t=n+b, h>=3ceil(log_2 q), m=h+t, gq=ceil(log_2 q). Define deterministic ring columns E1=columns(BK), E2=columns(BG), C=columns(qB'). Bounds may be replaced by larger rational bounds so their computation does not require exact irrational comparisons.

Choose 0<epsilon<=1/16 and sigma>=2eta_epsilon(J). Initial ideal-Gaussian sampling to total error delta_init over all capped attempts is a separate charged implementation parameter. One explicit sufficient implementation is given in the proof. Let ell>=1 be a rational tail cutoff, and set

  gamma_hash = (1/2)sqrt((1+(q-1)2^-h)^n-1),
  delta_pub = h epsilon/(1-epsilon) + (t+k) gamma_hash,
  alpha = 1-nq^-m-delta_pub > 0,
  Btrap = max(1, sqrt(n)Z1+b+k),
  N=n(m+k),  tau_hint>=N Btrap log n,
  H=sigma n sqrt(h) ell sqrt(1+n^2 h t)
        + (sqrt(n)/q)||[BK | BG]||F,
  beta_zero = t q^n 2^(-nh)/alpha + 2^-n(1+epsilon)/(1-epsilon),
  beta_tail = 2hn exp(-pi ell^2)/alpha.

Use a cap a>=1 independent fresh attempts. Let delta_hint=gq 2^-n+delta_pre denote the full-joint canonical preimage-sampler error, including explicitly charged numerical implementation error delta_pre. Set

  delta_impl = delta_init + (1-alpha)^a + delta_hint,
  Delta = 2delta_pub/alpha + delta_impl.

The canonical preimage-sampler primitive is the precise SamplePre guarantee in primary 2026/2443 Lemma3.6: coefficient-expanded dimension n by N, a gadget trapdoor of maximum entry Btrap, width at least N Btrap log n, and error 2^-n per target. This algorithmic import and its cited WWW25 source remain separate review dependencies.

## Exact private construction and both public endpoints

In each attempt independently sample v_i~D_(J/q,sigma), i=1,...,h; set V=(v_i) and A0=qV mod qR. Independently sample R1 in R^(h by n), R2 in R^(h by b), S in R^(h by k), with every coefficient independently uniform in {-1,+1}. Define

  A = [A0 | A0 R1+E1 | A0 R2+E2] in Rq^m,
  W = C+A0 S in Rq^k,
  Q = [V | V R1+E1/q | V R2+E2/q] in (J/q)^m.

Keep only the first attempt for which A generates the unit ideal in Rq, equivalently A has a nonzero entry at every CRT root. Use fresh attempts; do not reuse any failed row or latent. If every attempt fails, return a declared failure symbol. The accepted retained state has the exact single-attempt law conditioned on this rank event, before implementation approximation.

Construct a bounded gadget trapdoor for Dpub=[A|W] as in the proof, and sample T with gq ring columns from the canonical law

  T_j ~ D_(Z^N,tau_hint) conditioned on Dpub T_j=2^j in Rq,

independently conditional on A,W. The actual finite SamplePre output has the charged delta_hint distance from this law while retaining the COMPLETE private state. Publish only (A,W,T); discard B,V,R1,R2,S,Q and the bounded construction trapdoor from the solver's view.

The ideal target public law is A uniform in Rq^m conditioned on the stated rank event, W independent uniform in Rq^k, and T from this exact canonical conditional law. The real public triple is within Delta of that target.

For any fixed efficiently samplable secret law Secret on Rq, independent of the construction, and any fixed independent error law E on Rq^m, this supplies BOTH full response endpoints:

  planted: (A,W,T, sA+e), s~Secret, e~E;
  comparator: (A,W,T, u), u uniform in Rq^m.

The real and ideal versions of EACH endpoint have distance at most Delta. This is a common-key simulation theorem; it does not change Secret. In particular, choosing coefficient bits defines a binary experiment but supplies no hardness for it. Giving the private masks or original basis to the distinguisher changes the stated joint law and is excluded.

## Reduction direction and loss

Suppose an algorithm on the IDEAL public ring succinct-SIS law returns x in R^m satisfying Ax=0 mod q and 0<||x||coef<=gamma with probability delta. The construction invokes it once and returns Qx if nonzero and of norm at most gamma H, otherwise fails. Its success probability is at least

  delta - Delta - beta_zero - beta_tail.

Every returned vector belongs to J. The construction uses h initial ideal-Gaussian samples per attempt, one SIS call, at most a attempts, and gq canonical ring preimage samples. Its runtime is expected polynomial in all dimensions, a, the COMPLETE binary encodings of B and every rational/integer parameter and requested precision, plus the SIS runtime and the explicit Gaussian/preimage implementation costs. No short J-basis is supplied as public advice.

The same law comparison gives response-distinguisher advantage loss at most 2Delta between the real and ideal response experiments; it does not turn a response distinguisher into an SIS solver by itself. The paper's quantum uniform-secret Fourier/search step, its search-to-decision losses and its extra auxiliary-width conditions must be separately reconstructed for this ring ensemble before any further implication is claimed.

## Parameter and foundation boundary

Taking h>=ceil(log_2(q-1))+2lambda+ceil(log_2 n)+O(log(t+k)) makes the CRT extraction term negligible; h>=3ceil(log_2 q) can be imposed simultaneously. The ring multiplication losses in H and the coefficient-expanded hint width are polynomial in n,h,t,ell. k<=2log_2 D by itself is insufficient to remove E1/E2: the integral carry/residual blocks are essential.

A nonempty algebraic/algorithmic window exists by taking q sufficiently large relative to the supplied basis and choosing sigma above both 2eta_epsilon(J) and the basis-dependent sampling floor. That is not a proof that gamma H is hard for this restricted input family. Low-index ideals with R as a short superlattice are not known here to capture standard worst-case ideal-SVP or RLWE hardness. No accepted primary theorem closing that gap is imported. All finite estimates and the new ring lifting proof still require adversarial review.
