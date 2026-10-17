# RS1 nonauthor source, parameter, and complexity review of EX-v2

Status: **provisional scoped pass, with the qualifications below**. No substantive source-interface, parameter, or bounded-PPT defect was found in the immutable EX-v2 packet. This is a recommendation to the coordinator, not claim acceptance, an independent certification of every analytic proof step, or a hardness proof for Base2. The separate mathematical and blind reviews remain necessary. Initial Track A research claims were not used as proof dependencies.

## 1. Exact inputs and review boundary

The assignment freezes theorem-only-v2 together with proof-v1 and the following three source/parameter files. SHA256 values were independently recomputed and match the manifest:

| File in `input/` | SHA256 |
| --- | --- |
| expansion-theorem-only-v2.md | 44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51 |
| expansion-proof-v1.md | 38c43826a936f69a775a97f19dfb3aeb90256cd03d8953d47fd54f82da27c8ae |
| source-contract-v1.md | bcb62c8553b456161381875cc6712d0f0b739f518657b2ac2b635160135e813b |
| source-comparison.md | a8fb956b8ebbdbfebeed68e2f8296690db915f0ca91a6372d48c1e07338a7ef1 |
| parameter-table.md | b7b6fd5d0269cb1f9ff12e2e5671c38edaf6a5e734556b3b6077880e6c7cfedd |

The same complete hashes are preserved in input-hashes.txt; the full manifest hash is 1258f319c46693b0076eb0a781a0394289699896811bf28e9782846c691e1cd1. All five files were read, including the complete proof. A nonblocking metadata mismatch remains: proof-v1's opening line calls theorem-only-v1 its frozen statement. This review explicitly compares that proof with the supplied **v2** statement, as required by the assignment. No substantive formula/scope mismatch was found. The report does not silently alter either author file.

Additional read-only evidence comprised the permitted September theorem/proof/supplement and source/parameter/full-review records, ATT-v3 and ATT-recheck, the current imported regression registry, initial A primary-source notes, and the run/cap instructions. The installed mathematical-proof-audit protocol and probability regressions were applied. No current blind-review file was read and no current blind reviewer was contacted. There were no numerical experiments, service changes, spawned agents, external model sessions, or author edits during RS1. Administrative hashing and registry bookkeeping are not mathematical experiments.

`sampler-budget-v1.md` supplies a complete bounded sampler and resource calculation. `regression-review-v1.json` preserves all 43 current registry IDs: the 40 historical controls plus the three later historical records. It includes the original imported records and scoped classifications. This report's recommendation is limited to the exact hashed packet and does not inherit acceptance from any previous version.

## 2. Source and target contracts

The sole computational premise is pseudorandomness of **one Base2 pair at the new q,d family**. Its hidden support T is uniform among all d-subsets of the n split roots. Conditional on T, U1,U2 are independent uniform elements of I_T, including every zero coordinate. All 2n coefficient errors are independent D_ell and jointly independent of T,U1,U2. The published object is only (U1+F1,U2+F2), compared with exact product-uniform R^2. There is no basis, support, witness, additional sample oracle, chosen ideal, or active-unit conditioning. This is precisely the SC-v1 interface; changing q,d changes the premise.

The expansion uses this pair once and only fresh local box/Gaussian coins. Its planted ideal components U1 R_j1+U2 R_j2 all remain in the same I_T. They need not be uniform or independent. The masks F1 R_j1+F2 R_j2+W_j may be strongly dependent. The proof requires common-ideal membership and a coefficient bound, not a hidden Base_m assumption. Neither the original pair nor the expansion coins are given to the target solver.

At the uniform endpoint the claim concerns the full law of (A1,A2,C1,...,Cm), compared with the retained uniform pair and m independent uniform ring elements. Thus it is strong enough to append fresh independent S and all E_j, form every response, retain the actual witness, and finally discard the seed. Marginal regularity alone would not suffice. Conditional independence of C_j is asserted given the original seed before any observations, and follows from the explicitly independent local coins.

The target has one uniform coefficient-binary S, m independent uniform multipliers, and all mn errors independently distributed as coefficient D_sigma, jointly independent of S and the multipliers. The source test independently samples S itself and accepts only if Q returns that actual S. Residual consistency, any preimage, and decision advantage are different tasks and are not substituted. The common quotient reveals at most q^d values once for all m outputs; it is not a q^(md) charge. The good-mask event depends only on source/expansion latents, so it does not condition S or the auxiliary G. Bad-mask probability is paid additively.

The finite implementation charge xi_source+2xi_alg+xi_target is correctly scoped to full laws. One xi_alg enters each source-test endpoint; a planted challenge approximation adds xi_source; comparing the implemented target's witness/transcript law adds xi_target. The uniform source comparator is exact. If it were approximated, its error would need an additional term. Merely correct one-dimensional sampler marginals would not justify this bound.

## 3. The first new sample gate and substance of the composition

For m=3, choose h=1, K=11, q=P(1,2n^11), and restrict to powers n>=4 (define any allowed finite prefix separately). This uses the same two source elements and a single target-solver call. The new regularity step is genuinely needed for this sample extension: omitting W from ideal-preserving linear combinations leaves, at any fixed CRT root, probability at least q^(-2) that all three C_j vanish, whereas three independent uniform outputs have that event with probability q^(-3). Hence the public marginal TV is at least q^(-2)-q^(-3), nonnegligible for fixed-polynomial q. Rotations or repeated masks do not remove that obstruction. EX includes fresh additive W and pays an explicit full-law regularity error.

Subject to the mathematical proof gates, this is a substantive conditional source-budget-preserving composition beyond the accepted A-PPT m<=2 statement: one Base2 hypothesis can support a specified polynomial target sample budget. It is more than renaming a Base_m premise because no independent planted multi-sample law is assumed or generated. This assessment concerns theorem content, not literature priority. Generic ring regularity and the identity-column remedy have close primary antecedents, described below.

## 4. Changed modulus, support, and noise

Let ell=log2(n). The exact comparison is:

| Quantity | September accepted A-PPT v2 | Frozen EX-v2 |
| --- | --- | --- |
| Source budget | one Base2 pair | one Base2 pair |
| Target samples | m=1 or 2 | polynomial-time computable 1<=m(n)<=n^h, fixed integer h |
| Modulus | P(1,2n^3), eventually q<=n^16 | P(1,2n^K), K=h+10, eventually 2n^K+1<=q<=n^(6K) |
| Source coefficient width | ell | ell |
| First d family | floor(sqrt(n)/ell^4) | same formula, at the new q |
| Second d family | floor(n/(64ell)) | floor(n/(24Kell)) |
| Target width | 2sqrt(m)n ell^3 | 2sqrt(m)n(2n+1)L ell^3, L=ceil(n sqrt(q)) |

The old and new source assumptions are distinct even in the first d family. At equal n,m and a hypothetical equal q, the new target width is larger by exactly (2n+1)L; in the actual comparison q also changes. This is a sample-budget extension with substantial modulus/noise cost, not an across-the-board parameter improvement.

For fixed h, the least-prime theorem gives

    q <= C(2n^K)^5.18 <= n^(6K)

eventually, because n^(0.82K)>=C 2^5.18 eventually. The lower bound q>=2n^K+1 follows from the progression itself. All q are split, odd, and exceed n^2. The constant C is effective, independent of adversaries. The algorithm need not know its numerical value to enumerate the first prime. Both d formulas always define integers in [0,n] and are eventually positive.

The new linear support formula gives

    d log2(q) <= n/(24Kell) * 6Kell = n/4.

The square-root formula eventually lies below it because 24K/(sqrt(n)ell^3) tends to zero. Since D_ell(0)<=1/ell,

    q^d ((1+D_ell(0))/2)^n
      <= 2^(-3n/4+n/(ell ln 2)) <= 2^(-n/2)

eventually; ell>=6 suffices for the last displayed exponent comparison after the q,d conditions hold. The proof correctly charges the upper prime bound here, rather than replacing q by its lower progression scale.

The historical q128 failure must remain rejected. Substituting q=P(1,2n^128) into the old d=floor(n/(64ell)) gives

    log2(q^d 2^(-n)) >=128ell floor(n/(64ell))-n
                       >=n-128ell,

so that proposed negligible bound fails. This is a counterexample to the old generic-modulus ledger, not a recovery attack. EX avoids it by explicitly coupling the support denominator to K. For example, h=118 gives K=128 and d=floor(n/(3072ell)), not the rejected old d. The counterexample, dependent reopening, and repaired restricted-family review remain intact; no rejected ledger is revived.

For the ratio, using L<=2n sqrt(q) and 2n+1<=3n,

    sigma <=12 sqrt(m)n^3 sqrt(q) ell^3,
    q/(n sigma) >= sqrt(q)/(12 sqrt(m)n^4 ell^3)
                 >=sqrt(2)n/(12ell^3) -> infinity.

Thus q/sigma>=n eventually. This assertion uses the lower prime bound and is not a concrete security threshold. The regularity error is negligible because its first squared term has logarithm at most n ln16+6Kn ln n-2pi n^2, while its second is (2/n)^n; multiplication by m<=n^h after the square root preserves negligibility. The mask and completion errors have exp(-Omega(ell^2)) decay times a fixed polynomial. Eventually Delta<1, while the finite formula explicitly uses eta=1 if that guard fails. Small n may have d=0 or vacuous probability bounds without contradicting a finite conditional theorem.

The order of quantifiers is essential: h and the efficiently computable m policy, q, d, widths, and sampler precision precede Q. Each fixed h has its own modulus/source family. The result is not simultaneous hardness for arbitrary polynomial sample exponents at one fixed q family. Uniform PPT is asserted; no advice-based, nonuniform, or quantum conclusion is imported.

## 5. Effectiveness and bounded implementation

The primary least-prime check is [Xylouris, *On the least prime in an arithmetic progression and estimates for the zeros of Dirichlet L-functions*](https://www.impan.pl/shop/publication/transaction/download/product/83078), printed pp.65–66, Theorem 1.1. The publisher PDF directly defines P(a,q) for coprime a,q and gives exponent 5.18 with an effectively computable constant. Substituting progression modulus 2n^K yields the bound above. This review checked the published theorem's statement and applicability, not its analytic-number-theory proof.

`sampler-budget-v1.md` closes the finite sampling obligation explicitly. It fixes xi=2^(-n^2), truncates both Gaussian tables at

    (n+ceil(log2(mn+2))+2) ceil(sigma),

assigns certified raw-weight and dyadic errors, and samples with bounded independent bit blocks. It proves xi_alg<=3xi/8, including all Gaussian tails, table rounding, and interval bias. Exact integer squares determine L and sigma^2; no rounded irrational width, continuous Gaussian substitute, real-number oracle, or unbounded rejection loop is used.

For fixed h its table size is O_h(n^(7h/2+34)ell^3), each probability needs O_h(n^2) bits, and an explicit storage bound is O_h(n^(7h/2+36)ell^3) bits. These enormous polynomial bounds establish existence only. The reduction uses one Q call, 2mn interval draws, mn draws at each Gaussian width, n secret bits, and 3m ring multiplications. Schoolbook ring work is O(mn^2) modular operations. Neither CRT roots nor the proof-only completion Gaussian H is an algorithmic subroutine. Prime enumeration by trial division costs at most O(q^(3/2)poly(log q)), hence is polynomial in unary dimension n under the published bound. All finite-prefix costs can be absorbed into the fixed-family constant. No practical running-time or memory claim follows.

## 6. Targeted primary ancestry and hardness boundary

[Order-LWE, ePrint 2018/494](https://eprint.iacr.org/2018/494), §7, printed pp.38 onward, Definitions 7.3–7.4 and Lemma 7.7, describes hidden-lattice noisy-point indistinguishability and a common-hidden-ideal two-point hybrid. SC-v1 corresponds to the inverse-image ideal of I_T; its complementary root subset indexes that lattice. In power-of-two cyclotomics, canonical squared norm equals n times coefficient squared norm, so coefficient width ell corresponds to canonical width sqrt(n)ell. Theorem 7.5 additionally assumes ordinary Ring-LWE and other conditions; its rerandomization/unit arguments do not establish this polynomial-q Base2 premise. The known-ideal decoding result in Theorem 6.2 also uses nonuniform short-vector advice, not merely an arbitrary public basis. Direct PDF access failed during initial A; exact indexed primary extracts were cross-checked against the permitted preserved extracts. These interface checks support motivation, not source hardness.

[Lyubashevsky–Peikert–Regev, *A Toolkit for Ring-LWE Cryptography*](https://sites.cc.gatech.edu/fac/cpeikert/pubs/toolkit.pdf), printed pp.35–37, Theorem 7.4/Corollary 7.5, proves regularity for normal-form [I_k|Abar] and discrete-Gaussian inputs, addressing the common-divisor obstruction with identity columns. For k=1,l=3, the row (1,A1,A2) and canonical width r>2n q^(1/3+2/(3n)) yield exponentially close uniform output for almost all seeds. In this cyclotomic, coefficient width is r/sqrt(n). Thus an all-Gaussian variant could use coefficient width above 2sqrt(n)q^(1/3+2/(3n)), improving the q exponent relative to EX's box/Gaussian construction. This is a separate possible direction: the unbounded multiplier tails, mask bounds, finite errors, and new theorem would require a fresh version and review. The cited theorem does not literally give EX's box input or displayed finite delta_exp. EX's direct regularity proof therefore remains necessary for its exact law. Generic regularity is established ancestry; no exhaustive priority claim is made.

[Brakerski–Döttling, *Lossiness and Entropic Hardness for Ring-LWE*](https://eprint.iacr.org/2020/1185.pdf), §3.1, already treats subset-sum and Gaussian rerandomization. Lemma 3.5, printed p.12, requires k>=log(|G|)+n log(q)+omega(log(lambda)) input samples and yields a distribution over error laws; it does not expand a constant two-point source. Theorem 6.9, printed p.22, assumes DSPR and ordinary Ring-LWE and requires noise lossiness at least n log(gamma log(n)sqrt(n))+omega(log(lambda)). The introduction explicitly identifies coefficient-binary secrets as outside its threshold. These are material source/secret differences, not generic rerandomization novelty. Exact indexed primary passages and the permitted September review were used; the local PDF hash matches 8ee650d5d05d2e7fe33657e35ff5bb9c79be6d16d8a0d8604d8278eb87aa7e46. The separate Gaussian construction is ancestry, not an imported EX proof step.

These primary sources were targeted checks, not a broad literature survey. No consulted source supplied a hardness reduction for the exact new Base2(n,q,d) families. The frozen theorem must retain that assumption. In particular, absence of an identified polynomial attack is not evidence that upgrades the assumption into a theorem.

Archived ATT-v3 and C01/ATT-recheck give a useful live qualification. For source error cutoff b0=ell^2, choose the least power of two r>=2d (eventually r<=n for both EX d families). Then

    q^(1-d/r) >= sqrt(q) >2n ell^2

eventually. The strict gate supports an exp(O(r))poly(n,log q) attack whose uniform false-positive bound is at most 2^r(2b0+1)^n/q^(n(1-d/r)); at EX parameters its logarithm is -Omega(n log n). Root enumeration is polynomial because q is polynomial. Since d=o(n) and d/log n tends to infinity, the available exp(O(d)) bound is subexponential but does not certify polynomial time. It is not a lower bound, and does not rule out a faster algorithm. For d=O(log n), the same upper bound can be polynomial; d=1 also permits direct enumeration of n*q ideal points. Thus all-d source plausibility is false even though the finite conditional theorem allows all d. The two eventual d families avoid that immediate small-d attack without establishing source hardness.

## 7. Regression and probability audit

All 43 imported IDs have an explicit entry in `regression-review-v1.json`, including exact imported provenance. The classifications are local to this review. The main applicable controls are:

| Controls | EX-v2 handling |
| --- | --- |
| R03–R05, R14–R15, C03-HC5, SE-CORRELATION-F3, PAIRWISE-SE-F3, N02-DUAL-NUMBER | The exact conditional source law and full target product law are specified; source zeros are retained; expansion dependence is admitted; no active-unit or marginal-only inference. |
| R12, C03-HC7 | Actual sampled witness is tested. One shared Y and one q^d quotient charge serve all samples. |
| R02, R08, C02-LATENT-PUBLIC, PUBLIC-ENCODED-F | Latents are used only for a guessing upper bound; no reverse TV projection or decoder from latent knowledge. H is not appended to the independent-noise endpoint. |
| R11, R18, C03-HC6, CP-1, N03-PV-CONDITIONING, N03-SCAL-POSTERIOR | Bad-mask probability is additive; independence is only conditioned on the original seed or nonpivot coefficients. No selected-stage product, posterior ratio prior, or signed-gap transfer is used. |
| C03-HC1–HC4, NC1-v1, RECT-ALG-1, S0-dependency | Normalizer/positive-matrix/rectangular gates remain explicit mathematical obligations; this review confirms their stated scope and parameter guard, leaving full verification to the mathematical referee. |
| A-PPT-LEDGER-SCOPE, SOURCE-SMALL-D, C01-ATT | The q128 defect and small-d attacks remain qualifications; the new q/d formulas and strict norm/root-input gates were checked here. |
| R01, R06–R07, R09–R10, R13, R16–R17, C02-CHAR, W2-SUBGROUP-BOUNDARY, W2-CONSTANT-COMPARISON | No structured-support sampler, Boolean-rank inference, quotient extractor, residual-box verifier, entropy-to-statistical-hardness implication, subgroup coverage claim, or attack-constant improvement is imported. These counterexamples remain valid within their original scopes. |
| UNIFORM-APPROX-COLLAPSE | EX intentionally uses approximate full-joint uniformity and pays delta_exp. No exact-uniform-preserving entropy obstruction is extended to this case. Initial A entropy claims are separate. |

For CP-1, the explicit renormalized posterior assigns mass 21/2000 to each trace A_b, b in {0,1}. Each trace matches the selected verifier positions when an independent oracle bit equals b, giving total event probability sum_b (21/2000)/2=21/2000=0.0105, exceeding 0.1^2. The later conditional factor 21/221 is below 0.1, but the earlier selected factor was changed by restriction and renormalization. Thus the historical product shortcut remains rejected. EX's pivot calculation conditions on all nonpivot coordinates of an original independent coefficient vector, so the pivot tuple remains independent with pointwise maximum-mass bounds. Its output product is conditional on the exact seed before output observations. The source good event leaves fresh S,G unchanged. These are explicit reasons why CP-1 does not refute the claimed products; this is not a blanket independence assumption.

## 8. Disposition and unresolved claims

The exact source budget, both endpoint interfaces, m=3 gate, changed q/d premise, finite-prefix quantifiers, ratio and entropy charges, effective prime generation, and bounded sampler/bit/time/memory obligations are closed within this review. No counterexample requiring rejection of this exact version was found. The proof-header version label is an administrative discrepancy recorded above, not silently repaired.

Remaining obligations are the independent mathematical/blind checks and coordinator reconciliation for the exact hashes. Base2 hardness at each new q,d family remains explicitly assumed. Standard-RLWE hardness, known-ideal efficient decoding, target decision hardness, all-sample-exponents-at-fixed-q hardness, nonuniform/quantum security, practical parameters, and literature priority remain unproved and unclaimed. The possible stronger Gaussian regularity variant is outside the frozen theorem. No author change or claim acceptance was made by RS1.
