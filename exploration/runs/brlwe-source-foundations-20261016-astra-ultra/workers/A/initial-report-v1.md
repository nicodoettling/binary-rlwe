# Track A initial research report v1

Status: **PROVISIONAL**. No computational hardness connection to standard RLWE has been established. This report preserves two exact failed maps, a new scoped source-budget obstruction, primary source checks, and a targeted ancestry check for the coordinator's separate EX-v1 construction.

| Claim ID | Current statement/status | Evidence and dependencies |
|---|---|---|
| A-H1-failed | REJECTED: erasing ordinary RLWE multipliers produces fixed-d Base2 | experiment-directions-v1.md; exact finite countercheck |
| A-ERASURE-v1 | PROVISIONAL: erasure gives `sum_t binom(n,t)(q-1)^t/q^n Base2_t`; distance to uniform <=n/q | Direct multiplication-image calculation; finite exact mixture |
| A-H2-failed | REJECTED: projecting responses into a locally chosen d-ideal preserves uniform comparator | Comparator is exactly Base2_d; planted output within d/q of it |
| A-PROJECTION-v1 | PROVISIONAL: both endpoints collapse as calculated | experiment-directions-v1.md; no Gaussian marginal shortcut |
| A-H3-v1 | PROVISIONAL: k ordinary RLWE samples cannot simulate m sparse Base_m points with TV below `(m-k+1)/m-o(1)` when k<=m through an exactly uniform-preserving randomized channel | entropy-budget-theorem-only-v1.md and entropy-budget-proof-v1.md; full nonauthor/blind review open |
| A-SOURCE-v1 | PROVISIONAL scoped verification: Order-LWE §7 motivates Base2 but does not establish its small-noise polynomial-q hardness | source-access-v1.md; primary indexed statements plus allowed historical extracts |
| A-ANCESTRY-v1 | PROVISIONAL comparison: normal-form ring regularity is a close existing ingredient of EX | expansion-ancestry-v1.md; LPR2013 Thm7.4/Cor7.5 |

The source-budget obstruction is useful but narrow: it requires EXACT comparator preservation and statistical planted simulation. It does not eliminate reductions using three or more ordinary RLWE samples to Base2, computational-only simulation, or general standard-assumption connections. Its finite form uses `g=(m-k+1-q^-k)n lnq-ln binom(n,d)-md lnq-mH_F` and `h2(epsilon)+epsilon mn lnq>=g`. Zero multipliers are retained in the exact rank expectation. No source resampling or latent witness is available to its algorithms.

The only experiment used an authorized light reservation, a 30-second timeout and a 256-MiB address-space limit. It completed in 0.144 seconds. Exact probabilities/ranks/TV passed; logarithmic displays use binary64 and are explicitly qualified. Code, original stdout/stderr and exact command are preserved in finite_controls_v1.py, finite_controls_v1.stdout.json, finite_controls_v1.stderr.txt and experiment-provenance-v1.md. Finite laws are regression controls, not asymptotic hardness evidence.

All writes stayed under workers/A. No agents, goals, detached computation, external sessions, service changes, packages or commits were used. No content-policy interruption occurred. Direct primary-PDF access failures were recorded rather than represented as successful downloads.

Next work authorized by coordinator: formal nonauthor source/parameter/complexity review of immutable EX inputs, once supplied. The initial A-authored obstruction remains separate and cannot be self-certified through that review.
