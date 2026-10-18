# C-LIFT-QUAD v1 — repeated quadratic lifting and genuine samplers

**PROVISIONAL, unreviewed.** This continues R2 within the frozen dimension-lift family. It distinguishes an arbitrary HSVP oracle from an actual sampler with extra balance guarantees. No short-vector advice or conditional sampler is supplied for free; source hardness remains OPEN.

## 1. The sibling ideal is available, but the norm products remain

Let a be the base degree, N=2^t a, r=2^t, and p a rational prime splitting in the entire tower. At a single degree-doubling from d to2d, the complementary ideal of a selected prime is exactly the other prime above its contraction, also of normp. Thus the large-index complementary-ideal input of the one-step degree-r trace repair can indeed be avoided if an oracle can solve the two appropriate sibling primes at that degree.

If both sibling outputs have HSVP factor γ_(2d), the trace bound in `linear-trace-repair-v1.md` gives

    γ_d <= γ_(2d)^2 sqrt(d).                              (Q1)

A conjugate-pair estimate sharpens sqrt(d) to sqrt(d/2). These are upper bounds on what the transfer guarantees, not lower bounds on every possible output. Applying the displayed unsharpened recurrence for t levels gives exactly

    γ_a <= γ_N^r a^((r−1)/2) 2^(((t−2)r+2)/2).            (Q2)

Indeed logγ_a=r logγ_N+(1/2)Σ_(j=0)^(t−1)2^j log(2^j a), with Σ2^j=r−1 and Σj2^j=(t−2)r+2. Repeatedly bounding only intermediate Euclidean norms loses information and can be worse than the direct relative-norm calculation.

There is a correlation-preserving way to obtain the sibling vector with no extra oracle: apply the relative involution to the first x. Then w=conj_rel(x), and the repaired quadratic trace is exactly

    Tr(x conj_rel(x)/2)=N_(K_doubled/K_base)(x).

Iterating this construction is exactly the full relative norm, not a new distribution or independence assumption. The sharper direct guarantee from `first-test-v1.md` is

    Γ = γ_N^r (a/2)^((r−1)/2).                            (Q3)

This already used all the relevant correlations. Feeding Γ into the actual prime-ideal hardness theorem gives the same lower bound p^(1/N)≥sqrt(a/2), incompatible with fixed binary index rate for growinga.

If instead one recursively obtains all necessary lower-degree vectors from separate top-degree oracle calls, the recursive products still obey (Q1)–(Q2). Merely observing that every leaf prime has small index does not bound the internal output norms. An actual improvement would need a proved, stronger joint output property that controls the traces or embedding products. Success probabilities of multiple oracle calls and the conditional p-law would also need charging; no independent per-call success is assumed here. Using conjugates avoids those new oracle-success issues but returns to (Q3).

## 2. A finite counting bound on existence of short outputs

Write u_max=(4A)^(1/N). Let F be the frozen extension-prime family: all degree-one primes Q' of R of normp∈[A,4A], where p≡1 mod2N. Its cardinality is

    M = N P_(2N)(A).

For B≥1 define the exact coefficient-ball count

    C_N(B) = #{x∈Z^N: 0<||x||₂≤B}.

A nonzero x∈R with this coefficient norm satisfies |N_(K/Q)(x)|≤B^N by AM–GM in the canonical embedding. Each distinct Q'∈F containing x contributes a factor at leastA to the principal-ideal norm |N(x)|. Therefore the number of such Q' is at most N logB/logA. A union bound gives the exact finite estimate

    Pr_(Q' uniform F)[there is 0≠x∈Q', ||x||_coef≤B]
       <= min(1, C_N(B) N logB / [M logA]).                (E1)

No independence or random-lattice heuristic is used. For B=1 the right side is0, correctly reflecting that the nonzero coefficient unit vectors are roots of unity and lie in no proper ideal.

A γ-HSVP output would have coefficient norm at mostγ p^(1/N)≤γ u_max. If u_max andγ are fixed constants, C_N(γu_max)=N^O(1): there are at mostfloor(B²) nonzero integer coefficients, each bounded byB. Under the verified GRH count M~3A/logA, with logA=Θ(N), (E1) is exp(−Ω(N)). Consequently almost all ideals in the intended family do not even admit such a constant-factor output. Calling a constant-HSVP oracle on that family is not a well-posed promise unless its success is correspondingly negligible or its ideal law is changed.

This also explains why balanced output magnitudes of constant size are not a free enhancement. Such balance implies coefficient normO(1), and is subject to the same count. The calculation does not exclude polynomial-factor HSVP solutions or every nonconstant balance regime.

## 3. Canonical Gaussian sampling pays a dimension scale

Let D_(Q',s) denote the discrete Gaussian with mass proportional to exp(−π||σ(x)||²/s²). The embedding convention matters: σ(R) is a rotated sqrt(N) Z^N. Its Euclidean dual is σ(R)/N, which is contained in σ(Q')*. The latter therefore contains the two nonzero vectors±σ(1)/N of Euclidean norm1/sqrt(N). The definition of smoothing gives the necessary condition

    η_ε(σ(Q')) >= sqrt[N log(2/ε)/π].                    (G1)

Thus an above-smoothing Gaussian has canonical parameter growing at least as sqrt(N). Its typical continuous-scale Euclidean norm is of order s sqrt(N), which corresponds to HSVP factor of order s/p^(1/N), not constant at p^(1/N)=O(1). An argument using continuous Gaussian product behavior must retain this scale and any discrete-to-continuous loss. No covariance-only argument establishes the full law.

There is a separate exact obstruction to simply choosing s=O(1) below smoothing. Since Q'⊂R and the zero vector has Gaussian mass1,

    Pr_(x~D_(Q',s))[x≠0]
      <= rho_s(σ(R)\{0})
       = [ Σ_(z∈Z) exp(−π N z²/s²) ]^N − 1.             (G2)

For s bounded, the right side is O(N exp(−Ω(N))). Conditioning on a nonzero output thus has exponential expected rejection cost in this regime, for every Q'. This is not a claim that all smaller-than-smoothing samplers fail; (G2) states exactly which width regime is excluded. A sampler that promises nonzero outputs by a different method needs its own law and efficiency argument.

Even an idealized balanced Gaussian calculation would require feeding its scale-dependent oracle approximation factor back into the base family parameterA. For a hypothetical per-embedding scale s with product behavior yielding Γ roughly(s/u)^r, where u=p^(1/N), the requirement u^r≳a²Γ would imply u²≳s a^(2/r). With (G1), this already prevents constantu. This last sentence is a diagnostic parameter calculation under the explicitly hypothetical product law, not a theorem importing Gaussian outputs from an arbitrary HSVP oracle.

## 4. Sampler versus advice

A genuine polynomial-time sampler of (Q',x) with the exact marginalQ' and the claimed shortness would satisfy the existence bound (E1); it cannot evade that bound by hiding its coins. A sampler of conditional short-vector ideals changes the ideal marginal and needs a new hardness reduction. A sampler with above-smoothing Gaussian outputs pays (G1); one using bounded canonical width and rejecting zero pays (G2).

For a given hard inputQ', a fresh sampler that generates unrelated prime ideals with trapdoors does not produce a trapdoor conditioned on that input. This distinction remains even when quantum factoring can implement the fresh sampler. A per-input short trace-dual element supplied as advice is a different problem. None of the checked primary theorems supplies the missing low-index decisional source from any of these models.

The exact algebra/counting statements here are newly provisional. The original primary field-family and progression hypotheses are those in `first-test-v1.md`; the Gaussian deductions use the displayed definitions directly. A separately reserved finite count control is pending and will be recorded without changing this immutable version.
