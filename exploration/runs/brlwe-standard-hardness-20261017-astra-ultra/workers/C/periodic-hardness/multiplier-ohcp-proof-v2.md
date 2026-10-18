# Proof candidate for multiplier OHCP, v2

Status PROVISIONAL; fresh review required. V1 is rejected as a completed proof for the normalization gap recorded in ohcp-v1-gap-and-repair-record.md. No v1 acceptance is inherited. Read theorem-v2 first. No claim of standard restricted-family hardness is made.

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

Fix pair j, set z*=2+e_j/d0 in C, and use the selected guess g_j(z)=d0*(z-2), zero elsewhere. The shift2 is a known real displacement in the complex plane. The hidden center satisfies1<=|z*|<=3, including when e_j=0. Set the OHCP scale to3. Its enlarged search neighborhood has |z-z*|<=3(1+1/kappa)<=6, hence selected residual |h_j|<=6d0. Every other residual remains e_i, of magnitude at most d0.

All multipliers except pair j have width v0; pair j has width v0 exp(t). Because6d0=6delta*w/(32nkv0)<=w/(2eta) and v0>=2eta, Section1's uniform posterior comparison applies for every permitted guess and t>=0. The ideal continuous query law has widths

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

With kappa also at least max(2k,2/delta,20log3), the excursion, decay and Lipschitz requirements of PRS17 Proposition4.4 hold in dimension two. Its oracle access is only required for guesses within the enlarged decoding neighborhood, where Section1's uniform posterior bound holds. A polynomial number of oracle calls times exp(-kappa²) remains negligible.

## 6. Zero centers and exact reconstruction

The shifted center has norm in[1,3], so the OHCP lower-center promise exp(-kappa)*3<=|z*| holds as soon as kappa>=log3. No rational-input algebraic lower bound is used for this promise. The zero-error and individual zero-coordinate cases are covered by the same construction.

Run the two-dimensional OHCP procedure for each conjugate pair. It returns z_hat with |z_hat-z*|<=3exp(-kappa). Subtract the known shift2 and multiply by d0. The resulting canonical coordinate approximation to e has error at most3d0 exp(-kappa). The inverse canonical transform has operator norm1/sqrt(n), so each coefficient error is at most3d0 exp(-kappa).

Since D J^-1 is contained in R, lambda belongs to(q/D)R. Round the coefficient vector T-minus-estimated-e to that rational grid. This recovers lambda exactly if3d0 exp(-kappa)<q/(2D); choose kappa accordingly. Verify membership in L and the decoding promise. The uniqueness assumption d0<q/(4D^(1/n)) suffices because a nonzero element of L has canonical infinity norm at least q/D^(1/n). Rational coefficient input makes the final exact rounding/membership computation finite and explicit; no imaginary exact-real input model is being claimed.

## 7. Explicit sampler and finite arithmetic obligations

An elementary sampler avoids invoking a short-basis oracle or an unverified GPV interface. Choose a>=eta_epsilon(R), and v0>=2a. In canonical orthonormal coordinates, let V be the desired width-square matrix, whose smallest eigenvalue is at least v0². Sample

    H~D_(H,(V-a²I)^(1/2)),
    r | H ~ D_(R,a,H),

where the second distribution is the lattice Gaussian of center H and spherical width a. The canonical power basis has orthogonal length sqrt(n), so this conditional distribution factors into n one-dimensional integer Gaussians of coefficient width a/sqrt(n), centered at H's coefficients. It is sampled using ordinary coordinate routines on the known ring R.

For every H, the coset normalizer rho_a(R-H) lies in[(1-epsilon)a^n/det(R),(1+epsilon)a^n/det(R)]. Gaussian convolution gives the unnormalized integral proportional to rho_V(r). The normalizer rho_V(R) is likewise flat since min v_i>=a. Consequently the output-to-D_(R,V) pointwise mass ratio lies between(1-epsilon)/(1+epsilon) and(1+epsilon)/(1-epsilon), and TV is at most epsilon/(1-epsilon). This includes BOTH normalizers; no unbounded-support rejection is hidden. Applying the finite scalar sampler from B's operational Gaussian packet adds its explicit per-coordinate approximation loss. The sampler does not enumerate a box of side exp(t).

The OHCP theorem makes Q=poly(kappa,2) adaptive oracle calls at logscales t<=poly(kappa,2). All multipliers therefore have polynomial bit length even though their magnitude can be exponential. Truncate H and the conditional integer Gaussians at a polynomial number of standard deviations, paying the explicit Gaussian tail; approximate canonical transforms and T-g(z) so that on the retained event the residual product changes by at most w*epsilon/sqrt(n). Translation of the final spherical G_w then costs O(epsilon) in TV. This needs O(log maximum multiplier + log(1/w)+log(1/epsilon)) additional bits, a polynomial amount.

The one-call errors are: k epsilon/(1-epsilon) from completion; k epsilon/(1-epsilon) from multiplier sampling; k times scalar-sampler and finite-grid losses; and the explicit truncation/translation loss. Adaptive coupling pays Q times this total. It is insufficient to say merely that an error is negligible without accounting for Q. Because epsilon=exp(-kappa²) and Q is a fixed polynomial, the analytic terms remain negligible. A final finite theorem must instantiate Q's polynomial and the scalar/grid parameters from B's packet; those operational constants remain review obligations.

A discrete approximation is not asserted to be TV-close to a continuous law before observation. Both benchmark and query distributions use the same specified finite observation kernel. Gaussian TV bounds are first applied to the continuous smoothed law, then data processing handles discontinuous rounding. This is exactly the access model needed for the GP-to-fractional-source composition.

## 8. Conditional downstream interpretation

A fixed binary-recovery algorithm can furnish pointwise D_J if the fractional-source lossiness theorem is uniform in J. An average-over-Gen distinguisher would not suffice for the uniform BDD conclusion. B's Gaussian-rounding kernel and A's lossiness composition are separate dependencies and must be reviewed independently.

The standard quantum BDD-to-DGS lemma, if applied after completing the finite BDD oracle, would sample on L*=conjugate(J)/(nq) at width sqrt(n)/(sqrt(2)d0). Scaling by nq and conjugating would give D_J at width n*q*sqrt(n)/(sqrt(2)d0). This is an absolute-width consequence for the same restricted J family. It does not supply the missing reduction from arbitrary worst-case ideals into that family.
