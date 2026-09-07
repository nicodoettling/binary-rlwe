# PR1 — a nonempty polynomial split-prime regime

Coordinator derivation, 2026-09-06 15:08 UTC; primary theorem statement checked, pending nonauthor scope review. This supplies only moduli for the analytic parameter inequalities. It supplies no source-hardness assumption or concrete security estimate. No experiment was run.

[Xylouris, Acta Arithmetica 150.1 (2011), Theorem 1.1](https://www.impan.pl/shop/publication/transaction/download/product/83078), printed p.66, states that the least prime P(a,M) in a reduced residue class obeys P(a,M)<=C M^5.18 with an effectively computable absolute C. The introduction on p.65 states the underlying effective polynomial Linnik bound. We use only this coarse polynomial existence conclusion, not a claim about the best present exponent.

Fix any desired constant gap exponent c>0. Choose a fixed integer h>1+c. For every power-of-two n let q be the least prime congruent to 1 modulo M=2n^h. Then

    2n^h+1 <= q <= C (2n^h)^5.18.

In particular q is odd and q=1 mod 2n. For ell=ceil(log2 n), sigma=2n ell^3, the lower bound gives q/sigma>=n^c for every sufficiently large n, because n^(h-1-c)/ell^3 tends to infinity. For any fixed K>5.18h, the upper bound gives q<=n^K eventually. Thus the required polynomial interval contains a fully splitting prime for every sufficiently large n. A theoretical polynomial-in-n search can enumerate this progression and test primality (even elementary trial division remains polynomial in n under this bound); no fast practical prime-generation claim is made or required.

Example: c=1, h=3 and any fixed K>15.54, such as K=16, give an asymptotically nonempty modulus family. The extractor, if proved for every qualifying polynomial q, and the completion can be evaluated at these same q. These conservative exponents are not optimized. For m=n^r target samples with the conservative sigma_m~sqrt(m)sigma_1, the same argument chooses h>1+c+r/2 and correspondingly larger fixed K; that is a recorded modulus/noise departure, not the original one-sample schedule.
