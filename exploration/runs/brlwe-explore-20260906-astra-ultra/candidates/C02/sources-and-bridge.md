# C02 source task, public sampler, and missing implication

Primary sources independently read on 2026-09-06:

* Brakerski–Döttling, *Lossiness and Entropic Hardness for Ring-LWE*, [2020/1185 primary PDF](https://eprint.iacr.org/2020/1185.pdf). Supplied [local text](../../sources/2020-1185.txt) and public PDF text were both available. Relevant source locations: Definitions 2.3 and 2.6, pp.8 and 10; Definitions 3.1–3.3 and Lemmas 3.4–3.5, pp.10–13; Definition 4.1 and Theorem 4.2, pp.13–15; Theorems 5.7–5.8, pp.18–19; Definition 6.1 and the Section 6 sampler/Lemma 6.6, pp.19–21; Theorem 6.9, p.22.
* Stehlé–Steinfeld, *Making NTRU as Secure as Worst-Case Problems over Ideal Lattices*, [2013/004 primary PDF](https://eprint.iacr.org/2013/004.pdf). Independently read the coefficient/canonical norm distinction in Section 2.2, pp.8–9, the projection bound in Lemma 2.7, pp.7–8, and the small-evaluation part of the Lemma 4.1 proof, p.26. Public screenshots of PDF pages 7 and 26 returned HTTP403; extracted primary text was readable. No conclusion uses an inaccessible image.

The rest of this file gives independently written definitions and deductions, not a new theorem claimed by those authors.

## 1. An independently described source family

Fix the same integral ring R=Z[X]/(X^n+1), a modulus q, and a canonical Gaussian width γ. Write κ=γ/sqrt(n) for the corresponding coefficient width. A ring Gaussian of this canonical width has iid coefficient law D_κ before conditioning.

**DSPR decision experiment.** Sample g with that ring Gaussian and independently sample f with the same law conditioned on f mod q being a unit. Give h=g/f mod q to a distinguisher. The other experiment gives a uniform h∈R_q. The assumption is computational indistinguishability at the specified (n,q,γ). The source contains no Boolean target secret and gives no noisy target transcript. This is the source task in BD Definition 6.1. Efficient conditioning requires a nonnegligible acceptance probability or another efficient conditional sampler; no such guarantee is silently extended to arbitrary q.

**Hermite-form RLWE decision experiment.** Fix an efficiently sampled source law χ on integral R. Sample s_0←χ and, for each requested source sample, independent uniform h_j∈R_q and e_j←χ; give (h_j,h_js_0+e_j). Compare with independent uniform pairs. BD Definition 2.6 uses the same χ for source secret and source error. Its one-sample special case is enough for each hybrid below. This is independently studied Hermite-form RLWE, with its parameters stated separately from the reference binary-secret/discrete-Gaussian target.

Classification: these are established, independently studied *assumption families*. This does not assert every small γ, every χ, or every odd q is hard, and it does not invoke a worst-case reduction in an unchecked regime. A new arbitrary denominator law asserted pseudorandom solely because it would make the desired proof work would instead be a tailored assumption.

## 2. The old public sampler and its computational reduction

For a fixed finite ring sample count m, define X_{γ,χ,m} by:

1. Sample f,g as in the DSPR experiment.
2. Independently sample r_i,r'_i←χ for i=1,...,m.
3. Compute z_i=g r_i+f r'_i over integral R.
4. Output the tuple A_i=f^{-1}z_i mod q.

Thus A_i=h r_i+r'_i with h=g/f mod q shared across i. The sampler coins T=(f,g,(r_i,r'_i)_i) are sampled independently of the subsequent target secret and target errors. The tuple generally has correlations from the shared h; the relevant indistinguishability statement is *joint* A≈U(R_q)^m.

The reduction behind BD Lemma 6.6 can be written publicly. Given a DSPR challenge h, sample all r_i,r'_i and output h r_i+r'_i. This requires neither f nor g. Once h is replaced by uniform, use an m-step hybrid to replace the outputs by independent uniforms. In hybrid i, a single Hermite-form challenge (h,b) occupies position i, while earlier positions are sampled uniformly and later positions are computed with freshly sampled r_j,r'_j and the public h. The common h can be discarded from the final adversary's view.

For any distinguisher against the tuple, this gives an advantage bound of the form

    Adv_X ≤ Adv_DSPR + Σ_{i=1}^m Adv_HNF,i.

This is a public simulation with an m factor in the source hybrid count and polynomial ring arithmetic. It preserves degree n, module rank one and modulus q. The source r_i and r'_i are internal sampler variables, not reference target error samples or extra observations given to a target attacker.

The source Section 6 norm analysis additionally takes χ bounded in canonical norm. Writing β for that bound avoids confusing it with a basis matrix or a coefficient bound. A target error with an exact coefficient discrete Gaussian has unbounded support and a different role; χ is not automatically that error law. If χ is truncated Gaussian, the truncation distance and the width's normalization must be recorded.

## 3. The exact missing combination

Independently of the above source tasks, let the target secret be uniform coefficient binary and generate m independent coefficient discrete-Gaussian error vectors of width σ, independent of all sampler coins. For each public tuple a, define g_{σ,q}(a) by the wrapped maximum-likelihood formula in [calculations](calculations.md), §1.

The candidate route needs an efficiently sampled public tuple law X satisfying both:

    (P) X is computationally indistinguishable from U(R_q)^m;
    (L) Pr_{a←X}[g_{σ,q}(a) ≤ 2^{-h}] ≥ δ,

where h=ω(log n) and δ≥1/poly(n), or the corresponding explicitly defined negligibly smoothed condition. Sampling each A marginal pseudorandomly is insufficient for (P). An entropy bound for the richer precursor is only a sufficient way to establish (L), and may fail even when (L) holds.

For X=X_{γ,χ,m}, the DSPR/Hermite assumptions provide (P), subject to their stated source regime. They do not provide (L) for the binary reference target. Conversely, the fixed denominators 1+X and 1-X-X² give useful exact-coset entropy controls, but the short-ratio public tests reject their naive use for (P). No distribution established here supplies the two properties together.

BD Definition 4.1 and Theorem 4.2 provide the abstract connection from a sometimes-lossy pseudorandom tuple to **mild search hardness** for the matching secret/error experiment. The entropy/error hypothesis must concern the actual transcript with the same law. Writing S uniform and E for the entire fixed m-error tuple, mild hardness excludes a PPT solver B and negligible ν for which the set of (S,E) satisfying

    Pr_{uniform A, solver coins}[B(A,AS+E)=S] > 1-ν

has nonnegligible probability. This is weaker than requiring every solver's average recovery probability to be negligible.

There is also a useful stronger sufficient condition that makes the finite-sample distinction transparent. If (P) holds and

    E_{a←X} g_{σ,q}(a) ≤ negl(n),

then standard search hardness for that same fixed m and exact error law follows directly: a public distinguisher samples S,E, runs a proposed solver on (A,AS+E), and tests whether its answer equals its internally known S. Its success under X is at most E_X g, and its difference from success under uniform A is bounded by the public-tuple distinguishing advantage. This is our elementary reduction, not a claim that the stronger average bound is available. A δ fraction of lossy tuples by itself does not give this negligible-average bound.

The first missing mathematical statement for the old sampler is therefore a wrapped-likelihood upper bound for the actual tuple under the *fixed discrete* target errors, on a nonnegligible fraction of its public outputs. Hiding sampler coins cannot supply that bound: under the joint conditional-error hypothesis, the exact posterior is already unchanged when those coins are revealed.

## 4. Error, sample, and hardness boundaries

The old Theorem 5.7 analyzes continuous Gaussian masking on a real torus. It introduces lattice-discrete intermediate Gaussians through convolution/smoothing estimates; those auxiliaries do not make its final target error automatically equal to W_{σ,q} in the present reference experiment. In the power basis, a canonical continuous width γ_0 corresponds to coefficient continuous width γ_0/sqrt(n). The discrete reference width σ has no unannounced substitution for either.

BD's source theorem uses a norm-controlled noise increase, including a sqrt(m) dependence from concatenating m ring numerator blocks. Neither a successful one-sample control nor m deterministic rotations proves a result for an arbitrary polynomial number of independent ring samples. All statements above fix m before defining the sampler and target law.

BD Theorem 6.9 states mild search hardness in its framework. Lemma 3.4's amplification uses an unbounded sample oracle; Lemma 3.5's finite-input rerandomization forms subset sums and produces a distribution of error laws. Those are separate steps with a changed sample/error ledger. This dossier imports neither as standard finite-sample hardness for unchanged iid coefficient discrete Gaussians.

Decision hardness of (A,AS+E) versus independent uniform pairs is a separate stronger target. No search-to-decision map with the binary secret and unchanged error/sample parameters is supplied.

## 5. Handling the norm qualification without an audit

BD Lemma 6.5 presents an inverse-norm estimate using the paper's canonical convention and cites SS2013 Lemma 4.1, whose norm and Gaussian width are coefficient based. C02 does not resolve the transfer of the stated probability and does not claim a source theorem is refuted.

The retained use is deliberately local: on the explicitly written canonical inverse event, the deterministic singular-value calculation proves Boolean injection. Separately, SS2013's stated one-dimensional projection estimate gives the fully normalized unconditioned sufficient regime in [calculations](calculations.md), §5. Conditioning on modular invertibility remains quantified by its separate probability. These two claims are not merged into an unqualified assertion about the old sampler.
