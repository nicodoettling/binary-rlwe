# F03 attack inventory for the entire source pair

Investigator derivations, 2026-09-06; provisional pending nonauthor review. No experiments run. The source is SC0 with a hidden d-active CRT support T and public (A,C)=(U+F,V+H). A is already sufficient to break a proposed pair assumption whenever a marginal test succeeds. Conversely, safe-looking marginals do not establish pair pseudorandomness.

## A1. Support and noise enumeration

If coefficient perturbations lie in sets E_F,E_H of cardinalities s_F,s_H, all possible planted pairs lie in a set of size at most

    binom(n,d) (q-1)^d q^d s_F^n s_H^n.

The same upper bound works with arbitrary correlations between F and H, provided the two coefficient-support bounds hold. Consequently an unbounded support-membership test accepts uniform input with probability at most

    binom(n,d) q^(2d) (s_F s_H/q^2)^n.

Truncated Gaussian tails are charged separately. This is an information-theoretic distinction, not a polynomial-time algorithm. Merely enumerating T costs binom(n,d), and even a known T leaves a bounded-distance decoding problem. Exhaustive ideal-value enumeration adds q^d per point. At d=Theta(n/log^3 n), neither is polynomial. Rich supports eliminate the old polynomial-sized support family; they do not eliminate decoding.

## A2. A structured-support enumeration attack that also applies to arbitrary T

The following is an elementary combination of the primary algorithms in [Boudgoust–Gachon–Pellet-Mary, 2022/709](https://eprint.iacr.org/2022/709.pdf), Theorem 3.1 and Corollary 4.2. It is a deduction here, not claimed as a theorem stated in that paper or as novel.

**Finite setting.** Suppose 1<=d<=n/2 and the centered coefficients of F satisfy |F_j|<=b, where b>=1. Let r divide n, be a power of two, and satisfy 2d<=r<=n. Fix epsilon>0. A sufficient condition for the attack below is

    q^(1-d/r) >= 8 n^(1+epsilon) b.                 (A2.1)

There is an attack on the A marginal with runtime exp(O(r/epsilon))*poly(n,log q), planted acceptance one, and uniform acceptance at most

    2^r (2b+1)^n / q^(n(1-d/r)).                 (A2.2)

For a noise tail delta_F outside the coefficient box, planted acceptance is at least 1-delta_F. Thus for fixed epsilon, r=Theta(d), polynomial q,b, and (A2.1), the algorithm runs in exp(O(d))*poly(n,log q). In particular it is polynomial when d=O(log n). The principal d=Theta(n/log^3 n) regime is not broken in polynomial time by this bound.

**Algorithm and proof.** The Galois group of the 2n-th cyclotomic has order n and contains a subgroup H of order h=n/r. Its action on fully split prime ideals, equivalently the CRT roots, is regular; H partitions the n roots into r orbits of size h. The true T meets at most d orbits. Enumerate all sets B of at most d such orbits; there are at most 2^r choices. Put Omega_B equal to the complement of their union. Then |Omega_B|>=n-hd, and for at least one B the true U is zero at every root in Omega_B.

Let L_B be the full integer ideal defined by vanishing modulo q at Omega_B. It is known to the algorithm, invariant under H, has norm q^|Omega_B|, and contains qR. On the correct branch,

    A mod L_B = F mod L_B.

The canonical norm of F is at most B_can=nb, since power-of-two canonical embedding multiplies the coefficient Euclidean norm by sqrt(n). This is PV-Knap for a known ideal. Its Hermite-BDD parameter is

    gamma_1 = sqrt(n) q^(|Omega_B|/n) / B_can.

Choose gamma_4=gamma_1/4. Corollary 4.2 reduces the BDD task to gamma_4-Hermite-SVP in L_B^(-1), since gamma_1>2gamma_4. The inverse is a scalar multiple of an integral complementary ideal, is unramified, and is invariant under H. Condition (A2.1) gives gamma_4>=2 n^epsilon sqrt(n), so Theorem 3.1 applies. With stabilizer size at least h, its runtime exponent is at most

    O(n log(n)/(h log(gamma_4/sqrt(h)))) = O(r/epsilon).

Theorem 3.1 accepts explicit polynomial-size field, automorphism and ideal bases, all available here. Scaling the fractional inverse to an integral ideal does not change its Hermite approximation factor. Run the returned BDD procedure on A mod L_B, then verify the congruence and the coefficient bound |F'_j|<=b. On a uniform input A, the coset A mod L_B is uniform among q^|Omega_B| possibilities. At most (2b+1)^n cosets contain a verified small F', regardless of the behavior of the decoder off its promise. A union bound over B proves (A2.2). Under (A2.1), that bound is negligible: (2b+1)/(8n^(1+epsilon)b)<=3/(8n^(1+epsilon)).

**Parameter reading.** For q approximately n^K, b approximately n^a, and r approximately C d, the strict sufficient margin is K(1-1/C)>1+a. It is not supplied by q/b>1 alone. Gaussian F of coefficient width gamma can use b=ceil(gamma log n) with negligible tail for polynomial n,gamma. If d is not a power of two, choose r the next power of two above a fixed constant multiple of d; this changes only constants when r<=n. Randomness of T is unnecessary for this attack.

**Why this matters.** A random T usually lacks a large exact stabilizer, but it is contained in the union of a small number of subgroup orbits. Coarsening the hidden support lets the attacker enumerate structured *super-supports*. This pays exp(O(d)), retains a large known zero set, and then invokes the known decoding attack. No inference of hardness is made when this runtime is superpolynomial.

## A3. Block/code decoding controls

For the retired binomial family J=(X^(n/L)-a), coefficient blocks of ideal points are scalar multiples of a known geometric vector. Enumerating the scalar and the polynomially many a values gives the prior polynomial attack; one block has uniform false acceptance at most q(s/q)^L. This remains a mandatory control, even if F/H are correlated.

For consecutive frequency sets and sparse coefficient corruption, Reed–Solomon-type decoding can apply. Dense small integer Gaussian perturbations are not sparse Hamming errors: a claim that a coding decoder handles them needs an explicit metric and radius. For a general known T, A mod the inactive-support ideal is a PV-Knap/BDD target. The BGP22 algorithms exploit automorphism stabilizers and can discard constraints to obtain a stable subideal; their random-support experiments are concrete algorithm evidence, not a worst-case hardness theorem. The new A2 enumeration is one way to account for *hidden* T without pretending it is public.

## A4. Short multipliers and short rational representations

Every w in J_T kills both U and V, so

    wA=wF,     wC=wH mod q.

If w is known, short, and these two products are small compared with q, a public residual test can distinguish. An exposed small denominator or a polynomial-size family of denominators is therefore dangerous. For hidden general T, the task is to find such a w from A,C; that is an additional lattice/decoding problem, not a freely available operation.

An elementary existence fact emphasizes the attack surface: if 2^n>q^d, two binary coefficient vectors have the same residue modulo J_T, so a nonzero ternary w lies in J_T. This existential statement gives no efficient way to find w. A general search can use the lattice

    L_(A,C)={(w,z1,z2) in Z^(3n): z1=wA mod q, z2=wC mod q},

with coordinate weights selected for the expected sizes. Its determinant is q^(2n). The planted w produces an unusually short candidate when F,H are narrow; lattice reduction must be assessed at this joint dimension and the actual noise law.

For a *fixed* w of multiplication rank rho over F_q, uniform wA,wC are independent uniform points in its rho-dimensional image. One may select rho linearly independent coefficient positions, so requiring each product coefficient in a box of size s has probability at most (s/q)^(2rho). Charging only q^(-2n) would incorrectly treat a nonunit multiplier as invertible. For nonzero ternary w, the integer field norm satisfies |Norm(w)|<=n^(n/2), while each vanishing CRT coordinate contributes a factor q; hence rho>=n-n log(n)/(2 log(q)). This is at least n/2 for q>n. These statements aid a finite candidate-family union bound; they do not supply the candidate family.

## A5. Pair combinations and completion correlations

For a known scalar t, C-tA=(V-tU)+(H-tF). Conditional on T,U,F,H, V-tU is uniform in I_T. This combination can expose a much narrower residual if H is close to tF. An adversary can enumerate polynomially many scalar or short polynomial t values and test all resulting combinations. Conversely, if H=H0+tF was introduced by the public shear proved in F03.md, applying the inverse shear simply returns the base source. It is not automatically a new attack.

At each active CRT coordinate, V_i/U_i is uniform in F_q. One scalar cancels all active coordinates with probability q^(1-d), averaged over V,U, because all d ratios must agree; guessing an arbitrary ring multiplier has q^d relevant active values. Do not replace V by a single globally proportional point. More general short relations P U+Q V=0 can be sought in a ring-module lattice; the responses then become P F+Q H. This attack uses the entire pair and can exploit covariance or common-factor structure invisible in either marginal.

Completion should also be checked through low-degree polynomial combinations, empirical CRT histograms and Fourier coefficients of the pair. The targeted primary search found a relevant precedent: [Agrawal–Pellet-Mary 2020/415](https://eprint.iacr.org/2020/415.pdf), Definition 4.1 and Lemma 4.3, breaks a different correlated-noise RLWE source using four pairs and a product of 2-by-2 determinants when q grows sufficiently faster than (n sigma)^8. Its reciprocal small denominators and shared secrets differ from SC0, so that lemma is not an attack on the present two-element challenge. It is a concrete reason to analyze actual polynomial correlations, not marginal widths alone.

## A6. Exact character identity for a tractable subclass

Assume F,H are independent of U,V conditional on T (they may be jointly correlated with each other). Write chi_a(x)=exp(2pi i<a,ev(x)>/q), so a denotes a character in CRT coordinates. Then the active-unit source has

    E[chi_a(A) chi_b(C)]
      = E_T[ 1_{b|T=0} prod_(i in T) c(a_i)
              E[chi_a(F)chi_b(H)|T] ],

where c(0)=1 and c(t)=-1/(q-1) for nonzero t. This follows by summing a nontrivial character over F_q^*. For unconditioned uniform U, the product is replaced by 1_{a|T=0}. Thus joint noise Fourier mass and the shared support enter together. This factorization is invalid if K depends on U; then the U-character must stay inside the conditional expectation. Identifying an efficiently computable character with inverse-polynomial bias is an attack criterion; failing to identify one is not evidence of hardness.
