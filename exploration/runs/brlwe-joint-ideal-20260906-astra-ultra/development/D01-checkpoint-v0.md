# D01 — candidate A random-support joint extraction

Working note, 2026-09-06. Task deadline 15:45 UTC; final writing reserved from 15:40 UTC. Source law and parameters are candidate A1: ell=ceil(log2 n), tau=gamma=ell, b=ell^2, sigma=2n ell^3, initially d=max(1,floor(n/ell^3)), and qualifying split primes sigma*n^c<=q<=n^K. Only slot A is examined. No experiment allocation has been requested or used.

The exact target is extraction jointly with uniform d-subset T, Y=S+G, and the SC0 source auxiliaries U,F,H. Independence of the actual source kernel from S,G means the auxiliaries cause no further extraction loss once the statement jointly with T,Y is proved. U is explicitly active-nonzero; J_T vanishes on T and I_T=Ann(J_T) is supported on T.

The required sufficient statistic is

    M_d = q^d E_Delta[binom(z(Delta),d)/binom(n,d)],
    P[Delta_j=0]=1-beta/2, P[Delta_j=+1]=P[Delta_j=-1]=beta/4,

where beta=4 E[p_Y(1-p_Y)] for the SAME wrapped D_ell auxiliary law. The joint extraction TV is at most (1/2)sqrt(M_d-1). Uniformity at individual roots does not control the required factorial moment.

Primary check in progress: Breuillard–Varju Theorem 5 and Lemma 6 concern scalar geometric progressions. Their companion paper explicitly advertises a more general Proposition 24; I will check whether its precise recurrence/multidimensional statement yields a usable joint estimate before treating scalar mixing as the endpoint. The ring leftover-hash manuscript and partial-Fourier source estimates are being read directly as well.

Known control: the earlier binomial support yields block factorization but its source is polynomially decoded. It will not replace random T here. The F03 grouped-support decoder also excludes d=O(log n) under its explicit narrow-F modulus inequality, so a merely scalar or constant-dimensional extraction theorem cannot make candidate A computationally supported.

## Checkpoint: a stronger primary source gives a useful smaller dimension

Direct primary reading of [Breuillard–Varju, arXiv:1810.13360, Section 5, Definition 22 and Proposition 23](https://arxiv.org/pdf/1810.13360) gives the following finite application. Put Lambda=d*log q, choose kappa in (0,1/100) and rho in (0,1), and suppose every selected CRT root avoids nonzero integer polynomials of degree at most 3Lambda and Mahler measure at most exp(kappa). If

    ||mu_beta||_2^2 < 1-rho,
    Lambda >= max(kappa^(-1),rho^(-1)),
    n-1 >= C (kappa*rho)^(-1) d Lambda (log Lambda)^3,

then

    0 <= M_d-1
      <= q^d/(n)_d * exp(-c*rho*kappa*(n-1)/(Lambda*(log Lambda)^2)),

where (n)_d=n(n-1)...(n-d+1), mu_beta is the ACTUAL weighted ternary difference law above, and c,C are the source's absolute constants. Its notation log(Q^D) becomes d log q, not log(qd). The set supplied to the proposition comprises all ordered distinct d-tuples of the n CRT roots, so each unordered support occurs d! times. This is precisely the needed factorial-moment bound, not a product of marginal estimates.

Proposed within-slot dimension range, pending final checks:

    ceil((log n)^2) <= d <= floor(sqrt(n)/(log n)^4).

Keep all other candidate A parameters unchanged. Take kappa=(log n)^(-3), rho=1/4. For large n the weighted ternary law has beta>=1/2, hence 1-||mu_beta||_2^2=beta-3beta^2/8>=13/32>rho. The dimension conditions hold uniformly over polynomial q. The source bound then makes M_d-1, and thus full joint extraction error, negligible. Initial d=max(1,floor(n/ell^3)) remains a separately deferred claim; this estimate does not cover it.

The planned admissibility proof applies to EVERY support, so it requires no rejection and pays no bad-support probability. Dobrowolski's bound, in the form used in the primary affine-walk paper's proof of Lemma 6, makes a degree-<n polynomial of Mahler measure <=exp((log n)^(-3)) a product of cyclotomic factors and powers of X, for sufficiently large n. A root of order 2n cannot vanish at any such product of degree<n: if q divides a cyclotomic index m, phi(m)>=q-1>n; otherwise a root of Phi_m mod q has exact order m, forcing m=2n and degree n. Distinctness and nonzero coordinates are the only additional genericity conditions in Definition 22. Sign pairs and inverse pairs are allowed.
