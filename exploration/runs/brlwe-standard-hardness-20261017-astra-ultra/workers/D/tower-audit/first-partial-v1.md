# D tower audit: first partial

2026-10-17. PROVISIONAL; source hardness remains OPEN. Primary sources were inspected, not imported from survey statements. No experiment was run.

## Exact distributions being compared

Standard source candidate: R_n=Z[X]/(X^n+1), n a power of two, rank k (ordinary RLWE means k=1), modulus q_s, shared s uniform R_(n,q_s)^k, independent multipliers a_i uniform R_(n,q_s)^k, and responses b_i=<a_i,s>+e_i with independent coefficient D_tau errors. Comparator: independent uniform multipliers and responses. Number of samples M is explicit and may be polynomial.

Desired expanded target: S_N=Z[Y]/(Y^N+1), N=n d a power of two, rank exactly1, modulus q_t satisfying the original split/polynomial-modulus requirement, shared coefficient-binary S uniform{0,1}^N, independent full uniform A_i in S_(N,q_t), and B_i=A_i S+E_i with independent coefficient D_sigma errors. Comparator: independent uniform full pairs. The number m of target ring samples is independent of M; identifying one source module response with one full target ring response is not allowed without an explicit map.

An intermediate binary module target has degree n and rank d, secret tuple(s_0,...,s_(d−1)) with independent binary coefficients, uniform a in R_(n,q)^d, and only one response in R_(n,q) per module sample. It is not the rank-one degree-N target above, despite matching secret entropy and multiplier entropy.

## Verified primary module reduction

[Boudgoust–Jeudy–Roux-Langlois–Wen2021](https://cjeudy.github.io/assets/pub/BJRW21_Hardness_bin-MLWE.pdf), Definition1 and Theorem2, preserves ring degree n, modulus q and sample count m while increasing rank k to d>=(k+1)log2(q)+omega(log n), with d<=m<=poly(n). Its error bound grows by n sqrt(2d) sqrt(4n²+1); its stated target uses bounded elliptical continuous dual-torus Gaussian errors, and coefficient-binary dual secrets. The paper gives a power-of-two instantiation at q=5 mod8 in Section3.3. These are actual structured reductions, but they do not lower rank to1 or enlarge the field. Full splitting and exact spherical discrete target noise require separate bridges.

The2023 journal extension *On the Hardness of Module Learning With Errors with Short Distributions* is identified; its publisher abstract still requires at least logarithmic module rank. Full detailed statements are being checked using primary author material. No claim that2021 is the strongest current result is made before that check.

## Concrete tower correlation gap, derived independently

Take S_N=R_n[Y]/(Y^d−X), so Y^N+1=0. Packing d coefficient-binary R_n elements into S=sum_j Y^j s_j indeed gives the exact coefficient-binary target secret. Packing d independent uniform R_n multipliers into A likewise gives a full uniform element of S_(N,q). Those facts alone do not supply all response blocks.

For d=2, write A=a_0+Y a_1 and S=s_0+Y s_1. The required two responses are

    B_0=a_0s_0+X a_1s_1+E_0,
    B_1=a_1s_0+a_0s_1+E_1.

A single rank-two module sample can supply the first equation after a public coefficient permutation/unit twist, but provides no value for the second. Two independent rank-two module samples have independent multiplier rows, whereas the two rows above must be (a_0,Xa_1) and(a_1,a_0). A uniform pair of module rows satisfies those public equalities with probability q^(−2n). Thus naive regrouping/rejection cannot give the full target law at polynomial q and growing n.

More generally, a full degree-nd ring multiplication block is determined by d base-ring elements. An arbitrary d-by-d module multiplier block contains d² independent elements. The ring-multiplication subspace has fraction q^(−n(d²−d)) inside the uniform module matrix space. The equalities are public and exactly testable. Conditioning on them is exponentially unlikely, and calling a recovery oracle on arbitrary grouped blocks does not satisfy the original rank-one target promise. Filling missing response blocks with uniform data preserves a comparator but gives the wrong planted law; reusing one error across blocks also violates the target's independent errors.

This is a gap for direct packing, not an impossibility theorem for all tower/gadget reductions. A new mechanism must generate the missing products with the same unknown secret while preserving the public multiplier correlations and independent target errors. Modulus changes, trace projections and sample amplification must be stated as separate transformations with both endpoints.

## Remaining primary checks

Check the2023 bounded-secret extension and2024 entropic Module-LWE/rank-one modulus-switching statements; distinguish a coefficient-binary target from canonical binary restrictions and from base-q digit-packed secrets. Check any Order-LWE short-secret normal form against its actual Gaussian width, which need not reach binary coefficients. No compatible rank-one binary theorem has yet been verified in this audit.
