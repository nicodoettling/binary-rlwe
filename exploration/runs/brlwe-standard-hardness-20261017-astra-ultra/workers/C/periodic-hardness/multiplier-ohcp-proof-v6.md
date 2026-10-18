# Finite multiplier OHCP proof, v6

Status PROVISIONAL; fresh review required. V1 is rejected as a completed proof for the normalization gap recorded in ohcp-v1-gap-and-repair-record.md. No v1 acceptance is inherited. Read theorem-v6 first. V6 resolves the finite primary-contract gap preserved in ohcp-v5-finite-contract-gap-record.md; earlier version bytes remain unchanged. No claim of standard restricted-family hardness is made.

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

### 7.1 Explicit finite comparison and walk bounds

The primary source actually inspected is PRS's June4,2020 author version, pages12–16, retrieved as indexed primary text at its author PDF URL. Page12 gives the weighted empirical-maximum comparison algorithm, page13 proves its accuracy, page14 specifies every guided-walk operation, and pages15–16 analyze progress. Direct PDF access failed; the source-access distinction is retained. We now give conservative rational parameters and prove the needed bounds; we do not infer a generic finite oracle representation contract from the words polynomial time.

Write K=kappa+200, d_H=2, T_walk=10^6 K^3 d_H^4, and Lambda_walk=10K d_H^2 ceil(log2(2T)). Set C=K+Lambda_walk. The OCP instance has shifts in[-C,C], C-Lipschitz profile, excursion at least1/C after its first shift, and decay2exp(-t/C), by the exact shift argument in PRS page14. It is enough to distinguish shift2<=shift1-1/C from shift2>shift1. This is stronger than the needed improvement1/Lambda_walk because C>Lambda_walk.

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

Use these comparisons in the primary guided walk: start at u0=0; for each i=0,...,T_walk choose j uniform in{1,2}, sign uniform, and X uniform[0,1]; propose v=sign exp(-2K X)e_j/(K sqrt(2)); accept v exactly when the comparison returns YES. The only data-dependent branch is the comparison of empirical rational maxima just described. The scale3 is restored by z=3u. On the high-probability correctness event, PRS's page15 induction keeps the true radii in the comparison promise and each successful progress step decreases log radius by at least1/(4K d_H^(3/2)), with conditional progress probability at least1/(10K d_H). Its martingale estimate gives at least T_walk/(10K d_H)-10sqrt(KT) such steps except with probability exp(-K)/2. Our larger T_walk makes this greater than10K^2 d_H^(3/2). Also10(T_walk+1)exp(-Lambda_walk/2)<exp(-K)/2. These are the numerical inequalities needed by the primary correctness proof. Hence the ideal real walk returns distance at most exp(-K) in normalized coordinates, with failure at most exp(-K). Increasing Lambda_walk only strengthens its comparison accuracy and the rare-near-center estimate. No stopping predicate or true-distance test is implemented.

Each OHCP invocation therefore makes at most

    Q_H=2(T_walk+1)(G+1)N

calls. Run every n/2 pair under A and then under1-A, for Q_*=nQ_H total. The same deterministic loop bounds hold in the incorrect orientation, whose answers may be arbitrary. No extra sign-calibration calls are made. The correct global orientation is common to all pairs because its initial gap comes from the same spherical benchmark.

### 7.1a Fixed analytic accuracy and absence of circular choices

Choose ONCE epsilon0=min(1/16,zeta/(64kQ_*)), a=ceil(sqrt(log(8n/epsilon0)/pi))+1, v0>=2sqrt(n)a, and d0=delta*w/(32nkv0), enlarging v0 for uniqueness if necessary. The two fixed normalizer comparisons over all kQ_* samples cost

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

    B=2M+2K+ceil(log2(256Q_*(T_walk+2)/zeta))+10.

Sample a B-bit uniform integer and use its dyadic midpoint X_hat in[0,1], coupled with ideal X in the same cell. Then |X-X_hat|<=2^(-B). Approximate the proposed scalar step at X_hat by a dyadic to absolute error2^(-B). The derivative of exp(-2KX)/(Ksqrt(2)) has magnitude at most2, so each step changes by at most3*2^(-B). Until oracle bits disagree, all empirical comparisons agree exactly and the normalized positions differ by at most3(T_walk+1)2^(-B); including a trial position and scale3 gives position discrepancy at most9(T_walk+2)2^(-B).

At an adaptive query, first compare the ideal analytic oracle with the exact PHYSICAL oracle at the ideal real position, using Section7.0's uniform posterior error; then compare physical kernels at the real and dyadic positions by the GLOBAL bound above; then use the finite sampler at the dyadic position. This order avoids assuming continuity of the analytic patch boundary. Conditional maximal coupling and a union bound charge the walk-position perturbation by at most

    Q_* exp(M) 9(T_walk+2)2^(-B) < zeta/16.

Logscales i Delta are exact rationals, so need no separate random-logscale perturbation. The computed dyadic walk positions have bit length O(B+log T_walk); the step exponential can be evaluated to B-bit absolute precision in polynomial time in K+B. As M and every loop count are polynomial in kappa, B is polynomial in kappa and log(1/zeta). The final position discrepancy is at most exp(-kappa)/4, while the primary output error is3exp(-K)<=3exp(-kappa)/4. Hence the total physical-center error is below3exp(-kappa), preserving Section6. This is a coupling for this concrete physical oracle; it does not assert that arbitrary real OHCP oracles admit finite precision.

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

It suffices to approximate every coefficient of T-g(z) to b tau_j/[64pi n²(1+||r||infinity)], by the negacyclic convolution bound. Gaussian translation BEFORE rounding then costs at most (2pi/b)||mhat-m||_1<=tau_j/32. Roots of unity, exponential widths, and computable-real oracle queries are approximated to this residual-product precision. Its bit requirement depends on the actual t and actual exact r, and is polynomial in their bit lengths. No exact-real input model or t-independent precision is assumed. The OHCP routine now requests only the rational logscales and dyadic positions specified in Sections7.1 and7.1b. Its own random-step approximation is charged there separately.

To sample Q_h(mhat+G_b), truncate each standardized coefficient Gaussian at

    T_G=ceil(sqrt(log(64n/tau_j)/pi))+1,
    M=2 ceil(b T_G/h_J)+5,
    p_G=ceil(log2(256nM/tau_j)).

The combined tail is at most tau_j/16. At most M grid cells occur per coordinate. A p_G-bit uniform variate, binary search of Gaussian CDF boundaries, and CDF evaluation to absolute error 2^-p_G return the ideal rounded cell unless the ideal uniform variate lies within 4*2^-p_G of a boundary. The union bound is at most 8nM 2^-p_G<=tau_j/32. Use a fixed endpoint outside the truncated interval. The search takes O(log M) CDF evaluations. log M and p_G are polynomial in log P, log D, log w, the mean bit length and log(1/tau_j). Approximation decisions use certified intervals; any ambiguous branch is included in the boundary event just bounded. This constructs a finite categorical distribution close to the EXACT rounded Gaussian law, never asserting raw TV closeness of a discrete random variable to a continuous one.

Reduce the resulting rational vector modulo qJ^-1 by exact basis arithmetic and invoke A. Including the tau_j/16 bounded-rejection charge, the numerical terms sum to less than tau_j with slack. Along with both fixed epsilon0 terms, the entire adaptive transcript loss is less than zeta. Polynomial bit complexity follows from the explicit finite loop and position bounds in Section7.1 and the displayed per-query precision rules; log(j+1), t, and log||r|| are polynomially bounded.

### 7.5 Recovery and total success

For the correct orientation, the ideal OHCP calls all succeed except with probability at most (n/2) exp(-kappa). Run the explicit walk at confidence K=kappa+200. Section7.1b charges its dyadic-position error as well as all finite random steps. The resulting coordinate error is at most 3d0 exp(-kappa), as used in Section 6. The finite adaptive transcript changes success probability by at most zeta.

Round T-minus-estimated-e to (q/D)Z^n. Check candidate membership in L exactly. Approximate each canonical residual by certified intervals of width d0/8, and accept only if the certified upper infinity norm is at most 2d0. The true lambda has residual at most d0 and passes. Any other lattice vector differs from it in infinity norm by more than 4d0, hence has residual more than 3d0 and fails. At most two complete candidates, one for each global orientation, are checked.

The success probability is at least 1-(n/2)exp(-kappa)-zeta. Runtime is polynomial in the input bit lengths, n,k,log P,1/delta,log(1/zeta),kappa, plus at most Q_* calls to A. The analytic and finite claims are one parameterized theorem/proof. The explicit comparison/walk loop bounds replace the previously unverified generic finite T_H contract. All added numerical errors are conditional transcript bounds, and their sum remains below zeta with slack. Runtime includes the full binary encoding lengths of EVERY supplied scalar (including numerator and denominator lengths), ideal basis, target, and parameter-evaluation routine, plus the actual certified evaluation cost at each requested precision. Polynomial-time scalar representations are part of the declared input model; no bound polynomial only in log of a scalar magnitude is asserted. Rational or explicitly algebraic scalars with polynomial-time certified evaluation suffice.

## 8. Conditional downstream interpretation

A fixed binary-recovery algorithm can furnish pointwise D_J if the fractional-source lossiness theorem is uniform in J. An average-over-Gen distinguisher would not suffice for the uniform BDD conclusion. B's Gaussian-rounding kernel and A's lossiness composition are separate dependencies and must be reviewed independently.

The standard quantum BDD-to-DGS lemma, if applied to the finite BDD oracle, would approximately sample on L*=conjugate(J)/(nq) at width sqrt(n)/(sqrt(2)d0). Scaling by nq and conjugating would give D_J at width n*q*sqrt(n)/(sqrt(2)d0). The actual output law includes primary Gaussian-truncation, reference-state, finite-gate, and coherent BDD errors; it is not an exact sampler. This is an absolute-width consequence for the same restricted J family. It does not supply the missing reduction from arbitrary worst-case ideals into that family.
