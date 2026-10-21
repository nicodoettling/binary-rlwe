# DD2 nonauthor review of coordinator DD3-AM-v1

Reviewed 2026-10-21 12:42 UTC. Inputs: coordinator/dd3-averaged-modulus-statement-v1.md, coordinator/dd3-averaged-modulus-proof-v1.md, coordinator/dd3-selected-functional-v1.md, RECENT/workers/B/proof-v1.md, and the exact inherited same-J statement. This is a nonblind review; the coordinator's proposed proof and intended route were visible. Same-model scrutiny is correlated, not formal verification. Verdict: favorable for AM1/AM2 as scoped; the full bridge remains PROVISIONAL pending the explicit downstream interfaces.

AM1 as written is valid. The full norm is nonzero because X^n+1 is irreducible, and its upper bound follows from Parseval and AM-GM. The max/sum order is safe: the diagonal m_c occurs once, while only distinct-pair collisions are summed over all roots. The exact divisor-count bound is deterministic for any common fixed partition and any distinct split-prime list. It does not need a prime equidistribution theorem. I independently derived a stronger coefficient n rather than n² via Smith normal form and froze `am1-strengthened-theorem-v1.md` with its full proof; that strengthening is not automatically accepted through this review.

AM2's extension of the inherited Gaussian envelope is sound: for each y the predictor chooses a pair (j,v), and its exact success numerator sums the Gaussian masses of the corresponding fiber before taking a max. The uniform pointwise Gaussian envelope bounds that entire selected sum by its cardinality times one common envelope. Centered theta maximum and the ratio bound retain the true lattice normalizer. Full Y may reveal more than c, and the proof does not claim posterior uniformity. The selected pair is one output, so no stagewise probability multiplication occurs.

Prime-list supply can be made polynomial in VALUE using auxiliary congruences and effective Linnik; `prime-list-theorem-proof-v1.md` supplies an explicit algorithm and primary-source theorem. Its average-modulus target promise remains an additional hypothesis. No fixed-q result follows from this alone.

Pending/caution items for the integrated version:

1. Choose one common source sample count k and one σ for all q before applying the uniform θ overhead. If k depends on logQmax, solve that parameter dependency explicitly. A polynomial sample count in q's numerical value can make q≥nσ circular or impossible, so the intended regime must specify a uniform k0(n) bound.
2. A list dependent on J by gcd filtering is harmless to AM1, but the D_q average guarantee must concern precisely that final list (or pay the removed fraction from a fixed master-list promise). A one-q promise is insufficient.
3. Every extractor uses only one final selected pair. A list of guesses would cost its list size in the fiber envelope.
4. Reusing a challenge bank after selecting a root requires simultaneous hypothetical-estimator accuracy for all root/guess choices, or a separate fresh bank. Conditioning a reused bank on its selected root and then calling it iid is invalid. Root's statement proposes the valid union-bound approach; exact extraction proof remains pending.
5. At fractional multipliers, D is off-promise; only the unconditional information-theoretic source bound applies. No invocation of its ordinary-RLWE advantage may occur there.
6. The same-J source completion must include the real generated S and all k challenge samples, not merely D's k0 sample count. Gaussian completion's spectral bound depends on this actual stacked size.
7. A positive average source gap does not give an executable choice of q from an unavailable fractional-source sampler. Running every q's bounded decoder with common conservative parameters and verifying all candidates is a plausible repair; its radius and verifier soundness must be charged.
8. Supplied code versus service access remains distinct for any later coherent DGS composition. A classical ideal decoder needs only bounded classical D calls; a quantum sampler needs actual bounded code.

DD2's earlier direct binary-cancellation attempt is a separate, baseline-dominated construction; it does not justify this new route and its failure does not refute AM1/AM2.
