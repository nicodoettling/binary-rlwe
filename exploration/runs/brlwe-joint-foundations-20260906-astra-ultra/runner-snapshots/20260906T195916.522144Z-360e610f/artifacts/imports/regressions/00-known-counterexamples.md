# Imported counterexample and failure registry R0

Read before proposing variants. Primary provenance is the read-only prior run `/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-explore-20260906-astra-ultra/`. Full reports are authoritative over these summaries.

| ID | Exact failure or boundary | Provenance / required scope |
|---|---|---|
| R01 | Binomial ideal masks have blocks scalar times known geometric vectors. Enumerating a and a scalar in F_q costs polynomial time; false positive <= L q (|E|/q)^L, for coefficient-small E. | candidates/C01.md; candidates/C01/calculations.md. Retire that sampler, not arbitrary rich supports. |
| R02 | Coins C=G, H=E-FG make conditional independence vacuous for arbitrarily large F. | criticism/C01/additive-obstruction.md. Require conditional G law to survive and distinguish public from latent correctness. |
| R03 | A1=A2 uniform has exactly uniform marginals and distinguishable pair. | criticism/C02/checks-and-regressions.md J1. Joint pair assumption mandatory. |
| R04 | E1=Z, E2=(-1)^(S xor T)Z, S,T fair, Z Gaussian: all conditional error marginals Gaussian, but p_guess(S|E1,E2,T)=1-W(0)/2 versus 1/2 without T. | Same, C2. Product Gaussian target cannot be inferred from marginals. |
| R05 | S,T fair, E=S xor T, A=0: pairwise independence does not give full conditional kernel. | Same, C1. |
| R06 | q=3 half-dimensional quotient family omits one of nine outputs per four bits; TV tends to one despite entropy budget. | scouts/S04.md and experiment_e02.json. Outside reference growing-q regime; entropy alone insufficient. |
| R07 | Field kernel dimension can coexist with no nonzero ternary kernel vector; Boolean lossiness requires actual fibers. | scouts/S05.md. |
| R08 | A secret-dependent precursor can nearly reveal S while the public degraded transcript retains substantial entropy (fixed A=1 control). | criticism/C02/checks-and-regressions.md; E04. Precursor recovery is not public attack. |
| R09 | Strict injection thresholds cannot include equality: n=2,f=1+X has colliding binary 0 and 1+X. Lucas quotient occupancy is index minus one at n=4,8,16, missing (2,1), not full. | Same I1 and E05. No all-degree occupancy claim. |
| R10 | No-wrap alone can give uniform acceptance 1 when residual box spans all centered residues. Known denominator or short numerator tests still attack enumerably structured families. | Same D1; scouts/S12.md. |
| R11 | Half A=0, half A=I noiseless model is sometimes lossy but average recovery ~1/2. | Same H1. Mild/sometimes hardness cannot become negligible average success silently. |
| R12 | At n=1,q=3,a1=a2=1,t=1, binary (1,0),(0,1) are both verified preimages; verification does not identify original planted witness. | candidates/C03/transport.md. |
| R13 | Renyi event transfer Q(F)>=P(F)^2/M2(P||Q) requires this orientation; it does not transfer signed decision advantage. | candidates/C03/transport.md; criticism/C03/mathematical-checks.md. |
| R14 | Uniform ideal U has bad active-unit probability 1-(1-1/q)^d, nonnegligible for polynomial q; conditioning changes the exact source. | candidates/C01.md. |
| R15 | Repeated added noise, rotations, independent secrets, or common V_i=U_i K do not supply independent samples sharing S. | BRIDGE_CONTRACT; prior reconciliation; C03 transport. |
| R16 | Statistical planted-to-uniform claim fails by existential binary-residual-box test; posterior transport may need hard sampling; tower packing requires unavailable correlated responses. | rejected-or-deferred.md; scouts/S01–S03. Computational and statistical assertions distinct. |
| R17 | Independent-matrix moments fail at three-point ring-commutativity terms; public exact symmetries have tiny orbits; QCSD F2 masking loses planted recoverability and odd-q carries; sparse Fourier support gives no general quantum speedup. | rejected-or-deferred.md; scouts/S07–S11. Do not revive these mechanisms by renaming. |
| R18 | CP-1 cached-prefix regression has event probability .0105 > .01 despite residual per-stage marginal bounds. | mathematical-proof-audit probability-regressions.md. Applicable if multiplying selected-stage probabilities; not a blanket objection to fixed independent coefficient products. |

Imported primary-source mismatch controls: Order-LWE Section 7 uses a full CRT-support family, separate HLBDD and ordinary RLWE assumptions, noise-swallowing separations and superpolynomial-q invertibility. The supplied ring leftover-hash work already counts collisions by ideals. Cyclic/negacyclic knapsack theorems differ in task, block count and width from the exact two-binary-block planted problem. Recheck every load-bearing import.
