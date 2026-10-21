# SFUNC-v2 proof

The exact joint mass of (S,Y) is 2^-n 1_(y-b in J)rho_t(y-b)/rho_t(J). Optimizing one success event for every observed y gives

    p_selected=[2^n rho_t(J)]^-1 sum_c sum_(y in c+J)
                 max_(j,v) sum_(b modJ=c,F_j(b)=v) rho_t(y-b).

All sums are of nonnegative terms, and randomization cannot improve the pointwise maximum. Put u=(1/2,...,1/2), a=sqrt(t^2+r0). Completing the square gives rho_t(y-b)<=exp(pi*n/(4r0))*rho_a(y-u) for every cube b. The selected inner sum has at most max_(j,v)N(c,j,v) terms. Sum the common envelope over c+J, then apply the centered theta maximum rho_a(J+x)<=rho_a(J), which follows from Poisson summation and the triangle inequality. A second exact Poisson identity gives

    rho_a(J)/rho_t(J)=(a/t)^n *rho_(1/a)(J*)/rho_(1/t)(J*)<=(a/t)^n.

The final inequality is termwise because a>=t, with both positive normalizers retained. This proves the upper bound and its trivial cap1. The residue c reveals S modJ, under which S is uniform inside its occupied fiber. The optimal residue-only strategy chooses its largest functional bin and has success K_F, proving the lower bound for the defined optimum. Using log(1+x)<=x at r0=t gives the displayed overhead. Conditional revelation is valid only with the stated product law intact. This is the cube envelope/normalizer mechanism inherited from RECENT/workers/B/proof-v1.md, with a new selected-function bin count.
