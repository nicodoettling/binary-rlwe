# Exact M1 proof-v2 recheck

Worker B, nonauthor full-proof/source/complexity review, 2026-10-21 06:05:53 UTC live checkpoint. This addendum together with report-v1.md and source-review-v1.md is the complete final nonauthor report. Same-model correlated scrutiny; no ACCEPT issued.

Exact inputs re-read in full and hashed:

- theorem-only-v1.md:320164e4e692ce801f2fde10a3deb7279629b9ff467bf4a155aa0828bba11845;
- proof-v2.md:829d79b9aa0c162ac213605659f780791b14dc311ab145def9cbf4a8b8d95ebc.

The complete v1-v2 textual diff was inspected. Only the documented global-zero fallback selection, uniform-proposal bit-count clarification, resulting termination/bit-growth sentence and version record changed. The mathematical normalizer, HNF, collision-basis, width, example-family and adaptive arguments are unchanged and retain the conclusions of report-v1.md. The repaired scalar procedure now aborts the whole lattice algorithm and outputs zero on every declared cap/exhaustion failure. No formerly sampled coordinate is retained in a fallback output. Proposal attempts use ceil(log2 N) bits; b is the number of allowed attempts, while b bits separately implement the dyadic acceptance probability.

For the repaired global failure event, compare the full execution to the unbounded exact-coordinate process up to the first failure. The exact scalar conditional law can be viewed on an extended alphabet with an abort flag; its discrepancy is bounded by the same tail, exhaustion and numerical/cap terms. Mapping every abort to the lattice point zero cannot increase TV. The claimed sum of conditional scalar errors therefore remains valid; no successful branch is renormalized, and no extra error term is needed. Integer center reduction remains exact arithmetic; a final global-zero failure need not be translation-equivariant, and M1 does not require that stronger kernel property.

Root reserved B-M1-FV1. The targeted exact finite regression ran once under20s wall/18s CPU/256MiB limits, exit0,0.05s measured wall and21,504KiB measured peak RSS. Source SHA25620fbad63fb6fb9859612481d71a3ebdca1e6b3f77ca0be15bad7f0d2744668ed; full output SHA2562d2a0d1269126cf4a098babbb8becbe06e96f1f7030e21e38312058b2e85116f. The source, all2,048 tapes, exact reference/old/repaired laws, cap snapshot, command, output, stderr, exit and resources are retained in repair-control-v1-*.

The finite model chooses stage1 failure from the actual preceding successful stage2 coordinate. Its repaired law has TV55/512 from the reference, bounded by actual failure71/512 and the uniform conditional union bound3/16. It retains the rejected old continuation witness: after stage2 outputs1, stage1 fallback0 gives old final output(0,1), while the repaired branch gives(0,0). An exact lower-triangular negative control with a129-bit entry confirms that diagonal entries alone do not bound Gram–Schmidt lengths in the wrong ordering. The proper upper HNF has squared lengths1,1. The explicit f=1+i, J=Z[i] collision-basis transform has squared Gram–Schmidt lengths2,1/2, both within||f||^2=2. These are finite regression controls, not an implementation or certification of the infinite Gaussian sampler.

Final scoped verdict: B-M1-FALLBACK-1 is resolved in these exact v2 bytes. No remaining load-bearing defect was found by this review. The theorem remains subject to root reconciliation, fresh-blind review, exact artifact checks and the unchanged accuracy/coherence/family scope. The original computational foundation remains OPEN.
