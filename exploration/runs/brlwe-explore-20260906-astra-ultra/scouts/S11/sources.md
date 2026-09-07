# S11 primary-source notes

## Outside mechanism sources accessed before barrier release

1. A. Yu. Kitaev, *Quantum measurements and the Abelian Stabilizer Problem*, arXiv:quant-ph/9511026 (1995), https://arxiv.org/pdf/quant-ph/9511026 . Access succeeded through built-in web at approximately 09:48 UTC on 2026-09-06. Section 1, printed pp. 3–4, explicitly specifies a group-action subroutine callable by a quantum computer. Section 4, printed pp. 18–19, defines the dual character group, Fourier eigenvectors in equation (21), and sampling of characters from the stabilizer quotient. Section 5 supplies efficient quantum Fourier transform machinery. [source-verified result] This supplies the actual outside mechanism and demonstrates why the interface must include the appropriate coherent action. It does not analyze RLWE or the sparse transcript encoding below.

2. Lov Grover and Terry Rudolph, *Creating superpositions that correspond to efficiently integrable probability distributions*, arXiv:quant-ph/0208112 (2002), https://arxiv.org/pdf/quant-ph/0208112 . Access succeeded through built-in web at approximately 09:48 UTC on 2026-09-06. Pages 1–2, equations (2)–(6), construct an amplitude state by recursive conditional masses, controlled rotations, and uncomputation. [source-verified result] The application to a known finite empirical distribution is a deduction here: prefix counts over m explicitly listed 2n log(q)-bit records are computable in polynomial time, so the recursive scheme prepares the state to inverse-polynomial or smaller requested accuracy using polynomial overhead. This is not an assertion that the authors analyze binary RLWE.

Search discovery also returned unrelated later state-preparation and hidden-subgroup papers; none are relied on. No access failures for the two used primary sources. Search-result snippets are not treated as proof locations.

## Separation of source claims and deductions

- The coherent group-action interface, dual-character sampling, and conditional-mass state preparation are source-verified.
- The RLWE translation M_s^T=M_{s^dagger}, the exact error-bucket projection identity, the K/q^n bound, wrapped-noise expectation, and public-ratio counterexample are calculations in development.md, not attributed to the sources.
- No quantum lower bound, reduction, conjectured cryptographic hardness, or numerical experiment is supplied.

## Post-release comparison, after 09:56:30 UTC

Baseline packet first opened at 09:56:33 UTC. Read target.md and the indexed literature review before finalizing. No other scout notes were read.

3. Alex B. Grilo, Iordanis Kerenidis, Timo Zijlstra, *Learning with Errors is easy with quantum samples*, arXiv:1702.08255v2 (2018), https://arxiv.org/pdf/1702.08255 . Access succeeded through built-in web at approximately 09:57 UTC, after the release. Sections II–III, printed p. 2, define quantum samples with a coherent superposition over q^n inputs and discuss the error randomness. Section III.B, printed p. 3, explicitly separates the classical public-key model from the coherent sample model and discusses subset-superposition/index-erasure obstacles. Section IV.B, Theorem IV.1, printed pp. 4–5, allows a random support V and gives a success guarantee |V|/(20 k q^n) for bounded scalar noise. [source-verified result] This is a close pre-existing scalar-LWE instance of the imported mechanism, so the final note makes no novelty claim. It does not itself state the ring-valued error-bucket identity or the explicit-list rejection calculation supplied here.

4. Zvika Brakerski and Nico Döttling, *Lossiness and Entropic Hardness for Ring-LWE*, ePrint 2020/1185, https://eprint.iacr.org/2020/1185 . Primary text accessed locally from R/sources/2020-1185.txt at approximately 09:57 UTC. Introduction around Theorem 1.1 explicitly says the entropy requirement is insufficient for binary coefficient secrets. The subsequent s+eZ_0 discussion explains leakage of the secret's lattice coset. [source-verified result] The quantum sparse-state calculation neither changes that entropy condition nor supplies a reduction around it. The final comparison does not assume this is an impossibility barrier for all future methods.

No access failures occurred for these primary-source checks. No baseline quantum theorem is transported silently to composite q, ring-valued output, Boolean secret, or coefficient Gaussian error: those distributions differ, and all new calculations use the exact reference ledger.
