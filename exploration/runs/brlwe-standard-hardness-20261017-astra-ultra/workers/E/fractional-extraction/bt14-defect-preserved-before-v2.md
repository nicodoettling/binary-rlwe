# BT14 defect preserved before pair repair

2026-10-17 resumed E role. Read sealed `criticism/BT14/complete-report-v1.md`, SHA256 `95442ce58d243135992228710d7acdc896d369a93b277ebdbce2b22d24fff306`, its complete preserved counterexample, and coordinator `bt14-history-gap-before-repair.md`. All existing E v1 artifacts remain unchanged.

The unrestricted atomwise reading of `pair-theorem-only-v1.md` (SHA256 `8bce599bcf65ce6dc980b2859e2f89e9b07f0a0f3642f7557359292e2966c0b7`) is REJECTED. The exact defect is its conditional premise only on positive-probability complete-history branches, without restricting those histories to a countable space or specifying an almost-sure regular conditional law.

Counterexample: n=2, R=Z[i], I=H=R, c=1, J=R, gamma=1, W=10, m=2. Retain U uniform on [0,1], put X_1=0, and X_2=1 for U<1/2 and i otherwise. Both stages are attempted. Every complete-history atom containing U has probability zero, making the literal eta_2=0 premise empty. Useful success is one whereas b=9/100. The counterexample already has X_1 in J and does not depend on ambient-space ambiguity. Its source file SHA256 is `4ee6c5fcab8e8cc57d767be2842e87eb8c211a044e17c01cc1be707b0f19edc1`.

The independent-list geometric result and the causal proof under a genuine almost-sure conditional-TV premise survive. They do not confer acceptance on unrestricted sequential v1. Every downstream use of the sequential wording must refer to a freshly checked repaired claim; previous favorable self-checks missed this distinction. No accepted computational foundation followed from v1.

Planned v2 repair: fixed common ambient R^n; nested standard Borel history random variables; attempted-stage indicators measurable before the corresponding draw; regular conditional sample kernels; deterministic eta_j bounds holding almost surely on attempted histories. No history-atom condition. X_1 can have any R^n-valued law. The exact centered normalizer, ideal packing constants and pair-selector event containment will all be reproved, rather than inherited from v1.
