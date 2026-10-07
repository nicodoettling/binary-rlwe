# NC-RECT v1 — proof-only rectangular discrete Gaussian completion

Frozen coordinator derivation, 2026-09-07. Status PROVISIONAL pending nonauthor review. This narrows the historical NC1 v2 to its independent-summand part and reproves it; no sequential sampler is used. The matrix B below is an exponent parameter, not the actual covariance of a discrete distribution.

Let n,p be positive integers, M an integer p-by-n matrix, and tau,sigma>0. Suppose tau²||M||² <= (1-a)sigma² for 0<a<=1. Set

    B = sigma² I_p - tau² M M^T,
    Theta = tau² I_n - tau⁴ M^T M / sigma²,
    delta = sum_{k in Z^n, k != 0} exp(-pi k^T Theta k).

Thus B >= a sigma² I_p and Theta >= a tau² I_n. Independently draw G from the product D_tau law on Z^n and H from the exact law on Z^p proportional to exp(-pi h^T B^-1 h). Set N=MG+H. Define

    e(delta)=min(1,delta/(1-delta)) if delta<1; e(delta)=1 otherwise.

Then TV(N,D_sigma^p)<=e(delta). No efficient sampler for H is asserted or needed when H is used only to bound information in a mathematical coupling.

The pointwise result extends to a latent variable C, with M=M(C), if conditional on every positive-probability C the joint law of (G,H) is the stated product and the parameters and bound are uniform. It gives TV((C,N),(C,E))<=e(delta_bar) for independent E~D_sigma^p whenever delta<=delta_bar. Append any S jointly independent of (C,G,H) to obtain the witness-retaining comparison. Reduction modulo q and subsequent deterministic maps contract this distance. H is integrated out of the noise comparison; retaining H would be a different, generally false assertion.

## Complete calculation

All Gaussian sums below converge absolutely because the parameter matrices are positive definite. Completing the square gives, for real g,z,

    ||g||²/tau² + (z-Mg)^T B^-1(z-Mg)
      = ||z||²/sigma² + (g-mu_z)^T Theta^-1(g-mu_z),
    mu_z = tau² M^T z / sigma².

Indeed Theta^-1=tau^-2 I_n+M^T B^-1 M and Theta^-1 mu_z=M^T B^-1 z; substitution also verifies the constant term. These identities follow by multiplication from B=sigma² I_p-tau² M M^T and hold for rectangular or singular M.

For each integer z, every integer g corresponds to exactly one integer h=z-Mg because M is integer. Thus the mass at z is a constant independent of z times

    exp(-pi ||z||²/sigma²) rho_Theta(Z^n-mu_z),
    rho_Theta(Z^n-c)=sum_g exp(-pi(g-c)^T Theta^-1(g-c)).

The Fourier transform of the Schwartz Gaussian x -> exp(-pi x^T Theta^-1 x) is k -> sqrt(det Theta) exp(-pi k^T Theta k). Poisson summation therefore implies

    r_z := rho_Theta(Z^n-mu_z)/sqrt(det Theta)
         = sum_k exp(-pi k^T Theta k) exp(-2pi i k^T mu_z).

Consequently 1-delta<=r_z<=1+delta uniformly in z. Writing P=D_sigma^p, the normalized output is exactly Q(z)=P(z)r_z/E_P r. If delta<1 then

    TV(P,Q)= E_P |r_z-E_P r|/(2 E_P r)
            <= delta/(1-delta).

The bound TV<=1 supplies the other branches, including delta>=1. This explicitly rejects historical NC1 v1: M=0,n=p=1,sigma=1,tau=1/3 has N=D_1 exactly while delta>=2 exp(-pi/9)>1, so the unguarded expression would be negative.

For t>0 define kappa(t)=2 sum_{j>=1}exp(-pi t j²). Since j²>=1+3(j-1),

    kappa(t)<= 2 exp(-pi t)/(1-exp(-3pi t)),
    delta <= (1+kappa(a tau²))^n-1.

The latter is an identity for a product of unconditioned independent integer-coordinate summation indices followed by a pointwise positive-term comparison. It is not a selected-stage probability product. No caching or posterior replay is present.

## Ring stacking and finite losses

For coefficient masks F_1,...,F_m in [-b,b]^n, let M_i be integer negacyclic multiplication by F_i and stack M_i vertically into M of dimensions mn-by-n. Since each shift is orthogonal, ||M_i||<=||F_i||_1<=nb, hence ||M||²<=sum_i||M_i||²<=mn²b². Taking sigma_m=2nb tau sqrt(m) gives a=3/4. The completion B has cross blocks -tau² M_i M_j^T; the target comparison is the entire independent product D_sigma_m^(mn). The Gaussian smoothing sum is n-dimensional despite the mn-dimensional output. The same one G masks S for every response.

For tau=ell=ceil(log2 n), the uniform delta_bar=(1+kappa(3ell²/4))^n-1 is exp(-Omega(log² n)); after its guard e(delta_bar) is negligible. Choosing b=ell² makes sigma_m=2n ell³ sqrt(m), polynomial for m<=2 (or any specified polynomial m when a source supplies that budget). This calculation alone does not provide source samples.

If m independent masks initially have iid D_ell coefficients, conditioning all mn coefficients on [-ell²,ell²] costs at most

    delta_F,m <= mn exp(-pi ell²)/(pi ell).

To see this, the one-dimensional normalizer is at least ell by Poisson summation with zero shift. For integer b=ell², monotonicity gives 2 sum_{z>b} exp(-pi z²/ell²) <= 2 integral_b^infty exp(-pi x²/ell²) dx <= ell² exp(-pi b²/ell²)/(pi b). Divide by ell and union bound. This conditioning involves only masks, so independence of S,G and masks persists; no completion is drawn until the mask has been fixed.

## Dependencies and scope

The proof uses elementary linear algebra, the Gaussian Fourier transform, and Poisson summation for Schwartz functions. The Gaussian conventions match Peikert, *An Efficient and Parallel Gaussian Sampler for Lattices*, Sections 2.4–2.5, https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf. Its Theorem 3.1 is not imported as this lemma: that source's shifted-lattice experiment has dependent summands. The displayed derivation supplies the exact independent integer-summand model here.

Finite sampling of the actual target E is a separate public operation. A proof-only exact H, G, or hidden ideal is not an algorithm input and contributes no runtime to the source distinguisher. The historical H_seq normalizer controls remain preserved, but this version makes no assertion that H_seq equals D_B and does not depend on a sequential sampler.
