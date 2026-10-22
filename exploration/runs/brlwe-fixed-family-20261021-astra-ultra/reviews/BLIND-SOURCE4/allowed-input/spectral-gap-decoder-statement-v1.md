# SV-GAP-DECODE-v1: prime-exponent source decoding from a spectral gap

Let n>=2 be a power of two, and let an integral ideal J in R=Z[X]/(X^n+1) be supplied by an ordinary integer basis. Assume its additive quotient exponent is a completely split odd prime p, and J is neither R nor pR. For a primitive2n-th root alpha in F_p, let T_alpha be the nonempty proper subset of indices j in Z/nZ for which every element of J vanishes at alpha^(2j+1). Write t=|T_alpha|, so N(J)=p^t. Let g_alpha be the largest positive cyclic gap between consecutive elements of T_alpha, with gap n for a singleton. Let g_max be the maximum g_alpha over all primitive roots alpha. These quantities and a maximizing root/interval are deterministically computable in time polynomial in n, NUMERIC p and full input lengths, without a supplied factorization of J.

For rational T=lambda+w with lambda in J^-1 and canonical infinity error at most rational r, a deterministic algorithm recovers lambda whenever

    r<1/2 and 8*p^2*r^2 < g_max.

The algorithm uses the same coefficient rounding and explicit finite-field linear system as SV-RS-DECODE-v1, now with a containing Reed–Solomon code of dimension n-g_max+1. In particular

    g_max >= ceil(n/t).

For eligible ideals p^t<=2^(rho*n), 0<rho<1, the simpler sufficient condition

    r<1/2 and 8*p^2*r^2 < log2(p)/rho

therefore guarantees recovery. This applies to arbitrary split-prime support, not just a bounded number of factors or a consecutive interval. Substitute the actual inherited DD r exactly; no Gaussian-sampling reversal is used. Polynomial numeric p gives polynomial runtime.

The bound improves the scalar-rounding sufficient guard in a structural regime but is not a complete classification, and failure of the bound is not hardness. A large cyclic gap is sufficient, not necessary. Optimizing over primitive roots is a polynomial search, not advice about the unknown target lambda.
