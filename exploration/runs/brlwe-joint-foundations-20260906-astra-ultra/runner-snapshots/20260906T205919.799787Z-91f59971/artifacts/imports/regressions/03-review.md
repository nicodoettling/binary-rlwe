# C02 — exact sources, attacks, and retirement review

Reviewer: fresh nonauthor C02, gpt-6-astra / ultra. Review completed on 2026-09-06 within the authorized finite run. This is bounded mathematical criticism, not formal certification or independent statistical confirmation. No experiment, worker, service, remote execution, goal, or continuation was used.

**Assessment.** The exact A2 source is well defined, but its computational premise remains unsupported by the checked independent-noise HLBDD, Order-LWE, DSPR, or matrix-entropic-LWE results. B's public source shear is correct; its tested independent-iid-shear completion route fails the required negligible retained-F noise budget. The uniqueness and fixed-character statements survive their stated scope. Frozen ATT v2 is valid with its solver-success probability retained. Some R02 prose overstates that qualified statement; a separate deterministic solver correction has been saved for a different reviewer, and is not accepted by its author C02.

## Authorization, frozen inputs, and review scope

Before research I read the absolute active `run.json` and checked affirmative `launch_authorized`, `launch_confirmation_received`, `deadline_supervisor_implemented`, and `deadline_supervisor_verified`. The identity/path fields match `brlwe-joint-ideal-20260906-astra-ultra`, project `/home/nico/projects/research_projects/binaryRLWE`, and its designated output directory. The frozen start is `2026-09-06T14:21:13.181175+00:00`, workers stop at `19:06:13.181175+00:00`, and hard deadline is `19:21:13.181175+00:00`; the listed phase deadlines are consistent with the manifest offsets. My earlier task deadline is `16:15:00Z`, with research stop by `16:10:00Z`. The first clock reading was `15:37:20 UTC`. No deadline was inferred or extended.

I read `PLAN.md`, `BRIDGE_CONTRACT.md`, `TASK_TEMPLATE.md`, `run-config.json`, the full frozen counterexample registry, review instructions, assignment, and the mathematical-proof-audit skill and both required references before proposing the correction. This review is not blind: the assignment supplied the author arguments and correction history.

The author input is the immutable `snapshots/review-v1` bundle, frozen `2026-09-06T15:36:43.466709+00:00`. Administrative hash checking verified all 36 manifest entries. Complete expected and actual hashes are in [input-hashes.json](input-hashes.json); all match. The manifest SHA-256 is `29ef8e92ea6f82e6e4582e245f525e1f71e2f7e17eb0a542fba50155e981a143`, and claims.json is `4c1194bb72d934fd2207182999a6eb72a7a82b47da6e314c3989d38cd563274d`.

Substantively read: candidates/A.md and B.md; sources-and-assumptions.md; parameter-table.md; foundations/F03.md, F03-source-ledger.md, F03-attacks.md, and F02-completion.md; development/D02.md, D02-A-correlation.md, D02-review-packet.md, and D03-common-k.md; refinement/R02-break-A.md and R01-compatibility.md; claims.json and known-counterexamples.md. Hash verification of other bundle entries is not a claim to have reviewed their mathematical contents. In particular, I do not independently recertify D01's extraction theorem, the prime-existence import, or every decision/search theorem.

## Exact laws and literature comparison

A2 fixes `ell=ceil(log2 n)`, `d=floor(sqrt(n)/ell^4)`, `b=ell^2`, `tau=ell`, `sigma=2n ell^3`, and split primes with `sigma n^c<=q<=n^K`. It uses all uniform d-supports, active-nonzero U, independently uniform V in the same ideal, iid truncated D_ell coefficients F, and the exact canonical coefficient-order H_seq conditional on F. Only `(U+F,V+H_seq)` is public. H_seq uses source coins and F; it never uses the bridge's independent S or G. A finite implementation approximates this mathematical law and carries its own full-source error. The integer LDL decomposition, finite Gaussian tables, conditional tail bounds, and polynomial-size adaptive centers provide a coherent approximation route; no actual sampler was executed.

The coefficient/canonical normalization is `||can(x)||=sqrt(n)||coeff(x)||`. Thus a spherical canonical width r corresponds to coefficient width r/sqrt(n). Elliptical canonical widths do not generally become iid coefficient noise. This basis conversion cannot create the missing joint conditional H law.

The primary checks support the source ledger's distinctions:

- **HLBDD / Order-LWE.** Definitions 7.3–7.4 and Lemma 7.7 use uniform ideal points with independent Gaussian errors. The same-ideal reading is supported by Lemma 7.7's common Q; Definition 7.4 alone is terse and prints an ambiguous comparator. Theorem 7.5 additionally assumes ordinary RLWE and swallowing; Definition 2.13 quantifies that swallowing negligibly, and the H3 step explicitly invokes super-polynomial q. Neither A2's active-U law nor its F-dependent H_seq is supplied. See [2018/494, Section 7](https://eprint.iacr.org/2018/494.pdf#page=38) and [the H3 step](https://eprint.iacr.org/2018/494.pdf#page=41). My deduction: with polynomial target widths, this swallowing import forces negligible source width; its almost-noiseless proper-ideal marginal is then rejected by a gcd/unit test. This is an obstruction to that import, not to all completion channels.
- **DSPR.** Definition 6.1 has one conditioned short denominator. Lemma 6.6 transfers the tuple `(g/f)e_i+e'_i` using DSPR and Hermite RLWE. Theorem 6.9 has a mild-search endpoint and requires noise-lossiness at least `n log(gamma log(n) sqrt(n))+omega(log lambda)`. This is a different source, task, and entropy regime. At the checked nonnegligible Gaussian widths the sufficient threshold exceeds binary S's n bits. See [2020/1185, Definition 6.1 and sampler](https://eprint.iacr.org/2020/1185.pdf#page=19), [Lemma 6.6](https://eprint.iacr.org/2020/1185.pdf#page=20), and [Theorem 6.9](https://eprint.iacr.org/2020/1185.pdf#page=22). I also checked Theorem 6.2 and Lemma 6.8's displayed width/conditioning requirements; I did not recertify all their underlying norm-probability estimates.
- **Matrix entropic LWE.** Theorem 4.1 uses a rectangular public lossy matrix `BC+F`; Proposition 3.2 supplies a continuous Gaussian complement for a specified matrix. Neither defines a hidden CRT-ideal source or a correlated noisy-ideal pair. See [2020/119, Proposition 3.2 and Theorem 4.1](https://eprint.iacr.org/2020/119.pdf#page=15).
- **Partial Vandermonde decoding.** Definition 2.14 supplies the known-root-set decoding experiment. Theorem 3.1 and Corollary 4.2 justify the ideal-decoding connection after the attacker has explicitly chosen a supersupport; the direction is an attack reduction, not source hardness. Relevant primary locations are [2022/709, Definition 2.14](https://eprint.iacr.org/2022/709.pdf#page=14), [Theorem 3.1](https://eprint.iacr.org/2022/709.pdf#page=15), and [Corollary 4.2](https://eprint.iacr.org/2022/709.pdf#page=21).

No checked result matches A2 or the common-K source at the same basis, first-mask law, H kernel, widths, sample count, and task. This is the outcome of this narrow primary-source comparison, not a universal nonexistence or novelty claim. The source bridge cannot justify the computational hypothesis that it assumes.

**Discriminating source controls.** In a one-coordinate ideal, changing uniform U to nonzero U has TV `1/q`, whereas the bridge's average rank defect is `1/q-1/q^2`; these costs differ. At polynomial q neither is automatically negligible. For the almost-noiseless proper-ideal import, the source A is a nonunit except for negligible noise tails, while uniform A is a unit with probability `(1-1/q)^n>=1-n/q>1/2` for split q>=2n+1. For the common-denominator entropy comparison, `H(S)<=n` is unconditional and cannot be enlarged by the auxiliary noisy observation. These controls reject the corresponding silent imports.

## BSH and BNG: independent reconstruction

For every fixed a,L,W the map `c0 -> c0+La+W` is a translation. Therefore a public test composed with the independent L,W sampler has exactly the sheared-source advantage against its precise base, and a uniform pair remains uniform. Conditional on J,U,F,L,W,H00, translating fresh uniform V0 by LU leaves V uniform in I with a constant conditional law. Hence V is independent of U,F,H conditional on J. This proves BSH; it does not change U's law, justify a new base width, or provide a completion kernel.

For the wrapped obstruction write `N=F(G+L)+X`, `X=H00+W`, and condition on `C=(J,U,F_1,...,F_(n-1))`. F0 is independent of C; the relevant G,L coefficient pairs are independent across coordinates; conditional on J,U, X is independent of the entire `(F,G,L)` tuple. At frequency theta=k/q, the conditional character values on F0=0 and F0=1 are x and zx, with x possibly complex, `|z|<=1`, and target value `b_theta=phi_sigma(theta)>0`. Thus

    b_theta |1-z|
      = |z(x-b_theta)-(zx-b_theta)|
      <= |x-b_theta|+|zx-b_theta|
      <= 2(epsilon_0+epsilon_1).

Averaging conditional TV gives the factor `min(p0,p1)/2`. These p values are the wrapped residue masses when the retained F is an element of R_q. The character factors are q-periodic in every integer F coefficient, so summing all lifts on a residue fiber preserves the argument. The integer masses used numerically are lower bounds for those wrapped masses. R01 correctly resolves the original notation ambiguity.

Poisson summation makes the scalar Gaussian characteristic positive; its modulus is at most one. Differentiating its normalizer gives `Var(D_sigma)<=sigma^2/(2pi)`. With `k=floor(q/(4sigma))`, q>=8sigma gives `1/(8sigma)<=theta<=1/(4sigma)` and `b_theta>=1-pi/16`. The exact bounds `Z_ell<=1+ell`, `1-cos(2pi t)>=8t^2` for |t|<=1/2, and `sum_(j=1)^ell j^2>=ell^2(ell+1)/3` give

    min(p0,p1)>=exp(-pi)/(1+ell),
    1-phi_ell(theta)>=(16/3)exp(-pi)ell^2 theta^2.

For Gaussian shear, `z=phi_tau phi_kappa`; for arbitrary independent iid shear, `|1-z|>=1-phi_tau`. Substitution yields exactly

    eta_N >= (1-pi/16) exp(-2pi) /
             [96 n^2 ell^4 (1+ell)].

The proof integrates H and retains J,U,F, exactly as required. A2's changing H|F kernel violates the common-x hypothesis, so it is outside this obstruction. Independent broadening only changes x and cannot evade the two-fiber inequality. A negligible full-joint implementation error may be subtracted once. The general B3 extension uses an additional monotonicity import; BNG's main-width result does not depend on B3, and my acceptance concerns BNG's displayed main-width statement.

**Controls.** For the complex-number sublemma, x=i, z=-i, b=1 gives equality `|1-z|=|x-b|+|zx-b|=sqrt(2)`. It checks that no real-phase assumption can be inserted. A retained F0 uniform on `{0,q,1,q+1}` has residue masses 1/2,1/2, and its character factors agree across the paired lifts; treating the integer lift as a public variable is unnecessary. If G'=G, cancellation would be exact, but independence fails, reproducing registry R02's forbidden hidden-G coupling. Finally, over F_5 take U=1, F uniform on {0,1}, V uniform, and compare H=0 with H=F. Their latent `(F,H)` TV is 1/2 but their public `(U+F,V+H)` laws coincide. This directly rejects promotion of a latent lower bound to a public source attack.

The inverse-polynomial bound retires only the tested all-negligible retained-F completion budget. It is not a useful upper bound for a finite reduction, an impossibility for every public-transcript hybrid, or a restriction on correlated-coefficient/nonlinear simulators outside its hypotheses.

## ATT v2: orbit enumeration, decoding, and success

Independently reconstructing the attack: the regular Galois action has a subgroup of order h=n/r and r equal-size root orbits. T meets at most d orbits. Enumerating at most 2^r orbit collections covers T on at least one branch and leaves a known zero set Omega of size t>=n(1-d/r). The ideal L of those constraints contains qO_K; hence `A mod L=F mod L` on the correct branch. Its inverse scaled by q is an integral complementary ideal, unramified and invariant under the same subgroup.

The canonical error bound is nb, not sqrt(n)b. Consequently `gamma_1=sqrt(n)q^(t/n)/(nb)` and `gamma_4=gamma_1/4` match the paper's decoding parameters. The displayed gap gives `gamma_4>=2 n^epsilon sqrt(n)`. If the full stabilizer has size s>=h, then `s log(gamma_4/sqrt(s))` increases over 1<=s<=n, so the cost is at most `exp(O(r/epsilon))*poly`. The A2 choice `epsilon=c/4`, `r` the next power of two above `C0 d`, with `C0>=max(2,4(1+c)/c)`, satisfies the gap eventually. No knowledge of T is supplied free.

For a fixed branch, uniform A projects uniformly to q^t cosets. At most `(2b+1)^n` cosets contain a verified box vector. A union bound therefore gives exactly the stated `p_false`, irrespective of off-promise decoder behavior. At A2 it is `exp(-Omega(n log n))`.

The probability-qualified guarantee is sound: define a designated correct branch as, for example, the lexicographically first enumerated orbit collection containing T, and let p_alg be the average success of its actual solver policy over planted inputs and its random tape. Running or conceptually fixing all branch tapes makes total planted acceptance at least p_alg; no conditional independence of previously failed branches is required. Thus advantage is at least `p_alg-p_false`. A uniform lower bound on every promised input is another sufficient way to define p_alg. The running time must include any chosen repetition policy.

BGP Lemma 2.11 calls its algorithm probabilistic. Its underlying [HPS11 Theorem 1](https://perso.ens-lyon.fr/damien.stehle/downloads/bkz.pdf#page=2) bounds a truncated BKZ execution given exact HKZ/SVP calls. Neither the frozen attack nor that conditional theorem fixes a numerical success probability for an arbitrary chosen implementation. One cannot set p_alg=1 or call this alone an unconditional security ceiling.

Tracing that source also revealed a concrete separate repair: deterministic exact SVP in the low-rank fixed-subfield intersection. It is fully specified in [proposed-ATT-v3.md](proposed-ATT-v3.md), with BGP Theorem 3.2, the exact coefficient/subfield norm conversion, integer rectangular representation, and [Micciancio–Voulgaris Corollary 5.5](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download#page=21). This proposed policy has deterministic `exp(O(r))*poly` cost and needs fresh nonauthor review. I accept only frozen ATT v2's qualified statement here. No alleged numerical base probability or implementation benchmark is invented.

**Controls.** For n=8,r=2 the subgroup `{1,5,9,13}` modulo 16 has the two primitive-exponent orbits `{1,5,9,13}` and `{3,7,11,15}`. Any singleton support lies in one enumerated orbit, while the attacker still pays for the branch choice. If a putative decoder always returns failure, p_alg=0 and the bound yields no positive attack guarantee; existential uniqueness alone cannot rule out this control. If it returns arbitrary vectors off-promise, verification still confines uniform acceptance to the counted cosets. All probabilities use one union bound, not a product of selected-stage success rates.

## UNIQ and CHAR

If two bounded decompositions exist, w=F-F' vanishes at at least n-2d CRT roots. A nonzero integer cyclotomic norm is divisible by `q^(n-2d)`; orthogonality and AM-GM give `|Norm(w)|<=||coeff(w)||^n<q^(n-2d)` under the stated strict inequality. Thus w=0, and active U identifies T. A2 only decreases d from the prior diagnostic, so its eventual uniqueness inequality holds. This proves information-theoretic uniqueness, not efficient decoding. The box/support existence test on uniform A has the stated counting bound.

For CHAR, independence from T,U,V is genuinely present in A2, whereas H remains conditional on F. The exact active-U factor is `E_T[1_(beta|T=0) product_(i in T)c(alpha_i)]`, with c(0)=1 and c(a)=-1/(q-1) otherwise. The inner noise term remains `E_F[chi_alpha(F) E(chi_beta(H_seq)|F)]`.

For a character of CRT support s, its coefficient frequencies `w_j=sum_i alpha_i r_i^j` satisfy `W(r_l^(-1))=n alpha_l`. Centering w and applying the cyclotomic norm yields `||w||>=q^(1-s/n)` and `dist(w/q,Z^n)>=q^(-s/n)`, with no omitted n factor. For small s<=n/ln(q), the latter is at least e^-1. The positive Poisson expression for D_B and a half-exponent split yield R02.5. Since `B_F>=3sigma^2 I/4` uniformly in F, the resulting H bound is uniform before the F average.

The H_seq comparison correctly pays every adaptive normalizer. Pointwise in the complete path h, the density is the quadratic Gaussian mass divided by the product of exact conditional normalizers. Each normalizer has its stated uniform interval for every center. Bounding that complete product and then its global normalization proves the uniform eta_seq; no marginal event product is used. Its character cost is 2eta_seq. F's product-law truncation costs at most `n exp(-pi ell^2)/(pi ell)` in TV and twice this for its character expectation.

For large beta support, avoidance has probability at most exp(-ds/n). For large alpha support and beta=0, the absolute active-U factor is an elementary symmetric mean of s weights 1/(q-1) and n-s weights one. Maclaurin/pairwise averaging proves its upper bound by the dth power of the average weight; it is not a sequential independence assertion. Combining cases gives exactly R02.9, negligible at A2, including the stated polynomial-l1 test class. It does not control data-dependent character choice or arbitrary nonlinear tests.

**Controls.** In n=2,q=5 with roots 2 and 3, alpha=(1,0) gives centered coefficient frequencies w=(1,2). Then W(3)=2, W(2)=0, `|Norm(1+2X)|=5`, and `dist(w/5,Z^2)=1/sqrt(5)`: both normalization bounds are tight. The same ring shows why the uniqueness gate matters: F=(1,1), F'=(0,-1), U with CRT values (0,1), and U' with values (0,3) give two decompositions with b=d=1; the claimed strict norm gate fails, as it must. For n=2,q=5,d=1 and zero noises, a one-coordinate alpha has U factor 3/8 and a one-coordinate beta has V factor 1/2, checking both the active correction and the need for noise suppression. Finally A2's A marginal has support at most `binom(n,d)(q-1)^d(2b+1)^n`, a negligible fraction of q^n. It is statistically far from uniform despite CHAR, so CHAR cannot imply general pseudorandomness.

I also reapplied registry R18's CP-1 control: the selected event has probability .0105>.01 despite the listed residual marginals. That false product argument is not used in either the pointwise H_seq density bound or the fixed uniform-subset symmetric-mean inequality.

## Source-law scope for multiple samples

The common-K source uses one uniform K independent of the entire Gamma_m and publishes `(U_i+F_i,U_i K+H_i)`. With active U_i, conditional on U_vec, its ideal-point vector has q^d possible values, versus q^(dm) for independent ideal points. Their latent TV is `1-q^(-d(m-1))`; for R=F_3,U1=U2=1 this is 2/3. That distance need not survive public projection, but the mismatch prevents a tensor-product import of P0.

The complete sample-major H_seq uses the full stacked matrix, with cross blocks `-tau^2 M_Fi M_Fj^T`. It is a different kernel, including potentially different one-row marginals, and the displayed sufficient target width changes to sqrt(m)sigma. A source hardness premise for that exact tuple is missing. Its source-law description is coherent; full quantitative noise/extraction and task-conversion checks belong to the other critics. No polynomial-sample result for one unchanged reference target follows from P0 alone.

## Material objections and dependency footprints

**C02-O1 — probability-qualified ATT versus unconditional prose.** ATT v2's finite inequality is acceptable; F03's literal planted acceptance one and R02's unqualified “security ceiling” / “subexponential upper bound” wording do not follow for an unspecified probabilistic implementation. Footprint: ATT-related prose in candidates/A.md, parameter-table.md, sources-and-assumptions.md, refinement/R02-break-A.md, and final synthesis; it does not invalidate BSH, BNG, UNIQ, CHAR, AN, or the source hypothesis definition. Repair: retain p_alg and its actual repetition cost everywhere, or adopt the separately authored ATT-D v1 correction only after a different critic checks it. This is not a claim that the desired algorithmic bound is false.

**C02-O2 — missing exact computational source premise.** P0 v2 remains an open assumption. Independent-noise HLBDD, a public shear, an efficient hidden-F sampler, small fixed characters, uniqueness, and failed attack searches do not supply it. Footprint: P0 v2 and every claim presented as unconditional hardness through A0 v2/B0/S0; the finite conditional bridge and the analytic AN claim do not need to be retired. Repair: mark exact source hardness deferred and phrase the bridge conditionally. No in-scope existing source transfer closes it.

**C02-O3 — no tensorization of P0 into Pm.** The common K and full H kernel change the joint source; m also changes the conservative width. Footprint: Pm v1 and any unconditional or unchanged-target reading of M0 v2. Repair: preserve the exact separate source assumption, sample budget, and width change. The frozen M0 wording already respects this objection.

The old D02 wrapped-lift ambiguity is resolved by the separately identified R01 correction and does not remain an objection to BNG v1 as frozen with that evidence. No additional material flaw was found in BSH, the main-width BNG bound, scoped B retirement, UNIQ, or the fixed-character calculation.

## Exact claim-version dispositions

Here ACCEPT means no remaining objection from this bounded critic to the stated scope; it does not override the coordinator's dependency or certification gates.

| Claim | Disposition | Scope |
|---|---|---|
| A2 v1 | ACCEPT | Exact mathematical source definition and coherent polynomial approximation interface; no hardness conclusion. |
| P0 v2 | DEFER | Exact joint computational premise is unsupported; C02-O2. |
| A0 v2 | DEFER | A fully supported hardness construction is not established. Its statement of the missing premise is accurate. |
| BSH v1 | ACCEPT | Exact public transform and conditional uniformity, preserving the specified base law. |
| BNG v1 | ACCEPT | Main-width wrapped bound under the exact iid-shear independence conditions and R01 residue convention. |
| D0 v2 | ACCEPT | Retire only the tested negligible-error completion route; source map retained. |
| ATT v2 | ACCEPT_CONDITIONAL | Stated runtime/advantage route with p_alg and the actual solver policy/repetition cost retained; no unconditional numeric success imported. |
| UNIQ v1 | ACCEPT | Strict norm criterion; information-theoretic uniqueness only. |
| CHAR v1 | ACCEPT | Fixed characters and polynomial-l1 fixed combinations, including uniform H_seq comparison and truncation costs. |
| AN v1, source-law portion | ACCEPT_CONDITIONAL | Exact law and sampler interface match; full acceptance depends on the other critics' NC1/X1/PR1 checks. |
| Pm v1 | DEFER | Coherent separate exact source law, unsupported computational premise; C02-O3. |
| M0 v2, source-law portion | ACCEPT | The stated limitation and separate common-K premise are correct; full quantitative theorem is outside this review. |
| Proposed ATT-D v1 | DEFER | Newly authored correction in proposed-ATT-v3.md; requires a different reviewer. |

## What may safely appear in the final report

The final report may state that A2 is an explicitly sampled correlated source with analytically compatible bridge obligations if the companion reviews close those proofs, while its exact computational hardness is still open. It may retain the exact source shear and the narrowly scoped wrapped obstruction retiring B's tested completion route. It may state uniqueness without an efficient decoder and suppression of the explicitly bounded fixed-character class without calling that hardness evidence. It may include ATT v2 with its solver-success qualification; an unconditional deterministic attack needs the fresh check of the separate correction. It should keep Pm separate from P0 and record its changed kernel, sample budget, and widths.

It may not claim a completed binary-secret RLWE hardness construction, supported exact A2 source hardness, general public-simulator impossibility, practical security parameters, novelty from a failed search, or an unchanged-target polynomial-sample theorem from the one-pair premise.

Research stopped after the bounded checks above. No CPU experiment was allocated or run; hand controls and read-only source/hash checks are the evidence. All author inputs were read-only, and all C02 files are confined to the assigned criticism directory.
