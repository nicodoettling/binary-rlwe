**Binary-secret RLWE: initial literature review, 5 September 2026**

I reviewed the two supplied papers and searched for related reductions, follow-ups, and attacks. The search found substantial progress for Module-LWE, but no verified reduction covering the intended target: rank-one RLWE with independent uniform binary coefficients and suitably small Gaussian error. This is a report of the literature located, not an impossibility claim. A particularly recent status check is Boudgoust's 14 July 2026 talk, which explicitly lists **decision** RLWE with binary secrets as open; that statement alone does not settle the status of every search variant. [Slides, numbered slides 10 and 18](https://katinkabou.github.io/Presentations/202607_NovelLatticeAssumptions.pdf).

Throughout these notes, the reference target is

\[
R_q=\mathbb Z_q[X]/(X^n+1),\qquad
s=\sum_{j=0}^{n-1}s_jX^j,\quad s_j\overset{\$}{\leftarrow}\{0,1\},
\qquad (a_i,a_i s+e_i),
\]

with power-of-two degree \(n\). This fixes a representative setting for comparing results; it is not a restriction imposed on the eventual research question. Module rank, ring degree, and number of ring samples are different parameters. One ring sample gives \(n\) structured scalar equations, not \(n\) independent ordinary LWE samples. Gaussian conventions also differ: coefficient versus canonical embedding, primal versus dual, and errors measured modulo \(q\) versus modulo 1. Numerical noise bounds below retain the cited paper's normalization.

**The supplied ordinary-LWE paper.** Brakerski–Döttling, *Hardness of LWE on General Entropic Distributions*, EUROCRYPT 2020. [Local PDF](2020-119.pdf), [ePrint](https://eprint.iacr.org/2020/119). Page and theorem numbers here refer to the supplied PDF.

The organizing quantity is noise lossiness,

\[
\nu_t(S)=\widetilde H_\infty(s\mid s+g_t),
\]

the negative logarithm of optimal average guessing probability after Gaussian perturbation. In the ordinary-LWE statements below, the observation is reduced modulo \(q\). The significant change from previous bounded-secret arguments is to decompose the sample error at the source. After replacing the public matrix by a pseudorandom lossy matrix,

\[
A=BC+F,\qquad
sA+e=sBC+(s+g_t)F+e_2,
\]

the information about the secret is bounded by that in \((sB,s+g_t)\). The decomposition is possible when the target Gaussian width dominates \(t\|F\|\); Proposition 3.2 and Theorem 4.1 make this precise.

Theorem 4.1, p.16, assumes decisional LWE in source dimension \(k\), with discrete Gaussian width \(\gamma\). For target dimension \(n\), \(m\ge n\) scalar samples, and an \(r\)-bounded secret distribution, search hardness follows when

\[
\nu_t(S)\ge k\log_2\!\left(\min\{2C\gamma\sqrt n\,r,q\}\right)
+\omega(\log\lambda),\qquad
\sigma>C\sqrt m\,\gamma t.
\]

For decision hardness, the theorem instead uses \(\nu_t(S)\ge k\log_2q+\omega(\log\lambda)\), requires either prime \(q\) or binary \(s\), and states the additional decisional LWE assumption at target noise width. The binary alternative is useful: the ordinary linear hash family can extract from binary sources even without prime modulus.

Lemmas 5.2 and 5.4 distinguish arbitrary from bounded distributions. In their stated parameter regime,

\[
\nu_t(S)\ge H_\infty(S)-n\log_2(q/t)-1,
\qquad
\nu_t(S)\ge H_\infty(S)-\sqrt{2\pi n}\,(r/t)\log_2 e.
\]

The second estimate explains why binary and other bounded sources can fare much better than arbitrary sources of the same entropy. Hermite normal form also reduces the information carried by \(sB\), allowing the search entropy threshold to avoid dependence on \(q\) in the bounded regime. The polylogarithmic-entropy consequence uses a much stronger, subexponential LWE assumption and complexity leveraging; it is not a free consequence of polynomial-time hardness.

Sections 6–7 give two different limitations: explicit easy distributions when \(q\) has a suitable divisor, and a black-box barrier for general entropic distributions, including prime moduli. Their quantifiers matter. They do not rule out exploiting the particular geometry and product structure of the binary cube. Nor does the ordinary-LWE theorem immediately apply to the structured matrix obtained by expanding an RLWE sample.

**The supplied ring paper.** Brakerski–Döttling, *Lossiness and Entropic Hardness for Ring-LWE*, TCC 2020. [Local PDF](2020-1185.pdf), [ePrint](https://eprint.iacr.org/2020/1185).

The paper replaces ordinary low-rank lossiness with a short-basis construction. The public multiplication matrices take the form \(A_i=HZ_i\), where \(HZ_0=I\bmod q\), and the \(Z_i\) are short. The concrete construction samples short Gaussian \(f,g\), and uses

\[
a_i=(g/f)e_i+e'_i\pmod q.
\]

Single-ratio DSPR first makes \(g/f\) pseudorandom, and decisional Hermite-form RLWE makes the resulting collection of \(a_i\)'s pseudorandom. Thus the formal theorem assumes both DSPR and an RLWE assumption, even though the introductory informal statement emphasizes DSPR.

Theorem 6.9, p.22, states that for a \(B_{\rm err}\)-bounded source error distribution and \(k\) ring samples, it suffices that

\[
\nu_t(S)\ge n\log_2(\gamma\log n\sqrt n)+\omega(\log\lambda),
\qquad
\sigma_0\ge O(t\,n\log n\,B_{\rm err}\sqrt k).
\]

This is the paper's **mild search hardness** statement. Section 3 handles amplification and sample rerandomization. Those steps need attention when specifying a final Gaussian-error theorem: Lemma 3.4 uses an unbounded sample oracle, and the subset-sum construction of Lemma 3.5 produces bounded, generally non-Gaussian error distributions. The formal instantiation also inherits smoothing, invertibility, and singular-value hypotheses from Theorem 5.8 and Lemma 6.8; the imported estimates have ring/modulus conditions. The displayed formula should not be read as a theorem for arbitrary \(q\), arbitrary rings, and unrestricted sample counts at fixed noise.

The decisive binary obstruction is identified explicitly on pp.4–6. Moving the noise towards the secret eventually exposes a quantity of the form \(s+eZ_0\). Controlling its lossiness costs the information in a lattice coset. The relevant index is

\[
|\mathbb Z^n/\Lambda(Z_0)|=|\det Z_0|,
\]

whose logarithm is bounded using the largest singular value. The introduction describes the dominant cost as approximately \(n\log\gamma\); the formal bound includes further dimension factors. A uniform binary secret has only \(n\) bits, and \(\nu_t(S)\le n\). Increasing the masking noise can approach that ceiling but cannot pay a larger entropy cost. This is a limitation of the method, not a proved attack on binary RLWE.

The paper also explains how sufficiently wide Gaussian ratios eliminate the additional DSPR assumption via Stehlé–Steinfeld. Its resulting threshold is roughly \((1/2+\alpha)n\log q+O(n\log n)\), for the stated \(\alpha\)-range and statistical-error conditions. That route is even farther from binary entropy. Consequently, merely strengthening the running-time assumption does not repair this instantiated theorem: the entropy inequality itself fails.

**Related reductions and their relevance.**

| Work | What it contributes | Relation to binary rank-one RLWE |
|---|---|---|
| Order-LWE, ASIACRYPT 2019 | CRT-sensitive entropic security under RLWE and HLBDD | Binary coefficients are not shown to satisfy the required CRT condition |
| Binary Module-LWE, CT-RSA 2021 | Decision reduction with binary coefficients | Target rank must exceed a logarithmic threshold |
| Short distributions, J. Cryptology 2023 | Consolidated search/decision bounded-secret results | Does not cover rank one with constant-size coefficient alphabets |
| Module-NTRU to entropic Module-LWE, INDOCRYPT 2022 | Extends the supplied ring lossiness framework, preserving rank | Explicitly excludes binary secrets by its entropy condition |
| Entropic Module-LWE, TCS 2024 | Better module bounds and restricted entropic ring results | Binary module rank remains large; packed ring secrets are not binary |
| Ring LHLs, EUROCRYPT 2026 | General extraction bounds using ideals, smoothing, and leakage | New tools, rather than a binary RLWE hardness theorem |
| General-distribution MLWE, PKC 2026 | Search hardness for bounded error and joint secret/error distributions | Explicitly excludes module rank one |

1. **Bolboceanu, Brakerski, Perlman, Sharma — *Order-LWE and the Hardness of Ring-LWE with Entropic Secrets*, ASIACRYPT 2019.** Section 6 studies secrets in ideals and shows why total entropy alone is insufficient. Theorem 7.5 uses ordinary RLWE plus Hidden-Lattice BDD (HLBDD), together with bounded secrets satisfying a condition on selected CRT coordinates (Definition 7.1). Independence of binary coefficients is different from this CRT condition; the needed binary extraction statement is not established. This is an alternative conditional framework that remains relevant when considering assumptions. [Paper](https://eprint.iacr.org/2018/494.pdf).

2. **Boudgoust, Jeudy, Roux-Langlois, Wen — *On the Hardness of Module-LWE with Binary Secret*, CT-RSA 2021.** Theorem 2 reduces decision Module-LWE of rank \(k\) to binary-secret Module-LWE of rank
   \[
   d\ge(k+1)\log_2q+\omega(\log n).
   \]
   It preserves ring degree and modulus, with Gaussian-width growth \(\Theta(n^2\sqrt d)\) in the general cyclotomic statement, plus explicit modulus and sample conditions. Even a rank-one **source** produces a higher-rank **target**. The paper explicitly leaves constant target rank, particularly binary RLWE, open. [Paper](https://eprint.iacr.org/2021/265.pdf).

3. **The same authors — *On the Hardness of Module Learning With Errors with Short Distributions*, J. Cryptology 36(1), article 1, 2023 (online 2022).** This consolidates and extends their earlier reductions. Theorem 3.1 requires \(d\log_2(2\eta+1)\ge k\log_2q+\Omega(\log n)\) for search with coefficients uniform in \([-\eta,\eta]\); Theorem 3.2 uses \((k+1)\log_2q+\omega(\log n)\) for decision. Here \(\eta=1\) means ternary, not binary. The open-problems discussion and Figure 3.1 explicitly identify the rank-one limitation. [Paper](https://eprint.iacr.org/2022/472.pdf), [journal](https://doi.org/10.1007/s00145-022-09441-3).

4. **The same authors — *Entropic Hardness of Module-LWE from Module-NTRU*, INDOCRYPT 2022.** Theorem 5.2/Corollary 5.2 extend the short-basis lossiness construction to modules. Their main route uses rectangular Module-NTRU directly, removing the separate HNF-MLWE assumption, and preserves rank. The comparison discussion explicitly observes that binary secrets, with entropy \(nd\), never meet the corollary's entropy requirement. This is the most direct continuation of the supplied TCC paper, and a useful source for improved singular-value analysis. [Paper, especially Sections 5–6](https://eprint.iacr.org/2022/245.pdf).

5. **Lin, Wang, Zhuang, Wang — *Hardness of Entropic Module-LWE*, Theoretical Computer Science 999 (2024), 114553.** Earlier versions appeared as *Hardness of Module-LWE and Ring-LWE on General Entropic Distributions*. Lemma 18 gives search binary Module-LWE from primal decisional RLWE with \(d>11\log q\), \(m>n\), and \(\alpha>6c\sqrt m\,\beta\), in its normalization. Section 5 packs module secrets with \((1,q,\ldots)\), raising the modulus. Theorem 10 requires entropy at least \(n\log q+5.5M\sqrt n/\alpha'\), plus bounded digits; it does not cover an \(n\)-bit coefficient-binary secret. Its decision results also require appropriate entropy in prime-ideal projections. [Published PDF](https://pure.tudelft.nl/ws/portalfiles/portal/186654080/1-s2.0-S0304397524001683-main.pdf), [ePrint](https://eprint.iacr.org/2020/1238).

6. **Boudgoust–Lapiha — *Leftover Hash Lemma(s) Over Cyclotomic Rings*, EUROCRYPT 2026, ePrint 2025/1080.** Theorems 4–5 organize extraction bounds around the ideal generated by differences of independent source samples, including conditional collision probabilities under leakage. Theorem 6 gives the Gaussian smoothing approach; later results treat leakage. Corollaries distinguish low-splitting conditions, where short nonzero differences can be units, from bounds using entropy modulo ideals or spread across CRT coordinates. This provides a useful framework for reassessing extraction arguments. It does not assert binary RLWE hardness. Full text obtained from the authors' HAL deposit; introduction and main theorem statements checked. [Paper record](https://eprint.iacr.org/2025/1080), [HAL manuscript](https://hal.science/lirmm-05396888v2/document), [local PDF](related/2025-1080.pdf).

7. **Boudgoust, Jeudy, Tairi, Wen — *Hardness of M-LWE with General Distributions and Applications to Leaky Variants*, PKC 2026, ePrint 2025/1472.** Establishes search results for bounded high-entropy error distributions with sample restrictions, then HNF results for joint secret/error distributions and leakage. Section 1.2, printed p.6, explicitly excludes rank one. Although Theorem 4.1 formally permits \(d=k\), at equality its entropy/ball-counting bound is vacuous: the ball contains the source support. This last observation is our parameter check. Theorem 5.1 preserves rank, so a mixed binary-secret/Gaussian-error distribution does not escape the restriction. Full text obtained from HAL; these statements and their relation were checked. [Paper record](https://eprint.iacr.org/2025/1472), [HAL manuscript](https://hal.science/lirmm-05396885v2/document), [local PDF](related/2025-1472.pdf).

**Assumptions and cryptanalysis worth carrying forward.**

- **Pellet-Mary–Stehlé, *On the Hardness of the NTRU Problem*, ASIACRYPT 2021.** Provides worst-case ideal-lattice hardness for a particular average-case search NTRU variant, and a reduction from another search variant to decision NTRU. The distributions and search tasks differ. This updates the 2020 landscape, but is not an automatic worst-case justification for narrow Gaussian DSPR. Its introduction explains the distinctions. [Paper](https://eprint.iacr.org/2021/821.pdf).
- **Ducas–van Woerden, *NTRU Fatigue: How Stretched is Overstretched?*, ASIACRYPT 2021.** Refines attacks exploiting the dense sublattice in overstretched NTRU instances. Relevant to any proposal that reduces denominator size while increasing modulus or noise: plausibility must be evaluated at the actual DSPR parameters. [Paper](https://eprint.iacr.org/2021/999).
- **Boudgoust–Gachon–Pellet-Mary, *Some Easy Instances of Ideal-SVP and Implications on the Partial Vandermonde Knapsack Problem*, CRYPTO 2022.** Finds easy instances associated with ideal symmetries and attacks some partial Fourier-recovery settings. Relevant when formulating assumptions about selected CRT coordinates. This is not a demonstrated break of HLBDD or binary RLWE. [Paper](https://eprint.iacr.org/2022/709).
- **Hou–Jiang–Ogilvie, *Careful with the Ring! Concrete Hardness Gaps Between LWE and MLWE*, CRYPTO 2026.** Ring symmetries improve hybrid attacks, especially for sparse secrets. This reinforces the need to distinguish dense uniform binary secrets from fixed-weight sparse distributions and to account for ring structure in concrete estimates. It does not establish a polynomial-time attack on the target problem. The merged publication combines ePrints 2026/279 and 2026/366; figures can differ between versions. [Published paper](https://doi.org/10.1007/978-3-032-35377-1_15), [updated full version (b)](https://eprint.iacr.org/2026/366).

For the ordinary-LWE baseline, the relevant chain is Goldwasser–Kalai–Peikert–Vaikuntanathan, *Robustness of the Learning with Errors Assumption* (ICS 2010); Brakerski–Langlois–Peikert–Regev–Stehlé, *Classical Hardness of Learning with Errors* (STOC 2013); and Micciancio, *On the Hardness of Learning With Errors with Binary Secrets* (Theory of Computing 2018). Micciancio gives a direct decision reduction with arbitrary polynomially many target samples and a bounded source sample count. [GKPV](https://www.mit.edu/~vinodv/papers/ics10/robustlwe.pdf), [BLPRS](https://arxiv.org/abs/1306.0281), [Micciancio](https://www.theoryofcomputing.org/articles/v014a013/).

**What this review establishes for the next discussion.** The identified obstacles are specific: ordinary lossiness spends a freely chosen lower-dimensional projection; ring short-basis lossiness spends a lattice-coset index; binary module reductions increase module rank. A future result must specify which of these restrictions it changes. A stronger complexity assumption alone cannot fix an information-theoretic inequality that excludes binary entropy. Search versus decision, finite versus arbitrary sample counts, the coefficient basis, and the precise source distribution must remain explicit when composing reductions.

The two supplied papers and the central 2019–2024 follow-ups were examined at the level of arguments and theorem conditions. The relevant statements in the two 2026 tool papers were also checked after obtaining author-deposited manuscripts; both PDFs are saved under `literature/related/`. The attacks and ordinary-LWE predecessors were checked selectively for relevance. This is a literature review rather than a proof audit or a research plan. Bibliographic records are in [related.bib](related.bib).
