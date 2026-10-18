# D-LSW-1 reservation and estimate

Root approved one local light job on 2026-10-17: <=30 seconds wall, <=256 MiB, <100000 states. Script enforces RLIMIT_AS 256 MiB and RLIMIT_CPU 25 seconds; outer timeout enforces 30 seconds. One Python worker process; timeout and time are supervising launch wrappers, not extra workers.

Estimated primitive state count <10000: 25 scalar theta terms; 28 probability triples times 27 weight triples =756 reweighting cases; fewer than100 exact small matrix minors/operations treated as state checks. Integer sizes are bounded by the fixed scalar cutoff12 and 3x3 rational matrices. Expected RSS<32 MiB and runtime<1 second. Code is self-contained standard-library Python and deterministic. Full JSON result includes exact scalar tail fractions and all matrix witnesses. No claim is certified by passing this bounded control.
