# Integral ideal classes admitting binary collisions, theorem v1

PROVISIONAL. No new result is accepted until exact full-proof, source/parameter, fresh blind, regression and artifact gates close. This is a scoped obstruction to a same-class integral completion interface, not computational hardness or a general reduction barrier.

For n>=2 a power of two, let K=Q(zeta_(2n)), R=Z[zeta_(2n)], and Cl(R) the ordinary ideal class group with order h_n. Write

    B_n=n^(n/2),
    v_n=(n/2) log_2 n,
    u_n=floor(log_(2n+1) B_n),
    M_n=(v_n+1) 2^u_n.

The two exponents v_n,u_n are nonnegative integers. Let C_n be the set of ideal classes containing at least one nonzero INTEGRAL ideal J for which the coefficient map {0,1}^n -> R/J is not injective. Then the following finite bound holds:

    |C_n| <= (3^n-1) M_n.

There is no bound on N(J) in this definition. Consequently, using the unconditional power-two cyclotomic class-number lower bound log h_n >= (1/4+o(1)) n log n established in the accepted ROOT-SAMECLASS-v1 proof,

    |C_n|/h_n <= exp(-(1/4+o(1)) n log n).

The asymptotic statement has no effective starting n. It is a fraction under the uniform law on the finite ordinary class group, not a sampling algorithm or a statement about uniform CRT-root sets.

For every class outside C_n, every integral representative J in that class, every independent uniform coefficient-binary secret S, and EVERY probability distribution of G supported on J, observing G+S determines S exactly. Thus its optimal posterior guessing probability is one. The same statement holds conditionally on public information when J and the full law of G are fixed and G remains independent of S. A Gaussian shape change cannot alter this support fact.

The observation G+S is proof-only in the intended application: this conclusion does not supply a public attack on binary RLWE. Multiplication by a nonzero field element preserves the ideal class, so same-class normalization to an integral representative cannot avoid this obstruction on the excluded classes. Fractional representatives, class-changing maps, field/dimension changes, computational-only simulations, other proof exposures and different source mechanisms are outside the claim.

Full proof: proof-v1.md. The analytic class-number dependency is the exact accepted proof coordinator/same-class-count-proof-v1.md, SHA256 bf625ccfa90a819c6b36639850a4cf2ab021c865cf3e84b67bc984cb3469d733, with its full/source/blind reviews linked in claims.json. This theorem does not inherit acceptance from that dependency.
