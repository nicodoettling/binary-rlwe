# C scrutiny v1: short mixtures plus additive Gaussian

2026-10-16 21:19 UTC. Status: PROVISIONAL supporting calculation. This is an author's scrutiny of the coordinator's communicated candidate, not an independent or blind review. It does not certify a theorem version that has not yet been received.

## Candidate under examination

Uniform comparator seeds A1,A2 in R=F_q[X]/(X^n+1). Independently for every generated sample j, take coefficient-small R_j1,R_j2 and coefficient Gaussian W_j, and publish C_j=A1 R_j1+A2 R_j2+W_j. Keep all mixing coins private. The planted source uses the same public map on its sole Base2 challenge. It has U'_j=U1 R_j1+U2 R_j2 in the original I_T and F'_j=F1 R_j1+F2 R_j2+W_j. This does not give Base_m: the U'_j and F'_j are correlated, including correlations with one another through the R's. The accepted abstract lossiness proof allows an arbitrary joint latent C law and only needs independent S,G followed by a fixed completion kernel H given C.

## Adjoint support check

In coefficient Euclidean pairing, multiplication by X is a signed orthogonal cyclic shift. Its transpose is multiplication by X^-1. Thus M_A^t=M_(A*) where A*(X)=A(X^-1) modulo X^n+1. The involution maps CRT evaluation at alpha to evaluation at alpha^-1 and permutes roots (n even). For a Fourier frequency z, M_A^t z=A* z. If z has k nonzero CRT coordinates, A uniform makes A* z uniform in the k-dimensional ideal supported on those coordinates. No active-coordinate nonzero assumption on A is used.

## Norm check

Let z be the centered coefficient lift of any nonzero Fourier vector. Its degree is below n. Since X^n+1 is irreducible over Q for power-of-two n, multiplication M_z has nonzero integer determinant. Its reduction modulo q has rank k, equal to the number of nonzero CRT coordinates. Integer Smith normal form (or integral row/column operations with determinant ±1) implies q^(n-k) divides det(M_z), hence |det(M_z)|>=q^(n-k).

For the n complex roots zeta of X^n+1, the determinant is product_zeta z(zeta). Parseval gives sum_zeta |z(zeta)|^2=n||z||_2^2. AM-GM therefore yields

    |det(M_z)| <= (sum_zeta |z(zeta)|^2/n)^(n/2)
                 =||z||_2^n.

Hence ||z||_2>=q^(1-k/n). There is no sqrt(n) factor. For k<n/2 this gives ||z||_2^2>q. At k=n/2 it gives >=q. The argument depends essentially on power-of-two cyclotomic irreducibility and the centered lift only for the Gaussian Fourier estimate, not for determinant divisibility.

## Small-box Fourier collision check

Let R have independent coefficients uniform on any interval of L distinct residues, L<=q. The difference of two independent such coefficients, reduced modulo q, has maximum mass <=1/L, including wraparound. Its n coordinates remain independent. For any rank-k linear map P:F_q^n->F_q^k, choose k pivot columns. Condition on all nonpivot coordinates of D=R-R'. Each required pivot value has probability <=1/L, so Pr[P(D)=0]<=L^-k. This is one product distribution conditioned only on its distinct nonpivot coordinates, not an adaptive posterior product bound.

For z of CRT support k,

    E_A |phi_R(M_A^t z)|^2 <= L^-k.

Independence of A1,A2 therefore gives the two-box factor <=L^-2k. This claim concerns Fourier coefficient averages over uniform comparator seeds. It is not a statement conditional on planted seeds.

## Gaussian Fourier alias and sample-law checks

For wrapped iid coefficient D_w, Poisson summation expresses each normalized Fourier coordinate at t in [-1/2,1/2] as sum_l exp(-pi w^2(l-t)^2)/sum_l exp(-pi w^2 l^2). The numerator can be bounded by 3 exp(-pi w^2 t^2) for w>=1: after the closest term, the two one-sided tails are bounded by geometric Gaussian tails, with the possible tied nearest point at |t|=1/2 included. A written proof should retain this alias constant; replacing the Fourier transform by exp(-pi w^2 t^2) exactly would be false. Thus |phi_W(z)|^2 <=9^n exp(-2pi w^2||z||_2^2/q^2).

With w^2=n q ell^2 and q<=n^K for fixed K, the total contribution of all support k<n/2 frequencies is bounded by q^n 9^n exp(-2pi n ell^2), which is negligible. At k>=n/2, counting <=binom(n,k)q^k frequencies and taking L>=n sqrt(q) gives

    sum_(k>=n/2) binom(n,k) q^k L^-2k <=2^n n^-n.

These are conservative finite bounds. The zero Fourier character is omitted from chi-square.

For the conditional single-output kernel K_a, Parseval gives the conditional chi-square distance to uniform as the sum of squared nonzero Fourier coefficients. If the averaged chi-square is <=B, Jensen and TV<=sqrt(chi-square)/2 give E_A TV(K_A,U)<=sqrt(B)/2. Conditional on A, all fresh output draws are genuinely independent, so

    TV(Law(A,C1,...,Cm), Law(A,U1,...,Um))
      <=m sqrt(B)/2.

The U_i on the right are independent of A. Averaging then dropping A is valid. Appending independently sampled binary S and independent Gaussian target errors preserves this bound. No claim of independence after integrating A out is needed. The finite product TV inequality is applied conditionally to an actual product kernel; this avoids the CP-1 failure mechanism.

## Coarse planted noise and nonempty-regime checks

On max|F_ij|<=ell^2, max|R_jr,k|<=L and max|W_jk|<=w ell, every new coefficient has magnitude at most

    b'=2n ell^2 L+w ell.

Consequently ||M_(F'_j)||op<=n b' and the stack satisfies ||M||op<=sqrt(m)n b'. With tau=ell and sigma=2sqrt(m)n b' ell, the accepted rectangular completion applies to the entire m n-dimensional response noise, including all off-diagonal blocks. Its smoothing dimension is still n and the quotient charge is still q^d. Marginal independent completion would be invalid.

For L on the order of n sqrt(q), w on the order of sqrt(nq)ell, this conservative sigma is O(sqrt(m)n^3 sqrt(q)ell^3). Therefore q/sigma is polynomially nontrivial for q sufficiently larger than m n^6 ell^6; q/sigma>=n follows, for example, from q growing faster than m n^8 ell^6. The original baseline lower bound q>=2n^3+1 does not suffice for this conservative calculation. Any changed polynomial modulus family and its Base2 assumption must be stated explicitly.

For m<=n^c with c fixed, selecting a fixed modulus progression with q>=2n^h+1 and h>c+8 gives q/sigma>=n eventually. A polynomial upper bound q<=n^K then makes d<=n/(4K ell) an entropy-safe choice. The parameter family must be selected before the recovery algorithm and its success exponent. A theorem for each fixed c is not one fixed source family supporting every possible polynomial sample count.

## Remaining obligations

1. Freeze complete finite constants, rounding choices, legal interval L<=q and exact width definitions.
2. Prove Gaussian alias bound in full and retain the normalized discrete law.
3. Carry the witness/transcript TV comparison and source tails once, with exact equality to the locally sampled secret.
4. Specify exact or negligible-error bounded-time independent sampling of R,W,S,E and polynomial bit complexity.
5. Preserve baseline and new source-family assumptions separately.
6. Obtain fresh nonauthor proof/source/complexity and blind reviews of the exact selected theorem; this note is supporting reasoning only.
