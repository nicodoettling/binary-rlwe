# F02-C1 — an explicit one-sample discrete completion

Frozen derivation version 1, finalized 2026-09-06 14:45 UTC. Evidence: complete calculation and an explicit finite-precision sampling construction; pending nonauthor review. This is a noise lemma and source interface, not a hardness theorem. The matrices below parameterize Gaussian exponents; a continuous Gaussian with parameter matrix B has actual covariance B/(2pi). An integer discrete Gaussian does not have exactly that covariance.

## Statement and dependencies

Let M be any integer n-by-n matrix, let tau,sigma>0, and suppose

    B = sigma^2 I - tau^2 M M^T > 0.
    T = tau^2 I - (tau^4/sigma^2) M^T M > 0.

Define D_B on Z^n by probability proportional to exp(-pi h^T B^(-1) h). Independently sample G~D_tau^n and H_*~D_B. Put

    delta(T)=sum_{k in Z^n, k!=0} exp(-pi k^T T k).

If delta(T)<1, then

    TV(MG+H_*, D_sigma^n) <= delta(T)/(1-delta(T)).                 (C1)

The same bound holds after reduction modulo any q. It also holds jointly with any latent variable C such that M is fixed given C, G keeps its iid D_tau law conditional on C, and H_* has the displayed law conditional on C independently of G, provided the right-hand side is bounded uniformly on C. H_* is integrated out. It may not be retained as an extra coordinate in (C1).

For practical sufficient parameters, if

    tau^2 ||M||_op^2 <= (1-a) sigma^2,   0<a<=1,

then B >= a sigma^2 I and T >= a tau^2 I. With

    kappa(s)=2 sum_{j>=1} exp(-pi s j^2),
    kappa(s) <= 2 exp(-pi s)/(1-exp(-3pi s)),

we have delta(T) <= (1+kappa(a tau^2))^n-1. Thus constant a and tau=omega(sqrt(log n)) make (C1) negligible. The bound on kappa follows from j^2>=1+3(j-1), j>=1.

## Proof of C1, including normalization

The identity

    ||g||^2/tau^2 + (z-Mg)^T B^(-1)(z-Mg)
      = ||z||^2/sigma^2 + (g-mu_z)^T T^(-1)(g-mu_z),
    mu_z = (tau^2/sigma^2) M^T z                                  (C2)

holds for every real g,z. One way to check it is to expand both quadratic forms, using T^(-1)=tau^(-2) I+M^T B^(-1)M, T^(-1)mu_z=M^T B^(-1)z, and B+tau^2 M M^T=sigma^2 I. These identities hold whether or not M is invertible. They also follow by singular-value decomposition and scalar identities on each singular direction.

For every z in Z^n, independence gives

    Pr[MG+H_*=z] = constant * exp(-pi||z||^2/sigma^2)
                            * rho_T(Z^n-mu_z),
    rho_T(Z^n-c)=sum_{g in Z^n} exp(-pi(g-c)^T T^(-1)(g-c)).

Poisson summation, applied to this Schwartz Gaussian, gives the absolutely convergent identity

    rho_T(Z^n-c)/sqrt(det T)
      = sum_{k in Z^n} exp(-pi k^T T k) exp(-2pi i <k,c>).

Therefore r_z=rho_T(Z^n-mu_z)/sqrt(det T) lies in [1-delta,1+delta], uniformly over z. If P=D_sigma^n, the output law is exactly Q(z)=P(z)r_z/E_P[r]. In particular its likelihood ratio lies in [(1-delta)/(1+delta),(1+delta)/(1-delta)]. Since E_P[r]>=1-delta and |r_z-E_P[r]|<=2delta, TV(P,Q)<=delta/(1-delta). This proves C1. No conditioning on H_* and no approximation by continuous random variables occurs.

The underlying matrix Gaussian and smoothing methods are standard; see Chris Peikert, *An Efficient and Parallel Gaussian Sampler for Lattices*, April 13, 2011 version, Sections 2.4 and 3, https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf. Theorem 3.1 there permits shifted-lattice dependence, so it is not imported as an independent-summand theorem without checking its experiment. C2 and the displayed Poisson argument supply the independent integer-summand statement needed here directly.

## C3 — the actual auxiliary-noise sampler

We specify an efficient law H_seq instead of silently pretending that generic exact D_B sampling is available. Compute the rational LDL decomposition

    B=L diag(d_1,...,d_n) L^T,

with L unit lower triangular and each d_i>0. Start with no sampled coordinates. At step i, compute

    c_i = sum_{j<i} L_ij y_j,
    sample h_i in Z with mass proportional to exp(-pi(h_i-c_i)^2/d_i),
    y_i=h_i-c_i.

Use fresh randomness at every step, and return h=(h_1,...,h_n). The centers depend on earlier draws. They are not ignored in the following calculation.

For b=lambda_min(B)>0, every pivot d_i>=b. Indeed d_i is the Schur complement of the preceding principal block. Its variational expression is a minimum of v^T B_i v over vectors v ending in 1; all such vectors have norm at least 1, so the minimum is at least b. Define kappa=kappa(b), assume kappa<1, and put

    R_seq = ((1+kappa)/(1-kappa))^n,
    eta_seq = min(1, (R_seq-1)/2).

Then TV(H_seq,D_B)<=eta_seq. To check the adaptive-normalizer issue explicitly, let

    Z_i(c)=sum_{k in Z} exp(-pi(k-c)^2/d_i).

The one-dimensional Poisson identity implies Z_i(c)/sqrt(d_i) in [1-kappa,1+kappa] for EVERY real c. The sampler's exact probability of h is

    Q_seq(h)=exp(-pi h^T B^(-1)h) / product_i Z_i(c_i(h_<i)).

This equality uses the exact conditional kernels. It is not a multiplication of marginal event bounds. Writing D(h)=product_i Z_i(c_i(h_<i)), we have

    sqrt(det B)(1-kappa)^n <= D(h) <= sqrt(det B)(1+kappa)^n.

Moreover P_B(h)=Q_seq(h)D(h)/E_Qseq[D], because Q_seq(h)D(h) is exactly the unnormalized target Gaussian mass. Thus P_B/Q_seq lies in [R_seq^(-1),R_seq], proving the TV bound. This comparison accounts for every adaptive center and the global normalization.

Combining C1 with this sampler and wrapping gives

    TV(MG+H_seq mod q, W_sigma,q^n)
      <= delta(T)/(1-delta(T)) + eta_seq.                         (C4)

H_seq depends on M and the public widths, and does not use G or S. Let H_impl denote its finite-precision implementation described next, and let eta_H be a uniform bound on TV(H_impl,H_seq) for all admitted M. For the implemented source the noise bound is exactly the right side of C4 plus eta_H (and the independently charged G-sampling error, if G too is approximated). The extraction/source experiment uses H_impl throughout; H_seq and D_B are intermediate comparison laws only.

## Finite precision and running time

For the parameter regime below, entries of M and sigma,tau have polynomial-size rational descriptions and polynomial magnitudes, with B>=a sigma^2 I for constant a. LDL can be computed in rational arithmetic with polynomial bit complexity; no eigenvalue approximation is needed when the conservative norm bound is used. All pivots satisfy a sigma^2<=d_i<=sigma^2.

Each one-dimensional sampler can enumerate integers in |k-c_i|<=n sqrt(d_i)+2 and normalize dyadic approximations to their Gaussian weights. Uniformly over c_i, the omitted conditional tail is exp(-Omega(n^2)) when d_i>=1. For example, compare the two tails with integrals starting at n sqrt(d_i), using the lower normalizer sqrt(d_i)(1-kappa(d_i)); this yields a constant multiple of exp(-pi n^2)/(n(1-kappa(d_i))). There are O(n sigma) entries per conditional table, polynomial under polynomial sigma.

For a completely bounded algorithm, the enumeration boundary can use n sigma+2 in place of n sqrt(d_i)+2. This is wider and has the same polynomial cost. On this truncated execution |y_i|<=n sigma+2. Since sum_{j<=i} L_ij^2 d_j=B_ii<=sigma^2 and d_j>=a sigma^2, we have sum_j L_ij^2<=1/a. Consequently all centers have magnitude at most sqrt(n/a)(n sigma+2), and their rational bit lengths are polynomial. This also avoids any unbounded intermediate arithmetic.

Approximate each conditional probability table to total variation at most 2^(-n)/(10n), with exact dyadic normalization. O(n+log(n sigma)) output precision bits plus the rational input bit length suffice for absolute probability errors; standard interval evaluation of exp and pi at polynomial precision supplies the weights. The maximum exponent on the wider table is O(n^2/a), so its integer part also has polynomial length. The joint error of all conditional draws is at most the sum of their uniform conditional errors, by a sequential maximal-coupling argument, plus the Gaussian tail bound. This yields an explicitly chargeable negligible eta_impl. The same table method samples G and the finite-support F law. Uniform finite-field draws can be performed by capped rejection with exp(-Omega(n)) failure, or their own dyadic approximation; charge this in eta_impl as well. No claim of a finite exact sampler for arbitrary real Gaussian probabilities is made.

## One source family with an explicit F-law parameter

Fix a power-of-two n>=2, an odd fully split polynomially bounded prime q, an integer d in [0,n], and an efficiently sampled hidden d-element CRT support T_support. Uniform d-subsets are the rich-support instance; the binomial supports are a separately identified failing control. Let I be the ideal supported on T_support and J=Ann(I). A source challenger, without a secret input, does the following:

1. Sample T_support. In CRT coordinates sample U_i uniformly in F_q^* for i in T_support, and set U_i=0 otherwise. Thus multiplication by U is always an isomorphism R_q/J -> I. This is direct active-unit sampling, not uncharged rejection of a uniform ideal sample. Sample V_i independently uniformly in F_q for i in T_support, with zero elsewhere.
2. Fix one of the following two public choices for the coefficient law of F, independently over all n coefficients and independently of U,V,T_support:
   - Rademacher: F_j is uniformly +1 or -1; take b=1.
   - Truncated Gaussian: F_j has exactly D_gamma conditioned on |F_j|<=b, with gamma>=1, ell=ceil(log2 n), and b=ceil(gamma ell). Here gamma and b are polynomially bounded. This is a different exact source law from Rademacher F and from untruncated D_gamma F. It belongs to the same completion family because only |F_j|<=b is used.
3. Set tau=ell=ceil(log2 n), sigma=2 n b tau. Build the integer negacyclic multiplication matrix M=M_F, and B=sigma^2 I-tau^2 M M^T. Sample H=H_impl(B), the finite-precision implementation of C3 with the policy above, independently of U,V once F is fixed. Output only (A,C)=(U+F,V+H) mod q.

For the truncated-Gaussian option, a strictly finite implementation fixes a public deterministic Gaussian-weight approximation routine and its precision and samples its normalized finite table. Its exact output law is denoted F_impl. The noise proof applies directly to this actual law because its support remains |F_j|<=b; it does not require that its probabilities equal transcendental ideal Gaussian probabilities. If a source hypothesis is instead formulated using ideal truncated D_gamma, the coefficient-table distance must be charged explicitly. Uniform signs need no such Gaussian probability approximation. Likewise exact uniform CRT coordinates define the ideal source interface; capped rejection implements them with a separately budgeted negligible source-sampling distance. On a capped failure U's fallback must stay active-nonzero (e.g. all ones on its support). No finite-field sampling error is silently treated as exact uniformity.

The source assumption, if stated, compares this EXACT joint pair to two independent uniform ring elements, at the same F law, H algorithm, support distribution, U law and precision. It is not implied by marginal pseudorandomness or an independently noised HLBDD pair. The completion creates correlations between F and H and, in general, between the coefficients of H. In the ideal finite-field interface V remains uniform and independent of (U,F,H) conditional on the ideal; its finite implementation's deviation is part of the explicitly budgeted source-sampling distance.

The elementary operator bound ||M_F||_op<=||F||_1<=n b follows because M_F is a sum of signed orthogonal cyclic-shift matrices weighted by F_j. Therefore tau^2||M_F||_op^2<=sigma^2/4, so a=3/4. We obtain

    delta(T) <= (1+kappa(3 tau^2/4))^n-1 = exp(-Omega(log^2 n)),
    eta_seq <= exp(-Omega(n^2 b^2 log^2 n)).

The first display is an asymptotic upper bound, not an equality assertion for the actual error. The finite formulas C1/C3 determine constants. Sampling errors can be made negligible with the described polynomial resources. If desired, the n-coordinate total variation from replacing untruncated D_gamma by its restriction is at most n exp(-pi ell^2)/(pi ell): sum the omitted decreasing Gaussian tails by integration and use Z_gamma>=gamma. This estimate does not make the two exact source definitions interchangeable without charging it.

For the reference baseline additionally require

    2 n b ceil(log2 n) n^c <= q <= n^K,     q=1 mod 2n.           (C5)

Thus for b=n^beta up to logarithmic factors, any fixed K>1+beta+c leaves a numerical interval eventually; the statement is along qualifying split-prime sequences in that interval. Existence of primes at every such narrow exponent is not asserted. For example b=1, sigma=2n ceil(log2 n) fits every qualifying polynomial q sufficiently larger than n^(1+c) log n. A polynomial modulus is compatible with the noise lemma.

## Extraction interface and the first unresolved gate

The public reduction samples a fresh binary S_0 and independent G_0~D_tau^n, and computes Y=S_0+G_0 mod q. This needs only tau; it does not use hidden F,J,U,H or the source secret, which does not exist. In the mathematical bridge, independent S,G of that same law generate Y=S+G. The challenger sampled H using only F, so H is independent of S,G conditional on J,U,F. Consequently any established extraction law jointly retaining (J,Y) extends by data processing to (J,U,F,H,Y). The extraction law itself is not proved here for rich supports.

For binomial supports, the previously proved extractor allows this growing tau, but the first source marginal is attacked by the existing block decoder. For rich supports, completion and PPT samplability are now explicit. The unresolved gates are conditional extraction for the selected support/quotient dimension and computational pseudorandomness of this exact correlated source pair. The latter is a separate hypothesis, with no supporting reduction supplied by C1–C5. The large gap between F's coefficient width and H's width changes the source regime and must be assessed by the source worker.

This is one target sample. Reusing G across samples changes the conditional precision matrix and the whole error kernel; C4 alone proves no multi-sample statement. Exact completion at small constant widths is not claimed and can fail, as the Z/5 control in F02.md shows.
