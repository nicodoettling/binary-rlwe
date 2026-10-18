# Proof and finite sampler for switch-gaussianize-theorem-v1

2026-10-17. PROVISIONAL; no hardness premise is established.

## A. Full normal-form law

The t pivot multipliers are independent of every error. Selecting the first unit among them therefore leaves the selected error exactly B_n, independent of all untouched multipliers and errors. For each fixed selected unit a_p, multiplication by -a_p^{-1} is a bijection of R_q. Hence the transformed A_i are iid uniform, independent of the selected error and fresh errors. Direct substitution gives

    b_i-a_i a_p^{-1}b_p
     =a_i s+e_i-a_i a_p^{-1}(a_p s+e_p)
     =(-a_i a_p^{-1})e_p+e_i.

This identity requires no property of the original secret. Its uniform law is part of the declared source, but the algebraic target law holds for any independent original secret if the pivot metadata is omitted. On the comparator, condition on the complete pivot pool and every multiplier. Each untouched b_i is an independent uniform one-time pad, so C_i is independent uniform; this remains true after any independently generated additive noise. The output multipliers are iid uniform by the same bijection. The CRT isomorphism R_q=F_q^n gives unit probability u=(1-1/q)^n, and independent pool trials give u_t. Every nonunit, including zero, goes only to the pool-selection failure logic. There is no undefined inverse branch.

Retaining arbitrary discarded pivot responses would require their actual joint law and is not part of the simulator. This omission is essential: those responses still share the original secret and can reveal combinations of the pivot errors. Only the reduction keeps its original input as private workspace; the recovery oracle receives the frozen target tuple.

## B. Deconvolution and its normalizer

Write p_j=exp(-pi j^2/sigma^2)/Z, Z=sum_j exp(-pi j^2/sigma^2). For j>=0 the sequence p_{j+1+h} is decreasing to zero. Pair consecutive terms of the absolutely convergent alternating sum to see f(j)>=0. Reflection gives f(-1-j)>=0. Also f(j)<=2p_{j+1}, so f is summable.

For every integer x>=1, cancellation of consecutive tails gives

    [f(x)+f(x-1)]/2=p_x.

Reflection gives the same identity for x<=-1. At zero,

    f(0)=2(p_1-p_2+p_3-...) = p_0-delta_sigma.

Consequently the unnormalized convolution with a uniform bit is p-delta_sigma*pointmass_0. Summing this identity gives sum_j f(j)=1-delta_sigma. In particular p_0>=delta_sigma and all displayed output masses are nonnegative. Normalizing proves the exact Q formula. At x!=0 the difference Q(x)-p_x equals delta_sigma*p_x/(1-delta_sigma), while at zero it is its negative total. This proves the exact TV expression.

Poisson summation on Z with the character (-1)^j gives

    delta_sigma = [sigma/Z] sum_{h in Z} exp(-pi sigma^2(h+1/2)^2).

Since Z>=sigma and (h+1/2)^2=1/4+h(h+1) for h>=0, pairing h with -1-h and using h(h+1)>=2h yields

    0<delta_sigma<=2 exp(-pi sigma^2/4)/(1-exp(-2pi sigma^2)).

For sigma>=2 this is below 3 exp(-pi sigma^2/4)<1/2. The positivity here is a theta identity, not a sign guess about a truncated alternating sum. In particular the integer-parity obstruction forbids an exact Bernoulli convolution equal to D_{Z,sigma}; our correction removes exactly the exponentially small parity bias at zero.

## C. A bounded-time finite sampler

We give a deliberately elementary algorithm, polynomial in sigma's value. Let the desired one-coordinate TV error be zeta in (0,1/4). Use unnormalized Gaussian weights r_j=exp(-pi j^2/sigma^2). Let

    L=ceil(log_2(256/zeta)),
    K=2 ceil(sigma^2)+2L.

These integers can be computed by exact rational arithmetic and comparisons with powers of two; no exact transcendental ceiling is needed. K is even, K>=2sigma^2, K>=2L, and K>=20.

Define finite weights on j=0,...,K-1 by

    v_j=2 sum_{h=0}^{K-j-1} (-1)^h r_{j+1+h},
    v_{-1-j}=v_j,

and zero elsewhere. They are nonnegative by the same alternating-tail argument. They can be computed backwards from v_{K-1}=2r_K and v_j=2r_{j+1}-v_{j+1}.

Let v_infinity denote the unnormalized infinite weights (Z times f). On the 2K retained positions each weight differs by at most 2r_{K+1}. Off the support, the total mass is at most 4 sum_{j>=K+1}r_j. Since K>=2sigma^2, consecutive tail terms have ratio at most exp(-4pi)<1/2. Also r_{K+1}<=exp(-2pi K)<=2^{-K}. Thus

    ||v-v_infinity||_1 <= (4K+8) 2^{-K}
                           <=2^{-K/2}<=zeta/256.

For K>=20, 4K+8<=2^{K/2}; this elementary inequality follows at K=20 and its right/left ratio increases thereafter. The mass of v_infinity is Z(1-delta_sigma)>1. Normalizing two nonnegative vectors changes TV by at most their unnormalized L1 difference divided by the reference mass. Thus normalized v is within zeta/256 of F_sigma, and the mass of v is greater than 1-zeta/256>1/2.

Approximate every r_j to absolute error at most zeta/(256K^2). Backwards recurrence then has error at most 2K times this tolerance in each of the 2K positions, so total L1 error is at most zeta/64. Clip negative approximate weights to zero; because exact weights are nonnegative, clipping cannot increase their L1 error. Normalize the resulting nonnegative rational vector. Its TV distance from normalized v is at most zeta/32 (using the exact mass bound >1/2).

Finally round the probabilities down to multiples of 2^{-b}, where b=ceil(log_2(256K/zeta)), and place the remaining mass on one fixed support point. The total rounding TV is at most 2K*2^{-b}<=zeta/128. Sample exactly from this dyadic distribution using b unbiased bits and an integer cumulative table. The sum of the three errors is less than zeta.

All loops have predetermined finite bounds. Approximating pi and exp of rational arguments to the displayed absolute precision can be done by the usual convergent series with range reduction in time polynomial in K, all rational input bit lengths, and log(1/zeta). Here sigma>=2 bounds division away from zero, and the largest exponent argument is O(K^2). Table construction is polynomial in K; sampling requires only a bounded number of random bits and arithmetic operations. There is no unbounded rejection loop. This is an algorithmic existence proof, not an empirical sampling claim.

## D. Products, oracle transfer and validation

Run the finite sampler independently in all Mn coordinates with zeta=eta/(Mn). The product coupling bound charges at most eta. Independently, exact scalar convolution and product coupling bound the full fresh-error law by Mn delta_sigma/(1-delta_sigma) from D_{Z,sigma}^{Mn}. Both statements hold jointly with S and all multipliers because the fresh errors and additive coins are independent of them. Deterministic modular reduction cannot increase TV.

Apply the recovery oracle to the success branch. A coupling with the ideal target loses at most Delta in its success probability. When it returns S=e_p, the algebraic formula for shat is correct. Fresh validation pairs were used nowhere else. Conditional on the comparator's earlier transcript and any candidate shat, each validation response is uniform independent of its multiplier, so its residual is uniform R_q. There are exactly 2^n accepted residuals out of q^n; k independent checks give (2/q)^{nk}. Correct planted recovery passes every check since the original validation errors are bits. This gives the stated advantage. On abort the decision routine always rejects. The direct decision-oracle inequality follows by triangle inequality and the identical abort mass.

Neither this argument nor the scalar sampling construction provides the missing standard-hardness reduction to the declared BE source.
