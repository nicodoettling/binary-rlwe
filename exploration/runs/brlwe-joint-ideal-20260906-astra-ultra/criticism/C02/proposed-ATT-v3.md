# C02 proposed correction ATT-D v1 — deterministic solver policy

Proposed 2026-09-06 by critic C02. **REPAIRED-PENDING-RECHECK: C02 is the author of this correction and does not independently accept it.** It changes the solver policy inside the existing grouped-orbit attack; it is not a third source family. The frozen ATT v2 remains the reviewed, probability-qualified claim until a different reviewer checks this note.

The input snapshot is `snapshots/review-v1`; its manifest SHA-256 is `29ef8e92ea6f82e6e4582e245f525e1f71e2f7e17eb0a542fba50155e981a143`. The reviewed R02 note has SHA-256 `f6ad32c87995741c7a17a7ee28e22b3370071ab15f1387cca5ce81079f08bf59`.

## Exact proposed statement

Let n be a power of two, q an odd prime congruent to 1 modulo 2n, and b>=1 an integer. Suppose A=U+F modulo q, U has at most d nonzero CRT coordinates, and F has integer coefficients in [-b,b]. Let r divide n, with r a power of two and 2d<=r<=n. Assume

    q^(1-d/r) > 2 n b.                                     (D1)

There is a deterministic distinguishing algorithm, using only A, with running time `exp(O(r))*poly(n,log q,log b)`, accepting every such planted A, and accepting uniform A with probability at most

    min(1, 2^r (2b+1)^n / q^(n(1-d/r))).                    (D2)

Thus its advantage is at least one minus the displayed false-positive bound. The original stronger ATT v2 condition `q^(1-d/r)>=8 n^(1+epsilon)b` implies D1. At A2's r=Theta_c(d), this gives `exp(O_c(d))*poly(n,log q)`, with the same negligible false-positive upper bound already derived in R02. This is an asymptotic deterministic algorithm, not an implementation, timing claim, practical bit-security estimate, or polynomial-time attack at A2's d.

## Explicit algorithm and norm/representation check

1. Use the known subgroup H of the cyclotomic Galois group of order h=n/r. Enumerate all at-most-d-subcollections B of its r orbits on the n CRT roots. Their number is at most 2^r. Let Omega_B be the complement of the union, t=|Omega_B|, and L_B the integer ideal vanishing modulo q on Omega_B. Then t>=n(1-d/r). At least one branch has the entire true CRT support of U inside its orbit union, so A=F modulo L_B.

2. Form the integral ideal D=q L_B^(-1). Since q splits without ramification, D is the product of precisely the complementary primes above q. In particular it is unramified, is stable under H, and contains qO_K. Its basis has a polynomial-size integer coefficient representation. This uses the same branch ideals as ATT v2.

3. Compute the full stabilizer H_D by testing the n explicitly represented cyclotomic automorphisms against D. Put s=|H_D|>=h and K_D=K^(H_D). Compute the integer lattice J=D intersect K_D by solving the fixed-space equations and intersecting with D. It has rank k=[K_D:Q]=n/s<=r. BGP Section 3.2 gives the polynomial-time basis operations. Every object remains expressible in the ambient power coefficient basis; no approximation to a complex embedding is required here.

4. Run the deterministic exact SVP algorithm of Micciancio–Voulgaris Corollary 5.5 on the integer coefficient lattice J, represented by an n-by-k integer basis. Its cost is `exp(O(k))*poly(n, input bit size)`. Their Section 2 explicitly permits rectangular integer bases and restores polynomial dependence on ambient dimension and entry bit size. This distinction matters when r=O(log n).

5. Let v be the returned nonzero element. For every x in K_D, power-of-two orthogonality and repetition of subfield embeddings give

       ||Sigma_K(x)||_2 = sqrt(n) ||coeff(x)||_2,
       ||Sigma_K(x)||_2 = sqrt(s) ||Sigma_K_D(x)||_2,
       ||Sigma_K_D(x)||_2 = sqrt(k) ||coeff(x)||_2.

   Consequently the integer coefficient solver returns an exact shortest vector for the subfield canonical Euclidean norm too. Minkowski makes this a sqrt(k)-Hermite-SVP solution in J. BGP Theorem 3.2 lifts it to a sqrt(n)-Hermite-SVP solution in D. Therefore

       ||Sigma_K(v)||_2 <= sqrt(n) det(Sigma_K(D))^(1/n).

   Since the power-of-two field discriminant is n^n and N(D)=q^(n-t), dividing by q yields w=v/q in L_B^(-1) satisfying

       ||Sigma_K(w)||_2 <= n q^(-t/n).                     (D3)

6. Use BGP Corollary 4.2 with gamma_4=sqrt(n) and gamma_1=sqrt(n) q^(t/n)/(nb). D1 implies gamma_1>2gamma_4, so it decodes every promised coset A=F modulo L_B with ||Sigma_K(F)||<=nb. Verify the returned F' has integer coefficients in [-b,b] and A=F' modulo L_B; otherwise reject that branch. Accept if any branch verifies.

The last step can also be realized directly with exact coefficient arithmetic. For j=0,...,n-1, the vectors `coeff(conj(X^j w))` are independent vectors of the coefficient dual lattice of L_B: for z in L_B,

    <coeff(z), coeff(conj(X^j w))>
      = Trace(z X^j w)/n

is the integer constant coefficient of z X^j w. Their lengths equal `||Sigma_K(w)||/sqrt(n)`. The hidden coefficient error has norm at most sqrt(n)b, so every corresponding error inner product has absolute value at most

    b ||Sigma_K(w)|| <= n b q^(-t/n) < 1/2.

Rounding the n dual inner products of an integer lift of A and solving the resulting rational linear system recovers the L_B lattice point exactly on a promised branch. This supplies the error F without numerical embedding operations. The final verification controls all off-promise branches. It is permissible to add the stronger public check that A-F' has at most d active CRT coordinates if true-mask recovery is desired; D2 needs only the stated branch checks.

## Success, uniform false positives, and costs

The solver policy is deterministic and exact. Every planted input has a correct branch, and the branch's strict rounding radius proves acceptance there. No probability of recovering the hidden support is omitted: all required orbit collections are explicitly enumerated. No success probability for F03's originally unspecified randomized implementation is retroactively asserted.

For a fixed branch, uniform A modulo qO_K has a uniform image in O_K/L_B, of cardinality q^t. At most (2b+1)^n cosets contain an admissible F'. The verification rule therefore bounds acceptance by (2b+1)^n/q^t independently of off-promise decoder behavior. A union bound over the at-most-2^r branches proves D2. This is a union bound, with no multiplication of selected-stage probabilities.

Each branch uses polynomial-time ideal and linear algebra plus exact SVP in rank k<=r. Multiplication by 2^r branches leaves `exp(O(r))*poly(n,log q,log b)`. Exponential memory may be used; no polynomial-space claim is made.

## Primary sources actually checked

- Boudgoust–Gachon–Pellet-Mary, ePrint 2022/709: [Definition 2.14](https://eprint.iacr.org/2022/709.pdf#page=14), [Theorem 3.2 and Lemma 3.3](https://eprint.iacr.org/2022/709.pdf#page=16), [Section 3.2 basis computation](https://eprint.iacr.org/2022/709.pdf#page=18), [Corollary 4.2](https://eprint.iacr.org/2022/709.pdf#page=21). Theorem 3.1 supplies the original approximate-solver runtime, whereas this proposed policy uses the mathematical lifting theorem and exact low-rank SVP.
- Micciancio–Voulgaris, ECCC TR10-014 revision 1, full version: [Section 2 integer rectangular input/bit model](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download#page=7), [Theorem 5.4](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download#page=20), [Corollary 5.5 deterministic SVP](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download#page=21). The ambient dimension and input precision have polynomial cost; the exponential depends on lattice rank.
- Hanrot–Pujol–Stehle, [Theorem 1](https://perso.ens-lyon.fr/damien.stehle/downloads/bkz.pdf#page=2) and its Section 2 discussion trace the original BGP Lemma 2.11 import to exact HKZ/SVP subroutines. No numerical base probability is supplied by that conditional theorem alone. The deterministic policy above specifies a separate choice instead of inventing such a probability.

## New targeted controls for the recheck

For n=8, r=2, H={1,5,9,13} modulo 16 has order four. Its action partitions the primitive root exponents into {1,5,9,13} and {3,7,11,15}; every singleton hidden support is covered by one enumerated orbit. The full stabilizer can only decrease k below r, which improves the exact-SVP cost. This control checks that hidden support is guessed through supersupports rather than handed to the algorithm.

The strict radius is necessary for the decoding argument. Equality `n b q^(-t/n)=1/2` cannot be substituted into nearest-integer uniqueness. The proposed statement uses a strict D1, while ATT v2's factor-eight gap provides spare room. Conversely, if a returned vector were zero, it would not generate n independent dual vectors; exact SVP explicitly returns a nonzero vector.

If this new correction is not freshly checked, final wording must retain ATT v2's `p_alg-p_false` guarantee and qualify every security-ceiling claim.
