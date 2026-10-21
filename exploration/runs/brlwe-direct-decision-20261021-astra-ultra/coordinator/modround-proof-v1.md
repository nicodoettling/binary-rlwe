# MR-v1 proof

PROVISIONAL; binds modround-statement-v1.md. All TV comparisons below retain the full batch and shared binary S.

## Scalar Gaussian comparisons

Write g_s(x)=s^-1 exp(-pi*x^2/s^2), the density of continuous G_s, and p_s(z)=exp(-pi*z^2/s^2)/rho_s(Z), the discrete Gaussian law. Since integral |g_s'|=2/s, for any unit-cell partition C_z=[z-1/2,z+1/2),

    sum_z |g_s(z)-integral_(C_z) g_s(x)dx| <= 2/s.

Indeed bound |g_s(z)-g_s(x)| by the integral of |g_s'| between x and z, then sum; every derivative value is counted with weight at most1. Let A=sum_z g_s(z)>0. The difference |A-1| is bounded by that same sum. Since sum_z |g_s(z)/A-g_s(z)|=|1-A|, the L1 distance between D_(Z,s) and rnd(G_s) is at most4/s. Consequently

    TV(D_(Z,s),rnd(G_s))<=min(1,2/s).                (1)

No normalization constant is discarded.

For s>=1 the density of G_s modulo1 is at most2. To see this, Poisson summation gives sum_m g_s(m+x)=sum_l exp(-pi*s^2*l^2) exp(2pi*i*l*x), whose maximum is at x=0. At x=0 it is rho_s(Z)/s. Monotonicity on the positive half line yields rho_s(Z)<=1+s, hence the upper bound1+1/s<=2. Thus the probability that G_s+c lies within lambda/2 of a half-integer, for 0<lambda<=1, is at most2lambda. Boundary endpoints have zero continuous probability.

Couple E~D_(Z,sigma/lambda) with rnd(G_(sigma/lambda)) using (1); the mismatch probability is at most2lambda/sigma. On a match, |lambda*E-G_sigma|<=lambda/2. Therefore

    TV(rnd(lambda*E+c),rnd(G_sigma+c))
       <=2lambda/sigma+2lambda.

Translation of a density and integral |g_sigma'|=2/sigma give TV(G_sigma+c,G_sigma)<=|c|/sigma. Applying rounding is a deterministic kernel, and (1) then compares rnd(G_sigma) with D_(Z,sigma). By the triangle inequality, if |c|<=n/2,

    TV(rnd(lambda*E+c),D_(Z,sigma))
       <=2lambda/sigma+2lambda+(|c|+2)/sigma
       <=4lambda+(n/2+2)/sigma.                   (2)

This proof uses a coupling separately to bound one conditional law; it does not assume that the coupling mismatch event is independent of G_sigma or a rounding boundary.

## Public law and exact planted identity

For a uniform integer a in {0,...,Q-1}, the cyclic rounding map rnd(q*a/Q) mod q has fibers of size floor(Q/q) or ceil(Q/q). Each fiber is the integer points in a half-open cyclic interval of length Q/q; the fixed tie rule selects exactly one endpoint when needed. Hence its TV from uniform modulo q is at most q/(2Q)<=lambda. All nk input coefficients are independent, so their joint rounded public law is within nk*lambda of uniform.

Set C_i=rnd(lambda*Abar_i) in Z^n and Delta_i=C_i-lambda*Abar_i. Each coefficient of Delta_i is in [-1/2,1/2], with a deterministic endpoint convention. The ring congruence for B_i, and translation-equivariance of rnd under integer shifts, give the exact identity

    B'_i = C_i*S + rnd(lambda*E_i-Delta_i*S) mod q.

All products here are negacyclic coefficient products. Every coefficient of Delta_i*S has absolute value at most n/2 because every coefficient of S is0 or1. Conditional on the entire A bank and S, these shifts are fixed, and the error variables E_(i,j) remain mutually independent. Thus the joint conditional rounded error law differs from the independent D_(Z,sigma) target by at most nk times (2). Integrate over the SAME joint (A,S) law, retain S, and then change only the rounded public law to uniform. The second operation is a kernel from (A',S) using fresh independent target errors; its charge is at most nk*lambda. The resulting planted bound is exactly the one stated.

In the comparator all2nk coefficients of A,B are independent uniform modulo Q; rounding gives a product law within2nk*lambda of the uniform q comparator. A Boolean expectation changes by at most TV, so adding the two endpoint bounds proves (MR). The two final guards bound each of its two summands by epsilon/8, giving gap error at most epsilon/4. All conclusions hold conditional on any fixed metadata; mixing different Q values with the same laws in both worlds preserves them. No product of adaptively conditioned marginal probabilities is used.
