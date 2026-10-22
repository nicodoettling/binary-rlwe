# FIXED-MAIN-v2 proof

PROVISIONAL; binds fixed-main-statement-v2.md, AM-MAIN-v3 and MR-v1 exact definitions. The new work in this composition is an explicit finite-law transfer; inherited hidden-center/periodic-Gaussian decoding is used through its recorded exact interface.

For each auxiliary prime q in Q0, apply MR-v1 with its large modulus Q=q, small modulus q=q0, sample count k=k0, and target width sigma=sigma0. Its source width is exactly sigma_q=(q/q0)*sigma0, as specified in the auxiliary target. The guards imply q>=Qmin>=q0, sigma0>=1, and a signed-gap change at most epsilon_*/4. Thus every auxiliary signed gap has the SAME orientation as the fixed-target gap and magnitude at least3epsilon_*/4. Averaging over the fixed master list retains that orientation and magnitude. In particular the required AM-MAIN-v3 global signed gap premise with epsilon0=epsilon_*/2 holds. No conditioning on a favorable secret, public multiplier or modulus is involved.

Both endpoint laws retain the same public multiplier distribution and metadata in their respective comparisons. MR's Gaussian comparison is conditional on the full public bank and the one shared S, and its final bound is on the entire batch. Thus no marginal per-sample conclusion is promoted to a shared-secret joint law. Continuous Gaussians occur only inside a coupling proof; the actual finite Q and q0 experiments in the theorem both use coefficient discrete Gaussians. The transformed law is only statistically close to the exact target, and the full two-endpoint loss is explicitly paid before invoking the decision advantage.

The width lower guard at Qmin gives sigma_q>=sigma_floor for every master prime; q0>=n*sigma0 gives sigma_q<=q/n. Also Qmin>=n*sigma_floor is explicitly assumed. AM-MAIN-v3 permits precisely these widths and uses the SAME specified width in each exact target completion and finite executable wrapper. Its latent convolution/smoothing proof is uniform over widths above the floor. Its finite scalar sampler changes the proposal interval with sigma_q but leaves the number of trials and common cap counts unchanged, charging the larger integer encodings. Therefore there is no unproved equal-width substitution at this composition edge.

All remaining AM-MAIN-v3 assumptions are included verbatim by reference and explicit guards in the fixed statement. Applying that theorem gives the stated radius, success and complete all-input schedule. Each D_alg call executes exactly one D0 call plus deterministic rational rounding; therefore its call bound becomes the stated D0 bound with no extra oracle factor. There is no coherent-code or quantum claim.

For the asymptotic family, q0 is polynomial in value and M,Qmin are polynomial in value. The effective prime-list construction returns Qmax polynomial in those numeric inputs, so logQmax=O(logn) for each fixed family exponent. With epsilon=epsilon_*/4,

    Ncal+Ntest=O(n^(2c+2)*logn),
    K=O(n^(b+2c+2)*logn), ell=O(logn),
    sigma_floor=O(n^((b+2c+7)/2)*(logn)^(9/2)).

The fixed target noise sigma0=n^(b+c+4) exceeds8*k0*n*(n/2+2)/epsilon_* eventually. The Qmin modulus-rounding guard reduces to n^(b+2c+12)>=56*k0*n/epsilon_*, which eventually holds. The smallest auxiliary width is

    (Qmin/q0)*sigma0 >= n^(2b+3c+16),

which exceeds sigma_floor by a positive polynomial power. Since q0>=n*sigma0, this also implies Qmin>=n*sigma_floor. The upper-width guard holds identically, independent of Qmax. No circular choice uses K to choose Qmin or the prime list.

The AM functional term satisfies sqrt(mu)=O(n^(-c-3/2)) and sqrt(D/2^n)<=2^(-(1-rho)n/2); Gamma tends to1. The tail, theta-ratio and implementation terms are negligible against epsilon=Theta(n^-c). Hence (G-AM) holds eventually uniformly in J. The inherited C8 bounds admit a polynomial-value kappa choice, chi=O(sqrt(logn)) at fixed/inverse-polynomial zeta, and the uniqueness guard holds as in AM-MAIN-v3. Consequently r=epsilon*ell^2/(256*n*K*chi*Qmax) is inverse polynomial. This expression is equivalent to d0/Qmax because delta=epsilon/4; here epsilon denotes the AM internal epsilon=epsilon_*/4. Large constants/exponents and bit-length accounting are explicit; practical feasibility is not claimed.

All ideal restrictions persist. A conditional BDD reduction on this family does not itself prove that the family is hard, or repair the separate standard-hardness foundation.
