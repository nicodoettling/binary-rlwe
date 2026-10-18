# A-FRAC: explicit finite bridge and nonempty width window

Status PROVISIONAL. This companion uses A-FRAC theorem-only-v1.md and proof-v1.md. It composes B-IDEN-GP-T v1 as a separate, still provisional theorem; it is not an independent full proof review of B's implementation.

## 1. One complete parameter choice

Fix rho<1, c>0 and a polynomial sample count k. Put

    ell=ceil(log_2(2nk)),
    tau2=2n²,   t=2n² ell,
    r=w=ell²,   s=sqrt(2) ell²,   L=ell,
    sigma=8 n² ceil(sqrt(kn)) ell^4.

Every ideal J with D<=2^(rho n) has a basis of norm at most n²D^(1/n)<2n², by the proof-only geometry lemma. Further,

    2t s sqrt(kn)L =4sqrt(2)n²sqrt(kn)ell^4 <=sigma.

Thus the exact discrete target completion theorem applies with a numerical tau2 that is independent of J. The target condition q/sigma>=n^c is satisfied whenever the supplied split prime q obeys

    q >= 8 n^(c+2) ceil(sqrt(kn)) ell^4.                 (W1)

If k<=n^a, this is a polynomial lower threshold of order n^((a+5)/2+c)log^4(n). In particular any supplied split-prime family sufficiently above this threshold and still polynomial in n lies inside the analytic window. The target width is polynomial. No step requires q to be exponential in value, although polynomial-bit larger moduli are also allowed. The condition gcd(D,q)=1 remains part of the ideal family.

This is a compatibility result for widths and entropy. It does not assert that an ideal family with a hard GP distribution exists. For example J=R satisfies the geometry and entropy assumptions but its fractional source is easy; such a family cannot serve as the missing hardness premise.

For completeness, the finite arithmetic window is nonempty without a prime-generation assumption. Given any integer threshold T exceeding the right side of (W1), let b=T! and choose any prime divisor q of b^n+1. Then q>T, and b has order exactly 2n modulo q because n is a power of two and b^n=-1. Hence q=1 mod2n. Moreover log_2 q<=n log_2(T!)+1=O(nT log T), polynomial for polynomial T. This only proves existence of a suitable polynomial-bit supplied modulus; it does not claim that finding the indicated prime divisor is efficient. Efficient generation of a particular polynomial-value split-prime family is a separate public-parameter choice. No factoring algorithm is assumed inside our reduction.

## 2. Explicit negligible analytic losses

The source-tail term is

    delta_tail <=4kn exp(-pi ell²).

For x>0,

    kappa(x)<=2exp(-pi x)/(1-exp(-3pi x)),

using j²>=1+3(j-1). Therefore

    Delta=(1+kappa(3ell²/4))^n-1

and eta are negligible for polynomial k. The product entropy term satisfies rho_t(Z)>=t by Poisson summation, so

    beta <=min(1,2^(-(1-rho)n) exp(n/t))
          =min(1,exp(-(1-rho)n log(2)+1/(2n ell))).       (W2)

This is exponentially small for fixed rho<1. It is the actual binary-secret guessing bound, not a Shannon entropy surrogate.

For B's finite bridge choose

    epsilon_b=nu=2^(-ell²),    P=2^(2ell²).

These parameters have polynomial bit length. Since ell>=2 and n<=2^(ell-1), r=ell² satisfies B's explicit sufficient smoothing inequality r>=max(1,sqrt(log(8n/epsilon_b)/pi)). The full bridge comparator is EXACT uniform, even with its finite dyadic scalar sampler and fallback. Its planted loss is

    delta_bridge =2k epsilon_b/(1-epsilon_b)
                   +2pi kn/(P r)+kn nu.                 (W3)

All terms are negligible. The finite torus grid is h_J=1/(DP), with sample coordinates in h_J Z^n/qJ^-1. Its representation length is polynomial even when D is exponential in n. The input is a rounded continuous Gaussian versus exact uniform finite-group distribution; that is the precise source problem, not an exact real oracle implicitly supplied to a machine.

Use an approximate scalar sampler for the TARGET integer D_sigma law with error at most nu per coordinate. B's explicit finite scalar sampler, with center zero and width sigma, is one available construction, subject to the same independent implementation review. Product coupling bounds delta_wrap by kn nu. Combining (F1) with B's finite endpoint statement gives

    epsilon <= Adv_(GP_P) + delta_tail + beta + eta
                +2k epsilon_b/(1-epsilon_b)
                +2pi kn/(Pr)+3kn nu.                    (W4)

This bound concerns the executable reduction with an approximate target sampler, while epsilon is recovery success on the mathematically exact discrete target. An externally approximated GP_P challenge carries its own additional total endpoint distance, which is not hidden in (W4).

The normalized source width is w/q=ell²/q in coefficient norm, or sqrt(n)ell²/q in the full canonical embedding. The source lattice Gaussian width is s=sqrt(2)ell² in coefficient norm. These are distinct from the target sigma and the proof-only Gaussian width t.

## 3. Full endpoints and runtime

Pointwise for each admissible public J, the executable reduction receives k samples from GP_P. It uses B's public map to obtain k ring elements A_i. Then it samples n fresh uniform bits S and independent approximate scalar target Gaussians, calls Rec on the k completed samples and checks the returned vector against that same S. Its ideal comparator is the original target distribution, with J either consistently retained or consistently discarded. B's actual finite bridge preserves that exact multiplier comparator. Target sampler approximation is the only comparator loss in (W4).

The planted bridge is within (W3) of the shared-J, conditionally iid a_i~D_(J^-1,s) source. The wrapper uses exactly the same S and target noise law in this world. In the analysis alone, an auxiliary G~D_(J,t) and covariance-completing H explain its small actual-secret success. Those random variables, their basis witnesses and the good-event predicate are never sampled or tested by the reduction.

The full algorithm uses one Rec call, k GP input samples, B's ordinary ideal arithmetic and scalar samplers, plus k ring multiplications and an equality test. Runtime is expected polynomial in the supplied basis/input bit lengths, n,k,log q,log P and the scalar-sampler precision. No inverse-ideal Gaussian sampler, short-basis oracle, factoring oracle, or real-valued computation is implicitly available.

If Rec is the original binary-recovery algorithm without a J input, the reduction simply ignores J when invoking it. Its baseline epsilon is then the same for every admissible J. Thus (W4) supplies a pointwise GP_P distinguisher advantage epsilon minus the displayed losses. This is stronger than an average over Gen but still does not prove GP_P hard or solve arbitrary-lattice BDD. C's separate source-to-standard-problem investigation must establish that next edge with its precise radius and family restrictions.
