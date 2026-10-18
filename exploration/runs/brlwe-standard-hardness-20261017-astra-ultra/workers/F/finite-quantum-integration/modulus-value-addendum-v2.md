# F v2: split-prime value versus bit length

This addendum preserves and qualifies the v1 modulus discussion. It is a parameter-existence check, not a source-family hardness result or an acceptance of the new quantum theorem.

The factorial argument in `integration-ledger-v1.md` proves that for power-of-two n, a prime divisor q of (T!)^n+1 has q>T and q=1 mod 2n, and gives a polynomial bound O(nT log T) on its BIT LENGTH when T is polynomial in n. Indeed T! has exact multiplicative order 2n modulo an odd such prime: its n-th power is -1, and n is a power of two. This argument does not bound q's VALUE by a polynomial and provides no efficient factorization algorithm. Consequently it alone does not make a width containing a multiplicative q polynomial in n.

The supplied A addendum `workers/A/fractional-composition/polynomial-modulus-existence-v1.md`, SHA256 e96f46d05a36ddae1c9662c4befe0637bf50cc09d58865a6a581cae4162fe272, makes the stronger value claim using a primary least-prime theorem. Its cited source is Triantafyllos Xylouris, *On Linnik's constant*, arXiv:0906.2749v1, submitted 15 June 2009. The author's primary abstract states an absolute-constant upper bound C m^5.2 for the least prime in a reduced residue class modulo m. This review directly checked that abstract; it does not re-prove the analytic number theory or claim an explicit numerical value for C.

For an integer T above the required polynomial threshold, set m=2nT and take the least prime q=1 mod m. Since gcd(1,m)=1, the cited theorem applies. A prime in this class cannot be 1, so q>=m+1>T, and q=1 mod2n. The bound q<=C(2nT)^5.2 proves polynomial VALUE for polynomial T, and hence logarithmic-in-that-value bit length. The existence of an absolute C suffices for this asymptotic statement. It is not a numerical modulus bound with a specified constant.

An algorithm may enumerate 1+jm and test primality until the first prime. Even trial division gives a finite polynomial-in-n asymptotic time under this value bound, although its exponent and constant are impractical. It need not know C to terminate. No efficient factoring is invoked. For the fully explicit finite sampler, q is SUPPLIED and all bit/gate bounds use its actual encoding, so there is no hidden C in the quantum gate certificate.

For every eligible ideal retain gcd(N(J),q)=1 as an independent hypothesis. The progression 1 mod2nT alone does not ensure that for arbitrary J. One can fix q and restrict to the already stipulated eligible ideals; J=R is a nonempty example. Alternatively finding a q that avoids a particular possibly exponential D needs an additional argument and is not asserted here. A fixed supplied q with this pointwise condition is exactly what the existing A/B/C composition uses.

With polynomial-value q, fixed rho<1, polynomial k and inverse-polynomial recovery gap delta in the v1 explicit family, the displayed same-J output width nq/(sqrt(2)d0) is polynomial in n, because d0 and its logarithmic/numerical precision schedule are already explicit there. This is a width compatibility observation. It does not turn the bounded-norm integral-ideal family into an arbitrary ideal family or prove a standard worst-case approximation consequence.

Primary source: [Xylouris, arXiv:0906.2749v1](https://arxiv.org/abs/0906.2749). Source limit: primary abstract checked; full analytic proof not independently audited.
