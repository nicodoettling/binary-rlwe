# Exact comparator experiment C-E1

Status: completed exact finite regression; no asymptotic certification.

Parent reservation granted before execution: one light job, at most 30 seconds wall and 256 MiB address space. Executed command from repository root:

```sh
timeout 30s python3 -B exploration/runs/brlwe-source-foundations-20261016-astra-ultra/workers/C/exact_m3_control_v1.py > exploration/runs/brlwe-source-foundations-20261016-astra-ultra/workers/C/exact_m3_control_v1.out.json
```

The script installs RLIMIT_AS=256 MiB before allocating tables. Estimated size: 390625 scalar cases enumerated sequentially; 125 scalar output bins; 15625 full-ring triple bins and about 421875 sparse convolution updates. Memory well below the installed cap. Exit code 0; observed wall time 0.25229069 seconds. No detached process. Reservation released immediately after reading the saved output.

All arithmetic relevant to probabilities is integer or Fraction. Decimal values in output are display only. No random seed is needed; enumeration is exhaustive. No truncation tails or numerical precision errors occur. Independent finite ternary coefficient noise is an explicitly labelled surrogate, not the SC-v1 Gaussian.

Checks: exact scalar private-mixture law, tensor CRT reconstruction for n=2 and q=5, exact TV to product uniform, equality to the stated finite closed formula, normalization after each noise convolution, and TV contraction after independent additive noise.

Results: full noiseless ring TV=753424/9765625; scalar zero-event gap=124/3125; full ring TV after adding finite noise to all three multipliers=3336449/625000000. The zero-event theorem lower bound is 4/125. These values discriminate the failed noiseless expansion from a potentially repairable additive expansion; they do not prove the Gaussian repair.
