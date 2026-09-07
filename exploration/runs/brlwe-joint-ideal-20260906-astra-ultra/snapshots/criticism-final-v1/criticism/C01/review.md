# C01 independent review of bridge, extraction and common prime regime

Completed 2026-09-06, research ended at 15:46 UTC, before the 16:10 research stop and 16:15 task deadline. Reviewer C01 did not author the reviewed claims. This is a bounded adversarial mathematical review, not formal certification or statistical evidence from independent models. No workers, experiments, external execution, goals or continuation were started.

**Result:** accept the conditional bridge, the exact posterior collision identity, the every-support extraction theorem in its stated asymptotic range, and the prime-existence argument. A2's analytic compatibility is accepted here conditional on C03's review of completion and implementation. Exact source hardness remains open. One dependency-record correction is required for the instantiated A2 recovery claim S0; no counterexample to the reviewed bridge or extractor was found.

## Frozen provenance and blindness

The active manifest was read before research, with affirmative launch_authorized and deadline_supervisor_verified. Its exact run identity, model policy, absolute project/output paths, start and hard deadline, and every phase deadline were verified. The independently imposed earlier task deadline was respected. Machine-readable evidence, every reviewed file's SHA256, the unchanged blind report hash, and primary-source locations are saved in [inputs-and-verification.json](inputs-and-verification.json). All files in the review-v1 manifest matched their recorded hashes.

The proof-blind stage read only the required contract, complete counterexample registry, plan/configuration and F01/D01 frozen theorem packets, plus permitted primary sources. [blind-check.md](blind-check.md) was saved before any author proof, claim status, canonical candidate or compatibility note was opened and remains unchanged. The stage-2 review then read these snapshot files in full:

- foundations/F01.md and both F01/D01 theorem-v1 packets;
- development/D01.md and development/coordinator-prime-regime.md;
- refinement/R01-compatibility.md and refinement/R03-interface-audit.md;
- candidates/A.md, bridge.md, parameter-table.md, dependencies.md and claims.json.

Snapshot review-v1 was frozen at 2026-09-06T15:36:43.466709+00:00. Important hash anchors are F01 theorem e8b8218ca2bb2d851b6068b4456983739cf5188bd4f12c49d880054064068852; F01 proof c6a09c470a6d2e8b62f0e592d6b7fae4c87d89cca4179c597d2a296c5fd22039; D01 theorem 83f76af8f9a8364dcef3937df0ca0bf70c7745f8c5ab78e65e8cc823d7a2f3df; D01 proof 154d1b1d343d3ef8bbf3bde6a6589a773af7f3ca5be840ac37ebf0b7ebb97bbe; and claims.json 4c1194bb72d934fd2207182999a6eb72a7a82b47da6e314c3989d38cd563274d. Full hashes for all other reviewed files are in the verification artifact.

## Bridge and recovery checks

The actual source is the pair (U+F,V+H), with Gamma=(J,U,F,H) independent of the fresh S,G, and V conditionally uniform in I=Ann(J). Only that pair is public. No binary secret is an input to the source definition.

The first reduction samples public S,E and ignores its second challenge coordinate. The second samples an independent public S0,G0 and forms Y=S0+G0. Neither needs source coins, J, a quotient algorithm or the completion sampler. This verifies the hidden-Y-sampler requirement constructively, including both computational endpoints.

The noise edge appends only independent S to the compared tuple (J,U,F,noise), so H is averaged out. Extraction uses H as an output-map input and therefore retains H,Y along with J,U,F. After extraction, K=Z-pi_J(Y) is conditionally uniform in R/J; multiplication by bijective U makes UK uniform in I with a conditional law depending only on J. This proves the required full source/Y product law. Finally (a,c) -> (a,ay+c) is bijective for every y, even with zero divisors. The two computational tests need not have equal advantages. Their summed advantages plus eta_N+eta_X give B0.

For a nonbijective U, uniform K maps to uniform UR. Its exact conditional discrepancy is 1-|UR|/|I|. For uniform ideal U the average is 1-(1-1/q+1/q^2)^d; direct nonzero active-coordinate sampling has zero defect but defines a different source law. Both formulas are correct. No inverse-polynomial failure mass is dropped.

The implementation coefficients 2 xi_src+2 xi_1+xi_Y+xi_target are correct. Source approximation enters two source endpoints; B1 sampler error enters both of its endpoints; B2 preserves uniformity for any independent approximate Y, so only one Y error is charged. Public target TV alone does not transfer the original planted witness.

One-sample self-verification gives planted acceptance at least epsilon_rec-delta_T. For fixed uniform-input a, acceptance implies membership of b in the union of at most 2^n translates of T, hence uniform acceptance at most 2^n |T|/q^n. This remains valid when Rec chooses its output adaptively from that same input. With B=ceil(sigma log n), (2B+1)/q <= 2 log n/n^c+3/(2n+1), making the volume term negligible. The author Gaussian integral bound, unioned over n coefficients and using sigma<=n^K, makes the tail negligible. Thus one target sample really suffices for this one-sample exact-recovery consequence. Held-out verification is a distinct argument that consumes the additional samples it uses.

Hand controls included: equal source marginals but C=A; hidden G coins and H=E-FG; omission of H in extraction; retention of H on the wrong noise edge; zero active coordinates; full F01 F_3 example with unequal computational gaps 0 and 1/9 and extraction loss 1/3 summing to target advantage 4/9; adaptive same-input recovery; and the shared-K diagonal source. The imported CP-1 probability 0.0105>0.01 rejects marginal selected-stage products. Here product claims use either originally independent coefficient pairs or genuinely fresh held-out samples after conditioning; no cached-prefix shortcut occurs.

## Joint extraction and primary-source hypotheses

The source-theorem statements were directly checked against the primary PDFs, not inherited from the author summaries:

| Primary source actually checked | Exact location and matching requirement |
|---|---|
| [Breuillard--Varju, arXiv:1810.13360v2](https://arxiv.org/pdf/1810.13360v2) | Section 5.1, Definition 22 and Proposition 23, printed pp. 23-24. Distinct nonzero coordinates, low-Mahler polynomial exclusion, coefficient support, strict L2 deficit, duration/logarithm gates; arbitrary tuple subsets are allowed. This statement does not assume RH. |
| [Voutier, height paper](https://arxiv.org/pdf/1211.3110) | Theorem and Corollary 2, printed pp. 3-4. The needed corollary applies to a nonzero algebraic number of degree m>=2 that is not a root of unity, giving log Mahler measure >2/(log(3m))^3. |
| [Xylouris, Acta Arithmetica 150.1](https://www.impan.pl/shop/publication/transaction/download/product/83078) | Introduction and Theorem 1.1, printed pp. 65-66. Least prime in a reduced residue class is at most C times modulus^5.18, with effective absolute C. |

The independent derivations and finite controls are detailed in the frozen blind report. In particular the posterior bit is Bernoulli with p_y=W(y-1)/(W(y)+W(y-1)). Two independent replicas conditional on the SAME Y yield iid differences with probabilities beta/4,1-beta/2,beta/4, where beta=4 E p_Y(1-p_Y). This is neither a prior-replica substitution nor a uniform ternary substitution. The exact collision excess for a fixed T is

    C_T-1 = q^d E_Y Coll(pi_T(S)|Y)-1,

and uniform support averaging yields M_d=q^d E[binom(z(Delta),d)/binom(n,d)]. These are the chi-square divergences of the corresponding joint laws retaining Y, or T,Y. Their nonnegativity and the TV square-root bound follow directly. The wrapped Gaussian shift-overlap argument gives beta>1/2 for ell>=3; the exact L2 deficit beta-3beta^2/8 is then at least 13/32, exceeding rho=1/4.

The joint theorem is specialized with M=1, D=d, Q=q and index n-1, since there are n coefficients. Lambda=log(Q^D)=d log q. The absolute summed probability error is converted by q^d/(n)_d for ordered-support averaging, or q^d for a singleton. The every-T theorem deliberately uses the latter factor. It does not combine scalar coordinate estimates.

For all-root admissibility, put L=log n and kappa=L^-3. Eventually kappa<2/(log(3n))^3 and exp(kappa)<2. Unit integer content, the degree-one cases and Voutier exclude all noncyclotomic factors of any relevant polynomial of degree below n. Every CRT root has exact order 2n. A cyclotomic index divisible by q would have degree at least q-1>=2n; otherwise its roots modulo q have the exact cyclotomic order by squarefreeness. Either case excludes a vanishing factor of degree below n. The blind report separately checked the q-power-index reduction formula, reaching the same conclusion. Degree n itself is a real obstruction, witnessed by X^n+1, so the strict 3Lambda<n gate matters.

Sign pairs and inverse pairs are permitted distinct nonzero tuples. For r,-r, even and odd coefficient polynomials provide an explicit invertible two-coordinate transformation over odd q; no equality of coordinates follows. Their dependence is controlled by the joint imported theorem. There is no support rejection, exceptional prime or root set, RH step, or probability mass silently charged as negligible.

For d in the frozen natural-log range and q<=n^K, the duration requirement is at most 4 C_BV K d^2 L^7 <=4 C_BV K n/L=o(n). The negative exponent is at least c_BV n/(8K d L^6), while normalization costs at most KdL; their ratio tends to infinity uniformly because n/(d^2 L^7)>=L. The remaining gates Lambda>=L^3, log Lambda<=L and 3Lambda<n hold eventually. Absorption and the square root give exactly the advertised constant form, with c_K=c_BV/(32K) after enlarging N_K. The exponent is at least c_K sqrt(n)/L^2, hence negligible. A2's d=floor(sqrt(n)/ell^4) is eventually in this range because ell>=L and sqrt(n)/(ell^4 L^2) tends to infinity.

The original d=floor(n/ell^3) is not covered: the displayed duration gate would be of order n^2 L. This is failure of that sufficient estimate, not a counterexample to the larger-dimension extractor.

## Prime regime and canonical A2 interface

Let h be a fixed integer greater than 1+c. Applying the checked Xylouris theorem to residue 1 modulo 2n^h gives

    2n^h+1 <= q <= C(2n^h)^5.18.

Since n is a power of two, q splits X^n+1. Also q/(2n ell^3) >= n^c eventually; every fixed K>5.18h absorbs the upper-bound constant. Thus c=1,h=3,K=16 is a legitimate eventual choice for every sufficiently large power-of-two n. Enumerating the progression and trial-dividing candidates is polynomial in n under this fixed polynomial bound. This is an existence/complexity result, not a practical generation estimate or a proof for every fixed K>1.

A2 uses exact truncated coefficient F and one exact canonical H_seq law in coefficient order. Its matrix is positive because tau^2 ||M_F||^2<=sigma^2/4. H_seq uses only F and fresh source randomness; V is independently uniform in I. The same fresh full wrapped D_ell auxiliary is used in both the extractor and noise interface. H_seq is retained for extraction and integrated out for noise. The older D01 illustrative paragraph referring to F_impl,H_impl is covered by the theorem's arbitrary independent-kernel quantifier; canonical A2/R01/R03 govern the actual computational source. No redefinition of the frozen extractor is needed.

I checked the interface-level distinction between H_seq, the noise-proof intermediate D_B, and implementation error. Eta_seq is a mathematical noise-comparison term; whole-source approximation is charged at the two source endpoints. This does not double count H implementation error. R03's conditional table errors are uniformly bounded over sampler histories and are combined by a sequential coupling sum; no selected-stage marginal product is asserted. The detailed completion/sampler proof and its constants remain assigned to C03, so AN's final unconditional disposition requires that separate check.

## Objection and dependency footprint

**C01-O1 — S0 v2 omits AN in the instantiated A2 dependency record.** The coordinator flagged this metadata omission during review; C01 independently confirms it. S0 v2 lists B0 and REC with conditional P0, but an A2 negligible-error conclusion also needs AN to supply negligible statistical and implementation losses. This is a GAP in dependency closure, not a false recovery inequality or a bridge defect.

The correction and proposed S0 v3 record are in [correction-S0-dependency.md](correction-S0-dependency.md). Add AN's reconciled version to S0's explicit dependencies. The affected footprint is S0 and any final A2 exact-recovery consequence that omits the statistical premises. B0, REC, XG1, X1 and PR1 do not need mathematical modification. A0 v2 already lists AN. P0 remains open after this repair. No other material mathematical objection was found within the assigned scope.

## Version-specific dispositions

ACCEPT below means the exact stated mathematical claim passed this bounded review, subject to the stated hypotheses; it is not a claim that a computational assumption has been proved.

| Claim/version | C01 disposition | Exact scope |
|---|---|---|
| SC0 v1 | ACCEPT | Consistent paired source definition and hidden/public interface. |
| Y0 v1 | ACCEPT | Fresh public independent sampler; no hidden challenge inputs. |
| X0 v2 | ACCEPT | Correct retained-variable hypothesis schema, not an automatic bound. |
| N0 v2 | ACCEPT | Correct sufficient noise schema integrating H. |
| U0 v2 | ACCEPT | Exact image-loss formula and distinct active-unit law. |
| B0 v1 | ACCEPT | Conditional finite theorem, including optional approximation accounting. |
| XG1 v1 | ACCEPT | Exact posterior ternary law and joint collision identity. Existing experiment results were not needed or rerun. |
| X1 v1 | ACCEPT | Every-T asymptotic theorem in its exact d,q,G range, from the checked primary results. |
| PR1 v1 | ACCEPT | Eventual split-prime family for sufficiently large fixed K, including the given example. |
| A2 v1 definition | ACCEPT | Exact law is fixed and matches the extraction/bridge interfaces; no hardness verdict. |
| NC1 v1 | DEFER | Detailed completion proof belongs to C03. |
| AN v1 | ACCEPT_CONDITIONAL | Interface and simultaneous numerical regime pass; final disposition inherits C03's NC1 and implementation review. No source hardness is inferred. |
| P0 v2 | DEFER | Open computational hypothesis; C01 found no supporting reduction and conducted no new hardness search. |
| A0 v2 | DEFER | Fully supported hardness construction still lacks P0 support; the conditional implication through AN+B0 is sound. |
| REC v1, m=1 component | ACCEPT | Same-input exact planted recovery bound and baseline tail/volume estimates. General m review remains C03's assignment, though the stated fixed-candidate union-bound interface is sound. |
| S0 v2 | GAP | Dependency metadata C01-O1 for the instantiated negligible-error A2 statement. Finite one-sample recovery mathematics is accepted. Proposed v3 is valid conditional on AN and P0. |

## What may safely appear in the final report

It is safe to report a correct conditional one-sample reduction with two source tests; the joint every-support extractor proved from the checked BV/Voutier statements; and a nonempty eventual polynomial split-prime regime. Subject to C03's completion and implementation disposition, it is safe to report A2 analytic compatibility using one matched source law and auxiliary distribution. Under that analytic compatibility and the explicit, still-open exact pair assumption P0-A2, the baseline gives one-sample decision and one-sample exact planted-recovery consequences.

It is not safe to present AN as independent evidence of source hardness, replace the exact active-U correlated source by an external marginal or independent-noise assumption, certify practical parameters from the unspecified asymptotic threshold, claim extraction at A1's larger dimension, or extend this one-sample result to independent shared-secret samples without the new source/noise argument. The source-hardness audit and detailed multi-sample/noise review belong to the other critics. No theorem novelty claim or full reproof of the imported primary theorems is supplied by this review.

## Reconciliation check before freezing this report

At 15:48 UTC, after completing the core review, C01 read the coordinator's separately identified `corrections/NC1-v2-and-dependencies.md`. It explicitly changes S0 to v3 with dependencies AN v2, B0 v1 and REC v1, conditional on P0 v2. AN v2 propagates C03's guarded NC1 v2 dependency. **This proposal closes C01-O1** as a dependency correction, provided the coordinator records those versions exactly and AN inherits C03's final guarded-completion disposition. The mathematical REC and B0 statements are unchanged. S0 v2 remains GAP historically; proposed S0 v3 is ACCEPT_CONDITIONAL on AN v2 and P0 v2. C01 does not claim to have independently audited C03's entire NC1 repair.

The core C01 review is now frozen. The coordinator separately authorized a bounded, nonauthor reconciliation check of C02's proposed ATT v3; any result will be in ATT-recheck.md and will not change this proof-blind report or the core bridge/extraction dispositions. C01 stops all research on returning the completed assigned reports and by the original deadline.
