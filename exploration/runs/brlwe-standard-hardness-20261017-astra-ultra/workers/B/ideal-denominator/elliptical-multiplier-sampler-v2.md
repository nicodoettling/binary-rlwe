# Finite elliptical integer-Gaussian sampler for the multiplier oracle, v2

Status: REPAIRED-PENDING-RECHECK auxiliary lemma. The runtime defect is preserved in elliptical-sampler-runtime-defect-v1.md; v1 remains immutable. Constants and statistical laws are unchanged. This is an implementation extension of gaussian-periodic-proof-v2.md, not a source-hardness theorem. It concerns the public ring lattice R itself and supplies no short ideal basis.

## Statement in coefficient coordinates

Let V be a positive definite Gaussian width-squared matrix on R^n. Let a>=max(1,sqrt(log(8n/epsilon)/pi)) and suppose V>=2a²I. Put C=V-a²I. Assume V, and hence a square root of C, can be computed to p-bit accuracy in time polynomial in p and the declared parameter bit lengths. Rational positive definite V is a sufficient case. Let 0<epsilon,nu,zeta<=1/4 and xi>0.

There is a finite randomized expected-polynomial-time sampler for an integer vector E whose distance from

    D_(Z^n,V)(e) proportional to exp(-pi e^T V^-1 e)

is at most

    epsilon/(1-epsilon) + 4pi xi/a + zeta + n nu.

Runtime is expected polynomial in n and the TOTAL binary encoding length of V, a, epsilon, nu, zeta and xi, including the complete numerator and positive denominator of every rational input and any separately supplied precision parameter. For a computable nonrational matrix representation, its declared square-root approximation algorithm and cost are additionally part of the input hypothesis. Numerical magnitude logarithms do not replace these encoding lengths. The cost is polynomial in the logarithm of the largest Gaussian width and the full input length, rather than in the width itself.

The sampler first produces a rational Hhat coupled to continuous H~D_C with ||Hhat-H||_1<=xi except with probability zeta. It then samples each integer E_i by the finite scalar sampler in gaussian-periodic-theorem-v2.md at width a and center Hhat_i. Only the public integer lattice is involved.

## Exact normalizer comparison

Consider first ideal H and the exact product integer kernel D_(Z^n,a,H). Their joint law is

    p(h,e)=g_C(h) rho_a(e-h)/rho_a(Z^n-h).

Define the alternative normalized joint law proportional to g_C(h)rho_a(e-h). Gaussian convolution gives its E marginal exactly D_(Z^n,V), including the correct discrete normalizer. Its H marginal is g_C reweighted by rho_a(Z^n-h), divided by the ACTUAL expectation of that theta function under g_C.

Since a>=eta_epsilon(Z^n), the theta factor divided by a^n lies in [1-epsilon,1+epsilon], uniformly over every h. The joint distance, and hence the output distance, is at most epsilon/(1-epsilon). This is one reweighting, not an assertion that discrete and continuous Gaussian convolution is exactly Gaussian. No condition on the largest eigenvalue of C is used.

The uniform scalar center bound already proved in gaussian-periodic-proof-v2.md gives a product-kernel distance at most (4pi/a)||Hhat-H||_1. Averaging over the coupling and its exceptional event adds at most 4pi xi/a+zeta. Replacing the exact scalar kernels by the finite samplers adds at most n nu. This proves the stated bound.

## Constructing the finite continuous approximation

Choose B with BB^T=C and sample an ideal standard Gaussian X, so H=BX. Couple a finite inverse-CDF approximation Xhat to X so that each coordinate error is below a chosen dyadic eta except with total probability at most zeta/2. The scalar Gaussian tails permit restricting |X_i|<=T with another failure probability at most zeta/2, where T is polynomial in sqrt(log(n/zeta)). Approximate B entrywise by a rational Bhat and set Hhat=Bhat Xhat.

On the good event,

    ||Bhat Xhat-BX||_1
      <= n² ||Bhat-B||_max T + n² ||Bhat||_max eta.

Choosing the two precisions so that each displayed term is at most xi/2 suffices. The required number of bits is polynomial in log(1+||B||), log(1/xi), n and log(1/zeta), even if ||B|| is exponentially large. C>=a²I makes its smallest eigenvalue bounded away from zero. Standard rational Cholesky/square-root approximation therefore uses polynomial precision and time; no unbounded condition number is being hidden. Scalar inverse-CDF evaluation on a truncated interval likewise takes polynomial bit complexity. The proof uses a coupling and a smooth subsequent integer kernel, not the false claim that a discrete approximation is close to a continuous law in raw total variation.

## Application to canonical multiplier widths

For power-of-two cyclotomics, the canonical embedding equals sqrt(n) times an orthogonal transformation of coefficient coordinates. If the desired canonical multiplier widths are v_i, the coefficient width-squared matrix has eigenvalues v_i²/n. It is therefore enough to choose

    v0 >= 2sqrt(n) a,  and v_i>=v0 for every embedding.

For the proposed multiplier hidden-center oracle, v_i=v0 outside one conjugate pair and v_j=v0 exp(t) on that pair, with t>=0. The largest width has logarithm O(log v0+t), so a polynomial bound on the oracle logscale gives polynomial bit complexity. The finite output multiplier remains an EXACT element of R; therefore its cancellation of lattice points modulo qJ^-1 is exact even though its probability law approximates the ideal elliptical Gaussian.

For Q adaptive oracle calls, each using k independent multipliers, set the per-multiplier error above to at most delta_impl/(Qk). A sequential coupling then bounds the change in the entire adaptive transcript by delta_impl. This prescription requires an actual upper bound Q from the implemented hidden-center routine; it does not declare an unspecified numerical error negligible without charging it.

This lemma removes the need to import a separate correlated lattice-Gaussian sampler for this particular public ring lattice. It does not by itself complete the hidden-center theorem, the common finite observation interface, or the missing standard reduction to low-index ideals.
