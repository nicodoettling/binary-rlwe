# FF3 phase2 review index

This additive packet preserves author-phase1-seal-v1.json and its87files. Full phase1 review is in ../../reviews/FULL-FF3; it is not blind and does not cover these new versions. No phase2 acceptance is claimed.

Priority theorem-only inputs:
1. exhaustive-kernel-statement-v1.md with corrected proof exhaustive-kernel-proof-v2.md; enum-repair-ledger-v1.md and FULL-FF3-ENUM-SIGN-1. Statement unchanged, proof repaired.
2. compressed-selector-information-statement-v1.md; proof separate. Public-side-information extension is compressed-selector-public-extension-v1.md. Gaussian corollary depends on corrected ENUM.
3. energy-rank-kernel-statement-v1.md; proof separate, with energy-rank-order-conventions-v1.md. Exact integer DP/rank sampling versus real h sampling must remain separate.
4. joint-rank-finite-statement-v1.md; proof separate and explicit47entry certificate experiments/joint-rank-n2-certificate-fv16.json. Full n2 rational model only.
5. compact-selector-statement-v1.md; proof separate and FV11 exact33entry certificate. Generic theorem requires endpoint equations separately; H correctness alone is insufficient after selection.
6. two-event-noise-kernel-statement-v1.md is the new theorem-only split; original two-event-noise-kernel-v1.md is unchanged full note. No finite exact transcendental sampler is claimed.

Exact finite exclusions to review: FV10 three local Farkas witnesses; FV13 joint-residual-n4-farkas-fv13.json; FV17 joint-rank-n4-certificate-fv17.json and saved joint-rank-n4-integer-system-fv17.npz. Reconstruct the matrices from ring probabilities rather than relying only on author serialized matrices. FV13 preserves an independently assembled exact n2 FV11 embedding. FV16 verifies rank normalization for every source input/edge/target class pair. All certificates are checked with integer/Fraction arithmetic after numerical discovery.

Retain UNKNOWN/error distinctions: FV12 and FV15 numeric infeasibility are not exact exclusions. FV16 n4 UNKNOWN and FV17 primal ERROR remain preserved even though FV17's separately obtained exact dual certifies that same n4 model. Source/target rational noise must not be called wrapped Gaussian.

Regression registry: original203references remain in inherited-regression-references.json; original phase1 controls in regressions.json; new controls in regressions-phase2-v1.json. FV14 targets the information theorem's hypotheses, including randomized classes, full-input leakage, nonuniform prior, repaired ENUM sign and CP-1.

Full-direction-open-interfaces-v1.md contains the explicit legal ring symmetry formulas and UNTESTED group-averaged extension. It is not an exhaustion certificate or a main theorem. Phase2-report-v1.md gives the author status summary. Author-phase2-seal-v1.json binds the exact review bytes; later changes require new versions.
