# Gaussian-to-binary change of measure: scope and modular correction

2026-10-17. PROVISIONAL independent derivation. No experiment. This audits coordinator/normalform-binary-test-v1.md; it does not assume source hardness or rule out adaptive reductions.

## Exact favorable restriction calculation

Let P_t on Z have density proportional to exp(-pi(x-1/2)^2/t^2), and let P=P_t^n. Write E={0,1}^n and p=P(E)=p_t^n. Symmetry makes Q=P conditioned on E exactly uniform on E. The two outside points -1 and2 have relative mass exp(-2pi/t^2) compared to0 and1, giving

    p <= (1+exp(-2pi/t^2))^(-n).

For fixed positive t this decays exponentially. If p>=n^(-C), then n log(1+exp(-2pi/t^2))<=C log n, which implies exp(-2pi/t^2)=O(log n/n), hence t^2<=2pi/(log n-log log n-O(1)). This is a necessary condition, not a sufficient imported hardness regime.

On E, Q/P=1/p. For every order alpha>1,

    sum_x Q(x)^alpha P(x)^(1-alpha)=p^(1-alpha),
    D_alpha(Q||P)=-log(p).

Thus the exponentiated Renyi divergence is1/p, independent of order. The reverse divergence D_alpha(P||Q) is infinite because P has mass outside E. If the data-generating kernel given the secret is exactly the same in both laws, these identities also hold for the joint law including the latent secret, public multipliers, errors and algorithm coins. A recovery algorithm whose outputs always lie in E has success at most p under P. Therefore optimizing the Renyi order does not remove the direct-restriction loss. Marginalizing out the secret can reduce divergence substantially; this is not a lower bound on the distance between the PUBLIC transcript distributions, and is not a barrier to a different simulation.

The actual centered normal-form D_tau secret conditioned on{0,1}^n is not uniform binary. Its masses at0 and1 differ by exp(-pi/tau^2). The half-centered calculation is favorable but hypothetical unless an explicit transformation supplies that law and the response equations. Translating an integer-centered secret by a residue representing1/2 does not by itself produce the half-centered integer Gaussian.

## Integer lifts versus the actual mod-q secret

A normal-form oracle recovers e_0 MODULO q. The literal event e_0 in{0,1}^n is smaller than the event e_0 modq in{0,1}^n. Consequently the raw integer p_t bound cannot automatically upper-bound success in the modular recovery problem. For the half-centered distribution the correct one-coordinate branch mass is

    p_(t,q) = 2 sum_(k in Z) exp(-pi(kq-1/2)^2/t^2)
                  / sum_(z in Z) exp(-pi(z-1/2)^2/t^2).

The wrapped masses at residues0 and1 are equal by x -> 1-x; the favorable restriction/Renyi formulas remain valid with p_(t,q)^n. Any substitution p_(t,q)≈p_t requires a tail estimate. This is a scope correction to the integer calculation, not a rejection of the coordinator's separately stated finite-modulus bound.

For centered D_t modulo odd q, define h=max_a P[X modq=a]. Poisson summation of the shifted one-dimensional Gaussian shows that the maximum occurs at residue0: every Fourier coefficient of the periodic Gaussian is nonnegative, so its value is maximized at zero. Hence the exact identity is

    h = rho_(t/q)(Z) / rho_t(Z).

The elementary theta bounds rho_a(Z)<=1+a and rho_t(Z)>=t give h<=1/t+1/q. Therefore, for every bijection phi:R_q->R_q fixed independently of the secret,

    Pr[phi(X) in{0,1}^n] <= min(1, 2^n h^n)
                             <= min(1, (2/t+2/q)^n).

This follows simply by counting2^n preimages and bounding every atom by h^n. For L independently fixed maps, sum the bounds. A random map selected using only multipliers and coins independent of X is covered by conditioning on those data. This finite-modulus statement is exact and includes aliases. For the test tau=n^2 and q>=n^2 it is at most(4/n^2)^n, before multiplying by L.

## What a genuinely adaptive map must prove

If H is arbitrary side information correlated with X and phi_H is a bijection chosen from H, the exact replacement is

    Pr[phi_H(X) in{0,1}^n]
      <= min(1, 2^n E_H max_x Pr[X=x | H])
       = min(1, 2^(n-Htilde_infinity(X|H))).

The unconditional h^n cannot be substituted for the posterior quantity. If H has at most L values, the elementary leakage bound gives E_H max_x P[X=x|H]<=L max_x P[X=x], but ordinary RLWE responses have a far larger transcript space and can carry substantial information about the secret. A polynomial number of samples is not a polynomial-size transcript alphabet. For sequential queries use the posterior conditional on the actual history at each step, and account for the union of successful branches. The fixed-map result does not exclude an oracle-assisted adaptive reduction.

Any proposed adaptive use of a binary recovery algorithm must still prove that each promised query has the ORIGINAL law: shared iid binary secret, full iid uniform ring multipliers, independent prescribed coefficient errors, and the advertised number of samples. On inputs outside that law the oracle's behavior is unrestricted. In particular, writing X=2Z+B where B is near-uniform parity does not simulate a valid query: the missing term2AZ involves unknown Z. Knowing the correct parity distribution does not generate the needed responses. This is a missing construction, not a general impossibility theorem.

## Implementation and samples

The normal-form arithmetic and unit event in first-candidate-v1.md are exact and require one pivot plus M fresh samples. Repeating designated-pivot trials consumes fresh pivot samples; selecting a favorable unknown Gaussian error by rejection would require observing that error or a justified test. Public acceptance selected from responses can alter the posterior secret and conditional error laws, so its actual accepted joint law must be analyzed. If a sampler or discretizer is delta-close per invocation and K invocations are made, the elementary compositional error is at most K delta; such precision losses must be included in any eventual reduction advantage. None is silently absorbed into the branch probability above.
