# BDD orientation of a selected prime-above lift

Status: PROVISIONAL algebraic obstruction to one proposed linear lift. This is not an impossibility theorem for all dimension changes. C's separate dimension-lift/linear-trace-repair-v1.md already identifies the complementary ideal needed for tracing short vectors back. This note records the forward BDD direction.

Let K subset L be an extension of number fields with full integer rings R_K subset R_L. Suppose a prime ideal Q of R_K splits unramified as

    Q R_L = P_1 ... P_a,    a>=2,

with distinct primes. Fix P=P_1. For x in K, its normalized valuation at every P_i equals its valuation at Q. Membership x in P^-1 requires nonnegative valuation at P_2,...,P_a. Hence v_Q(x)>=0. The same argument at all other primes gives

    P^-1 intersect K = R_K,
    (q P^-1) intersect K = q R_K

for any nonzero rational integer q. The converse inclusion is immediate. The intersection statement uses the presence of another prime above Q; it is not asserted for an inert prime of arbitrary degree.

Thus the direct field inclusion does not send qQ^-1 into qP^-1. A target T=q lambda+e with lambda in Q^-1 generally does not remain a BDD target with the same lattice point after simply embedding its coordinates into L. A proof must supply an actual target map and charge its noise, rather than only compare the norms of Q and P.

Every K-linear map from K to L has the form x -> w x. Such a map sends Q^-1 into P^-1 exactly when

    w Q^-1 R_L subset P^-1,

equivalently

    w in C := Q R_L P^-1 = P_2 ... P_a.

The same criterion holds for R_K-linear maps on Q^-1 after extending scalars. Thus a multiplication-based forward BDD lift needs an element of the SAME complementary ideal that C's trace repair requires. It is not enough to choose an arbitrary small element of P or P^-1.

For an extension of degree a in which all these primes have the same norm N(Q)=p, N(C)=p^(a-1). Any nonzero w in C therefore has |N_L(w)|>=p^(a-1) and canonical multiplication operator norm at least p^((a-1)/[L:Q]). This is only a lower bound; a sufficiently short usable w might exist. Computing one with an adequately controlled operator norm is the substantive missing algorithm in this proposed linear map. An ordinary HNF provides elements but does not certify that noise budget.

This obstruction does not rule out non-linear maps, several correlated lifted targets, different prime splitting, or additional justified sampling transformations. It prevents silently reusing the original base BDD error under direct inclusion and identifies the exact algebraic requirement for one natural repair.
