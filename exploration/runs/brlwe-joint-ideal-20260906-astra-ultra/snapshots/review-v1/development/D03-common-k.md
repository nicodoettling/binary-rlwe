# D03-K: a conditional common-K multi-sample theorem

Author derivation, version 1 finalized 2026-09-06 at 15:15 UTC. This is a distinct m-sample source experiment, not a consequence of the one-pair assumption. All statements remain pending nonauthor review. Let R be a finite effectively represented commutative ring, J an ideal, I=Ann(J), Q=R/J, and pi:R->Q. In the application R=F_q[X]/(X^n+1).

## Exact source and statistical premises

Fix a mathematical joint source law

    Gamma_m=(J,U_1,...,U_m,F_1,...,F_m,H_1,...,H_m),  U_i in I,

defined without a binary secret input, and require a polynomial-time implementation with an explicit approximation bound as specified below. Given Gamma_m draw ONE K uniformly from Q, with independent randomness conditional on J, and publish

    Src_K,m = ((A_i,C_i)=(U_i+F_i,U_i K+H_i))_{i=1}^m.          (K1)

Here U_i K means the quotient multiplication map. The reference challenge consists of 2m independent uniform ring elements. The source need not expose J,U,F,H,K. H may depend on the entire U,F vector. It must not use the bridge's S or G; K is independent of all of Gamma_m conditional on J.

Independently of Gamma_m draw S from the target binary law and G from a fixed public law, and put Y=S+G. Let E_vec consist of m independent target errors, independently of Gamma_m. Assume

    TV((J,U_vec,F_vec,(F_i G+H_i)_i),
       (J,U_vec,F_vec,E_vec)) <= eta_N,m,                         (K2)

and

    TV((Gamma_m,Y,pi_J(S)),(Gamma_m,Y,Z)) <= eta_X,m,             (K3)

where Z is uniform in Q conditional on J and independent of the retained variables given J. Noise comparison K2 integrates out the ENTIRE H vector and G. Extraction K3 retains the ENTIRE H vector. The same Gamma_m and G laws occur in both premises.

## Conditional decision theorem

The target Tgt_m consists of m independent uniform a_i, one shared binary S, and independent target E_i, publishing ((a_i,a_i S+E_i))_i. For every polynomial-time test D there are two tests against K1:

    B1((a_i,c_i)_i): draw one s, draw independent target e_i;
                       return D((a_i,a_i s+e_i)_i).

    B2((a_i,c_i)_i): draw one independent y with law S+G;
                       return D((a_i,a_i y+c_i)_i).

Both use one source challenge, invoke D once, and perform O(m) ring operations besides sampling. Their finite advantages satisfy

    Adv_Tgt,m(D) <= Adv_SrcK,m(B1)+Adv_SrcK,m(B2)
                   +eta_N,m+eta_X,m.                           (K4)

The computational source bound occurs twice because these tests can have different advantages. There is no automatic factor m in the extraction error: a single quotient is extracted once. All dependence on m in the actual joint noise error and sampling approximation must still be charged. If every source test has advantage at most epsilon_K,m, then the right side is 2epsilon_K,m+eta_N,m+eta_X,m. Equivalently one source test has advantage at least half the positive remaining target gap.

Proof. Replace the entire uniform public-multiplier vector by U_vec+F_vec using B1. K2, after adjoining independent S and mapping the retained variables, replaces the responses by U_i S+F_iY+H_i simultaneously. K3 replaces the single pi_J(S) by Z. Define K'=Z-pi_J(Y). Conditional on every fixed (Gamma_m,Y), K' is uniform in Q; because Y is independent of Gamma_m, K' and Y are independent conditional on Gamma_m. Thus the resulting responses are

    U_i Z+F_iY+H_i = (U_i+F_i)Y + U_i K'+H_i.

This is exactly B2's output from K1 and an independent Y. For every fixed y the map ((a_i,c_i)) -> ((a_i,a_i y+c_i)) is a bijection of R^(2m), and therefore preserves the entire independent uniform reference law. Telescoping the two computational edges and two TV edges proves K4. It does not replace U_i K' by independent ideal points.

Because K1 defines V_i=U_i K directly, this theorem itself needs only U_i in I, not individual bijectivity. The candidate-A specialization still samples active-unit U_i, preserving uniform V_i marginals. At m=1 and bijective U_1, K1 equals the independent-uniform-V source once the F,H law is matched, since U_1K is uniform in I conditional on all source variables. Dropping active-unit conditioning would change this exact source law; it is permitted only as an explicitly reformulated common-K source, not an uncharged import of the old independent-V source.

The F01 implementation accounting applies at vector dimension m: if the implemented source differs by xi_src, B1's (s,E_vec) sampler by xi_1, B2's Y sampler by xi_2, and the public target law by xi_tgt, add 2xi_src+2xi_1+xi_2+xi_tgt. The unchanged factor on xi_2 uses pointwise preservation of uniformity even for an approximate independent y law. If the implemented source law itself is Gamma_m and K2/K3 are proved for it, do not charge xi_src again. Exact planted-success transfers require joint secret/transcript comparisons, as in F01.

## Why this is not the independent-ideal source

For fixed bijective U_1,...,U_m and N=|I|=|Q|, the map

    k -> (U_1 k,...,U_m k)

is injective, so its uniform image contains N points in I^m. The total variation from m independent uniform ideal points is exactly 1-N/N^m=1-N^(1-m). This is a statement retaining the U vector. It is not a lower bound on the public distance after forgetting U and adding F,H; proving that public distance small would require a new argument.

Mandatory hand control: R=F_3,J=0,U_1=U_2=1. The common-K pair takes (0,0),(1,1),(2,2), each with probability 1/3; independent ideal points give all nine pairs probability 1/9. Summing the three diagonal and six off-diagonal differences gives TV=2/3. Marginal uniformity is exact in both experiments. Thus a tensor product of one-sample ideal-image statements is false.

Repeated multiplication of one source pair by public ring elements can produce a common-K relation, but it need not preserve an independent uniform source comparator. In the noiseless field example, all generated rows satisfy a rank-one determinant relation. Any public rerandomization that repairs that issue needs its own statistical or computational proof; the published additional-RLWE route is discussed in D03.md.

## D03-N: rectangular stacked discrete completion

For coefficient dimension n and m output ring samples, put p=mn and

    M = (M_F1;...;M_Fm) in Z^(p by n),
    B = sigma_m^2 I_p-tau^2 M M^T,
    T = tau^2 I_n-(tau^4/sigma_m^2)M^T M.

Assume B is positive definite; this is equivalent to T being positive definite. These are Gaussian exponent matrices, not exact discrete covariance matrices.

Equivalently,

    B_ij = sigma_m^2 delta_ij I_n-tau^2 M_Fi M_Fj^T,
    T = tau^2 I_n-(tau^4/sigma_m^2)sum_i M_Fi^T M_Fi.            (N1)

A direct scalar continuous check is n=1,m=2,F_1=F_2=1. The B matrix has diagonal sigma_m^2-tau^2 and off-diagonal -tau^2; its eigenvalues are sigma_m^2 and sigma_m^2-2tau^2. Separate marginal complements would require only sigma_m^2>=tau^2, but this full continuous complement requires sigma_m^2>=2tau^2. For example sigma_m^2=3tau^2/2 passes both marginal tests and fails the joint test. This diagnostic does not assert a general wrapped impossibility.

All cross blocks are required. With G~D_tau^n and independently H_*~D_B on Z^p, completing squares gives, for z in Z^p and g in Z^n,

    ||g||^2/tau^2+(z-Mg)^T B^(-1)(z-Mg)
      = ||z||^2/sigma_m^2+(g-mu_z)^T T^(-1)(g-mu_z),
    mu_z=(tau^2/sigma_m^2)M^T z.                                (N2)

The identity follows by expanding, with T^(-1)=tau^(-2)I_n+M^T B^(-1)M. Rectangular M is allowed: B+tau^2MM^T=sigma_m^2I_p, and the Woodbury identity gives the displayed T. Hence the output probability is proportional to

    exp(-pi||z||^2/sigma_m^2) * rho_T(Z^n-mu_z).

Let delta_n(T)=sum_{k in Z^n,k!=0}exp(-pi k^T T k). Poisson summation on the INPUT lattice Z^n bounds the last factor, divided by sqrt(det T), between 1-delta_n and 1+delta_n. Normalizing therefore proves

    TV(MG+H_*,D_sigma_m^p) <= delta_n(T)/(1-delta_n(T))          (N3)

whenever delta_n(T)<1. This is a full p-dimensional product target. Wrapping modulo q is a common deterministic map and cannot increase TV. No cross-sample independence is inferred from marginals or discrete covariance matching.

For the EXACT mathematical source used in this note, choose H=H_seq as follows. Order coordinates first by sample index i=1,...,m, then by coefficient index j=0,...,n-1; take the unique unit-lower-triangular LDL decomposition with positive diagonal pivots, and use F02's exact one-dimensional Gaussian conditional kernels in that order. This defines a single probability law, with no unspecified rounding tolerance in its definition. Apply those kernels to the full p-by-p B. With beta=lambda_min(B), kappa(beta)=2sum_{j>=1}exp(-pi beta j^2), and the additional sampler condition kappa(beta)<1,

    eta_seq,p <= min(1, [((1+kappa(beta))/(1-kappa(beta)))^p-1]/2).

The proof is the same pointwise product-of-conditional-normalizers argument as F02, with p stages. Each LDL pivot is at least beta. The exact K1 source and K2/K3 premises all use this SAME H_seq law. Its noise error is at most N3+eta_seq,p. Every permitted finite implementation must have an explicitly proved uniform error eta_H from H_seq. Compare its whole source challenge to the exact mathematical source, include eta_H and all other source-sampling discrepancies in xi_src, and charge 2xi_src at the two source endpoints of the implementation theorem above. Approximation of B2's independent Y sampler belongs to xi_2. This convention does not call a class of samplers within a tolerance one exact source law.

A safe polynomial approximation uses rational LDL in dimension p, takes each conditional integer draw in |h_j-c_j|<=p sigma_m+2, and approximates each conditional table to total variation at most 2^(-n)/(10p). Capped tails are exp(-Omega(p^2)); all table lengths are O(p sigma_m). With constant slack, the centers have polynomial magnitude by the row-norm argument in F02. Matrix arithmetic costs O(p^3) arithmetic operations with polynomial bit lengths; O(p^2 sigma_m) table entries suffice for this conservative implementation. For m,sigma_m polynomial in n all costs and precision lengths are polynomial. This supplies a class of implementations each compared to the single exact H_seq source, not a replacement definition of its law. No sampler implementation was executed.

## Parameters and exact source change

Let the F_i coefficient laws be independent copies of the candidate-A bounded law, with absolute values at most b. Then

    ||M||_op^2 <= sum_i ||M_Fi||_op^2 <= m n^2 b^2.

Taking tau=ell=ceil(log2 n) and sigma_m=2nbtau sqrt(m) gives B>=3sigma_m^2 I_p/4, T>=3tau^2 I_n/4 and

    delta_n(T) <= (1+kappa(3tau^2/4))^n-1 = negligible(n).

The smoothing sum has dimension n, whereas the H sampler has dimension p=mn. Both errors remain negligible for every explicitly fixed polynomial sample bound m(n). In candidate A's Gaussian option gamma=ell,b=ell^2, this is sigma_m=2n ell^3 sqrt(m). Because sigma_m^2 is rational/integer in this choice, the matrix computation does not require exact representation of sqrt(m).

The original sigma_1=2n ell^3 is not unchanged. If one insists on a fixed target width sigma_1, the exact sufficient gate is

    tau^2 lambda_max(sum_i M_Fi^T M_Fi) <= (1-a)sigma_1^2,
    a tau^2 = omega(log n),                                    (N4)

with enough B smoothing for the H sampler. The conservative bound used here guarantees constant slack for m<=3 at sigma_1; it proves no such bound for growing m. Typical matrices may permit more samples, but no probabilistic operator theorem is imported or needed for the explicit sqrt(m)-growth variant.

For the baseline additionally require

    2n ell^3 sqrt(m) n^c <= q <= n^K,     q=1 mod 2n.            (N5)

Thus at m=n^r, the numerical exponent requirement is K>1+c+r/2, up to the log factors, along qualifying primes. At fixed q, the conservative sample allowance is m<=q^2/(4n^(2+2c)ell^6). This is a common parameter constraint, not a proof of prime availability at every requested exponent.

The source law has changed twice: V_vec now has one common K, and H_vec is sampled using the full stacked H_seq kernel. Even its H marginals are not asserted to equal the exact one-sample H_seq law. K4 therefore assumes pseudorandomness of K1 itself. One-sample source hardness and a sampler for the joint error do not establish that assumption. These changes are an m-sample variant of candidate A, not an admitted third source family.

The exact ideal-part entropy ledger in the active-unit specialization is log2 binom(n,d) support bits, md log2(q-1) U bits, and only d log2 q K bits, versus md log2 q bits for independent V points. Conditional on U the common V vector has exactly d log2 q bits. F contributes mn H(F_scalar)<=mn log2(2b+1) bits. H contributes its actual conditional entropy under the full H_seq law, not m independent copies of a scalar Gaussian entropy formula. The target secret still supplies n bits, and common-Y extraction asks for only d log2 q quotient bits at the same J,tau,q. These are actual distributional entropy statements; no hardness inference follows from them.

The exact mathematical F law in this variant is the displayed coefficient D_gamma conditioned on the finite interval [-b,b] (or the separately labeled exact uniform-sign choice). Uniform finite-field and support laws are exact mathematical laws too. A finite implementation is compared to this single source distribution via xi_src. A separately fixed executable source algorithm could instead be made the definition and analyzed directly, but no unspecified finite-precision policy is treated as such an algorithm here.

Finally m(n) is a prescribed public sample budget. With fixed q=n^K and a fixed reference gap exponent c, N5 limits how large that budget may be under the displayed sigma_m construction. This does not prove hardness of one fixed target parameter family against all polynomially bounded oracle query counts, nor does it turn a width-changing reduction into an unchanged-width result.
