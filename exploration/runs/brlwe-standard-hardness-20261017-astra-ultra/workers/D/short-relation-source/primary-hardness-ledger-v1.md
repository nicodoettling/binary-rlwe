# D-SREL primary hardness ledger v1

Status: source audit only; no new standard source edge established. Accessed 2026-10-17. Claims below use primary papers or an author's presentation. Secondary search results were navigation only. Full direct ePrint retrieval failed; indexed primary theorem passages were read, with author-hosted primary PDFs used where available. The restricted shell could not resolve external hosts; no paper download was completed. These ordinary access errors were not content-policy interruptions. No external model session or executable experiment was used.

## SS11: broad Gaussian public-key ratios

Primary: [Stehle–Steinfeld, Making NTRU as secure as worst-case problems over ideal lattices](https://users.monash.edu.au/~rste/ntruenc.pdf), Theorem3, printed p14, and key-generation figure. For power-of-two n>=8 and split prime q>=5, its sufficient coefficient width is sigma>=2n sqrt(log(8nq)) q^(1/2+2epsilon). Independently sampled, shifted/scaled Gaussian numerators and denominators are restricted to q-units; their ratio is close to uniform on R_q^times. The displayed distance is 2^(3n) q^(-floor(epsilon n)).

This ratio theorem is statistical. Encryption hardness additionally uses RLWE; it is not a hardness proof for distinguishing sparse ratios. Its denominator is broad, not a weight-O(log n) ternary relation. It does not retain the denominator ideal. Uniform units are not exact uniform R_q: their distance is 1-(1-1/q)^n. These are distinct from the FG numerator-shape failure proved independently in principal-ntru-joint-law-v1.md. No security statement is transferred from the encryption theorem to the new source.

## PMS21: actual ideal-to-NTRU reduction and incompatible decision edge

Primary: [Pellet-Mary–Stehle, On the hardness of the NTRU problem](https://eprint.iacr.org/2021/821.pdf), Algorithms4.1–4.2, Theorems4.4/4.9, Section5. In canonical degree-d coordinates, Theorem4.9 assumes sqrt(q)/gamma>=13 d³ log(d) delta_K² Delta_K^(1/d), and gamma gamma' sqrt(d)>1. With N=floor((sqrt(q)/(gamma d^(3/2)delta_K Delta_K^(1/(2d))))^d), it sends the specified ideal distribution to NTRUvec, with gamma_HSVP=(gamma/gamma')4d delta_K; one call preserves success. Algorithm4.2's distribution comes from randomized ideals and rounding, not independent sparse coefficients. The preceding worst-case edge has an ERH and additional algorithmic-cost dependence.

Section5 instead reduces NTRUmod to decision NTRU. These search tasks differ. The authors explicitly explain the noncomposition in their [primary talk abstract](https://simons.berkeley.edu/talks/hardness-ntru-problem). No standard decision-FG conclusion follows by concatenating those arrows. None of these claims says NTRUvec lacks standard evidence.

## FPS22: module-uSVP strengthens the search picture, with explicit extra oracle

Primary: [Felderhoff–Pellet-Mary–Stehle, On Module Unique-SVP and NTRU](https://eprint.iacr.org/2022/1203.pdf), Theorem4.1, printed p18. It gives vector/module reductions preserving their corresponding task types, for a distribution induced by its uSVP-to-NTRU transformation. The theorem requires access to gamma_HSVP-id-HSVP and reports a runtime polynomial in input size, exp(d log(d)/log(2q/q0)), and zeta_K(2). For power-of-two cyclotomics zeta_K(2)=O(1).

Consequently, at polynomial q the displayed exponential factor does not furnish a polynomial-time bound; changing q does not remove the ideal-HSVP oracle. This is a limitation of that published guarantee, not an algorithmic lower bound. Its rank-two module and induced NTRU search distributions are not the rank-one, public-hidden-denominator FG experiment. Importing the desired ideal solver as this extra oracle would not independently establish that source's hardness. The authors' [2023 overview](https://apelletm.pages.math.cnrs.fr/page-perso/documents/presentations/NTRU_RISC_Alice.pdf), slide20, retains the ideal-SVP-oracle qualification.

## FPSW23: stronger small-norm-prime standard search source

Primary: [Felderhoff–Pellet-Mary–Stehle–Wesolowski, Ideal-SVP is Hard for Small-Norm Uniform Prime Ideals](https://perso.jfelderhoff.fr/work/papers/FPSW23.pdf), Theorem6.2, Corollary6.3, pp32–34 of the author PDF. Corollary6.3 gives, under ERH, a quantum expected-polynomial reduction to vector NTRU for h=IdealToNTRU(p,q), with p uniform in its specified prime-ideal interval. Its modulus has form (gamma^4/gamma'^2)poly(Delta_K^(1/d),log Delta_K,delta_K). Runtime includes inverse oracle success and inverse prime-density factors.

This is genuine standard-family search evidence, stronger than discarding NTRU wholesale. Theorem6.2 also forces every valid short solution's denominator g into the source ideal p. If N(p)>w^(n/2), no weight-w ternary g can lie there: |N(g)|<=||g||coef^n=w^(n/2), while N(p) divides |N(g)|. Thus its high-norm source cannot secretly supply the needed sparse denominator within that solution window. The decision/public-J/spherical-FG edges remain missing. This norm implication is a separate elementary deduction, not a claim made by the paper.

## CDPR16: exact scope of short-generator recovery

Primary: [Cramer–Ducas–Peikert–Regev, Recovering Short Generators of Principal Ideals in Cyclotomic Rings](https://ir.cwi.nl/pub/24685/24685B.pdf), Theorem4.1 and Section5. The recovery condition bounds projections of Log(g) on all relevant unit vectors by c sqrt(m)/(log m)^(3/2) with specified probability; its supplied generator must differ by a cyclotomic unit. Section5 proves the distribution condition for continuous spherical Gaussians and sufficiently wide discrete Gaussians. The full unit/cyclotomic-unit index is a separate issue discussed after the theorem.

A weight-O(log n) ternary coefficient law does not automatically satisfy that log-embedding condition, nor does Euclidean shortness alone certify the required unit-coset input. I therefore do not declare arbitrary hidden sparse generators polynomial-time recoverable from this theorem. The general 2^Otilde(sqrt(n)) approximate-SVP result also gives no useful polynomial-factor attack on the narrow source by itself. Conversely, failure to apply this attack supplies no standard hardness theorem or security evidence.

## Exact target still required

The candidate to be founded is the whole law (HNF(J),(A_i)_i), J sampled with a hidden sparse relation and A_i conditionally independent spherical FG(J^-1,s) modulo q, against the same J marginal and exact independent uniform responses. The primary statements above do not furnish this law. Current result: OPEN standard foundation, with explicit law/parameter failures rather than a general impossibility assertion.
