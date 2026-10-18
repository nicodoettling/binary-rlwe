# Proof of the integral binary-collision class count, v1

PROVISIONAL. All norms of ideals are absolute integer indices. Algebraic field norms are absolute values where appropriate.

1. Collision criterion. A collision between distinct coefficient-binary vectors s,s' is exactly a nonzero z=s-s' in J with all coefficients in {-1,0,1}. Conversely every such z is the difference of two binary vectors, by assigning positive and negative coordinates to separate vectors. There are exactly3^n-1 possible nonzero z. Irreducibility of X^n+1 over Q ensures each is a nonzero field element.

2. Norm bound. The canonical embedding matrix E satisfies E*E=nI. By AM-GM on the n squared embedding moduli,

    |N_K/Q(z)| <= (sum_j |sigma_j(z)|^2/n)^(n/2)
                = ||z||_coeff^n <= n^(n/2)=B_n.

This uses the complete canonical embedding including both conjugates. No assertion that all embeddings individually have magnitude at most sqrt(n) is needed.

3. Prime ideal norms. If a prime ideal P lies over an odd prime p and has residue degree f, the image of zeta in the residue field has exact order2n: its nth power is -1, which is not1 in odd characteristic, and2n is a power of two. Thus2n divides p^f-1 and N(P)=p^f>=2n+1. Above2 there is exactly one prime P_2 of norm2. Indeed R/(2)=F_2[X]/((X+1)^n) has exactly one prime quotient F_2. Unique ideal factorization in the ring of integers then gives the required decomposition for every principal integral ideal.

4. Divisor count. Factor (z)=P_2^a product_(P!=P_2) P^e_P. Since its norm is at most B_n, a<=log_2 B_n=v_n. Put Omega=sum_(P!=P_2)e_P. The preceding lower bound on unramified prime norms gives (2n+1)^Omega<=B_n and hence Omega<=u_n. The exact number of integral ideal divisors of (z) is

    (a+1) product_(P!=P_2)(e_P+1)
       <= (v_n+1) 2^Omega <= M_n,

using e+1<=2^e for every integer e>=1. Ramification at2 is counted once, not as n independent prime factors. Multiple odd primes or different residue degrees create no additional omitted factor: the product already ranges over prime ideals.

If z belongs to an integral ideal J, then (z) is contained in J, which means J divides (z) as an integral ideal. Thus every ideal relevant to C_n occurs among the divisors of at least one of these3^n-1 principal ideals. Counting ideals first and then their classes yields |C_n|<=(3^n-1)M_n. Overcounting the same ideal or class is harmless. No distribution on generators or divisors is introduced.

5. Asymptotics. Since log B_n=(n/2)log n, one has u_n<=n/2 and v_n=O(n log n). Therefore log((3^n-1)M_n)<=n log3+(n/2)log2+O(log n). The independently accepted bound log h_n>=(1/4+o(1))n log n gives the displayed fraction. No effective threshold follows from that analytic dependency. This is the same unconditional normal-field Brauer-Siegel/class-number argument as the frozen dependency; no real-class-number-one assumption or GRH is added.

6. Proof-only guessing. For a fixed integral J whose binary quotient map is injective, the sets J+s over s in{0,1}^n are pairwise disjoint. Any realization y=G+S belongs to exactly one of them, so S is a deterministic function of y (and J). This holds for any probability masses on J, including zero masses and non-Gaussian laws. Since there are finitely many secrets, a measurable decoder exists; efficiency is not asserted. Conditional public information does not change the proof when the stated conditional independence and fixed support hold. No sequential product, posterior factorization or restored-independence assertion occurs.

7. Finite falsification plan and scope. Enumerate every ternary polynomial for n=2,4,8, compute its exact algebraic norm by recursive relative norms and check selected cases by independent integer determinants. For each norm, factor its integer value and use residue degrees ord_(2n)(p) to bound the total odd prime-ideal multiplicity. Verify exact divisibility of valuations by residue degree, (2n+1)^Omega<=|N(z)|, and the divisor upper bound. This can falsify a finite algebraic/counting error; it cannot certify class-number asymptotics. In degree2, z=1+i has norm2 and exactly two ideal divisors R and(1+i), showing why the ramified factor is necessary. The theorem leaves fractional ideals and class-changing normalization open, and it proves no computational hardness.
