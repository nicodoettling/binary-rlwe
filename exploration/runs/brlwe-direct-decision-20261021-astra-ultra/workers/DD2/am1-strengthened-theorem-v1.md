# DD2-AM1-SNF-v1: selected-root fibers averaged over distinct primes

Status: PROVISIONAL, separately frozen strengthening of coordinator DD3-AM-v1. Author DD2; not blind review. No acceptance before nonauthor and blind gates. This is a finite arithmetic statement, not a binary-RLWE reduction by itself.

Let n≥2 be a power of two and R=Z[X]/(X^n+1). Let C={0,1}^n in the coefficient basis. Let π:C→A be any fixed deterministic map to a finite set, with C_π occupied fibers. In particular π may be reduction modulo an integral full-rank ideal J, with C_π=C_J≤N(J). Fix ANY list Q of M≥1 distinct odd primes, each q≡1 mod2n and q≥Qmin>1. The map π and the list may be chosen together; the inequality below is deterministic for every such choice. For each q enumerate all n distinct roots ζ_(q,j) of X^n+1 in F_q, and put

    N_q(c,j,v) = #{b∈C: π(b)=c, b(ζ_(q,j))=v},
    K_q = 2^(-n) sum_(occupied c) max_(1≤j≤n,v∈F_q) N_q(c,j,v),
    ν = n log n / (2 M log Qmin).

Then

    (1/M) sum_(q∈Q) K_q ≤ min(1, sqrt(C_π/2^n)+sqrt(ν)).

The selected root j may depend on the entire revealed fiber c. There is one final guessed pair (j,v), not a list of guesses. No randomness, equidistribution, genericity, or independence between roots is assumed. The list need not be sampled from the primes and may depend on the chosen partition. The result does not hold with an arbitrarily q-dependent partition unless that new dependence is separately controlled: the proof sums the same pairs inside each fiber across q.

For the ideal specialization, if every q is coprime to D=N(J), one may replace ν by

    max(0, (n/2)log n − log D) / (M log Qmin)

whenever there is at least one non-singleton binary fiber. The simpler ν above avoids this optional refinement and is the designated dependency for the reduction.

Asymptotic implication: if C_π≤2^(ρ n), ρ<1 fixed, and M≥n log n/(2η² log Qmin), the displayed average is at most2^(-(1−ρ)n/2)+η. This does not make any one specified q good, nor make the average guarantee follow from a distinguisher available at one q.

Computational scope: K_q and the partition may be expensive to enumerate; the inequality is information-theoretic. Its use as a source bound must not require computing K_q. Roots can be enumerated in O(nq) modular arithmetic operations when q is polynomial in value. Degree, sample count, modulus, source family, and error law remain obligations of any downstream reduction.
