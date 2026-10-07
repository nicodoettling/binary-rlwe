# Exact source comparison and assumption boundary

The primary candidate uses Base2: sample a uniform d-root support T once, two independent uniform points U_1,U_2 of its supported ideal, and two independent coefficient D_ell noise vectors F_1,F_2. Publish (U_1+F_1,U_2+F_2), versus two independent uniform R_q elements. It contains no binary secret. This is an explicit two-point specialization of the same-hidden-ideal HLBDD source motivated in Order-LWE Section7. Its pseudorandomness at the chosen polynomial modulus and support dimension remains the computational assumption. No worst-case source reduction is claimed.

| Interface | Sample scope and differences |
|---|---|
| Search candidate A | Both available source points become public multipliers; two responses generated locally under one known-to-reduction S. One source advantage, one quotient guessing loss. |
| Earlier W3 observable decision bridge | One target pair; two source tests and a nonnegligible uniform-point rank loss at fixed polynomial q; imported extraction/completion remained provisional. |
| Earlier correlated A2/P0 | Active ideal point and F-dependent H_seq in source; unsupported exact correlated premise. A does not produce that source. |
| B partial splitting candidate | One original-ring target pair; exact packing of2f=Theta(log n) smaller-ring source points from one common ideal; conditional extraction not certified here. |
| C larger-q candidate | One target decision pair with log q~n^(1/8); polynomial bits, full imported/rederived extraction graph still pending review. |

The source definition's explicit comparator resolves terse printed notation using the primary proof's uniform R_q² endpoint. The exact source motivation and prime bounds are frozen in [source-and-parameters-v1.md](coordinator/source-and-parameters-v1.md). Existing source attacks only constrain the stated regimes and runtimes; no blanket absence-of-attack claim is made. The two concrete growing d choices are the scope of the proposed effective families. Neither independent nonbinary syntax nor this comparison proves the computational premise.
