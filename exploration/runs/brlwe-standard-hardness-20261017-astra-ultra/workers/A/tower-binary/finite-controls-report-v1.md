# A-tower-finite-1 result

2026-10-17. Coordinator authorized one job of at most 30 seconds wall time and 256 MiB address space. The reservation was announced before execution and released after output inspection. The job exited zero; /usr/bin/time reports 0.21 seconds wall, 0.20 seconds user, peak resident memory 12,288 KiB. stderr is empty. No experiment remains active.

The exact integer/Fraction controls passed:

- All 83,521 degree-four multipliers over F_17 were tested for A(Y-2)=0: exactly 17 satisfy it. A separate degree-four F_41 grid found only zero among its 81 tested points; it was not a full F_41 exhaustion.
- Each field had 1,296 exact binary-product block comparisons and all 16 binary radix-defect checks. Every enumerated annihilator solution satisfied A Z=A embed(G_2(Z)) for all 16 binary Z.
- gamma=5+12X in F_17[X]/(X^2+1) satisfies gamma^2=X, with CRT values 2 and 8 at X=4 and 13.
- Full affine-cube enumeration at q=3 and q=5, dimension two, and separate full degree-two ring-unit controls agree with the reviewed classification. The characteristic-two negative control fails the classification as expected.
- The honest digit lift for n=2,r=8,q=97 has M=2, 194 distinct integer lifts per coefficient and exact joint binary-law distance 6975/16384. This intentionally finite, non-negligible instance checks the formula; it is not a claimed useful parameter choice.
- Disjoint finite-difference triple counts for all interval residues modulo four at q=17,41,97 satisfy the stated lower count.

Reproduction records: finite-controls-v1.py, finite-input-v1.json, finite-command-v1.txt, unedited finite-stdout-v1.json, finite-stderr-v1.txt, finite-resources-v1.txt, finite-hashes-v1.sha256. All calculations were deterministic and used only the Python 3 standard library. They do not establish an asymptotic theorem, source hardness, or a working binary-recovery reduction.
