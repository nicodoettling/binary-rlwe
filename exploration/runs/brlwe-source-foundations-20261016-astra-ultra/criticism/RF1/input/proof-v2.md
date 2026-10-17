# Proof of the EX-v2 noisy expansion and recovery theorem

The exact frozen statement is [expansion-theorem-only-v2.md](expansion-theorem-only-v2.md). Review status and exact accepted hashes are recorded separately in the run claim ledger and reconciliation. All computational hardness statements are conditional on the exact two-point Base2 premise at the specified new parameter family. The construction does not output the iid planted law Base_m.

## 1. Probability spaces and public interface

Write R=F_q[X]/(X^n+1), n a power of two, q>=n^2 an odd split prime. Coefficients identify its additive group with F_q^n and fix the pairing <z,x>=sum_i z_i x_i mod q. Define characters chi_z(x)=exp(2 pi i <z,x>/q). All noise below is sampled on integer coefficients and then reduced; no Gaussian law on finite-field CRT coordinates is used.

Set ell=log2 n, L=ceil(n sqrt(q)), b=(2n+1)L ell^2. Since q>=n^2 and q is an integer, L<=q. The interval box distribution P_R has independent coordinates uniform on {0,...,L-1}. P_W has independent integer D_L coordinates. For each output j, independently sample (R_j1,R_j2,W_j) from P_R times P_R times P_W, independently of the entire input pair. With A=(A1,A2), let K_A be the resulting single-output law of C=A1 R_1+A2 R_2+W. Conditional on A, the actual m-output law is K_A^{otimes m}. Unconditionally these outputs need not be independent. Our regularity theorem compares the full retained-seed law P_A(dA)K_A^{otimes m}(dC) against P_A(dA)Unif(R)^{otimes m}(dC), with P_A exactly uniform on R^2.

The source test computes this map using its only two supplied ring elements. It discards the pair and all expansion coins before giving the target solver the m RLWE pairs. It separately samples a common uniform binary S and independent iid coefficient D_sigma errors E_j, independent of input and expansion coins, computes responses C_j S+E_j, and tests the solver's output against S itself. There is no hidden-ideal basis, witness, source oracle, resampling oracle or conditional completion sampler in this algorithm. Retaining or revealing expansion coins occurs only in the planted-world guessing upper bound below, never in the comparator theorem or target interface.

## 2. Two elementary algebraic facts

For a ring element z, write k(z) for the number of its nonzero CRT coordinates; multiplication by z over F_q has rank k(z). If M_a is the coefficient negacyclic multiplication matrix, M_a^t=M_{a^*}, where the involution a^*(X)=a(X^{-1}) modulo X^n+1 reverses signed coefficients. This follows by taking transposes of the signed shift matrix, whose transpose is its inverse. The involution permutes ring elements and CRT roots. For uniform A, M_A^t z=A^* z is consequently uniform in the k(z)-dimensional ideal I_supp(z). No assumption that z or A is a unit is made.

Let z be a nonzero residue vector, lifted coefficientwise to centered integers in [-(q-1)/2,(q-1)/2]. Its integer multiplication determinant N(z)=det M_z is nonzero: X^n+1 is irreducible over Q for n a power of two. One direct proof applies Eisenstein at 2 to (X+1)^n+1: all nonleading binomial coefficients are even, while its constant term is 2 and not divisible by 4. Because M_z has rank k modulo q, integer Smith normal form has at least n-k nonzero diagonal entries divisible by q. Thus q^{n-k} divides the nonzero integer N(z), and |N(z)|>=q^{n-k}.

For the n complex roots zeta of X^n+1, the determinant is product_zeta z(zeta), and Fourier orthogonality gives sum_zeta |z(zeta)|^2=n||z||_2^2. Applying arithmetic-geometric mean to these n nonnegative values yields |N(z)|<=||z||_2^n. Therefore

    ||z||_2 >= q^(1-k(z)/n).                         (2.1)

In particular, 1<=k(z)<=n/2 implies ||z||_2^2>=q. This is a statement about any centered integer lift of a residue with small CRT support. It does not assume that its coefficient norm is already small, and it includes every CRT zero pattern.

## 3. Collision bound for the short coefficient box

Let R,R' be independent P_R samples, reduced modulo q, and D=R-R'. Its coefficients are independent. For any residue t, Pr[D_i=t] equals the size of the intersection of two length-L subsets of F_q divided by L^2, and hence is at most 1/L. This remains true when the integer difference wraps, because L<=q makes each interval injective in F_q.

For any rank-k F_q-linear system H D=0, choose k pivot columns. Conditional on all nonpivot coefficients, the k pivot coefficients have at most one required tuple. Their independence and individual maximum mass at most 1/L imply

    Pr[H D=0] <= L^(-k).                            (3.1)

The bound is pointwise in the conditioned nonpivot values, including rare branches; zero-mass branches contribute nothing. This is not a product of marginal bounds after arbitrary conditioning. The pivot tuple is fixed by the nonpivot tuple and the independent coordinate law supplies the product bound directly.

Write phi_R(y)=E_R chi_y(R). For any k-dimensional subspace V, character orthogonality gives

    E_{Y uniform V} |phi_R(Y)|^2
      = E_{R,R'} E_Y chi_Y(R-R')
      = Pr[R-R' in V^perp] <= L^(-k).              (3.2)

The orthogonality constraints defining V^perp have rank k. Applying the algebraic fact in Section 2 to two independent uniform seeds A1,A2 yields, for every z of CRT support size k,

    E_A |phi_R(M_A1^t z) phi_R(M_A2^t z)|^2
      <= L^(-2k).                                 (3.3)

All averages here are under the original uniform product seed law. No conditioning on the output, observed ratios, or survival events is used.

## 4. Discrete Gaussian Fourier bound with aliases retained

For an integer Gaussian D_L and real t in [-1/2,1/2], one-dimensional Poisson summation gives

    E exp(2 pi i t D_L)
      = [sum_{a in Z} exp(-pi L^2(a+t)^2)]
        /[sum_{a in Z} exp(-pi L^2 a^2)].           (4.1)

Both sums are positive, and the denominator is at least one. For integers a, (a+t)^2-t^2>=a^2-|a|. Since L>=1, the numerator is bounded by

    exp(-pi L^2 t^2)
       * [1+2 sum_{a>=1} exp(-pi L^2(a^2-a))]
      <= 4 exp(-pi L^2 t^2).                       (4.2)

For the last constant, the a=1 terms contribute 2; for a>=2, a(a-1)>=a, so the remaining sum is at most 2 e^(-2pi)/(1-e^(-pi))<1. This deliberately loose bound retains both nearest aliases. With product coefficient W and centered residue lift z,

    |phi_W(z)|^2 <=16^n exp(-2 pi L^2||z||_2^2/q^2).
                                                               (4.3)

The universal bound |phi_W(z)|<=1 is also available. Poisson summation can be proved by periodizing the Gaussian and computing its absolutely convergent Fourier series, as in the accepted September proof; it uses no computational or lattice-hardness input.

## 5. Full noisy expansion regularity

For fixed A, convolution and linearity give the exact coefficient character formula

    phi_{K_A}(z)=phi_R(M_A1^t z) phi_R(M_A2^t z) phi_W(z).

Finite-group Parseval gives the chi-square divergence to uniform as

    chi2(K_A || U_R)=sum_{z!=0}|phi_{K_A}(z)|^2.

For 1<=k(z)<=n/2, discard the box factors, use (2.1), (4.3), and L^2>=n^2 q. Each term is at most 16^n exp(-2pi n^2). There are fewer than q^n such terms. Their total is at most 16^n q^n exp(-2pi n^2).

For k(z)>n/2, discard the W factor and use (3.3). There are exactly binom(n,k)(q-1)^k residues of support size k. Since q/L^2<=1/n^2<=1,

    sum_{k>n/2} binom(n,k)(q-1)^k L^(-2k)
      <= 2^n (q/L^2)^(n/2) <=(2/n)^n.

Consequently E_A chi2(K_A||U_R)<=B_exp, where

    B_exp=16^n q^n exp(-2pi n^2)+(2/n)^n.          (5.1)

For each fixed seed, Cauchy-Schwarz gives TV(K_A,U_R)<=sqrt(chi2)/2. Jensen then gives E_A TV(K_A,U_R)<=sqrt(B_exp)/2. Conditional on that exact seed the m fresh outputs have product kernel K_A^{otimes m}. A product coupling or telescoping triangle inequality, with no adaptive selection, gives

    TV(K_A^{otimes m},U_R^{otimes m})<=m TV(K_A,U_R).

Averaging over the retained seed proves EX-REG with delta_exp=min(1,m sqrt(B_exp)/2). In particular this is valid for m=3, includes seeds with one or both zero CRT coordinates, and controls the entire joint law rather than just Gaussian marginals or coordinate covariance. The W term is essential to this proof: without it a pure ring-ideal-preserving expansion retains the all-zero root branch at mass at least q^-2, giving a public inverse-polynomial gap from m>=3 independent uniform outputs at polynomial q.

## 6. The planted law and the common ideal quotient

On the planted source write A_i=U_i+F_i, with the exact SC-v1 joint law. Let U'_j=U_1 R_j1+U_2 R_j2 in R. Each U'_j lies in the SAME ideal I_T, without requiring uniformity, conditional independence, active nonzero coordinates or full rank. Choose the integer mask lift

    F'_j=F_1 R_j1+F_2 R_j2+W_j

using integer negacyclic multiplication. Then C_j=U'_j+F'_j modulo q. Let C_lat retain T, U_1,U_2, F_1,F_2, all R_j1,R_j2, and all W_j. It determines all U'_j,F'_j. C_lat is independent of the fresh target S and, in the proof, an auxiliary G~D_ell^n. The F'_j need not have any independent Gaussian law; their dependence on one another and on U'_j is permitted.

Let Good require all 2n original F coefficients to satisfy |F_i,t|<=ell^2 and all mn W coefficients to satisfy |W_j,t|<=L ell. The elementary tail bound, using Z_t>=t and an integral from the integer cutoff t ell, is

    Pr[|D_t|>t ell] <= exp(-pi ell^2)/(pi ell)

when t ell is an integer, as here for t=ell or L. A union bound over (m+2)n coordinates yields Pr[not Good]<=delta_mask. Conditioning on Good only changes C_lat, leaving S,G independent with their original laws. No assumption of success independent of Good is made.

On Good each negacyclic product coefficient is bounded by n ell^2(L-1), and therefore

    |F'_j,t| <=2n ell^2(L-1)+L ell <=(2n+1)L ell^2=b.

Let M vertically stack the m integer negacyclic multiplication matrices M_F'j. The signed-shift representation gives ||M_F'j||<=nb and ||M||^2<=mn^2 b^2. At sigma=2sqrt(m)n b ell, the positive exponent complement

    B=sigma^2 I_{mn}-ell^2 MM^t >=3sigma^2 I/4

and the input smoothing matrix

    Theta=ell^2 I_n-(ell^4/sigma^2)M^t M >=3ell^2 I/4

are strictly positive. All off-diagonal sample blocks are retained. For each fixed good C_lat, draw H in Z^{mn} with mass proportional to exp(-pi h^t B^-1 h), independently of S,G. This is proof-only. G is shared by all m samples; H is the full joint Gaussian, not a product of separately completed blocks.

## 7. Completion and guessing, with normalization and witness

For completeness, the rectangular Gaussian calculation works for arbitrary p=mn. Completing squares in g gives

    ||g||^2/ell^2+(z-Mg)^t B^-1(z-Mg)
       =||z||^2/sigma^2+(g-mu_z)^t Theta^-1(g-mu_z),
    mu_z=(ell^2/sigma^2)M^t z.

Let P(z)=D_sigma^{p}(z), and r_z be the shifted Theta Gaussian integer sum divided by sqrt(det Theta). The exact law Q of MG+H satisfies Q(z)=P(z)r_z/E_P r. Poisson summation and Theta>=3ell^2 I/4 give |r_z-1|<=Delta=(1+kappa(3ell^2/4))^n-1. If Delta<1 then E_P r>=1-Delta and TV(Q,P)<=Delta/(1-Delta), capped at one. If Delta>=1 use the universal bound one. This is exactly eta. The normalizer is never dropped; the exponent matrix is not confused with the actual discrete covariance.

The comparison is pointwise for each good C_lat and hence retains that entire latent variable. S is independent of the entire compared pair and can also be retained. H is integrated out of this comparison; it is not appended separately to the independent-noise endpoint. Mapping to transcripts gives witness-retaining TV at most eta between the real good-branch planted transcript and

    ((U'_j+F'_j, U'_j S+F'_j(S+G)+H_j))_j.

Only in this completed world reveal (C_lat,H,Y,pi_T(S)), with Y=S+G in R and pi_T the d CRT coordinates on T. These data determine every displayed pair, because U'_j S depends only on pi_T(S). Conditional on any good C_lat,H, the joint law of (S,Y) is unchanged. The leakage pi_T(S) has at most q^d values for every fixed T, including empty fibers and all-zero U'_j tuples.

For any finite secret S and any observation Y, and any leakage f(S) of at most D values, summing the largest mass in each fiber gives P_guess(S|Y,f(S))<=D P_guess(S|Y). This inequality concerns unnormalized joint masses and remains valid on rare observation branches; it does not presume a uniform quotient. For iid uniform bits S and independent iid D_ell noise G, the integer-observation guessing probability is ((1+D_ell(0))/2)^n, by symmetry/unimodality in one coordinate and factorization of the full product law. Reducing Y modulo q only lowers guessing power. Thus planted success is at most

    q^d ((1+D_ell(0))/2)^n+eta+delta_mask.          (7.1)

The tail is paid additively and only once; a bad-mask branch can have success one. The source-test uniform endpoint differs from the target's FULL witness/transcript law by at most delta_exp, because EX-REG permits independently adjoining S and E and then computing responses and discarding seeds. Hence epsilon_m<=p_uniform+delta_exp<=Adv_Base2(B_Q)+p_planted+delta_exp, proving EX-REC. The acceptance test compares to the actual internally sampled S. Residual consistency is not used.

## 8. Explicit polynomial sample and modulus family

Fix h>=0 an integer before adversaries and m(n) a polynomial-time computable integer with 1<=m(n)<=n^h. Put K=h+10 and let q be the least prime 1 modulo 2n^K. Xylouris Theorem 1.1 gives q<=C(2n^K)^5.18<=n^{6K} eventually, since (6-5.18)K>0; also q>=2n^K+1. This is a particular effectively generated split-prime family, not a conclusion for every polynomial q. Trial division while enumerating progression candidates is already polynomial in unary n under this bound; exhaustive root enumeration is also polynomial, though the reduction itself needs no roots.

Since L<=n sqrt(q)+1<=2n sqrt(q) and 2n+1<=3n,

    sigma=2sqrt(m)n(2n+1)L ell^3
      <=12 sqrt(m)n^3 sqrt(q) ell^3.

It follows that q/(n sigma)>=sqrt(q)/(12sqrt(m)n^4 ell^3)>=sqrt(2)n/ (12ell^3), which tends to infinity. Thus q/sigma>=n eventually. The deliberately coarse constant and K=h+10 leave strict asymptotic slack.

For d=floor(n/(24K ell)), q^d<=2^{n/4}. The separate choice floor(sqrt(n)/ell^4) is eventually positive and lies below this bound because 24K/(sqrt(n)ell^3) tends to zero. Since Z_ell>=ell and D_ell(0)<=1/ell, the guessing term is at most 2^{-3n/4+n/(ell ln2)}, hence at most 2^{-n/2} eventually. Each d choice is its own computational source assumption.

At q<=n^{6K}, log B_exp's first summand is at most n log16+6K n log n-2pi n^2=-Omega(n^2). Its second summand is (2/n)^n=exp(-Omega(n log n)). Multiplication by m<=n^h after the square root preserves negligibility. Both eta and delta_mask are exp(-Omega(ell^2)) times fixed polynomial factors, hence negligible. All parameters and precision schedules precede Q and its success exponent. Therefore Base2 pseudorandomness at the chosen family forces negligible actual-secret success for the stated m-sample target.

For m=3 one can fix h=1 and restrict to n>=4; finite prefixes are irrelevant to the asymptotic statement. This proves a sample extension from two source points if the new proof gates close. For any one fixed h, it covers all specified m<=n^h at that h's q/noise family. It does not quantify over all polynomial sample exponents at one fixed modulus family. Its larger q and source d are not inherited from the September q=least-prime(1 mod 2n^3) premise.

## 9. Algorithmic cost and finite implementation

Apart from one Q call, the test uses n fair secret bits, 2mn independent uniform interval draws, mn coefficient D_L draws, mn coefficient D_sigma draws, 3m ring multiplications (two for expansion, one for responses), and O(m) ring additions plus one canonical equality check. Schoolbook multiplication takes O(m n^2) modular operations on O(log q) bits; sampled coefficients have polynomial magnitude at each fixed h,K. No resultant, CRT computation, matrix complement, or ideal witness is executed by the reduction.

Both L^2 and sigma^2=4m n^2(2n+1)^2 L^2 ell^6 are exactly represented integers. A bounded polynomial sampler exists as follows. Put tau_max=ceil(sigma), compute by integer square root, and cut all Gaussian tables at B_cut=(n+ceil(log2(mn+2))+2) tau_max. The two widths are at most tau_max; the total discarded probability is exp(-Omega(n^2)) times a polynomial factor. The table has polynomially many atoms for fixed h,K. Approximate each unnormalized Gaussian weight with absolute precision 2^{-n^2}/poly(mn B_cut), preserve the zero weight one, normalize and round to a dyadic law of polynomial precision. The normalizer is at least one, so raw L1 error and dyadic rounding give a polynomial multiple of the chosen small error. Independent bounded bit blocks sample these tables in worst-case polynomial time. Uniform interval coefficients may similarly use a dyadic approximation with per-draw TV at most L 2^{-r}, taking r=n^2+ceil(log2(2mnL+1))+O(1). All local errors together can be made 2^{-Omega(n^2)} times a polynomial, hence negligible without dependence on Q.

If xi_alg bounds TV of the entire local expansion/secret/error sampler from its exact joint independent law, xi_source bounds the planted pair's deviation from exact Base2, and xi_target bounds the complete target witness/transcript deviation, the implemented inequality adds xi_source+2xi_alg+xi_target. A nonexact uniform source comparator needs its own additional term. These are full-law errors; mere marginal sampler correctness is insufficient.

This proves existence of a uniform PPT wrapper for fixed h, with potentially very large polynomial exponents and memory. No practical cryptographic parameter estimate or implementation benchmark is asserted. Experimental local resource caps are separate from this asymptotic algorithm analysis.

## 10. Scientific boundary

The candidate adds a full noisy expansion regularity argument to the inherited common-quotient lossiness method. It preserves the original source budget of two points but changes the chosen q family and target noise substantially. It neither proves Base2 from standard RLWE nor generates independent planted Base_m points. It makes no target decision, quantum/nonuniform, practical-security or literature-priority claim. Certification, including falsification, primary source/parameter/complexity review, fresh blind review and exact dependency reconciliation, is recorded in the run ledger rather than inferred from this proof artifact.
