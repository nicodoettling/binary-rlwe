# Proof candidate for multiplier OHCP, v1

Status PROVISIONAL. Read theorem-v1 first. No claim of standard restricted-family hardness is made.

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

## 2. Fixed nuisance coordinates and radiality

Fix pair j. All multipliers except pair j have width v0; pair j has width v0 exp(t). For a guess z in C with |z-e_j/d0|<=1+1/kappa<=2, the residual has |h_j|<=2d0 and |h_i|=|e_i|<=d0 otherwise. Since d0=delta*w/(32nkv0), delta<=1 and v0>=2eta, the posterior inequalities above hold.

The ideal continuous query law has widths

    b_i=sqrt(w²+v0²|e_i|²),  i outside pair j;
    b_j(s)=sqrt(w²+(v0*d0*exp(s))²),
    s=t+log|z-e_j/d0|.

The unknown other errors enter only through fixed b_i. Let p(s) be A's acceptance on k independent copies of this continuous Gaussian modulo L. Its dependence on z,t is EXACTLY through s. This uses circular symmetry of the Gaussian on the complex plane; arbitrary A need not itself respect any symmetry.

## 3. Nonnegligible excursion

At s=0 every variance ratio to the spherical Gaussian is at most 1+a², where a=v0*d0/w=delta/(32nk). For centered real Gaussians, KL(P||Q)=one-half the sum of u-log(1+u), with 0<=u<=a². Since u-log(1+u)<=u²/2, the k-sample KL is at most nk a^4/4. Pinsker gives TV<=a² sqrt(nk/8)<delta/16. Therefore

    p(0)-p_infinity >= 15delta/16,

where p_infinity is A's acceptance under Haar, after choosing the sign of A. This is a statement about a distribution family at s=0, not about querying the unknown center exactly.

## 4. One pair tends to full Haar

For power-two cyclotomics, R^vee=R/n up to a unit, and the Euclidean dual of L=qJ^-1 is conjugate(J)/(nq). In particular each nonzero dual element a has

    |N(a)| >= D/(nq)^n.

Applying diagonal widths, with every unselected width at least w and selected pair width W, yields product lower bound D*w^(n-2)*W²/(nq)^n. AM-GM gives dual minimum at least sqrt(n)*c, with

    c=[D*w^(n-2)*W²]^(1/n)/(nq).

This is exactly PRS17 Lemma6.9 specialized to I=L, since N(L)=q^n/D and Delta_K=n^n. It gives smoothing error exp(-n c²) for c>=1, and hence TV at most exp(-n c²)/2 from Haar. One could also derive a slightly weaker bound by packing the scaled dual; no spectral mass assumption on A is involved.

For the query above set h=v0*d0 and a0=D^(1/n)*w^(1-2/n)*h^(2/n)/(nq). Then c(s)>=a0 exp(2s/n). Define S=max(0,(n/2)log(1/a0)). For s>=S,

    |p(s)-p_infinity| <= (k/2) exp[-n exp(4(s-S)/n)].

Choose kappa>=4S+4n+4log(k+1)+20. For s<=kappa/2 the OHCP bound 2exp(-s/kappa)>=1 holds trivially. For s>kappa/2, s-S>=s/2 and the preceding double-exponential bound is at most 2exp(-s/kappa). Negative s also satisfies the trivial bound. Thus the required decay holds with polynomial kappa whenever input logarithms are polynomial.

The coordinator initially raised a proper-subtorus concern. It is resolved because a nonzero field element cannot vanish at the selected embedding; its real one-plane image is generally dense modulo L. The algebraic norm makes the density quantitatively effective. An arbitrary real lattice or a reducible product algebra need not have this property.

## 5. Lipschitz bound and OHCP

The derivative of log b_j(s) is between zero and one. A two-dimensional Gaussian whose log width changes by ds has total-variation derivative at most2: differentiate its density and use E[2pi||X||²/b²]=2. Thus k independent samples give |p(s)-p(s')|<=2k|s-s'|. Modulo reduction, A, and any common observation kernel contract this bound.

With kappa also at least max(2k,2/delta,20log3), the excursion, decay and Lipschitz requirements of PRS17 Proposition4.4 hold in dimension two. Its oracle access is only required for guesses within the enlarged decoding neighborhood, where Section1's uniform posterior bound holds. A polynomial number of oracle calls times exp(-kappa²) remains negligible.

## 6. Tiny centers and exact reconstruction

Let B be a common positive integer denominator of the coefficient representation of T, and H0=D*B. Because D J^-1 is contained in R, H0 e belongs to R. Membership T in L can be checked directly; under d0<q/(4 D^(1/n)) it is the zero-error case. Indeed a nonzero element of L has infinity norm at least q/D^(1/n), so two errors bounded by d0 cannot represent the same target.

If e is nonzero then every embedding is nonzero, and

    1 <= |N(H0 e)| <= H0^n |e_j|² d0^(n-2).

Therefore |e_j|/d0 >= (H0*d0)^(-n/2). Taking kappa at least (n/2)log max(1,H0*w)+2 is sufficient to satisfy the lower-center promise; d0<=w. This bound uses only known denominator data, not a short generator or advice.

Run the two-dimensional OHCP procedure for each conjugate pair, always leaving all other guesses at zero. It returns coordinate approximations to e within d0 exp(-kappa). The inverse canonical transform has operator norm1/sqrt(n), so coefficient error is at most d0 exp(-kappa). Since lambda lies in (q/D)R, rounding T-minus-estimated-e coefficientwise to that rational grid recovers lambda if d0 exp(-kappa)<q/(2D). Verify membership in L and the decoding promise. This recovers all coordinates without assuming a fixed preferred coordinate of A or a Galois-equivariance property.

## 7. Proposed operational implementation and remaining review

The canonical power basis of R has orthogonal length sqrt(n). After inverse elliptical scaling, each basis vector has norm at most sqrt(n)/v0, regardless of the largest width. Standard basis-based Gaussian sampling therefore applies at v0>=sqrt(n)*omega(sqrt(log n)); choose epsilon=exp(-kappa²) and the larger stated v0 to make the sampler's joint loss negligible. This is not sampling on the unknown ideal J; only R's public basis is used.

The OHCP algorithm requests t bounded by a polynomial in kappa and dimension. Thus exp(t) has polynomial bit length. Truncate the sampled r at exp(poly(kappa)) times its widths with negligible Gaussian tail; approximate T-g(z), canonical transforms and Gaussian arithmetic to absolute precision less than w exp(-kappa²)/max||r||. The induced error before adding G_w is at most w exp(-kappa²), and Gaussian translation then gives negligible TV. This requires polynomial bits even at the largest multiplier width. Applying the common finite observation kernel after this step preserves the TV estimate. A discrete approximation to a continuous law is not asserted to be close in raw TV; the finite observation kernel and Gaussian translation are essential.

These finite implementation claims, including the exact sampler theorem and adaptive query count, remain review obligations. The analytic core is more explicit than a completed finite-bit reduction. No claim is made that an arbitrary ideal can be transferred to D<=2^(rho n), or that bounded-index BDD is a standard worst-case hardness premise.

## 8. Conditional downstream interpretation

A fixed binary-recovery algorithm can furnish pointwise D_J if the fractional-source lossiness theorem is uniform in J. An average-over-Gen distinguisher would not suffice for the uniform BDD conclusion. B's Gaussian-rounding kernel and A's lossiness composition are separate dependencies and must be reviewed independently.

The standard quantum BDD-to-DGS lemma, if applied after completing the finite BDD oracle, would sample on L*=conjugate(J)/(nq) at width sqrt(n)/(sqrt(2)d0). Scaling by nq and conjugating would give D_J at width n*q*sqrt(n)/(sqrt(2)d0). This is an absolute-width consequence for the same restricted J family. It does not supply the missing reduction from arbitrary worst-case ideals into that family.
