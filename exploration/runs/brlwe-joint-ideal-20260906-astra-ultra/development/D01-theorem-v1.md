# D01 frozen extraction theorem, version 1

Frozen 2026-09-06. Statement and definitions only; the author proof is in D01.md. This packet does not assert source hardness or a multi-sample result.

Fix K>1. There exist positive constants c_K and N_K such that the following holds for every power-of-two n>=N_K, every prime q=1 mod 2n with q<=n^K, and every integer

    ceil((log n)^2) <= d <= floor(sqrt(n)/(log n)^4).          (D1)

All logarithms in (D1) and the bounds below are natural. Put ell=ceil(log2 n), R=F_q[X]/(X^n+1), and let Rts be the set of its n roots in F_q. For every d-subset T of Rts, fix an ordering and define

    pi_T(s)=(s(r))_(r in T) in F_q^d,
    J_T=ker(pi_T), I_T=Ann(J_T).

Sample S with n independent uniform binary coefficients. Independently sample G with n independent coefficients D_ell(z) proportional to exp(-pi*z^2/ell^2), reduced modulo q, and set Y=S+G in R. Let Z be uniform in F_q^d independently of Y. Then, uniformly for EVERY T,

    TV( (Y,pi_T(S)), (Y,Z) )
      <= (1/2) exp(-c_K*n/(d*(log n)^6)).                  (D2)

Consequently the error is negligible uniformly over (D1), since the exponent is at least c_K*sqrt(n)/(log n)^2. There is no exceptional support set, exceptional prime set, RH hypothesis, or inverse/sign-pair exclusion. This is an asymptotic theorem along qualifying split primes; it supplies no concrete value of N_K.

Let T instead have ANY law independent of S,G, and let Gamma=(J_T,U,F,H) be sampled using an arbitrary conditional kernel given T, independently of S,G. Let Z be conditionally independent uniform in the quotient given T. Then the same bound holds for

    TV( (T,Gamma,Y,pi_T(S)), (T,Gamma,Y,Z) ).               (D3)

In particular (D3) applies to candidate A's actual independent source kernel: U has nonzero active coordinates on T, F is sampled in the coefficient box |F_j|<=ell^2, and H is the prescribed F-dependent completion drawn without S or G. Retaining these variables costs no further extraction error. U's active-unit condition is needed by the bridge, not by this extraction theorem.

The candidate-A application keeps gamma=tau=ell, b=ell^2, sigma=2n ell^3, and additionally requires sigma*n^c<=q<=n^K with fixed c>0. Changing d from the initial max(1,floor(n/ell^3)) to a value in (D1) is an explicit within-slot change of source parameters. The support remains uniform among ALL d-subsets; no support rejection or structured-support replacement is made. A simple eventual example in (D1) is d=floor(n^(1/3)). This theorem does not prove extraction at the original larger dimension.

## Finite source-application bound underlying the theorem

For an arbitrary wrapped coefficient auxiliary law W, put

    p_y=W(y-1)/(W(y)+W(y-1)),
    beta=4 E[p_Y(1-p_Y)],
    mu_beta(0)=1-beta/2, mu_beta(+1)=mu_beta(-1)=beta/4.

Zero-probability Y fibers are omitted. Let Delta have iid coefficient law mu_beta, let z(Delta) count the roots in Rts at which Delta vanishes, and set z(0)=n. The exact normalized averaged collision is

    M_d = q^d E_Delta[binom(z(Delta),d)/binom(n,d)].

The joint TV retaining uniform T,Y is at most (1/2)sqrt(M_d-1).

Put Lambda=d log q, let 0<kappa<1/100 and 0<rho<1, and let c_BV,C_BV>0 denote the absolute constants of Breuillard–Varju Proposition 23. Assume every root in Rts avoids nonzero integer polynomials of degree <=3Lambda and Mahler measure <=exp(kappa), and assume

    ||mu_beta||_2^2 < 1-rho,
    Lambda >= max(kappa^(-1),rho^(-1)),
    n-1 >= C_BV*(kappa*rho)^(-1)*d*Lambda*(log Lambda)^3.   (D4)

Then

    0 <= M_d-1
      <= q^d/(n)_d * exp(-c_BV*rho*kappa*(n-1)
                              /(Lambda*(log Lambda)^2)), (D5)

where (n)_d=n(n-1)...(n-d+1). For any ONE fixed support the same normalized collision excess is at most the right side with q^d replacing q^d/(n)_d. This latter bound implies the uniform assertion (D2).

Permitted primary sources: [Breuillard–Varju, arXiv:1810.13360, Section 5, Definition 22 and Proposition 23](https://arxiv.org/pdf/1810.13360); [Voutier, original height paper, Theorem and Corollary 2](https://arxiv.org/pdf/1211.3110); [Breuillard–Varju scalar affine walks, Theorem 5 and Lemma 6](https://arxiv.org/pdf/1909.09053); and the locally supplied Boudgoust–Lapiha ring-LHL manuscript. The scalar theorem and ring-LHL manuscript provide comparisons; they need not be imported to prove (D2) once Proposition 23 and the Mahler bound are available.

