# B elliptical multiplier sampler v2 recheck

2026-10-17. PROVISIONAL nonblind review; no acceptance authority and no experiment. Fresh SHA2569077cb68d8a6f4fd29fa276d1819518980e81b492852a86e35e5410ef9c9cf2b matches the requested exact file. Read the entire v2 and all v1-to-v2 changes.

The new wording correctly states EXPECTED polynomial time and charges all rational numerator/denominator encodings, every requested-precision parameter, and the declared square-root algorithm/cost for nonrational representations. The unbounded uniform-integer rejection in its scalar dependency is consistent with expected time. A bounded-time caller must cap it separately; C-OHCP-v5 does so explicitly.

The analytic law is unchanged and survives recheck. The actual joint density is g_C(h)rho_a(e-h)/rho_a(Z^n-h). Removing its h-dependent denominator and normalizing produces an E marginal proportional to exp(-pi e^T V^-1 e). Its H marginal is g_C reweighted by the theta sum divided by its actual expectation. With a at smoothing this single normalized reweighting costs epsilon/(1-epsilon). Center coupling contributes4pi xi/a+zeta; independent finite scalar kernels contribute n nu. The proof never treats a finite approximation as TV-close to a continuous Gaussian before applying a smooth integer kernel.

For C=V-a^2I>=a^2I, the stated square-root and scalar precision bounds are polynomial in complete input encodings and actual precision. The largest width may be exponential, but its binary length is explicitly charged. Canonical-to-coefficient conversion gives eigenvalues v_i^2/n. The implemented multiplier is always an exact ring integer even when its probability law is approximate, so ideal-point cancellation remains exact.

No further law or runtime defect found within the declared computable-matrix model. Recommend the repaired auxiliary lemma for coordinator consideration; no source hardness or full OHCP acceptance follows by itself. V1's runtime defect remains preserved by its author. This review does not contact or import isolated blind-review findings.
