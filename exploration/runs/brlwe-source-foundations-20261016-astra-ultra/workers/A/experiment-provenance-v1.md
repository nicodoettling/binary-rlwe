# A finite-control provenance v1

Reservation: coordinator authorized one light experiment, <=30 seconds and <=256 MiB address space. Released after completion at approximately 2026-10-16T21:23Z.

Size estimate before execution: 15,625 noiseless source seeds in the split degree-two ring; 6,561 candidate 2-by-4 scalar matrices, of which 6,240 have full row rank; at most 27 scalar source seeds per map. Counter dictionaries have at most 15,625 entries. Estimated memory below 256 MiB and runtime below 30 seconds.

Exact command (from project root):

```sh
timeout --signal=TERM --kill-after=1s 30s python3 -B exploration/runs/brlwe-source-foundations-20261016-astra-ultra/workers/A/finite_controls_v1.py > exploration/runs/brlwe-source-foundations-20261016-astra-ultra/workers/A/finite_controls_v1.stdout.json 2> exploration/runs/brlwe-source-foundations-20261016-astra-ultra/workers/A/finite_controls_v1.stderr.txt
```

The script sets `RLIMIT_AS` soft and hard to 268435456 bytes before allocating experiment objects. The shell tool returned exit 0 and elapsed 0.144034074 seconds. Stderr is empty. Stdout is preserved verbatim. There is no randomized seed: every loop is deterministic and exhaustive in its stated finite domain. No jobs were detached and no packages or remote computation were used.

Probabilities, ranks and minimum total-variation distance are exact integers/Fractions. Entropy displays and checks use binary64 natural logarithms, without interval certification; the smallest checked finite inequality margin was about 1.0014. The finite errors are explicitly zero or ternary regression laws, not a Gaussian approximation. Hence no truncation/tail claim arises in the experiment. The symbolic general proof, not this finite search, supports the proposed asymptotic statement.

Checks: erasure-mixture identity exactly in F5[X]/(X²+1) and F3 with nonuniform finite noise; expected image rank 48/25; noiseless two-sample source KL exactly `(52/25)ln5` by rank identity; all 6,240 full-rank F3-linear kernels satisfy the proposed inequality in the zero-noise d=0 control, with minimum TV exactly 16/27.
