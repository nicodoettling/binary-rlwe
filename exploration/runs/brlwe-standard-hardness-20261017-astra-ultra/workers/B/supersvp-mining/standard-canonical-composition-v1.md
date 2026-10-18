# B-SUP-STD-C v1: complete standard-input to canonical-hint composition

Status: PROVISIONAL composed construction; all constituent new results remain subject to independent review. This packet closes a standard uniform-secret RLWE input edge to the explicitly defined canonical hinted ring experiment. It does NOT close the binary-secret or low-index fractional-source edge.

## 1. Parameters and exact target experiment

Let n be a power of two, q>=5 a split prime, degree L>=1, padded gadget length g>=ceil(log2q), h>=2g, M=L²g, N=nM. Let sigma_R>=2. Use the exact standard-rlwe-decomposed-theorem-v1.md source and triangular-endpoints-v1.md map, with the same L,g,h and integer-coefficient Gaussian R width sigma_R. No module secret or changed ring dimension is introduced.

The FINAL public law is

  A uniform Rq^(1 by M), W uniform Rq^(L by h), independently;
  T has independent integer coefficient-Gaussian columns of width sigma_hint,
    conditioned on [I_L tensor A | W]T=I_L tensor G.

There are Lg ring columns of T, each of ring height LM+h; its coefficient representation has n(LM+h) rows and Lg sampled columns. Each ring column expands to n rotations when expressing the gadget identity, but the canonical law samples ONE coefficient vector per ring column, not n independent rotations. The final published tuple is (A,b,W,T), with either b=sA+e_out, s uniform Rq, e_out iid coefficient D_tau_out, or b independently uniform Rq^M. The identity and canonical hint are the complete public metadata. Neither source decomposition R nor triangular X nor the temporary trapdoor is retained.

The same maps preserve any other specified source secret law, including binary, but standard uniform-secret hardness only yields the UNIFORM-secret target stated here.

## 2. Full map, losses and resources

Start with M standard ring samples (a_i,b_i) sharing s. Sample the complete h by Lg ring R, and test FULL concatenated rank. On failure emit a common declared symbol. On success sample each Wi uniformly from the FULL affine fiber WiR=a_irow-diag_i G. The source response is retained verbatim. This gives both decomposed endpoints within

  rho=min(1,n(q^(Lg)-1)mu^h), mu=min(1,1/sigma_R+1/q).

Apply the triangular map: X is g by(M-g), iid ternary coefficients; S=[[I,X],[0,I]], Astar=AdecS and bstar=bS+f. Abort if any R coefficient exceeds B. On the surviving branch the explicit integer trapdoor is the stacked S^-1 blocks and -R. Sample the canonical T from it at width

  sigma_hint >= n(LM+h) max(1,B) log(nL).

The coefficient-expanded general preimage SAMPLER applies to this supplied ring trapdoor; no general-matrix hardness theorem is used. Its dimension is nL equations by n(LM+h) variables, and its total canonical error is at most Lg2^(-nL), plus separately charged numerical/sampler error. Use the retained-INTEGER output convention checked in the primary sampler packet; a reduced modq representative is insufficient.

Let B_S=1+n sqrt(g(M-g)), choose tau>=2 eta_epsilon(Z^N), tau_out>=2tau B_S, and sample integer f with covariance parameter

  F=tau_out²I-tau² S_c^T S_c.

Then eS+f is within delta_noise=epsilon/(1-epsilon)+delta_F of iid D_tau_out. The proof retains its posterior theta normalizer. The finite elliptical sampler-v2 supplies a candidate implementation, counting all rational covariance encoding lengths; its approximation is included in delta_F. The uniform response remains EXACT conditional uniform under the ideal finite-field map, even with approximate f, as S is unimodular and f is independent of b.

Write alpha_R=Pr[max coefficient|R|>B], delta_hint=Lg2^(-nL), and

  gamma_R=.5 sqrt((1+(q-1)mu^h)^n-1),
  gamma_X=.5 sqrt((1+(q-1)3^-g)^n-1),
  delta_ext=g gamma_R+(M-g)gamma_X+2n q^-h.

For EXACT discrete-D_tau standard input, the full final planted/comparator distances are bounded respectively by

  E_P=rho+2alpha_R+delta_ext+delta_hint+delta_noise+delta_impl,
  E_Q=rho+2alpha_R+delta_ext+delta_hint+delta_impl.

Here delta_impl is a complete per-endpoint implementation budget excluding delta_F already displayed. Every fallback is explicit; ranks and tail events are not conditioned away. A canonical-hint distinguisher of advantage delta therefore gives a standard input distinguisher of advantage at least delta-E_P-E_Q. It uses exactly M input samples and one target call. Storage and arithmetic are polynomial in n,L,g,h,logq, all parameter encoding lengths and log inverse accuracy. Finite-field linear algebra samples each complete affine fiber; its coefficients use O(logq) bits. The sampled public T has polynomial dimension and polynomial bit length. Strict polynomial runtime uses bounded elementary rejection loops with their error absorbed in delta_impl; expected polynomial samplers alone do not establish that strict claim.

## 3. Continuous standard Gaussian to the discrete source, explicitly

The checked standard worst-case theorem is initially continuous, so the following extra step is required. In the primal coefficient convention let continuous errors have spherical width tau0 and let r>=eta_epsilon0(Z^N). For each real coefficient x of a response, independently output k in Z with probability proportional exp(-pi(k-x)²/r²). This randomized discretization commutes with every integer translation and therefore with reduction moduloq. The comparator becomes EXACT independent uniform integer residues. On a planted integer secret/multiplier shift, the error output is this same rounding applied to the continuous error.

Put tau²=tau0²+r². Integrating the continuous error density against this kernel gives a mass proportional to exp(-pi||k||²/tau²), times the conditional expectation of 1/rho_r(Z^N-x) under the Gaussian completion for x given k. By Poisson summation,

  rho_r(Z^N-x)/r^N lies in[1-epsilon0,1+epsilon0]

uniformly in x. Consequently the unnormalized multiplicative factor lies between (1+epsilon0)^-1 and (1-epsilon0)^-1; normalizing by its ACTUAL expectation gives TV at most epsilon0/(1-epsilon0). This is a joint N-dimensional comparison, not covariance matching. The planted loss E_P gains this amount; the ideal comparator gains zero. Finite real input/rounding precision is separately included in delta_impl. The operational convention is the usual finite-precision continuous RLWE model from the primary theorem; accuracy needed here is polynomial, and arbitrary hidden rational encoding lengths are not omitted.

Primary source check: LPR, A Toolkit for Ring-LWE Cryptography, Theorem2.22 and Lemma2.23, author PDF https://sites.cc.gatech.edu/fac/cpeikert/pubs/toolkit.pdf . The first theorem covers split polynomial primes with alpha q=omega(sqrt(logn)); its M-sample canonical width is alpha q(nM/log(nM))^(1/4), with a quantum ideal-SVP/SIVP reduction at factor O-tilde(sqrt(n)/alpha). Lemma2.23 allows equivariant randomized discretization and preserves the uniform endpoint. For the power-of-two ring, multiplying the dual response by n converts canonical continuous width r_can into coefficient width tau0=sqrt(n)r_can. No rounded-continuous distribution is identified with an exact discrete Gaussian without the comparison above. These are source theorem hypotheses, not an assertion that every allowed ideal approximation factor is computationally hard.

## 4. Nonempty polynomial parameter intersection

Fix an integer b>=0 and let L=n^b. Choose a polynomial-value split prime family with q>=n^(2b+8); an effective least-prime construction in the progression1 modulo2n^(2b+8) gives a polynomial bound via the usual fixed Linnik exponent. Its only role is to provide a split polynomial prime with the stated lower bound. Set

  kappa=8[n+ceil(log2q)+ceil(log2(L+1))+1], g=kappa,
  sigma_R=2,
  h=2[Lg ceil(log2q)+kappa+ceil(log2n)]+2g,
  B=2 ceil(sqrt(kappa+ceil(log2(4nhLg))+1)),
  epsilon=epsilon0=2^-kappa,
  r=ceil(sqrt(kappa+ceil(log2(8N))+1)), tau0=n^(b+3),
  tau²=tau0²+r²,
  tau_out=4 n^(b+3)(1+nLg).

All inequalities in Sections1–3 hold for sufficiently large n. The displayed r smooths Z^N: its nonzero dual Gaussian mass is bounded by exp(4N exp(-pi r²))-1<=epsilon0. The same estimate shows tau>=2eta_epsilon(Z^N). The scalar D_2 tail and a union bound give alpha_R<=2nhLg exp(-piB²/4)<=2^-kappa. Since mu<=.7<2^-1/2, rho<=2^-kappa. The explicit extraction expression gives delta_ext=2^-Omega(n); canonical error Lg2^-nL is negligible. Select the bounded sampler budgets negligible as well.

Asymptotically g=O(n), h=O(n^(b+1)logn), M=O(n^(2b+1)), B=O(sqrt(n)), tau=Theta(n^(b+3)), and

  tau_out=O(n^(2b+5)),
  sigma_hint=O(n^(3b+5/2) polylog(n)),
  q/tau_out=Omega(n^3)

up to fixed constants and, for the b=0 hint expression, harmless logarithmic factors. Thus standard sample count, mask/hint size, response-noise blowup and computation are all polynomial, and the output response noise is meaningfully belowq.

For the standard continuous source take

  alpha=tau0/[sqrt(n) q (nM/log(nM))^(1/4)].

Then alpha q=n^(b/2+2) times a fixed logarithmic factor, satisfying the primary floor; the ideal-lattice approximation factor is polynomial because q is polynomial. The source remains uniform-secret RLWE throughout. The output is a NEW canonical hinted ring distribution; this composition does not place its multipliers in a sparse ideal, remove the W term from hints, or prove the low-index fractional Gaussian source hard. The binary-secret computational-foundations question therefore remains open.
