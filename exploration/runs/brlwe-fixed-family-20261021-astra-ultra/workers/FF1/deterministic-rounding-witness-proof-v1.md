# FF1-MR-WITNESS-v1 proof candidate

Binds deterministic-rounding-witness-statement-v1.md. All independence is conditional on the single shared S; no product claim is made after a posterior selection.

## Exact channel law

For a uniform scalar torus coordinate A, C=rnd(A) modq is uniform, and Delta=rnd(A)-A is uniform on [-1/2,1/2), up to irrelevant endpoints, independent of C. Apply coefficientwise. Translation equivariance of rnd under integers gives the exact residual

    B'-A'S = rnd(G-Delta S) modq.

Conditional on S, the complete (A',Delta,G) triples are independent over samples; A' is independent uniform and independent of (Delta,G). Coefficients of Delta and G are independent before applying ring multiplication. No independence of the final residual coefficients is asserted.

Let w=wt(S). The coefficient zero of Delta S is a signed sum of exactly w independent centered uniform unit-interval variables, since negacyclic multiplication only selects/signs coordinates in that row. Thus its distribution depends on S only through w. Put t=1/q, sinc(x)=sin(x)/x with sinc(0)=1. The conditional channel expectation of Z=cos(2pi(B'-A'S)_0/q) is

    mu_w = sum_{l in Z} exp(-pi sigma^2(t+l)^2)
                         sinc(pi(t+l))^(w+1).              (1)

To verify (1), the quasi-periodic function exp(2pi i t rnd(x)) equals exp(2pi i t x) times a periodic function with Fourier coefficients sinc(pi(t+l)). Integration against the smooth density of G plus the independent uniform sum justifies the absolutely convergent integrated Fourier series: the Gaussian factor dominates every coefficient. Each uniform variable contributes another sinc; negacyclic signs disappear by symmetry. The real expectation is the displayed real sum.

For the exact coefficient discrete Gaussian target, Poisson summation with its actual normalizer gives

    mu_* = [sum_{l in Z} exp(-pi sigma^2(t+l)^2)] /
           [sum_{l in Z} exp(-pi sigma^2 l^2)].              (2)

The nonzero-l numerator terms in (1)/(2) have total absolute mass <=Rt; the nonzero-l denominator terms in (2) have mass <=R0. These bounds follow from (j-t)^2>=(1-t)^2+(j-1) for j>=1, and j^2>=j. They are deliberately loose positive geometric bounds.

Set m=w+1<=n+1 and a=1-sinc(pi/q). For q>=4, Taylor's alternating bound gives a>=pi^2/(7q^2), while a<=pi^2/(6q^2). Since q>=max(4,n), ma<=1. Bernoulli gives (1-a)^m<=1/(1+ma), hence

    1-sinc(pi/q)^m >= ma/(1+ma) >= m pi^2/(14q^2)
                              >= m/(2q^2).

Also exp(-pi sigma^2/q^2)>=exp(-pi/n^2)>1/4. Equations (1),(2), with both normalizers retained, therefore imply

    mu_*-mu_w >= m/(8q^2)-R0-Rt >= 1/(16q^2)=d.            (3)

## Whole-batch witness

Observe the empirical average of Z_i over i=1,...,k, retaining S to compute each residual. Under P, the Z_i are iid conditional on S with mean mu_*; under C, they are iid conditional on S with mean mu_w<=mu_*-d. Their range is [-1,1]. The event that their average is >=mu_*-d/2 has P-probability at least 1-exp(-kd^2/8), and C-probability at most exp(-kd^2/8), by bounded independent-variable concentration CONDITIONAL ON EACH S. Integrating over the unchanged uniform S preserves these bounds. Their difference proves (W1). This is not a product of marginal success probabilities and involves no posterior-selected secret.

## Finite-Q convergence

Let lambda=q/Q. Couple A_Q uniform on {0,...,Q-1} with A_cont=lambda(A_Q+V), V uniform on [0,1), independently coefficientwise. Then A_cont is exactly uniform on [0,q), and |lambda A_Q-A_cont|<=lambda. A public rounding coordinate differs only in a boundary strip of measure at most2lambda under uniform torus measure. Charge 2knlambda.

For each coefficient couple E_Q~D_(Z,sigma/lambda) with rnd(G_(sigma/lambda)) as in accepted MR-v1's scalar normalized lemma. The mismatch charge is <=2lambda/sigma; on a match |lambda E_Q-G_sigma|<=lambda/2. Union bound over kn coefficients costs <=2knlambda/sigma. On all matches, each unrounded response coordinate differs from the continuous response by at most(n+1/2)lambda. Conditional on A_cont,S, G_sigma modulo1 has density <=2 (MR-v1), so being within this distance of a rounding boundary has probability <=4(n+1/2)lambda. This bound is applied to the original continuous Gaussian law and unioned with the coupling mismatch; no independence of those events is assumed. Charge <=4kn(n+1/2)lambda. The total is <=8kn(n+1)lambda, proving (W2). All ring/modulus representative changes are integer translations before rnd and do not affect this coupling.

The comparator statement is exact in the continuous channel because rounding a uniform coefficient torus point produces a uniform residue independently in every coordinate and sample.

## Pending audits

Finite-support conditional-law control is registered separately. This analytic candidate has not received nonauthor review. CP-1 does not contradict it: the proof conditions on S before an iid sample concentration estimate and never infers a sequential product after selected observations. The historical retained-S/full-batch regressions apply directly. Sample-only efficient separation remains outside the claim.
