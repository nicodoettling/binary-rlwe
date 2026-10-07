# RS1 v1 — source, parameter, and scientific-scope referee report

**Disposition: PASS WITH EXPLICIT SCOPE QUALIFICATIONS for the source interpretation and the two concrete effective parameter families. The source-hardness premise itself remains OPEN. Full mathematical acceptance of (F), (I), and (A) is outside this referee's bounded assignment and remains pending the other exact-proof reviews.**

If those mathematical gates close, the packet gives a meaningful new conditional PPT search-hardness implication for **exactly one or two** binary-secret ring samples, from a separately defined, literature-motivated noisy hidden-ideal source at polynomial modulus. It does not settle the original polynomially-many-samples recovery objective. The general interval for d is an analytic range, not a claim that every associated computational premise is plausible; it includes demonstrably easy sources. General computability of d is weaker than polynomial-time generation of the complete source family.

## 1. Frozen input, procedure, and limits

The complete assignment is in [assignment.md](assignment.md). I used the mathematical-proof-audit skill and read both its audit protocol and probability-regressions reference. I read launcher-run.json and its **cap.status_file**, which records start 2026-09-07T21:34:27.111419+00:00, wrap-up 2026-09-08T00:14:27.111419+00:00, graceful shutdown 00:33:22.111419+00:00, and hard cap 00:34:27.111419+00:00. My assigned earlier research deadline is 2026-09-07T22:25:00Z. A partial was saved before 22:07 UTC. No agents, goals, mathematical experiments, services, package installation, or external communications were used. RB1 was neither read nor contacted.

| Immutable input | SHA256 verified and copied to RS1/input |
|---|---|
| workers/A1/theorem-only-v2.md | bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124 |
| workers/A1/proof-v1.md | 198c36bce9a73b87f2e1f5cf644d7e96b13cda063922f1ab10b0b2ee60114042 |
| workers/A1/supplement-v1.md | 71752406e81e327b5c47d0d118ea9bc6aa0f87566d23345daf290a7b8322410a |
| coordinator/source-and-parameters-v1.md | 131e6a3feec87010007a30ddc1e37bdec44687648120bfe1e8c5187e6e779f50 |

[input-hashes.json](input-hashes.json) records the copies. [additional-input-hashes.json](additional-input-hashes.json) freezes supporting local inputs and confirms equality with the historical hash index wherever an entry exists. Hashing a file does not assert a full reproof of its contents. The review uses the previous run's final report, selected current claim entries, reconciliation, source comparison, parameter table and target, plus the specifically identified frozen source/attack dossiers and reviews. It does not promote their global PROVISIONAL labels to certification.

This referee shares the requested Astra ultra model with the other workers. The review is correlated mathematical scrutiny, not independent statistical evidence. My scope is imported source statements, parameter algebra, effectiveness, source plausibility relative to permitted attacks, novelty relative to the checked record, and scientific endpoint. Reading the author proof to identify dependencies is not certification of its rectangular Gaussian calculation.

## 2. Primary sources, locations, and what they actually supply

### 2.1 Order-LWE / HLBDD

Primary checked locations: Section 2.2.1, printed pp. 9–10 (Gaussian convention); Section 2.3.2, p. 13 (canonical embedding); Section 7, pp. 37–41, especially Definitions 7.3–7.4, p. 38, and Lemma 7.7, pp. 40–41. Definition 7.3 picks a uniform intermediate lattice and a uniform quotient point with ambient discrete Gaussian noise. Definition 7.4 specifies two samples, but its repeated-lattice convention and comparator notation are terse. Lemma 7.7 H3/H4 explicitly uses two uniform points of the same Q/qR and ends at uniform Rq × Rq. Section 7 uses the discrete integral primal convention. Its application assumes HLBDD hardness; the H3 transition explicitly invokes superpolynomial q, and its noise steps require swallowing. These statements supply motivation and the intended source interface, not hardness at A1's polynomial q and widths. [Order-LWE full version](https://eprint.iacr.org/2018/494.pdf#page=38).

### 2.2 Xylouris

The paper defines P(a,Q) for coprime positive integers on printed p. 65. Theorem 1.1 on printed p. 66 states P(a,Q) <= C Q^5.18 with effectively computable C. This is a theorem imported as published; this bounded referee checks the statement and its substitution, not the analytic-number-theory proof. [Xylouris, Theorem 1.1](https://www.impan.pl/shop/publication/transaction/download/product/83078#page=2).

### 2.3 Ordinary entropic LWE

Theorem 4.1, printed p. 16, proves search hardness under a noise-lossiness threshold from ordinary decision LWE. Section 4's construction uses an unstructured lossy matrix and a Gaussian decomposition; the technical overview on printed pp. 5–6 explains revealing a projection plus the noisy secret. Its formal Gaussian decomposition is continuous. This supports the ancestry of A1's method, not a black-box theorem for negacyclic multiplication matrices or the exact discrete completion used here. [Brakerski–Döttling, 2020/119](https://eprint.iacr.org/2020/119.pdf#page=16). The supplied local PDF hash is c69651af78208bad640aa817afcb338e574215448dde50e04afeb228023319e4.

### 2.4 Entropic Ring-LWE

The introduction on printed p. 4 explicitly says its threshold remains insufficient for coefficient-binary secrets. Theorem 6.9, printed p. 22, assumes DSPR and Ring-LWE, and gives mild entropic Ring-LWE hardness under noise lossiness at least n log(gamma log(n) sqrt(n)) plus a superlogarithmic margin. Its source and threshold differ from this packet. It does not already supply the Base_2 premise or A1's one/two-sample implication. [Brakerski–Döttling, 2020/1185](https://eprint.iacr.org/2020/1185.pdf#page=22). The supplied local PDF hash is 8ee650d5d05d2e7fe33657e35ff5bb9c79be6d16d8a0d8604d8278eb87aa7e46.

## 3. Source-by-source comparison against the frozen experiment

The exact premise under review is one pair A_i=U_i+F_i, i=1,2, with one uniform d-subset T; independent uniform U_i in I_T conditional on T; and all 2n source-noise coefficients independently D_ell, jointly independent of T,U_1,U_2. The challenger gives no T, U_i, F_i, oracle, auxiliary G, completion H, or binary secret. Its comparator is the exact product uniform distribution on Rq^2. Computational indistinguishability quantifies over uniform randomized polynomial-time bit tests and absolute endpoint differences.

**Ideal identification.** Let the integer ideal Q_T be the inverse image of I_T under R -> R/qR. Then Q_T is the product of the prime ideals indexed by the n-d roots outside T. Thus Q_T belongs to the uniform family P_(n-d), and Q_T/qR=I_T. Complementing a uniform d-subset gives a uniform (n-d)-subset. The supported ideal has Fq dimension d; its annihilator J_T has dimension n-d; and |Rq/J_T|=q^d. This checks that the exponent d in the guessing term is the supported dimension, not the number of vanishing roots or the number of target samples.

**One hidden ideal really is shared.** Both points in the frozen law share T by construction, and the literature's final hybrid has the same shared Q. Reading 'two samples' as two independently initialized hidden ideals would define a different experiment. No reduction between those two initialization conventions is proved here. For a concrete distinction before adding noise, in F5 × F5 with a uniform singleton support, the event that the two nonzero points lie on different axes has probability zero under shared support and 8/25 when the support is redrawn independently. Thus the qualification is mathematically consequential. The coordinator correctly calls the frozen source an explicit interpretation/specialization; a stronger claim that it is a verbatim complete literal copy of Definition 7.4 would be unjustified.

**Zeros are permitted.** A uniform point of I_T has independent uniform Fq coordinates on T, including zero with probability 1/q each. It is not a uniform generator of I_T. The new input preserves that law. For one point the latent active-conditioning change has mass 1-(1-1/q)^d, at least 1/q for d>=1; at fixed polynomial q this is not negligible. A1's guessing argument does not require multiplication by U_i to be an isomorphism on the quotient. This is why the old unit/rank loss is not a hidden source assumption here. Even if both points vanish at one active coordinate, the single leakage-cardinality upper bound remains available; no requirement that their generated ideal equal I_T appears.

**Coefficient/canonical noise calculation.** For f=sum_j f_j X^j and complex primitive 2n-th roots zeta^(2k+1), the evaluation matrix V has V*V=n I. Consequently

    ||Sigma(f)||_2^2 = n sum_j f_j^2.

At canonical spherical width r=sqrt(n) ell, the unnormalized lattice mass on f in R is therefore exp(-pi sum_j f_j^2/ell^2), whose normalization factorizes as Z_ell^n. This proves exact equality with the coefficient product law, rather than an approximation or a claim about standard deviations. The Section 7 ambient lattice is R and quotient qR; neither a dual-lattice Gaussian nor a torus error is silently substituted. Mapping a separate general dual/continuous Ring-LWE theorem would require its own scaling/noise interface, which this claim does not invoke.

**Small noise and modulus.** Base_2 has coefficient width ell, not the target width sigma_m and not negligible width. Its truncation at ell^2 is used only for proof comparison with a paid tail. The computational assumption concerns the original untruncated law. At these parameters no cited worst-case hardness theorem supplies the source premise. Equally, the published swallowing/unit proof cannot simply be instantiated and credited as proving the desired theorem. The coordinator's explicit conditional premise is the load-bearing computational hypothesis.

**Comparator and challenge budget.** Uniform Rq^2 means independent uniform coordinates. There is no public hidden-lattice basis. For m=1, B_1 ignores A_2; for m=2, B_2 uses the two challenge elements once each as multipliers. It locally samples a new common binary S and two independent target errors, then evaluates exact equality with S. Thus two target samples really fit the two-source-point budget. No source response is being assumed: both RLWE responses are computed locally. More multipliers would require a new source tuple or a separately justified expansion. Rotations, repeated use of one A_i, and source resampling do not supply independent target multipliers.

## 4. Nonemptiness, effectiveness, precision, and quantifiers

Put M=2n^3 and q=P(1,M). The prime import gives

    q >= 2n^3+1,
    q <= C (2n^3)^5.18 = C 2^5.18 n^15.54.

Since 16-15.54=0.46>0, the eventual bound q<=n^16 follows whenever n^0.46 >= C 2^5.18. There is no missing exponent slack. Also 2n divides M, so q=1 mod 2n and X^n+1 fully splits with distinct roots over Fq. This is an actual infinite family through every sufficiently large power-of-two n, not an unproved intersection of incompatible inequalities.

For fixed m=1,2,

    q/(n sigma_m)
       >= (2n^3+1)/(2 sqrt(m) n^2 ell^3)
       > n/(sqrt(m) ell^3) -> infinity.

Hence q/sigma_m>=n eventually, with c=1 and K=16 fixed before any adversary or success exponent. No concrete practical threshold is claimed.

**Uniform generation.** Given unary 1^n, enumerate 1+jM for j>=1 and test primality by trial division through the square root. The least successful candidate is polynomially bounded in n, and the number of candidate/divisor operations is polynomial too. A crude all-integer-candidates upper bound is O(q^(3/2)) times polynomial bit arithmetic, hence polynomial in n. No knowledge of the numerical value of C is needed for this terminating search; C supplies its complexity bound. The finitely many small n can be absorbed in a uniform polynomial runtime bound. This is polynomial in n, not a claim of polynomial complexity in log n alone.

Once q is generated, even enumerating all field elements and testing x^n=-1 costs polynomial time in n. Roots can be ordered canonically, and CRT interpolation and ring operations use polynomial time and O(log n)-bit residues. A list of all roots costs O(n log n) bits. Public source and target challenges have O(n log q)=O(n log n) bits for either fixed sample count.

The exact Gaussian distributions are mathematical laws on integers reduced modulo q. A1 supplies bounded finite-table approximations for its local target-error sampler with sigma_m^2=4m n^2 ell^6 integral, truncation radius B_E=2m n^2 ell^3, and polynomial table/precision cost. I checked that B_E/(n sigma_m)=sqrt(m)>=1 and that the table size O(n^2 ell^3) is polynomial. The full sampler proof and its precise constants remain the mathematical referee's responsibility; no efficient sampling of the proof-only correlated H is required by the source test.

For concrete d, an executable source challenger can likewise compute T, uniform ideal coefficients and negligible-error Gaussian tables using polynomial time. An exactly uniform draw from an odd-size finite set cannot generally be generated from a bounded fixed number of fair bits; use bounded approximate sampling with explicit TV errors, or the exact mathematical source model. The packet properly separates these possibilities. Its implementation inequality keeps the comparator exact; an approximate comparator would need its own endpoint error. Polynomial-size representations alone would not have justified generation, but the explicit procedures do.

**The two concrete d choices.** Since n is a power of two, ell=log2 n exactly. The baseline floor(sqrt(n)/ell^4) is uniformly polynomial-time computable, eventually at least one, and satisfies

    d log2 q <= 16 sqrt(n)/ell^3 = o(n).

The square root and floor need no real-number oracle: d is the largest integer with d^2 ell^8 <= n. The larger concrete example floor(n/(64ell)) is also uniformly polynomial-time computable and eventually positive. For every integer d in that larger range, once q<=n^16,

    d log2 q <= n/4,
    log2[ q^d ((1+D_ell(0))/2)^n ]
       <= -3n/4 + n/(ell ln 2).

For ell>=6, this is at most -n/2. The baseline belongs to the larger interval eventually because 64/(sqrt(n)ell^3)->0. The remaining displayed statistical errors depend on n,ell,m, not d, and are of scale exp(-Omega(log^2 n)); this is negligible against every fixed inverse polynomial. These substitutions do not require choosing widths after observing a solver's success exponent.

**RS1-Q1: computable is not necessarily efficiently generated.** A fixed uniformly computable d(n) may take superpolynomial time to evaluate, even though its values lie in [1,n/(64ell)] and have O(log n) bits. This does not invalidate the literal conditional reduction: B_m ignores d, and the target ensemble depends on n,q,m only. The hypothetical source ensemble can be defined mathematically for such a sequence. It does invalidate any blanket assertion that the complete source family for every allowed d is generated uniformly in polynomial time from n. If efficient source generation is part of the intended scientific statement, restrict that general clause to polynomial-time computable d, or foreground either concrete family and label the broader clause as purely conditional. Providing d as public input permits polynomial sampling given d but does not solve generation of d from n.

**RS1-Q2: the interval includes easy sources.** The quantifier is 'for each chosen d, if its Base_2 premise holds'; it is not 'the premise holds for all d in the interval' and not a transfer between d choices. This distinction must remain explicit. The next section gives an actual contradiction to plausibility at small d.

## 5. Source attacks and obstructions in their correct scope

The exact archived attack used here is corrections/ATT-v3.md, hash **4766209d639d73de1252b4eac1343289f9a250e0b79a1ef9731c5bd485066b24**, with corresponding C01/ATT-recheck.md, hash **640e4c1af9441ba436ded264a548ad6653a183c9e6974e64680e0600f074b40e**. Both match the historical index. Its corrected public-root input, deterministic solver policy, strict radius, and exponential-memory permission are retained. Its current global status remains PROVISIONAL; I use its version-specific reviewed scope, not a claim that the whole old run was certified.

The finite ATT statement accepts every A=U+F with support(U)<=d and F in [-b,b]^n when a power-of-two r dividing n satisfies 2d<=r<=n and q^(1-d/r)>2nb. Its time is exp(O(r)) times polynomial input cost and its uniform acceptance is bounded by

    min(1, 2^r (2b+1)^n / q^(n(1-d/r))).

This theorem directly allows zero active coordinates, so it applies to the **uniform-point first marginal** of Base_2 after the independently bounded mask-tail loss. The noise or correlation of A_2 is irrelevant because the algorithm ignores A_2.

For the current stronger q lower bound and any 1<=d<=n/(64ell), take r to be the least power of two at least 2d. Then 2d<=r<4d<=n eventually, and

    q^(1-d/r) >= sqrt(q) > sqrt(2) n^(3/2) > 2n ell^2

eventually. The final strict inequality is equivalent to n>2ell^4. With b=ell^2, the uniform false-positive logarithm is at most O(d)+O(n log ell)-(n/2)ln q=-Omega(n log n). The actual source first mask lies in the box except with probability at most n exp(-pi ell^2)/(pi ell), also negligible. This is a direct specialization of the finite reviewed attack, without importing its A2 asymptotic assumptions blindly.

For both concrete growing d choices, exp(O(d)) is a **superpolynomial upper bound** and supplies no polynomial-time refutation. It is also subexponential in n: d=o(n). More precisely d/log n -> infinity for both. This is a limitation on the strength of a source assumption, not evidence proving its hardness. No practical bit-security estimate or exhaustive absence-of-attacks claim follows.

For d=O(log n), the same reviewed bound is polynomial, so the source premise is contradicted in that range. There is also an elementary fully explicit control at d=1, needing no lattice-algorithm import: enumerate the n singleton supports and their q ideal amplitudes U; accept if A_1-U has a centered representative in [-ell^2,ell^2]^n. Time is polynomial because q<=n^16. Planted acceptance is at least 1-n exp(-pi ell^2)/(pi ell), and uniform acceptance is at most

    n q (2ell^2+1)^n/q^n = exp(-Omega(n log n)).

Thus at least one legal general d sequence is **demonstrably easy**, rather than merely insufficiently studied. d=0 is easier still but excluded eventually in the asymptotic clause. At the other finite extreme d=n the source is exactly uniform, while the displayed guessing bound is vacuous; this is consistent with the finite theorem and supplies no accidental hardness result.

For the other permitted archived results, I checked the exact W1-final-v1 note hash **98194bd60d4d53fb786f3a4986529d39dd4658b30e0d9da418dc5e4db2429a8f** with N01 review hash **b2567a04649aca0f668f8fd5278412e1f00f280f755a9b0a7801ec93da365c43**, and W2-final-v1 note hash **6fdaef8bd1f4aa648bd6e00cc0f443120eba0fad274e074d9f927348b4ea013f** with N03 review hash **0213a8425cc1fa1aa9a1b199eca7e296131c18f8343bb9c6508e979914577391**. Their applicability is limited as follows.

| Reviewed archived item | Relevance to Base_2 / A1 |
|---|---|
| W1 broad-source entropy obstruction | Starts from the broad active-point independent-noise source and requires exact uniform-comparator preservation. Base_2 has two small independent noises. A1 does not try to output the old correlated source. No contradiction. |
| W1 repeatable latent-kernel sampler-to-attack | Requires an additional uniformly accurate PPT sampler on the same A with fresh repeated coins, exposing its hidden completion law. B_m provides no such capability and never executes H. No actual polynomial source attack follows. |
| Old uniform-point image/rank defect | Concerns replacing US by an independent uniform ideal point in a decision hybrid. A1 charges quotient information and does not make that replacement. It does not claim a negligible public active-conditioning map. |
| W2 orbit refinements and small-fixed-field coverage | Do not supply an exp(o(d)) attack or a general algorithmic lower bound. The archived example does not improve optimized ATT merely by improving one conservative constant. No new source security follows. |
| W2 scalar-cancellation analysis | Its active-U ratios and exact second-noise model are not silently applied to uniform-U Base_2. Even in its own scope it excludes only a scalar mechanism. |
| W2 known-support PV search reduction | Has a stated search direction and additional known-support interface. It does not convert an arbitrary two-point source distinguisher into recovery or establish Base_2 pseudorandomness. |
| Retired structured/binomial-support source | Its support distribution differs from a uniform subset among all d-subsets. Its decoding failure does not by itself refute either concrete Base_2 family. |

No checked polynomial-time algorithm in the permitted material refutes Base_2 at either concrete growing choice. This is a bounded statement about identified methods, not an affirmative security argument.

## 6. Independent motivation, novelty, and the user's goal

**Independent source motivation: PASS, with the computational strength disclosed.** The premise specializes a pre-existing hidden-lattice noisy-point problem: choose a lattice between qR and R from a natural family of split ideals, hide it, and distinguish noisy uniform lattice points from ambient uniform points. The latent structure is a random ideal and q-ary ideal points, and the challenge consists only of noisy points. Neither binary-secret Ring-LWE recovery, a target response, nor a target-dependent simulator is used to define it. More substantively than the absence of a binary input, the same hidden-ideal family, quotient-point law, ambient Gaussian mechanism and two-point interface occur in the prior HLBDD application. The exact polynomial-modulus, small-noise and chosen-d specialization is still an explicit average-case hardness assumption. It is not a worst-case lattice theorem or a conservative consequence of ordinary Ring-LWE established here.

**Relative novelty: PASS as a new implication in the checked record; OPEN as an exhaustive literature claim.** The previous authoritative run retained a conditional one-pair decision route with an extraction obligation, independent-source conversion, and nonnegligible uniform-point rank loss. The present packet instead directly bounds exact recovery under a lossy multiplier law, uses uniform ideal points without unit conditioning, and uses the two available source elements for two multipliers. Its information charge can reach d=floor(n/(64ell)), where the old arbitrary-support extraction was not established. These are concrete changes in the reduction interface and conclusion, rather than a renamed source or a status upgrade for an old theorem.

The general noise-lossiness/projection principle has published ancestry, and the report must credit it. The identified new content is its stated ring-source specialization, witness-preserving exact-recovery test, discrete joint-completion proof and resulting parameter/sample claim. None of the four checked primary works or the allowed archived outcomes already states this exact implication. This bounded comparison does not establish priority against all existing literature, including every later paper mentioned in the project bibliography; those unapproved primary papers were not freshly surveyed in this assignment.

**Analytic obligations: conditional PASS of the source-side closure only.** The frozen author proof claims to prove the Gaussian completion, noise-lossiness identity, truncation and finite implementation comparisons directly, rather than assume an extractor or an executable hidden H sampler. The prime existence dependency is externally checked here. Accordingly there is no additional unproved source-conversion analytic premise identified by this review. Whether those direct mathematical proofs actually close is for the exact-proof and blind reviews. A favorable source assessment cannot certify them.

**Goal scope.** If all mathematics is accepted, it is reasonable to describe the result as: 'Assuming pseudorandomness of the explicitly defined two-point, same-hidden-ideal Gaussian source at a fixed nontrivial growing d, coefficient-binary Ring-LWE exact recovery from one or two independent shared-secret samples is PPT-hard, at polynomial q and q/sigma>=n, with negligible reduction loss.' This is a meaningful conditional advance matching the requested new-implication criterion. It must not be advertised as completing the original polynomially-many-samples objective. Even a result for two ring samples is not a theorem for arbitrary polynomial sample count. Nor does it imply target decision hardness, a standard Ring-LWE source reduction, nonuniform-circuit hardness, quantum hardness, or practical security.

## 7. Claim-addressed dispositions

| Claim / interpretation | Disposition and reason |
|---|---|
| SOURCE-2: exact joint source is motivated by same-ideal HLBDD | **PASS with interpretation stated**; same Q in the primary final hybrid, explicit two-point budget, primal ambient Gaussian, and exact new comparator. Not a claim of a complete literal verbatim definition or imported hardness. |
| SOURCE-2: uniform ideal points and zero coordinates match | **PASS**; no active condition. A unit-conditioned substitution would be **REJECTED** without its nonnegligible loss. |
| Computational Base_2 premise at either concrete d | **OPEN / explicitly assumed**; no approved polynomial attack refutes it, no source-hardness proof establishes it. |
| Computational premise plausibility for every d in the general interval | **REJECTED**; d=1 has an elementary PPT distinguisher; reviewed ATT reaches d=O(log n). Literal if-then quantification survives. |
| PRIME-POLY: q least 1 mod 2n^3, q<=n^16 and q/sigma_m>=n eventually | **PASS** from primary theorem and explicit algebra. |
| Polynomial-size and uniformly polynomially generated concrete parameter families | **PASS** in security parameter n, with finite approximation distances. No practical performance claim. |
| Polynomial-time generation for every merely uniformly computable d sequence | **REJECTED as a blanket interpretation**; source sampling given d and generation of d are distinct. Conditional implication itself can remain valid. |
| Larger-d entropy substitution and fixed quantifier order | **PASS** as a parameter/entropy calculation. No hardness transfer between d values. |
| Actual target sample budget m in {1,2} | **PASS**; one challenge pair, fresh local common S, independent local target errors, one Q call. |
| More target samples, decision hardness, or source oracle | **OPEN / not claimed**; cannot be inferred. |
| (F), (I), (A) full mathematical proof | **OPEN for global acceptance in this report**; another referee owns the complete proof gate. |
| Meaningful new conditional search implication if math closes | **PASS in the limited stated scope**; relative novelty as above. |
| Completion of the original polynomially-many-samples research goal | **REJECTED as a description of this theorem's scope**. |

No edited author statement is issued by this reviewer. Qualifications can be incorporated in exposition without changing the frozen finite claim. Replacing 'uniformly computable' by 'polynomial-time computable' would be a new narrowed statement version and should be tracked explicitly if made.

## 8. Access and evidence record

All four approved primary URLs returned usable PDF text through the web tool. Order-LWE screenshot requests for zero-indexed PDF pages 37 and 40 returned exactly the ordinary retrieval failure 'Failed to fetch https://eprint.iacr.org/2018/494.pdf: Cache miss'. I continued with the already available primary text; no alternate content-policy route was used. The Xylouris screenshot request returned a reference but no image was inspected; its theorem was checked in primary text. A local attempted read of this current run's nonexistent target.md returned 'No such file or directory', so the already-authorized previous target and root task history supplied scope. No package/library absence was newly tested or claimed. No content-policy interruption occurred.

There was no mathematical experiment and no experimental slot requested. The finite axis-law and d=1 controls are exact hand arguments, while hashing/reading files is administrative. Full proof-referee outputs, blind outcomes, and later coordinator decisions were not read or assumed. This report ends the bounded RS1 task early, with the source computational premise and global proof disposition explicitly unclosed.
