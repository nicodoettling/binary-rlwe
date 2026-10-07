# Blind partial report RB1 — 2026-09-07 22:03 UTC

Input frozen: `input/theorem-only-v2.md`, SHA256 `bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124`.
Only candidate input read is that theorem. Process-only sources read are the mathematical-proof-audit skill and its two named references. `launcher-run.json` and its exact `cap.status_file` were read for operational timing. No proof, historical objection, research list, source log, or worker note was read. The first Python freeze command failed because `python` is unavailable; `python3` succeeded and verified the requested digest. No content-policy interruption occurred.

## First finite/degenerate checks

For d=0, both U elements are exactly zero; this is a valid source and requires no inversion. For d=n, the source pair is exactly uniform in R^2 and its distinguishing advantage is zero. The displayed finite upper bound is then at least 1 because q>=5 and ((1+D_ell(0))/2)>=1/2. For intermediate d, U_1 or U_2 can be zero, but the argument below uses only image size, never nonzero ideal coordinates. For the comparator, A_1,A_2 are exactly independent uniform ring elements; the fresh secret and fresh error samples are independent of the entire pair. Thus the wrapper gives the exact specified target law for m=1 and m=2. With m=1, the unused second element has no effect.

## Independently reconstructed route to (F)

Let B be the vertical stack of the integer negacyclic multiplication matrices of the first m F elements, and condition on their coefficients having absolute value at most ell^2. Then ||B||_op <= sqrt(m)n ell^2, and for sigma^2=4m n^2 ell^6 the matrix C=sigma^2 I-ell^2 BB^T is positive definite with C >= 3 sigma^2 I/4. Introduce G~D_ell^n and an independent integer matrix Gaussian H with weight exp(-pi h^T C^{-1}h). Completion of squares shows BG+H is close to the product D_sigma law. Its residual lattice covariance is K=(ell^{-2}I+B^T C^{-1}B)^{-1} = ell^2 I - ell^4 B^T B/sigma^2 >= 3 ell^2 I/4. A direct periodized-Gaussian Fourier calculation should give the stated Delta_N and eta_N including the normalization denominator. This is still being written and checked in full.

In the replacement law, the second components equal U_i S+F_i(S+G)+H_i. Revealing Z=S+G and V=(U_i S)_i suffices to generate this transcript, together with variables independent of (S,G). For every fixed U tuple, V has at most q^d possibilities, because its map factors through the d CRT coordinates in T. The average optimal guessing probability for S from Z alone is exactly ((1+D_ell(0))/2)^n: in one coordinate, the sum of max(D_ell(z),D_ell(z-1)) over integers z is 1+D_ell(0). Arbitrary q^d-valued leakage multiplies this bound by at most q^d. This proof accommodates zero U values.

The truncation tail per F coefficient is at most exp(-pi ell^2)/(pi ell), using Z_ell>=ell and the Gaussian integral tail. Union bounding over mn coefficients yields delta_F,m. This is a union bound, not a product of conditional events. The wrapper on the uniform comparator has success epsilon_m, so the absolute distinguishing advantage is at least epsilon_m minus its planted success.

## Outstanding checks

Full normalization derivation and finite-support diagnostic; precise implementation total-variation bookkeeping; deterministic bounded runtime of finite Gaussian sampling; least-prime asymptotic substitutions and uniformity. No counterexample has been found so far, and no complete acceptance verdict has yet been frozen.
