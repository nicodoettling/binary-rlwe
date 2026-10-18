# Fractional padding: all fixed R-linear extraction maps, test v1

PROVISIONAL. This is a more precise test of the same R2 fractional-padding mechanism, not a hardness theorem or an obstruction to nonlinear, adaptive or class-changing reductions. No integral-only Gaussian/BDD theorem is imported onto a fractional ideal by notation.

Let n>=2 be a power of two, K=Q(zeta_(2n)), R=Z[zeta_(2n)], with coefficient Euclidean norm in the usual power basis. Let I,H be nonzero integral ideals, D_I=N(I), D_H=N(H), and let c be a positive rational integer with cR contained in I. Define

    J=IH/c,       Lambda=J^-1=c I^-1 H^-1.

Then H is contained in J, so every coefficient-binary collision in H survives in J. The ordinary class of J is [I][H]. Its coefficient covolume is D_I D_H/c^n. These identities do not establish how to sample a hard distribution of such ideals.

Fix q>=2 coprime to c D_I D_H. The planted source is k independent exact centered D_(Lambda,s) points reduced modulo qLambda and then naturally into R/qR, with the SAME public ideal/basis/parameter information in its comparator, k independent uniforms on R/qR. The rational reduction is an isomorphism because all relevant fractional ideals localize to R at primes above q. Fresh binary secrets, if subsequently introduced, are independent of this entire input law. Sampling Lambda is part of the proposed source law; no short basis/trapdoor is silently made available to an executable reduction.

Every nonzero x in Lambda obeys

    ||x||_coeff >= R0 := c/(D_I D_H)^(1/n).

Indeed xJ is a nonzero integral ideal, so |N(x)|N(J)>=1, whereas the full canonical AM-GM identity gives |N(x)|<=||x||_coeff^n. The complete centered normalizer therefore gives the previously checked shell bound: if pi(R0/s)^2>=2n log5, then planted Pr[A=0]>=1-2exp(-pi R0^2/(2s^2)), and the one-point zero test has gap at least that quantity minus q^-n. This is the actual discrete law, not a covariance surrogate. Nonzero points that reduce to zero can only increase the planted probability. Thus very small Gaussian widths do not hide a large inverse-lattice covolume in this construction.

The new extraction calculation is exact. Every R-linear map T:J->I is multiplication by some t in

    Hom_R(J,I) = I J^-1 = c H^-1.

To verify the assertion without a basis shortcut, extend an R-linear map to K by tensoring with the fraction field. Both fractional ideals become one-dimensional K-vector spaces, so the extension is multiplication by t in K. The condition tJ contained in I is exactly membership in I J^-1; invertibility of the ideals cancels I. This cancellation also shows that the extraction module contains no extra favorable dependence on the original I.

For nonzero t, the ideal (t/c)H is integral and nonzero. Hence |N(t)|>=c^n/D_H. Multiplication by t in coefficient coordinates is unitarily diagonalized by the normalized full cyclotomic Fourier matrix. Its real Euclidean operator norm is max_sigma |sigma(t)|, with the conjugate pairs carrying the same singular values. Consequently

    ||T||_(2->2) >= |N(t)|^(1/n) >= c/D_H^(1/n).

Suppose the only available output certificate is ||X||_coeff<=B_J for X in J, and the proposed transfer uses its operator-norm consequence ||TX||<=||T|| B_J. If B_J>=D_H^(1/n), EVERY nonzero fixed R-linear extraction map has certified radius at least c. But the public nonzero integer c already belongs to I and has norm c. Thus none of these operator-norm certificates supplies a search guarantee stronger than that public vector. This concerns the specified certificates, not the actual output lengths or all possible analyses of the output distribution. A map t may be selected from public data, even with advice; the pointwise inequality still applies to each selected t. Claims based on input-dependent selection, output-dependent coefficients, cancellations between multiple samples, or distribution-specific anisotropic tail bounds need their own analysis and are not excluded here.

For the favorable hypothetical C-chain scale from fractional-escape-test-v2.md, impose explicitly n>=2,k>=1,0<delta<=1,a>=1,v0>=2sqrt(n)a,q/s>=1,0<w_B<=s, and use

    d0=delta sqrt(n) w_B/(32 n k v0),
    W_J=nq/(sqrt2 d0),
    B_J=W_J sqrt(n) L_tail,       L_tail>=1.

Then W_J>=32sqrt2 n^2. If D_H<=2^(rho n),0<=rho<1, one has D_H^(1/n)<2<B_J. Therefore the obstruction applies to ALL fixed R-linear scalar extractions, improving the direct multiplication-by-c test. The extension of the BDD/DGS chain to this fractional J remains a hypothesis solely for this diagnostic; its validity, nonzero-output probability, coherent quantum access and computational hardness are not established. For an exact centered Gaussian the displayed B_J has failure bound 2n exp(-pi L_tail^2); any sampler TV error is additional. No independence of coordinates is used in that tail estimate.

Exact degree-two control: R=Z[i], I=(2+i), D_I=c=5, H=(1+i), D_H=2. Then J=((1+3i)/5)R, Lambda=((1-3i)/2)R, and Hom_R(J,I)=((5/2)(1-i))R. The shortest nonzero extraction multiplier attains norm 5/sqrt2, so using only integer clearing by 5 would not be sharp; the general lower bound is attained. Its product with the displayed generator of J is 2+i. The inverse generator has squared norm5/2, attaining R0^2. At s^2=pi/(4log2), the nine points ((1-3i)/2)(a+bi), a,b in{-1,0,1}, have exact weights1024^(-a^2-b^2). Their nonzero mass is1-(512/513)^2<1/16, while the full shell estimate is1/16. With q=17 their reductions are distinct and the uniform zero probability is1/289. This finite conditional calculation does not prove the infinite-tail or universal homomorphism claims.

The next unresolved mechanism is an extraction that uses more information than a spherical radius plus a fixed R-linear map, while preserving both source endpoints and the original binary law. No new standard computational foundation follows from the calculations here.
