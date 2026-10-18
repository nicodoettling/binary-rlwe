# D resumed-assignment checkpoint

2026-10-17T20:47Z. All claims below are PROVISIONAL or REPAIRED-PENDING-RECHECK; D has no acceptance authority. Source hardness and the original binary target remain OPEN. Original absolute discovery/worker stop times remain01:39:14Z/01:59:14Z on October18. No goals, spawns, external sessions, service changes, or writes outside workers/D were performed. Frozen earlier theta bytes were preserved. No policy interruption occurred.

## Completed findings

- Primary LSW exact Theorem1 identity drops a shifted theta normalizer; its scalar counterexample is preserved. This does not refute an appropriately approximate leakage theorem.
- B-LSW v2 repairs both normalizers. Complete joint-law and independence audit found no algebraic defect. Pointwise bound is epsilon/(1−epsilon)+epsilon^4/(1−epsilon^4)+delta_num for the explicit widths, safely bounded by2epsilon/(1−epsilon)+delta_num. Comparator remains exactly uniform independently of the statistical repair.
- The published scalar Condition2 forces broad spherical noise for the dense map and therefore uniformity modulo q at a=n². This sufficient condition is not universally necessary; the exact anisotropic countercontrol demonstrates that distinction.
- F=4a²HH^T is a feasible anisotropic candidate with exact idealized source (R,T,U−f), f~D_sqrt(F_R), and an exact uniform comparator. Its full density and all latent correlations are frozen. The naive independent-integer shared-noise representation is not justified.
- A provisional fiber lemma gives a constructive conditional interface: for integer K with KR=0, ker K=im R, and the requisite ring/CRT surjectivity, Kf is close to a discrete Gaussian on K Z^J with exponent4a²KK^T. A short K would give smaller subgaussian masks; no such efficient construction is supplied.
- A's observation yields a direct quantitative test: a standalone efficient short surjective K already distinguishes ordinary RLWE through Kb'=Ke'. An oracle-assisted K may instead realize the desired reduction, provided queries have the original binary-secret law and selection preserves the relevant error independence. The separate oracle-scope addendum preserves this distinction.
- B-IDEN public-basis and uniform-short-lift bounds check out. Its concrete n-element hidden ideal catalog also admits a nonuniform OR-of-bases attack if the useful short bases exist with polynomial descriptions. This does not exclude exponentially large hidden catalogs or provide a uniform short-basis algorithm.

## Frozen core artifacts

| File | SHA256 |
|---|---|
| LSW-theorem1-normalizer-objection-v1.md | 855284f0719b0d790f3d4b7584f390ac52ca0e61cefd255b0c99a4afd1c65ca1 |
| first-partial-v1.md | 0f8eda3a0978598cf7b39c456dda18eb0a687d2fc59487d985e7ce56bdcc7f59 |
| audit-v2.md | 7cd91e6a9d58a984093a51f6b71b2b8254624efb15fe9c40e77a518536045844 |
| anisotropic-joint-law-v1.md | b66dcc1c86bd6ca31432a5571f6d6d1ca73e368c04eca5794e6274ce9ea5850b |
| homogeneous-short-map-obstruction-v1.md | 10c45b306b1244471507dda621e598f909a180cb7f5a93288376af58e5c255dd |
| homogeneous-oracle-scope-v1.md | e314cf1c16721f28dc9cf9f74620ea3c7acfde2af3b9b70066a067ae8e210e61 |
| ideal-denominator-audit-v1.md | 8d9bca589c21caa99cc19a0443f56cb7256d177b9f93c3dc3f989285c2524f91 |

## Experiment ledger

Only D-LSW-1 ran in this resumed assignment, with explicit root reservation: <=30s wall,<=256MiB,<100000 states. Actual801 states,0.03s wall,11264KiB RSS,exit0,empty stderr. Full code/input/estimate/command/output/resources and rigorous rational scalar tail are in lsw-control-v1*. Reservation was released immediately. Code hash0fbf67d705c6f59365b940a7d24a69349367bb6d531dc9414992c5947badadf5; output hash1e621b9afa7d933776f78207166dc784e53f5824da6ad782755f1a0787c5b46d. No second experiment was requested or run.

## Precise open obligations

Fresh nonauthor review is needed for the repaired joint simulation, the new anisotropic fiber lemma, and each scoped obstruction. A concrete correlated-Gaussian sampler with full precision/bit-complexity accounting is still required for a certified polynomial-time map. The fiber lemma does not construct short homogeneous relations. Oracle-assisted relations require a new valid query-programming argument; merely invoking binary recovery on arbitrary instances is not allowed. Directional downstream completion requires a new cube/lattice guessing bound and cannot be inferred from the rank of the pre-sampling covariance. No computational foundation has been obtained.
