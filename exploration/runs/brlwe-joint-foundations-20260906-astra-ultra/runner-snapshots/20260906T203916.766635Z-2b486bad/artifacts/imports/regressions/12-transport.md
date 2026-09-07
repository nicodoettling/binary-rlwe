# C03 quantitative transport calculations

Evidence: fully written small calculations; investigator check, pending the coordinator's separate review. No numerical experiment was run here. These are conditional algorithmic implications, not source-hardness results.

## T0: frozen experiment and finite claims

Let n be a positive power of two, q>1 odd, R_q=(Z/qZ)[X]/(X^n+1), and C={0,1}^n in the coefficient basis. Fix sigma>0 and

    P_sigma(z)=exp(-pi z^2/sigma^2)/Z_sigma,
    Z_sigma=sum_(z in Z) exp(-pi z^2/sigma^2).

All Gaussian coefficients below are independent. Their actual modular distribution is W_(sigma,q)(r)=sum_(z congruent r mod q) P_sigma(z).

The planted source K2 samples independently a_1,a_2 uniform R_q and x,y uniform C, and publishes (a_1,a_2,t=a_1x+a_2y). The planted task returns this original pair (x,y). The any-preimage task may return any (x_hat,y_hat) in C^2 satisfying the public equation. Source instances contain one ring equation and two hidden binary blocks.

Fix an arbitrary randomized algorithm T receiving exactly one pair (A,B). Its target success is

    epsilon=Pr[T(A,Ax+E mod q)=x],

where A is uniform R_q, x uniform C, E has coefficient law P_sigma, and all these variables and T's random tape are independent. No oracle access to additional target samples is assumed. The two reductions below make one invocation of T on the received source instance. Let rho_q=Pr[a_2 is a unit].

Define

    K_0(n,sigma)=((1+exp(2pi/sigma^2))/2)^n,
    tau=pi/sigma^2,
    k_c(sigma)=1+exp(tau)(cosh(2tau)-1),
    K_c(n,sigma)=k_c(sigma)^n.

The uncentered public map has planted success at least rho_q epsilon^2/K_0. The centered public map has planted success at least rho_q epsilon^2/K_c. Either bound also lower-bounds any-preimage success. The mathematical statements use exact Gaussian samples; an implementation with joint Gaussian sampling error eta has corresponding conditional success at least max(0,epsilon^2/K-eta), multiplied by rho_q.

## C03-L1: public normalization and recovery

Test whether a_2 is a unit; abort otherwise. On the unit branch compute

    A=a_2^(-1)a_1,
    C=a_2^(-1)t=Ax+y.

Conditional on each fixed unit a_2, multiplication by a_2^(-1) permutes R_q. Consequently A is uniform and independent of (a_2,x,y), while x and y retain their independent uniform binary laws. The conditioning event uses only a_2; it does not select x, y, A, or a solver outcome.

Given a candidate x_hat from T, reject if it is not binary, and set

    y_hat=C-Ax_hat mod q.

Reject if y_hat is not binary or if the original public equation fails. If x_hat=x then y_hat=y exactly. Conversely, returning the original planted pair requires x_hat=x. Thus planted recovery is exactly the event that the target solver returns the original x, regardless of possible other preimages. Verification recognizes valid preimages, not whether one is the planted preimage. No uniqueness claim or amplification of exact planted success is used.

## C03-L2: general change-of-measure and wrapping

For countable probability laws P,Q with P absolutely continuous with respect to Q, set

    M_2(P||Q)=sum_z P(z)^2/Q(z)=1+chi^2(P||Q).

For every event F, including events using an independent random tape,

    P(F)=E_Q[1_F P/Q]
        <=sqrt(Q(F) M_2(P||Q)),

so Q(F)>=P(F)^2/M_2(P||Q). The numerator is the target law; the denominator is the simulated law.

For a deterministic map f, apply Cauchy–Schwarz separately on every fiber f^(-1)(r):

    (sum_(f(z)=r) P(z))^2/(sum_(f(z)=r) Q(z))
      <=sum_(f(z)=r) P(z)^2/Q(z).

Summing proves M_2(f(P)||f(Q))<=M_2(P||Q). This covers coefficientwise reduction modulo q, without estimating a no-wrap event. Tensor products satisfy M_2(P^n||Q^n)=M_2(P||Q)^n by nonnegative product summation.

Appending an independent variable with the same law under P,Q leaves M_2 unchanged. Appending the solver's random tape is one such operation. Applying the shared map (A,x,e)->(A,x,Ax+e mod q), then evaluating the event T(A,B)=x, is therefore legitimate for the joint secret/transcript law.

## C03-L3: original uncentered integer-Gaussian comparison

The uncentered output is (A,B=C+G mod q) for a fresh G with coefficient law P_sigma. Its error is y+G. Set P=P_sigma^n and Q=E_y[P+y], where y is an independent uniform binary vector and (P+y)(z)=P(z-y).

For every integer vector u, completing the square gives the exact identity

    M_2(P||P+u)
      = Z_sigma^(-n) sum_z exp((-2pi||z||^2+pi||z-u||^2)/sigma^2)
      = exp(2pi||u||^2/sigma^2)
          Z_sigma^(-n) sum_z exp(-pi||z+u||^2/sigma^2)
      = exp(2pi||u||^2/sigma^2).

The last equality uses an integer shift of Z^n, not a continuous-Gaussian approximation. Convexity of v->1/v yields

    M_2(P||Q)
      <=E_y[M_2(P||P+y)]
      =E_y exp(2pi||y||^2/sigma^2)
      =((1+exp(2pi/sigma^2))/2)^n.

By L2, wrapping and inclusion of (A,x) and solver coins preserve this upper bound. Applying it to F={T(A,B)=x} proves conditional planted recovery >=epsilon^2/K_0. L1 recovers the original y; multiplying by rho_q accounts for aborts.

This recovers the requested original formula without a total-variation approximation. For comparison, symmetry and monotonicity make the differences P_sigma(z)-P_sigma(z-1) telescope on either side of the origin, so TV(P_sigma,P_sigma+1)=P_sigma(0)=1/Z_sigma. Mixture linearity and the product TV upper bound therefore give TV(P,Q)<=n/(2Z_sigma), which cannot preserve every nonnegligible success probability for a fixed polynomial sigma merely by subtraction.

## C03-L4: centered improvement with exact scalar identities

Write H=1+X+...+X^(n-1). The centered output is

    A'=2A,
    B'=2C-H+G mod q=A'x+(2y-H)+G mod q.

The scalar 2 is a unit because q is odd, so A' remains uniform and independent of x and y. The original binary secret x is unchanged. Residual coefficients R_j=2y_j-1 are independent uniform signs. The fresh noise G still has width sigma; it is sampled after scaling the source equation, so its width has not been doubled.

Let P=P_sigma on Z and Q(z)=(P(z-1)+P(z+1))/2. Direct substitution gives

    Q(z)/P(z)=exp(-tau)cosh(2tau z)>=exp(-tau).

For every integer k, an integer shift gives

    E_(Z~P) exp(2k tau Z)=exp(k^2 tau).

In particular E cosh(4tau Z)=exp(4tau), whence

    M_2(Q||P)
      =exp(-2tau) E_P cosh^2(2tau Z)
      =exp(-2tau)(1+exp(4tau))/2
      =cosh(2tau).

The direction in this exact identity is Q||P. To obtain the direction needed for target-success transfer, use the pointwise lower bound on Q:

    chi^2(P||Q)=sum_z (P(z)-Q(z))^2/Q(z)
      <=exp(tau) sum_z (P(z)-Q(z))^2/P(z)
      =exp(tau) chi^2(Q||P)
      =exp(tau)(cosh(2tau)-1).

Therefore M_2(P||Q)<=k_c(sigma). Tensorization, wrapping, and L2 applied to (A',x,B') prove conditional success >=epsilon^2/K_c. The same recovery map from L1 uses the original stored A,C (equivalently A=A'/2), and recovers the original y whenever T outputs x. It never needs y to construct the target sample.

The exact scalar reverse moment is also expressible as exp(tau) E_P[sech(2tau Z)]. The bound above avoids estimating this sum. We do not claim the k_c expression is its exact value.

## C03-L5: why the mixture comparison preserves the planted witness

The likelihood comparison retains the original source x as a latent coordinate. It marginalizes y because T sees only (A',B'), and its success event is equality of its output with x. The pointwise implication in L1 then restores the original y from the stored source equation. No fresh candidate for the source secret is sampled, and no computational posterior sampler is assumed.

The full joint law additionally exposing y, C, or the source transcript to T is a different experiment. Conditioning on y destroys the cancellation of the two sign shifts; the centered O(sigma^-4) estimate is not asserted for that expanded transcript. The improved comparison is sufficient for the actual recovery event, and is stronger than a comparison of the public marginal (A',B') alone.

An exact finite distinction between success notions: for n=1,q=3,a_1=a_2=1,t=1, the binary pairs (1,0) and (0,1) have the same public equation. A verified preimage need not be the planted one. Our lower bound evaluates equality with the planted x explicitly and thus does not identify the two notions.

## C03-L6: units for all reference odd moduli

Factor q mathematically as product_(p|q) p^(e_p); no factorization algorithm is required below. For each odd prime p, all roots of X^n+1 have order exactly 2n, because 2n is a power of two and zeta^n=-1. The Frobenius orbit of each root consequently has length

    d_p=ord_(2n)(p).

The polynomial is squarefree modulo p since p does not divide n. It has n/d_p irreducible factors of degree d_p. By CRT, a uniform element modulo p is a unit with probability (1-p^(-d_p))^(n/d_p). A class over p^(e_p) is a unit precisely when its reduction modulo p is a unit: a modular inverse lifts because the error lies in the nilpotent ideal pR. Thus

    rho_q=product_(p|q) (1-p^(-d_p))^(n/d_p).

Since p^(d_p) is 1 modulo 2n and exceeds 1, p^(d_p)>=2n+1. Bernoulli's inequality gives each distinct-prime factor at least

    1-n/(d_p p^(d_p)) >=1-n/(2n+1)>1/2.

Writing omega(q) for the number of distinct prime divisors, we obtain

    rho_q >=2^(-omega(q)) >=q^(-log_3(2)).

The second inequality follows from 3^(omega(q))<=q. Hence abort loss is at most polynomial for all odd q<=n^C. For prime q, the simpler general factor union bound gives rho_q>=1-n/q; in the frequently used q>2n subclass this is at least 1/2. No negligibility of abort is needed for an inverse-polynomial success reduction.

Public computation of a_2^(-1) does not need q's prime factors: form its n-by-n multiplication matrix M, compute det(M) over the integers and gcd(det(M),q), and, when this gcd is 1, use the modular inverse of the determinant and adjugate to invert M modulo q. Its action on the multiplicative identity yields a_2^(-1). These have polynomial bit complexity in n and log q.

## C03-L7: polynomial parameters and sample budget

For growing sigma,

    log K_0 = n(tau+log cosh(tau)) = pi n/sigma^2 + O(n/sigma^4),
    log K_c = 2pi^2 n/sigma^4 + O(n/sigma^6).

The stated original certificate has polynomial denominator exactly in the asymptotic regime n/sigma^2=O(log n); the centered certificate has polynomial denominator when n/sigma^4=O(log n). These characterize these displayed guarantees, not an impossibility threshold for all other transports or the exact wrapped moment. The latter condition is sigma=Omega((n/log n)^(1/4)); sigma^4=Omega(n) gives a constant likelihood-loss factor before unit aborts. For sigma=n^alpha, alpha>=1/4 suffices for the centered certificate; alpha>=1/2 suffices for the original one. Below these thresholds the particular displayed denominator is superpolynomial, which by itself is not an attack or an impossibility theorem.

If epsilon>=n^(-a), q<=n^C, and log K_c<=b log n, source success is at least n^(-2a-b-C log_3(2)). Thus every nonnegligible one-sample success transfers nonnegligibly in this regime. The reference small-noise constraint q/sigma>=n^c must also hold. It can coexist with these conditions, but no hardness claim applies uniformly throughout the resulting parameter region.

This reduction supplies exactly one ring sample. Repeated additions of Gaussian G keep A fixed and reuse the same hidden y; rotations and known ring multiples retain algebraic dependence. They are not independent target samples. Independent K2 instances have independent x and therefore also do not supply many samples sharing the reference target secret. Hardness for the one-sample target alone would not establish hardness for solvers allowed polynomially many samples.

For an explicit polynomial-time implementation, assume sigma^2 has a polynomial-bit rational description and sigma<=n^C, as appropriate for the reference polynomial-width family. A truncated discrete Gaussian on |z|<=ceil(n sigma), with polynomially many precision bits and negligible rounding error, gives negligible total variation error jointly across n coefficients. Enumerating this polynomial-size interval and sampling dyadic approximations is sufficient; no specialized exact sampler theorem is required. For any chosen inverse-polynomial loss target, approximation error can instead be bounded explicitly by eta and charged as stated in T0.

## Claim dependencies and regressions

| Claim | Dependencies | Investigator status |
|---|---|---|
| L1 normalization and planted recovery | Ring algebra; conditioning only on a_2 | Fully written calculation |
| L2 change of measure | Cauchy–Schwarz; nonnegative summation | Fully written calculation |
| L3 original bound | L1,L2; integer Gaussian shift; convexity | Fully written calculation |
| L4 centered bound | L1,L2; two explicit integer Gaussian shifts | Fully written calculation |
| L5 joint witness interpretation | L1,L2,L4 | Fully written calculation |
| L6 unit probability | Frobenius orbits; CRT; integer arithmetic | Fully written calculation |
| L7 asymptotic/runtime statement | L3,L4,L6; effective sigma | Fully written calculation |
| Independent source hardness | Separate source-regime bridge | Unresolved; no such bridge supplied |

Mandatory regressions checked by hand: likelihood orientation (P=(1,0), Q=(theta,1-theta), F={0} attains Q(F)=P(F)^2/M_2(P||Q)); planted versus verified preimage at the n=1,q=3 example; q composite unit conditioning; modular wrapping without a no-wrap premise; prohibition on exposing y to T; and prohibition on counting rotations as independent samples. No sequential conditioning or product of adaptive marginal event bounds is used. Tensorization is solely over independently sampled coefficients under a frozen product error law. The cached-prefix sequential regression is therefore not a premise of this product calculation. No ACCEPT certification or exhaustive numerical search is claimed.
