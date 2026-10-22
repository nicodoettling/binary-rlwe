# BOUNDED-AFFINE-TV-v1

Let n>=4 be a power of two, and let M_s be the real coefficient matrix for multiplication by s in R_R=R[X]/(X^n+1). Let S be uniform in {0,1}^n. The finite-second-moment random pair (Delta,Z) is independent of S; its two components may be arbitrarily dependent. Put W_s=Z-M_s Delta. Let Y have one common distribution, independent of S. Suppose ||W_s||_2<=R and ||Y||_2<=R almost surely for every s, for a real R>0. Then

    TV( Law(S,W_S), Law(S,Y) ) >= E||Delta||_2^2 / (n^3 R^2).

More generally, if S is uniform on a weight-w slice, 2<=w<=n-2, and the same independence and bounds hold on that slice, the lower bound is

    4 p_w E||Delta||_2^2 / (n^3 R^2),
    p_w=4*w*(w-1)*(n-w)*(n-w-1)/(n*(n-1)*(n-2)*(n-3)).

There is also a tail-explicit version without the almost-sure bounds. Suppose Y has finite second moment, and define eta_s=E[||W_s||_2^2 1_{||W_s||_2>R}], eta_Y=E[||Y||_2^2 1_{||Y||_2>R}]. The uniform-cube lower bound becomes

    [ E||Delta||_2^2/n^3 - E_S eta_S - eta_Y ] / R^2.

For the slice replace the first numerator by4 p_w E||Delta||_2^2/n^3. A negative bound has no force.

For an integer modulus q, suppose additionally W_s is integer-valued and bounded by R<q/2. Let Y_G have independent coefficient D_(Z,sigma) errors and tau=Pr(||Y_G||_2>R). Then the retained-S law modulo q satisfies

    TV( Law(S,W_S modq), Law(S,Y_G modq) )
       >= E||Delta||_2^2/(n^3 R^2) - tau,

with the same slice replacement. The finite conditioning used here is on the full coefficient-norm ball, not separate coordinate events.

This concerns secret-independent additive residual perturbations of the displayed form, including non-Gaussian pairs. It does not cover a kernel whose joint (Delta,Z) law depends on s, arbitrary nonlinear transfer, or a comparison that discards S. Inverse-polynomial moment and polynomial R give an inverse-polynomial retained-secret mismatch when the tail is smaller; this is not an impossibility theorem for all fixed-family reductions.
