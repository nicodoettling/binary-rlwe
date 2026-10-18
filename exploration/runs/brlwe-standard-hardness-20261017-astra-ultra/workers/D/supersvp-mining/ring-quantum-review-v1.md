# Uniform-secret ring quantum v1 adversarial review

2026-10-17T21:22:20Z tool clock at final pass. PROVISIONAL nonblind review, no acceptance authority and no experiment. Exact statement SHA2563d676bfbe4e7254bfa607045f054594a0aa98e65a4e93941bde2bb7ddb2e55f6; proof SHA256d61e01affd359c6305c89876466ac17aa983956981538bbc27f0f7156e76f4cb. Both freshly hashed and read in full. Primary2026/2443 Theorem7.1/Lemma7.2 had already been read through their proofs and parameter page64 visually checked.

## Disposition

The algebraic/probabilistic uniform-secret SEARCH-to-ring-SIS proof survives this pass. The new shared-key moments supply the missing ring kernel estimate, and the exact Fourier coefficient distribution prevents an uncharged q^n multiplier on a Gaussian approximation error. Recommend a fresh independent review within the explicit coherent-circuit and quantum implementation model. No decision-to-search or binary-secret edge is supplied, and the restricted ideal-family hardness premise remains OPEN.

One minor exposition qualification: the signed coefficient conjugation preserves the distribution of iid coefficients only when their one-coordinate law is symmetric. The actual law here is |fhat1|^2, which IS symmetric because f1 is real and even. Alternatively apply the moment calculation to the uniformly distributed conjugated key a* and the original X. Thus no change to the theorem or constants is needed; the broad prose should be read with this condition. The author has been notified, and frozen bytes remain unchanged.

## Exact endpoints and coherent algorithm

The input public tuple has a uniform ring row a conditioned on generating Rq, and arbitrary fixed conditional metadata Z given a. Fresh uniform secret and product Gaussian errors are independent of this whole tuple. The planted response and independent-uniform comparator share that public law. Only planted RECOVERY successdelta is assumed; no behavior on the comparator is imported.

The coefficient map L_a from n secret coefficients to M=nm response coefficients is injective exactly under the generation condition. Solving its linear system permits reversible erasure of the secret register. A recovery circuit may retain all its random coins and work registers; running its inverse and checking error/work registers leaves the stated unnormalized amplitude weighted by its true conditional output probabilityp(s|b). Nonnegative Gaussian amplitudes give the average overlap lower bounddelta-epsilon_E. The algorithm does not resample the arbitrary metadata law; it receives and retains the supplied public tuple.

Uniform secret Fourier orthogonality gives hhat=q^(n/2) fhat restricted toker(L_a^T) EXACTLY. For negacyclic coefficient matrices, M_a^T=M_(a*). Applying coefficient conjugation to the measured vector therefore yields the original ring relation sum a_i y_i=0, preserving norm and nonzeroness. Ignoring this transpose correction would be incorrect.

## Independent derivation of the ring moments

For a fixed vectorX=(X_i), letz(X) count CRT roots at which all X_i vanish. Against an unconditioned uniform key, each of the n-z active roots contributes one independent linear equation, soPr_a[sum a_i X_i=0]=q^(-(n-z)). This includes every zero-divisor pattern. Conditioning on key generation loses at most1/alpha0, wherealpha0=1-nq^-m.

For product coefficient law with maximum atommu, a rank-t CRT projection determines t pivot coefficients after conditioning on all remaining coefficients, so its zero probability is at mostmu^t. Independence between the ORIGINAL ring samples gives at mostmu^(mt) for a shared root subset. Expanding c^z as a sum over these subsets then proves

    E[c^z] <= (1+(c-1)mu^m)^n,

without assuming the root events themselves independent. Taking c=q bounds the full comparison-vector norm byK1/alpha0. Taking c=q^2 and applying Cauchy-Schwarz to a norm-tail eventF givesE[q^z 1_F]<=sqrt(K2 Pr[F]), retaining the SAME random key throughout. No averaged collision probabilities are multiplied.

The rank-conditioning bound is conservative: for a fixed nonzero CRT vector one can also count nonzero key vectors in its hyperplane directly. The stated coarser1/alpha0 bound is nevertheless valid and requires no extra assumption.

## Gaussian register, constants and errors

The exact finite register uses the product of centered-representative Gaussian amplitudes f1. Its measured law differs from the wrapped integer Gaussian by at most the omitted tail epsilon_E=2M exp(-pi q^2/(8chi^2)). Under4sqrt(H)<=chi<=q/(8sqrt(H)), H=lambda+ceil(log2(M+1)), chi>=8.

Every Fourier amplitude is at most its zero-frequency magnitude. The elementary mass bounds give

    max p <= (1+sqrt(2)chi)^2/(0.9qchi) <=3chi/q=mu.

The exact Fourier probabilities factor over all M coefficient coordinates. The primary one-dimensional Fourier comparison and tensor estimate give the displayed tail theta=2^(1-M)+16M exp(-2pi lambda); its constants are conservative relative to the proof's vector-distance bound. This tail estimate is used ONLY inside the exact shared-key moment/Cauchy-Schwarz calculation. An approximating Gaussian distribution is never substituted and then multiplied byq^n.

The zero vector contributes at mostz0=q^n mu^M. Consequently the bad comparison-vector energy is at mostz0+sqrt(K2 theta)/alpha0. A second Cauchy-Schwarz over the actual common(a,Z) law bounds the desired unconditional measurement success exactly as displayed. The algorithm's success includes the zero-test probability, so no postselection normalization amplifies its implementation error. Subtracting a supplied total trace error delta_Q is appropriate.

In the example regime n(q^2-1)mu^m<=2^-lambda, K1 andK2 are1+O(2^-lambda). Also nq^-m<=nmu^m/(3chi)^m is negligible, soalpha0=1-negligible. Finallyz0=(qmu^m)^n is negligible. With polynomialM andM>=4lambda+4, theta and the successive square-root losses remain negligible. Thus the claimed delta^2-negligible simplification follows; the ring sample countm cannot be replaced byM in the CRT moment condition.

## Operational and secret-distribution scope

The theorem explicitly requires coherent reversible access to the recovery circuit and its inverse, plus the stated quantum Gaussian/QFT preparation to total tracedelta_Q. Its ordinary arithmetic is polynomial in the full input encodings. This review checks the finite target states and error flow and imports the primary efficient Gaussian-register/QFT primitives; it does not claim to have implemented a quantum sampler experimentally. There is no experiment reservation or run.

For another independent secret lawP, the kernel Fourier weight isC_P=(sum sqrt(P(s)))^2, giving kernel reference energy at most(C_P/q^n)K1/alpha0. Uniform bits haveC_P=2^n, recovering the exponentially small(2/q)^n factor already found in exact-controls-v1.md. The mass outside the desired kernel cannot be discarded. This is an exact obstruction to substituting bits in THIS proof, not a universal impossibility for adaptive quantum reductions.

## Regression disposition

CP1 and the shared-key controls are addressed by taking expectations over one actual(a,Z) distribution and expanding root-subset indicators before expectation. N03-SCAL-POSTERIOR and public-tape controls are addressed by retaining metadata and true conditional solver probabilities. C02-CHAR is addressed by the full Fourier distribution and both CRT moments. R14/N02-DUAL-NUMBER are addressed by explicit zero-divisor ranks, not field assumptions moduloq. UNIFORM-APPROX-COLLAPSE is addressed by separating exact register identities, initial measured-error approximation, and final quantum implementation error. No secret/error correlation or binary-prior replacement is asserted. The source-family and computational-vs-statistical boundaries remain explicit.

The result is a concrete provisional ring extension of the uniform-secret quantum search template. It cannot be composed with a binary-only recovery oracle or a mere distinguisher without new verified steps.
