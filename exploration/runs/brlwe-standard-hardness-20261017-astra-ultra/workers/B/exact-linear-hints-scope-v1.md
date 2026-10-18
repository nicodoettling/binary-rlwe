# B-WLL: exact scalar linear leakage is not a batch error oracle

Status: PROVISIONAL primary-scope check, 2026-10-17 20:34 UTC. No theorem imported as a new source foundation.

Primary: Wang–Lai–Liu, *Ring/Module Learning with Errors under Linear Leakage—Hardness and Applications*, PKC2024, [author ePrint](https://eprint.iacr.org/2023/826.pdf). Direct PDF access failed; primary indexed text exposed Definition3.1–3.2 (printedp12) and Theorems3.8–3.9 (p15).

Definition3.1's leakage is a single Z_q value, a sum of k coefficient inner products. The parameter k counts summands in that scalar value; it is not k separately exposed ring-valued hints. In Definition3.2 the hint descriptors are chosen before the challenge. Theorem3.8 guesses the one scalar leakage and loses a factor q in search success; q is polynomial in the security parameter. The following search-to-decision stage has further model and parameter hypotheses. No challenge-dependent full-error disclosure follows merely from the paper's title.

For the dense elimination map, cancelling H e needs nm scalar coordinates in the displayed complete-hint construction. Substituting one scalar inner product does not supply this vector. Repeated calls to a one-hint solver cannot be identified with one joint experiment exposing many hints on the same unknown errors. Guessing an entire h-coordinate vector costs q^h under the same direct strategy; polynomial q only makes this efficient for bounded h, not h≈n.

This observation does not rule out a different exact-leakage theorem or a different use of one scalar hint. It only closes the named import. The semi-adaptive noisy LSW interface is treated separately and constructively in semiadaptive-hints-map-v1.md.
