# C second route test: noninvertible-order hardness

Status **PROVISIONAL**; targeted primary-theorem check and explicit endpoint audit, not a proof that all such routes fail.

Navigation lead supplied by coordinator: Jutla–Lin, [Ring-LWE Hardness Based on Non-invertible Ideals, ePrint 2023/1839](https://eprint.iacr.org/2023/1839). The primary indexed PDF supplied Theorem 5.1, Definitions 5.1–5.3 and Lemma 5.7. Direct PDF opens failed; no primary PDF bytes or hash were obtained.

## Exact published endpoint

Theorem 5.1 considers an integer m coprime to q and orders O⊆R with mR⊆O. Its worst-case DGS input is a Z-basis of an O-ideal, with m and a maximal-order basis supplied; the order itself need not be given. Its conclusion is a quantum reduction to ordinary dual Ring-LWE with integer modulus q, full uniform secret in R∨/qR∨, visible uniform multiplier in R/qR, and the shared latent elliptical Gaussian family Υ_α. The condition is αq/m≥2w(n), α∈(0,1), w→∞. The displayed DGS scale contains η(L) sqrt(2)m w/α and sqrt(2n)/λ_1(L*).

This does broaden the worst-case input family, and its hidden-order representation is substantive. It does not give a low-dimensional ideal secret at the average-case endpoint. In particular, its word “hidden” refers to the order of the worst-case lattice input, not a hidden d-subset in the output RLWE challenge.

Lemma 5.7's clearing maps are module isomorphisms

    I/qI ≅ R/qR,
    mI∨/qmI∨ ≅ R∨/qR∨,

with a product compatibility relation. Both sides have q^n elements. They require an appropriate modular generator and ideal determinant; the paper's FindGen machinery supplies the algorithmic route, with a stated qualification on prime factors of q when the order is not provided. Our q>=n² prime satisfies the cited large-prime qualification. No small CRT image follows from noninvertibility of I as an O-ideal.

## Candidate use 1: erase the published multipliers

After dual conversion and coefficient rounding, planted responses are

    B_i=a_i S+F_i mod q,

with S uniform on all R_q. Erasing a_i produces the exact support mixture

    sum_{J⊆roots} (q-1)^|J|/q^n · (Unif(I_J)^⊗k + F),

where F retains its shared latent Gaussian parameter. On the comparator, responses are exactly independent uniform R_q. The full-support branch has probability (1-1/q)^n and gives exactly uniform responses independently of F. Hence the erased planted pair is within 1-(1-1/q)^n≤n/q of uniform. This is the historical erasure endpoint, now explicitly checked against the new paper's actual conclusion. It does not produce fixed sparse d.

Adding a fresh point from an arbitrarily chosen sparse I_T cannot reduce the existing ideal support of a_i S. Multiplying/projecting both worlds into I_T gives an I_T-supported comparator, not ambient uniform. The noninvertible clearing isomorphism does not change either calculation.

## Candidate use 2: retain noninvertible-ideal coordinates

Applying the inverse clearing map to the uniform multiplier produces uniform I/qI of cardinality q^n. This changes representation while preserving full entropy. It is not a source with q^d ideal leakage. Taking the *natural inclusion* of I into R modulo q instead may have a smaller image, but then the same inclusion acts on the comparator; it is not the clearing isomorphism. A proof must charge the discarded information and noise exactly. The checked primary statements do not furnish that missing simulator.

## Hypothetical generalized ideal-modulus variant

No ideal-modulus Q version of Theorem 5.1 is supplied by the inspected statements. If one extends it while retaining uQ⊆O, then u(QR)⊆R. Consequently, whenever the extended R-ideal has norm N(QR)=q^d, the norm argument still gives

    ||u||∞≥q^(-d/n).

If the extension also retains the BBPS α/||u||∞≥2w(n) gate, it inherits the same conflict with q^d≤2^(ρn). This conditional calculation is not a theorem about every possible extension: a genuinely different Gaussian/modulus mechanism could change the premise. An added conductor factor m≥1 cannot improve that unchanged gate by itself.

## Decision

This lead changes the worst-case lattice family but leaves the missing low-ideal noisy-point edge open. It does not presently supply a compatible binary-secret source. The next route is a direct reduction from standard known-ideal BDD/GapCVP/DGS to a public Gaussian-coset decision experiment, with an explicit acceptance and Fourier-mass calculation. That route must not assume that average-case noisy-point distinction is already a worst-case decoding oracle.
