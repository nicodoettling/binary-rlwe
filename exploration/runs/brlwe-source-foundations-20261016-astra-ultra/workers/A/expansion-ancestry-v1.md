# Targeted ancestry check for coordinator EX-v1

**PROVISIONAL source comparison, not full proof/parameter acceptance.** Inputs read: coordinator/expansion-theorem-only-v1.md and expansion-proof-v1.md, frozen SC-v1 and September baseline, and primary locations/access records in source-access-v1.md. This note is separate from worker A's authored entropy obstruction.

The close precedent is LPR2013 normal-form regularity. Therefore EX-v1 should not claim that adding fresh noise to short ring combinations, avoiding common-divisor failures, or statistically obtaining near-uniform outputs from a fixed random seed is itself new. The relevant proposed addition is using such expansion on the *two-point hidden-ideal source*, retaining the common annihilator while permitting dependent planted masks, then applying full stacked lossiness to exact sampled-secret recovery with independent coefficient-Gaussian target errors.

The normal-form theorem is not literally EX-v1: EX uses two coefficient boxes plus a coefficient Gaussian, whereas the imported theorem uses a joint spherical Gaussian on ring coordinates. EX's explicit Fourier split and its finite constants still require direct checking. The source-hardness assumption stays separate; neither regularity nor smoothing proves it.

## Quantitative alternative suggested by the primary statement

This is a new parameter substitution proposed for investigation, **not an approved repair or a replacement of EX-v1**. Let the primary theorem's matrix dimensions be k=1,l=3, with row `(1,A1,A2)`. Its canonical Gaussian condition reads

    r > 2n q^(1/3+2/(3n)).

For the power-of-two coefficient basis, canonical norm squared is n times coefficient norm squared, so choosing all three local polynomials with iid coefficient Gaussian parameter t corresponds to r=sqrt(n)t. The sufficient condition becomes

    t > 2sqrt(n) q^(1/3+2/(3n)).

For each fixed polynomial bound q<=n^C, `q^(2/(3n))=exp(O(log n/n))`, so e.g. `t=ceil(n q^(1/3))` eventually meets the strict condition. The coefficients of both local multipliers would now be Gaussian and unbounded; their tails and the planted mask bound must be recomputed. This could improve the q exponent in noise from 1/2 to1/3 while using the same two source points. With l=2 and row `(1,A1)`, one random source point suffices at exponent1/2. These are alternate constructions; adopting either requires a new frozen theorem and fresh review.

## Current scientific boundary

The September baseline supplies arbitrary bounded/dependent ideal points in its abstract lossiness statement, but the instantiated theorem uses only one or two source multipliers. EX's source-budget-preserving expansion would be a substantive new composition relative to that recorded baseline if its own gates close. I have not verified a primary paper already explicitly composing HLBDD with this regularity map to obtain the exact binary coefficient target at polynomial integer modulus. The targeted checks do not justify an absolute literature-priority claim.

Order-LWE's existing polynomial-sample route adds an ordinary-RLWE assumption and swallowing; its §7 theorem uses a CRT-wise secret hypothesis. Those differences are material to the proposed exact Gaussian binary target and Base2-only premise.
