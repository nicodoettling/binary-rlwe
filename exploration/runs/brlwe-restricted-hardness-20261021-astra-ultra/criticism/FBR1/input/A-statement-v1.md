# Integral linear transfer decomposition — frozen statement v1

This statement concerns exact integral linear maps, not all possible family transfers. No computational-hardness conclusion is asserted.

Let n>=2 and m=tn be powers of two, R=Z[w]=Z[X]/(X^n+1), S=Z[z]=Z[X]/(X^m+1), w=z^t, and Pi=Tr_(Frac(S)/Frac(R))/t. Use ordinary coefficient Euclidean norms. Let I be an odd prime R-ideal, J a prime S-ideal above I, and C=IS J^-1. Let T:S->R be any nonzero Z-linear map given by an integral n by m coefficient matrix, satisfying T(J) subset I. No efficiency of constructing T is assumed.

There is a deterministic exact procedure, polynomial in n,m, the represented ideals, and the entries of T, which returns at least one of the following:

1. A nonzero a in C with

       ||a|| <= min(n ||T||_op, sqrt(n) ||T||_F).

2. A nonzero y in I with

       ||y|| <= min(n ||T||_op, sqrt(n) ||T||_F).

Here ||T||_op is the real coefficient operator norm, and ||T||_F its Frobenius norm. No numerical computation of ||T||_op is required by the procedure. For every automorphism sigma_u:w->w^u, u odd modulo 2n, define

    B_u(x)=sum_{j=0}^{n-1} sigma_u(w)^(-j) T(w^j x),
    U_u=sigma_u^-1 composed with B_u,
    a_u=sum_{r=0}^{t-1} z^(-r) U_u(z^r).

All a_u are integral, U_u(x)=Pi(a_u x), and sum_u B_u=nT. Each nonzero a_u lies in

    S intersect [sigma_u^-1(I)S J^-1].

If sigma_u^-1(I)=I, it supplies output 1. If sigma_u^-1(I) differs from I, it lies in sigma_u^-1(I)S, and any nonzero R-coefficient block of a_u, transported by sigma_u, supplies output 2. These classifications are exact and efficiently checkable from the represented ideals. If every coefficient of T has magnitude at most 2^b, the produced a_u has coefficient magnitudes at most n2^b and signed bit length at most b+ceil(log2 n)+2. Computing all components requires at most O(n^3 m) signed additions of numbers of those bit lengths, besides permutation bookkeeping and polynomial ideal-membership/equality checks.

The same algebraic decomposition and its bounds apply without the restricted-family norm condition on J. In a restricted-sampler application, additionally impose the exact same-J eligibility, recovery and width requirements; those requirements do not supply T. The theorem supplies no subroutine for finding either short outcome from I,J alone. It says that a proposed short integral map T with exact ideal containment already encodes one of the two short objects above.

Allowed elementary background: power-two cyclotomic arithmetic and its ordinary integral power basis; the perfect relative pairing Pi(ax); unique factorization of nonzero ideals; Euclidean matrix norm inequalities. The elementary module identity {a in Frac(S): Pi(aJ) subset I}=IS J^-1 may be used as background. No Gaussian estimate or probability theorem is needed for this algebraic statement.

Explicit exclusions: nonlinear maps; containment only with high probability; uncharged rejection/conditioning; rational maps without an additional integrality argument; arbitrary lattice maps with no coefficient operator-norm control; a lower bound on all algorithms; or a proof that the original hardness foundation is complete.
