# FULL1-FV1 preregistration

Frozen before execution. This is independently written reviewer code; no author experiment has been imported or inspected. Deterministic exact rational/integer enumeration; no random seed or stochastic search.

Code: finite_controls_v1.py, SHA256 recorded in finite_controls_v1.code.sha256 before execution. Inputs are literal in this code: original CP-1 five-bit/5-trace model; n=2, q=5 complete CRT laws for 25 secrets and the three-point correlated CRT error law with weights 1,2,3; exact endpoint deviations; all nonzero ternary vectors for n=2,4,8 with fixed prime lists; all 15 partitions of the two-dimensional binary cube; finite rational independent S,G observation law; gap vectors in {-1,0,1}^{6 or 12}; rational coefficient verifier targets on the 1/64 grid in radius 1/8. Dimensions never exceed 8; field primes never exceed 113; arbitrary precision integer arithmetic is used, with maximum norm bit size recorded.

Hypotheses: exact full (A',B') laws equal the appropriate hybrid despite correlated CRT errors; the strict endpoint separation is sufficient and equality at 4a is not; every modular zero costs its own norm factor; the fiber bound keeps one diagonal term; moving the selected-function maximum outside the observation sum can lower success; fixed-list removal costs at most removed mass; exact verification rejects all false candidates; CP-1 reproduces the old product failure. Expected outcome PASS, or a preserved assertion traceback and smallest failing loop state for diagnosis. A PASS certifies only these finite controls, not the analytic theorem or asymptotic hardness.

Resources: one foreground light job reserved by root; timeout 120 seconds with TERM then KILL after 2 seconds, RLIMIT_AS=536870912 bytes, RLIMIT_CPU=115 seconds, no subprocesses inside the mathematical code, no network, no descendants spawned. The wrapper uses a fresh process group and kills the whole group on timeout. stdout, stderr, exit status, elapsed time and maximum resident memory are retained. No install, escalation, detached execution, goal or further model call.

Exact command, from project root:

    python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/reviews/FULL1/run_finite_controls_v1.py

The wrapper code and hash are frozen before the command. It invokes the current Python interpreter on the adjacent finite_controls_v1.py with the declared resource limits and process-group cleanup, writes finite_controls_v1.stdout.json and finite_controls_v1.stderr.txt verbatim, and records finite_controls_v1.receipt.json. No test retry is authorized by this preregistration; any code repair will be versioned and separately documented.
