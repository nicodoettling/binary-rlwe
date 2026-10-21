# B-M1-FALLBACK-1: preserve before clarification

Nonauthor review of M1 theorem-only-v1/proof-v1. This is a specification ambiguity, not a counterexample to existence of the stated sampler.

The theorem says every fallback outputs lattice point zero. The scalar implementation paragraph allows scalar fallback0 followed by continued basis sampling, or global fallbackzero. These choices have different final laws/support records. For J=Z^2 with standard basis, suppose reverse-order sampling chooses z2=1 and then stage1 hits its cap and substitutes scalar z1=0. Continuing returns (0,1), not lattice zero. This branch has positive probability for a finite capped sampler at a finite positive width.

Choosing the expressly allowed global-zero variant on every proposal-cap or exhausted-trial failure fixes the wording without changing the stated error budget. The first-failure coupling charges that branch by the existing cap/exhaustion probability. The exact final algorithm should select that variant. No scalar fallback branch should be silently declared zero if it actually retains previously sampled coefficients.

The main theorem's existence claim survives this observation because its proof already permits global fallbackzero. This record must remain if the specification is tightened.
