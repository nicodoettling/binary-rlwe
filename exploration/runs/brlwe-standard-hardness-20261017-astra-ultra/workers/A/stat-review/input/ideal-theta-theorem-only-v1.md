# D-THETA v1: statistical uniformity of rounded ideal points under an elliptical floor

Status: **PROVISIONAL**. This is a frozen analytic statement and scoped composition obstruction, not a computational hardness result or a general impossibility theorem.

Let n>=2 be a power of two, K=Q[X]/(X^n+1), R=Z[X]/(X^n+1), and q>=2 an integer. Let P be a nonzero integral R-ideal containing qR, and Q=qP^-1. Let u be a nonzero element of Q^-1. The canonical embedding σ lists all n complex embeddings and has its usual real inner-product space H; complex-conjugate entries are paired. The norm identity is ||σ(x)||²=n||coeff(x)||². The Euclidean coefficient dual of P is denoted P*.

Let Λ be an arbitrary latent random variable. Conditional on Λ=λ, let e_1,...,e_k be independent centered continuous canonical Gaussians with the same positive, conjugate-paired width vector r(λ), using density proportional to exp(-π sum_i |σ_i(e)|²/r_i²) on H. Suppose a deterministic c>0 satisfies

    r_i(λ) >= c |σ_i(u)|

for every i and every λ in the latent law's support (almost everywhere suffices). Independently draw U_1,...,U_k iid uniform P/qR, including zero. Publish

    A_j = U_j + Round_coeff(nq e_j) mod qR,

where nearest-integer coefficient rounding has a fixed tie convention. Set

    Theta_n(c) = [sum_(a∈Z) exp(-2π n c² a²)]^n - 1,
    delta_n(c) = min(1, sqrt(Theta_n(c))/2).

Then the full joint law retaining the latent variable obeys

    TV((Λ,A_1,...,A_k),(Λ,Z_1,...,Z_k)) <= min(1,k delta_n(c)),

where Z_j are iid uniform R/qR and independent of Λ. The same pointwise result can retain any additional public parameters, such as P,Q,u,T, or a random ideal choice, provided the hypotheses hold conditionally with the same c. There is no independence assertion for the A_j after Λ is forgotten.

In particular, the BBPS Gaussian family of Definition 3.6 has r_i>=α f(n)|σ_i(u)|/(sqrt(2)||u||∞) for every latent ellipse. Taking c=α f(n)/(sqrt(2)||u||∞), the theorem's hypothesis α/||u||∞>=2w(n), w(n)->infinity, with f(n)=ω(sqrt(log n)), makes k delta_n(c) negligible for polynomial k. This corollary requires the primary family's actual full law and retains its shared latent ellipse; it does not replace it by coefficient discrete Gaussians. It is a mathematical consequence of the width lower bound alone.

Small-mask consequence. Suppose additionally q is a split prime, I_T=P/qR has F_q dimension d, and Delta_k=min(1,k delta_n(c)). For every real b>=0,

    Pr[for all j, A_j∈I_T+[-floor(b),floor(b)]^n mod q]
      <= min(1,[q^d(2floor(b)+1)^n/q^n]^k)+Delta_k.

This rules out a high-probability alternative representation A_j=V_j+F_j in the SAME ideal with ||F_j||∞<=b whenever the right side is small, regardless of dependence among V_j,F_j. Even allowing an arbitrary common ideal of dimension d gives the unconditional bound

    Pr[there exists a common d-ideal I and such bounded F_j]
      <= min(1,binom(n,d) q^(kd)(2floor(b)+1)^(kn)/q^(kn))+Delta_k.

Thus if q>=n², q^d<=2^(ρn) for fixed ρ, b<=q/(2 log2(n) n^a) for fixed a>=0, and k>=1 is polynomially bounded, both bounds are negligible under the BBPS width condition. This concerns these short-mask representations and this common-ideal completion approach. It does not prove that the original RLWE problem is easy or exclude other source transformations.
