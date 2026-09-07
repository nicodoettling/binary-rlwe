# C02 proposed reconciliation edits

These are proposed edits only. Frozen author files were not changed. See review.md for exact claim-version dispositions and input-hashes.json for the frozen file hashes.

## C02-O1: attack success wording

Affected frozen material: ATT v2 evidence in foundations/F03-attacks.md and refinement/R02-break-A.md; corresponding summaries in candidates/A.md, parameter-table.md, sources-and-assumptions.md, and any final report.

If ATT v2 is the terminal accepted version, replace unqualified statements such as “planted acceptance one”, “a concrete subexponential upper bound on source security”, and “security ceiling” by:

> The grouped-orbit method has running time exp(O_c(d)) times a polynomial factor under the stated gap. If its designated correct-branch solver succeeds with probability p_alg under the specified policy, its distinguishing advantage is at least p_alg-p_false. The algorithm and repetition policy must supply that success probability; no unconditional numerical success bound is inferred from the frozen probabilistic implementation.

For the finite statement, define p_alg as either a uniform lower bound on success for every correct promised branch or the average success on a fixed designated correct branch, such as the first enumerated branch containing T. Include repetition costs in the runtime. Do not condition it on earlier failed branches without rederiving the probability.

The alternative is a separately versioned correction: [proposed-ATT-v3.md](proposed-ATT-v3.md), labeled ATT-D v1. That note specifies deterministic low-rank exact SVP and gives its complete proposed proof and primary-source dependencies. C02 authored it; another critic must review it before acceptance. If that check closes, distinguish the new deterministic policy from F03's originally unspecified probabilistic implementation rather than silently treating the latter as deterministic.

## C02-O2: computational source gap

Preserve P0 v2 as DEFER/OPEN. A safe synthesis sentence is:

> A2 defines an exact active-U, F-dependent H_seq source and a conditional bridge. The checked literature does not provide a matching reduction establishing pseudorandomness of that same source at these parameters. Its computational hardness is a separate unresolved premise.

Keep any eventual AN acceptance explicitly analytic. Do not cite HLBDD, DSPR, the fixed-character estimate, uniqueness, or failed attack searches as establishing P0. A0 remains a deferred hardness construction unless that premise is separately supported.

## C02-O3: multi-sample source change

Preserve the frozen M0 v2 qualification. A safe synthesis sentence is:

> The common-K extension uses a separate joint source, a full stacked H_seq kernel with cross blocks, and the displayed sample-dependent widths. Its computational premise Pm is not implied by one-pair P0, so it gives no polynomial-sample theorem for one unchanged reference target from that assumption alone.

## Resolved notation point, not a remaining rejection

When quoting D02's two-F-fiber proof for untruncated F, use `p_a=Pr[F_0=a mod q]` on the actual retained ring-variable fibers, as R01 already does. Character periodicity makes the lift-summed fibers valid; their masses dominate the displayed integer D_gamma masses. No new numerical constant or additional latent lift is needed. For A2's bounded coefficients the relevant representatives are unique.

The accepted BNG scope remains the independently sampled iid-shear family under its main-width hypotheses. Its lower bound concerns retained-(J,U,F) noise TV and cannot be promoted to public-transcript impossibility.
