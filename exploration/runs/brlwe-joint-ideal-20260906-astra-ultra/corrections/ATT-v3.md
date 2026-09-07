# Reconciled ATT version 3 — deterministic grouped-orbit attack

This selects the separately specified deterministic solver policy of criticism/C02/proposed-ATT-v3.md (ATT-D v1), as independently checked by C01 in criticism/C01/ATT-recheck.md. It preserves the original qualified ATT v2 and C02 proposal unchanged in snapshots. It is a correction within the existing attack, not a new candidate family.

For power-of-two n, a split odd prime q, integer b>=1, and a power-of-two r dividing n with 2d<=r<=n, assume q^(1-d/r)>2nb. In the GENERIC arbitrary-q theorem, a complete public CRT root list, or a supplied primitive 2n-th root generating that list, is part of the input. It is independent of the hidden support. With that input there is a deterministic algorithm using only A (and public parameters), time exp(O(r))*poly(n,log q,log b), accepting every A=U+F with CRT support(U)<=d and coefficient F in [-b,b]^n. Uniform A is accepted with probability at most

    min(1, 2^r(2b+1)^n/q^(n(1-d/r))).

The algorithm enumerates subgroup-orbit supersupports, forms the complementary integral ideal, uses deterministic exact SVP on its rank-at-most-r fixed-subfield intersection, lifts a short inverse-ideal vector, and performs exact rational dual rounding with final verification. The strict error radius is essential. The proof, bit model, norm conversion and primary theorem locations are in the two cited critic notes. Exponential memory is allowed; no implementation or concrete bit-security estimate is claimed.

For A2, q<=n^K for fixed K, so deterministic field enumeration produces the CRT roots in polynomial time in n. Taking r to be the next power of two above C0 d, with C0>=max(2,4(1+c)/c), satisfies the strict gap eventually. Consequently the exact A2 first marginal has a deterministic attack in exp(O_c(d))*poly(n,log q) time, with advantage 1-exp(-Omega_c(n log n)). At d=floor(sqrt(n)/ell^4), this is subexponential and superpolynomial. A source implementation within xi_src changes the advantage by at most xi_src. This does not refute polynomial-time P0-A2 or support its hardness.

C02-O1 is closed for this explicitly selected new deterministic policy; no success probability is retroactively assigned to F03's original unspecified probabilistic implementation. C01-ATT-O1 is closed by the supplied-root generic input and the separately justified A2 root preprocessing.
