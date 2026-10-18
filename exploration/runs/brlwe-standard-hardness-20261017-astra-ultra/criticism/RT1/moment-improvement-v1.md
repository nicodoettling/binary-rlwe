# RT1-authored product second-moment improvement v1

Status: PROVISIONAL NEW RT1 AUTHOR LEMMA, requiring a fresh nonauthor check. This is distinct from RT1's nonauthor review of root's frozen v1. It does not certify the original goal. Original failures are preserved in `preserved-failures-v1.md`.

## Frozen claim

Use the root tower notation R⊂S, m=tn, integral target I with A=N(I)^(1/n), and supplied integral ideals F_1,...,F_r with ∏F_j⊂IS and N(F_j)≤2^(rho m), 0≤rho<1. Assume r≥1, W_j≥4√m, and exact independent X_j∼D_(F_j,W_j). Let Y=Π(∏X_j). Then

    E||Y||² ≤ n m^(r-1) ∏_j [W_j²/(2π)].                 (M1)

For any h∈(0,1), the same deterministic algorithm with full-tuple implementation law within joint TV eta of that exact product law returns a nonzero point of I of norm at most

    B_mom=√(n/h) m^((r-1)/2) ∏W_j/(2π)^(r/2)             (M2)

except with probability at most

    min(1, eta + 4√m Σ_j 1/W_j + h).                    (M3)

All failures remain in the original law, and actual moments of an approximate source are not asserted. Off-ideal implemented samples trigger failure. The same assumptions about ordinary bases, fresh independent binary secrets upstream, exact membership arithmetic, and fully charged finite executions apply.

## Proof of the moment estimate

For any full lattice F and W>0, full centered Gaussian symmetry gives E X=0. Completing the square and the translated-theta maximum give, for every u∈R^m,

    E exp(〈u,X〉)≤exp(W²||u||²/(4π)).

Both sides are twice differentiable at zero and agree to first order. Applying the inequality along every real direction and comparing second derivatives gives

    Cov(X)≼c Id, c=W²/(2π).                              (M4)

For completeness, theta maximality follows directly by Poisson summation:

    ρ_W(F-a)=(W^m/det F) Σ_(v∈F*) exp(-πW²||v||²) exp(2πi〈v,a〉).

Pair v and -v and bound every cosine by one. Absolute convergence justifies the manipulations. The Gaussian mgf has all derivatives finite.

If T:R^m→R^d is fixed, (M4) yields E||TX||²=tr(T Cov(X) T^T)≤c||T||_F². For coefficient multiplication M_a, every row is a signed permutation of a's coefficients. Thus

    ||M_a||_F²=m||a||²,
    ||Π M_a||_F²=n||a||².                               (M5)

Under the exact product reference law, define A_0=1 and A_j=∏_(i≤j)X_i. Conditional on A_(j-1), the next sample is fresh. Therefore

    E[||A_j||² | X_1,...,X_(j-1)] ≤ m c_j ||A_(j-1)||².

Iteration gives E||A_(r-1)||²≤m^(r-1)∏_(j<r)c_j, including the r=1 empty product. Conditioning once more and using the second identity in (M5) gives

    E||Y||² ≤ n c_r E||A_(r-1)||² ≤ n m^(r-1)∏c_j.

Zeros cause no problem in this identity and are never discarded. The only conditional independence used is the original exact product law, not a successful-selection posterior.

Markov's inequality bounds Pr[||Y||>B_mom] by h. Combine it by a union bound with root's proper-subspace nonzero estimate. Finally transfer the bounded failure event by total variation, adding eta exactly once. This proves M2/M3.

The marginal-covariance premise alone cannot justify the conditioning: correlated samples need not obey M1. The implementation's joint TV premise is only used after the reference-law argument. In particular an eta-contamination at an arbitrarily large lattice point can make an implemented second moment arbitrarily large while preserving TV≤eta. Claiming (M1) for that implemented law would be false.

## Optional sharper zero-atom term

A separate elementary refinement, still provisional, is available without additional source assumptions. Poisson summation at zero gives ρ_W(F)≥W^m/N(F), so

    Pr_D(F,W)[X=0] ≤ N(F)/W^m.

Use this for the first r-1 zero exclusions and keep the last proper-subspace estimate. M3 may then be replaced by

    min(1, eta + Σ_(j<r) N(F_j)/W_j^m + 4√m/W_r + h).   (M3a)

Any ordering of factors is allowed if fixed independently of fresh samples. This improves the success estimate; it does not improve the radius or remove the source requirement. It does not multiply conditional zero probabilities. All estimates remain under the exact reference before the single TV transfer.

## Exact finite falsification/control and its limits

Reserved RT1-MOMENT-FV1 uses m=4,n=2,I=3R,F±=(3,z²±z+2),F3=S. Each prime norm is9 and eligible at rho4/5. Centered finite laws on F∩{-1,0,1}^4 have weights w^||x||². There are9,9,81 support points, so exactly6561 triples per schedule, two schedules.

For w=1/2 the exact covariances are (3/8)Id,(3/8)Id,(1/2)Id, and E||Y||²=9/4=n m²(3/8)(3/8)(1/2). For w=1/4 they are (1/12)Id,(1/12)Id,(1/3)Id, and E||Y||²=2/27=n m²(1/12)(1/12)(1/3). Thus the dimension dependence in the covariance-only argument is attained by these finite centered eligible-ideal laws. This is evidence that a better universal moment estimate needs extra information beyond the displayed covariance caps and independence. It is not a full-Gaussian lower bound, and equality in an expectation bound is not an actual-output lower bound with high probability.

The program checks the conditional identity tr(T Cov T^T) for every first-two-factor realization, including zeros, and retains the full output laws. All-inputs-nonzero/output-zero branches have masses3/64 and20/6561. Finite Gaussians on a restricted cube do not automatically satisfy the infinite Gaussian mgf theorem; the program computes their actual rational covariance caps independently. No inference from finite masses to a full Gaussian law is made.

## Comparison and growing-norm obstruction of this certificate

Root's high-probability radius is B_root=m^(r-1/2)L^r∏W_j. The new radius has only m^((r-1)/2) before ∏W_j, with √n and one common h^(-1/2). It replaces repeated deterministic worst-case multiplication bounds by conditional second moments.

Nevertheless the necessary family budget A≤2^(rho r) and the explicit floor W_j≥4√m imply

    B_mom/A
      ≥ (th)^(-1/2) [4m/(2^rho√(2π))]^r
      = h^(-1/2)t^(r-1/2)[4n/(2^rho√(2π))]^r
      ≥ h^(-1/2)[4n/(2^rho√(2π))]^r.                   (M6)

For fixed 0<rho<1 and A=n^alpha with alpha>0, r≥(alpha/rho)log_2 n. Since h≤1, (M6) is exp(Ω((log n)^2)). This is a rigorous lower bound on the numerical approximation certificate M2, even at its minimal permitted widths. It is not a lower bound on Y, not a failed-event conditioning argument, and not a barrier against correlations, normalization, selected output searches, weighted traces, or different source families.

No extra arithmetic or samples are needed to use this analytical improvement; all finite source and product costs are unchanged. The positive-success requirement eta+nonzero-error+h<1 remains explicit.
