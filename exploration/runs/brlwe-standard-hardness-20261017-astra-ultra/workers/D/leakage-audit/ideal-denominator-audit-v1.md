# D supplementary audit of B-IDEN v1

Frozen 2026-10-17; PROVISIONAL, no acceptance authority. Input workers/B/ideal-denominator/first-test-v1.md, SHA25640d201c879de44d20cc707df816c1058fbbe3e96f21f75257e54739c392ec9ac. This note audits Sections4–5 and records one additional scoped consequence. It does not review every primary-literature import in that packet.

## Public-basis test

The row-action convention is internally consistent. The first column of M_a is P coeff(a), with P the displayed signed permutation, so B_J P coeff(a) is an integer vector because B_J M_a is integer. Its Euclidean norm is at most ||B_J|| ||M_a|| <=tau2 tau1, hence every coordinate is bounded by that product. If B_J is published and det(B_J) is a unit modulo q, B_J P is invertible modulo q. Conditional on every published B_J, a uniform comparator A_1 maps to an exactly uniform coefficient vector. Therefore the exact box acceptance ((2floor(tau1tau2)+1)/q)^n and the stated planted-minus-uniform advantage follow when the box radius is below q/2.

This uses the norm of the actual provided short basis. Replacing it by a potentially large HNF basis without preserving that norm would invalidate the planted test. No such substitution is justified. The probability of Good includes any probabilistic basis/tuple bound; conditioning on Good is not imposed on the comparator.

## Uniform fractional-module counting

For an integral J of index D prime to q, reduction J^-1/qJ^-1 -> R_q is a bijection. To check the kernel explicitly: if a in J^-1 reduces to zero, then every integer coefficient of aJ vanishes modulo q, so aJ is contained in qR and a/q lies in J^-1. Surjectivity holds since R is contained in J^-1. The quotient has q^n elements. Each of the D cosets of R in J^-1 contributes at most(floor(2B)+1)^n points to[-B,B]^n. The stated upper bound on a uniform residue having a short lift follows, with collisions only reducing the count. J must be fixed independently of that uniform residue; adaptively selecting J is outside this proof.

## Additional small-catalog advice consequence

Suppose the hidden ideal generator has support in a publicly indexed catalog J_1,...,J_s with s polynomial in n, and for each catalog member relevant to Good there exists a basis B_i satisfying the desired norm bound, with polynomially many bits. A nonuniform polynomial-size advice string may list all those bases. The distinguisher tests A_1 against every B_i and accepts if any centered B_i P A_1 lies in the short box. Planted acceptance is at least Pr[Good]; uniform acceptance is at most

    s ((2floor(tau1tau2)+1)/q)^n

by the union bound, regardless of overlap among tests. The hidden ideal index itself is unnecessary. All bases and the list are selected before the challenge and depend only on the public parameter index; this is ordinary nonuniform advice, not challenge-dependent advice.

In particular the concrete sampler with fixed public p,omega and J=(p,X−r) over the n odd roots has support size n. If the proposed useful short-basis geometry holds with high probability in that family, then hiding which of these n ideals was selected does not prevent this nonuniform attack. This conclusion is conditional on the adversary model allowing polynomial advice and on the claimed basis geometry/bit bound. It is not a uniform algorithm for finding short bases, and it does not apply to an exponentially large hidden ideal catalog by listing all bases.

Thus B's general statement that the public-basis test alone does not exclude every hidden-J candidate is correct. The particular small-catalog hidden-J example requires the additional nonuniform qualification above. A hardness import using nonuniform short-vector advice must be compared against that same adversary model; hiding only the catalog index does not resolve the issue.

No experiment was requested or run for this algebraic audit. Source hardness remains OPEN.
