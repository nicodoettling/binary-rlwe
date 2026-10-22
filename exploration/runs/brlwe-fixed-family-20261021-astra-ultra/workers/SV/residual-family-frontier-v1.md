# Residual source frontier and alternatives, v1

2026-10-21. Author analysis, not a hardness claim. Exact source radius remains epsilon_*ell²/(1024 nKchi Qmax); a changed FF source radius reopens all comparisons.

## What the effective classifications remove

SV-BDD-CLASS v1 removes all polynomial numeric index, small exponent e<1/(2r), and effectively known sufficiently short members. SV-FROB-PRIME v1 removes EVERY eligible prime ideal of polynomial numeric characteristic p, including exponential index. SV-SYMDESC v1 computes a stronger invariant from an ordinary basis: after removing2, d_H=N(J_o)^(1/|Stab(J_o)|). Polynomial numeric d_H suffices by actual fixed-lattice collision construction. Prime powers have d_H=p^b. These are PROVISIONAL exact-version theorem candidates, not accepted results yet.

For prime ideals the polynomial guarantee now leaves superpolynomial characteristic p, not merely p>=1/(2r). Their residue degree satisfies f log2p<=rho n; in particular f=o(n/log n) whenever logp/logn→infinity. This is a genuine narrowing of arithmetic candidate families, with no implication that the remainder is hard.

## Large split prime in ordinary coordinates

Take an odd prime p=1 mod2n, a∈F_p with a^n=-1, and J=(p,X-a). An ordinary basis is p in the first coordinate and X^i-a^i for i=1,...,n-1, with powers represented modulo p. Its index and quotient exponent arep, and its Galois stabilizer is trivial, so d_H=p. Encoding length is O(n² logp), even when p is exponential in n.

The exact inverse lattice has the description

    J^-1=Z^n+(1/p)Z*(1,a^-1,...,a^-(n-1)),

with powers interpreted modulo p. To check this, J is the kernel of the coefficient functional (1,a,...,a^(n-1)) modulo p, so its coefficient dual is Z^n+(1/p)Z*(1,a,...,a^(n-1)). Conjugation sends the displayed latter vector to(1,-a^(n-1),...,-a), which equals(1,a^-1,...,a^-(n-1)) modulo p because a^n=-1. The coefficient dual of conjugate(J) isJ^-1.

At r<1/2, decoding is therefore exactly the task of finding k modp such that T-k*(1,a^-1,...)/p is within canonical-infinity radiusr of some integer coefficient vector. Given k, ordinary coefficient rounding recovers that integer vector; from the true lattice output, k=p*lambda_0 modp. This is an algebraic normal form, not a newly asserted hardness assumption. The canonical error constraint is retained and must not be replaced silently by independent scalar errors.

A proposed established-hardness transfer must produce such p,a,J and map arbitrary source inputs/errors into this exact task with polynomial represented resources and useful radius. Mere absence of a decoder, or the common shape of a modular-approximation problem, supplies no such map. The earlier complementary-multiplier and integral-map obstructions still apply at their exact scopes to attempts that move between ideal families.

## Different Frobenius groups and products

For J=I_1...I_t, constructing f_i∈I_i separately and multiplying gives a member ofJ. If every ||f_i||₂<=sqrt(n), the elementary negacyclic norm inequality ||uv||₂<=sqrt(n)||u||₂||v||₂ yields

    ||product_i f_i||₂<=n^(t-1/2).

An additional2-part costs at most factor2 in the eligible family. Hence this route is sufficient at exact radius whenever4r n^(t-1/2)<1, with every acquisition and factorization cost separately charged. Constant t can meet this condition; an unrestricted growing t cannot be certified by this bound. This is an alternative when the intersection of component stabilizers is small, not an impossibility theorem for products.

Two distinct rational characteristics cannot be permuted by a Galois automorphism, so the stabilizer of a product of one prime power above each characteristic is the intersection of their stabilizers. It can be much smaller than either one. For several primes above the SAME characteristic, the residue image of fixed elements can be a product of several F_p copies; the prime proof's image-sizep claim cannot be reused. Example: degree16, p97 is split, and the product of two distinct primes has norm97²<2^16. sigma97 is identity and its fixed-lattice residue image has97² elements. SV-SYMDESC computes the actual image index rather than assumingp.

Ordinary-input acquisition of component factorization is an additional obligation if this product route is promoted to a theorem. Polynomial numeric quotient exponent permits elementary integer trial division; factoring X^n+1 over finite fields and recovering prime-power ideal factors still needs an explicit polynomial-cost algorithm/source. No such unreviewed factorization theorem is hidden in the current main classification.

## Rejected extensions retained

Dropping the strict rounding margin fails at J=R,f=2,T=1/4. Ignoring signed Frobenius cycles fails already at n4,p3 because X² maps to−X². Applying d_H^|H|=D before removing ramified2 fails at J=(1-X),n4: D2,h4,d_H2 gives16≠2. Declaring all polynomial encoding lengths numerically enumerable fails on exponential p orD. Reversing easy wide DGS into BDD remains invalid.

Next useful work is exact-version adversarial review, then either (a) an effective smaller-index invariant lattice for residual ideals, (b) a fully costed bounded-component decomposition algorithm with its exact radius, or (c) an independently established hardness map into the remaining large-characteristic source. None is established by this frontier note. FF, SV diagnosis and hardness remain separate.
