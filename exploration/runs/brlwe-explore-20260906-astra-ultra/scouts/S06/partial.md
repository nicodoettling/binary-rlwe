# S06: occupied Boolean cosets and real transcript leakage

Started 2026-09-06 09:59:31 UTC. Finite scout; deadline 10:29 UTC. No experiments or CPU allocation requested.

## Distribution ledger

Reference: growing power-of-two ring degree n; rank one; odd polynomial q; coefficient basis 1,X,...,X^(n-1); S uniform on {0,1}^n; m polynomial ring samples, independently sampled coefficient discrete Gaussian errors with width sigma as in target.md. Rotations are deterministic and correlated. Toy lattice observations below explicitly depart from the actual transcript and carry no hardness assertion.

## Baseline/source reading

- Read run target.md and context/barriers.md and literature/reading-notes-2026-09-05.md.
- Primary local text 2020-1185.txt: directly read Section 1.2, Definition 2.3, Sections 2.1/2.3/3, Theorems 5.7–5.8 and 6.9, and Section 6 construction. Verified the proof passes from a modular transcript through a noisy-secret precursor to a lattice-convolution augmentation, and pays log |Z^n/L| at the augmentation step. This is not a proof that the public modular transcript reveals the integer lattice coset.
- Source URL: https://eprint.iacr.org/2020/1185 . Local supplied primary text is available; no access failures so far.
- Procedural note: opened sources/index.md expecting a file map, but it contains coordinator source-check summaries. Do not use those summaries as discovery evidence; all load-bearing source claims are verified independently in the primary text. No other scout output or coordinator-checks directory opened.

## Initial deductions to write completely

1. Exact lattice-coset toy: p_guess(S | S mod L) = N_occ / 2^n. Count occupied Boolean cosets, not determinant; injection iff L intersects {-1,0,1}^n only at zero.
2. Public sampler diagnostic: if A=f(T), (S,E) are jointly independent of T, and E has a fixed law independent of S, then S is conditionally independent of T given (A,Y=AS+E mod q). Revealing sampler randomness cannot change information-theoretic guessing. A precursor involving S can strictly increase guessing.
3. Actual transcript likelihood must use product of wrapped coefficient Gaussian probabilities, including every independent ring sample exactly once.

Status: complete. Final 588-word report is ../S06.md; full small calculations are calculations.md and source/normalization/access qualifications are sources.md. No experiments were run. Discovery ended early once the two bounded mechanisms and source comparison were complete. The imported inverse-lemma probability transfer is explicitly unresolved; the deterministic cube-injectivity certificate and separately normalized original small-ball bound are recorded without treating the discrepancy as an audit.
