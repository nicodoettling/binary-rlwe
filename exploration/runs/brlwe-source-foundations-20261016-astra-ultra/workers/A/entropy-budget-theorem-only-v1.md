# A-H3 v1: exact-comparator source-sample budget obstruction

**PROVISIONAL. Frozen author candidate, not certified.**

Let `R=F_q[X]/(X^n+1)` split into n distinct linear factors over `F_q`. Fix integers k,m>=1 and d in [0,n]. Let P_k be the law of k primal integral RLWE samples

    ((a_i,b_i=a_i*s+e_i))_(i=1)^k,

with s uniform R, all a_i independent uniform R, and the full error vector `(e_i)_i` independent of `(s,(a_i)_i)`; the source errors need not be independent across i. Let Q_k be uniform on R^(2k).

Let B_m be the following separate source: choose a uniform d-subset T of the n CRT roots; independently conditional on T choose m uniform points U_i of I_T, including zero coordinates; add independent coefficient-product integer D_ell masks F_i and reduce modulo q. Denote by H_F the Shannon entropy in natural units of the resulting single wrapped mask F_i in R.

Let K be any randomized map from R^(2k) to R^m whose coins are independent of its input and which satisfies `K Q_k = U(R^m)` exactly. No complexity restriction on K is imposed. Let

    epsilon=TV(K P_k,B_m),
    g=(m-k+1-q^(-k))*n*log(q)
      -log(binom(n,d))-m*d*log(q)-m*H_F.

Candidate conclusion:

    h2(epsilon)+epsilon*m*n*log(q) >= g.

In particular, for fixed m,k, powers-of-two n, ell=log2 n, q the baseline least prime 1 mod 2n^3, and either baseline d family, if k<=m then

    epsilon >= (m-k+1)/m - o(1).

The k=m=2 specialization has lower bound `1/2-o(1)`. This rules out exactly uniform-comparator-preserving kernels consuming only two ordinary RLWE samples as negligible-TV simulations of Base2. It does not rule out more source samples, a computational rather than statistical planted simulation, approximately uniform comparators without further density control, adaptive/source-oracle reductions, or general hardness connections.

Required review: conditional rank calculation with zeros, entropy contraction for randomized rectangular kernels, Gaussian wrapped-entropy bound, finite-parameter signs, and source budget scope. There is no sequential independence argument and no use of CP-1's rejected product step.
