Hypothesis: the sealed finite positive and Farkas certificates describe the exact declared ring-law systems, including full fixed-secret and comparator endpoints, and the root symmetry extensions only exclude their finite stated models.

Code independent-certificate-check-v1.py is frozen before execution. Inputs: hashed snapshots of FF3 FV10/FV11/FV13/FV16/FV17 certificate JSON, radial H entries, original n4 matrix, root SYM-RANK-FV1/FV2 matrix/orbit/certificate files. New matrix coefficients are reconstructed from negacyclic multiplication using signed-shift powers, exact point probabilities, half-open rank-interval overlaps and integer group aggregation. No optimizer is run; no saved coefficient matrix is trusted without full equality against reconstruction. The 32 legal group permutations are independently built as signed integer matrices and checked for closure and uniform orbit multiplicity. All eight cyclic/reversed rank variants are rebuilt.

Expected result: exact positive checks for 47- and 33-weight n2 tables; exact nonnegative A^Tz and negative b^Tz for the three FV10, FV13, FV17 and two root symmetry certificates; all author/root arrays match independently reconstructed laws. Input probability denominators and certificate integer arithmetic are exact. No Gaussian tails, random seeds or precision approximation occur. Any failure and trace remains preserved.

Requested one HEAVY slot, 120-second wall, 2GiB address space, expected under90seconds/600MiB. Explicit root grant is required before execution. Command from this review directory:

    /usr/bin/time -v timeout --signal=TERM --kill-after=5s 120s prlimit --as=2147483648 -- python3 independent-certificate-check-v1.py

Retain stdout JSONL, stderr/time resource report, command/code hash/start/end/exit/cleanup receipt. No detached process. Finite certificates do not prove asymptotic impossibility or a Gaussian-family transfer.
