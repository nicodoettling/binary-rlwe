# C-LOWINDEX v1: full-rank short denominators and the actual hardness distributions

Status: **PROVISIONAL — author calculation, not independently reviewed or certified. Source hardness remains OPEN.** This is a genuinely different attempted mechanism from common modular ideals. The finite experiment is a falsification control, not a proof of hardness. The tower v1/v2 counterexample and correction are separately preserved in `../tower-correction-v1-to-v2.md`; no inherited review is claimed.

## 1. Frozen proposed source and both exact endpoints

Let R=Z[X]/(X^n+1), n a power of two, q an odd split prime. All norms below are specified; coefficient Euclidean norm is ||·||_coef, while ||σ(x)||_2=√n||x||_coef and ||M_x||_op=max_j|σ_j(x)|. The coefficient multiplication matrices are normal and are simultaneously diagonalized by the normalized Fourier matrix. Rational inverses are in K=Q[X]/(X^n+1); modular inverses are in R_q. They are not interchangeable by coefficient rounding.

Choose a joint latent law Λ of (f,g)∈R², independent of the fresh target binary secret S and target noise G, with f modq invertible. This is a named input requirement, not a distribution supplied by NTRU search hardness. Independently choose E_i,E'_i iid χ, i=1,...,k, for a specified coefficient or canonical bounded noise law χ. Set z_i=gE_i+fE'_i and

    H = f^{-1}g modq,
    A_i = f^{-1}z_i modq = H E_i + E'_i modq.

Publish A=(A_1,...,A_k) only. A latent source event Good may bound |N(f)|, ||M_f||, and the entire stacked rational multiplication matrix T=(M_{f^{-1}z_1},...,M_{f^{-1}z_k}); it is independent of S,G. Its probability is charged, never used for unimplemented rejection sampling. No f,g,H or fresh same-denominator oracle is supplied.

The full source comparison is P_Λ=Law(A) versus U_k=Unif(R_q^k), with any actual public metadata included on both sides under its correct joint law. The target completion map samples S uniform on coefficient {0,1}^n and independent coefficient noise G_i of the specified target width, then produces (A,A_i S+G_i)_i, retaining the same S in any proof-only joint law. Under U_k this is exactly the desired uniform-multiplier binary-secret target. Under P_Λ it is exactly the denominator-based joint law, with common latent f,g and correlated z_i. No Gaussian or independence approximation is being substituted into this endpoint identity.

A distinguisher D for this source can be used on a raw ratio challenge h by sampling the E_i,E'_i and giving D(hE_i+E'_i)_i. Thus the first hybrid is exactly

    f^{-1}g  -->  a uniform R_q;
    (A_i)_i --> (a E_i+E'_i)_i.

The second hybrid replaces the latter entries one at a time by uniform elements, using the one-sample Hermite-RLWE experiment with its public a and fresh small secret E_i. The common a is retained by the hybrid simulator and hidden from D. There is no claim that these entries are statistically independent uniform conditional on a. If raw-ratio distinguishing advantage is at most ε_ratio and each Hermite-RLWE advantage at most ε_H, this explicit chain bounds the source advantage by ε_ratio+k ε_H (plus any separately justified noise-conversion losses). Standard search NTRU hardness does not supply ε_ratio. Publishing H would change both endpoints and require the corresponding joint theorem.

## 2. The finite coset is the correct entropy charge

For any nonsingular integral multiplication matrix M_f, the lattice L=fR has finite index D=|det M_f|=|N(f)|. The precise information step behind TCC2020 Theorem5.7 uses log_2D, before its coarser n log_2||M_f|| bound. The extracted proof's displayed H_0(E') bound is false for an unbounded Gaussian E'; the following argument avoids it.

Fix f. Let E be any integer-valued noise independent of S. Put K=E mod L, taking exactly D possible values. Let E' be sampled by a Markov kernel depending only on K, with independent fresh kernel randomness. For example, E' can be a discrete Gaussian on L-E: that coset depends only on K. Let Y=S+E. Then

    S -- (Y,K) -- (Y,E') -- Y+E'

is a valid sequence of stochastic post-processings for guessing S: given (Y,K), sample E' from its kernel; the final sum is deterministic. Consequently

    p_guess(S|Y+E') <= p_guess(S|Y,E')
                         <= p_guess(S|Y,K)
                         <= D p_guess(S|Y).

The last inequality follows directly by summing max_s Pr[S=s,Y=y,K=k] over y,k and bounding each maximum by max_s Pr[S=s,Y=y]. This proof does not pretend E' has finite support or is independent of E unconditionally. The same argument holds conditionally on any fixed latent f and public metadata for which E is sampled independently with the stated law. No zero-norm or noninvertible denominator branch is admissible without explicit handling.

For coefficient integer Gaussian E~D_σ^n and uniform binary S, p_guess(S|S+E)=((1+D_σ(0))/2)^n, by unimodality and telescoping the two shifted one-dimensional masses. For an unwrapped coefficient continuous Gaussian of parameter σ, the corresponding exact expression is Φ(√(π/2)/σ)^n, where Φ is the standard normal CDF. Folding modq cannot increase guessing probability. Thus log_2D≤ρn, ρ<1, really is compatible with a binary entropy margin when σ grows sufficiently.

This establishes only the finite-coset step. To turn it into the entire TCC Gaussian theorem, its independent convolution and continuous/discrete comparison lemmas must also hold with the chosen coefficient convention and target distribution. A candidate refinement keeps their hypotheses

    σ > τ2 η_ε(Z^n),   σ0 >= 2^(3/2) τ1 σ,
    τ2 >= ||M_f||_op,  τ1 >= ||T||_op,

but replaces n log_2τ2 by log_2|N(f)| in the entropy loss. The original comparison budget is 20ε in its conventions. This packet does not silently certify that full refinement, precision implementation, or a changed discrete target law. In particular, a small determinant does not control τ2 or τ1.

## 3. A public annihilator defeats the unit and ramified families

**Provisional clearing lemma.** Suppose a known positive integer m, coprime to q, satisfies mR⊂fR on a source event Good. Suppose also ||T||_op≤τ1 there. Then m f^{-1}z_i∈R. Each coefficient of f^{-1}z_i has absolute value at most τ1: apply the i-th block to the coefficient basis vector 1 and use its norm bound. If B=floor(mτ1)<q/2, the centered coefficients of m A_i are precisely those of m f^{-1}z_i. The polynomial-time test

    accept iff every centered coefficient of m A_1 lies in [-B,B]

therefore accepts P_Λ with probability at least Pr[Good]. Under the exact uniform comparator, multiplication by m is a permutation, so acceptance is exactly ((2B+1)/q)^n. The advantage is at least

    Pr[Good] - ((2 floor(mτ1)+1)/q)^n.

No latent f or unit basis is needed to run the test. Multiple samples are unnecessary. If a polynomial-size public list of possible m values covers the good branch, the OR of these tests has the corresponding sum of uniform acceptance bounds. The test also works with an added mask only if its actual size after multiplication by m is charged; there is no free extra mask.

Always m=|N(f)| works, because the integral adjugate gives N(f) f^{-1}R⊂R. This does not give a polynomial-time test over all unknown D≤2^{ρn}, and when Dτ1 is comparable to q the bound is vacuous. Hence this lemma does **not** rule out every low-index denominator source.

It does rule out the following natural candidates in a meaningful noise range:

* f=u a hidden unit: m=1, independently of which unit is sampled.
* f=(1+X)^r u, 0≤r≤n, u an arbitrary hidden unit: m=2, although D=2^r can be exponential in n.

The second assertion has an elementary ideal proof with the containment direction explicit. N(1+X)=2, obtained by evaluating X^n+1 at -1. Since n is a power of two, the intermediate binomial coefficients of (1+X)^n are even, and X^n=-1 in R; hence (1+X)^n∈2R. Therefore (1+X)^nR⊂2R. Both ideals have index 2^n, so they are equal. For r≤n,

    2R=(1+X)^nR ⊂ (1+X)^rR=fR.

Unit multiplication does not change the principal ideal. It cannot change the small public annihilator.

For a concrete asymptotic intersection calculation, assume the candidate TCC comparison hypotheses above and target width σ0≤q/n^c, c>0. Then

    τ1 < q / (2^(3/2) n^c τ2 η_ε(Z^n)).

Because f is a nonzero algebraic integer, τ2≥|N(f)|^(1/n)≥1. For m≤2 and η_ε(Z^n) bounded below by a positive constant, the uniform acceptance bound is at most

    (m/(sqrt(2) n^c τ2 η_ε(Z^n)) + 1/q)^n = negligible.

A nonnegligible Good probability then gives an efficient source distinguisher. Thus hidden random units do not produce the needed pseudorandom source for these denominator ideals while retaining this usable rational-matrix width. This argument concerns A_i=f^{-1}z_i, not just the raw g/f ratio, so multiplying by fresh small E_i and adding E'_i does not remove it when the same τ1 condition is maintained.

## 4. Comparison with the actual published distributions

### 4.1 Original TCC Gaussian denominator

The primary TCC distribution samples f,g from a wide discrete Gaussian, conditions f to be a unit modq, and sets z_i=gE_i+fE'_i. Its inverse-norm good branch has ||σ(f^{-1})||_2≤C_inv√n/γ for an absolute constant C_inv. The extracted constant appears as `24` and may flatten an exponent; retain C_inv symbolically rather than infer typography. AM–GM gives, exactly on this branch,

    |N(f)| >= (√n / ||σ(f^{-1})||_2)^n >= (γ/C_inv)^n.

Consequently this actual good branch intersects |N(f)|≤2^{ρn} only if γ≤C_inv 2^ρ. The statistical-uniformity regime used to remove DSPR instead requires γ≥n sqrt(ln(8nq)) q^(1/2+α), 0<α<1/3. These conditions are disjoint asymptotically. This is stronger than merely retaining the coarse τ2 upper bound, but it is scoped to the published inverse-controlled good branch; it is not a tail theorem excluding every other latent event under the Gaussian law. Conditioned modq-unit probabilities and the uniform-unit versus full-ring comparator distance must still be charged in any complete reduction. Source: Brakerski–Döttling, TCC2020, local full primary extraction `exploration/runs/brlwe-explore-20260906-astra-ultra/sources/2020-1185.txt`, Lemmas6.5–6.8 and Theorem6.2, https://eprint.iacr.org/2020/1185.pdf .

### 4.2 Worst-case-supported polynomial-modulus NTRU

Use the notation (b,f) for a relation b=h f modq, so f is our denominator. In FPSW2023 Theorem6.2, h=IdealToNTRU(a,q), and every relation satisfying its short-solution threshold ||σ(b)||_2,||σ(f)||_2≤√q/γ' has f∈a\{0}. Hence (f)⊂a and |N(f)|≥N(a). The worst-case-supported family samples a uniformly among prime ideals of norms [A,4A]; its displayed construction chooses A^(1/n)=C' c_0 n Δ^(1/n) Γ with C'≥1, c_0>1, Γ≥1. In our cyclotomics Δ^(1/n)=n, so log_2|N(f)|≥log_2A≥2n log_2n+n log_2c_0, exceeding the binary budget. Unit multiplication preserves this lower bound. This excludes all relations within that theorem's short threshold, not merely one chosen witness. Longer or differently shaped relations are outside this deduction. The theorem does not ensure f is a unit modq. Its endpoint is search NTRU, with quantum/ERH and prime-density dependencies, not decisional uniform ratios. Trapdoor sampling additionally uses factoring. Source: https://perso.jfelderhoff.fr/work/papers/FPSW23.pdf , Corollaries5.4/6.3 and Theorem6.2 proof. No unverified PS21 primary statement beyond the explicit proof reproduced there is imported.

The exact threshold used in that proof is at most

    ||σ(b)||_2,||σ(f)||_2 <= q / [n^(3/2) δ_K Δ^(1/(2n)) N(a)^(1/n)],

with its parameter choice ensuring √q/γ' is within it. The reference's printed prime-density runtime expression needs its preceding success loss Ω(ε²/tildeρ_A) retained; no uniform polynomial lower bound on prime density is assumed here. The modulus furnished by the theorem is not automatically the frozen split prime q either. Even granting these extra conditions favorably, the denominator norm gap already holds.

### 4.3 Rounded Arakelov ideal distribution

The previously checked BDPW2020 rounding outputs an inverse integral ideal Q^{-1}; its explicit high-probability shell has N(Q)≥(M/2)^n with M/2≥2^(n+1)n² for our power-of-two normalization. Any integral scalar f clearing that fractional ideal, fQ^{-1}⊂R, lies in (Q^{-1})^{-1}=Q. Therefore |N(f)|≥N(Q), again exceeding 2^{ρn}. Multiplying f by units preserves the norm and ideal membership. This is a deduction about denominator clearing of the actual published rounded family, not about every possible discretization of Arakelov classes or every principal-unit distribution. That primary reduction supplies a search ideal-SVP family, not a raw-ratio/uniform decision theorem. Source: https://ir.cwi.nl/pub/30072/30072.pdf , extraction and parameter calculation preserved in `../ideal-family-randomization-test-v2.md`.

## 5. Exact finite control and what remains open

C-LOWINDEX-1 was approved by the coordinator, run once, and released. `control-v1.py` uses exact integers and Fractions, no randomness. It checks all 25 f=(1+X)^r(1+X+X²)^t, r=0,...,4, t=-2,...,2, in n=4 and all 16 binary numerators each, q=17. All f are integral, |N(f)|=2^r, and 2f^{-1} is integral. All modular identities and small-lift reconstructions pass. A negative case records f=1+X,z=1: the rational quotient is (1,-1,1,-1)/2, while its modular ratio is (9,8,9,8); coefficient rounding is incorrect. Multiplying by2 and centering gives (1,-1,1,-1).

The comparator enumeration visits every a∈R_17 twice, for m=1,2, and verifies exact acceptance counts (2B+1)^4 for B=0,1,2,4,8. A separate exact index-2 finite Markov-kernel example gives guessing probabilities 9/16,3/4,3/4,35/48 for Y,(Y,K),(Y,E'),Y+E', respectively. Conditional dependence is preserved. All assertions pass; wall0.275950s, maxRSS11264KiB, address-space cap256MiB, stderr empty. Complete output, resource record, command, and code are adjacent; the experiment does not certify the asymptotic or imported Gaussian claims.

The viable unproved corner is a denominator law with |N(f)|<2^{ρn}, no efficiently exploitable small public annihilator, suitably bounded actual τ1 and τ2, and a **verified** reduction from a standard worst-case problem to its decisional ratio distribution (or directly to its completed source). No checked theorem above supplies that corner. The exact coset refinement is a useful interface, not a replacement hardness assumption and not completion of the computational-foundations objective.
