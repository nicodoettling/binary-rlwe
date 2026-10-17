# RP1 fresh recheck of A-PPT ledger v2

**Disposition: PASS for the exact ledger-scope repair and its parameter consequence.** The edited statement follows from the unchanged frozen finite theorem, proof, supplement, and current dependency versions. The unsupported arbitrary-polynomial-q reading of v1 remains rejected. No new mathematical flaw was found. This is a fresh nonauthor parameter/ledger recheck, not a source-hardness proof or a global acceptance vote. At intake all underlying claim nodes were still PROVISIONAL; the coordinator owns their reconciliation, final graph closure, and delivery acceptance.

## 1. Assignment, frozen bytes, and authority

The complete assignment and academic theoretical-cryptography scope are preserved in `assignment.md`. I read the mathematical-proof-audit skill, audit protocol, and probability-regressions reference, then the launcher and its exact cap status. The service was running; RP1's deadline was 2026-09-07T22:42:00Z, before the shared wrap-up and cap. `partial-v1.md` was saved before 22:31 UTC. No goals, children, packages, services, commits, publications, or messages to other people were created. All output writes are within RP1. No content-policy interruption occurred.

I read the full RF1 and already-frozen RB1 reports, RS1's completed report, the exact theorem/proof/supplement, coordinator source and completion notes, current claims, plan/config, and the imported regression registry. Applicable historical original files were read via their authorized index entries. These are correlated Astra reviews; neither blind reconstruction nor agreement is statistical independence or proof by vote.

`input-hashes-v1.json` records snapshots and hashes of every main input, including the immutable edited ledger and a time-specific mutable claims ledger. The four assignment hashes match exactly:

| Input | SHA256 |
|---|---|
| coordinator/A-PPT-ledger-v2.json | e8ac045319cc40b0979cc54a3bd4e6c659badefdeee25dff221fe96cfc680447 |
| candidates/search/theorem-only-v2.md | bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124 |
| candidates/search/proof-v1.md | 198c36bce9a73b87f2e1f5cf644d7e96b13cda063922f1ab10b0b2ee60114042 |
| candidates/search/supplement-v1.md | 71752406e81e327b5c47d0d118ea9bc6aa0f87566d23345daf290a7b8322410a |

The frozen theorem controls mathematical scope; its proof and supplement supply derivations. The live ledger is integration metadata, not authority to broaden that theorem. The v2 ledger states the two concrete d formulas, whereas the theorem also permits a wider conditional interval. Thus v2 narrows to two explicit efficiently computable examples and makes no broader interval-plausibility claim.

The original rejected ledger and the pre-repair scope-defect note were preserved and read. The rejected file retains its historical PROVISIONAL status field, with rejection explained by the separate defect note and replacement metadata; I do not interpret that old field as current acceptance.

## 2. Exact old-defect disposition

Put n=2^ell and d=floor(n/(64ell)). Write the finite proof's entropy charge as

    G(n,q,d)=q^d ((1+D_ell(0))/2)^n,
    log2 G=-n+d log2 q+n log2(1+D_ell(0)).

Let q_128(n) be the least prime 1 modulo 2n^128. It fully splits X^n+1. The same least-prime theorem gives q_128<=C 2^5.18 n^663.04<=n^664 eventually; hence this really is a fixed polynomial-modulus family, and not a superpolynomial counterexample masquerading as one. Also q_128>=2n^128+1>=n^128. Since D_ell(0)>=0,

    log2 G(n,q_128,d) >= 128ell floor(n/(64ell))-n
                       >= n-128ell.

The second inequality follows directly from floor(x)>=x-1. Its right side tends to positive linear scale in n. Consequently G grows exponentially eventually, so the finite displayed upper bound on success does not yield negligible additive loss along this polynomial family. The old prose did not exclude this family.

This is a counterexample to **the asserted parameter substitution/negligible-bound inference**, not a counterexample to actual-secret hardness. A loose upper bound exceeding one conveys no useful recovery bound; actual recovery probability is still at most one. No source distinguisher or target solver contradicting the implication at q_128 has been constructed here. In particular the broad literal implication could require a different proof; this review rejects its support from the frozen argument, not all conceivable proofs.

The exact search finds the first positive displayed lower exponent in ell=1..256 at ell=10,n=1024,d=1: 128*10*1-1024=256. At this finite point the coarser n-128ell=-256 is weaker and negative; the exact floor expression, not that coarse bound, supplies +256. From ell>=11 the coarse bound is positive and increases. Thus the test also detects the distinction between the exact floor lower bound and its asymptotic relaxation.

## 3. Why the repaired parameter sequence closes the bound

I directly checked the primary statement of Xylouris Theorem 1.1: the least prime in a coprime progression is bounded by C times the modulus to power 5.18, with effective C. Its statement was checked, not its analytic-number-theory proof. [Primary paper, printed page 66](https://www.impan.pl/shop/publication/transaction/download/product/83078#page=2).

For the exact v2 sequence q=P(1,2n^3),

    2n^3+1 <= q <= C 2^5.18 n^15.54 <= n^16 eventually.

The exponent slack is 16-15.54=0.46>0. The unknown numerical threshold is fixed independently of every adversary. The congruence gives distinct full splitting. For m=1,2 and sigma_m=2sqrt(m)n ell^3,

    q/(n sigma_m) > n/(sqrt(m)ell^3) -> infinity,

so q/sigma_m>=n eventually. Constants 16,64,1 and the Gaussian widths are chosen before Q or its success exponent.

The zero-shift Gaussian identity gives Z_ell>=ell and D_ell(0)<=1/ell. Since ln(1+x)<=x,

    log2 G <= -n+16ell d+n/(ell ln2)
            <= -3n/4+n/(ell ln2).

For ell>=6 this is strictly below -n/2: ln2>2/3 gives 1/(ell ln2)<3/(2ell)<=1/4. This is an analytic proof valid for every eventual degree at which q<=n^16, not an extrapolation from a search. The baseline d=floor(sqrt(n)/ell^4) is eventually positive and is eventually within floor(n/(64ell)), because 64/(sqrt(n)ell^3)->0. Its floor can be evaluated exactly as isqrt(n)//ell^4. Its finite early zero values, including ell<=43 in the tested range, are permitted by the finite theorem and have no asymptotic effect.

For tau=ell, n*kappa(3ell^2/4)=exp(-Omega(ell^2)); hence Delta_N is negligible, eventually below 1/2, and eta_N<=2Delta_N is negligible. The mask-tail bound mn exp(-pi ell^2)/(pi ell) has the same negligible scale. These errors do not grow with d. The finite sampler's fixed accuracy 2^-n is also negligible. Thus the exact finite inequality yields Adv_Base2(B_m,impl)>=epsilon_m-negl(n), with one uniform PPT wrapper and parameter policy independent of Q. The assumed pseudorandomness of the chosen Base2 family then forces negligible actual-secret success.

Uniform setup is justified for both explicit d formulas: enumerate progression candidates and trial-divide to the first prime; the published polynomial q bound makes this polynomial in unary n, albeit impractical. Roots can also be enumerated in polynomial n time. The explicit d formulas use integer arithmetic. This does not imply polynomial time in log n alone. The wider theorem's merely uniformly computable d clause is not asserted by the repaired ledger as an efficiently generated family.

## 4. Load-bearing proof/interface checks

The finite argument's random law is mu(dC) K_C(dH) P_G(dG) P_S(dS), where C retains the source support, ideal points and used integer mask lifts; G has the independent product D_ell law; H's exact Gaussian kernel depends on C only; and S is jointly independent. The source-mask box event depends only on masks and preserves the relevant product law. The full retained-source noise comparison appends S legitimately, then maps to the witness/transcript law. H is integrated out of that TV comparison. It is revealed only in the completed world for a guessing upper bound. This avoids appending a correlated latent variable through TV.

For each fixed (C,H), revealing pi_J(S) splits each (s,y) joint-mass row into at most |R/J| fibers. Summing maxima over those fibers costs at most |R/J| times the original maximum. No quotient uniformity or independence from Y is required. Since every U_i annihilates the same J, a single quotient works for both samples. Its size is q^d; the factor is not q^(md). The iid noisy-bit identity follows from the Cartesian binary support, pointwise maximization of the full product law and Tonelli. Modulo-q wrapping is a guessing upper bound, not necessarily equality.

For the rectangular completion, M has mn rows and n columns. With b=ell^2 and sigma_m=2sqrt(m)n b ell, the stack norm obeys ||M||^2<=mn^2b^2; hence B>=3sigma_m^2 I/4 and Theta>=3ell^2 I/4. The square-completion identity yields the exact normalized law Q(z)=P(z)r_z/E_P[r]. Bounding |r_z-1| by Delta_N gives TV<=Delta_N/(1-Delta_N) only when Delta_N<1; the stated guard supplies TV<=1 otherwise. For m=2 the cross blocks -ell^2 M_1 M_2^T are present, so the comparison is to the full independent 2n-coefficient target law. The proof-only H is not sampled by the reduction.

The source supplies one pair with independent uniform ideal points conditional on one common hidden support, including zeros. The comparator supplies two independent uniform ring elements. B_1 ignores the second element; B_2 uses both once as multipliers. It generates a fresh common binary S and fully independent target errors locally, invokes Q once, and compares Q's output to the **actual sampled S**. It receives neither a source oracle nor any hidden source data. No additional independent multiplier arises from generating responses. Therefore the exact scope is m=1 or m=2, no decision conclusion, and a separate computational assumption for each d choice.

The sampler has integral sigma_m^2=4mn^2ell^6, cutoff B_E=2mn^2ell^3>=n sigma_m, and N_E=2B_E+1 polynomial atoms. A raw-weight error xi/(8pN_E), p=mn, costs normalized TV at most xi/(8p) because both normalizers are at least one (the zero weight stays exactly one). Dyadic probability rounding costs another xi/(8p); independent product coupling costs xi/4. The tail is at most m exp(-pi n^2)/pi<xi/2 for xi=2^-n,n>=2,m<=2. A deterministic finite table with polynomial precision and independent fixed-length bit blocks implements the sampler. Error accounting xi_source+2xi_alg+xi_target pays both local-sampler endpoints and retains the actual witness in the target comparison.

These checks validate the load-bearing chain relevant to the repaired substitution. They do not assert hardness of Base2 from ordinary RLWE, DSPR, worst-case lattices, or a renamed analytic assumption.

## 5. Newly targeted exact experiment and administrative failure

Command:

    timeout 120s python3 exploration/runs/brlwe-goal-routes-20260907-astra-ultra/criticism/RP1/parameter-search-v2.py

One allocated slot was used sequentially, then released. The successful result `parameter-search-v2.json` completed at 22:32:57.985507 UTC in about two seconds, exit zero. It uses exact integers/Fraction, no randomness, floating Gaussian sums, primality experiments or large cryptographic instances.

The search covers ell=1..256, support denominators {16,32,48,63,64,65,96,128}, and modulus exponent budgets 1..160: 327,680 exact floor/exponent cases. It checks both sides of the floor slack, the repaired n/4 budget and the repaired negative exponent. A 60-term rational atanh series encloses ln2 with an explicit geometric tail. No float approximation decides any inequality. There are 251 repaired ell>=6 cases, 750 exact dyadic-rounding cases, 256 sampler-width/precision cases, 250 small-d false-positive inequalities, 81 guarded-denominator points, and explicit old-denominator, CP-1 and actual-witness controls.

The initial v1 process completed the mathematics, then failed an **overstrict administrative equality assertion** between the frozen ledger object and the mutable claim node. The latter had acquired `reviews` and `mathematical_review_disposition`; its theorem fields were unchanged. `parameter-search-v1.py`, `parameter-search-v1.stderr.txt`, and `parameter-search-v1-failure.json` preserve that failure. V2 excludes exactly those two review-metadata keys and checks all remaining keys plus recursive dependency versions. It passes. The corrected rerun completed before the coordinator's later message advising that no mathematical rerun was needed solely for this metadata change. No failed theorem check was erased. My earlier commentary that the whole current object was byte-for-byte consistent was too broad; the assigned frozen ledger hash matched, and its load-bearing fields match, while live review metadata differs.

Bounded success of these searches is supporting evidence, not a proof for untested dimensions or actual source hardness. The algebra above carries the asymptotic result.

## 6. Historical regressions: explicit applicability

Every one of the 40 registry IDs is classified below. Relevant C03 and N02 original control packets and ATT v3 were checked against their historical index hashes (`historical-input-hashes-v1.json`). Other controls are classified using the imported registry and full completed referee reports, without rerunning unrelated large experiments.

| Control IDs | Disposition for the repaired ledger and unchanged proof |
|---|---|
| R01; C01-ATT | Structured/binomial-support decoding is not an attack on uniform-all-d-subsets by that reasoning alone. The reviewed ATT v3 budget exp(O(d))*poly is retained as a source limitation. Both concrete d/log n tend to infinity, so that bound supplies no PPT refutation. It does not prove source hardness. |
| Small-d source attack (RF1/RS1) | LIVE LIMITATION, directly rechecked. At d=1 enumerate n supports and q amplitudes; accept a residual in [-ell^2,ell^2]^n. Planted acceptance is at least 1-negl; uniform acceptance <=n q(2ell^2+1)^n/q^n. Since q>=n^3 and 2ell^2+1<=n eventually, this is <=n^(4-2n), negligible. Thus the premise at d=1 is false. The repaired two growing families require distinct source assumptions and do not claim plausibility over the entire small-d interval. |
| R02 | C=G,H=E-FG violates the fixed conditional G/product law. The actual proof excludes it; source-dependent H alone is permitted. |
| R03, R04, R05; SE-CORRELATION-F3; PAIRWISE-SE-F3; C03-HC5 | Uniform/Gaussian marginals and pairwise independence are insufficient. Common-K F3 gives TV 2/3; F,S,E=-F-S has product pairwise marginals but triple TV 2/3; E=-S produces the old target discrepancy 2/9. The full joint product assumptions and full stacked completion exclude these models. |
| R06, R07 | Entropy-only extraction and field-kernel-to-Boolean-fiber implications remain rejected. Current proof uses arbitrary-fiber leakage cardinality and the exact noisy-bit guessing identity; no extractor or Boolean collision shortcut is used. |
| R08; C02-LATENT-PUBLIC; PUBLIC-ENCODED-F | Latent distance need not lower-bound public distance (F5 erasure gives 1/2 versus 0). Current reveal only upper-bounds guessing with extra information. Public encoding of F is likewise no obstruction to this direction. |
| R09, R10 | Strict uniqueness, Lucas occupancy and a residual box filling all centered residues remain valid countercontrols for their old claims. No such uniqueness, occupancy or residual-only decision test enters A-PPT. |
| R11; C03-HC6 | Sometimes-lossy does not imply negligible average recovery; success can equal the bad-error event. Current bound is direct average guessing and pays the mask tail by TV/union subtraction, not multiplication by a good-event probability. |
| R12 | LIVE exact-witness check. New dual-number enumeration gives target success 11/16 and 55/64; source acceptances 3/8 and 7/16; gaps 5/16 and 27/64 for m=1,2. Residual verification accepts both worlds with probability one. The wrapper uses equality with its own S. |
| R13 | Positive-event Renyi transfer does not preserve signed decision advantage. No such transfer appears: one exact-success event and its absolute endpoint gap prove the finite inequality. |
| R14; N02-DUAL-NUMBER | Uniform ideal points may have zero active coordinates. They are not conditioned to units. The N02 varying-ideal TV=9/32 control and nonunit quotient isomorphism remain valid; the guessing bound needs only annihilation and cardinality, including zero multipliers. |
| R15; C03-HC7 | No source expansion, common-K replacement by independent ideal points, rotations as independent multipliers, or multiple separately revealed Y values is used. One common G and one quotient are proof-only; the challenge budget stays two. |
| R16, R17; C02-CHAR | Statistical source pseudorandomness, hard posterior transport, tower-packed unavailable responses, matrix independence, symmetry-orbit sufficiency, QCSD shortcuts and fixed-character sufficiency are not asserted. The exact source pseudorandomness premise is computational and explicitly assumed. |
| R18; CP-1 | Reproduced posterior A_b=21/2000,C_b=1/20,D=879/1000, total one; selected event 21/2000>1/100 and later incidence 21/221<1/10. Support restriction/renormalization defeats the old selected-stage product. Current products are explicit unconditional coordinate laws or positive theta sums, not adaptive residual-event products. |
| NC1-v1; C03-HC1 | LIVE guard regression: M=0,tau=1/3,sigma=1 gives true TV zero but delta>2(1-22/63)=82/63>1. The unguarded ratio is negative; the current piecewise expression returns one. Exact rational guard-grid tests pass. |
| C03-HC2 | H_seq has parity-dependent second normalizers and need not equal D_B. Positive marginal complements need not give a positive full stack. Current H is exact proof-only D_B; full B and Theta have the stated uniform PSD margin. No sequential sampler is asserted. |
| C03-HC3 | Discrete covariance is not the Gaussian exponent matrix divided by 2pi. Current proof uses exact quadratic weights and Poisson normalization, with no covariance substitution. |
| C03-HC4 | Positive Fourier ratios can give signed inverse mass (-1/20 entries); narrow wrapped exact deconvolution can fail. Current proof defines positive D_B under explicit PSD/smoothing conditions and pays approximation error. It makes no arbitrary exact wrapped-deconvolution claim. |
| S0-dependency | No old AN/NC1 certificate is inherited. A-FINITE v1 depends on current NC-RECT, A-GUESS, MASK-TAIL and SOURCE-2 v1; A-PPT v2 also depends on SAMP-E and PRIME-POLY v1. These exact versions and paths were checked recursively. |
| W2-SUBGROUP-BOUNDARY; W2-CONSTANT-COMPARISON | n8,d2 subgroup coverage one and the optimized ATT constant qualification remain retained. No all-subgroup negligible-coverage or improved attack-runtime claim is used by A-PPT. |
| UNIFORM-APPROX-COLLAPSE | No exact-comparator entropy no-go is extended to approximate preservation. The uniform source endpoint is the exact target under the specified local sampler; finite implementation TV is charged explicitly. |
| N03-PV-CONDITIONING; N03-SCAL-POSTERIOR | No active-PV signed transfer or independent-prior ratio law after public conditioning is used. Only the mask box is selected, with its conditional product law and TV loss explicit. |

## 7. Final scope and process limitations

The fresh repair gate is satisfied: exact edited bytes checked, the old flaw retained, dependency versions checked, all historical controls classified, a new targeted exact search passed, and constants and quantifiers rederived. **Recommend closing the A-PPT v2 scope-repair obligation**, subject to the coordinator's graph/reconciliation and final-artifact gates. This report does not mutate any claim status or author file.

The conclusion remains a conditional uniform-PPT **actual-secret recovery** implication for exactly one or two coefficient-binary rank-one RLWE samples at the stated concrete polynomial-modulus sequence and widths. Each d choice has its own exact Base2 assumption. No practical security estimate, standard-assumption source reduction, nonuniform/quantum extension, target decision hardness, arbitrary polynomial-q theorem, or additional sample count is certified.

Ordinary access issues: `python` was absent, so administrative code used installed `python3`; no package was installed. The registry's `imports/regressions/...` copy paths were absent in this run, so the indexed authorized historical originals were read instead and their hashes verified. Primary Xylouris PDF text was accessible. These were source/tool access matters, not policy interruptions.

`input-hashes-v1.json`, `historical-input-hashes-v1.json`, the preserved failed and successful scripts/results, `slot-release-v1.json`, and final manifest support reproduction. Use a fresh owned subdirectory for rerunning the script because it refuses to overwrite its result. No acceptance of an unrestricted probabilistic lemma is inferred merely from the finite grid.
