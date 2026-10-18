# D-R1: anisotropic joint law and output combinations

Frozen 2026-10-17. Status PROVISIONAL, new mathematics pending review. This is a constructive conditional interface, not source hardness or an impossibility theorem. It follows the explicit request to test the feasible covariance F just above a²HH^T. No new experiment was run.

## 1. A feasible full joint law

On public pivot success write H=[−R,I_J], dropping unused auxiliary columns, with J=mn and R the stacked coefficient multiplication matrices of the m fresh ratios. Let a²>=2eta_epsilon(Z^(n+J))² and t=2a. Set A=t²I_(n+J) and

    F_R=t² HH^T=t²(I_J+RR^T).

Because H has full row rank,

    G=(A^-1+H^T F_R^-1 H)^-1
      =t²(I−P_row(H)/2)>=2a²I.

Thus the repaired two-normalizer argument in audit-v2.md applies pointwise in R with V=G−a²I>=a²I. It simulates the ideal pair E~D_sqrt(A), f~D_sqrt(F_R), Y=HE+f, where E and f are independent conditional R. The source endpoint is

    (R,T,C)=(R,T,U−f mod q),

with T uniform and independent of R, U_j iid uniform I_T conditional R,T, and f~D_(Z^J),sqrt(F_R) independent of U,T conditional R. Its marginal after forgetting R is a mixture of these ellipsoidal Gaussians. It is not a fixed spherical source. The simulation error is at most2epsilon/(1−epsilon)+delta_num, with fallback handled as before. The uniform-input endpoint is exactly (R,T,Unif(R_q^m)), even retaining the Gaussian simulation coins specified in the earlier audit. No simulation theorem is needed for that comparator.

F_R has J−n eigenvalues t² when R has full column rank; its remaining eigenvalues are t²(1+s_i(R)²). The rank of the *large contribution* RR^T is at most n. The full noise covariance is positive definite.

The exact conditional finite-modulus density is

    Pr[C=c | R,T]
      = |I_T|^(−m) sum_(u in I_T^m)
          sum_(z in Z^J: z mod q=u−c) rho_(F_R)(z) / Z_(F_R)(0).

Every normalization and latent/public variable appears explicitly. Forgetting R averages this density over its actual public distribution. A low-rank exponent contribution alone does not evaluate that mixture's total variation or make its masks short.

## 2. A tempting representation that is not justified

If X~D_t^J and Y~D_t^n are independent integer Gaussians, then X−RY has a marginal whose exponent matrix is F_R but whose weight also includes a shifted theta factor with parameter

    P=t²(I_n+R^TR)^−1.

For dense R of size q, lambda_min(P) can be of order t²/q², far below smoothing. Therefore neither equality nor a negligible comparison with D_sqrt(F_R) follows. The unit-pivot uniformity argument for independent integer Y cannot simply be transferred to this anisotropic Gaussian. The same issue affects an assertion that all broad noise is exactly a hidden ring multiple RY modulo q.

## 3. Public integer combinations: both endpoints

Let K=K(R) be a public integer coefficient map corresponding to a p-by-m matrix over Z[X]/(X^n+1). Assume it depends only on R (or on other declared public data), and its reduction modulo q has full row rank over R_q, meaning rank p in every CRT coordinate. Then K maps uniform R_q^m exactly to uniform R_q^p. It maps I_T^m onto I_T^p for every T, so KU is exactly iid uniform I_T conditional R,T, and is independent of Kf conditional R,T. Consequently postprocessing the source gives

    (R,T,K C)=(R,T,U'−Kf mod q),

while the actual comparator stays exactly uniform. On a public rank-failure branch an explicitly uniform fallback preserves that comparator but changes the planted mixture and must be charged. If K depends on T and succeeds with T-dependent probability, the source's posterior T law must also be tracked; it cannot silently remain uniform. The simple R-only full-CRT-rank condition avoids that issue.

To cancel the large exponent contribution it suffices to have **K R=0 as an integer/real matrix**, not merely modulo q. Then

    K F_R K^T=t² K K^T.

The distinction matters because f is an actual integer ellipsoidal Gaussian, not the unjustified independent convolution in Section2. Congruence cancellation of a hypothetical integer latent Y does not cancel the actual Gaussian exponent.

A rational real projection onto ker(R^T) is not automatically a map on the q-torus: changing a representative by qz changes its image by qKz, which need not vanish modulo q. Replacing denominators with modular inverses changes the integer lifts and the relevant real noise norms. This must be handled as a new channel, not identified with a short real projection.

## 4. Exact fiber density and a useful smoothing lemma

The pushforward Kf is not automatically D_sqrt(KF_RK^T). Let K be a full-row-rank integer p0-by-J matrix, Lambda=K Z^J, L=ker(K) intersect Z^J, and S=K F_R K^T. For each v in Lambda choose an integer lift z_v and put x_v=F_R K^T S^-1 v. Since Kx_v=v, z_v−x_v lies in ker K. Completing the quadratic form along each fiber gives the exact unnormalized mass

    Pr[Kf=v] proportional to rho_S(v)
        sum_(l in L) exp(−pi ||F_R^(−1/2)(z_v−x_v+l)||²).

Thus Kf is the discrete Gaussian on Lambda with exponent S reweighted by the displayed fiber theta normalizer. Its normalizing denominator is the expectation of that factor under the same Gaussian on Lambda.

There is a favorable special case. Assume R is a full-column-rank J-by-n integer matrix, KR=0, and ker(K)=im(R) over the reals; equivalently K has exactly J−n independent real rows. Then the fiber lattice L contains R Z^n. In the whitened fiber subspace, the lattice B=F_R^(−1/2)R Z^n has Gram matrix

    B^T B=R^T F_R^-1 R
      =t^(-2) Q(I+Q)^−1 <=t^(-2)I,
    Q=R^T R.

Its dual has squared norm form (B^TB)^−1>=t²I. Since F_R^(−1/2)L contains B, its dual is a sublattice of B's dual. Hence its nonzero dual Gaussian mass is at most sum_(z nonzero in Z^n)exp(−pi t²||z||²). If t>=eta_epsilon(Z^n), Poisson summation makes every fiber factor, divided by the fiber's fixed covolume reciprocal, lie in[1−epsilon,1+epsilon], uniformly in v. Normalized reweighting then proves

    TV(Kf, D_(Lambda),sqrt(S)) <= epsilon/(1−epsilon),
    S=t² K K^T.

This lemma keeps the entire lattice Lambda, rather than replacing it with Z^(J−n). It holds pointwise in R,K. The proof does not assume a basis of the primitive fiber lattice is efficiently known, and it does not by itself construct K. It is a prospective distribution lemma, pending nonauthor review.

Centered discrete Gaussians on any lattice have an exact useful moment bound. Completing the square and using that a centered theta sum is maximal among its translates gives

    E exp(2pi<v,Z>) <= exp(pi v^T S v),
    Z~D_(Lambda),sqrt(S).

Thus when ||K|| is small, this conditional interface would give masks with small directional subgaussian parameters, plus the stated comparison loss. It does not automatically give iid coefficient D_ell masks or the frozen baseline source law.

## 5. The missing short-map construction

For two ring outputs, K=[M_r2,−M_r1] has KR=0 exactly because ring multiplication commutes. It is surjective modulo q whenever r_1,r_2 do not both vanish in any CRT coordinate, an event of probability(1−q^−2)^n for independent uniform ratios. If at least one ratio is nonzero over the integers, R has full real column rank because X^n+1 is irreducible over Q for power-of-two n. Thus the preceding fiber lemma applies on the corresponding full-rank branch. However this K has coefficient size q and norm typically at least order q, so its masks retain width of order aq; it does not solve the source problem. It also leaves only one output. Three or more fresh outputs admit analogous syzygies producing two or more outputs, with the same dense coefficients.

For many outputs, a short K with KR=0 and enough CRT rank would give a concrete improvement through Section4. Finding it is a separate lattice relation problem. The existence of many kernel vectors, a real orthogonal projection, a volume estimate, or a trapdoor generated for different multipliers does not provide an efficient sampler for such K on the actual public ratios. No such construction has been established here. Short relations only modulo q require a different proof from Section4.

## 6. Directional downstream scope

A's response identifies a second distinct rank: the stacked multiplication map M_f from the n-dimensional binary-secret space to mn response coordinates already has rank at most n for every mask tuple, including the original A-ADM interface. In unitary canonical Fourier coordinates its singular values are sqrt(sum_j |f_j(omega)|²). Low rank of the pre-sampling covariance contribution RR^T does not ensure that few of these n frequencies are large after f is sampled.

For Gaussian completion with an auxiliary secret perturbation covariance C, one needs the pointwise PSD domination M_f C M_f^T<=sigma²I while preserving a guessing bound for S+G. The existing isotropic interface pays for the maximum singular value. A directional improvement requires a new cube/lattice guessing bound that charges the actual directions in which C becomes small. Revealing output-determining noise is not an admissible way to obtain that bound. No such replacement is supplied here.

Current frontier: the anisotropic source is a valid candidate distribution after the repaired public simulation; short full-rank integer output relations would conditionally produce smaller subgaussian masks with exact comparator; those relations and a compatible downstream binary guessing argument remain OPEN. Source hardness and the original target foundation remain OPEN. Frozen earlier D theta artifacts are unchanged.
