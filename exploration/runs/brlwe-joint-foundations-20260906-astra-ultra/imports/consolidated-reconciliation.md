# Versioned reconciliation of the interrupted joint-ideal investigation

The source run is read-only. This document reconciles its complete raw reports, not just its unfinished summary. Paths below are relative to [the source run](../../runs/brlwe-joint-ideal-20260906-astra-ultra/). Exact hashes are in [input-hashes.json](input-hashes.json). Every original claim version remains in the source ledger and the historical section of the consolidated ledger.

“Closed” means the identified objection has a checked resolution in the stated version. It does not mean the entire research program or every certification gate is complete. Mathematical claims retain `PROVISIONAL` with version-specific review dispositions. The computational premises P0 and Pm remain `OPEN`.

## Material objections and amendments

| ID | Exact issue | Resolution and scope | Current footprint / evidence |
|---|---|---|---|
| R0-01 | A1's proposed d=floor(n/ell³) exceeds the sufficient joint-walk duration range. | **Open for A1.** A2 uses d=floor(sqrt(n)/ell⁴), for which the checked range holds. Failure of the earlier estimate is not a counterexample to larger-d extraction. | X1 v1, A2 v1, AN v2; C01/review.md, D01.md, R01-compatibility.md. |
| R0-02 | An arbitrary approximation class for H does not define one exact computational source. | **Closed as a definition repair.** A2 uses one canonical H_seq law. Implementations approximate that exact source with whole-source error charged at two endpoints. H_seq is generally not D_B. | A2 v1, NC1 v2, AN v2, MN v2, P0 v2, Pm v1; C01 and C03 reviews. |
| R0-03 | B's retained F is modular, so conditioning on a specific integer lift is too strong. | **Closed.** The proof conditions on wrapped residue fibers; character factors agree over lifts, and integer atom masses supply valid lower bounds. | BNG v1/D0 v2; C02/review.md and R01-compatibility.md. |
| R0-04 / C02-O1 | ATT v2 has a probabilistic decoder with unspecified success; acceptance one and an unconditional security ceiling do not follow. | **Closed only for the separately selected deterministic ATT v3.** Preserve v2's p_alg−p_false formula and actual repetition cost. C02 authored a new exact-SVP solver policy, and C01 freshly checked it. No success probability is retroactively assigned to the older implementation. | ATT v3; criticism/C02/proposed-ATT-v3.md, criticism/C01/ATT-recheck.md, corrections/ATT-v3.md. |
| C01-ATT-O1 | The generic arbitrary-q deterministic cost assumes CRT roots without supplying a deterministic poly(log q) procedure for them. | **Closed.** The generic v3 includes a public full root list or primitive 2n-th root. In the restricted polynomial-q A2 ensemble, field enumeration has polynomial-in-n cost. | ATT v3; C01/ATT-recheck.md and corrections/ATT-v3.md. |
| R0-05 | The separate-Y leakage threshold derived for larger A1 was reused at smaller A2. | **Closed.** A2's sufficient threshold is m=Ctau²ln n, C>2/pi; the tau²ln ln n threshold stays scoped to A1. Equality at the stated constants is not asserted. | LEAK v1/M0 v3; C03/review.md and hand-controls.md HC7. |
| C03-O01 | Literal NC1 v1 omits delta<1; positive definiteness alone does not make delta/(1−delta) a valid bound. | **Closed in NC1 v2, v1 rejected.** At M=0,n=p=1,sigma=1,tau=1/3, TV=0 while delta>1 makes the old bound negative. The repair uses trivial TV≤1 outside delta<1 and kappa(beta)<1. C03 freshly checked all branches. | NC1 v2; corrections/NC1-v2-and-dependencies.md and C03/objections.md. |
| NC1 dependency propagation | Replacing NC1 changes every statement whose ledger depends on it. | **Recorded.** AN/MN/CHAR advance to v2; A0/M0 advance to v3. A2/MN's regimes already satisfy the guards eventually. CHAR's mathematical review was on v1; its v2 dependency update is recorded without claiming a new full proof-blind review of the entire amended claim. | Updated claims.json; C02 CHAR review, C03 guarded-completion review. |
| C01-O1 | S0 v2's instantiated A2 consequence omits AN, which supplies negligible statistical and implementation losses. | **Closed in S0 v3.** Dependencies now include AN v2, B0 v1 and REC v1, conditional on P0 v2. C01 checked this exact dependency correction. Finite B0 and REC were not falsified. | criticism/C01/correction-S0-dependency.md; C01/review.md reconciliation paragraph. |
| C02-O2 | No checked external theorem supplies P0-A2's exact active-U, F-dependent H_seq correlated source at the stated parameters. | **Open.** Keep P0 v2 open and the fully supported A0/S0 hardness applications blocked or conditional. The bridge does not justify its own source assumption. | P0 v2, A0 v3, S0 v3; C02/review.md, sources-and-assumptions.md. |
| C02-O3 | P0 cannot be tensorized into common-K Pm; the source correlations and full H kernel differ. | **Open computational premise; source mismatch resolved in statement.** Pm is a new assumption. Prescribed m, full cross blocks and the sufficient sqrt(m) width change remain explicit. | Pm v1, KM v1, MN v2, M0 v3; C02/C03 reviews, D03-common-k.md. |

## Mandatory historical controls and their disposition

The complete original R01–R18 registry remains at `known-counterexamples.md`; its primary provenance is the earlier exploration run. These controls are imported, not discarded because a candidate changed. The raw review reports contain the finite witnesses and hand calculations. This consolidation checked their recorded scopes but did not rerun the original enumeration or turn a bounded search into a proof. Separately, the coordinator reran E01 postprocessing from copied source and saved counts: all 24 rows and eight independent binary-image checks reproduced. The [preparation diagnostic](../../verification/20260906-preparation/math-diagnostics.json) records that bounded verification and its limitation; the original ternary enumeration was not rerun.

| Control | Required interpretation in the consolidated claims |
|---|---|
| R01: binomial scalar-block decoding | Retire the efficiently decoded binomial small-error sampler; A2's richer support does not inherit its claimed hardness. |
| R02: source coins contain G and H=E−FG | Reject vacuous conditional-independence arguments. A2 source randomness remains independent of the bridge G; a public-only relaxation requires its own full proof. |
| R03: uniform marginals, correlated pair | Source pseudorandomness is a joint pair statement; equal marginals do not suffice. |
| R04/R05: Gaussian marginals or pairwise independence leak through joint law | Require the full noise comparison, with the exact retained tuple. Do not infer iid noise from marginals or covariance alone. |
| R06/R07: entropy budgets and ambient kernels | Quotient extraction uses the same-Y posterior collision identity and the checked joint theorem; entropy counts alone and field-kernel dimension do not prove it. |
| R08: precursor identifies S while public image is lossy | A retained-variable obstruction is not automatically a public transcript attack. |
| R09/R10: strict thresholds and residual-box boundaries | Preserve strict rounding and norm inequalities; ensure the verification box is smaller than the modulus in the asymptotic regime. |
| R11: sometimes lossiness | No conversion of a mild/sometimes statement to negligible average exact recovery. |
| R12: verified residual preimages need not be the planted witness | REC uses exact planted success only as a lower bound on decisional acceptance; the converse is not asserted. |
| R13: Rényi event transfer | Preserve P||Q orientation and joint witness law. A positive-event bound does not preserve signed distinguishing advantage. |
| R14: active zero coordinates | Retain the exact image-defect term for uniform ideal U; active conditioning is a different source law. |
| R15: common secret and repeated samples | Shared K is not a vector of independent ideal points; rotations, repeated noise and independent secrets do not produce the target iid shared-secret experiment. |
| R16/R17: statistical planting and discarded cross-disciplinary simulations | No statistically uniform small-noise binary transcript claim, unavailable-secret public sampler, iid-matrix surrogate or renamed old failed mechanism is imported. |
| R18 / CP-1 | The selected-stage event .0105 exceeds .01; marginal residual probabilities cannot be multiplied. The checked H_seq proof instead bounds complete-path normalizers pointwise, and held-out verification conditions on the whole solver prefix before drawing fresh errors. |
| C03-HC1 | Reject unguarded NC1 v1; guarded NC1 v2 returns the trivial bound outside its useful domain. |
| C03-HC2 | H_seq's adaptive normalizer may depend on parity; its comparison with D_B is necessary. Positive marginal covariance complements do not imply a positive stacked complement. |
| C03-HC4 | Positive Fourier ratios may have a signed inverse. The wrapped Z/5 and exact rational controls reject naive independent deconvolution; they do not refute growing-width approximate smoothing. |
| C03-HC5 | Common-K diagonal law over F3 has distance 2/3 from independent pairs. Forgetting hidden variables can reduce that distance; it is not a public lower bound. |
| C03-HC6 | Same-input solver success can coincide with bad noise, so subtract the error tail. Only genuinely fresh held-out errors support the displayed product formula. |
| C02 latent/public F5 control | Distinct latent (F,H) distributions can induce identical public pairs. BNG's lower bound remains scoped to the strong retained-F condition. |
| C02 CHAR control | A2 is statistically far from uniform despite negligible fixed-character bias. The proven class is fixed characters and polynomial-l1 fixed combinations, not arbitrary adaptive or nonlinear efficient tests. |
| C01 ATT new controls | The n=2,q=17 exact dual-rounding example, n=8 subgroup orbit coverage, nonzero SVP output and strict radius check the repaired deterministic policy without assigning hidden support to the algorithm. |

## Version-specific review coverage

- **C01 core:** proof-blind theorem/definition stage was frozen before author proofs were read. Its raw `blind-check.md`, full `review.md`, and `inputs-and-verification.json` preserve the input boundary. It then checked B0, extraction, prime existence and interfaces. Its AN disposition depended on C03's completion audit. It freshly checked the S0 dependency correction.
- **C02:** nonauthor but not proof-blind review of exact source laws, old-source mismatch, B's shear and obstruction, uniqueness, fixed characters and probability-qualified ATT v2. It authored the deterministic ATT correction and therefore did not certify its own repair.
- **C03:** nonauthor completion, sampler, obstruction, common-K, leakage and recovery review. Its `hand-controls.md` preserves new finite controls. It freshly checked the separately hashed NC1 v2 repair; X1, PR1 and CHAR's full argument were outside its assigned scope.
- **C01 ATT recheck:** a subsequent nonauthor check of C02's proposed solver. It found and closed the public-root input defect, retaining A2's separately justified preprocessing. This did not rewrite the earlier blind report.

These agents share a model and project context lineage. Agreement is repeated mathematical review, not independent statistical evidence. The consolidated ledger identifies reviewed claim versions and the exact amendment evidence instead of copying empty precritic disposition arrays.

## Certification boundary and remaining work

No current claim is assigned global `ACCEPTED`. The archive contains substantial derivation, primary-source checks, a proof-blind stage and exact hand controls, but this consolidation has not established a complete clean-state reproducible certification run for every claim and dependency. In particular, the mathematical Gaussian sampler has not been implemented, the asymptotic prime/extraction constants do not yield practical parameters, and a fresh full audit of every downstream exposition after all metadata corrections is not asserted. Hash and graph consistency checks certify file integrity and bookkeeping only.

The central unresolved obligation is **independent computational support for the exact source**, followed by the separate common-K source question. The new run may pursue explicit public reductions or attacks, but it must not treat analytic compatibility, the lack of a polynomial attack so far, or a weaker external source assumption as already closing that gap.
