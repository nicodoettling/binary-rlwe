# R03 — A2 parameter and sampler-interface refinement

Bounded cross-interface review, 2026-09-06; deadline 15:40 UTC. This is not the independent final criticism. The F02 and D03 notes remain frozen. Inputs read: D01-theorem-v1.md, D01.md when it became available, F01.md and its frozen theorem, the counterexample registry and previously read full correlated-error controls. No experiment or implementation project was run.

Version 1 frozen at 15:31 UTC after checking the table-normalization constant, capped-rejection count, shifted-tail bound, exact kernel dependencies, dimension range and revised leakage threshold. The bounded assignment is complete. Final nonauthor criticism remains a separate step.

## Disposition

No cross-interface contradiction was found at the proposed A2 parameters, conditional on D01's analytic theorem surviving its separate review. The exact mathematical source must be fixed as the law below. In particular H_seq is the source law; D_B is only a noise-proof intermediate, and an unspecified class of finite approximations is not one exact source experiment. The precise finite sampler convention below provides an explicit uniform polynomial approximation and the corresponding bridge charges.

D01's explanatory source paragraph refers to F_impl,H_impl, whereas A2 here chooses ideal truncated F and exact H_seq. Its actual extraction theorem allows ANY source kernel independent of S,G conditional on T, so this wording difference causes no extraction loss or theorem change. The canonical A2 source definition, rather than that example paragraph, must control the computational assumption and noise comparison.

## Fixed mathematical source and the dimension check

Let ell=ceil(log2 n), b=ell^2, tau=gamma=ell, sigma=2n ell^3, and

    d=floor(sqrt(n)/ell^4).

Take a fully split odd prime q with sigma n^c<=q<=n^K, for fixed positive c,K. Qualifying prime sequences are an input condition; no prime-generation result is supplied. The numerical interval requires K>1+c, which also makes it nonempty eventually before imposing primality and splitting. At K=1+c the ell^3 factor already makes the interval empty. All guarantees are asymptotic: use sufficiently large n for d>=ceil((ln n)^2) and D01's unspecified N_K.

Because ell>=ln n, the displayed d is at most floor(sqrt(n)/(ln n)^4). Also sqrt(n)/(ell^4(ln n)^2) tends to infinity, so the lower dimension condition holds eventually. Therefore A2 lies in D01's stated range, with no change of logarithm base hidden in a constant. One may use the stronger, exactly integer-checkable condition d>=ell^2 as a sufficient finite check for the lower endpoint; it too holds eventually. The floor defining d can be computed from integer square root and division by ell^4.

The ambient ring has coefficient dimension n. J_T has CRT dimension n-d, I_T=Ann(J_T) has dimension d, and R/J_T has dimension d. B below remains an n-by-n COEFFICIENT matrix; its dimension is not d. The target error is n independent coefficient D_sigma samples.

Order the n roots by their representatives in {0,...,q-1}; sample T uniformly among ALL d-subsets. Sample U with independent nonzero uniform active coordinates on T and zeros off T. Sample V independently uniformly in I_T, including zero active coordinates. Independently sample iid F_j from D_ell conditioned on [-b,b]. Form the integer negacyclic coefficient multiplication matrix M_F, and

    B=sigma^2 I-tau^2 M_F M_F^T.

Use the unique unit-lower-triangular LDL decomposition B=L diag(d_i)L^T in increasing coefficient order 0,...,n-1. The EXACT law H_seq is defined by the recursion

    c_i=sum_{j<i} L_ij y_j,
    h_i ~ mass proportional to exp(-pi(h_i-c_i)^2/d_i),
    y_i=h_i-c_i,

with fresh independent sampling randomness at each conditional draw. The centers use prior residuals y_j, not untransformed h_j. The public mathematical source is precisely (U+F,V+H_seq) mod q. No S or G is an input or an internally reused source variable.

## The retained kernels match

The fresh mathematical auxiliary is G~D_ell^n with its FULL integer law wrapped modulo q, independent of the entire source. It is not F's truncated law. The public second source test samples an independent fresh binary S_0 and G_0 of that public law and returns Y=S_0+G_0. Its sampling uses no hidden ideal, F, H or source coins.

D01 retains (T,J,U,F,H_seq,Y,pi_T(S)). Conditional on T, the source kernel is independent of S,G, so appending it is a valid common-kernel operation. The theorem's per-support bound therefore applies at A2:

    eta_ext <= (1/2) exp(-c_K n/(d(ln n)^6))
             = exp(-Omega_K(sqrt(n)/(ln n)^2)).

No support rejection, exceptional-support conditioning, or altered quotient output is needed. This application is conditional on the independently reviewed validity of D01's primary analytic import; R03 does not certify that import.

The noise edge instead retains only (J,U,F) and integrates H_seq,G out. Since abs(F_j)<=b always, ||M_F||_op<=nb and

    B>=3sigma^2 I/4,
    T_noise=tau^2 I-(tau^4/sigma^2)M_F^T M_F>=3ell^2 I/4.

Write kappa(s)=2sum_{j>=1}exp(-pi s j^2),

    delta_conv=(1+kappa(3ell^2/4))^n-1,
    eta_conv=delta_conv/(1-delta_conv),
    kappa_B=kappa(3sigma^2/4),
    eta_seq=min(1, [((1+kappa_B)/(1-kappa_B))^n-1]/2).

For sufficiently large n the denominators are positive. F02 gives the joint noise bound eta_noise<=eta_conv+eta_seq. Here eta_seq compares the center-dependent-normalizer law H_seq with D_B and appears ONLY in the noise edge. D_B is not another candidate source. These are exponent matrices, not assertions that an integer discrete Gaussian has exact covariance B/(2pi).

U is active-unit by definition, so F01's eta_iso is zero. This is a different source law from uniform U in I. The non-negligible polynomial-q cost 1-(1-1/q)^d cannot be discarded when comparing to an external assumption with unconditioned U; no such hardness import is made here.

## One explicit polynomial approximation convention

The mathematical source above is the fixed reference. The following convention demonstrates a concrete finite implementation whose distance from it is uniformly bounded; it does not redefine the reference as a tolerance class.

All sampler tapes use fresh independent fair bits. Set

    N_max=2n sigma+10,
    p=n+ceil_log2(1024 n N_max),
    L_cap=4n+ceil_log2(16n).

Here ceil_log2 on an integer is computed by bit length. Matrix entries of B are integers of magnitude O(n^2 ell^6). Reduced rational LDL takes polynomial bit complexity: leading principal determinants have O(n log n) bits by Hadamard, and positive pivots satisfy 3sigma^2/4<=d_i<=sigma^2. Reduce rational results after arithmetic operations; forward substitution has polynomial-size reduced outputs by the corresponding determinant bounds. No approximate eigenvalue decision is used.

For each H conditional kernel, enumerate the integers in abs(k-c_i)<=n sigma+2, in increasing order. The table has at most N_max entries. For F enumerate exactly [-b,b]; there is no tail omission from its defined truncated law. To approximate G or the target E in the reductions, enumerate the centered intervals abs(k)<=n tau+2 and abs(k)<=n sigma+2 respectively. Their ideal reference laws remain the full discrete Gaussians.

For every table exponent x>=0, a rational number, deterministically approximate exp(-pi x) within 2^(-p-3), clamp the approximation to [0,1], and round it DOWN to a multiple of 2^(-p). The resulting rational weight differs from the true weight by at most 2^(1-p). Set a zero exponent's weight exactly to 1. This approximation step can, for example, be implemented entirely in rational arithmetic as follows: approximate pi using the alternating Machin arctangent series; range-reduce a rational approximation to pi*x to u in [0,1] by powers of two; approximate exp(-u) by its alternating Taylor series with a certified remainder; then square back. Choose the internal error so that the final absolute error is at most 2^(-p-3), using |a^r-b^r|<=r|a-b| on [0,1]. This is a fixed deterministic rule once the smallest truncation orders meeting those error bounds are used, with increasing-series-index tie conventions. It avoids deciding whether an exact transcendental weight lies on a rounding boundary.

Every exponent encountered in the H table is O(n^2): d_i>=3sigma^2/4 and abs(k-c_i)<=n sigma+2. F, G and E exponents have the same polynomial bound. Thus O(p+log n) internal accuracy bits and polynomially many rational operations suffice. Exact rational squaring may increase bit lengths by a polynomial factor but remains polynomial. Any standard proved rational interval implementation of these specified error rules gives the same error guarantee; the source ensemble itself remains the unique H_seq law regardless of this implementation choice.

After rounding, multiply by 2^p to obtain integer weights, sum them to W, and draw an integer uniformly from {0,...,W-1} by binary rejection, capped after L_cap trials. Return the first table entry whose cumulative weight exceeds that integer. On a cap failure return the nearest integer to c_i (ties toward the larger integer), or zero in a centered F/G/E table. Each cap failure has probability at most 2^(-L_cap), uniformly over the complete preceding sampler history.

At least one H table point lies within 1/2 of c_i, and d_i>=1, so its true weight exceeds 1/4. The other tables contain their center zero. Hence every ideal truncated normalizer is at least 1/4. If N<=N_max weights each have error at most 2^(1-p), normalizing changes the categorical law by TV at most 4N*2^(1-p)<=2^(-n)/(128n). The chosen p also makes the rounded normalizer nonzero. This argument handles conditional centers uniformly, including rare histories.

The full one-dimensional normalizer at center c is at least sqrt(d_i)(1-kappa(d_i)) by Poisson summation. Comparing the omitted shifted-lattice tails with integrals starting at n sqrt(d_i) gives a per-H-stage tail at most 2 exp(-pi n^2)/(pi n), using kappa(d_i)<1/2. The same bound holds for the centered G/E samplers, whose widths are at least one. On a truncated H execution, abs(y_i)<=n sigma+2 and sum_j L_ij^2<=4/3, so abs(c_i)<=sqrt(4n/3)(n sigma+2). All centers and their exact rational descriptions have polynomial size; there is no unbounded intermediate-value assumption.

For support sampling, use a partial Fisher–Yates shuffle in the canonical root order, with each uniform integer choice sampled by the same capped binary rejection rule. Sample U's active values uniformly in {1,...,q-1} and V's in {0,...,q-1} similarly. On cap failure use an admissible value: 1 for U, 0 for V and the first remaining index for a shuffle step. This preserves the support cardinality and active invertibility on every branch. CRT conversion is exact modular linear algebra. Roots can be enumerated by testing field elements because q<=n^K with fixed K; this is polynomial in the promised input regime, even though it is not intended as an optimized implementation.

There are at most 5n categorical or uniform-integer draws in the source. A sequential maximal-coupling/hybrid bound, using the uniform transition errors above, gives the explicit conservative source distance

    xi_src <= 2^(-n)/64 + (2/pi)exp(-pi n^2)
                         +5n*2^(-L_cap) < 2^(-n)

for sufficiently large n. The bound can retain the full source tuple before wrapping, so it also bounds the public pair. It is NOT obtained by multiplying marginal success probabilities after conditioning. Similarly the reduction's (S,E) sampler and its independent Y sampler can each be implemented with xi_1,xi_2<2^(-n), respectively. Fresh S bits need no approximation. No exact finite sampler for transcendental Gaussian probabilities is claimed.

## Computational accounting, with no double charge

Use the exact H_seq source and full ideal Gaussian auxiliary in the mathematical noise/extraction proof. For a chosen finite implementation within xi_src and the finite reduction samplers above, F01 gives

    Adv_target(D) <= Adv_src_impl(B1_impl)+Adv_src_impl(B2_impl)
                     +eta_ext+eta_conv+eta_seq
                     +2xi_src+2xi_1+xi_2.                      (R03-1)

The two source distinguishers may differ. A public target-law approximation, if introduced, gets its own xi_tgt; none is needed for the mathematical target here. An exact planted-recovery transfer cannot be inferred from public target TV alone.

Under this convention H's finite approximation is included in xi_src and paid twice at the two source endpoints. It is not also added to the ideal noise edge. Eta_seq, by contrast, is the ideal H_seq-to-D_B comparison and is paid only in eta_noise. Neither term is an active-unit penalty. The exact source hardness assumption still concerns the specified joint correlated pair; no marginal assumption, unconditioned HLBDD source, or one-sample-to-many-samples inference is substituted.

## Updated separate-Y leakage threshold at A2's dimension

The D03 A1-specific threshold remains scoped to its larger output dimension. At A2,

    D_out=d log2 q=Theta(sqrt(n)/(ln n)^3).

For m independent observations Y_i=S+G_i with width tau=ell, the D03 scalar averaging argument gives bit error at most exp(-pi m/(4tau^2)) plus negligible wrapping error. Binary Fano bounds H(S|Y_vec) by n times binary entropy of that error. Conditional entropy continuity then gives the actual quotient-extraction distance

    eta_ext,separate >= 1-[H(S|Y_vec)+1]/D_out.

Consequently, for any fixed C>2/pi, m>=C tau^2 ln n makes the residual entropy O(n^(1-pi C/4) ln n)=o(D_out), so extraction TV is 1-o(1). A sharper sufficient threshold is

    m >= (4/pi)tau^2[(1/2)ln n+(4+epsilon)ln ln n],

for any fixed epsilon>0. The earlier A1 tau^2 log log n threshold is not an A2 conclusion. All these statements concern the explicitly revealed auxiliary observation collection; they are not public attacks on hidden RLWE auxiliaries. Common Y exposes one observation and does not incur this repeated-leakage loss.

For completeness, the new dimension also updates D03's COMMON-Y statistical status. D01's arbitrary conditional source-kernel extension applies to the entire Gamma_m, including a full stacked H_seq vector, whenever that source remains independent of S,G given T. Thus at A2's d and the same tau,q, its one-Y extractor supplies the extraction premise for D03's correctly defined common-K theorem as well. Together with the separately stated sqrt(m)-width completion, both statistical premises then have a common parameter regime, conditional on their reviews and the bound sigma_m n^c<=q<=n^K. The computational common-K source assumption is still new and unsupported, and this does not preserve the original fixed sigma for arbitrary growing m. The old D03 statement about an open extractor was scoped to the original A1 dimension and remains frozen as such.

## Most discriminating checks and limits

1. The active ideal and quotient both have dimension d; noise completion still uses n coefficients. A2 meets D01's lower/upper dimension conditions eventually, with no support rejection or prime exceptions added.
2. F is truncated; G is a fresh full D_ell law. H's conditional sampler uses F and its own past, never S,G,Y or V. Noise integrates H out, while extraction retains it. The imported hidden-G and Gaussian-sign counterexamples are therefore excluded by actual generative conditions.
3. H_seq is exactly defined, but is not exactly D_B. Its conditional normalizers are handled in eta_seq; finite table errors are uniformly bounded over all centers and charged through xi_src. The cached-prefix regression is avoided by pointwise transition bounds and coupling, not marginal products.
4. Direct active-unit sampling removes the bridge's rank loss, while changing the external source assumption. It does not justify borrowing an unconditioned ideal-point hardness statement.
5. The conditional one-sample conclusion has a common polynomial parameter regime for this stated extractor, completion and approximation interface. Computational pseudorandomness of the exact correlated A2 source remains open, and the analytic extraction import still needs its separate nonauthor review. Neither this refinement nor the earlier completion work establishes a hardness theorem.

No additional optimization or experiment is needed to decide these interface checks.
