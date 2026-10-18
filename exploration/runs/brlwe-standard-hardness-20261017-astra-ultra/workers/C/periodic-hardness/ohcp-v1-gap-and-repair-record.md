# OHCP v1 rejection and repair record

Recorded 2026-10-17 20:59:37 UTC before writing v2. V1 bytes are retained unchanged. The v1 theorem/proof packet is REJECTED AS A COMPLETED PROOF pending repair; this is not a counterexample to its intended theorem.

Affected immutable files:

- multiplier-ohcp-theorem-v1.md SHA256 e499d9a439f274fad2d353c21fff22f63006ea0ae2a7ad4e10aff85b77a322d1.
- multiplier-ohcp-proof-v1.md SHA256 f215a23cf90d6c785becc8e4eacc3aa39b7208841d29aa54e19da62d9a61b7ca.

B's review identified a normalization gap in proof Sections4–6. The actual oracle acceptance at the starting guess is p(0,t)=p(t+log|e_j/d0|), whereas Section4 bounded the unshifted profile p(s). BRST Lemma3.8, the explicitly read and imported OHCP statement, requires decay of p(0,t) to p_infinity as a function of t. V1 separately imposed kappa>=4S+... and a lower-center bound kappa>=B0, but this did not justify substituting the potentially negative log|e_j/d0| into the displayed decay estimate. A sufficient direct repair would charge S+B0 together in the confidence parameter.

The underlying algebraic lower bound in Section6 is not the defect: for rational coefficient input T and integral J, H0=D*denominator(T) clears e, and the norm argument correctly shows |e_j|/d0>=(H0*d0)^(-n/2) when e is nonzero. Exact-zero error can be recognized by membership under the stated uniqueness promise. This reasoning must not be extended to arbitrary real inputs without an exact representation model.

The coordinator proposed a cleaner repair, to be used in v2: replace the selected center by z*=2+e_j/d0, take OHCP scale3, and use guess g_j=d0(z-2). Then 1<=|z*|<=3, so log|z*|>=0 and the starting-guess decay is bounded by the same unshifted estimate. The enlarged search neighborhood has residual at most6d0, still well inside the posterior smoothing budget. At starting guess z=0 and t=0, the selected residual is at most3d0; the Gaussian comparison constants must be recomputed with that factor. This handles zero selected coordinates and avoids the algebraic lower-center step.

A separate operational refinement from B replaces the unverified GPV sampler import by continuous Gaussian convolution followed by coordinate discrete-Gaussian rounding on the known power basis of R. This is an improvement to the implementation dependency, not the source of the OHCP normalization gap.

All v1 downstream OHCP/DGS conclusions must be reopened. V2 will receive fresh review; no review or acceptance is inherited from v1. The exact cancellation, posterior square-completion identity, and PRS6.9 full-Haar limit are not invalidated by this gap.
