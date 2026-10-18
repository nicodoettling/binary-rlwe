# Finite multiplier OHCP proof, v4

Status PROVISIONAL; fresh review required. V1 is rejected as a completed proof for the normalization gap recorded in ohcp-v1-gap-and-repair-record.md. No v1 acceptance is inherited. Read theorem-v4 first. V3 incorporates the neighborhood correction and a finite wrapper; earlier version bytes remain unchanged. No claim of standard restricted-family hardness is made.

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

## 4. One pair tends to full Haar

For power-two cyclotomics, R^vee=R/n up to a unit, and the Euclidean dual of L=qJ^-1 is conjugate(J)/(nq). In particular each nonzero dual element a has

    |N(a)| >= D/(nq)^n.

Applying diagonal widths, with every unselected width at least w and selected pair width W, yields product lower bound D*w^(n-2)*W²/(nq)^n. AM-GM gives dual minimum at least sqrt(n)*c, with

    c=[D*w^(n-2)*W²]^(1/n)/(nq).

This is exactly PRS17 Lemma6.9 specialized to I=L, since N(L)=q^n/D and Delta_K=n^n. It gives smoothing error exp(-n c²) for c>=1, and hence TV at most exp(-n c²)/2 from Haar. One could also derive a slightly weaker bound by packing the scaled dual; no spectral mass assumption on A is involved.

For the query above set h=v0*d0 and a0=D^(1/n)*w^(1-2/n)*h^(2/n)/(nq). Then c(s)>=a0 exp(2s/n). Define S=max(0,(n/2)log(1/a0)). For s>=S,

    |p(s)-p_infinity| <= (k/2) exp[-n exp(4(s-S)/n)].

Choose kappa>=4S+4n+4log(k+1)+20. For s<=kappa/2 the OHCP bound 2exp(-s/kappa)>=1 holds trivially. For s>kappa/2, s-S>=s/2 and the preceding double-exponential bound is at most 2exp(-s/kappa). Negative s also satisfies the trivial bound. Because p(0,t)=p(t+log|z*|) and log|z*|>=0, the same decreasing upper bound gives |p(0,t)-p_infinity|<=2exp(-t/kappa). Thus the actual starting-guess decay required by BRST Lemma3.8 holds with polynomial kappa whenever input logarithms are polynomial.

The coordinator initially raised a proper-subtorus concern. It is resolved because a nonzero field element cannot vanish at the selected embedding; its real one-plane image is generally dense modulo L. The algebraic norm makes the density quantitatively effective. An arbitrary real lattice or a reducible product algebra need not have this property.

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

### 7.1 Primary runtime, orientations, and fixed analytic accuracy

Fix the algorithm in PRS Proposition 4.4 / BRST Lemma 3.8. Denote by T_H(2,kappa) ANY fixed valid polynomial upper bound on its time, number of calls, query logscales, and query-description lengths in dimension two. The primary theorem asserts such a polynomial. No numerical degree or constant has been independently verified here. The formulas are quantitative in T_H; a runtime bound for this imported algorithm is not advice about J or a new hardness premise.

Run all n/2 coordinate pairs with A, then all n/2 pairs with 1-A. The correct orientation is common to every pair because each initial gap comes from the same spherical benchmark. Reconstruct at most one complete vector for each orientation and verify it. There are at most

    Q_* = n ceil(T_H(2,kappa))

calls to A and k Q_* samples, with no calibration or exponential coordinate combinations. Enforce a Q_* call cap. For each primary invocation also enforce T_H bounds on execution steps, logscale, and query-description lengths, aborting that orientation if any bound is exceeded. The primary guarantee makes these caps inactive for the correct ideal orientation. The other orientation need not satisfy the OHCP excursion promise, so these caps are necessary for its unconditional runtime guarantee.

For 0<zeta<=1/8 choose ONCE

    epsilon0 = min(1/16, zeta/(64 k Q_*)),
    a = ceil(sqrt(log(8n/epsilon0)/pi))+1,
    v0 >= 2 sqrt(n) a,
    d0 = delta*w/(32 n k v0).

Enlarge v0 if needed for d0<q/(4D^(1/n)). In canonical coordinates eta_epsilon0(R)<=sqrt(n)a. The posterior comparison and intrinsic multiplier comparison each cost at most epsilon0/(1-epsilon0) per sample, so over both orientations their total is

    2 k Q_* epsilon0/(1-epsilon0) < zeta/16.

We do NOT vary v0 with the query index, which would change the radial profile. This explicitly distinguishes the imported symbolic polynomial runtime from an independently calculated numerical exponent.

There is no circular choice of kappa: h=v0*d0=delta*w/(32nk) and therefore S from Section 4 are independent of v0 and T_H. First take kappa satisfying Sections 4–5, kappa>=log(8n/zeta), and 3w exp(-kappa)<q/(8D), then define Q_*, epsilon0, a, v0 and d0. Since d0<=w the last inequality is sufficient for reconstruction. All parameter logarithms are polynomial in the declared input and 1/delta, log(1/zeta).

### 7.2 The exact finite benchmark laws

Set h_J=1/(DP), where P>=1 is an arbitrary public integer, and F_J=h_J Z^n/qJ^-1 in COEFFICIENT coordinates. Coordinate nearest-grid rounding Q_h, with a fixed tie convention, commutes with qJ^-1. The two exact laws are

    planted: (J, Q_h(G_w) mod L)^k,
    comparator: (J, uniform(F_J))^k.

Here w is CANONICAL width, so the coefficient width of G_w is b=w/sqrt(n). The finite group has order q^n D^(n-1)P^n and is represented by ordinary HNF/SNF. Haar followed by Q_h is exactly uniform(F_J). Every Gaussian comparison in Sections 1–5 occurs BEFORE this same observation kernel, so discontinuous rounding is harmless by data processing. This is precisely B's finite input interface after substituting coefficient width b for B's w. All public J metadata is common to the two experiments.

### 7.3 Summable numerical accuracy and exact integral multipliers

Use one global counter j=1,2,... over samples in BOTH orientations and all coordinate runs. Put

    tau_j=zeta/[16(j+1)^2].

Beyond the two fixed epsilon0 terms, the numerical error for sample j is at most tau_j below. The sum is less than zeta/16 even for an unbounded counter. Every bound holds conditionally on every prior transcript. Sequential maximal coupling therefore charges their sum under adaptive queries; there is no uncharged multiplier Q.

In coefficient coordinates the multiplier width-square matrix Vcoef has eigenvalues v_i²/n>=4a². Apply B's explicit sampler: H~G_(Vcoef-a²I), approximate it by rational Hhat, then use independent D_(Z,a,Hhat_i) scalar samplers. Set

    xi=a tau_j/(64pi), zeta_H=tau_j/16, nu=tau_j/(16n).

B's bound is epsilon0/(1-epsilon0)+4pi xi/a+zeta_H+n nu. The numerical part is 3tau_j/16. The scalar algorithm is finite: K=ceil(log2(64/nu)), N=ceil(aK)+1, p=ceil(log2(1024(K+1)/nu)); make at most ceil(40K log(16/nu)) uniform proposals in [-N,N], use p-bit approximations to Gaussian weights, and use the stated fallback. B's proof charges the fallback and proves integer-translation equivariance. For uniform integers in a finite interval use binary rejection with a fixed cap. Let L_j=ceil(40K log(16/nu)) be the scalar proposal cap and R_j=ceil(log2(16nL_j/tau_j)). Each proposal uses at most R_j binary-rejection attempts; on failure use a deterministic fallback and record that event. An attempt accepts with probability at least1/2, so over at most nL_j proposals the extra distance is at most nL_j 2^-R_j<=tau_j/16. This replaces expected-polynomial rejection by bounded runtime within the existing error slack. The multiplier r is ALWAYS an exact element of R, so r lambda cancels exactly.

An explicit H approximation is obtained as follows. Let B B^T=Vcoef-a²I and T=ceil(sqrt(log(16n/zeta_H)/pi))+1. Approximate B entrywise within xi/[4n²(T+1)]. Approximate each standard Gaussian by inverse-CDF coupling to error xi/[4n²(1+||Bhat||max)], except with total probability zeta_H/2, and truncate coordinates at T with the remaining allowance. Then ||Hhat-H||_1<=xi. Required precision is polynomial in log(1+||B||), log(1/xi), n and log(1/zeta_H); log||B||=O(log v0+t). No enumeration of exponentially large boxes is used.

### 7.4 Finite mean, Gaussian grid, and bit complexity

After sampling exact r, approximate the coefficient mean m=r(T-g(z)) by rational mhat so that

    ||mhat-m||_1<=b tau_j/(64pi).

It suffices to approximate every coefficient of T-g(z) to b tau_j/[64pi n²(1+||r||infinity)], by the negacyclic convolution bound. Gaussian translation BEFORE rounding then costs at most (2pi/b)||mhat-m||_1<=tau_j/32. Roots of unity, exponential widths, and computable-real oracle queries are approximated to this residual-product precision. Its bit requirement depends on the actual t and actual exact r, and is polynomial in their bit lengths. No exact-real input model or t-independent precision is assumed. The primary polynomial-time OHCP routine is understood in its usual computational model; its requested elementary real quantities are approximated as part of this uniform query error budget.

To sample Q_h(mhat+G_b), truncate each standardized coefficient Gaussian at

    T_G=ceil(sqrt(log(64n/tau_j)/pi))+1,
    M=2 ceil(b T_G/h_J)+5,
    p_G=ceil(log2(256nM/tau_j)).

The combined tail is at most tau_j/16. At most M grid cells occur per coordinate. A p_G-bit uniform variate, binary search of Gaussian CDF boundaries, and CDF evaluation to absolute error 2^-p_G return the ideal rounded cell unless the ideal uniform variate lies within 4*2^-p_G of a boundary. The union bound is at most 8nM 2^-p_G<=tau_j/32. Use a fixed endpoint outside the truncated interval. The search takes O(log M) CDF evaluations. log M and p_G are polynomial in log P, log D, log w, the mean bit length and log(1/tau_j). Approximation decisions use certified intervals; any ambiguous branch is included in the boundary event just bounded. This constructs a finite categorical distribution close to the EXACT rounded Gaussian law, never asserting raw TV closeness of a discrete random variable to a continuous one.

Reduce the resulting rational vector modulo qJ^-1 by exact basis arithmetic and invoke A. Including the tau_j/16 bounded-rejection charge, the numerical terms sum to less than tau_j with slack. Along with both fixed epsilon0 terms, the entire adaptive transcript loss is less than zeta. Polynomial bit complexity follows from T_H and the displayed per-query precision rules; log(j+1), t, and log||r|| are polynomially bounded.

### 7.5 Recovery and total success

For the correct orientation, the ideal OHCP calls all succeed except with probability at most (n/2) exp(-kappa). Run the primary routine at confidence kappa+log 4 and compute its returned coordinates to additional error at most exp(-kappa)/4. T_H(2,kappa) is defined to bound this shifted-confidence invocation throughout this packet. The resulting coordinate error is at most 3d0 exp(-kappa), as used in Section 6. The finite adaptive transcript changes success probability by at most zeta.

Round T-minus-estimated-e to (q/D)Z^n. Check candidate membership in L exactly. Approximate each canonical residual by certified intervals of width d0/8, and accept only if the certified upper infinity norm is at most 2d0. The true lambda has residual at most d0 and passes. Any other lattice vector differs from it in infinity norm by more than 4d0, hence has residual more than 3d0 and fails. At most two complete candidates, one for each global orientation, are checked.

The success probability is at least 1-(n/2)exp(-kappa)-zeta. Runtime is polynomial in the input bit lengths, n,k,log P,1/delta,log(1/zeta),T_H(2,kappa), plus at most Q_* calls to A. The analytic and finite claims are now one parameterized theorem/proof, with no open numerical-error or adaptive-call multiplier. The numerical degree of the PRIMARY imported OHCP runtime remains unstated, as it is in the cited theorem.

## 8. Conditional downstream interpretation

A fixed binary-recovery algorithm can furnish pointwise D_J if the fractional-source lossiness theorem is uniform in J. An average-over-Gen distinguisher would not suffice for the uniform BDD conclusion. B's Gaussian-rounding kernel and A's lossiness composition are separate dependencies and must be reviewed independently.

The standard quantum BDD-to-DGS lemma, if applied to the finite BDD oracle, would sample on L*=conjugate(J)/(nq) at width sqrt(n)/(sqrt(2)d0). Scaling by nq and conjugating would give D_J at width n*q*sqrt(n)/(sqrt(2)d0). This is an absolute-width consequence for the same restricted J family. It does not supply the missing reduction from arbitrary worst-case ideals into that family.
