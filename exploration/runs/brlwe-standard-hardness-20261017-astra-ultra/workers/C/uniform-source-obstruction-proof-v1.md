# Proof of C-UNI v1

Status PROVISIONAL. The statement is uniform-source-obstruction-theorem-v1.md. Its algebraic injectivity step also appears as worker A's provisional A-BIN v1; this proof repeats the necessary argument so its dependency can be reviewed exactly.

1. **Noninjectivity limits CRT support.** For U∈R_q, let r be its number of nonzero CRT values. If multiplication by U is noninjective on coefficient-binary vectors, there is nonzero v∈{-1,0,1}^n with Uv=0 modulo q. At all r active roots of U, v vanishes. The integer multiplication matrix M_v has rank at most n-r modulo q, so q^r divides det M_v by Smith normal form. Its determinant is nonzero because X^n+1 is irreducible over Q and v is nonzero of degree below n. Negacyclic Fourier diagonalization and arithmetic-geometric mean give |det M_v|≤||v||_2^n≤n^(n/2). Thus q^r≤n^(n/2).

For every fixed support of size r, there are (q-1)^r possible U. Summing over the at most 2^n supports satisfying this inequality gives

    # {U : multiplication by U is noninjective on binary vectors}
       ≤ 2^n n^(n/2).                                  (1)

The count deliberately includes supports whose binary projection is actually injective. No converse to the norm condition is used. For a noninjective tuple Ψ_U, the same colliding pair makes multiplication by U_1 noninjective, which is all that will be needed.

2. **Small multiplication norm bounds the coefficient vector.** The first standard basis vector is the constant polynomial 1. Hence M_F1 e_0=F_1, so

    ||F_1||_2≤||M_F1||_2≤||M||_2≤S

on Good. No covariance or tail estimate is substituted for this pointwise relation.

3. **Integer-ball count.** Let B(n,S)=#{f∈Z^n:||f||_2≤S}. For t>0,

    B(n,S)≤exp(πS²/t²) [sum_{a∈Z}exp(-πa²/t²)]^n.

The one-dimensional sum is at most 1+t: monotonicity bounds its positive tail by the integral from zero to infinity. If S>0, choose t=sqrt(2π)S/sqrt(n), obtaining

    B(n,S)≤[sqrt(e)(1+sqrt(2π)S/sqrt(n))]^n.              (2)

For S=0 the left side is 1 and the same right side is e^(n/2)>=1, so the inequality remains valid.

4. **Count public first rows admitting a bad decomposition.** Let E_S be the subset of R_q consisting of all residues U+F with U noninjective on binary vectors and integer ||F||_2≤S. Each pair contributes at most one residue; wraps and collisions only reduce the set size. Combining (1) and (2),

    |E_S|/q^n ≤ [2sqrt(e n)/q+2sqrt(2πe)S/q]^n,

capped by one. If Good occurs and Ψ_U is noninjective, A_1∈E_S regardless of how the latent decomposition or Good was chosen. Since the first marginal is δ-close to uniform,

    Pr[Good and noninjective]≤Pr[A_1∈E_S]
                            ≤δ+|E_S|/q^n.

This proves UNI without conditioning on a selected support, latent Gaussian, or acceptance event. It is a set inclusion followed by an original-law TV estimate. No product of posterior probabilities occurs; CP-1 is inapplicable to the proof and its rejected product remains rejected.

5. **The claimed upper bound becomes vacuous.** On any injective branch, |image Ψ_U|=2^n, and p>=1/2 implies min{1,2^n p^n}=1. Therefore

    δ_bad+β≥Pr[not Good]+Pr[Good and injective]
            =1-Pr[Good and noninjective].

UNI proves VAC. This argument allows Good to depend on all source variables, U, masks, support ranks and other source-only coins. It does not assume independence of Good and injectivity.

6. **Asymptotic substitution.** With q>=n² and S/q≤1/(2τ n^c), the displayed bracket is bounded by 2sqrt(e)n^-3/2+sqrt(2πe)/(τ n^c). For fixed c>0 and τ>=1 this is O(n^-min(c,3/2)), so its nth power is exp(-Ω(n log n)) and negligible. Adding negligible δ preserves negligibility. Finite instances with bracket>=1 give a vacuous finite inequality, as explicitly allowed.

The probabilistic argument uses only the exact first-marginal TV hypothesis. It has no hardness premise, efficiency claim, Gaussian approximation or advice dependence. Finite falsification controls and independent review remain outstanding before acceptance.
