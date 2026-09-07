# Binary-secret RLWE: discussion and research record

Prepared on 7 September 2026. This note records the discussion and the resulting work through the completion of the third research run. It is a synthesis of the conversation and saved artifacts, not a verbatim transcript, a new literature search, or a proof certificate. All run times below are UTC.

**Current position.** We have a reviewed conditional, one-pair hardness implication for binary-secret RLWE from pseudorandomness of a simpler noisy-hidden-ideal source with independent second noise. That source's computational hardness remains unsupported in the precise form needed for negligible reduction loss. We have also identified several restricted obstructions and a subexponential distinguishing algorithm for the proposed source family. We have neither a complete hardness theorem for the original problem nor a polynomial-time distinguisher for the latest source candidate. The latest bounded run finished normally, and no research run remains active.

## 1. The original question

The starting point was the work with Zvika Brakerski on LWE with binary secrets. For ordinary LWE, the question concerns recovering a uniformly random $s\in\{0,1\}^n$ from

$$
(A,sA+e),\qquad A\leftarrow\mathbb Z_q^{n\times m},
$$

with suitable Gaussian error. The aim of returning to the problem was to understand under which reasonable assumptions one might establish the analogous hardness for **rank-one Ring-LWE with independent binary coefficients**.

For comparison across the investigations, we fixed the representative ring

$$
R_q=\mathbb F_q[X]/(X^n+1),\qquad
S=\sum_{j=0}^{n-1}S_jX^j,\quad S_j\overset{\$}{\leftarrow}\{0,1\},
$$

where $n$ grows through powers of two. The desired samples are $(a_i,a_iS+E_i)$, with independent uniform $a_i$ and independent coefficient Gaussian errors. Our convention is $D_t(z)\propto\exp(-\pi z^2/t^2)$, wrapped modulo $q$; $t$ denotes Gaussian width, not standard deviation. The main comparison regime has polynomially bounded $q$ and $q/\sigma\ge n^c$ for a fixed $c>0$.

This reference setting does not assert hardness for all such parameters. It also does not identify module rank, ring degree, and sample count: one ring sample supplies structured scalar equations, and its rotations are not independent fresh samples. The original objective concerns recovery from potentially polynomially many samples. Most of the new reduction work below concerns **decision indistinguishability for one pair**, leaving a substantive gap to that objective.

## 2. Reading the original papers and assessing related work

The first request was to read the two supplied papers and search for related research before making a plan. The detailed results are in the [initial literature review](../literature/reading-notes-2026-09-05.md), with references in [related.bib](../literature/related.bib).

### The two supplied papers

**Brakerski–Döttling, *Hardness of LWE on General Entropic Distributions*, EUROCRYPT 2020.** [Local PDF](../literature/2020-119.pdf), [ePrint 2020/119](https://eprint.iacr.org/2020/119).

The organizing quantity is noise lossiness: how much uncertainty remains about a secret after an auxiliary Gaussian perturbation. A pseudorandom lossy matrix and a noise decomposition reduce the information about the secret to a lower-dimensional projection together with a noisy secret observation. Bounded distributions, including binary secrets, can retain more useful entropy than a generic entropy-only estimate suggests. The search and decision statements have different entropy thresholds and assumptions.

**Brakerski–Döttling, *Lossiness and Entropic Hardness for Ring-LWE*, TCC 2020.** [Local PDF](../literature/2020-1185.pdf), [ePrint 2020/1185](https://eprint.iacr.org/2020/1185).

The ring construction uses short bases and Gaussian ratios, with DSPR and an RLWE assumption in its formal theorem. Moving noise toward the secret leads to information about a lattice coset. The associated entropy cost, bounded through a lattice index and singular values, exceeds the $n$ bits available in a coefficient-binary secret in the stated instantiation. Making the complexity assumption stronger does not by itself repair that failed entropy inequality. The paper's mild search result, amplification, error conventions, and sample requirements must also be kept distinct when composing a final theorem.

### Related works identified

The following is a compact record of the earlier search, not a claim to have exhaustively surveyed the literature as of this note's date.

| Work | Relevance and limitation for our target |
|---|---|
| Bolboceanu–Brakerski–Perlman–Sharma, [*Order-LWE and the Hardness of Ring-LWE with Entropic Secrets*](https://eprint.iacr.org/2018/494.pdf), ASIACRYPT 2019 | A distinct conditional framework involving hidden-lattice BDD (HLBDD) and entropy in selected CRT coordinates. Coefficient independence alone does not establish its required CRT condition. |
| Boudgoust–Jeudy–Roux-Langlois–Wen, [*On the Hardness of Module-LWE with Binary Secret*](https://eprint.iacr.org/2021/265.pdf), CT-RSA 2021 | Binary-secret decision reductions, but the target module rank exceeds a logarithmic threshold. A rank-one source does not yield a rank-one binary target. |
| The same authors, [*On the Hardness of Module Learning With Errors with Short Distributions*](https://eprint.iacr.org/2022/472.pdf), J. Cryptology 2023 | Consolidates and extends short-secret search and decision reductions; does not reach rank one with constant-size coefficient alphabets. |
| The same authors, [*Entropic Hardness of Module-LWE from Module-NTRU*](https://eprint.iacr.org/2022/245.pdf), INDOCRYPT 2022 | A direct continuation of the short-basis lossiness approach, with an improved source interface and rank preservation. Its entropy requirement still excludes binary secrets. |
| Lin–Wang–Zhuang–Wang, [*Hardness of Entropic Module-LWE*](https://eprint.iacr.org/2020/1238), TCS 2024 | Improved module bounds and restricted entropic ring results. Binary module rank remains large; packing module secrets into a ring does not preserve coefficient-binary secrets. |
| Boudgoust–Lapiha, [*Leftover Hash Lemma(s) Over Cyclotomic Rings*](https://eprint.iacr.org/2025/1080), EUROCRYPT 2026 | Extraction tools based on ideals generated by source differences, smoothing, and conditional collision probabilities under leakage. These are useful new tools, not a binary-RLWE hardness theorem. |
| Boudgoust–Jeudy–Tairi–Wen, [*Hardness of M-LWE with General Distributions and Applications to Leaky Variants*](https://eprint.iacr.org/2025/1472), PKC 2026 | General error and joint secret/error distributions, with search and leakage results. The relevant results exclude the rank-one case. |

Additional checks concerned NTRU hardness, overstretched NTRU, ideal symmetries and partial Vandermonde decoding, and concrete differences between LWE and Module-LWE. These matter when evaluating a proposed source assumption at its actual parameters; none was treated as a demonstrated polynomial-time break of dense coefficient-binary RLWE. The ordinary-LWE background included GKPV, BLPRS, and Micciancio's binary-secret reduction; bibliographic details are in the initial review.

### Are the follow-ups new ideas or extensions?

Our assessment was mixed. Much of the direct follow-up literature extends the range of existing lossiness, bounded-secret, or module techniques, often improving assumptions and quantitative bounds in substantial ways. The ring leftover-hash results and the Order-LWE/HLBDD framework offer different structural tools worth importing. Nevertheless, the identified results do not remove the specific obstacles of binary entropy, rank one, and the required source distribution simultaneously.

The adjacent [NTRU hardness work of Pellet-Mary–Stehlé](https://eprint.iacr.org/2021/821.pdf) is a more substantial conceptual departure. Its different source distributions and search tasks still do not automatically justify the narrow Gaussian DSPR assumption used in the earlier ring construction.

That motivated a broad search for structural ideas. It did not establish that every future solution must abandon all earlier methods, or that the follow-ups contain no conceptual innovation. The useful question became: **which structural restriction can a new idea actually change?**

## 3. The broad exploratory run

The request was for a broad, multidisciplinary multi-agent investigation, potentially drawing on areas such as statistical mechanics and algebraic geometry. It was explicitly to be a finite run with limited objectives and a maximum duration, **not a goal run**. The selected model was **Astra with ultra reasoning**, retained for subsequent research runs.

The [broad plan](../exploration/PLAN.md) used twelve scouts, with some initially given only the formal problem and others also given the known barriers. Their work covered planted distributions and partition functions; posterior transport; ring towers; Fourier analysis and random walks; Boolean fibers and algebraic codes; exact lossiness; likelihood moments; symmetries; coding and knapsack sources; and quantum sampling. Three candidates received further development and nonauthor criticism. Six bounded experiments supplied diagnostics.

| Run | Maximum | Actual interval on 6 September | Outcome |
|---|---|---|---|
| Broad exploration | 6 hours | 09:11:38–10:54:26 | Completed early after the assigned exploration and criticism. |
| First joint-ideal investigation | 5 hours | 14:21:13–15:59:48 | Interrupted by a `cyber_policy` error; reviews survived, final reconciliation was unfinished. |
| Joint-foundations investigation | 5 hours | 19:54:15–21:10:51 | Completed normally after investigation, review, reconciliation, and artifact checks. |

The broad run's [final report](../exploration/runs/brlwe-explore-20260906-astra-ultra/final.md) retained three useful pieces of mathematics, with different limitations.

**Conditional extraction through special ring quotients.** For the specified binomial family $R_q/(X^d-a)$, take a fully splitting polynomially bounded prime $q$, a power-of-two divisor $L=\Theta(\log^3 n)$ of $n$, $d=n/L$, and $a$ of order $2L$. The binary coefficients split into weighted blocks. Fourier collision calculations and [Breuillard–Varjú's affine random-walk mixing theorem](https://arxiv.org/abs/1909.09053) yield near-uniformity of the quotient secret even given independent noisy coefficient observations $Y=S+G_\tau$, with $\tau\ge\tau_0>0$. This was the strongest concrete import from another area; it is not an assertion for arbitrary binomial quotients or arbitrarily vanishing auxiliary noise.

The obvious accompanying small-noise ideal sampler, however, is efficiently distinguishable by block enumeration when $q$ is polynomially bounded. Hiding the binomial parameter among polynomially many choices does not fix this. Thus the extraction statement survived while that computational source did not.

**Lossiness of the actual public transcript.** The run distinguished the information in the public sample from information in a more revealing proof precursor. Exact binary entropy after revealing a lattice coset depends on the number of occupied cosets,

$$
\widetilde H_\infty(S\mid S\bmod\Lambda)
=n-\log_2 N_{\rm occ}.
$$

This can be more informative than a determinant bound, and examples showed that a precursor can disclose substantially more than the transcript. These observations sharpen the missing entropy statement; they do not provide a pseudorandom public sampler with the necessary lossiness.

**A noise-transfer calculation.** Centering a binary-noise simulation before adding Gaussian noise improved a reverse Rényi-moment bound, giving polynomial loss under a condition of the form $n/\sigma^4=O(\log n)$. The calculation preserves the planted witness and applies to a one-sample search transfer. Its proposed knapsack source, after normalization, was too close to binary-secret/binary-error RLWE to supply an independently supported hardness explanation. The transfer lemma was retained; that explanation was retired.

Other approaches produced useful failures of specific mechanisms, including statistical quiet planting to uniform, missing correlated responses in tower constructions, and restricted exact symmetry transformations. These were not general impossibility theorems.

## 4. From extraction to a computational reduction

The next question in the discussion was how an apparently information-theoretic extraction result could help prove computational hardness.

The proposed connection was to use a public multiplier that is computationally indistinguishable from uniform but has a hidden ideal structure. Let $J$ be an ideal, $I=\operatorname{Ann}(J)$, and $Q=R_q/J$. If multiplication by $U\in I$ maps $Q$ bijectively to $I$, then replacing $S\bmod J$ by a uniform quotient element makes $US$ uniform in $I$.

We considered a source pair

$$
(A,C)=(U+F,V+H),\qquad V\leftarrow\operatorname{Unif}(I).
$$

The computational premise concerns this **joint pair versus two independent uniform ring elements**. Separate claims about the two marginals do not suffice. In particular, correlations between $F$ and $H$ are part of the assumption.

With $Y=S+G$, the intended proof uses two statistical comparisons:

$$
\begin{aligned}
\operatorname{TV}((J,U,F,FG+H),(J,U,F,E))&\le\eta_N,\\
\operatorname{TV}((J,U,F,H,Y,\pi_J(S)),
 (J,U,F,H,Y,Z))&\le\eta_X,
\end{aligned}
$$

where $\pi_J$ is the quotient map, $E$ has the independent target-noise law, and $Z$ is conditionally independent uniform in $Q$. Here $S$ and $G$ are independent draws, jointly independent of the source tuple; the replacement $E$ is independent of that tuple and the secret jointly. The complete independence conventions are essential: the first comparison integrates out $H$, whereas the second retains it.

Starting from $AS+E$, noise completion gives $US+FY+H$, and extraction gives $UZ+FY+H$. Writing $K=Z-\pi_J(Y)$ converts the latter into $AY+(UK+H)$. Under the bijectivity condition, $UK$ is an independent uniform ideal point. This connects to the source using the public transformation $(a,c)\mapsto(a,ay+c)$, which preserves a uniform pair for every fixed $y$.

The resulting conditional bound uses two potentially different source distinguishers and costs $\eta_N+\eta_X$, before implementation errors. It explains the role of extraction, but **does not prove the source premise**. That distinction led to the first focused five-hour investigation.

## 5. The first focused investigation and its consolidated results

After showing the [focused plan](../exploration/joint-ideal/PLAN.md) and receiving explicit launch approval, the run investigated the exact bridge, noise completion, computational sources, attacks, and multiple samples. Its partial report was later superseded, for the mathematical state, by the [consolidation](../exploration/consolidated/joint-ideal-20260906/CONSOLIDATED.md).

### A common analytic regime

The candidate called **A2** uses

$$
\ell=\lceil\log_2 n\rceil,\quad
d=\lfloor\sqrt n/\ell^4\rfloor,\quad
b=\ell^2,\quad \tau=\ell,\quad \sigma=2n\ell^3,
\qquad \sigma n^c\le q\le n^K.
$$

Here $q\equiv1\pmod{2n}$ is prime, $T$ is a uniform $d$-subset of the CRT roots, and $I_T$ is the ideal supported on $T$. The active coordinates of $U$ are independently uniform nonzero elements, while $V$ is uniform in $I_T$, including zeros. The coefficients of $F$ are independent $D_\ell$ draws conditioned on $[-b,b]$.

Writing $M_F$ for integer negacyclic multiplication by $F$, the completion shape matrix is

$$
B_F=\sigma^2\operatorname{Id}-\tau^2M_FM_F^{\mathsf T}.
$$

The actual mathematical completion law is a canonical coefficient-order **sequential discrete Gaussian** derived from an LDL factorization. It has adaptive centers and conditional normalizers. It must not be identified with a globally normalized lattice Gaussian merely because the shape matrices agree. In particular, $B_F$ is not the actual covariance matrix of this discrete law.

The extraction work extended beyond binomial quotients to **every support of size $d$ in the smaller stated range**, using a joint affine-walk theorem and a Mahler-measure bound. Thus two different results must be kept separate: special quotients at dimension approximately $n/\log^3 n$, and arbitrary supports at approximately $\sqrt n/\log^4 n$. The larger dimension for arbitrary supports is unproved, not refuted.

Noise and extraction errors are negligible in the common asymptotic regime, subject to the recorded analytic dependencies and finite guards. The example $c=1,K=16$ uses a qualifying prime-existence argument; no practical parameter threshold was established. The exact source-hardness premise, called **P0-A2**, remains open.

### Attacks, repairs, and alternatives

A deterministic grouped-orbit algorithm using exact SVP distinguishes the first source component in time

$$
\exp(O_c(d))\operatorname{poly}(n,\log q),
$$

with very high advantage in the stated regime. This is subexponential in $n$ but superpolynomial at A2. It constrains plausible security claims without refuting polynomial-time hardness. The repaired theorem states the strict norm conditions, root inputs, rounding, and solver costs explicitly.

The noise-completion lemma also needed a genuine correction: an earlier denominator bound became negative outside its domain. The corrected version uses guarded, piecewise bounds; the intended asymptotic regime satisfies the guards. Both this repair and the attack repair received fresh nonauthor checks.

An alternative public shear inherited a source distribution correctly, but its tested completion retained an inverse-polynomial noise discrepancy. That defeats this particular negligible-error route, not every public transformation or every possible completion.

### Multiple samples

One-pair hardness cannot simply be tensorized. Sharing $Y$ across samples leads to a common quotient variable $K$ and ideal points $U_iK$, rather than independent $V_i$. A correct completion requires a stacked completion matrix with cross-sample blocks and a separate source premise, called Pm. The sufficient target width grows by $\sqrt m$.

Using separate observations $Y_i=S+G_i$ creates a different problem: sufficiently many observations reveal too much of $S$ for the required extraction. The consolidated analysis quantifies this in the stated auxiliary model. It is not a claim that the public RLWE samples themselves reveal those observations. Search-to-decision transfer also needs its own sample budget and residual-verification bounds. None of these obligations follows from the one-pair result.

## 6. The interruption, feedback, and execution changes

The first focused run exited after about 98 minutes with a persisted **`cyber_policy`** error. It was a content-policy termination, not a sandbox/tool-permission rejection sent through automatic approval review. The exact triggering passage and classification rationale were not available. Given the purely academic mathematical task, we reported it as a **suspected false positive**, not as a confirmed diagnosis of the classifier.

The clarification about “review” had two meanings. The platform event did not enter the tool-approval review route. Separately, the research run **had already completed three mathematical critic reports and additional rechecks**. What the termination prevented was the coordinator's final reconciliation and normal completion. The saved work was therefore recoverable, but the interrupted run's partial final report was not a reliable final synthesis.

The user authorized reporting the incident. A feedback report was successfully submitted on 6 September at 18:09:59 using the installed Codex feedback interface. It included the session, model, timestamp, error, and academic scope; logs and research attachments were excluded. The receipt establishes submission, not a support resolution. See the [incident report](../exploration/incidents/2026-09-06-cyber-policy-feedback.md) and [submission receipt](../exploration/incidents/2026-09-06-feedback-receipt.json).

At the user's request, the preparation for the next run added:

1. A complete academic scope and precise mathematical task in every assignment.
2. Rolling claim, objection, progress, and partial-report records, with roughly five-minute checkpoints and preserved snapshots.
3. A separate supervisor with a hard runtime limit, structured error monitoring, and a final exit manifest even after research interruption.
4. Explicit separation of process success, saved-artifact integrity, and mathematical completeness; no automatic restart, resume, or rerouting after an error.

Historical quoted error messages were excluded from being treated as fresh confirmed failures. Alerts remain local files and logs, rather than push notifications. These changes preserve evidence and make failures legible; they do not guarantee that content-policy interruptions cannot recur. The runner changes passed 37 unit tests before the next launch. The [runner documentation](../exploration/runner/README.md) records the implementation and verification limits.

The old results were consolidated, a [new plan](../exploration/joint-ideal-next/PLAN.md) was presented, and the user separately approved its launch. All research runs were finite, used Astra ultra, and allowed at most three workers alongside the coordinator. No goal run or automatic continuation was authorized.

## 7. The latest run: simplifying the computational premise

The latest run split the work into public source reductions, structural algorithms, and an alternative public reduction. It developed the first and third directions, reviewed the structural results, and left the multiple-sample extension deferred. It completed normally at **21:10:51 UTC on 6 September**, about 1 hour 16 minutes after launch, because the assigned work and review obligations had reached bounded dispositions.

The main advance is an independent-noise source:

$$
\mathsf{Src}_{\rm ind}=(U+F,V+E_\sigma),
$$

with independent second error. The correlated completion $\widehat H=H_{\rm seq}(F)$ is now used **only as a coupling inside the proof**. Neither the source experiment nor the public reduction needs to sample it.

### The public tests and the bound

For a target distinguisher $D$, the tests are

$$
B_1(a,c)=D(a,aS+E),\qquad
B_2(a,c)=D(a,aS_0+c),
$$

where the secrets and target error are fresh independent draws. The second test now uses a fresh binary $S_0$, rather than the earlier noisy auxiliary $Y$.

Under the complete product-kernel law and the retained noise/extraction premises, the reviewed statement gives

$$
\operatorname{Adv}_{\rm target}(D)
\le\operatorname{Adv}_{\rm ind}(B_1)
+\operatorname{Adv}_{\rm ind}(B_2)
+2\eta_N+\eta_X+\eta_{\rm iso},
$$

before the separately specified sampling errors, with

$$
\eta_{\rm iso}=\mathbb E\left[1-\frac{|UR_q|}{|I_T|}\right].
$$

The extra use of the noise-comparison lemma converts $F(S_0+G_0)+\widehat H$ back into $FS_0+E_0$ after extraction. This is why the new bound has **two** noise-error terms. A uniform ideal translation then yields the public second test. The full argument is in the [edited observable-bridge proof](../exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/candidates/observable/statement-and-proof-v2.md).

### Active points versus ordinary uniform ideal points

If $U$ is nonzero on every coordinate in $T$, multiplication has full image $I_T$ and $\eta_{\rm iso}=0$. This gives negligible statistical loss in the analytic regime. **Hardness of this exact active-point independent-noise source is still unsupported.**

If $U$ is instead uniform in $I_T$, then

$$
\eta_{\rm iso}=1-(1-1/q+1/q^2)^d\asymp d/q.
$$

This differs from the latent conditioning cost

$$
\delta_{\rm act}=1-(1-1/q)^d
$$

for conditioning all active coordinates to be nonzero. Both are nonnegligible at the fixed polynomial modulus scale. Merely choosing a large fixed exponent for $q$ does not make them negligible against every inverse-polynomial advantage.

A public independent-noise broadening map connects an explicitly defined ordinary uniform-point, same-ideal HLBDD source to the uniform-point version of our source, up to negligible Gaussian and truncation errors. It preserves the law of $U$ and therefore leaves the rank defect. Moreover, the cited HLBDD framework treats its source hardness as an assumption; the run did not derive that assumption from worst-case lattice hardness at our parameters.

In the strict norm regime, an explicit **exponential-time** public test shows that the two relevant observable hybrid distributions differ by essentially $\eta_{\rm iso}$. Thus this statistical discrepancy is not merely an artifact of retaining hidden variables. It does not give a polynomial-time source attack, or rule out a different computational reduction.

### What the other workstreams established

The source-conversion work produced restricted obstructions. In particular, for the specified broad independent-noise input, a stochastic map that preserves the uniform pair **exactly** cannot approximate the original correlated A2 source with negligible total variation in the proved regime. The scope excludes small-noise starting sources and merely approximate preservation of the uniform comparator.

A hypothetical repeatable polynomial-time public sampler for the latent completion kernel from $A$ alone, with fresh independent coins and uniform negligible error, would permit recovery of $FF^\dagger$ through covariance estimates and yield a polynomial-time distinguishing test. Here $F^\dagger$ denotes the negacyclic adjoint, induced by $X\mapsto X^{-1}$. No such sampler was constructed or supplied by the source challenge. General transformations that also use the second component remain outside that statement. Posterior-sampling examples separately showed why correct behavior on a source distribution does not ensure correct behavior on uniform input.

The structural work reviewed orbit occupancy, subgroup coverage, scalar cancellation, and a specified partial-Vandermonde search transfer. It obtained no polynomial-time or $\exp(o(d))$ algorithm. A better constant relative to an older conservative bound did not improve the optimized prior $\exp(O(d))$ algorithm.

### Review and evidence status

A blind review found a missing full-joint-independence hypothesis in an intermediate general theorem packet. An exact $\mathbb F_3$ counterexample refuted that literal version. The corrected proof specified the product law and passed a fresh nonauthor recheck, including additional finite controls. The rejected version remains in the record.

The frozen author proof still has a historical “pending recheck” header; the subsequent [recheck](../exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N02/review-v1.md), [claim ledger](../exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/claims.json), and [reconciliation](../exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/reconciliation.md) record the later disposition. Favorable agent review is bounded scrutiny, not a formal certificate. Imported analytic dependencies remain globally provisional.

All workers finished, experiments returned, and twenty final saved-artifact checks passed. These checks verify consistency and preservation, not the mathematics. One earlier Gaussian diagnostic JSON was overwritten during a correction; the final corrected data, earlier stdout, and a labelled source reconstruction are retained, with the limitation documented. High-precision numerical diagnostics were not interval-certified proofs.

The [final research report](../exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/final.md) records mathematical completion within scope. The separate [exit manifest](../exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/exit-manifest.json) confirms exit code zero, an inactive service, and no recorded failure category or alerts. There was no content-policy interruption in this run.

## 8. Where the discussion leaves us

| Question | Present state |
|---|---|
| Can binary coefficients become uniform in useful ring quotients despite noisy coefficient observations? | Positive conditional-extraction results for the specified special quotients and smaller arbitrary supports. |
| Can this extraction participate in an efficient public reduction? | Yes, conditionally, for one pair with explicit joint laws and quantitative losses. |
| Must the computational source include the correlated completion noise? | No. The latest reduction keeps that noise inside the proof and uses independent second source noise. |
| Is the original correlated A2 source justified by an established reduction? | No; P0-A2 remains open. |
| Is the active-point independent-noise source justified with negligible loss from the ordinary uniform-point source? | No; this is the clearest remaining computational question. |
| Is there a polynomial-time distinguisher for the latest candidate? | None was obtained. The reviewed distinguishing algorithm is superpolynomial at the chosen parameters. |
| Does the work prove the original multiple-sample search-hardness goal? | No. Multiple samples and the corresponding task conversion remain separate obligations. |

The most discriminating next question proposed in the discussion is:

> Can the explicitly specified active-point, same-ideal HLBDD source inherit hardness from the ordinary uniform-point source, or another independently motivated assumption, with negligible total distinguishing loss in the fixed polynomial-modulus regime?

A positive answer would provide the missing computational premise for the independent-noise route, subject to the retained analytic dependencies. It would not by itself prove hardness of the original correlated A2 source, nor settle the multiple-sample objective. Other possibilities left open by the restricted obstructions include transformations using both public components and controlled approximate preservation of the uniform comparator. These are unresolved avenues, not newly approved or launched investigations.

The progression of the discussion was therefore from a broad search for structural ideas, through conditional quotient extraction, to an explicit computational source problem, and finally to a simpler source assumption with a sharply identified active-coordinate gap. The saved reports preserve both the useful implications and the failed shortcuts needed to assess a future proposal.
