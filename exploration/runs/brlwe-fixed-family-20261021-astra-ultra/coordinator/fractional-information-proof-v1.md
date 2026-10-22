# FRAC-INFO-v1 author proof

Use coefficient inner product <x,y>=Tr(x conjugate(y))/n. R is self-dual for this pairing, so Lambda^*=conjugate(J) is a sublattice Gamma of Z^n. Equivalently Lambda contains Z^n and its Euclidean dual is integral; the latter inclusion alone suffices below.

Fix distinct b,c in the binary cube and d=c-b. Pick j with d_j nonzero (hence +/-1, nonzero modq). The additive character A -> exp(2pi i (A*d)_j/q) on R/qR is nontrivial, since its value at A=1 is not1. Pull it back through Lambda/qLambda. Every character of this finite lattice quotient is represented by y in q^-1 Gamma/Gamma; nontriviality means y not in Gamma. Since Gamma is integral, every vector in Gamma-y is a nonzero vector of q^-1 Z^n, so dist(y,Gamma)>=1/q.

Poisson summation with all normalizers retained gives

    phi_A(d,j) = E exp(2pi i (A*d)_j/q)
               = sum_(z in Gamma) exp(-pi*s^2*||z-y||^2)
                 / sum_(z in Gamma) exp(-pi*s^2*||z||^2).

It is real and nonnegative. Split each numerator term into two equal Gaussian factors. The first is at most exp(-pi*s^2/(2q^2)). The remaining shifted theta sum is at most its unshifted value: Poisson summation on Gamma shows the latter dominates each shifted value because its dual coefficients are positive and cosines <=1. The denominator is >=1. Finally Gamma subset Z^n yields

    0<=phi_A(d,j)<=exp(-pi*s^2/(2q^2))*rho_(sqrt(2)/s)(Gamma)
                 <=exp(-pi*s^2/(2q^2))*U(s,n).

For a coefficient E_j from D_(Z,sigma), Poisson summation similarly yields

    phi_E(1/q)=sum_m exp(-pi*sigma^2*(m-1/q)^2)
               /sum_m exp(-pi*sigma^2*m^2) >= gamma>0.

Consider the complex-valued observable F_b(A,B)=exp(2pi i (B-A*b)_j/q), of absolute value1. Under P_b its expectation is phi_E; under P_c it is phi_E*phi_A(d,j). Thus their expectation difference is at least gamma*mu. For any |F|<=1, the absolute expectation difference is <=2TV, proving TV>=delta. The statistic may depend on the candidate pair; it is used only to bound pairwise separation.

For finite probability laws, their Bhattacharyya affinity BC=sum_x sqrt(P_b(x)P_c(x)) satisfies TV<=sqrt(1-BC^2). Hence BC<=sqrt(1-delta^2)<=exp(-delta^2/2). Conditional on any fixed S=b the K samples are iid; their affinity against c is BC^K. Under b, Markov's inequality applied to sqrt(P_c^K/P_b^K) bounds the event P_c^K>=P_b^K by BC^K. Full support makes these likelihood ratios well-defined. A union bound over the 2^n-1 other secrets gives the stated per-secret maximum-likelihood error. There is no averaging of conditional success products or conditioning on future success; iid is used only after the true secret is fixed.

For the fixed-family corollary, q has fixed polynomial value, K=nq^4 and ell=Theta(log n), hence s^2=Theta((log n)^4) and s/q tends to0. The scalar tail sum in U is 1+O(exp(-pi*s^2/2)); consequently U=1+exp(-Omega((log n)^4)), with n absorbed. This error is o(s^2/q^2) for every fixed B. Taylor expansion, or 1-exp(-x)>=x/2 for sufficiently small x>0, gives mu=Theta(s^2/q^2). Since sigma=n^2 and q>=n^4, gamma tends to1 and is bounded below by an absolute positive constant. Therefore K*delta^2=Omega(n*s^4)=Omega(n*(log n)^8), dominating n log2. These estimates use a fixed B; they do not silently choose target exponents after an adversary.

This provides no computationally efficient ML algorithm. In particular its success cannot be used to claim an RLWE attack, and no source hardness is concluded from this diagnostic. What fails is an attempted sample-exponent-independent statistical ignorance bound for this exact fractional experiment.
