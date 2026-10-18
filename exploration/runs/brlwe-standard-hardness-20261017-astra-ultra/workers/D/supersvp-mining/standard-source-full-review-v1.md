# Standard-input decomposition and canonical composition review

D; tool clock 2026-10-17T21:42:34Z before this freeze. PROVISIONAL NONBLIND full-proof review; no acceptance authority. No new experiment. Exact inputs:

- standard-rlwe-decomposed-theorem-v1.md: b82435a83a5b4babc6289f351864d49adfd9d18adbdad6469b91596aff24fe32.
- standard-rlwe-decomposed-proof-v1.md: 4d7c0d537eaa95a982454d91eb349073243bf0cede4a67ea5568ed7a4cc19318.
- standard-canonical-composition-v1.md: 172968cf199aae648d3bcfb19377b2eb06158ce4406a0158eddba5c5276007e4.
- repaired standard-canonical-composition-v2.md: 9a168be29fd5fbf020b253980ace92aac178105d8f7f8bc4b98883713a4ed860.

Disposition: the standard-to-decomposed v1 theorem/proof survives. The standalone canonical v1 target law has the preserved unreachable-key definition defect; v2 repairs precisely that defect, and the complete v2 composition survives this review. This is a new uniform-secret canonical-hint source edge. It does not provide a binary-secret conversion or the low-index fractional-source foundation. Recommendation remains subject to independent reconciliation and review of its declared primary sampling dependencies.

## 1. Full source law and rank probability

The ordinary input has M=L²g uniform ring multipliers with one shared secret of the specified law and the same independent error tuple. Comparator responses are independent uniform given the entire multiplier array. The simulator samples the FULL h by Lg coefficient-Gaussian matrix R independently of that input. Its rank event depends only on R. For every CRT root, each row dot a fixed nonzero vector has maximum atom at most mu: condition on all but one contributing ring entry, then all but that entry's constant coefficient. Gaussian reduction has maximum atom at zero, and the integral/Poisson bound gives mu<=1/sigma_R+1/q. Rows are independent; no independence of CRT coordinates is presumed. Union over all nonzero vectors and all roots yields rho<=n(q^(Lg)-1)mu^h.

On full rank, w->wR is surjective onto Rq^(Lg), every affine fiber has size q^(n(h-Lg)), and sampling uniform source A_i followed by uniform fiber W_i gives each W_i probability q^-nh. This proves the full retained joint law (R,W,A), not only individual blocks. It also proves W_i are independent conditional on R exactly as in the decomposed target. Keeping b verbatim preserves the full planted joint law with S,e and the exact conditional uniform comparator. No failed row or pivot sample is reused.

Replacing a bad-rank branch by a common failure symbol costs at most rho separately at each endpoint. A strict finite implementation error delta_impl is also per endpoint. Hence the standard-to-decomposed advantage loss is 2rho+2delta_impl. One rank attempt suffices; no rare conditioning is hidden in runtime. Fq linear algebra on the coefficient expansion implements the map without factoring the cyclotomic polynomial. The source degree, modulus, secret distribution, noise and M samples are all unchanged.

The author's exact fiber control was read: n=2,q=5,L=2,g=1,h=3; 15,625 W states, 625 image states with equal fibers25; pointwise planted response and comparator checks. It separately falsifies blockwise rank (each block surjective while the joint image has25 rather than625 states) and single-CRT-root rank. This supports the full-rank obligation but is not a proof of the asymptotic Gaussian failure bound.

## 2. Triangular transport, correlations and canonical hints

The supplied triangular-endpoints and ring-extraction packets were reread. S=[[I,X],[0,I]] is integer unimodular for every X. Thus bS preserves uniform response exactly conditional on all local coins; adding independent f does too. The secret remains the original rank-one ring secret, with no dimension expansion or module-secret replacement.

The trapdoor identity is exact: (I_L tensor Astar) times the stacked Q_i, minus W R, equals I_L tensor G because Astar Q=Adec. The coefficient expansion of the transported trapdoor has entry bound max(1,B). Its dimensions are nL equations and n(LM+h) variables. Since M=L²g,h>=2g,g>=ceil(log2q), L³+2>=3L proves the primary sampler's variable-dimension floor. Column permutation identifies the coefficient gadget with the standard gadget, and zero padding is legitimate. The canonical law samples Lg ring columns, not their n coefficient rotations independently.

The primary SamplePre scope was independently checked in the earlier ideal-ring-sis review: [WWW25 author full version](https://www.cs.utexas.edu/~dwu4/papers/MultiPreimage.pdf), Theorem3.9, supplied-paper Lemma3.6. It applies to every supplied valid gadget trapdoor, uses maximum-entry norm, and supplies the stated width/error. This is a sampling theorem, not a random-matrix hardness theorem. Retained INTEGER Gaussian hints are required; arbitrary mod-q representatives would not establish the declared law. Numerical sampler accuracy remains a separately charged implementation term.

The extraction argument retains W but discards R and X. The exact averaged CRT chi-square expression accounts for all zero-divisor supports; a general-matrix two-universal hash assertion would be false. First replace W1R1 columns while retaining W1, then use the ACTUAL conditional R1 posterior to reconstruct the other blocks. This posterior depends on W,A0 but not fresh X. Consequently the second hash hybrid may replace A0X by uniform while preserving those reconstructed correlations. An arbitrary transported hint could reveal discarded R; instead the canonical hint is a common kernel of the final A,W. The extraction cost is therefore exactly the displayed delta_ext, plus the separately charged hint sampler and tail costs.

## 3. Noise law and both endpoint budgets

Conditional on X, eS is EXACTLY D_(Z^N,C) for C=tau² S_c^T S_c, because S_c is unimodular. Set F=tau_out²I-C. The norm bound B_S gives F>=3C under tau_out>=2tau B_S. The convolution posterior P=(C^-1+F^-1)^-1 is therefore >=C/2. Poisson smoothing of C/2 follows from the unimodular change S_c Z^N=Z^N, rather than an incorrect claim that the smallest eigenvalue of C is tau². This distinction is necessary for the sheared noise.

The convolution is the desired spherical D_tau_out reweighted by rho_P(Z^N-m_z) divided by its ACTUAL expectation under that target law. Uniform translate bounds give TV<=epsilon/(1-epsilon); numerical F sampling adds delta_F. This full-joint comparison is uniform in retained X,R and independent of S. Replacing the noise and then appending canonical hints is valid. No covariance-only identification or missing theta normalizer occurs.

The comparator response is exact conditional uniform for the actual public tuple, even when f is approximate. The COMPLETE comparator endpoint is nevertheless only close to the independent uniform-key canonical endpoint. Its charges are rho+2alpha_R+delta_ext+delta_hint+delta_impl. The planted endpoint adds delta_noise, as stated. Tail/rank events are paid additively and do not justify retaining a Gaussian product law after conditioning. The two endpoint budgets give the displayed advantage loss; they are not multiplied by an unrelated adaptive query count. This simulator makes one final distinguisher call using M input responses.

## 4. Exact v1 defect and v2 recheck

The v1 FINAL public law samples unconditional uniform A,W, then a Gaussian conditioned on all gadget equations. At A=W=0, a positive-probability key, the gadget's target1 has no preimage. That conditional Gaussian is undefined. The earlier triangular packet's failure convention does not make a standalone exact law sufficiently explicit. The defect is frozen in standard-composition-v1-definition-objection.md SHAb9b1d4c79730598c6d6617a3090b702a2b1ec5ddd4bae201c087ceb9df65a15f.

The v2 diff was inspected in full. Its sole mathematical addition declares T=FAIL on every unreachable key while retaining A,W and the specified response b; otherwise it uses the canonical column law. A,W are not rank-conditioned. The same kernel is used at both endpoints. Actual transported non-abort keys have the displayed gadget trapdoor, so applying this extended kernel to the public extraction hybrid pays the exceptional-key mass already within delta_ext. There is no extra loss and no hidden conditioning. The exact v1 remains defective; v2 repairs this issue with unchanged bounds.

## 5. Published continuous source and discretization

Independently retrieved primary [LPR Toolkit](https://sites.cc.gatech.edu/fac/cpeikert/pubs/toolkit.pdf), Theorem2.22 and Lemma2.23, including the indexed complete theorem statement. The source theorem has a polynomial-value split prime, alpha q growing faster than sqrt(log n), M-sample spherical canonical width alpha q(nM/log(nM))^(1/4), and a quantum worst-case ideal-SVP/SIVP reduction. Lemma2.23 supplies equivariant discretization with the same sample count. These are the imported primary facts; no claim of a stronger small-secret theorem is made.

In the power-two ring R^vee=(1/n)R. Multiplying the dual response and secret by n maps the quotient to qR and the uniform secret to uniform Rq. The canonical Gaussian width is multiplied by n, and the canonical/coefficient scale sqrt(n) then gives coefficient width tau0=sqrt(n)r_can, exactly as stated. Ordinary coefficient spherical errors and the same rank-one secret result.

For randomized integer rounding at width r, conditional probability is rho_r(k-x)/rho_r(Z^N-x). Its dependence on x cannot be omitted. Completing the joint continuous Gaussian product gives a D_tau kernel, tau²=tau0²+r², reweighted by the conditional expectation of the inverse rounding normalizer. Poisson bounds its numerator factor in [(1+epsilon0)^-1,(1-epsilon0)^-1]; division by its actual expectation gives TV<=epsilon0/(1-epsilon0). Thus only the planted ideal endpoint receives this error. Equivariance and equal torus cell masses make the comparator EXACT uniform before finite numerical approximation. Discrete outputs are never compared directly in raw TV to a continuous input.

The primary source theorem is continuous and therefore relies on its declared finite-precision model. The new rounding needs only polynomial precision with charged kernel errors; it does not gain access to exact uncomputable real challenge values. Full scalar encoding lengths remain counted.

## 6. Polynomial intersection and remaining restrictions

For fixed b, q can be chosen in the progression1 modulo2n^(2b+8), with polynomial value and q>=n^(2b+8). The least-prime polynomial bound is the only number-theoretic input; an independently checked primary reference is [Xylouris, On Linnik's constant](https://arxiv.org/abs/0906.2749). Sequential primality testing up to that fixed polynomial bound is polynomial in n. No optimized Linnik exponent is required or claimed.

Then g=Theta(n), h=O(n^(b+1)log n), M=Theta(n^(2b+1)), B=O(sqrt n), tau=Theta(n^(b+3)). The displayed r smooths Z^N by the direct dual-theta bound. For sufficiently large n, tau<=2tau0 and B_S<=1+nLg, hence the chosen tau_out meets the required bound. Gaussian coefficient tail, rank and both extraction expressions are exponentially small. The hint sampler width is O(n^(3b+5/2)polylog n), including the b=0 extra h logarithm, and tau_out=O(n^(2b+5)). Thus q/tau_out=Omega(n³).

The source alpha obeys alpha q=n^(b/2+2) times a fixed logarithmic factor. Its primary floor and polynomial ideal approximation factor both hold. This is a nonempty asymptotic parameter regime; it does not claim every finite n satisfies the displayed inequalities. Scalar Gaussian, fiber and canonical samplers require their declared bounded finite implementations and accuracy charges, not merely a generic expected-runtime assertion. The cited sampler contracts plus the existing bounded scalar wrappers support those bounds within the full-encoding model.

The result supplies a valid standard uniform-secret hardness edge to the NEW canonical hinted law after the v2 definition repair. It preserves the source secret exactly and therefore cannot turn a binary recovery oracle into a uniform-secret oracle. It does not remove the augmented W term, manufacture a short joint quotient preimage, or make the bounded-index ideal family standard-hard. Those gates remain OPEN; this positive auxiliary edge is not completion of the original foundation goal.
