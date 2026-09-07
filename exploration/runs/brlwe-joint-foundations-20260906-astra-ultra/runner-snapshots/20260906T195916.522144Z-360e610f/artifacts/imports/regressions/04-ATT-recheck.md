# C01 bounded nonauthor recheck of the proposed deterministic ATT repair

Completed 2026-09-06 at 15:54 UTC, within the unchanged 16:15 task deadline and before the 16:10 research stop. This additional reconciliation check was expressly assigned by the coordinator after the core C01 review was frozen. C01 did not author C02's proposed solver change. No experiment, worker, algorithm implementation or new attack optimization was performed.

**Disposition:** the deterministic short-vector and exact rounding argument passes. Accept its A2 consequence: a deterministic exp(O_c(d)) times polynomial(n,log q) distinguisher using the first source component, accepting every exact planted A2 input and with negligible uniform false acceptance. For the generic arbitrary-q theorem, add a public complete CRT root list or a suitable primitive 2n-th root to its input. Without that addition, its claimed deterministic poly(log q) root-setup cost is not justified by the proof.

## Exact reviewed versions

- `criticism/C02/proposed-ATT-v3.md`, internally titled ATT-D v1, SHA256 **1fce3b7ad8c10de075fb161baab32d38786651bd72e059e9e2998a332bd6081f**.
- Frozen `snapshots/review-v1/refinement/R02-break-A.md`, SHA256 **f6ad32c87995741c7a17a7ee28e22b3370071ab15f1387cca5ce81079f08bf59**.
- The canonical A2, parameter table and prime-regime inputs already reviewed in the core C01 report.
- Coordinator's explicit reconciliation instruction: the generic attack may assume public CRT roots; A2 uses its polynomial-q field enumeration. C02's proposed file remains unchanged, and this input correction must be reflected in the reconciled ATT record.

The core C01 report SHA256 remains **010715d762513148506589cdb432e6fb619eeac30f4cb413985f1e7b6d98b88b**. Its bridge/extraction verdicts and unchanged blind report are not rewritten by this additional check.

## Primary results directly checked

[Boudgoust--Gachon--Pellet-Mary, ePrint 2022/709](https://eprint.iacr.org/2022/709.pdf): directly checked Theorem 3.2 and Lemma 3.3 (printed pp. 16-17), Section 3.2's integer basis/stabilizer operations (pp. 18-19), and Corollary 4.2 (p. 21). The lifting theorem requires an integral ideal with no ramified prime factors and its decomposition field; a gamma Hermite solution there lifts with factor sqrt(ambient degree/subfield degree). The power-of-two BDD reduction requires gamma_1>2gamma_4. This recheck uses the lifting theorem, not the unspecified success policy of the original approximate solver.

[Micciancio--Voulgaris, ECCC TR10-014 revision 1](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download): directly checked Section 2 (printed pp. 6-7), Theorem 5.4 and Corollary 5.5 (pp. 20-21). Corollary 5.5 supplies deterministic exact SVP in single-exponential lattice rank. Section 2 explicitly allows a d-by-k integer basis and restores polynomial dependence on ambient dimension d and entry bit size; the exponential parameter is rank k. Thus a large ambient dimension is not silently treated as polynomial in the small subfield rank.

The Hanrot--Pujol--Stehle approximate-solver import is not load-bearing for this replacement, so this critic did not newly audit it or infer any numerical success probability from it.

## Independent reconstruction

Let K=Q[X]/(X^n+1) with n a power of two. The ring of integers has the displayed power basis. Fix public split q, an integer coefficient bound b, and a power-of-two r dividing n with 2d<=r<=n. Given the CRT roots, the cyclotomic automorphism group acts freely on them. A subgroup H of order h=n/r therefore has r equal-size orbits. There is such a subgroup for every requested power-of-two order, and its automorphisms are explicit signed permutations in the coefficient basis.

Enumerating all collections of at most d orbits takes at most 2^r branches. A planted support of size at most d is contained in at least one enumerated union. On that branch, if Omega is the complement of the union and t=|Omega|, then t>=n(1-d/r) and A-F belongs to the integer ideal L vanishing on Omega. The branch does not receive the hidden support or F.

Since q is fully split and odd, it is unramified in K. The ideal L is a product of the t distinct primes corresponding to Omega. Hence D=q L^-1 is the product of the other n-t primes. It is integral, has norm q^(n-t), contains q O_K, and is H-stable. These properties include the empty-product branch. Computing its full stabilizer gives size s>=h; its fixed field has degree k=n/s<=r. The lattice J=D intersect K_D has rank k. Integer congruence bases, stabilizer tests and rational fixed-space intersections have polynomial input-bit cost, as the source's Section 3.2 also explains.

For every x in K_D, power-of-two canonical orthogonality gives

    ||Sigma_K(x)|| = sqrt(n) ||coeff_K(x)||,
    ||Sigma_K(x)|| = sqrt(s) ||Sigma_K_D(x)||.

Consequently the subfield canonical norm is exactly sqrt(k) times the ambient coefficient norm on J. A deterministic exact SVP solver on the rectangular integer coefficient lattice therefore returns an exact subfield-canonical shortest nonzero v. Minkowski's ordinary k-dimensional cube bound makes v a sqrt(k)-Hermite solution. BGP's lifting theorem then makes it a sqrt(n)-Hermite solution in D. Since det(Sigma_K(D))^(1/n)=sqrt(n) q^((n-t)/n), w=v/q belongs to L^-1 and satisfies

    ||Sigma_K(w)|| <= n q^(-t/n).

No numerical complex embedding is needed by the algorithm. The factor sqrt(k) norm conversion is constant over the whole subfield; it is not an unproved equivalence between two varying norms. As a further bit-size control, q belongs to J, so the returned coefficient-shortest vector has norm at most q and every output coefficient has O(log q) bits. Rational linear systems used afterward therefore have polynomial-size input and output descriptions.

The explicit dual rounding implementation is correct. For j=0,...,n-1, let d_j=coeff(conj(X^j w)). Then for every z in L,

    <coeff(z),d_j> = Trace(z X^j w)/n

is the constant coefficient of the integral element z X^j w, hence an integer. This divisibility is justified by the power-of-two power basis; it is not an arbitrary-number-field assertion. Since w is nonzero in a field, multiplication by w is invertible, so these n dual vectors are independent. Multiplication by X^j and conjugation preserve coefficient norm, and thus every d_j has norm ||Sigma_K(w)||/sqrt(n).

For a promised branch, the coefficient error has norm at most sqrt(n)b. Its dual inner products are therefore at most n b q^(-t/n). The strict hypothesis

    q^(1-d/r) > 2 n b

makes all these quantities strictly below 1/2. Rounding the dual inner products of an integer lift of A gives those of the exact L-point A-F. Solving the n independent rational equations recovers that point and hence F. The method requires independent dual vectors, not a full basis of the dual lattice: uniqueness of the real solution suffices once the correct integer inner products have been rounded.

Off-promise behavior is harmless because the algorithm verifies that F' has integer coefficients in the box and A-F' belongs to L. For uniform A modulo q O_K, its image modulo L is uniform among q^t cosets. At most (2b+1)^n cosets contain a candidate F'. A union bound over at most 2^r branches therefore gives

    p_false <= min(1, 2^r (2b+1)^n / q^(n(1-d/r))).

This bound does not require decoder success or independence between branches. For planted A, at least one promised branch is decoded deterministically and verifies. Thus the new solver policy has acceptance one on every promised planted input, rather than an unspecified p_alg. The total cost is 2^r branches times exp(O(k)) with k<=r and polynomial basis operations: exp(O(r)) times polynomial input size. Exponential memory is allowed.

## New targeted exact controls

**Dual sign and normalization control.** Take n=2,q=17,r=2,d=1,b=1, with the promised zero root 4. Then L consists of coefficient pairs (a,b) with a+4b=0 mod 17, and D can use shortest v=4+X. Indeed norm squared 17 is minimal by checking the possible second coefficients 0,+/-1,+/-2,+/-3,+/-4 below that norm; larger second coefficients cannot improve it. Put w=(4+X)/17. The two dual rows are (4,-1)/17 and (-1,-4)/17. Their dot products with L's vectors are integers.

Choose F=(1,1), L-point z=(13,1), and the representative A=(14,2). Its dual measurements are 54/17=3+3/17 and -22/17=-1-5/17. Rounding gives 3,-1 and the rational system returns z=(13,1), hence F=(1,1). Here sqrt(17)>4 verifies the strict promised radius. This checks the conjugation, 1/n trace normalization, integer representative change, and actual rounding path without a CPU experiment.

**Hidden support control.** For n=8,r=2, the subgroup {1,5,9,13} modulo 16 partitions the primitive exponent set into {1,5,9,13} and {3,7,11,15}. Every singleton support is covered by an enumerated branch; it is not assumed known. Larger full stabilizers only decrease the SVP rank.

**Boundary controls.** Equality of an error inner product to 1/2 does not permit unique rounding; the strict inequality is retained. Exact SVP must return nonzero v; otherwise the dual rows would be dependent. Verification protects the uniform false-positive bound even if an off-promise solve returns a rational nonlattice vector. None of these controls uses a product of conditional marginal success estimates.

## C01-ATT-O1: generic root-setup input is missing

The unrevised generic statement allows arbitrary split q and claims deterministic exp(O(r)) times poly(n,log q,log b), while supplying only the first ring component and the listed numeric parameters. Its algorithm starts with the full CRT roots. The known-root BGP setup does not itself supply a deterministic poly(log q) routine that produces those roots. This is a genuine missing algorithmic input in the proof, not an assertion that such root finding is impossible.

**Repair checked and accepted:** state the generic theorem with a public complete root list, or a supplied primitive 2n-th root whose odd powers generate it. This input is independent of the hidden support and can be verified by direct modular powering. All subsequent operations and the proved running time then have the stated deterministic cost. This is the coordinator's chosen correction. The unrevised generic paragraph remains GAP historically until that explicit input is recorded.

**A2 is unaffected:** q<=n^K for a fixed K, so deterministically testing every field residue for X^n+1=0 takes polynomial time in n. That preprocessing can produce and order all roots before the attack; it is part of the polynomial factor. No unjustified poly(log q) claim is needed for this restricted ensemble.

## A2 consequence and final dispositions

Choose C0>=max(2,4(1+c)/c), and let r be the least power of two at least C0 d. Eventually r<=n and r=Theta_c(d). Since q>=2 n^(1+c) ell^3 and d/r<=1/C0,

    q^(1-d/r) >= n^(1+3c/4) times a fixed power of ell,

which eventually exceeds 2 n b with b=ell^2. The logarithm of the false-positive upper bound is at most O(d)+O(n log ell)-Omega_c(n log n), so it is -Omega_c(n log n). The attack therefore has advantage 1-exp(-Omega_c(n log n)) against exact A2 and deterministic time exp(O_c(d)) times polynomial(n,log q). It uses only A and is independent of H or its completion correlation.

| Version or conclusion | C01 disposition |
|---|---|
| Original probability-qualified ATT v2 | Retain historically with p_alg-p_false; no retroactive success assertion. |
| C02 ATT-D v1 mathematical solver/norm/rounding proof | ACCEPT. |
| C02 ATT-D v1 generic deterministic runtime without public CRT roots | GAP, C01-ATT-O1. |
| Reconciled generic ATT v3 with explicit public CRT roots | ACCEPT; the input correction above closes C01-ATT-O1. |
| Deterministic ATT v3 restricted to the canonical A2 polynomial-q ensemble | ACCEPT, including root-enumeration preprocessing and every-planted-input success. |

This repairs the solver-success objection for the explicitly chosen new deterministic policy. It proves an asymptotic subexponential attack on A2 and is superpolynomial at d=floor(sqrt(n)/ell^4). It supplies neither a polynomial-time attack in that regime nor a practical security-bit estimate. P0-A2 is still an unsupported computational hypothesis; a subexponential distinguisher alone does not refute its polynomial-time formulation.

All assigned checks are complete. C01 stops research on returning this report.
