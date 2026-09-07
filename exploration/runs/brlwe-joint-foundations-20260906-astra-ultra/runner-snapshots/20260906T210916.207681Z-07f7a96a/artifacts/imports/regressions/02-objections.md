# C03 exact objections

## C03-O01 — missing domain guard in frozen NC1 v1 ledger

**Affected version:** `snapshots/review-v1/claims.json`, claim `NC1`, version 1. The associated detailed F02 and D03 statements explicitly include the guard and are not refuted.

**Defect:** positive definiteness of B and Theta alone does not imply delta(Theta)<1. The displayed TV upper bound delta/(1-delta) is negative when delta>1 and undefined when delta=1.

**Exact hand counterexample:** take an integer 1-by-1 zero matrix M, sigma=1, tau=1/3. Then B=1, Theta=1/9 and MG+H_* has exactly law D_1, so its distance from D_sigma is zero. Meanwhile delta(Theta)>=2 exp(-pi/9)>1, since pi/9<ln 2. The alleged unguarded upper bound is negative.

**Proposed replacement:** for integer rectangular M, B=sigma^2 I-tau^2 MM^T>0 and Theta=tau^2 I-tau^4 M^TM/sigma^2>0, define delta(Theta) as in F02. If delta(Theta)<1, independent G~D_tau and H_*~D_B satisfy the stated TV bound; otherwise use the trivial bound 1. For H_seq in output dimension p, its displayed nontrivial eta_seq formula additionally requires kappa(beta)<1, beta=lambda_min(B); otherwise use eta_seq=1. Sum the separate comparison errors and cap the final TV bound at 1 if desired.

**Dependency footprint:** the exact frozen ledger has direct dependents AN v1, CHAR v1 and MN v1; its complete recorded transitive closure additionally includes A0 v2 and M0 v2. CHAR's own mathematical claim is outside C03's audit. The frozen S0 v2 ledger omits the instantiated AN dependency; the separate correction explicitly adds it, so S0's version must also change on reconciliation. NC1's detailed proofs do not change. In A2 and the prescribed-polynomial-m stacked specialization, beta is polynomially large and Theta>=3ell^2 I/4, so both guards hold for sufficiently large n. Their asymptotic applications are unchanged after the versioned correction. This objection supplies no counterexample to those applications and no objection to B0/KM as conditional implications.

**Coordinator response:** accepted as a ledger statement defect; coordinator announced NC1 v2 and downstream dependency propagation. C03's final report remains tied to the frozen v1 statement, and any subsequently checked exact correction will be identified separately.

**Correction recheck, completed:** C03 independently read `corrections/NC1-v2-and-dependencies.md`, SHA-256 `a801c12d79a1d74093cc0a7ab265e2d4580521dafaf823694bc905011f15cad1`. Its piecewise guarded convolution and sequential bounds are valid, including equality/outside-domain branches handled by the trivial bound 1. **ACCEPT NC1 v2 as written in that correction. C03-O01 is closed by this exact correction.** The A2/MN noise and sampler applications are unchanged after version propagation. A later altered correction needs its own identified recheck.
