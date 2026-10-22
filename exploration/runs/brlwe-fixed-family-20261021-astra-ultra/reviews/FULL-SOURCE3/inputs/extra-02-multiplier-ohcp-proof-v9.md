# Finite multiplier OHCP full proof, v9 (theorem v8 and standalone algorithm v2)

PROVISIONAL; fresh exact-byte review required. Exact predecessor theorem7/spec1/proof8 was rejected only at the final nonrational-threshold specification C8-FV1. Its report is preserved before this repair. Version9 proves the explicitly rational final test of algorithm2; all analytic, sampler, walk and call-count arguments below are otherwise unchanged. This coherent version incorporates coordinator proof v7's causal corrected-decision reference walk (D's completion, exact-byte independently reviewed by A), supplies the complete finite sampler justification matching multiplier-ohcp-algorithm-v2.md, and fixes the exact-Haar endpoint to the CONTINUOUS PROXY only. Read theorem v8 and the definition-only companion first. BT7's exact counterexample and old v6 causal/standalone-specification gaps are preserved before repair. No old version inherits acceptance. All core parameters are unchanged; the companion fixes the formerly allowed conservative integer rounding. The literal log2(2T) notation is resolved to log2(2T_walk). No standard ideal-family hardness is asserted.

## 1. Exact cancellation and normalization

The ideal L=qJ^-1 is stable under R. Thus rT modulo L equals re whenever T=lambda+e and lambda in L. This is an exact identity for every r in R, including zero, nonunits, and negative coefficients. We do not replace r by a continuous multiplier before this cancellation.

Let V be the covariance-width operator of r: in real orthonormal coordinates it has eigenvalues v_i², repeated on each complex plane. Let M_h be multiplication by h=e-g(z). Its singular values are |h_i|. The unnormalized density of Y=M_h r+G_w is

    sum_(r in R) exp[-pi(r^T V^-1 r + ||y-M_h r||²/w²)].

Define

    P=(V^-1+M_h^T M_h/w²)^-1,
    m=P M_h^T y/w²,
    C=w² I+M_h V M_h^T.

Completing the square gives the exact normalized density ratio

    f_Y(y)/g_C(y)
      = [rho_P(R-m)/(det(P)^(1/2)/det(R))]
        /[rho_V(R)/(det(V)^(1/2)/det(R))].

Here rho_P(x)=exp(-pi x^T P^-1 x), and g_C is the normalized continuous Gaussian of width matrix C^(1/2). This ratio includes BOTH the posterior and original discrete-Gaussian normalizers.

If min_i v_i>=2 eta_epsilon(R) and max_i|h_i|<=w/(2 eta_epsilon(R)), then

    P^-1 <= [1/(4 eta²)+1/(4 eta²)]I,
    P >= 2 eta² I.

Poisson summation therefore puts each bracket in [1-epsilon,1+epsilon], uniformly in m,y and every arbitrarily large v_j. The pointwise ratio is in [(1-epsilon)/(1+epsilon),(1+epsilon)/(1-epsilon)]. Hence TV(f_Y,g_C)<=epsilon/(1-epsilon). Reduction modulo L and any common observation kernel contract this distance. For k samples the loss is at most k epsilon/(1-epsilon). This posterior bound is uniform over all OHCP logscales; growing v_j does not invalidate it.

## 2. Shifted center, fixed nuisance coordinates, and radiality

Fix pair j, set z*=2+e_j/d0 in C, and use the selected guess g_j(z)=d0*(z-2), zero elsewhere. The shift2 is a known real displacement in the complex plane. The hidden center satisfies1<=|z*|<=3, including when e_j=0. Set the OHCP scale to3. The centered allowed neighborhood has |z-z*|<=3(1+1/kappa). The BRST origin-centered Lipschitz ball has |z|<=3(1+1/kappa), hence |z-z*|<=6+3/kappa<8. We certify |h_j|<=8d0, covering both formulations. Every other residual remains e_i, of magnitude at most d0.

All multipliers except pair j have width v0; pair j has width v0 exp(t). Because 8d0=8delta*w/(32nkv0)<=w/(2eta) and v0>=2eta, Section1's uniform posterior comparison applies for every permitted guess and t>=0. The ideal continuous query law has widths

    b_i=sqrt(w²+v0²|e_i|²), i outside pair j;
    b_j(s)=sqrt(w²+(v0*d0*exp(s))²),
    s=t+log|z-z*|.

The other unknown errors enter only through fixed b_i. Let p(s) be A's acceptance on k copies of this Gaussian modulo L. Acceptance is exactly p(t+log|z-z*|); circular Gaussian symmetry supplies this dependence for arbitrary A. At the starting guess0, the profile is p(0,t)=p(t+log|z*|), with the NONNEGATIVE shift0<=log|z*|<=log3. This is the normalization repaired from v1.

## 3. Nonnegligible excursion at a permitted starting scale

At starting guess z=0 and t=0, the selected residual has magnitude at most3d0, and all others at most d0. Thus every variance ratio to the spherical Gaussian is at most1+9a², where a=v0*d0/w=delta/(32nk). The k-sample Gaussian KL is at most81nk a^4/4, using u-log(1+u)<=u²/2. Pinsker gives TV<=9a² sqrt(nk/8)<delta/16. After choosing the sign of A,

    p(0,0)-p_infinity >=15delta/16.

This supplies BRST Lemma3.8's excursion at the permitted scale t*=0. Equivalently the unshifted profile has its excursion at s*=log|z*| in[0,log3]. No query at the unknown center is required.

## 4. One pair of the continuous proxy tends to full Haar

For power-two cyclotomics, R^vee=R/n up to a unit, and the Euclidean dual of L=qJ^-1 is conjugate(J)/(nq). In particular each nonzero dual element a has

    |N(a)| >= D/(nq)^n.

Applying diagonal widths, with every unselected width at least w and selected pair width W, yields product lower bound D*w^(n-2)*W²/(nq)^n. AM-GM gives dual minimum at least sqrt(n)*c, with

    c=[D*w^(n-2)*W²]^(1/n)/(nq).

For completeness, an elementary packing argument supplies the exact bound used here, without an inaccessible primary lemma. If the scaled dual minimum is lambda>=sqrt(n)c, the shell [m lambda,(m+1)lambda) contains at most(2m+3)^n points. Put A0=pi-1-log5>1/2. Since2m+3<=5^m and c>=1, pi c^2 m^2-log(2m+3)>=c^2+A0*m. Thus its nonzero theta mass is at most exp(-nc^2) times sum_(m>=1)exp(-n A0 m)<exp(-nc^2), because n>=2 and2A0>log2. The Fourier density expansion and integration give proxy-to-Haar TV at most exp(-nc^2)/2. This uses the entire theta sum, not one character or a spectral-mass assumption about A.

For the query above set h=v0*d0 and a0=D^(1/n)*w^(1-2/n)*h^(2/n)/(nq). Then c(s)>=a0 exp(2s/n). Define S=max(0,(n/2)log(1/a0)). For s>=S,

    |p(s)-p_infinity| <= (k/2) exp[-n exp(4(s-S)/n)].

Choose kappa>=4S+4n+4log(k+1)+20. For s<=kappa/2 the OHCP bound 2exp(-s/kappa)>=1 holds trivially. For s>kappa/2, s-S>=s/2 and the preceding double-exponential bound is at most 2exp(-s/kappa). Negative s also satisfies the trivial bound. Because p(0,t)=p(t+log|z*|) and log|z*|>=0, the same decreasing upper bound gives |p(0,t)-p_infinity|<=2exp(-t/kappa). Thus the continuous-proxy starting-guess decay required by BRST Lemma3.8 holds with polynomial kappa whenever input logarithms are polynomial.

This endpoint is exclusively a statement about the continuous Gaussian proxy. Nonvanishing of every selected embedding permits its continuous spreading to smooth the full torus, with the quantitative norm argument above. It is FALSE in general that increasing the discrete multiplier width makes the physical query exactly Haar, or its rounded law exactly uniform: BT7's preserved rational-displacement example has a persistent nonzero character. Section1 provides a uniformly small, fixed physical-to-proxy discrepancy, which is all the transcript coupling uses. It does not imply an exact physical limit. The theorem's premise remains the exact finite spherical GP law versus exact finite uniform, not an altered physical-limit benchmark.

## 5. Lipschitz bound and OHCP

The derivative of log b_j(s) is between zero and one. A two-dimensional Gaussian whose log width changes by ds has total-variation derivative at most2: differentiate its density and use E[2pi||X||²/b²]=2. Thus k independent samples give |p(s)-p(s')|<=2k|s-s'|. Modulo reduction, A, and any common observation kernel contract this bound.

With kappa also at least max(2k,2/delta,20log3), the excursion, decay and Lipschitz requirements of PRS17 Proposition4.4 hold in dimension two. The precise local-oracle extension below avoids assuming any confinement of actual query points. Section 7 charges the exact fixed analytic comparison error against the primary algorithm runtime bound.

## 6. Zero centers and exact reconstruction

The shifted center has norm in[1,3], so the OHCP lower-center promise exp(-kappa)*3<=|z*| holds as soon as kappa>=log3. No rational-input algebraic lower bound is used for this promise. The zero-error and individual zero-coordinate cases are covered by the same construction.

Run the two-dimensional OHCP procedure for each conjugate pair. It returns z_hat with |z_hat-z*|<=3exp(-kappa). Subtract the known shift2 and multiply by d0. The resulting canonical coordinate approximation to e has error at most3d0 exp(-kappa). The inverse canonical transform has operator norm1/sqrt(n), so each coefficient error is at most3d0 exp(-kappa).

Since D J^-1 is contained in R, lambda belongs to(q/D)R. Round the coefficient vector T-minus-estimated-e to that rational grid. This recovers lambda exactly if3d0 exp(-kappa)<q/(2D); choose kappa accordingly. Verify membership in L and the decoding promise. The uniqueness assumption d0<q/(4D^(1/n)) suffices because a nonzero element of L has canonical infinity norm at least q/D^(1/n). Rational coefficient input makes the final exact rounding/membership computation finite and explicit; no imaginary exact-real input model is being claimed.

## 7. Finite wrapper and complete adaptive error budget

### 7.0 No unproved query-confinement assumption

PRS Definition 4.3 requires radial acceptance only for ||z-z*||<=beta*d. Its Proposition 4.4 asks the abstract profile p to have the stated global one-dimensional properties, which Sections 3–5 verify. BRST's equivalent formulation additionally states a Lipschitz condition on the origin-centered ball; that ball is covered by the 8d0 guard.

Define an ANALYTIC comparison oracle as follows. When |h_j|<=8d0 use the continuous Gaussian output law from Section 2. Else use the exact discrete-multiplier query law. This comparison oracle obeys the required radial law throughout the promised centered neighborhood and satisfies the origin-ball Lipschitz condition. Outside that neighborhood no radial law is required by PRS Definition 4.3. The abstract radial profile is defined by the continuous Gaussian formula for all real s, so its decay and Lipschitz properties are unchanged. On the guarded region the uniform posterior TV bound applies; outside it the exact discrete and comparison kernels agree. Hence the error bound is uniform at EVERY query, even if the primary algorithm probes outside either ball. The piecewise comparison is an analysis object, not a proposed algorithm using the unknown e. It does not require an unverified bound on query positions.

### 7.1 Explicit finite comparison and walk bounds

The primary source actually inspected is PRS's June4,2020 author version, pages12–16, retrieved as indexed primary text at its author PDF URL. Page12 gives the weighted empirical-maximum comparison algorithm, page13 proves its accuracy, page14 specifies every guided-walk operation, and pages15–16 analyze progress. Direct PDF access failed; the source-access distinction is retained. We now give conservative rational parameters and prove the needed bounds; we do not infer a generic finite oracle representation contract from the words polynomial time.

Write K=kappa+200, d_H=2, T_walk=10^6 K^3 d_H^4, and Lambda_walk=10K d_H^2 ceil(log2(2T_walk)). Set C=K+Lambda_walk. The OCP instance has shifts in[-C,C], C-Lipschitz profile, excursion at least1/C after its first shift, and decay2exp(-t/C), by the exact shift argument in PRS page14. It is enough to distinguish shift2<=shift1-1/C from shift2>shift1. This is stronger than the needed improvement1/Lambda_walk because C>Lambda_walk.

For one suffix define H(s)=max_(u>=0)(1+u)|p(s+u)-p_infinity|. H is nonincreasing. In the YES case, PRS's maximizer argument gives H(s2)-H(s1)>1/[C^2(1+100C log C)]>=1/(101C^4). The last inequality uses C>=200 and log C<=C. An excursion after s1 guarantees H(s1)>=1/C; decay confines its relevant maximizing location below100C log C. These are analysis facts, never algorithmic branches.

Choose

    Lambda_cmp=10000 C^4,
    M=100 C ceil(log2(C Lambda_cmp)),
    Delta=1/(100 C Lambda_cmp M),
    G=M/Delta=100 C Lambda_cmp M^2,
    N=10000 Lambda_cmp^2 M^2 [C+ceil(log2(8(G+1)))].

For each suffix and i=0,...,G obtain N independent oracle bits at i Delta, form their empirical frequency p_i, and compute exactly

    H_hat=max_i (1+i Delta)|p_i-p_G|.

Output YES iff H_hat(s2)-H_hat(s1)>4/Lambda_cmp. All quantities in this comparison are rational; there are no transcendental branch predicates.

Here is a direct accuracy check, including the conservative changes to the source constants. Hoeffding and a union bound over both suffixes and G+1 points show that all empirical errors are at most b=1/(100 Lambda_cmp M), except with probability at most

    4(G+1) exp[-2N b^2] <= exp(-C)/2.

Since s>=-C, the endpoint bias is at most 2exp(1-M/C)<=b. The mesh interpolation error in p is at most C Delta=b. Thus every empirical difference p_i-p_G approximates p(s+u)-p_infinity for u in[i Delta,(i+1)Delta] to at most4b. Multiplication by1+u and changing the prefactor contributes at most4b(1+M)+Delta<1/(5 Lambda_cmp). On u>=M, the envelope2(1+u)exp(1-u/C) is decreasing and at most1/(10 Lambda_cmp). Consequently |H_hat-H|<=1/Lambda_cmp. The exact comparison threshold above separates NO (difference<=2/Lambda_cmp) from YES (difference>=10000/(101 Lambda_cmp)-2/Lambda_cmp). This proves the required OCP guarantee, with failure below exp(-C)<=exp(-Lambda_walk), using exactly2(G+1)N calls and maximum logscale M.

Use these comparisons in the primary guided walk: start at u0=0; for each i=0,...,T_walk choose j uniform in{1,2}, sign uniform, and X uniform[0,1]; propose v=sign exp(-2K X)e_j/(K sqrt(2)); accept v exactly when the comparison returns YES. The only data-dependent branch is the comparison of empirical rational maxima just described. Restore scale3 by z=3u. The following causal reference process proves correctness without conditioning fresh steps on future successes. Here d=d_H=2, T=T_walk, and Lambda_walk is the fixed comparison confidence; the shifted normalized center has norm in[1/3,1].

The old v6 global-correctness wording leaves a causal obligation, not a permission to condition fresh coins on future success. Define F_i as the sigma-field of the corrected reference walk's complete past: all previous positions, proposals, empirical bits, numerical records if present, and past decisions, excluding future proposals and empirical bits. At stage i the new coordinate, sign and continuous X are independent with their stipulated laws conditional on every F_i-history. The following process and its indicators are adapted to that filtration.

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

To justify the interval estimate also for a nonradial chosen coordinate, fix its line and sign. If the line misses the epsilon-ball the probability is zero. Otherwise its positive step interval has product of endpoints r^2-epsilon^2; its endpoint ratio is maximized when the line passes through the center, giving log((r+epsilon)/(r-epsilon)). Dividing by the log-uniform density denominator2K gives the bound displayed above. The inequalities hold because Lambda_walk=10Kd²ceil(log2(2T_walk)) is much larger than K and log K. On every other trial the OCP hypotheses apply, and an incorrect promised decision has conditional probability <=exp(-C). Union over T+1 trials is bounded by the proof's conservative 10(T+1)exp(-Lambda_walk/2)<exp(-K)/2. Until the first bad event the actual and corrected processes coincide. Therefore the actual real walk fails with probability at most exp(-K), with no multiplication of marginal probabilities and no conditioning on all future comparisons succeeding.

This closes the precise martingale obligation for the specified walk, preserving the core v6 algorithm and constants. A literal future-conditioned proof would be rejected; this causal proof is the supplied reconciliation.

Each OHCP invocation therefore makes at most

    Q_H=2(T_walk+1)(G+1)N

calls. Run every n/2 pair under A and then under1-A, for Q_*=nQ_H total. The same deterministic loop bounds hold in the incorrect orientation, whose answers may be arbitrary. No extra sign-calibration calls are made. The correct global orientation is common to all pairs because its initial gap comes from the same spherical benchmark.

### 7.1a Fixed analytic accuracy and absence of circular choices

Choose ONCE epsilon0=min(1/16,zeta/(64kQ_*)), a=Up(sqrt(log(8n/epsilon0)/pi))+1, v0>=2sqrt(n)a, and d0=delta*w/(32nkv0), enlarging v0 for uniqueness if necessary. The two fixed normalizer comparisons over all kQ_* samples cost

    2kQ_*epsilon0/(1-epsilon0)<zeta/16.

The radial profile uses fixed v0 throughout. Kappa and all loop counts are chosen first: v0*d0=h0=delta*w/(32nk), so S is independent of both v0 and Q_*. The stated kappa bound makes the analytic OHCP hypotheses valid also at the larger K, as all three hypotheses weaken when the confidence parameter increases.

### 7.1b Finite random steps and global physical-kernel coupling

We must approximate the primary algorithm's own continuous random choices, not only its oracle samples. The following bound supplies the missing finite contract.

For the EXACT discrete multiplier r at any t<=M, let v_max=v0 exp(t), b=v_max/sqrt(n). In coefficient coordinates its width-square operator is at most b^2 I. Completing the square in the moment generating function, and using the same Poisson normalizer bound for every translate, gives

    E exp(theta r_l) <= [(1+epsilon0)/(1-epsilon0)] exp(b^2 theta^2/(4pi)).

Chernoff therefore yields Pr[|r_l|>=u]<=2c exp(-pi u^2/b^2), c=(1+epsilon0)/(1-epsilon0)<2. Tail integration implies E||sigma(r)||_2^2<=2n v_max^2. If two physical guess positions differ by complex Delta_z, their canonical mean difference has norm at most d0|Delta_z| ||sigma(r)||_2. Conditional on r, Pinsker for the added spherical Gaussian bounds TV by2d0|Delta_z| ||sigma(r)||_2/w. Average over r, take k products, then round/reduce/apply A. Thus the PHYSICAL oracle's acceptance kernel, at every z in the plane and every t<=M, is Lipschitz with constant at most

    4k sqrt(n) v0 exp(t) d0/w <= exp(M).

No guard or radiality assumption is used here. It remains true far outside the analytic patch. Intrinsic approximate multiplier sampling is charged separately by Section7.3.

Take the integer

    B=2M+2K+Up(log2(256Q_*(T_walk+2)/zeta))+10.

Sample a B-bit uniform integer and use its dyadic midpoint X_hat in[0,1], coupled with ideal X in the same cell. Then |X-X_hat|<=2^(-B). Approximate the proposed scalar step at X_hat by a dyadic to absolute error2^(-B). The derivative of exp(-2KX)/(Ksqrt(2)) has magnitude at most2, so each step changes by at most3*2^(-B). Until oracle bits disagree, all empirical comparisons agree exactly and the normalized positions differ by at most3(T_walk+1)2^(-B); including a trial position and scale3 gives position discrepancy at most9(T_walk+2)2^(-B).

At an adaptive query, first compare the ideal analytic oracle with the exact PHYSICAL oracle at the ideal real position, using Section7.0's uniform posterior error; then compare physical kernels at the real and dyadic positions by the GLOBAL bound above; then use the finite sampler at the dyadic position. This order avoids assuming continuity of the analytic patch boundary. Conditional maximal coupling and a union bound charge the walk-position perturbation by at most

    Q_* exp(M) 9(T_walk+2)2^(-B) < zeta/16.

Logscales i Delta are exact rationals, so need no separate random-logscale perturbation. The computed dyadic walk positions have bit length O(B+log T_walk); the step exponential can be evaluated to B-bit absolute precision in polynomial time in K+B. As M and every loop count are polynomial in kappa, B is polynomial in kappa and log(1/zeta). The final position discrepancy is at most exp(-kappa)/4, while the primary output error is3exp(-K)<=3exp(-kappa)/4. Hence the total physical-center error is below3exp(-kappa), preserving Section6. This is a coupling for this concrete physical oracle; it does not assert that arbitrary real OHCP oracles admit finite precision.

### 7.2 The exact finite benchmark laws

Set h_J=1/(DP), where P>=1 is an arbitrary public integer, and F_J=h_J Z^n/qJ^-1 in COEFFICIENT coordinates. Coordinate nearest-grid rounding Q_h, with a fixed tie convention, commutes with qJ^-1. The two exact laws are

    planted: (J, Q_h(G_w) mod L)^k,
    comparator: (J, uniform(F_J))^k.

Here w is CANONICAL width, so the coefficient width of G_w is b=w/sqrt(n). The finite group has order q^n D^(n-1)P^n and is represented by ordinary HNF/SNF. Haar followed by Q_h is exactly uniform(F_J). Every Gaussian comparison in Sections 1–5 occurs BEFORE this same observation kernel, so discontinuous rounding is harmless by data processing. This is precisely B's finite input interface after substituting coefficient width b for B's w. All public J metadata is common to the two experiments.

### 7.3 Full sampler justification and conditional numerical budget

The definition-only companion is part of the theorem. It fixes all scalar, ellipse, CDF, rejection, empirical and walk algorithms; no access to this proof is needed merely to execute them. Its Up operation is deterministic certified rounding, between ceil(x) and ceil(x)+1. Replacing a precision/cutoff by this upper bound only strengthens the error inequalities below. The integer expressions C,Lambda_cmp,M,Delta,G,N,Q_* use exact integer logarithms and do not change. The scalar a may increase by one from the nominal v6 choice; all smoothing estimates require only its stated lower bound. The actual d0 always uses the actual chosen a and v0, never an old nominal value.

The global counter c starts at0 and is incremented before every physical sample. Put tau_c=zeta/[16(c+1)^2]. All the following estimates are uniform in the query, rational target, position, current sample index, and complete earlier history. Fresh sample and A coins are used at every call. The sum over c>=1 is less than zeta/16; sequential coupling charges this sum, without multiplying it by a success probability or conditioning on a favorable future transcript.

First justify the standard real-Gaussian approximation Std(eps,alpha). Couple its p-bit midpoint Uhat to a uniform U in the same dyadic cell. Except when the true inverse-CDF value is outside[-H,H], whose probability is below alpha/4 by the displayed H, the inverse CDF has derivative at most exp(pi H^2)=1/ell. CDF evaluations and the dyadic midpoint perturb the probability argument by at most a constant times2^-p<=eta. Any early ambiguity return is therefore within eps/4 of the true quantile. All nonambiguous bisection decisions retain that quantile up to this same boundary tolerance, and after L steps the spatial interval width is below eps/4. Clipping at an endpoint is also within eps on the nontail event. The total exceptional probability is below alpha; the algorithm always terminates after the displayed finite L. This is a coupling in absolute position, not raw TV between a discrete and a continuous law. Certified evaluation precision is polynomial in log(1/eps),log(1/alpha), since H^2=O(log(1/alpha)). The CDF and exponential evaluations specified in the companion use finite series with certified remainders; argument and constant approximations are included in the returned error intervals.

For the elliptical multiplier, in coefficient coordinates let W=Vcoef-a^2 I, which is at least3a^2 I. Its positive square root B is explicitly diagonalized by the fixed real Fourier matrix. On the event that all ideal standard Gaussians have magnitude at most Hcut, the Bhat entrywise tolerance contributes at most xi/4 to the output l1 error. The n Std calls, each with positional tolerance eps_Z, contribute at most another xi/4 under multiplication by Bhat. Exact rational multiplication contributes no extra error. The union of their exceptional events and the original Gaussian tails has probability at most alpha_H; hence Hhat is coupled to H~G_W with ||Hhat-H||_1<=xi except with probability alpha_H.

The ideal continuous-center/discrete-scalar construction is close to D_(Z^n,Vcoef) with its full normalizers retained. For every H, rho_a(Z^n-H)/a^n is in[1-epsilon0,1+epsilon0]. Completing the Gaussian convolution without that denominator gives the weight det(Vcoef)^(-1/2) exp(-pi r^T Vcoef^-1 r). Its sum over integer r is another theta factor in the same interval. Dividing by the actual shifted denominator gives a density ratio to the normalized target discrete Gaussian between(1-epsilon0)/(1+epsilon0) and(1+epsilon0)/(1-epsilon0). Its TV discrepancy is at most epsilon0/(1-epsilon0).

Changing the scalar mean from H to Hhat changes the product discrete-Gaussian law by at most4pi||Hhat-H||_1/a. One direct proof differentiates the normalized scalar density: its TV derivative is at most(pi/a^2)E|X-EX|. The same uniformly flat translated theta normalizers give the moment-generating bound E exp(theta(X-c))<=2 exp(a^2 theta^2/(4pi)), hence E(X-c)^2<=2a^2 by tail integration. The displayed4pi/a derivative bound is therefore conservative. Tensorization gives the l1 mean bound. Integrating the coupling of H,Hhat adds at most4pi xi/a+alpha_H.

Here is a full bound for the scalar finite algorithm, uniform in every rational center. Write Ks>=log2(64/nu), Ns=a Ks+1, and Hs=2Ns+1=2a Ks+3. For a>=1, Poisson summation on Z gives rho_a(Z-f)>=0.9a, uniformly in f. The two tails outside[-Ns,Ns] have mass at most(a/(pi Ks))exp(-pi Ks^2), by comparison with the Gaussian integral; after normalization this is below nu/64. The retained ideal weight sum Z is at least0.85a. The ps-bit weight approximation changes its l1 unnormalized weights by at most Hs*2^-ps<=3a nu/1024. Thus the normalized retained weight law changes by less than nu/200. Its acceptance probability under a uniform proposal is at least1/(5Ks). The finite Ls>=40Ks log(16/nu) proposals have no-accept probability at most(nu/16)^8<nu/64. On at least one acceptance, the first accepted candidate has precisely the normalized approximated-weight law; independence is internal to those fresh proposals and no external challenge branch is conditioned. The deterministic fallback therefore costs only that failure probability. Tail, weight, and fallback errors total less than nu.

The preceding scalar bound temporarily uses exact uniform integer proposals. UniformCap fails with probability at most2^-Rcap per proposal, because each binary rejection attempt succeeds with probability at least1/2. Over n Ls proposals within one physical sample, its additional discrepancy is at most n Ls 2^-Rcap<=tau/16. A uniform failure returns an integer fallback, so algebraic membership r in R is exact on every branch. No rejection loop is unbounded.

With xi=a tau/(64pi), alpha_H=tau/16, and nu=tau/(16n), the total multiplier discrepancy is at most

    epsilon0/(1-epsilon0) + 4pi xi/a + alpha_H + n nu + tau/16
      <= epsilon0/(1-epsilon0) + tau/4.

This is a normalized full-law comparison, not merely a covariance calculation. It holds for every t<=M, including the largest selected width, and at every rational query position. The fixed intrinsic epsilon0 term is already included in the two-normalizer global allowance of Section7.1a.

### 7.4 Mean, rounded-grid sampler, final arithmetic and runtime

Let b=w/sqrt(n). The companion's rational mean mhat is within b tau/(64pi) in l1 of r(T_bdd-g). Gaussian translation before rounding therefore changes TV by at most(2pi/b)||mhat-m||_1<=tau/32. The coefficient precision rule in the companion follows from the negacyclic convolution bound n||r||_infinity. It uses the actual sampled integer r, so exponentially large multiplier magnitude is paid through its bit length, not an unbounded enumeration. Reduction modulo L and A only contract this distance.

For GridGaussian, each coordinate's finite support contains all cells meeting the interval mhat_l+[-b H_G,b H_G]. The joint omitted Gaussian tail is at most tau/16. The actual M_G=2[Up(b H_G/h)+2]+1 bounds the number of retained cells even under the companion's conservative rounding. Couple the p_G-bit midpoint to a uniform number in its cell. Unless that number is within4*2^-p_G of a true CDF boundary, every approximate binary-search comparison has the same answer as the ideal comparison. A union over at most n M_G boundaries gives loss at most8n M_G 2^-p_G<=tau/32. On the exceptional event the fixed finite search still returns a supported value; no correctness assumption about approximate threshold monotonicity is needed. Thus this procedure is close to the EXACT rounded Gaussian law, not to a continuous variable in raw TV. It takes O(log M_G) evaluations rather than enumerating M_G cells.

The numerical charges in one sample are at most tau/4+tau/32+tau/16+tau/32<tau. Together with the fixed two-normalizer charge and the walk-position perturbation, their conditional sums over both orientations are below zeta with slack. The filtration includes all previous samples, coins, numerical decisions and the global counter. At an equal coupled history, the next bound applies uniformly; after the first disagreement its probability has already been charged. This is the required causal sequential coupling, not a product of marginal probabilities.

All actual walk positions are dyadic with norm at most(T_walk+1)[1/(Ksqrt(2))+2^-B], regardless of oracle answers. Logscales are exact rationals in[0,M]. Every proposal cap, scalar output size, matrix/mean precision and CDF search length therefore has a polynomial bit bound in the theorem's complete input lengths and kappa,1/delta,log(1/zeta). Up takes one fixed-accuracy evaluation and an exact rational ceiling; no test for equality with an integer is required. Certified evaluation costs and numerator/denominator lengths of ALL supplied scalars are included. A's own bounded runtime is supplied as a premise, including on wrong-sign query distributions.

For final reconstruction, the ideal coordinate error is at most3d0 exp(-kappa). Computing the coefficient estimate to extra error q/(64D), as in the companion, still permits exact rounding to(q/D)Z^n: the theorem imposes3w exp(-kappa)<q/(8D), and d0<w, so the total error is below q/(8D)+q/(64D)<q/(2D). The final canonical-residual test is now explicitly rational. Since p_test>=log2(64/d0)+2 whenever this quantity is positive, and p_test=0 only when the required relative bound is already satisfied, eps_test=2^(-p_test)<=d0/256. Therefore |c_test-d0|<=d0/256, d_lower=c_test-eps_test lies in[(127/128)d0,d0], and threshold_test=3c_test/2 lies in[(765/512)d0,(771/512)d0]. All comparisons use these computed rational numbers. Residual intervals have width at most d_lower/8<=d0/8. The true candidate has upper endpoint at most9d0/8, strictly below threshold_test. Every false lattice candidate has residual greater than3d0, so its upper endpoint exceeds threshold_test. Neither the runtime nor this reasoning assumes a separation between an arbitrary off-promise candidate and the original nonrational value2d0. Only one predetermined evaluation precision and exact rational comparisons are used. The added arithmetic cost is polynomial in the required precision and the declared actual scalar evaluation/encoding costs; it makes no calls to A and changes no Q_* or probability budget.

### 7.5 Recovery and total success

For the correct orientation, the ideal OHCP calls all succeed except with probability at most (n/2) exp(-kappa). Run the explicit walk at confidence K=kappa+200. Section7.1b charges its dyadic-position error as well as all finite random steps. The resulting coordinate error is at most 3d0 exp(-kappa), as used in Section 6. The finite adaptive transcript changes success probability by at most zeta.

Round T-minus-estimated-e to (q/D)Z^n. Check candidate membership in L exactly. Use the rational d_lower/8 interval width and threshold_test specified and bounded in Section7.4. The true lambda has residual at most d0 and its certified upper endpoint is at most9d0/8, below threshold_test. Any other lattice vector differs from it in infinity norm by more than4d0, hence has residual more than3d0 and fails the same rational test. At most two complete candidates, one for each global orientation, are checked.

The success probability is at least 1-(n/2)exp(-kappa)-zeta. Runtime is polynomial in the input bit lengths, n,k,log P,1/delta,log(1/zeta),kappa, plus at most Q_* calls to A. The analytic and finite claims are one parameterized theorem/proof. The explicit comparison/walk loop bounds replace the previously unverified generic finite T_H contract. All added numerical errors are conditional transcript bounds, and their sum remains below zeta with slack. Runtime includes the full binary encoding lengths of EVERY supplied scalar (including numerator and denominator lengths), ideal basis, target, and parameter-evaluation routine, plus the actual certified evaluation cost at each requested precision. Polynomial-time scalar representations are part of the declared input model; no bound polynomial only in log of a scalar magnitude is asserted. Rational or explicitly algebraic scalars with polynomial-time certified evaluation suffice.

## 8. Conditional downstream interpretation

A fixed binary-recovery algorithm can furnish pointwise D_J if the fractional-source lossiness theorem is uniform in J. An average-over-Gen distinguisher would not suffice for the uniform BDD conclusion. B's Gaussian-rounding kernel and A's lossiness composition are separate dependencies and must be reviewed independently.

The standard quantum BDD-to-DGS lemma, if applied to the finite BDD oracle, would approximately sample on L*=conjugate(J)/(nq) at width sqrt(n)/(sqrt(2)d0). Scaling by nq and conjugating would give D_J at width n*q*sqrt(n)/(sqrt(2)d0). The actual output law includes primary Gaussian-truncation, reference-state, finite-gate, and coherent BDD errors; it is not an exact sampler. This is an absolute-width consequence for the same restricted J family. It does not supply the missing reduction from arbitrary worst-case ideals into that family.
