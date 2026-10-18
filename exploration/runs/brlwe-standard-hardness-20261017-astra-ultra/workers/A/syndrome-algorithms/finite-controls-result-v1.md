# A-syn-finite-1 result

Completed 2026-10-17T20:35Z, exit 0; reservation released to coordinator. All assertions passed. The original stdout contains every one of the 64 nearest-plane matrix cases and is preserved without filtering. Stderr is empty. Command, input, code, estimate and /usr/bin/time record are separate immutable v1 artifacts.

The exact collision identities matched: q=5,r=1,D=2,B=1 gave E chi^2=4/9, missing mass 4/25 and rank-failure 1/25; q=3,r=2,D=3,B=1 gave E chi^2=8/27, missing mass 632/6561 and rank-failure 35/243. Missing-mass/Jensen controls passed.

For 64 deterministic-seed full-rank matrices over F_5 with r=2,D=3, every target was tested, totaling 1600. Determinants equaled q^r before/after exact LLL; syndromes and the squared nearest-plane approximation bound 2^D were verified against exhaustive exact CVP over centered residues. In these small controls Babai actually attained every optimum; that observation is not extrapolated to the asymptotic upper bound.

The determinant-only negative control has Lambda=101Z x Z, target (50,0), nearest distance squared 2500 versus det(Lambda)^(2/D)=101. This refutes replacing a covering-radius proof by a determinant-root expression. The conditional designated-response comparator enumerated all 625 pairs of F_5^2 responses and produced all 625 output pairs once. The single-output centered coefficient box [-1,1]^2 had exact uniform mass 9/25.

Resource record: 0.24 seconds wall, 0.23 seconds user, maximum RSS 16,384 KiB, zero swaps, exit 0. Enforced address-space cap 256 MiB and timeout 30 seconds. These finite controls support implementation/algebra checks only; they do not certify the new theorem or provide evidence of source hardness.
