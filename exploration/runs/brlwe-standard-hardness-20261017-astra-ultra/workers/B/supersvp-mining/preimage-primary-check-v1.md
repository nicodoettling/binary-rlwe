# Primary preimage sampler check

Status: source statement checked; integer-output implementation interpretation remains a separate dependency.

Primary source: Brent Waters, Hoeteck Wee, David J. Wu, *New Techniques for Preimage Sampling: Improved NIZKs and More from LWE*, EUROCRYPT2025, full version Theorem3.9, PDF page12. Author-hosted version: https://www.cs.utexas.edu/~dwu4/papers/MultiPreimage.pdf . The ePrint URL https://eprint.iacr.org/2024/1401.pdf returned403 through the open tool; the author-hosted PDF opened successfully (46pages).

The stated gadget theorem applies to arbitrary valid trapdoors, with column count at least3n ceil(logq), width at least m||T|| logn, maximum-entry trapdoor norm, and distance2^-n from the canonical conditional preimage law. This matches the numerical primitive used in 2026/2443 Lemma3.6.

The author-hosted theorem writes its output in Zq^m. Our ideal-ring packet follows 2026/2443's explicit unreduced integer-output convention. The preservation of the integer sample should be checked against the underlying MP12 algorithm, rather than inferred solely from a modulo-q output signature. Its validity does not depend on random-matrix hardness, and a general preimage-sampler application to coefficient-expanded ring matrices is distinct from importing general-matrix hardness.

No theorem in this source supplies the missing binary-secret or low-index ideal hardness premise.
