# Conditional product transfer through an eligible factorization, v1

PROVISIONAL root constructive R2 candidate, not accepted. It changes the field and combines several sampler outputs; therefore it is not ruled out by the accepted same-field or fixed-linear-extraction controls. It does not establish a standard worst-case foundation.

Fix a power-two cyclotomic tower R=Z[zeta_(2n)] subset S=Z[zeta_(2m)], m=tn. In coefficient bases let Pi=Tr_(L/K)/t, the integral projection onto exponents divisible by t. Let I be a nonzero integral R-ideal, M=N(I), and SUPPLY ordinary bases of nonzero integral S-ideals F_1,...,F_r satisfying

    product_j F_j subset IS,       D_j=N(F_j)<=2^(rho m), 0<=rho<1.

Containment and bases can be checked by ordinary arithmetic. Existence, computation, and distribution of this factorization/cover are additional premises; they are not supplied by a small-ideal oracle. The ideals need not be prime or coprime. They and all future randomness are fixed independently of the fresh binary secrets used by any upstream recovery wrappers.

For each j suppose an ordinary sample oracle returns X_j in F_j with complete joint law within eta of the product of centered coefficient D_(F_j,W_j) laws, W_j>=4sqrt(m). A sufficient implementation premise is a conditional fresh-kernel TV error eta_j on every preceding history, with eta<=sum eta_j; marginal guarantees alone are insufficient. Off-ideal outputs are rejected and count as failures. No oracle outside its supplied family is called.

Compute Y=Pi(product_j X_j). Then Y belongs to I. For any L_tail>=1, except with probability at most

    eta + 4sqrt(m) sum_j 1/W_j + 2mr exp(-pi L_tail^2),       (P1)

Y is nonzero and has coefficient norm at most

    B = m^(r-1/2) L_tail^r product_j W_j.                    (P2)

The bound is capped at1. This is a solver returning a short nonzero vector, not a Gaussian sampler on I. Its approximation certificate is B/M^(1/n), since lambda_1(I)>=M^(1/n). It must be interpreted as a certificate, not a statement that every output has length near B. If r, t are constants, all W_j have polynomial VALUE in n, L_tail is polynomial in n, and the full bases and oracle executions have polynomial-bit costs, this gives a polynomial-in-n approximation with explicitly polynomial total runtime. Actual sampled-bit lengths or finite sampler support bounds must be charged; an exact infinite oracle is not finite code.

Proof of the nonzero bound, included rather than imported from a provisional companion. Every eligible F has a nonzero f with ||f||<=sqrt(m)D_F^(1/m)<2sqrt(m): apply Minkowski to the centered coefficient cube with volume just above2^mD_F and take a limit. Its m negacyclic rotations span the field over Q. Thus for every proper real linear subspace H there is a rotation v outside H with ||v||<2sqrt(m). For x in F intersect H, the cosets x+Z v are pairwise disjoint. Completing the square along each such line gives its Gaussian mass divided by rho_W(x) at least rho_(W/||v||)(Z+alpha), since the perpendicular correction factor is at least1. Scalar Poisson and triangle inequality give rho_a(Z+alpha)>=a/2 for a>=1: the dual error is at most2sum_(h>=1)e^(-pi a^2 h^2)<1/2. Therefore Pr[X in H]<=2||v||/W<4sqrt(m)/W. This argument uses the full normalized infinite Gaussian law, not a finite truncation.

First exclude X_j=0 for j<r using that subspace estimate. Condition only on these previous samples and their actual values. Their product A is then nonzero. Multiplication by A is invertible on the field, and Pi has nonzero rank, so kernel(Pi composed with M_A) is a proper real subspace. The fresh final X_r has conditional failure probability at most4sqrt(m)/W_r. A union bound proves the nonzero term; no law after successful selection is reused. For r=1 use A=1, with no preceding zero exclusions.

For each coefficient of a centered lattice Gaussian, completing the square and the translated-theta maximum give E exp(u X_i)<=exp(u^2 W^2/(4pi)). Chernoff and a union bound give Pr[||X_j||>W_j sqrt(m)L_tail]<=2m exp(-pi L_tail^2), without coordinate independence. Negacyclic convolution obeys ||xy||<=sqrt(m)||x||||y||. The projection Pi has operator norm1. On all norm events these facts give (P2). All zero, tail and implementation failures remain in the original probability space. Total variation contracts under the complete deterministic product/projection/failure map.

A necessary family budget is decisive. From product_j F_j subset IS,

    product_j D_j >= N_S(IS)=M^t.

Together with D_j<=2^(rho m), this implies

    M^(1/n)<=2^(rho r),  equivalently r>=log_2(M)/(rho n) when rho>0. (P3)

For constant r this route can cover only bounded normalized ideal norm. If M^(1/n)=n^alpha, fixed alpha>0, r must grow at least(alpha/rho)log_2 n. The displayed B certificate then typically becomes quasipolynomial when the delivered W_j are polynomial powers of n. This is a failure of this certificate to prove polynomial approximation; it is NOT a lower bound on actual product lengths or an impossibility theorem. A new correlated-product analysis, normalization, or richer source may change that conclusion.

For the tower example p17,n2,m8, four distinct prime factors J_a=(17,z-a), a in{3,5,12,14}, multiply to IS and each has norm17<2^6. Thus their product/projection restores exact I containment that a single factor's projection lacked. These are easy low-dimensional ideals. No known worst-case hard family is established by this example.

Reduction direction: given the pointwise executable binary-recovery premise in dimension m and the complete same-J composition at a common supplied modulus q coprime to every D_j, one could obtain the r finite samplers and then this short-vector procedure. Each sampler has its own verified parameter/error schedule; total coherent recovery executions at most2sum_j Qstar_j for one output, plus bounded classical arithmetic. A recovery premise at dimension n or one fixed modulus cannot silently be substituted at dimension m or another q. Product output is not DGS; no Gaussian covariance shortcut is involved. The missing arbitrary-ideal eligible-factorization and useful radius obligations remain separate.
