# Can the short class-word problem itself query the eligible ideal oracle?

2026-10-17. PROVISIONAL constructive test. This tries to use the restricted DGS oracle directly on a class-relation lattice produced by the quantum class computation. It is not a theorem that all class-changing reductions fail. No new experiment or probabilistic lemma is used.

## Actual ring and input

Let K be the power-of-two cyclotomic field of degree n>=4. Its Galois group is C2 x C_(n/2), with complex conjugation tau generating the first factor and the residue class 5 generating the second. Let H=<sigma> have order m=n/2. On the relative class group, tau acts by inversion. Thus the natural relation ring is

    A=Z[Gal(K/Q)]/(1+tau) = Z[T]/(T^m-1).

This is the ring used in CDW's relative-class argument, §4.3 of https://ir.cwi.nl/pub/30736/30736.pdf. It is a reducible cyclic ring, NOT the negacyclic domain Z[T]/(T^m+1) of the binary source. Indeed (T-1)(1+...+T^(m-1))=0 in A with both factors nonzero. Changing the sign convention cannot remove those zero divisors.

For an explicitly known class c, the map A -> A c sends an exponent vector to its Galois-orbit class product. Its kernel is an ideal of A, with index |A c|. Quantum class computation can describe this homomorphism and its integer kernel, but it does not change the ring. If several classes are needed to generate the relative class group, the natural kernel is a submodule of A^d rather than a rank-one ideal. That module-rank distinction is retained.

## A genuine componentwise query when the input qualifies

One can partially repair the ring mismatch on the odd-order part of a cyclic A-module. Over Z[1/2], T^m-1 splits into the power-of-two cyclotomic factors. Their pairwise resultants are powers of two, so the resulting idempotents act on every finite odd-order module. Each component M_j is a module over a genuine cyclotomic ring R_j=Z[T]/Phi_(2^j)(T). If the original module is cyclic, so is M_j, and its annihilator ideal J_j satisfies

    R_j/J_j is isomorphic to M_j,
    N(J_j)=|M_j|.

The corresponding ordinary ideal basis can be computed as the integer kernel of the explicitly known finite-group homomorphism. If d_j=deg R_j is a supported power of two, |M_j|<=2^(rho d_j), and gcd(|M_j|,q_j)=1, this J_j is an actual eligible query. These conditions must be checked; the degree-one component can simply be handled as an integer congruence separately.

For a qualified component and a target exponent vector a_j, one nonzero short DGS output x in J_j gives a full basis of J_j by rotations and flag saturation. If ||x||coef<=B_j, that basis has row lengths at most d_j B_j. Nearest-plane rounding then computes v_j in J_j with

    ||a_j-v_j||_2 <= (1/2) d_j^(3/2) B_j,
    ||a_j-v_j||_1 <= (1/2) d_j^2 B_j.

Thus this IS a public oracle-assisted class-representative algorithm on the qualified component. The output is a short exponent representative of the SAME finite-module element, with DGS errors/zero/tails charged explicitly. It is not a Gaussian class word. Reassembling components also requires the actual CRT idempotent coefficients, whose size must be charged. No claim of a small global word follows merely from their existence.

## Why this does not yet give the arbitrary-class reduction

The index condition is the component's actual order, not the index of the starting small prime ideal. Even if all ideals generating the original class group have polynomial norm, |M_j| can be much larger. Exact pigeonhole check: if a cyclic relative module M has |M|>2^(rho m), then at least one component violates |M_j|<=2^(rho d_j), because sum d_j=m and product |M_j|=|M| on the odd part. No asymptotic class-number assumption is needed for this per-instance test. An arbitrary target may have a nonzero coordinate in that unqualified component, so solving only the others does not solve the class equation.

Increasing the cyclotomic dimension by ordinary induction does not fix this. For R_d inside R_N, N=rd, the extension ring is free of rank r, and

    |R_N/J R_N|=|R_d/J|^r,
    log N(J R_N)/N=log N(J)/d.

The index per degree is unchanged. Holding the quotient order fixed instead would require a NEW action of the extension generator on the finite module, satisfying its exact cyclotomic relation; it is not supplied by a free dimension padding.

An exact small arithmetic control shows that such actions can be forbidden. For any power-of-two N>=2, the order of 5 modulo 2N is N/2: v_2(5^(2^t)-1)=t+2 proves this directly. Every prime above 5 in Z[Y]/(Y^N+1) therefore has norm 5^(N/2). If an ideal's index is divisible by 5, its index is at least 5^(N/2)>2^N. Hence NO eligible ideal with rho<1 has a quotient containing 5-primary torsion, in ANY such degree. Numerically the minimum indices for N=2,4,8 are 5,25,625, exceeding 4,16,256. These are exact hand calculations, not a new computer experiment.

This is a counterexample to a generic claim that every finite relation quotient can be encoded at low index merely by enlarging a power-of-two cyclotomic dimension. It does NOT assert that the actual class module in a particular input has 5-torsion, nor that every alternative class reduction preserves its quotient. No unproved claim about power-of-two cyclotomic class groups is made.

Finally, even the qualifying-component nearest-plane bound is not automatically competitive. At the supplied wide DGS parameter B_j is polynomial with a large exponent, so the displayed exponent-word bound can be substantially larger than the explicit Stickelberger bounds already available in their scope. An oracle call must improve the quantitative class-word construction to improve the full ideal-SVP implication; its mere legality is insufficient.

## Disposition

The attempted direct class-relation query has a real positive conditional algorithm, but three gates remain for the full arbitrary input: the actual cyclic/module structure, eligibility of EVERY needed component, and a competitive global exponent/CRT bound. The present checked source theorems do not provide these gates. The full computational foundation remains OPEN. A further repair must change the representation or use the oracle without preserving the entire finite class quotient, while still accounting for the target class and all geometric transfer losses.
