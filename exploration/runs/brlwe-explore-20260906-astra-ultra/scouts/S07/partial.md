# S07 working note — structured multiplication on binary differences

Run: brlwe-explore-20260906-astra-ultra. Started 2026-09-06 09:44:24 UTC. Only `context/formal-only.md` read initially. Literature/barrier release: 09:55 UTC. Task deadline: 10:14:30 UTC. No experiment requested or run.

## Reference ledger

Unless explicitly varied: growing power-of-two degree n; odd polynomially bounded modulus q; module rank one; coefficient basis of Z_q[X]/(X^n+1); iid uniform binary secret; independent coefficient D_sigma errors and independent uniform A_i; at most polynomially many ring samples. Errors in modular likelihoods use W_{sigma,q}. Rotations are deterministic correlated transformations.

## Pre-release representation

**Fully written small calculation (in progress).** For a candidate difference d in {-1,0,1}^n, study the complete directional image M_A d=A d mod q, and jointly (A d,A e), rather than a global singular-value statistic. A fixed unit d gives exactly uniform A d. For composite q, a nonzero ternary d is a primitive vector because one coefficient is ±1; iid uniform matrices therefore still give uniform H d, while ring multiplication may instead give uniform mass on the ideal (d).

For coefficient dot products and additive character chi(t)=exp(2 pi i t/q), the ring joint character is E_A chi(<u,A d>+<v,A e>)=1{M_d^T u+M_e^T v=0 mod q}. The iid-matrix character is E_H chi(<u,H d>+<v,H e>)=1{u d^T+v e^T=0 mod q}. This remains exact without unwrapping the modulus. The first question is how much of this pairwise dependence survives after wrapped error smoothing and after averaging over differences drawn from the binary-secret prior.

Status: no hardness implication yet; public circulancy alone is not a planted distinguisher.

### Pre-release: noise-smoothed likelihood field

**Fully written small calculation.** For one ring sample under the null law A,B independent uniform, put L_s=q^n prod_j W_{sigma,q}(B-A s)_j. Then E L_s=1 and

E[L_s L_t] = sum_{u: M_{t-s}^T u=0} |hat W(u)|^2,

where hat W(u)=prod_j E_{E~D_sigma} exp(2 pi i u_j E/q). Thus unit differences match iid matrices exactly at the second likelihood moment. Nonunits need not match; their first possible discrepancy is already second order.

For d=t-s and e=v-s, the third likelihood moment is

E[L_s L_t L_v] = sum_{a,b: M_d^T a+M_e^T b=0} hat W(a) hat W(b) hat W(a+b).

The iid-matrix replacement instead has a d^T+b e^T=0. Its only solution is a=b=0 for any three distinct binary candidates, even for composite q: the n-by-2 array [d,e] has a 2-by-2 minor ±1. Indeed its nonzero row types, up to a common row sign, are (1,0),(0,1),(1,1); distinct candidates force at least two types. Thus the iid third moment is exactly 1. The ring has universal syzygies a=M_e^T h, b=-M_d^T h. This is an exact modular Fourier identity; no independent rotation or unwrapped-noise assumption enters.

For h a coefficient unit vector, all coordinates of a,b,a+b belong to {-1,0,1}, up to negacyclic signs. Write alpha=E cos(2 pi E/q)>0 and K=# {j: s_j,t_j,v_j are not all equal}. The resulting term equals alpha^(2K). For an independent binary triple, K~Binomial(n,3/4), hence a natural syzygy has typically weight approximately alpha^(3n/2). The chosen h and -h give two distinct nonzero syzygies because q is odd, so the ring third moment is at least 1+2 alpha^(2K), without a unit assumption. If either d or e is a unit, the ±n coefficient-vector choices are all distinct and give the stronger bound 1+2n alpha^(2K).

**Fully written small calculation.** Averaging the single-syzygy weight over independent binary triples gives E alpha^(2K)=((1+3 alpha^2)/4)^n. Restricting to distinct triples changes an unnormalized expectation by at most 3*2^(-n). Thus the cubic discrepancy is typical-prior, not merely caused by a specially chosen sparse difference. For growing sigma, Poisson summation gives alpha approximately exp(-pi sigma^2/q^2); the exact alpha formula should be retained in any formal comparison. This exposes a constant-size moment obstruction when sigma sqrt(n)/q is bounded. It is only a moment obstruction, not an efficient attack or hardness result.

### Typical versus uniform cube directions

**Fully written small calculation.** Explicit specialization: q prime and q=1 mod 2n, so R_q splits completely. If 2^n>q, evaluating all binary polynomials at any root forces two distinct binary polynomials to collide. Their nonzero ternary difference is a nonunit. Thus a claim uniform over all cube differences cannot simply discard nonunits, even if a typical-difference unit statement could be shown. The typical unit probability requires a separate arithmetic estimate and is not inferred from random-matrix singular values.

More quantitatively, for any fixed split root rho, let p_r=Pr[S(rho)=r]. Then Pr[(S-T)(rho)=0]=sum_r p_r^2>=1/q. Removing S=T leaves probability at least 1/q-2^(-n) of a nonzero nonunit difference. Since q is polynomial, this bad event is not negligible in the cryptographic sense, although its probability can tend to zero. This does not prove that such differences yield a useful attack: wrapped error can suppress all nonzero annihilator characters.

**Heuristic / unresolved comparison mechanism.** A plausible comparison object must preserve the ring syzygy lattice, rather than replace the design by an iid matrix. One candidate object is the noise-weighted multi-candidate character sum above, or the distribution of the posterior likelihood field after explicitly retaining its cubic ring terms. A useful hardness bridge would need a reduction from a known hard source to a distribution with these same terms, together with an algorithmically meaningful comparison (bounded tests or recovery probability); agreement of selected moments or global singular values does not supply either requirement.

**Serious objection.** Large third moments may be driven by rare transcript likelihood spikes and need not separate bounded algorithmic observables. Even a typical binary-triple moment mismatch is not automatically a total-variation lower bound for planted-mixture laws. Conversely, the syzygy is publicly computable from the design and chosen directions; its existence is not a planted-secret attack.

**Fully written small calculation illustrating the objection.** In the noiseless illustrative limit (explicit departure: sigma tends to zero), if d is a unit and s,t,v are distinct, the ring cubic moment is q^n: all three exact-fit likelihoods intersect only at A=0,B=0, which has null probability q^(-2n), while their product is q^(3n). The iid cubic moment is 1. This shows why raw moment comparison may be destroyed by rare public designs even when one is ultimately interested only in bounded recovery tests. The zero-noise limit is not substituted into the reference problem.

The actual candidate residuals all share B, hence their syzygy character can cancel B identically under both planted and null laws. A proposed attack that merely checks this relation would recognize the public ring design and fail to distinguish planting. A useful comparison theorem must target the Bayesian experiment or recovery risk, not full-design total variation.

**Cheap analytic diagnostic.** Before running matrix universality simulations, plug h equal to one coefficient vector into the exact third-moment character sum. It gives a nonzero contribution alpha^(2K) absent for an iid matrix with linearly independent directions. This uses no CPU experiment and no unwrapped error approximation. Any claimed iid comparison should state whether its observable class can detect this contribution, or prove that smoothing/truncation removes it.

### Consequences and normalization details

For m genuinely independent ring samples, each displayed likelihood moment is raised to the m-th power. This follows from independent (A_i,B_i), never from rotations.

The exact alpha avoids width/variance confusion. If v_sigma=Var(D_sigma), cos(x)>=1-x^2/2 gives alpha>=1-2 pi^2 v_sigma/q^2. Consequently q^2 at least a fixed sufficiently large multiple of n v_sigma already leaves a positive constant lower bound on alpha^(2K), uniformly in K<=n. For growing sigma, v_sigma~sigma^2/(2 pi), yielding the stated width scale q/sigma~sqrt(n).

**Unresolved.** Independent-sample concentration of pairwise likelihood metrics for unit differences may support union bounds or information-theoretic decoding statements. Those statements do not compare efficient inference. A multi-candidate comparison is the first place where the exact ring syzygies must be confronted.

### Candidate comparison target, kept deliberately narrow

For a tuple s_0,...,s_r define the algebraic object K(s_0,...,s_r)=ker [M_{s_1-s_0}^T ... M_{s_r-s_0}^T] over Z_q. The (r+1)-st likelihood moment is exactly its noise-weighted character sum, with the additional weight for minus the sum of the r frequency vectors. Thus a ring-preserving comparison should compare these weighted kernels (or a bounded posterior functional derived from them), not replace their block row by the iid outer-product constraints.

**Unresolved missing hardness step.** For any fixed algorithm g, its binary-secret success probability is 2^(-n) E_null L_{g(A,B)}; this remains true for m samples using the product likelihood. A theorem comparing a few raw moments of fixed candidates does not compare this data-dependent functional. An algorithm can also recognize the public matrix family before acting. A hardness bridge therefore still needs a source-to-target simulation/reduction and control of efficient, data-dependent recovery risk. No such theorem is supplied by this scout.

### Final arithmetic check and closure

The scalar Fourier coefficient is positive for every residue u: Poisson summation writes it as the ratio [sum_{k in Z} exp(-pi sigma^2 (k+u/q)^2)]/[sum_{k in Z} exp(-pi sigma^2 k^2)]. Therefore retaining the two selected syzygies gives a valid lower bound; no omitted term is negative. Transposes of negacyclic multiplication apply the same signed permutation to d, e, and e-d for a fixed coefficient h, so their combined number of nonzero entries is exactly 2K. The iid rank argument uses a unit minor, not an unjustified field assumption.

Finished after baseline comparison and without experimentation. Final memo: `../S07.md` (566 words before any renderer-specific mathematical token counting). Source locations and initial path failures are recorded in `sources.md`. No hardness or attack claim is made.
