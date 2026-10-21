# DD1-EXTRACT-FV1 preregistration

Registered before execution. Scope: exhaustive full-joint-law falsification of EXTRACT-v1 at n=2,q=5,k0=1, roots2,3, all four binary secrets, both selected root positions, every candidate t in F5. Error coefficients independently have integer weights1,2,1 at -1,0,1. Enumerate ALL A in F5², p in F5 and independent prefix masks; compare exact normalized masses of (A',B') to direct hybrid j-1 for correct t and hybrid j for wrong t. This retains coefficient-noise correlation after CRT transformation. A second exhaustive rational check tests calibrated-endpoint classification with calibration/test errors at {-a,0,a}, epsilon1/2,n2 and endpoint probabilities on an eighth-grid, including threshold-adjacent cases. Include expected boundary failure at gap=4a with equal-distance ties, which the theorem excludes strictly.

Code extraction_finite_v1.py. Deterministic enumeration, no seeds. Largest dimension4, q5; integral counters and rational probabilities fit256-bit encodings. Expected <10sec, <128MiB. Limits120sec wall,512MiB RLIMIT_AS, one process, no descendants. Code/hash/input/full stdout/stderr+time/exit receipt retained under workers/DD1. Parent global lightweight slot coordination required.

Command:

    timeout --signal=TERM --kill-after=5s 120s /usr/bin/time -v python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD1/extraction_finite_v1.py

Expected:40 full-law comparisons PASS; all classification cases that pass the theorem threshold have exactly correct classification; gap4a boundary tie retained as excluded. This proves only finite identities and arithmetic, not concentration or the infinite theorem.
