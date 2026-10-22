# CRT-PROJ-v1: fixed-modulus small-projection Gaussian flattening


Let n≥2 be a power of two, q an odd prime with q=1 mod2n, and alpha_1,...,alpha_n the distinct roots of X^n+1 in F_q. Let T be any set of h distinct roots, 1≤h≤n. Draw independent E_i from the EXACT D_(Z,sigma), sigma≥1, and write E(X)=sum_(i=0)^(n-1) E_i X^i. Let E_T=(E(alpha))_(alpha in T) in F_q^h. Then

    TV(Law(E_T), Uniform(F_q^h))
      ≤ min(1, (1/2) q^(h/2) 3^n exp(-pi sigma² q^(-2h/n))).

The bound is uniform over the selected set T. No independence of CRT coordinates is assumed. Conditional on a fixed secret s and independent uniform A, translating E_T by A_T s_T preserves this distance, even jointly with A. For k independent raw samples conditional on s, the full-batch distance is at most k times the displayed bound. If T is selected using a disjoint bank of raw samples, the same bound holds conditional on every positive-probability history and s; it need not hold when T is chosen from the very errors to which the bound is applied.

Arithmetic companion: for every nonzero centered integer vector z=(z_0,...,z_(n-1)) satisfying z_i=sum_(alpha in T) u_alpha alpha^i modq with nonzero u∈F_q^h, one has

    ||z||₂ ≥ q^(1-h/n).

Identifying-certificate companion: put r=floor(n log n/(2 log q))+1 and assume r≤n. For ANY r distinct roots, their evaluation tuple uniquely identifies a coefficient-binary element among {0,1}^n. This is injectivity, not an efficient inversion algorithm. A predictor may select the roots adaptively; a correct certificate still corresponds to at most one binary S for every fixed output.

Illustrative fixed family: q polynomial in n with q≥n^4 and sigma=n², and q bounded above by n^B for one fixed B. For h≤r-1, q^(-2h/n)≥1/n. The displayed TV is bounded by (1/2) exp((n/4)log n+n log3-pi n³), negligible against EVERY inverse polynomial. Existence/effective construction of a split prime in a suitable polynomial interval uses a separate exact imported prime theorem; no new prime theorem is asserted here.

This is a noise/certificate lemma. It does not remove A-FRAC's sample-dependent completion width, prove FF, classify a new source radius, or establish hardness.
