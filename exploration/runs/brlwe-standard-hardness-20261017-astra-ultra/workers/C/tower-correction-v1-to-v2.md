# Preserved C-FAM tower correction

The initial ideal-family-randomization-test-v1.md used S=R_q[Y]/(Y²+1) as an illustrative quadratic extension and derived graph stability iff h²=-1. That calculation was algebraically correct for that algebra but did not identify the next power-of-two cyclotomic ring: R already contains a square root of -1 when n>=2, so this is not the intended field tower.

The counterexample to the intended identification is explicit: in R=Q[X]/(X^n+1), the element i=X^(n/2) satisfies i²=-1, so Y²+1=(Y-i)(Y+i) over R. Thus the v1 illustrative algebra is reducible over the base field.

Version2 replaces that paragraph with the actual tower S=R_q[Y]/(Y²-X)≅F_q[Y]/(Y^(2n)+1). Multiplication by Y sends (f,g) to (Xg,f), so the graph f=hg is stable iff h²=X. No review of v1 transfers automatically to v2. Both versions remain PROVISIONAL; no external review had accepted either. All other paragraphs are unchanged.

v1 SHA2565604a10b42b6b8b15f30bd29909ef445b1f41d270b3cb1c87845cd0e0adcdd64
v2 SHA25692388b38b3dd4dae5ba3805a07047a6961f3edecc89fc9017152376dfbe61716
