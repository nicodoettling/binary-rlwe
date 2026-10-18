# A-syn-finite-1 pre-run estimate

Parent reservation granted 2026-10-17, one light local exact-rational job, maximum 30 seconds wall and 256 MiB address space; no concurrent A computation. Expected less than 10 seconds and 64 MiB. Code uses Python standard library only. Matrix collision domains have 25 and 729 matrices respectively (q^(rD)); each box has at most 27 vectors. Nearest-plane controls use 64 full-rank 2-by-3 matrices, all 25 targets, and 125 centered residue vectors per matrix for exact CVP. Output includes every nearest-plane matrix and the exact rational summary. The computation is finite validation, never evidence of source hardness or an asymptotic proof.

Run finite-controls-command-v1.sh from this directory. It imposes ulimit -v 262144 and timeout 30s, preserves full stdout/stderr, and records /usr/bin/time -v resource counters. Input is finite-controls-input-v1.json; no hidden input or nondeterministic seed.
