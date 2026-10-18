# BT7 strict blind referee report, v1

## Verdict and exact scope

**Standalone finite BDD theorem: BLOCKED / NOT CERTIFIED.** I independently reconstructed the finite quotient, Gaussian completion, uniform local smoothing, starting advantage, quantitative continuous-proxy Haar endpoint, local-to-global comparison extension, adaptive error accounting, and exact recovery. Those calculations support the analytic reduction. I did not establish the explicitly claimed finite comparison/guided-walk theorem with the displayed constants, nor the particular B-bit implementation. The permitted PRS source was inaccessible, and the frozen input does not specify the comparison weights, comparison decision rule in full, walk transition law, output rule, or numerical quantizer. The missing finite walk contract is load-bearing. BRST's polynomial-time existence result does not certify these particular constants or this finite implementation.

**Separate rejected assertion under a literal physical-law interpretation:** the actual discrete-multiplier query need not tend to Haar, and its exact finite rounded law need not tend to uniform. Section 8 gives a fully specified hand counterexample. This does **not** refute the endpoint of the continuous Gaussian proxy, the uniform approximation argument, or the BDD existence claim. It means that “the selected width tends to FULL Haar” must explicitly refer to the analytic proxy. No counterexample to the standalone BDD conclusion was established.

No standard arbitrary-ideal hardness result, fractional-composition theorem, finite Gaussian-periodic bridge, or coherent quantum implementation is certified here.

## 1. Input freeze, isolation, sources, and procedure

The only mathematical local input was `input/theorem-v6.md`, read in full. Its SHA-256 is

`9e26263bd8e59c8ab1cbd716d7d7ccc946624f80b1cac8a0027eabb0ee2dfa67`.

The binding assignment SHA-256 is

`cbedff770644a21c19770b8b15cb100c8a1e583c18459b42e5ff01f2eb71f0dd`.

Both original files were preserved byte-for-byte. `input-receipt.json` records these hashes. I also read the generic mathematical-proof-audit skill and its two procedural references. The blind assignment's prohibition on project-history intake controlled; I did not perform that intake.

I did not read project status, ledgers, summaries, proof directories, package files, other reviews, historical runs, or other workers' output. I did not call `list_agents`, communicate with another worker, spawn an agent, create a goal, run an experiment, install anything, start a service, edit Git, or write outside BT7. Tool-metadata discovery exposed only generic tool descriptions, not mathematical/project evidence. No accidental prohibited exposure occurred. This is same-model role scrutiny, not formal verification or statistically independent confirmation.

The accessible primary source was [BRST, Continuous LWE](https://arxiv.org/pdf/2005.09595), particularly Definitions 2.6 and 3.7, the supporting Gaussian statements, and Lemma 3.8. Its relevant contract is polynomial-time OHCP under a local radial law, a positive profile gap, exponential tail control, and time Lipschitz continuity. It also says query times lie on a polynomially bounded fixed grid. It supplies no displayed numerical polynomial, finite random-bit specification, or certified-real implementation matching the frozen theorem.

The sole permitted PRS URL, [the author PDF](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf), repeatedly returned HTTP 502 through both available web interfaces. A direct curl attempt failed DNS resolution. A screenshot request could not resolve a PDF. I did not substitute another URL, search result, outside snippet, remembered proof, or historical local copy. Thus Definition 4.3, Proposition 4.4, and author-version pages 12–16 were not inspected. This is an exact source-access limitation, not evidence against their contents.

The derivations below are my reconstruction from the frozen statement and elementary calculations. The physical-endpoint flaw was preserved first in `physical-endpoint-counterexample-v1.md`; the report does not overwrite that record.

## 2. Dependency assessment

| ID | Claim | Assessment |
|---|---|---|
| B1 | Finite quotient, cancellation, and uniqueness | Checked independently |
| B2 | Completion formula with both normalizers | Checked independently |
| B3 | Uniform posterior smoothing in the declared local range | Checked independently |
| B4 | Continuous-proxy starting gap, tail, and time regularity | Checked independently |
| B5 | Local-to-global comparison extension | Checked independently against the accessible OHCP contract |
| B6 | Displayed finite OCP and guided-walk constants | OPEN; primary supporting pages unavailable and full algorithm unspecified |
| B7 | Claimed B-bit path coupling and scalar implementation | OPEN; viable principles identified, specific implementation not certified |
| B8 | Adaptive accumulation of stated pointwise errors | Checked conditionally on B6/B7 and the stated sampler errors |
| B9 | Exact output recovery and two-orientation handling | Checked conditionally on successful coordinate recovery |
| E1 | Exact Haar/uniform endpoint for the physical discrete query | False in general; explicit counterexample below |
| X1 | Separate composition/bridge and quantum/family imports | Outside acceptance scope; unresolved imports remain unresolved |

The final finite BDD conclusion depends on B6 and B7, so the analytic checks do not close its certification.

## 3. Finite interface, cancellation, and uniqueness

Write the full canonical space as the real subspace of conjugate-symmetric vectors in C^n, with squared norm the sum over all n embeddings. The coefficient-to-canonical matrix is orthogonal up to sqrt(n). Thus the coefficient width really is w/sqrt(n).

For an integral ideal J of norm D, D R is contained in J, whence J^-1 is contained in D^-1 R. Therefore L=qJ^-1 is contained in (q/D)R and in hR for h=1/(DP). In coefficient coordinates,

    det(L)=q^n/D,
    |h Z^n/L|=(q^n/D)/h^n=q^n D^(n-1) P^n.

Nearest-grid rounding is equivariant under hR translations outside its measure-zero tie set. Consequently rounding a Haar point of the real torus gives exactly uniform F. Gaussian-smoothed queries have zero probability of the tie set. A finite implementation still needs to control numerical boundary errors; it cannot infer them merely from pointwise convergence.

An integral multiplier r lies in R, so r lambda belongs to L. Hence cancellation of r lambda modulo L is exact. No invertibility of r and no coprimality of D and q is needed.

Every nonzero x in J^-1 has |N(x)|>=1/D: the integral ideal xJ has positive integer norm D|N(x)|. Thus every nonzero l in L has canonical infinity norm at least q/D^(1/n). The radius condition d0<q/(4D^(1/n)) gives a strict uniqueness margin for the promised lambda.

## 4. Completion formula and uniform smoothing

Use V for the positive diagonal real width operator of the multiplier; on conjugate pair i its width is v_i. Put h=e-g(z). Let H be multiplication by h in canonical coordinates. Set

    s_i^2=w^2+v_i^2 |h_i|^2,
    u_i^2=(v_i^-2+|h_i|^2/w^2)^-1,
    c_i(x)=v_i^2 conjugate(h_i) x_i/s_i^2.

Let S and U be the corresponding real width operators. Products/determinants here count both real dimensions in each conjugate pair. For the ideal physical multiplier r sampled from D_(R,V), the density of X=Hr+G_w is exactly

    f_X(x)=rho_S(x) rho_(R,U)(c(x)) / [w^n rho_(R,V)(0)]
          =[rho_S(x)/det(S)]
             * [rho_(R,U)(c(x))/det(U)]
             / [rho_(R,V)(0)/det(V)].

The identity det(S)det(U)=w^n det(V) verifies the normalizing factors. In particular the denominator rho_(R,V)(0) must not disappear, and the shifted posterior partition function must not be replaced by its unshifted value without a uniform bound.

The lattice R is a rotated sqrt(n) Z^n in the canonical Euclidean metric. Therefore, if every posterior width is at least sqrt(n) a, Poisson summation and the product theta bound give, uniformly in the posterior center c,

    det(R) rho_(R,U)(c)/det(U) in [1-epsilon0,1+epsilon0].

For completeness: put b=exp(-pi a^2)<=epsilon0/(8n). Then

    rho_(sqrt(n)a)(R*\{0})
       =(1+2 sum_(m>=1) b^(m^2))^n-1
       <=(1+epsilon0/(2n))^n-1
       <=epsilon0.

Here a is the frozen integer, epsilon0<=1/16, and the elementary estimate sum b^(m^2)<=b/(1-b^3)<=2b is enough.

For |h_j|<=8d0 and all nuisance coordinates |h_i|<=d0,

    u_min >= v0/sqrt(1+(8v0d0/w)^2)
          = v0/sqrt(1+(delta/(4nk))^2)
          > v0/2 >= sqrt(n)a,

uniformly for every t>=0. The multiplier widths themselves are at least v0. Both theta normalizations are therefore controlled. The completion density divided by the continuous Gaussian proxy lies between (1-epsilon0)/(1+epsilon0) and (1+epsilon0)/(1-epsilon0), yielding TV at most epsilon0/(1-epsilon0).

There is also a natural multiplier implementation: mix a broad continuous center in the selected pair with an isotropic discrete Gaussian on R centered at that point. Scalar coefficient sampling then uses the known orthogonal basis of R. Comparing its shifted normalization with the V-normalization gives another epsilon0/(1-epsilon0) error. This supports the frozen combined budget 2epsilon0/(1-epsilon0), but is not a substitute for a full bounded finite sampler specification.

## 5. Continuous proxy: starting gap, time regularity, and quantitative Haar endpoint

At z=0 and t=0, the selected error coordinate is e_j+2d0 and has magnitude between d0 and 3d0. Nuisance coordinates remain bounded by d0. The proxy is G_w plus an independent Gaussian whose total second moment is at most 9n v0^2 d0^2/(2pi). A translated width-w Gaussian has TV at most the translation norm divided by w. Jensen and a deliberately loose bound therefore give single-sample TV from G_w below 3n v0d0/w. Across k samples, including rounding and reduction modulo L by data processing, the loss is below

    3nk v0d0/w = 3delta/32.

Thus the correct global orientation has a starting proxy gap at least 29delta/32, in particular above delta/2>=1/kappa. The same orientation works for every coordinate pair, because the sign of the original GP-versus-U advantage is fixed for this J.

Only the two real dimensions of the selected pair change with t, and d(log s_j)/dt<=1. Differentiating the normalized two-dimensional Gaussian scale density gives TV variation at most |dt|. Hence the k-sample proxy profile is k-Lipschitz in t, comfortably within the frozen kappa bound. This calculation applies at every spatial point for the analytic Gaussian proxy.

For the Haar endpoint, the Euclidean dual is

    L* = conjugate(J)/(nq).

Every nonzero chi in L* satisfies |N(chi)|>=D/(nq)^n. At the starting query the selected pair width is at least h0 exp(t), while all other widths are at least w. Arithmetic-geometric mean on all n embeddings yields

    ||S_t chi|| >= sqrt(n) a0 exp(2t/n).

This is a quantitative ideal norm argument; mere nonvanishing of the selected embedding would not alone provide a rate.

Here is an explicit theta estimate sufficient for the displayed kappa. If a full-rank real lattice has minimum at least sqrt(n)b with b>=1, packing the shells [m lambda,(m+1)lambda) bounds its nonzero Gaussian mass by

    sum_(m>=1) (2m+3)^n exp(-pi n b^2 m^2)
       <= 2 exp(-n b^2).

For example, log(2m+3)<=2m and pi-2>1 imply this bound by a geometric-series estimate; n>=2 gives ample slack. Therefore, for t>=S,

    TV(proxy_t mod L, Haar) <= exp[-n exp(4(t-S)/n)],

and the k-sample distance is at most k times this expression.

For t>=kappa/2, the frozen lower bound implies t>=2S and t>=2log(k+1). Consequently exp(4(t-S)/n)>=exp(2t/n) and n exp(2t/n)>=2t. The k-sample bound is at most exp(-3t/2), hence at most 2exp(-t/kappa). For t<kappa/2 the latter exceeds 1, so the trivial TV bound suffices. This verifies the needed profile tail quantitatively. Rounding turns Haar into exactly U.

These are statements about the continuous proxy. They must not be silently transferred into an exact limit statement for the physical discrete query; see Section 8.

## 6. Local-to-global comparison and adaptive accounting

Normalize z=3u and let u*=z*/3. Then ||u*|| lies in [1/3,1], and |h_j|=3d0||u-u*||. Define a comparison law that equals the analytic Gaussian proxy when |h_j|<=8d0, and equals the ideal physical discrete-multiplier query outside that region.

The required local radial region ||u-u*||<=1+1/kappa lies strictly inside this patch. The required time-regularity region ||u||<=1+1/kappa also lies inside it, since ||u-u*||<=2+1/kappa<8/3. At u=0 the proxy is in force. Therefore the patched law meets the accessible OHCP requirements while differing from the physical law by a uniform pointwise TV bound. The patch can be discontinuous on its remote boundary; no continuity of that patch is needed if one first compares exact-real patched and physical executions, then compares exact-real and finite physical executions.

For the latter comparison, a global physical spatial Lipschitz bound is available. A Gaussian moment argument gives E||V^-1 r||^2<=n: use the ratio rho_(R,sqrt(2)V)(0)/rho_(R,V)(0), the theta bounds, and Jensen. Consequently E|r_j|<=v_j sqrt(n). Coupling the same r in two queries and using Gaussian translation TV bounds gives a k-sample normalized-spatial Lipschitz bound at most

    3 k d0 sqrt(2n) v0 exp(t)/w <= (3/32) exp(t).

Thus exp(M)-scale amplification is the issue a finite coordinate quantizer must pay for. This is genuinely global in the query position.

The adaptive probability argument must use the filtration consisting of all previous random bits, generated samples, oracle answers, numerical failures, and the current sample counter. Conditional on an equal coupled history, the next query is the same and the next pointwise TV estimate applies. A sequential coupling/union bound then pays the sum of these conditional bounds. It requires fresh sampling/oracle randomness on every call, and no multiplication of merely marginal success bounds.

The frozen fixed error budget checks arithmetically:

    2kQ_* epsilon0/(1-epsilon0)
       <= zeta/[32(1-1/16)] = zeta/30 < zeta/16.

The numerical budget over a counter starting at zero satisfies

    sum_(j>=0) zeta/[16(j+1)^2]
       = zeta pi^2/96 < zeta/8.

The additional declared walk-rounding loss zeta/16 leaves substantial room inside the overall zeta. These sums are valid under arbitrary adaptive scheduling if the numerical bounds really hold conditionally for each generated sample. The counter alone does not establish the sampler bounds.

The generic cached-prefix regression does not support any contrary product argument: its 0.0105 joint event exceeds 0.1^2 because conditioning changes support. This audit uses pointwise conditional TV and additive coupling, not that invalid product inference.

## 7. What is and is not checked about the explicit finite schedule

The parameter dependency order is acyclic: h0=v0d0 is independent of v0, so Q_* can precede epsilon0 and v0. Input bit lengths and certified evaluation costs are explicitly included, avoiding a magnitude-only complexity claim. All displayed counts are polynomial functions of kappa (with d_H=2 fixed).

The grid identity is exact:

    G Delta=M.

One comparison, if it consists of exactly two profiles on G+1 points with N calls each, uses 2(G+1)N calls. Running T_walk+1 such comparisons in each of n/2 pairs and both orientations gives exactly the displayed Q_*. This count is conditional on that being the actual walk structure; it does not supply an absent initialization, termination, scoring, or output algorithm.

The empirical sample count is ample for a useful accuracy target. For eta=1/(20 Lambda_cmp M), conditional Hoeffding gives per-mean error probability at most

    2 exp[-50(C+ceil(log2(8(G+1))))].

A union over both profiles and all G+1 points is far below exp(-C). Weighted maxima with weights bounded by M inherit O(1/Lambda_cmp) sampling error. A linear-weighted C-Lipschitz profile also has grid error O(C M Delta). These observations support the size of N and Delta, but do not identify the actual weights or prove the proposed comparison's geometric soundness/completeness.

The following obligations remain open:

1. Specify the weighted profile score, baseline treatment, endpoint truncation, and exact threshold rule. Prove comparison behavior in all radius regimes, including a query extremely close to the hidden center and nonmonotone acceptance profiles.
2. Specify the random-step law, initialization, acceptance/update rule, treatment of failed comparisons, and final output rule. Prove the drift and confinement/progress invariant giving failure at most exp(-kappa) within T_walk+1 steps. The large displayed polynomial is not itself that proof.
3. Match Lambda_walk, C, Lambda_cmp, M and the threshold 4/Lambda_cmp to the actual primary proof or supply a complete independent finite derivation. The inaccessible PRS pages cannot be replaced by BRST's asymptotic polynomial statement.
4. Specify what “B random bits” means for a multidimensional step. A B-bit scalar grid and a total-B-bit two-dimensional grid have different spatial resolutions. A generic B-bit vector encoding does not imply coordinate error 2^-B. Give the actual quantizer, its coupling, and the path-error recurrence.
5. Verify the resulting recurrence against the displayed B and the global exp(M) Lipschitz factor. If each scalar/coordinate has O(2^-B) coupled error and the accumulated path error is O((T_walk+2)2^-B), the displayed B has considerable slack. Those hypotheses have not been supplied or derived for the actual walk.
6. Give the bounded Gaussian/CDF/integer-rejection samplers and their internal error allocation, including grid-boundary errors, mean and embedding precision, and the rejection fallback. Efficient polynomial-bit construction is plausible, but a promise that “the proof specifies” it is not an available specification in the frozen input.

Wrong-sign runs can indeed be harmless once these finite bounds are unconditional: correctness of their oracle need not hold, but all loops, numerical precision, and stopping/fallback costs must still obey the cap. I have not inferred those unconditional implementation properties merely from a high-probability correctness proof for the right sign.

## 8. Exact hand counterexample to a physical Haar endpoint

Take

    n=2, R=Z[i], J=R, D=1, q=2, P=1,
    k=1, w=1, delta=1/4, zeta=1/8, kappa=64.

Then h0=1/256, a0=1/1024, S=log(1024), and all kappa lower bounds hold. In particular 4S+8+4log(2)+20<64 and 3exp(-64)<1/4. Compute epsilon0 and the integer a exactly as in the frozen statement, then set

    m=1024a+1, v0=m/256, d0=1/m.

Here m is 1 modulo 4, v0>=2sqrt(2)a, and the strict BDD radius condition holds. Take T=lambda=e=0, and query z=0. The multiplier displacement is the real scalar h=2/m.

Let A accept when the first rounded coefficient is even. Uniform F has acceptance 1/2. A coefficient X of G_w has density sqrt(2)exp(-2pi x^2), and

    Pr[|X|>=1/2] <= (sqrt(2)/pi)exp(-pi/2) < 1/4.

Thus GP acceptance exceeds 3/4 and A has advantage greater than delta. This is a legitimate instance of the theorem's assumption.

For the unrounded physical query, choose the nonzero dual character chi=m/4 in L*=R/4. For every r in R,

    <chi,(2/m)r> = Re(r) in Z.

Therefore the Fourier coefficient of (2/m)r+G_w modulo L at chi is exp(-pi m^2/8)>0 for every t. Haar's coefficient there is zero. The physical law does not tend to Haar.

The finite rounded limit is also nonuniform. As t tends to infinity, the first multiplier coefficient modulo m tends to uniform. The period-two parity function f(x)=(-1)^round(x) has the usual odd cosine expansion. Averaging over the m shifts 2r/m kills all frequencies except odd multiples of m. Because m is 1 modulo 4, the limiting parity expectation is

    (4/(pi m)) sum_(s>=0)
        (-1)^s exp[-pi m^2(2s+1)^2/8]/(2s+1).

The alternating terms strictly decrease in magnitude, so this expression is strictly positive. Hence the exact finite endpoint has a biased first-coordinate parity and is not U. Gaussian convolution makes the displayed Fourier computation absolutely convergent.

The bias can be much smaller than epsilon0. Thus the counterexample is fully consistent with uniform physical-to-proxy TV approximation. The appropriate clarification is to put the exact Haar limit on the analytic continuous proxy and retain approximation/coupling for the physical oracle. This clarification is not a new proof of B6 or B7.

## 9. Exact recovery, validation, orientations, and imported scope

If a coordinate walk returns z within 3exp(-kappa) of z*, then its recovered e_j has error at most 3d0exp(-kappa). Inverse canonical transformation does not enlarge the infinity error into coefficient coordinates. Since d0<w and the imposed condition gives 3w exp(-kappa)<q/(8D), these approximations leave a strict margin for rounding each coefficient of T-e to (q/D)Z. An additional numerical coefficient error below q/(8D) still leaves total error below q/(4D), safely below the half-grid threshold. Exact lattice membership then uses rational linear algebra on the supplied basis.

For arbitrary efficiently computable scalars, one should not demand an exact decision at the equality ||T-lambda||_infinity=d0. A certified relaxed threshold 2d0 suffices. The true candidate has distance at most d0; every other lattice point has distance greater than 3d0 by the norm lower bound and d0<q/(4D^(1/n)). Thus a finite certified comparison has a strict margin on every actual lattice candidate. This implements the stated “certified distance” verification without an undecidable equality test.

The correct global orientation yields every pair with probability at least 1-(n/2)exp(-kappa), before the separately budgeted implementation errors. The two full reconstructions produce at most two candidates. The relaxed verification rejects any wrong lattice candidate. No sign-calibration calls are needed. The resulting success probability is the displayed one if B6 and B7 are proved.

The finite GP bridge and fractional-composition assertions refer to separate work and were not available under this assignment. They are not inputs to the checked analytic BDD reduction. The quantum width scaling is algebraically compatible with L*=conjugate(J)/(nq), but no coherent BDD implementation, quantum state/gate precision, or quantum sampling theorem is certified here. The restricted-family-to-arbitrary-ideal edge remains open exactly as the frozen statement warns.

## 10. Required next evidence and terminal status

The minimal remaining evidence is the complete finite comparison/walk algorithm with its proof, using the displayed parameters, plus the finite quantizer/sampler specification and coupling recurrence. A fresh check should also enforce the explicit proxy/physical endpoint distinction and rerun the exact n=2 regression above.

This report ends with the standalone theorem **BLOCKED / NOT CERTIFIED**, supported analytic subclaims as recorded, and the literal physical endpoint rejected. It is a completed blind report, not a request to inherit certification from another reviewer. No substantive conclusion was sent to the coordinator before the complete report was hashed and its freeze receipt written.
