# Proof of SV-SPARSE-ACQ-v1

Enumerate supports of sizes j=1,...,min(h,n) and coefficients in{-B,...,-1,1,...,B}. The number is sum_j binom(n,j)(2B)^j<=sum_j binom(h,j)(2nB)^j=(1+2nB)^h; alternatively the crude ordered-slot encoding by h slots, each empty or one of2nB signed coordinate/value choices, directly gives this bound. Duplicates may be removed or retained. For each vector f, exact rational inversion tests A^-1 f integral, which is equivalent to f in J. At least one promised member appears. All arithmetic has polynomial bit lengths in A,n,B; h is fixed. No integer factorization or short-basis acquisition is hidden in this enumeration.

For any recovered f and lambda in J^-1, f lambda is integral. Parseval and the convolution/Cauchy-Schwarz inequality give ||fw||_coef,2<=||w||_canonical,infinity ||f||_coef,2<=r sqrt(h)B<1/2. Hence every coefficient of fT rounds uniquely to f lambda. Nonzero f is invertible in the cyclotomic field, so exact division recovers lambda. This is the existing short-member decoder with an explicit acquisition algorithm and a charged enumeration bound, not an inference of an algorithm from mere existence.

For the explicit family, write theta for the image of X in Z[X]/(X^2-X-1). This quadratic ring is free of rank2 over Z, theta is a unit with theta^-1=theta-1, and its conjugate is -theta^-1. Since n/2 is even for n>=4, theta^(n/2)+theta^(-n/2)=L_(n/2). Therefore

    theta^n+1=theta^(n/2) L_(n/2).

The factor theta^(n/2) is a unit. Thus the quotient by theta^n+1 is the quotient by the ordinary integer L_(n/2), with additive group(Z/L_(n/2))^2. Swapping the order of the two polynomial quotient operations identifies it exactly with R/fR. This proves both exponent and norm claims, with no prime assumption on the Lucas value.

Let phi=(1+sqrt5)/2. For even j, L_j=phi^j+phi^-j, so log2 L_(n/2)^2/n tends to log2 phi<1. Every stated rho above that limit gives eventual eligibility. The exponent grows exponentially. Under an inverse-polynomial inherited radius the product e*r tends to infinity, so the scalar sufficient guard eventually fails. The sparse witness has squared norm3 and is found by h3,B1 enumeration from any basis. Since r<1/(4sqrt n),12r²<3/(4n)<1. No claim is made about the stronger subfield or code decoders on this family, only the explicit separation from scalar quotient-exponent rounding and the availability of the sparse acquisition method.
