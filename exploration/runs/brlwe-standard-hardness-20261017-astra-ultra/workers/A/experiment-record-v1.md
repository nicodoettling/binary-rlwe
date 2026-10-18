# A-finite-1 experiment reservation and plan

Coordinator granted one light job, <=30 seconds wall and <=256 MiB address space. Deterministic exact enumeration in finite_controls_v1.py; no random seed, all probabilities rational. Expected ~315,000 transcript contributions, <128 MiB, <15 seconds. Original stdout/stderr and resource records will be retained.

The finite probability model uses F_3^4 as an explicitly labelled coordinate-product surrogate, not a cyclotomic Gaussian theorem instance. It checks arbitrary nonuniform correlated ideal points and masks, deterministic/public ideal, full independent error endpoint, leakage cardinality averaging, and failure if fresh-secret independence is removed. A separate actual n=8,q=17 cyclotomic exhaustive binary-image calculation tests the determinant injection threshold for every root subset. CP-1 is reproduced arithmetically. None is a source-hardness test.

Intended command: timeout 30s bash -c 'ulimit -v 262144; exec python3 finite_controls_v1.py', with stdout/stderr redirected inside workers/A. The live original cap is read immediately before launching.

Executed command exactly as above from workers/A, redirecting to finite_controls_v1.stdout.json and finite_controls_v1.stderr.txt. Exit 0, no stderr. Internal runtime 0.5759381520329043 seconds, maximum RSS 31,744 KiB; tool reported a separate 0.50220388-second wall interval. Both are raw measured values and are not reconciled by inventing precision. No random seed. Reservation released to coordinator on completion. Every assertion passed; full output is retained, and the empty stderr is retained as a zero-byte file.
