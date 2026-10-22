# Definitions and permitted sources

D_(L,s) assigns mass proportional to exp(-pi*||x||_2^2/s^2) to x in L. Coefficient norms and negacyclic T use basis 1,X,...,X^(n-1); canonical infinity is the maximum absolute embedding value. TV is one half the L1 distance. The supplied SV-SUBFIELD-v2 statement may be used as a dependency theorem; inspect its stated hypotheses. No status or proof is supplied.

Primary sources permitted: Milne, Algebraic Number Theory, https://www.jmilne.org/math/CourseNotes/ANT.pdf (ideal extension/contraction, unramified descent and norms); Kannan-Bachem https://epubs.siam.org/doi/abs/10.1137/0208040 (polynomial normal forms; distinguish abstract from full-paper access); Xylouris effective Linnik theorem https://www.impan.pl/shop/en/publication/transaction/download/product/83078 (a fixed exponent6 suffices). Basic finite-dimensional linear algebra, Fourier diagonalization of T, Poisson summation for Gaussians, elementary probability, and exact integer arithmetic are permitted.

Actual source-radius definition for comparisons: K>=1, ell=ceil log2(2nK), sigma_floor=8*n^2*ceil(sqrt(K*n))*ell^4, Qmin>=n*sigma_floor, Qmax>=Qmin, chi>=1, 0<epsilon<=1, r=epsilon*ell^2/(1024*n*K*chi*Qmax). These hypotheses imply r<1/(4sqrt(n)); verify if used. No new reduction is assumed.

Boundary cases for review: n=2 versus n>=4; weights0,1,n-1,n; singular covariance; retained versus hidden S; non-Gaussian rare tails; non-coprime q and D; nonscalar ideal bases; fixed S across repeated samples versus fresh S; rho=0; ramified subfield contraction; polynomial numeric index versus polynomial bit length. No proof or result of any prior review is provided.
