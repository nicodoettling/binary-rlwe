# DD1-FV1 preregistration

Registered before execution, 2026-10-21. Parent global slot coordination required before launch. No random solver or remote service.

Purpose: falsify elementary finite identities supporting WITNESS-v1 and the proposed centering/noise controls. These tests do not establish asymptotic Gaussian estimates or hardness.

Code: workers/DD1/finite_controls_v1.py. Inputs fixed in code: n=2, q in {5,13}; symmetric scalar law on {-1,0,1} with exact probabilities {1/4,1/2,1/4}; binary S uniform {0,1}². Enumerate n=2 one-sample negacyclic ring distributions. Confirm uniform-A W gap equals exactly 1/4 times the S=0 noise-only gap. Confirm fractional/narrow-A and uniform-A comparators retain the same A distribution. Confirm pointwise A-only centering does not change Delta. Confirm adding a global uniform response mask with probability 1/3 multiplies Delta by exactly 2/3. Confirm one shared secret across two noiseless A=1 samples gives equal responses with probability 1, versus probability 1/4 with independently resampled secrets. Confirm finite tube-cardinality upper bound for selected n=2,k=2 code matrices at q=5,13. Deterministic enumeration, no seed or randomized sampling; seed='none'.

Dimensions: response dimension at most 4; residue modulus at most13; integer inputs at most two decimal digits, rational probability denominators and accumulated numerators below512 bits. Expected runtime below10s and RSS below128MiB. Hard limits120s wall, RLIMIT_AS512MiB, one process, no descendants intended. Full stdout/stderr, exit and /usr/bin/time -v retained under workers/DD1. Timeout --kill-after=5s kills the process group if needed; no background/detached execution.

Expected results: all exact identities pass, known shared/independent-secret substitution fails as asserted, tube bounds hold. Any mismatch blocks dependent claims and is retained.

Command (from project root):

    timeout --signal=TERM --kill-after=5s 120s /usr/bin/time -v python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD1/finite_controls_v1.py

The script installs RLIMIT_AS before enumeration. Shell redirection stores complete stdout/stderr; exit receipt is recorded separately by the orchestrating exec call.
