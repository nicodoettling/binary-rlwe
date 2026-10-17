# Primary-source access and scoped verification — A v1

Date: 2026-10-16 UTC. New interpretations remain **PROVISIONAL**. Primary PDFs were targeted, not exhaustively surveyed. Direct open failures below are access errors, not content-policy interruptions. No remote computation occurred.

## Order-LWE / HLBDD

Primary: Bolboceanu–Brakerski–Perlman–Sharma, [ePrint 2018/494](https://eprint.iacr.org/2018/494), [full PDF](https://eprint.iacr.org/2018/494.pdf). The metadata page opened successfully and records last revision 2019-09-04. Direct PDF open returned HTTP 403. Primary-index searches returned the exact pages specified below; the permitted historical `workstreams/W1/primary-browser-extracts.txt` independently preserves the relevant prior PDF extraction. Alternate official-project PDF [PROMETHEUS copy](https://www.h2020prometheus.eu/sites/default/files/2022-06/Bolboceanu2019_Chapter_Order-LWEAndTheHardnessOfRing-.pdf) timed out on direct open.

Verified locations: full-version printed pp.34–36, Theorem6.2, Theorem6.3 and Corollary6.4; p.38, Definitions7.3–7.4; pp.39–41, Theorem7.5 and Lemmas7.6–7.7. Definition7.3 samples a hidden intermediate lattice, a uniform quotient point and ambient Gaussian. Definition7.4 specifies “two samples”; the same-ideal interpretation and ambient-uniform pair are fixed explicitly by Lemma7.7's final hybrids. Theorem6.2 uses a “non-uniform algorithm” with short complementary-ideal vectors as advice. Theorem7.5 assumes HLBDD and ordinary RLWE; Lemma7.6 uses rerandomization plus swallowing. Lemma7.7's unit step says “since q is super-polynomial”. Thus neither the worst-case Order-LWE theorem nor the known-ideal decoding statement proves the SC-v1 computational premise.

Exact quotes above total 10 words from this source. Primary search queries included the exact title plus `Definition 7.3`, `Theorem 6.2`, `Corollary 6.4`, and `Lemma 7.6`. The full PDF bytes were not retrieved, so no raw-PDF hash is claimed.

## Ring regularity and expansion ancestry

Primary: Lyubashevsky–Peikert–Regev, [A Toolkit for Ring-LWE Cryptography, ePrint2013/293](https://eprint.iacr.org/2013/293.pdf); [author-hosted full PDF](https://web.eecs.umich.edu/~cpeikert/pubs/toolkit.pdf); [conference version](https://www.iacr.org/archive/eurocrypt2013/78810035/78810035.pdf). Direct ePrint open returned403; author-hosted open returned502. Primary-index queries retrieved full-version printed pp.35–37 and39. Theorem7.4 and Corollary7.5 correspond to conference Theorem4.1/Corollary4.2.

The theorem uses `A=[I_k|Abar]`, with independent uniform random remaining columns, and Gaussian inputs on the canonically embedded integer ring. For `r>2n q^(k/l+2/(nl))`, it gives exponential statistical error and pointwise near-uniform output for almost all seeds. The discussion explains that the added identity column avoids the “common divisor” problem, and calls this “normal form”. Its regularity construction therefore closely precedes EX-v1's added W. Theorem7.4's expected Gaussian mass statement also supports a retained-seed average comparison. Exact box-input EX-v1 constants are not supplied by this Gaussian theorem. Printed p.39 Section8.2 provides the familiar compact encryption map behind later rerandomization.

Exact quotes above total4 words from this source. Primary-index queries were exact title plus `Theorem 7.4`, `Corollary 7.5`, `common divisor`, and `8.2`. No direct-PDF hash is claimed.

## Existing local entropic-RLWE baseline

The allowed local paper `literature/2020-1185.pdf` and its permitted September review attribute sample rerandomization to oracle-based or bounded-error constructions and impose a determinant/entropy cost excluding binary secrets. This is historical corroboration, not a newly re-proved result. A formal novelty review should compare EX's precise source, coefficient Gaussian target and fixed-h modulus family, rather than credit generic rerandomization as new.
