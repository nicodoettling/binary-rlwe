# RF3 primary-source and parameter review v1

Verdict: favorable for the exact frozen theorem and proof. The analytic import is applicable without GRH, and the finite numerator contributes only O(n) to its logarithm. No effective starting dimension or computational reduction follows. This is a nonauthor review, not project-level acceptance or formal verification.

Reviewed theorem SHA256: f090c6c128eb2d0fd52a9cadb2a2b67b8bdd731d84ef932aabbbdc3c74eb180a.

Reviewed proof SHA256: 012d77de4765194b8b22943d81773c42c59739f00e91012df8afd676ef210bfc.

The complete input manifest is reviewed-inputs-sha256-v1.json. In particular, the unchanged analytic dependency same-class-count-proof-v1.md has SHA256 bf625ccfa90a819c6b36639850a4cf2ab021c865cf3e84b67bc984cb3469d733, as cited by the new theorem. I read that proof in full instead of inheriting its prior favorable verdict.

## Exact primary-source statement and access record

I opened [Tsfasman–Vladut, arXiv math/0205129v1](https://arxiv.org/pdf/math/0205129v1). Printed page 8 defines BS as the limit of log(h Reg)/g and states BS=1 for asymptotically bad families when all fields are normal over Q, with GRH an alternative hypothesis. Printed page 2 defines g=(1/2)log|D|; the identity 2g=log|D| is explicit on printed page 19. Definition 2.2 and Example 2.1 on printed page 17 connect n/g tending to zero to the bad-family condition. Thus the imported conclusion is log(h Reg)=(1/2)log|D|+o(log|D|). The generalized good-tower theorem is not the premise used here.

I also opened [Lepisto, Two remarks concerning Dirichlet's L-functions and the class number of the cyclotomic field](https://www.acadsci.fi/mathematica/1969/no433pp01-08.pdf), Theorem 1, printed page 3. Its extracted text exposes normality and n/log|D| tending to zero, but its displayed relation glyph is degraded. Screenshot requests for that page and arXiv printed pages 2, 8, and 17 failed with cache-miss retrieval errors. No content-policy interruption occurred. I do not claim visual verification of the older scan. The readable arXiv statement supplies the exact analytic premise; I do not reprove Brauer–Siegel.

No unrelated summaries, broad source searches, or new analytic hypothesis were used.

## Independent hypothesis and parameter reconstruction

Write n=2^k, k>=1; let K=Q(zeta_(2n)), F=K^+, and d=n/2. The two sequences have degrees n and d, respectively. Both are abelian over Q, and therefore normal. Degrees grow strictly along powers of two, so the fields are pairwise nonisomorphic within each sequence.

The absolute discriminants are

    D_K=n^n,
    D_F=n^(n/2)/2.

The first identity follows by taking the norm of the derivative of X^n+1 in the full integer basis. For the second, put t=zeta+zeta^(-1). Reduction by zeta^2=t zeta-1 gives O_K=Z[t] + zeta Z[t]. This sum is direct over F; an element a+zeta b fixed by conjugation satisfies (zeta-zeta^(-1))b=0 and therefore b=0. Thus O_F=Z[t], and the displayed decomposition is an integral relative basis. Its relative discriminant is (zeta-zeta^(-1))^2. The absolute norm of this element from F is 4, because zeta-zeta^(-1) is a unit multiple of 1-zeta^2, Phi_n(1)=2, and [K:Q(zeta^2)]=2. Discriminant transitivity gives D_K=4D_F^2. This includes n=2; F=Q there is omitted from the asymptotic family to avoid the zero genus denominator.

Consequently,

    [K:Q]/log D_K = 1/log n -> 0,
    [F:Q]/log D_F = (n/2)/((n/2)log n-log 2) -> 0.

For each fixed rational prime power q, the number of primes of norm q is at most the field degree, as are the numbers of real places and complex-place pairs. Dividing these quantities by g=(1/2)log D makes every normalized invariant tend to zero. This establishes both asymptotic exactness and the bad-family hypothesis directly, with no subsequence or unproved density assertion. Both discriminants tend to infinity. Normality supplies the unconditional branch of the imported theorem.

The two applications give

    log(h_K Reg_K)=(1/2)n log n+o(n log n),
    log(h_F Reg_F)=(1/4)n log n+o(n log n).

Brauer–Siegel alone is not a class-number estimate, so the regulator subtraction must be checked. Both unit ranks are r=n/2-1. Let Q=[E_K:mu_K E_F]. For every K-unit u, all conjugates of u/conjugate(u) have absolute value 1; this quotient is an algebraic-integer unit, so Kronecker's lemma makes it a root of unity. Thus u^2 is in mu_K E_F, and the free quotient has exponent at most 2. This yields 1<=Q<=2^r. With the usual weights 1 for real logarithms and 2 for complex logarithms,

    Reg_K/Reg_F=2^r/Q,
    0<=log(Reg_K/Reg_F)<=r log 2=O(n).

The same calculation is valid at rank zero with regulators equal to 1. Subtracting the two analytic formulas and the O(n) regulator term gives

    log(h_K/h_F)=(1/4)n log n+o(n log n).

Since h_F>=1, this implies the claimed lower bound for h_K. Neither h_F=1 nor even log h_F=o(n log n) is required. No change from ordinary to narrow class groups occurs.

## Finite numerator and the asymptotic fraction

The finite proof supplies exactly

    |C_n| <= (3^n-1)(v_n+1)2^u_n,
    v_n=(n/2)log_2 n,
    u_n=floor((n/2)log n/log(2n+1)).

The power-of-two restriction makes v_n an integer. The floor makes u_n an integer, and both are nonnegative for n>=2. Since log(2n+1)>log n, u_n<n/2, so the proof's weaker u_n<=n/2 is valid. Also log(v_n+1)=O(log n). It follows that

    log |C_n| <= n log 3+(n/2)log 2+O(log n)=O(n).

There is at least one class in C_n: the principal class, using J=R. Thus its logarithm causes no empty-set convention issue. Combining the numerator with the reconstructed class-number lower bound gives

    limsup log(|C_n|/h_n)/(n log n) <= -1/4,

where n tends through powers of two. Equivalently, for every epsilon>0 the fraction is at most exp(-(1/4-epsilon)n log n) eventually. The original notation exp(-(1/4+o(1))n log n) denotes this upper bound; it is not a matching asymptotic equality. Its unspecified error has no prescribed sign.

## Resource, law, and scope boundaries

There is no reduction algorithm, running-time claim, advantage loss, sample-complexity claim, efficient class sampler, or effective analytic starting point. The uniform-class fraction is a mathematical counting measure, not the law of sampled ideals or CRT-root subsets. The n=2 fraction can equal 1 without contradicting the asymptotic statement.

All representative ideals in C_n are nonzero and integral in the same ring of integers. A collision forces their norm to be at most n^(n/2); this is derived from the collision, not an added assumption. Principal multiplication preserves ordinary class, so it cannot produce an integral colliding representative in an excluded class. Fractional scaling can produce collisions in every class, as recorded in counterexample-attempts-v1.md, and remains outside the theorem. Changing the coefficient encoding, ideal class, field, dimension, exposure, or source mechanism is likewise not excluded by this result.

The posterior claim uses the exact proof observation G+S and the fixed ideal support. It establishes no publicly available binary-RLWE attack. Its finite-support reasoning is checked in full-review-v1.md independently of the analytic theorem. No new experiment, model session, subagent, service, installation, or Git operation was used in this review.
