# SV-ALL-SUBFIELDS-v1: the standard chain captures polynomial contraction criteria

Provisional author candidate; full and fresh blind review required.

Let n>=2 be a power of two, K_n=Q(zeta_(2n)), R_n=Z[zeta_(2n)], and J_o a nonzero integral ideal. For ANY subfield L of K_n, write g=[L:Q] and d_L=[O_L:J_o intersect O_L], where O_L=R_n intersect L. Let m=min(2g,n). Then m is a power of two, m>=2, L is contained in the standard cyclotomic subfield K_m=Q(X^(n/m)), and

    d_m=[R_m:J_o intersect R_m] <= d_L^[K_m:L] <= d_L^2.

If d_L<2^g, then d_m<2^m. Consequently the minimum feasible standard-chain contraction d_* of SV-SUBFIELD-v2 is at most d_L^2 for every such L. If d_all denotes the minimum d_L over ALL subfields satisfying d_L<2^[L:Q], then

    d_all <= d_* <= d_all^2.

The feasible sets are nonempty whenever N(J_o)<2^n. Therefore polynomial numeric feasible contraction in ANY subfield is equivalent to polynomial numeric feasible contraction in the displayed standard cyclotomic chain. Passing to arbitrary subfields cannot yield an asymptotically new polynomial-time family for this particular binary-collision criterion. This does not rule out other algorithms, other short-member constructions, or a better finite running time from another subfield.

All subfields can in fact be enumerated by enumerating pairs of automorphisms, taking their generated subgroups, and deduplicating: every subgroup of (Z/(2n)Z)^* has at most two generators. Their integral invariant bases and d_L are computable by signed permutations and exact normal forms in polynomial bit complexity in n and the ordinary input basis encoding. This statement does not require executing that larger enumeration to attain the polynomial-family criterion.
