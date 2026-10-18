# Scientific boundary after the proposed OHCP bridge

PROVISIONAL assessment, based on checked primary definitions/theorems. The computational foundation is still OPEN. The positive proposed implication is uniform decoding for bounded-index ideals; no checked theorem below turns this into standard unrestricted ideal-lattice hardness.

## Exact restricted family and direction

Assuming the separate A-FRAC and B-FINITE source maps and the repaired C-OHCP packet, a fixed algorithm recovering binary secrets from the original uniform public law yields, for EVERY integral J with N(J)<=2^(rho n) and gcd(N(J),q)=1, an oracle solving BDD on qJ^-1 within canonical infinity radius d0. The ideal is a public input. No average family Gen, hidden ideal, short-basis advice, or trapdoor is needed for this conditional implication.

This is a worst-case quantifier over a restricted family. Calling it a worst-case problem does not identify it with the standard hardness premise over arbitrary ideals. The direction needed to close the run is a polynomial-time reduction from a verified standard worst-case ideal-lattice problem to this restricted decoding family with its actual radius and ring dimension.

## Primary standard definitions do not impose this index bound

Lyubashevsky–Peikert–Regev, [On Ideal Lattices and Learning with Errors Over Rings](https://sites.cc.gatech.edu/fac/cpeikert/pubs/ideal-lwe.pdf), Section2.3.7–2.3.8 and Definitions2.10/2.11, uses arbitrary fractional ideals represented by an integral basis and a denominator. It observes that one can clear denominators by an integer scalar without loss for homogeneous lattice problems. This permits large integral norms; it does not restrict norm to2^(rho n). Polynomial representation length bounds log norm, not norm per dimension by a constant.

Theorem4.1 and its iterative proof keep the same underlying ideal I while reducing the discrete-Gaussian width. Their BDD oracle is on I's dual. They do not replace an arbitrary I by a low-index ideal. The standard quantum BDD-to-DGS lemma therefore only gives, from the proposed oracle on L=qJ^-1, Gaussian sampling on L*=conjugate(J)/(nq). Scaling and conjugating gives sampling on the SAME J. For canonical Euclidean BDD radius d0, the conservative output width is

    s_J = n*q*sqrt(n)/(sqrt(2)*d0).

This can yield polynomial-factor short vectors for the bounded-index family when q/w and1/delta are polynomial, after completing the operational oracle. It does not enlarge the family.

## Rational and principal normalization do not preserve the binary ambient ring for free

Multiplication by a nonzero field element a sends an ideal I to aI and changes its norm by |N(a)|. An integral target J=aI requires a in I^-1. Finding a with |N(a)|N(I)<=2^(rho n), with controlled distortion, is itself a substantive task. Clearing a denominator instead multiplies the norm, and dividing an integral ideal by an arbitrary real or rational determinant scale generally produces a fractional ideal that is not contained in the fixed R.

The finite-coset lossiness budget counts R/J, where the secret is binary in the fixed coefficient basis of R. Replacing both the ideal and the ambient lattice by scaled objects changes this secret law. A binary coefficient vector in aR is not automatically a binary coefficient vector in R. A canonical diagonal Arakelov normalization likewise changes the integer lattice/secret alphabet; geometric normalization alone is not an endpoint-preserving reduction.

For orientation, even an existence-only Minkowski ideal-class normalization gives the familiar bound

    N(J) <= (4/pi)^(n/2) (n!/n^n) sqrt(Delta_K).

With Delta_K=n^n, its nth root is asymptotic to(2/(e sqrt(pi)))*sqrt(n), rather than a constant below2. This is an upper guarantee, not a lower bound on every ideal's best representative; it simply does not certify the required smaller family. Efficiently finding an optimally short representative and controlling multiplication distortion would be additional obligations.

## A checked randomization theorem has an explicit norm gap

Gentry's [primary thesis](https://crypto.stanford.edu/craig/craig-thesis.pdf), Theorem16.3.4, randomizes an input ideal of norm in[N,2N] into invertible primes of norm in[a,b], with a factoring oracle and prime-density conditions. Its displayed constraints include

    a² > 2N t0^n,
    t0>=t>=gamma_Mult(R)*n^(3/2)*s,
    s=n³||f||³(b/N)^(1/n)*omega(sqrt(log n)).

Let C_n=gamma_Mult(R)*n^(9/2)*||f||³*omega(sqrt(log n)). Eliminating N gives

    a² > 2b C_n^n >= 2a C_n^n,
    a^(1/n) > 2^(1/n) C_n.

Thus every target ideal in this theorem has norm per dimension growing polynomially, outside2^(rho n) for fixed rho<1. This conclusion does not rely on an arbitrary choice N=b or on averaging over a source family. Factoring/quantum access does not remove this quantitative condition.

The later de Boer–Ducas–Pellet-Mary–Wesolowski [Arakelov self-reduction](https://ir.cwi.nl/pub/30072/30072.pdf), Theorems4.4/4.5, has its own explicit large rounding/sampling scale. Earlier C packets already compute its denominator/index mismatch and the FPSW prime-family mismatch. Neither imported theorem currently supplies the required bounded-index family. Those prior scoped failures must not be broadened into a general impossibility claim.

## Completion judgment

The new periodic/OHCP mechanism, if all proofs and finite interfaces pass fresh reviews, is a meaningful computational reduction from original binary recovery to a concrete restricted ideal-decoding problem. It goes beyond merely naming a decisional noisy-point assumption. The run is not complete on standard hardness grounds until a verified theorem reaches the low-index family at the actual polynomial decoding radius, or a different mechanism avoids the index restriction. No such primary theorem has been verified here.
