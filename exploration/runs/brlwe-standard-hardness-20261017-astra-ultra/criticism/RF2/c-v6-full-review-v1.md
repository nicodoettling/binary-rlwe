# RF2 exact C-OHCP-v6 review

Reviewer D; 2026-10-17T21:40Z. NONBLIND full-proof adversarial review. PROVISIONAL recommendation, no acceptance authority. No new experiment run. Frozen inputs:

- theorem-v6.md SHA256 `9e26263bd8e59c8ab1cbd716d7d7ccc946624f80b1cac8a0027eabb0ee2dfa67`.
- proof-v6.md SHA256 `9c57cf10adf32b88a931ebf0cccec0a7705502f78640b71d1743e05954e29b76`.

These exact bytes were reread and hashed. The old generic finite-OHCP runtime contract is NOT imported. The explicit v6 algorithm and its polynomial counts survive this review, with the causal martingale proof clarification in section 4 below. That clarification supplies an explicit rigorous interpretation of the proof's high-probability-correctness wording; conditioning on future success literally would be invalid. It changes no algorithm or parameter. Recommend the finite gate for independent reconciliation/fresh review, scoped to the stated pointwise periodic-Gaussian-to-BDD reduction. Standard ideal-family hardness, binary secret conversion, and quantum implementation are not established by this result.

## 1. Primary source and exact endpoints

Independently inspected indexed primary text from the June 4, 2020 author PDF of Peikert--Regev--Stephens-Davidowitz, [Pseudorandomness of Ring-LWE for Any Ring and Modulus](https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf), printed pages 12--16. Direct PDF retrieval failed; indexed primary passages supplied the actual algorithms. Navigation queries with the full title and `h(s)`, `100λtmax`, `subprocedure YES`, and `10T λ` exposed respectively the weighted maximum, grid comparison, guided walk, and progress proof. Page 15 supplies the rare-near-center estimate and progress interval; page 16 supplies the martingale count. The larger v6 walk constant is checked independently below and is not attributed to the paper. The primary descriptions motivate the algorithm; the finite proof here does not rely on an unspecified real-oracle machine model.

The exact source is k independent coefficient-grid roundings of canonical G_w modulo L=qJ^-1, with public fixed J, versus iid uniform on F=(DP)^-1 Z^n/L. The quotient size is q^n D^(n-1)P^n. HNF/SNF and the grid preserve that same metadata. Haar followed by this rounding is exactly uniform: L is contained in the grid and all grid cells in the torus have equal measure. A's gap is pointwise for the same J. Average-over-J advantage gives only an appropriately qualified good-ideal statement.

For every integral multiplier r, r lambda lies in L; exact cancellation precedes any continuous comparison. Zero and nonunit multipliers are included. Every sample uses fresh multiplier and Gaussian coins conditional on the current query and full prior history. The actual oracle never knows e. Its piecewise analytic comparison may depend on e because it is only a proof kernel. Neither latent multipliers nor Gaussian tape are appended to public samples.

## 2. Analytic kernel, both normalizers, and center

Completing the full n-dimensional quadratic form gives P=(V^-1+M_h^T M_h/w²)^-1 and C=w²I+M_h V M_h^T. The exact density ratio has the posterior theta factor divided by the original theta factor. Both lie in [1-epsilon0,1+epsilon0] under the displayed smoothing bound, uniformly in the translate and selected width. Thus the posterior comparison costs epsilon0/(1-epsilon0) per sample; generating the approximate discrete multiplier costs the other such term. No omitted reverse-sampling normalizer is reintroduced.

The shift z*=2+e_j/d0 puts its norm in [1,3], including zero coordinates. Scale 3 and residual guard 8d0 cover both the centered radial ball and the origin-centered ball. The starting profile is p_*(t)=p(t+log|z*|), with nonnegative shift. Its gap at zero is at least 15delta/16 after the common orientation choice. The sign is the same for all coordinates because every starting law is delta/16-close to the same spherical benchmark. No sign-calibration calls occur.

The selected complex plane tends to full Haar, not merely a subtorus: every nonzero ideal-dual field element has nonzero selected embedding. Algebraic norm bounds the full scaled dual theta series. The earlier independent packing control remains applicable; a single-character bound would not suffice. Fixed nuisance widths are retained in the radial profile. Its Lipschitz constant 2k and decay bound satisfy the enlarged K hypotheses. All these are full-joint Gaussian comparisons before the common rounding kernel.

## 3. Explicit OCP comparison

Use the theorem's K, C, Lambda_cmp, M, Delta, G, N. Normalize the center by 3. On a legal walk history its norm lies in [1/3,1], current radius does not exceed the initial radius, and current/trial radii above exp(-Lambda_walk) give shifts in [-C,C]. The first shift is nonpositive, so the starting excursion survives on its suffix. The target improvement 1/C is smaller than 1/Lambda_walk and therefore suffices for the walk.

For H(s)=sup_(u>=0)(1+u)|p_*(s+u)-p_infinity|, increasing s cannot increase H. In the YES case, translate a maximizing point for the later suffix to the earlier one. An excursion gives H>=1/C. The decay bounds a relevant maximizing location by 100C log C, yielding gap >1/[C²(1+100C log C)] >=1/(101C^4). This argument does not assume unimodality or a single positive peak.

Set b=1/(100 Lambda_cmp M). Exactly N b²=C+ceil(log2(8(G+1))). Hoeffding over both suffixes and G+1 grid points gives failure at most 4(G+1)exp(-2Nb²)<=exp(-C)/2. The endpoint bias is at most 2exp(1-M/C)<=b and C Delta=b. Grid interpolation and the terminal estimate therefore contribute at most 4b(1+M)+Delta<1/(5 Lambda_cmp). The omitted tail contributes <1/(10 Lambda_cmp). The coarser claimed total 1/Lambda_cmp is valid. A NO difference is <=2/Lambda_cmp and a YES difference is >=(10000/101-2)/Lambda_cmp; the exact rational threshold 4/Lambda_cmp separates them. The call bound 2(G+1)N and maximum logscale M are exact, including all endpoint estimates.

The author control report SHA256 `04078318ccee7d0473be21f31f5dff4752ea528ad191055be28f948d6f77c3cf` was read. Its 60 exact signed multi-peak/grid controls and 343 adaptive two-bit controls are useful finite falsification attempts. They do not certify concentration, the complete walk, or runtime; those obligations are analytic here.

## 4. Causal walk proof; no conditioning on future correctness

The primary and v6 wording about being on the correctness event must not be read as conditioning fresh walk coins on future successes. The following reference process makes the argument rigorous.

At each step sample the fresh coordinate, sign, X and empirical-oracle bits as specified. Define a proof-only corrected-decision walk which overrides an empirical decision only when it contradicts the promised geometric rule: force NO for nondecreasing radius, and force YES for log-radius decrease at least 1/C. In the intervening region retain the empirical decision. This is a causal process; its transition uses only its present state and current fresh coins. It is not an implementable oracle requiring the unknown center. Its radii never increase.

When the radius r exceeds exp(-K), choose a coordinate with |y_j|>=r/sqrt(d), d=2, then the sign pointing toward the center and X in

    [-log|y_j|/(2K), -log(|y_j|/2)/(2K)].

The interval lies in [0,1], since K is large and r>exp(-K). Its conditional probability, including coordinate and sign, is log(2)/(4Kd)>=1/(10Kd). The step length lies between |y_j|/(2Ksqrt(d)) and |y_j|/(Ksqrt(d)). Consequently the squared radius drops by at least r²/(2Kd^(3/2)), so the log radius drops by at least 1/(4Kd^(3/2)). This exceeds 1/C and is forced accepted by the reference process. Once the target radius has been reached, count every later indicator as a success. Thus every indicator has conditional expectation at least p=1/(10Kd), without any future conditioning.

Azuma applied to the bounded martingale differences gives at least Tp-10sqrt(KT) counted successes except with probability at most exp(-50K), which is below exp(-K)/2. With T=10^6 K³d^4, the displayed lower bound equals

    10000 K²d²(10d-1) > 10K²d^(3/2).

If the target had never been reached, this many actual progress steps would decrease log radius by more than K (indeed by more than 2.5K), a contradiction. The reference walk therefore reaches and retains radius <=exp(-K) with the stated slack. Using T+1 rather than T steps only helps.

Couple the actual ideal walk to the corrected one until the first bad event. Before such an event, current radius is at least exp(-Lambda_walk), at most 1, and trial radius at most 1+1/K. A trial within exp(-Lambda_walk) of the center is declared bad regardless of its empirical acceptance. Conditional on any prior legal history its probability is at most exp(-Lambda_walk/2): if the current radius is <=10exp(-Lambda_walk/2), the minimum step exp(-2K)/(Ksqrt(d)) is too long to enter that tiny ball; otherwise the allowed log-uniform interval has probability at most

    exp(-Lambda_walk) / [K(r-exp(-Lambda_walk))]
      <= exp(-Lambda_walk/2).

This is the actual primary page-15 argument. The inequalities hold because Lambda_walk=10Kd²ceil(log2(2T)) is much larger than K and log K. On every other trial the OCP hypotheses apply, and an incorrect promised decision has conditional probability <=exp(-C). Union over T+1 trials is bounded by the proof's conservative 10(T+1)exp(-Lambda_walk/2)<exp(-K)/2. Until the first bad event the actual and corrected processes coincide. Therefore the actual real walk fails with probability at most exp(-K), with no multiplication of marginal probabilities and no conditioning on all future comparisons succeeding.

This closes the precise martingale obligation while preserving the v6 algorithm and constants. A literal future-conditioned proof would be rejected; this causal proof is the supplied reconciliation.

## 5. Finite walk and adaptive transcript

The physical discrete-multiplier kernel is globally Lipschitz in the guess, including outside the analytic guard. In coefficient coordinates its width-square is <=(v_max²/n)I. The translated theta bound gives the stated MGF inequality and hence E||sigma(r)||²<=2n v_max². Gaussian translation and k products give Lipschitz constant <=4k sqrt(n) v0 exp(t)d0/w <=exp(M). This bound concerns the physical kernel; no continuity is asserted at the analytic patch boundary.

Couple ideal X with the dyadic midpoint in its B-bit cell. The step derivative is <=2 and the finite exponential error is <=2^-B, so each step changes by <=3*2^-B. Until oracle bits first differ, every exact rational branch agrees. Position discrepancy at any query, restoring scale 3 and the trial step, is <=9(T+2)2^-B. At each adaptive query compare: analytic kernel at ideal position; physical kernel there; physical kernel at finite position; finite sampler. The first term is uniformly bounded even outside the guard (zero there), the second uses the global physical Lipschitz bound, and the last is a conditional numerical error. Their sums are valid by sequential coupling.

The position term Q_* exp(M)9(T+2)2^-B is <zeta/16. The chosen 2M term is sufficient because 2 log 2>1. The final deterministic position error is <exp(-kappa)/4, while 3exp(-K) is much smaller than exp(-kappa). Rational logscales i Delta need no perturbation. Every position and empirical maximum has polynomial bit length, even in the wrong orientation.

Q_H=2(T+1)(G+1)N and Q_*=nQ_H account for both global orientations and n/2 coordinate pairs. No success guarantee is required of the wrong orientation to establish these bounds. epsilon0 is chosen after this count, so 2kQ_*epsilon0/(1-epsilon0)<zeta/16. Since h0=v0d0 is fixed beforehand, S and kappa do not depend circularly on Q_* or v0. A previously established fixed distinguisher residual gap enters delta once; it is not charged at every query. Query simulation error is charged at every query.

## 6. Scalar implementation, recovery, and remaining scope

Every scalar rejection loop has a deterministic cap, including uniform-integer proposals. A global sample counter assigns tau_j=zeta/[16(j+1)²], and all bounds hold conditional on the entire preceding transcript. The multiplier approximation, capped uniform rejection, finite mean, Gaussian tails and CDF boundary errors sum to <tau_j. Their sum is <zeta/16; fixed normalizers and finite walk perturbations fit the stated zeta with slack. Actual multiplier coefficients are always integers. All Gaussian comparisons precede rounding; no discrete-versus-continuous raw TV assertion is made.

Potential exact-ceiling ambiguity is covered by the theorem's permission for conservative certified rounding; integer logarithm loop counts are exact. The previously reviewed Hermite-integral separation for B's scalar natural-log ceiling applies when its exact convention is used. No algorithm requires deciding equality to an arbitrary computable-real threshold. Certified scalar evaluation costs and all numerator/denominator input lengths are explicitly charged, not merely log magnitudes. The matrix square root has a positive gap Vcoef-a²I>=3a²I, so no singular square-root precision problem arises. Each sampler output and rejected proposal has bounded bit length under these caps.

The true lambda lies in (q/D)R. The theorem's stronger rounding condition 3w exp(-kappa)<q/(8D), with d0<w, leaves ample room for finite center error. Exact membership and certified residual upper bounds accept the true candidate and reject every other candidate: nonzero lattice differences have infinity norm >4d0, hence false residual >3d0. At most two complete candidates are tested. All coordinates are recovered under one common correct orientation.

Disposition: the explicit finite-primary gate survives, subject to the causal proof completion above and normal independent reconciliation. The mathematical output is pointwise BDD for the same J and same finite periodic Gaussian premise. It neither normalizes arbitrary ideal classes into bounded-index ideals nor converts a uniform ring secret to binary. A/B composition, actual coherent quantum implementation, and standard worst-case-family inclusion keep their separate statuses. Failed attacks supply no security evidence.
