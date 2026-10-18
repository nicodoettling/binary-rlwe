# RT2 exact-byte weighted v2 recheck

Role: nonauthor full-proof/source/parameter/complexity reviewer. Target: `coordinator/tower-lift/weighted-v2/theorem-only-v2.md`, SHA256 `1345e18aec9ecd74517ba400b03b66f70819dfe327710110d54c2924076e44bf`, with `proof-clarification-v2.md`. The complete new assignment is preserved in `recheck-assignment-preserved-v2.md`; actual input hashes are in `recheck-input-manifest-v2.json`. The unchanged RT1 weighted and moment proof hashes match their v1 frozen values. No blind report or rejection file has been read. No new experiment, research branch, subagent, or goal was started.

**Disposition: exact v2 rechecked, no mathematical defect found; PROVISIONAL, no acceptance issued.** The explicit conditional/joint-law and success-budget statements below are supported by the unchanged algebra/probability ingredients. This report does not discharge the short-multiplier algorithm, upstream source/advantage/cost obligations, or a standard hard-family reduction. Previous reports and failed-extension controls remain unchanged.

## 1. Exact statement delta

An exact textual comparison is preserved as `statement-diff-v2.patch`. Definitions and Claims 1 and 2 are unchanged. Claim 3 now begins with a fixed nonzero multiplier chosen before and independently of the fresh sample, and separately states the randomized-multiplier conditional moment, its integrated moment, and the conditional/joint TV alternatives. Claim 4 now distinguishes polynomial numerical certificate, positive stated success, and the additional assumptions needed for polynomial amplification. The allowed sources, algebraic family, full Gaussian normalizer, zero inclusion, constants, widths, and numerical inequalities do not change.

The recheck treats those revised sentences as load-bearing. It does not inherit a stronger certification from the favorable reading of v1 in RT2's earlier report. The earlier reports remain a record of what was checked and how the compact wording was interpreted then.

## 2. Fixed multiplier and randomized reference law

For fixed valid a, set T_a=Pi M_a. The unchanged proof gives

    Cov(X) <= W^2/(2pi) Id,
    ||T_a||_F^2=n||a||^2,
    E||T_a X||^2 <= n W^2||a||^2/(2pi).

Let mu be the law of a randomized multiplier U, with valid membership and norm premises pointwise on its allowed outputs. The independent reference is Q=mu times D_(J,W). Conditional on U=a, X has exactly the original full Gaussian law, so

    E_Q[||Pi(UX)||^2 | U=a] <= n W^2||a||^2/(2pi).

Integrating this inequality gives

    E_Q||Pi(UX)||^2 <= n W^2 E_mu||U||^2/(2pi).

The norm premise bounds ||U|| uniformly, so the expectation is finite in this specification. For represented ideal vectors the multiplier support is countable. The pointwise kernel calculation is defined for every allowed a; only positive-mass branches contribute to the integral. There is no informal conditioning on a zero-mass selected event.

These are statements about the independent exact reference, not the implemented approximate law. RT2-NC1 remains a mandatory rejected extension: for the preserved finite ideal law, sample-dependent a(X)=3 conjugate(X) when X is nonzero and a(0)=3 gives actual moment 81/2 versus the invalid expression 27/2, or 9 versus 11/6 at the other schedule. V2's independent reference and conditional statement exclude that shortcut explicitly.

## 3. Conditional TV and joint TV both suffice

For each allowed a, let E_a consist of tagged/off-ideal failure, Y=0, or ||Y||>B_a, where B_a=sqrt(n/(2pi h)) W||a||. The unchanged reference calculation gives

    Q(E_a | U=a) <= 4sqrt(m)/W+h.

If the implemented conditional sample kernel P_a has TV(P_a,D_(J,W))<=eta for every allowed a, then

    P_a(E_a) <= Q(E_a | U=a)+eta.

Averaging over the multiplier law gives the claimed bound. No successful branch is renormalized, and no conditional second moment of P_a is asserted.

Alternatively, assume TV(P,Q)<=eta for the complete joint law, where Q=mu times D_(J,W). The set

    E={(a,x): x produces tagged failure, or Pi(ax)=0, or ||Pi(ax)||>B_a}

is one measurable joint event. Its radius may depend on a because a is part of the joint state. Under Q, averaging the pointwise reference inequality gives Q(E)<=4sqrt(m)/W+h. Therefore

    P(E)<=Q(E)+eta<=eta+4sqrt(m)/W+h,

with the final cap at one. Joint TV need not imply a uniform conditional-TV bound; that is why this is a separate proof rather than an invalid deduction of one premise from the other. Marginal TV for X alone does not control this joint event. V2 expressly rejects that weaker premise.

If the multiplier premises fail with probability beta, tag those branches as failure. Under the reference, split the multiplier space into valid and invalid outputs before drawing the fresh sample. The event bound is at most beta+(1-beta)(4sqrt(m)/W+h), hence at most beta+4sqrt(m)/W+h; transfer or average the valid-source error as specified and add eta once. Thus the conservative overall bound is min(1,beta+eta+4sqrt(m)/W+h). The multiplier-failure event is not silently removed by conditioning.

The preserved TV-contamination and CP-1 controls still reject transfers of unbounded moments and products of selected marginal bounds. V2 uses neither. All zero/off-ideal branches and the full Gaussian normalizer remain present.

## 4. Polynomial certificate, positive success, and repetition are separate

The unchanged norm argument gives lambda_1(I)>=A. For a valid multiplier, the normalized radius satisfies

    B_a/A <= C0 sqrt(nm/(2pi h)) W/D^(1/m).

Since D>=1, polynomial numerical values of m,W,C0,h^(-1) make this a polynomial numerical bound. This algebraic fact has no implication about positivity of the probability certificate. In particular, W=4sqrt(m) makes eta+4sqrt(m)/W+h>=1+h>1 even when all parameter values are polynomial. V2 now states the extra strict inequality explicitly.

Writing delta=1-eta-4sqrt(m)/W-h, the one-shot success lower bound is max(0,delta). Positivity alone need not give an inverse-polynomial margin. As a numerical control, W=8sqrt(m), eta=0, and h=1/2-2^(-n), n>=2, yield delta=2^(-n), although W and h^(-1) have polynomial values. This is only a parameter check of what the displayed bound certifies; it does not assert an actual sampler, a matching success upper bound, or a new experiment.

V2 correctly draws no polynomial amplification conclusion from such a margin. Any repetition argument based on the stated lower bound must separately control the inverse success margin, the appropriate fresh conditional law on every preceding history, the represented inputs and outputs, the multiplier and sampler construction costs, and any stopping/verification cost. V2 expressly supplies no amplification theorem or available algorithm. The width's bit length alone remains insufficient for the numerical certificate, as already checked in RT2's source report.

## 5. Unchanged dependencies and computational scope

The perfect normalized-trace pairing and C=IS J^(-1) identity are unchanged. The norm/index identities, ideal eligibility obstruction, covariance/Frobenius estimate, proper-subspace bound, and lambda_1 lower bound are unchanged. Their full reconstructions remain in `full-review-v1.md`. The line-mass identity there uses the correct parallel-coordinate correction and does not rely on the inaccurate perpendicular-coordinate wording in root's frozen prose.

The weighted theorem depends on those individual covariance/subspace ingredients; it does not require acceptance of the complete product-transfer theorem. The old source-complexity report remains applicable: ROOT-SAMEJ is a restricted conditional input, not an arbitrary-ideal oracle; no recovery advantage-to-TV schedule, Qstar definition, uniform finite recovery/sampler code, or standard hard-family bridge has been newly supplied. No efficient short complementary multiplier algorithm is supplied. Ordinary basis/membership arithmetic is polynomial in encoded sizes but does not solve the missing short-vector problem.

Dependency update for the coordinator: the revised fixed/random reference-law and complete-event TV statements and the separated Claim 4 parameter interpretation have been freshly rechecked against the exact v2 bytes. No new flaw was found. Their status remains PROVISIONAL pending coordinator reconciliation and all other acceptance gates. The effective multiplier and standard-hardness implications remain BLOCKED; upstream source execution/advantage statements remain conditional and unverified here. This report issues no acceptance and does not read or reconcile blind conclusions.

## 6. Preservation and experiment boundary

The new input receipt records the exact v2 statement/supplement, complete assignment, unchanged author proofs, prior RT2 reports and finite-control artifacts, and administrative live-cap inputs. The v1 artifact manifest is checked separately without rewriting any v1 report, counterexample, code, output, or hash file. No new experiment was needed because the amended claims use the same reference-law identities and explicitly retain the already targeted independence, joint-law, zero, and success-margin restrictions. The full existing finite controls remain evidence within their original bounded scope, not proofs of an infinite Gaussian or an algorithmic hardness theorem.
