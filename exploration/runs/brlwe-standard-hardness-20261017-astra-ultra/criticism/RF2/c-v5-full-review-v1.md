# C-OHCP-v5 full nonblind review

2026-10-17. PROVISIONAL adversarial verdict, with no acceptance authority. No experiment was run. Exact theorem SHA256 2e7f13cc08d5173a9b028b9d757e7c038220cdbbfe83380c6e57320ddc52a38b; exact proof SHA256 5d81997477bd1683dfa377b29e510ace3a078073a5c08c3a851a00ec28406a35. Both match freshly computed file hashes. The full v3 statement/proof was read and rederived, then every v3-to-v4 and v4-to-v5 change was checked against the immutable files. No v1/v2 acceptance was inherited.

## Verdict and scope

No remaining mathematical or finite-simulation defect was found in the stated pointwise finite periodic-Gaussian decision-to-BDD theorem, under its declared scalar representation model and imported primary OHCP polynomial-time procedure. Recommend passing this finite gate to the coordinator and a fresh blind reviewer. This is not acceptance of a standard hardness foundation, the same-family quantum BDD-to-DGS consequence, or either A/B composition premise. In particular, no average-over-J advantage has been silently upgraded to pointwise advantage, and no general worst-case ideal family has been embedded into the low-index family.

The exact v3 bounded-runtime claim was incomplete because of unbounded uniform-integer rejection. Its objection is preserved in c-v3-finite-runtime-objection-v1.md. V4 repairs it and caps the incorrect orientation's execution. V5 additionally includes every scalar numerator/denominator encoding and certified-evaluation cost. V1 remains rejected by v1-logscale-countercontrol.md; subsequent corrections do not alter those bytes.

## Full joint laws and primary hypotheses

Fix J, its ordinary public basis, all declared metadata, and the rational BDD input T=lambda+e. Every actual oracle sample uses independent local multiplier and Gaussian coins given the current complete query/history. Since qJ^-1 is R-stable, the exact identity rT=r e modulo qJ^-1 holds for every integral r, including zero and nonunits. The exact benchmark laws have k independent rounded spherical Gaussians versus k uniform points of the same finite quotient, conditional on this same J. No sampler tape, short basis or hidden e is appended to the public benchmark.

For each query the comparison law uses full n-dimensional Gaussian completion. P=(V^-1+M_h^T M_h/w^2)^-1 and C=w^2I+M_h V M_h^T. The density ratio is the ratio of the normalized posterior theta sum rho_P(R-m) and original theta sum rho_V(R). Both lie in[1-epsilon0,1+epsilon0], yielding TV<=epsilon0/(1-epsilon0). The formula remains valid for singular and zero M_h. It is not an exact discrete Gaussian convolution claim and does not identify a width square with a discrete covariance.

The known shift gives z*=2+e_j/d0 with norm in[1,3]. The selected pair is radial while all nuisance widths stay fixed. At the initial guess, Gaussian KL gives a loss below delta/16 from the same spherical benchmark for every pair. Thus one GLOBAL sign is valid for all coordinates. The starting logarithmic shift lies in[0,log3], so the corrected actual starting-scale decay follows from the decreasing profile bound. Zero and arbitrarily tiny error coordinates cause no normalization failure.

The full-Haar conclusion uses the algebraic norm of each nonzero ideal-dual vector and the entire theta series, not merely pointwise decay of one character. The independent packing derivation in independent-smoothing-control-v1.md recovers the stated exp(-n c^2) error for n>=2,c>=1. Canonical and coefficient widths differ by sqrt(n), as recorded explicitly.

Independent retrieval of the primary PRS Definition4.3 and Proposition4.4 confirmed the local radial neighborhood and the three global profile requirements; see the source ledger in c-v3-finite-runtime-objection-v1.md. The residual8d0 guard contains both the center neighborhood and the origin-centered Lipschitz ball. The proof-only comparison oracle is continuous inside this guard and equals the actual discrete-multiplier oracle outside. Thus the conditional TV bound holds at EVERY query, without assuming that the primary algorithm stays inside an unproved region. The unknown e is used only to define the analysis object, never by the implementation.

## Parameters, calls and conditional precision

Parameter choice is acyclic. First choose kappa from S,delta,k and the rational reconstruction inequality; h0=v0*d0 is fixed independently of v0. Then set Q_*=n ceil(T_H), epsilon0=min(1/16,zeta/(64kQ_*)), a, v0 and d0. Enlarging v0 preserves h0 and all profile bounds. The confidence increase to kappa+log4 only weakens verified OHCP promises and gives spare output precision. T_H is a fixed valid polynomial from the primary algorithm, not an ideal-dependent advice string or an invented numerical exponent.

Two orientations times n/2 complex pairs give Q_* calls and kQ_* samples. The wrong orientation is explicitly capped in time, logscale and query-description length as well as calls; it is not assumed to satisfy the excursion promise. At most two complete candidate vectors are assembled, with no exponential combination of coordinatewise signs.

The global sample counter j runs across both orientations and every coordinate. The conditional numerical budget is tau_j=zeta/[16(j+1)^2]. The exact multiplier comparison costs its own epsilon0/(1-epsilon0), in addition to the posterior cost. The total fixed analytic loss is at most2kQ_*epsilon0/(1-epsilon0)<zeta/16. This latter strict inequality follows from epsilon0<=1/16 and epsilon0<=zeta/(64kQ_*), giving at most zeta/30.

For each sample, multiplier center approximation, Gaussian tails and scalar finite sampling cost3tau_j/16. The bounded uniform-integer subroutine has at most nL_j proposals, each capped at R_j=ceil(log2(16nL_j/tau_j)) attempts. Its extra failure probability is at most tau_j/16. Mean translation costs tau_j/32; Gaussian grid truncation costs tau_j/16; finite CDF decisions cost tau_j/32. Their sum is3tau_j/8<tau_j. Summing conditional errors is valid under arbitrary transcript adaptivity; multiplying marginal success estimates is not. No experiment or approximate numerical plot substitutes for these bounds.

The finite grid sampler couples to the EXACT rounded Gaussian categorical law. It never claims TV closeness between a finite and an unrounded continuous distribution. Polynomial-bit mean precision depends on the actual sampled multiplier and actual query logscale, with the stated negacyclic convolution bound. Scalar rejections are bounded, inverse-CDF and matrix approximations have explicit tolerances, and runtime includes every input encoding length and evaluation cost. This addresses the scalar-encoding issue separately raised for B's first bridge version; it does not accept B's unrepaired version.

## Exact recovery and remaining dependencies

For the correct orientation, the conditional ideal success is at least1-(n/2)exp(-kappa). Finite transcript distance lowers this by at most zeta. The inverse canonical transform and coefficient-grid rounding recover lambda exactly in(q/D)Z^n. Membership in L is checked exactly. Strict separation gives every other candidate residual greater than3d0, while the true residual is at most d0; certified intervals of widthd0/8 and acceptance threshold2d0 separate them.

This theorem only assumes its exact finite periodic decision advantage. It does not itself prove that B's implemented bridge, A's fractional guessing theorem, or a restricted SuperSVP premise supplies that advantage. B's revised full encoding/conditional-Gen statement needs separate review. The same-J quantum DGS interpretation also remains a separately imported consequence. The missing standard worst-case-family edge remains OPEN.

## Regressions

c-v5-regression-addendum-v1.json and .md provide claim-specific dispositions of all51 imported regressions plus13 current controls. JSON preserves each complete exact imported entry, pointer, canonical entry hash and registry provenance. CP1 is addressed by conditioning on the complete history before every sample bound, by same-J pointwise scope, and by declining to import any old sequential-product or binary-guessing claim. Fresh S/errors and proof-only G/H in A remain independently reviewed premises, not silently re-proved by C.
