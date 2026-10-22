# SV-RS-ACTUAL-v1: a nonempty inherited-radius regime beyond scalar rounding

Provisional parameter corollary of SV-RS-DECODE-v1 and SV-DENSE-SPLIT-v1; exact-version review required. It is not a new FF theorem.

Fix 0<rho<1 and any sufficiently large polynomial-value parameter family satisfying the accepted FIXED-MAIN-v2 / AM-MAIN-v3 guards, with its master auxiliary list fixed independently of J. Choose the common C8 integer kappa uniformly large enough for all 1<=D<=2^(rho*n), hence common Q_*, epsilon_C and lower ceiling a. The inherited theorem permits an explicitly charged integer chi>=a, not only its minimal corollary choice chi=a.

Put C=epsilon_*ell^2/(1024*n*K*Qmax), a positive represented rational. Choose a polynomial-value split prime p>Qmax with p>=n^4 and C*p>a+1, effectively by the same primary-source split-prime construction used for the auxiliary list. Let t be the largest positive odd integer at most floor(rho*n/log2(p)), and form the consecutive-support ideal J of SV-DENSE-SPLIT-v1. Set chi=ceil(C*p), and use the ACTUAL delivered radius r=C/chi.

For all sufficiently large n, this is an eligible ordinary-basis source with exponential norm, exponent p and trivial stabilizer. All quantities have polynomial value or charged polynomial bit length as appropriate. It satisfies

    1/2 < p*r <= 1,    8*p^2*r^2 <= 8 < n-t+1.

Thus the scalar-rounding sufficient guard 2pr<1 fails, whereas the direct RS decoder succeeds at this exact delivered radius. The best feasible standard-subfield contraction has exponential value p^t; via SV-ALL-SUBFIELDS-v1 the same is true of the best arbitrary-subfield collision index. These are failures of sufficient criteria, not hardness assertions. The choice of a larger chi is explicit: this corollary does not assert the same conclusion for the minimal chi=a radius.
