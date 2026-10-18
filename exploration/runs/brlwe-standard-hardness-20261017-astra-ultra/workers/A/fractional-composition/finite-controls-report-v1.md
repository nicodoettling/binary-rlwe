# A-frac-finite-1 report

2026-10-17. Reservation authorized by coordinator before execution, then released after complete output inspection. Limits were 30 seconds wall and 256 MiB address space. The single job exited zero in 0.50 seconds, peak RSS 12,288 KiB. stderr is empty; no experiment remains active.

The ring was Z[X]/(X²+1), J=(1+X), the coefficient parity lattice of index two. Its displayed basis has squared operator norm two. The fixed fractional multiplier was a=(1+X)/2. For every tested g in J, M_a g was integral. All 1,225 rational square-completion checks passed exactly with Gaussian weights

    G: (100/101)^(28||g||²),
    H: (100/101)^(8||h||²),
    target: (100/101)^(7||e||²).

These are actual discrete Gaussian weights, with t²=pi/(28log(101/100)), sigma²=4t² and C=(7/2)t² I. Their posterior exponent is exactly 32. The completion therefore tests a genuine nonintegral multiplication map whose image of J is integral, rather than silently switching to integral multipliers.

The convolution used 313 latent points and 2,401 output cells. Every initial weight interval was checked against its exact rational value. Finite sums used IEEE754 operations padded outward by nextafter, and omitted one-dimensional tails were bounded by the rational geometric expression

    2 b^(a(R+1)²)/(1-b^(a(2R+3))).

The latent truncation error is at most 8.483e-21. The output gives a convolution TV interval close to [1.5117154e-7,1.5117179e-7]. For a conservative reported enclosure, additionally allowing 1e-12 for the final few scalar combinations and displayed decimal conversion, use

    1.51170e-7 < TV < 1.51174e-7.

This lies below the certified conservative theorem-error upper bound 9.870438e-6. The extra final padding is intentional: the inner interval calculations are directed, but a single nextafter around a compound final scalar expression is not used as a general multi-operation rounding theorem. The 1e-12 allowance dominates the worst-case rounding of those few bounded scalar operations; the displayed enclosing endpoints are farther than that allowance from the computed interval.

The same calculation checked actual binary guessing for G~D_(J,t): its probability lies within [0.710575492250,0.710575492254]. The index-corrected bound is about 0.842140770680. Omitting D gives about 0.421070385340, strictly FALSE here. The actual theta-normalizer ratio is about 1.999999837539, bounded by D=2. A separate nonideal lattice 2Z times Z gives guessing about 0.648899364571 and again violates the bound without D while satisfying the index-corrected bound. That control checks the general finite-index guessing lemma; it is not presented as an ideal source.

Artifacts: finite-controls-v1.py, finite-input-v1.json, finite-command-v1.txt, original finite-stdout-v1.json, finite-stderr-v1.txt, finite-resources-v1.txt, finite-hashes-v1.sha256. All work was deterministic. This finite control does not certify the asymptotic theorem, the source tail for every J, B's public bridge, a hardness premise, or the standard-foundations edge.
