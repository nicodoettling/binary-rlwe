# Polynomial-value split modulus exists in the analytic window

2026-10-17. This supplements the parameter companion's supplied-modulus condition. It is only an arithmetic parameter existence check, not a cryptographic hardness claim.

Let T be an integer exceeding the polynomial lower threshold in (W1), and set m=2nT. The least prime q congruent to 1 modulo m satisfies q<=C m^5.2 for an absolute constant C, by the primary least-prime bound stated in [Xylouris, On Linnik's constant](https://arxiv.org/abs/0906.2749). I checked the author's primary abstract, which states the bound and exponent; I have not re-proved its analytic number theory.

As a deduction, q>m>=T, q=1 mod2n, and q is polynomial in n for polynomial T. Thus the width inequalities admit polynomial-VALUE split moduli, not only polynomial-bit moduli. Exhaustive testing of the progression until the first prime is polynomial in n under this bound, albeit with an impractically large exponent; public parameters can simply supply such a q. The separate condition gcd(q,D)=1 is still required of every ideal in the source family. No source-hardness family follows from this modulus construction.
