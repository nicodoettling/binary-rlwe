# FC1 exact controls: preregistration

This is a bounded review control for frozen sparse-acquisition v1 and compact-selector/energy-rank v2, not a discovery search. No job has run at the time this file is written. Parent LIGHT slot required before execution.

Hypotheses: (1) For n=4,8,16,32, multiplication by X^2-X-1 has determinant magnitude L_(n/2)^2, and the lcm of inverse-matrix entry denominators is L_(n/2); the independent quadratic-ring identity also holds. (2) Fixed-support enumeration using a unimodularly changed ordinary basis finds a <=3-sparse {-1,0,1} member and exact multiplication-rounding recovers two explicit targets for n=4,8. (3) Rank transport is exactly uniform for all 1<=M,N<=16; energy-shell DP matches full enumeration at n=2,3,4. (4) Frozen FV11 weight certificate satisfies all 81 row normalizers, 64 fixed-secret and 16 comparator endpoint equations, with four individually valid H kernels, using independently written full-state Fraction evaluation. (5) CP-1 still rejects the old product conclusion.

Code: control-v1.py. Inputs: workers/FF3/experiments/radial-ring-H-vertices.json and public-geometry-public_norm_local_edge_weights-witness.json; exact hashes are recorded before execution. All other inputs are literal integers/rationals in the code. No randomness, seeds, floating LP, optimization or tail truncation; Fraction arithmetic is exact. One log2 check is used only to compare a finite integral bit-length upper bound; it is not a probability or endpoint calculation. Expected outcome: all assertions pass. Any error/output is preserved; no silent rerun.

Estimated runtime <20 seconds; address-space cap 512 MiB, one CPU thread, enforced wall 120 seconds. No heavy job. Exact command, from project cwd:

    /usr/bin/timeout --signal=TERM --kill-after=5 120 /usr/bin/time -v -o exploration/runs/brlwe-fixed-family-20261021-astra-ultra/reviews/FRONTIER-CHALLENGE1/control-v1.time.txt python3 exploration/runs/brlwe-fixed-family-20261021-astra-ultra/reviews/FRONTIER-CHALLENGE1/control-v1.py

The launcher sets RLIMIT_AS=536870912 and records stdout, stderr, wall times, exit status, command and peak-RSS evidence in this review directory. No writes to source experiments. A PASS certifies only these finite checks, not an asymptotic FF theorem.
