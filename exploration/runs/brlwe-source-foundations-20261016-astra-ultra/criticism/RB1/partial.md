# RB1 blind checkpoint

Input: input/theorem-only-v2.md, SHA256 44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51.

Only theorem, assignment, allowed operational launcher metadata and proof-audit skill references have been read. No author proof or other reviewer report has been read. No computation experiment has been run.

Candidate independent proof graph:
1. EX-REG: Fourier/Parseval; average two-seed Fourier factor is p_xi^2 with p_xi <= L^{-r}, where r is the multiplication rank of xi. For r>n/2 the contribution is <= (2/n)^n. For r<=n/2, cyclotomic determinant gives ||xi|| >= q^{(n-r)/n}, so Gaussian W supplies 16^n exp(-2 pi n^2); count <=q^n. Conditional product hybrid gives the full seed-including joint TV bound for every m, including m=3.
2. EX-REC: write C=V+G with V in I_T, and condition on the source/local variables only. A mask event gives coefficient |G|<=b and failure <=delta_mask. Stacked multiplication matrix H of G has operator norm <=sqrt(m)n b. Set s=ell and sigma=2s sqrt(m)n b. Gaussian convolution E=H F0+E' with F0~D_s^n and E' elliptical discrete Gaussian of covariance parameter sigma^2 I-s^2 H H^T should approximate D_sigma^{mn} with TV <=eta by Poisson summation on an n-dimensional completed-square covariance >=3s^2/4 I. Need finish exact normalization derivation.
3. Reveal T, all source/local variables, Z=S+F0 and S's projection onto T. This determines a simulated transcript. Side information has <=q^d projection possibilities and P_guess(S|Z)=((1+D_ell(0))/2)^n. No posterior independence of secret coordinates after the ideal projection is asserted.
4. Asymptotics: q<=n^{6K}, d=floor(sqrt(n)/ell^4) gives exp(-Omega(n)); d=floor(n/(24K ell)) gives log(q^d p^n)<=-3n log(2)/4+n/ell. All listed errors negligible for fixed h. q/sigma >=constant*n^2/ell^3 eventually >=n.

Open checks: complete exact Gaussian convolution normalization; explicit q primality/effective bounded samplers and sampler TV bookkeeping; supplied primary least-prime source; m=3 and degenerate d=0,n/zero-seed cases.

## Checkpoint: Gaussian completion and effectiveness

For N=mn, H stacked multiplication by G, Omega=sigma^2 I_N-ell^2 H H^T is positive definite. Let B=(ell^-2 I_n+H^T Omega^-1 H)^-1 = ell^2 I_n-ell^4 H^T H/sigma^2 >=3ell^2 I_n/4. Completing the square in f gives ell^-2||f||^2+(e-Hf)^T Omega^-1(e-Hf)=||e||^2/sigma^2+(f-ell^2 H^T e/sigma^2)^T B^-1(f-ell^2 H^T e/sigma^2). Poisson summation bounds the translated n-dimensional theta factor in sqrt(det B)[1-Delta,1+Delta]. Dividing by its average under D_sigma^{N} yields pointwise density distortion <=2Delta/(1-Delta), hence TV<=eta. The construction uses only one n-dimensional F0, even for m=3; no independent ideal-row assumption is present.

The sole permitted mathematical primary source was opened: Xylouris, Acta Arith. 150.1 (2011), Theorem 1.1, https://www.impan.pl/shop/publication/transaction/download/product/83078. It states P(a,Q)<=C Q^5.18 with effectively computable C. No other mathematical source was used.

Bounded sampling: for fixed h all widths L and sigma are polynomial in n. Enumerate support [-n ceil(t),n ceil(t)] and approximate e^(-pi z^2/t^2) and cumulative probabilities to enough polynomial precision. Tail and rounding errors are negligible, and table length/bit complexity are polynomial. The dense elliptical Gaussian is only an information-theoretic proof device and is never sampled by B_Q. The finite implementation TV formula follows by two local-sampler replacements, one planted-source replacement, and one target witness/transcript replacement.

A single bounded finite-regression reservation was requested from the parent; no experiment has yet run. Planned exact controls: character rank/norm enumeration at n=2,q=5 and n=4,q=17; a 3-bit binary-secret finite-noise test over all one-bit deterministic leakage maps. Work remains blind.
