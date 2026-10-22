# FF1 frozen quantifiers and interfaces, version 1

Author analysis, not a new accepted theorem. Inherited exact-hash DD acceptance remains authoritative at its recorded scope. Read MR-v1, FIXED-MAIN-v2 and AM-MAIN-v3 statements and complete proofs.

## Required order

First fix powers-of-two degree sequence n, R_n=Z[X]/(X^n+1), represented polynomial-VALUE integer q_0(n), and represented polynomial coefficient width sigma_0(n). The target family is then immutable. For every all-input bounded randomized polynomial-time code D_n, every polynomial physical sample bound k_0(n), and every inverse-polynomial advantage lower bound epsilon_*(n), a reduction may choose its own polynomial resources, auxiliary prime list, source radius, sampling precision, and source approximation depending on D's runtime, k_0 and epsilon_*^{-1}. This dependence must be effective/charged and may not alter target n,q_0,sigma_0.

Target planted: S uniform on {0,1}^n ONCE; A_i independent uniform in R_n/q_0 R_n; E_ij mutually independent D_(Z,sigma_0), independent of S and all A; B_i=A_i S+E_i mod q_0. Comparator: same public and metadata law, B_i independently uniform. The absolute gap is >=epsilon_*. If ideal metadata is supplied, the premise is pointwise for that same ideal. Actual code calls can be off-promise, but each call is bounded on every input/tape. Uniformity and encoding choices belong in a final main statement; current inherited code model charges the supplied code and evaluator lengths/runtimes.

## Inherited edge and actual dependency

MR-v1 gives whole-batch gap error <= k_0 n [7q_0/Q+(n/2+2)/sigma_0]. The first term can be made arbitrarily inverse polynomial by selecting Q after resources are fixed. The second persists as Q grows. Its guard sigma_0>=8 k_0 n(n/2+2)/epsilon_* forces target parameters to follow adversary exponents. Replacing k_0 by sqrt(k_0) or improving constants cannot close the fixed-family quantifier.

MR conditions on full A bank and S; transformed errors are independent over coefficient/sample only at that conditioning, with shifts -(rnd(lambda A)-lambda A)S. After marginalizing the public residuals, coefficient errors need not be independent. A scalar variance match is therefore insufficient.

AM-MAIN-v3 accepts variable auxiliary sigma_Q>=sigma_floor=8n^2 ceil(sqrt(Kn)) ell^4, with K=k_0(Ncal+Ntest), ell=ceil(log2(2nK)), and sigma_Q<=Q/n. Taking sigma_Q=Q sigma_0/q_0 allows the lower floor by increasing Q and requires q_0>=n sigma_0. All extraction calls use the same physical K bank; the number of code calls does not multiply endpoint TV. The source success upper bound averages distinct split primes with ONE common partition; changing this is a new dependency.

## First channel frozen for falsification

MR deterministic nearest-integer channel: lambda=q_0/Q, A'=rnd(lambda Abar) modq_0, B'=rnd(lambda Bbar) modq_0. Exact planted residual is E'=rnd(lambda E-Delta S), Delta=rnd(lambda Abar)-lambda Abar. Comparator is independent rounded uniforms. The first witness studies this named channel only, including its Q->infinity limit; it does not refute all transfer kernels or fixed-family reductions.

## Alternative constructions under investigation

1. Secret-independent Gaussian randomized rounding/correction, with full conditional covariance and normalization. The ring multiplication covariance is not determined by binary Hamming weight, unlike a scalar inner product.
2. Signed expectation correction or high-order extrapolation implemented through bounded Boolean code. A signed kernel's l1 overhead must be charged on the full batch; per-coordinate cancellation alone does not imply polynomial overhead for arbitrary polynomial k.
3. Different joint modulus channel or proof using computational indistinguishability rather than universal statistical simulation. Any source-secret information available only to the outer analysis cannot be handed to the auxiliary D_alg.

CP-1 remains a mandatory rejection of unsupported marginal products. We use explicit conditional product laws or additive full-law coupling. All 203 DD regression references are retained in inherited-regression-references.json, with the registry's source hash and exact entry pointers.
