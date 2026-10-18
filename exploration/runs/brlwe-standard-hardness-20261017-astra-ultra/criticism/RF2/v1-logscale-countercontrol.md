# RF2 explicit control for the v1 logscale gap

Status: PROVISIONAL exact analytic countercontrol, no numerical experiment. It refutes the implication from v1's separately displayed confidence bounds to its claimed OHCP starting-guess decay; it does not refute the existence of a repaired larger confidence parameter.

Take n=2, R=Z[i], J=R, D=1, q=101, w=1, k=1 and delta=0.9. In the centered coefficient fundamental square [-q/2,q/2)^2, let A accept exactly the box [-1,1]^2. The canonical width1 Gaussian has independent coefficient widths1/sqrt(2). A standard Gaussian Chernoff bound gives planted acceptance at least1-4exp(-2pi), whereas Haar acceptance is4/101^2. Their gap exceeds0.9.

Let kappa tend to infinity through integers, v0=8kappa, B=floor(exp(kappa-3)), and T=e=1/B (lambda=0). All quantities are polynomial-bit in the rational target encoding; v0>=2eta_(exp(-kappa^2))(R) for sufficiently large kappa. Put d0=delta/(64v0), as in v1. Then |e|<=d0, and d0<101/4. The Section6 denominator H0 is B, and its separate requirement kappa>=log(B)+2 holds. The Section4 S is constant here, since v0*d0=delta/64 and a0=delta/(128q). Thus every separately displayed v1 lower bound on kappa holds for sufficiently large kappa.

Nevertheless the ACTUAL starting-guess query at t=0.9kappa has selected Gaussian width

    sqrt(1+(v0 exp(0.9kappa)/B)^2) -> 1.

There is only one conjugate pair, so no nuisance coordinates occur. For sufficiently large kappa this width is at most1.1, and A's acceptance minus Haar acceptance is at least

    1-4exp(-2pi/1.1^2)-4/101^2 > 0.95.

The decay bound claimed in v1 at that same permitted logscale would require this gap to be at most

    2exp(-t/kappa)=2exp(-0.9)<0.82.

Contradiction. The error is precisely that the radial profile is evaluated at t+log(|e|/d0), which is still very negative at this t. An additional constant-factor enlargement of kappa relative to the denominator transition, or v2's fixed center shift, avoids this countercontrol.

This uses C's ideal continuous query law, exactly the law for which its proof claims the imported OHCP conditions. Choosing a sufficiently fine common finite observation kernel preserves the strict gap, so the issue is not an infinite-precision distinction. The actual discrete multiplier query is already negligibly close by C's posterior estimate, and cannot bridge the constant gap.
