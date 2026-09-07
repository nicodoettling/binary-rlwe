# E01 — exact finite rich-support collision diagnostic

Coordinator allocation: 2026-09-06 14:35:34 UTC; enforced aggregate timeout 120 seconds and task deadline 14:50 UTC. Completed in under two seconds including compilation and postprocessing. No seed or truncation: all 3^n ternary differences were enumerated for (n,q)=(4,17),(8,17),(16,97), with exact integer weights. The n=16 case contains 43,046,721 differences. Postprocessing used exact rational arithmetic; only displayed square-root upper bounds use floating point. Code, raw counts, full results and execution metadata are in E01-root-collisions.cpp, E01-analyze.py, E01-root-collisions.json, E01-analysis.json and registry.json.

The effective posterior parameters beta=1 and beta=1/2 are deliberate finite-law diagnostics. They are not asserted to equal the Gaussian auxiliary widths of candidate A. In the beta=1 no-leakage control, a separate direct enumeration of all binary-secret quotient images for every support at n=4,8 verified the collision identity and computed actual average joint TV.

| n,q | support dimension d | normalized mean collision (beta=1) | actual average TV, if enumerated |
|---|---:|---:|---:|
| 4,17 | 1 | 17/16 | 1/17 |
| 8,17 | 1 | 4097/4096 | 1/272 |
| 8,17 | 2 | 21097/14336 | 487/2023, approximately .24073 |
| 16,97 | 1 | 134217833/134217728 | upper bound .00044225 |
| 16,97 | 2 | 474712277/402653184 | upper bound .21152 |

Thus individually near-uniform CRT coordinates can coexist with substantial joint deficit in these tiny rings. The d=2,n=8 case already has output entropy slightly larger than eight input bits; its deficit is not an asymptotic counterexample to a properly budgeted extractor. At n=16,q=97,d=2 the output fits the sixteen-bit no-leakage input budget, but the collision bound is still loose. Neither observation establishes asymptotic success or failure. Random supports do not inherit the binomial block bound merely from uniform marginals: for n=8,d=2 the selected binomial normalized collision is 289/256, different from the random-support average 21097/14336. Its source remains attacked regardless of this better finite extraction diagnostic.

Useful remaining question: bound the weighted root-count factorial moment in equation (2) of coordinator-extraction-gate.md at an asymptotic d beyond the enumerable-support regime and at the SAME Gaussian auxiliary width as the completion. No new hardness evidence is claimed by this experiment.
