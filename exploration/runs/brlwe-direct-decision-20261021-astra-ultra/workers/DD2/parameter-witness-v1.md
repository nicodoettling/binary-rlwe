# DD2-PARAM-v1: noncircular polynomial-value regime

Status: PROVISIONAL parameter witness for the averaged-modulus route, not acceptance of its source-gap or decoding theorem. Frozen 2026-10-21 12:50 UTC. Uses DD1 extraction-theorem-v1, DD2-PRIMES-v1 and the inherited same-J source parameters. Logarithms in exact loop counts are base2 ceilings.

Fix ρ<1 and n≥2 a power of two. Supply k0≥1 and rational0<ε≤1. Let C_L≥1 be one fixed effectively computable absolute integer for the conservative Linnik bound P(a,m)≤C_L m^6. Choose the integer

    B = max(2^20,n,k0,ceil(1/ε),C_L),
    M = B^8,
    Qmin = B^128,
    Qmax = B^1024.

Qmax is a declared upper bound used before the list is made; it is not required to equal the list's largest prime. Set η=ε/64 and use DD1's exact common sample counts with Qmax substituted for q:

    Lcal=ceil(log2(256(n+1)/ε)),
    Ltest=ceil(log2(256Qmax/ε)),
    Ncal=ceil(2048n² ε^(-2)Lcal),
    Ntest=ceil(2048n² ε^(-2)Ltest),
    K=k0(Ncal+Ntest),
    ell=ceil(log2(2nK)),
    σ=8n² ceil(sqrt(Kn)) ell^4.

All these choices precede the prime list and decoder executions. No fixed point is being solved by an implicit iteration.

## 1. Source sample and noise bounds

Since n,k0,ε^-1≤B and log2B≥20,

    Lcal≤10+2log2B≤3log2B,
    Ltest≤9+1025log2B≤1026log2B≤B.

The last inequality holds at B=2^20 and its difference increases thereafter (or follows from the elementary monotonicity of log x/x above e). Hence Lcal,Ltest≤B. Therefore

    Ncal,Ntest ≤ 2048B^5+1 ≤2B^6,
    K≤4B^7≤B^8.

It follows that ell≤2+9log2B≤10log2B≤B, and

    ceil(sqrt(Kn))≤ceil(B^(9/2))≤2B^(9/2)≤B^5.

Thus

    σ≤8B^11≤B^12,    nσ≤B^13<Qmin.

The inherited q≥nσ premise holds for every resulting prime.

## 2. Prime list fits the predeclared upper bound

Use DD2-PRIMES-v1 with M and Qmin above. For its t0=max(1,ceil((Qmin−1)/(2n))) we have t0≤Qmin/(2n)+1. Therefore

    4n(M+n+t0+2)
       ≤4B^9+4B²+2B^128+12B
       ≤3B^128.

The finite construction returns M admissible distinct primes, after gcd filtering, all at most

    C_L(3B^128)^6 ≤729B^769≤B^770<Qmax.

The sample count computed from Qmax is thus a valid common upper choice for every actual q. k0, K and the number of D calls remain distinct resource measures. The extraction field-coin cap uses actual q≤Qmax and a fixed requested ν_ext=ε/64; its logarithmic rejection bound is polynomial in logB, while actual q-guess calls are polynomial in B in VALUE.

## 3. Entropy and prime-collision part of the source guard

DD2-AM1-SNF-v1 gives

    ν = n log n/(2M logQmin) ≤1/(256B^7).

At t=2n²ell and r=t the inherited Gaussian envelope overhead is

    Γ=exp((π/8+1/4)/(n ell))<2.

Consequently Γsqrtν≤1/(8B^(7/2))≤ε/64. If D≤2^(ρn), then

    Γsqrt(D/2^n) ≤2·2^(-(1−ρ)n/2),

which is at most ε/64 once n≥[2/(1−ρ)]log2(128/ε). The full selected-functional source term is then at most ε/32.

The remaining finite guard consists of the inherited Gaussian tail/normalizer/GP endpoint errors evaluated at this K and ell. For fixed ρ<1, k0(n) bounded by any fixed polynomial, and ε(n)^-1 bounded by any fixed polynomial, B is polynomial in n, while ell=Θ(log(nK)) and the errors 2^(-ell²), exp(−c ell²) multiplied by polynomial factors are o(ε). Thus the integrated guard

    Γ[ sqrt(D/2^n)+sqrtν ] + other_charged_errors ≤ ε/8

holds for all sufficiently large powers of two n. The finite theorem must still test or assume its exact displayed guard; this asymptotic witness does not erase small-n failures or certify transcendental inequalities at equality boundaries.

## 4. Meaning and limits

M,Qmin,Qmax,K,σ are polynomial in numerical n,k0,ε^-1 with fixed universal exponents. The enormous exponents are an explicit conservative existence witness, not practical parameters. The ordinary basis encoding remains part of runtime. Effective Linnik constants are fixed theorem constants; no claim about their practical numerical value is made.

The distinguisher premise must hold for the resulting common σ and the actual final modulus list (or for a master list with a separately charged filtering loss). No one-fixed-q advantage is promoted to that premise. This establishes only that the stronger averaged-modulus variant has a nonempty compatible asymptotic regime. It does not establish arbitrary-ideal hardness, useful concrete security, or full-secret recovery.
