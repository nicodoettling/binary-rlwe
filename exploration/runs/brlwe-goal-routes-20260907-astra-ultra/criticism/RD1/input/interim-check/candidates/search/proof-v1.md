# A1 direct-search lossiness — complete author proof v1

Status: **PROVISIONAL, awaiting fresh nonauthor review.** This note proves the finite reduction from the frozen A1-T0 model and supplies a concrete Gaussian specialization. Its only computational assumption is explicitly stated below; it does not prove that assumption. The rectangular completion proof is included rather than treating historical NC1 v2 as certified. No active-ideal-point conditioning, quotient extraction, source oracle, or common-K source assumption occurs.

## 1. Exact finite model and the statement under review

Let R be a finite effectively represented commutative ring. Fix m>=1 and a law mu of

    C=(J,U_1,...,U_m,F_1,...,F_m),

where J is an ideal, U_i belongs to Ann(J), and |R/J|<=L. Let S~P_S and G~P_G be independent of one another and jointly independent of C. Conditional on C=c, sample H=(H_i)_i from a fixed kernel K_c independently of (S,G). This is the full product law

    mu(dc) K_c(dh) P_S(ds) P_G(dg).

Let E~P_E be independent of all these variables. No implementation of H or access to C is promised to any algorithm. Define Y=S+G. Assume the retained-source noise comparison

    TV((C,(F_i G+H_i)_i),(C,E)) <= eta_N.                 (N)

H and G are integrated out in (N). In particular (N) is not a claim after revealing the actual H realization.

The planted public transcript with its hidden witness is

    (S, X_pl) = (S, ((U_i+F_i,(U_i+F_i)S+E_i))_i).

The target has independent uniform a_1,...,a_m in R and the full product law P_a P_S P_E; a solver Q sees X_tgt=((a_i,a_i S+E_i))_i and outputs an element of R. Its success epsilon is Pr[Q(X_tgt)=S]. This is exact recovery of the sampled witness.

Source_m publishes exactly (U_i+F_i)_i, versus independent uniform a_i. For the intended m=1 and m=2 instantiations, the external source challenge always consists of **one pair** of ring elements: the m=1 algorithm ignores its second component, while m=2 uses both. No more source samples are available.

For every such solver Q there is the public source test

    T(a_1,...,a_m):
        sample fresh s~P_S and e~P_E independently;
        s_hat <- Q(((a_i,a_i*s+e_i))_i);
        return [s_hat=s].

It uses one source challenge, one Q invocation, no hidden source witnesses and no H or G sampler. Let Adv_Source(T) be the absolute acceptance-probability difference between the two source worlds. The finite claim is

    P_guess(S|X_pl) <= min(1,L P_guess(S|Y)+eta_N),        (1)
    epsilon <= Adv_Source(T)+L P_guess(S|Y)+eta_N.         (2)

One may replace L by E[|R/J|] if the upper bound is written in that form; fixed L suffices below. The exact runtime is at most

    T_Q+T_S+T_E+m(T_mult+T_add)+T_equal.

A randomized Q is included: condition on its independent tape and average. Equality checking refers to canonical ring-element encodings. If S has a designated injective binary encoding, the same test compares that encoding; invalid outputs reject.

## 2. Falsification gate: which witness-retaining law is actually compared?

Because S is independent of the ENTIRE pair (C,(F_iG+H_i)_i), appending S preserves (N):

    TV((S,C,(F_iG+H_i)_i),(S,C,E)) <= eta_N.

Mapping both sides by

    (s,c,n) -> (s, ((U_i+F_i,(U_i+F_i)s+n_i))_i)

gives

    TV((S,X_pl),(S,X_loss)) <= eta_N,
    X_loss=((U_i+F_i,U_i S+F_iY+H_i))_i.                (3)

This comparison retains the secret S and every source witness needed by the map. It does **not** retain H separately on the target side. That stronger assertion is generally false and is unnecessary.

Now reveal W=(C,H,Y,pi_J(S)) in the loss world only. Since U_i annihilates J, U_i S depends only on pi_J(S). Therefore a deterministic map from W computes every component of X_loss. This proves

    P_guess(S|X_loss) <= P_guess(S|W).                  (4)

The revealing operation in (4) does not claim W is a reduction input, does not transfer W through (3), and does not infer any public lower bound from latent distance. It is ordinary data processing for an upper bound on recovery. The actual source test samples only s,e and calls Q.

The full product law implies (C,H) is independent of (S,Y). Although H can strongly reveal F, and C reveals the secret ideal J, neither adds information about S before pi_J(S) is revealed. A kernel H depending on S or G would invalidate this argument; marginal laws and pairwise independence would not repair it.

An exact finite negative control illustrates why the full condition matters. In a four-element ring, let S be uniform and put H=S. H has the same marginal as independent uniform E, so the marginal noise comparison has TV zero when F=0. Yet TV((S,H),(S,E))=3/4. The false step is appending S to a comparison whose first noise already depends on S. Our product law excludes this model. Similarly, H=-G with uniform G has innocent uniform H and G marginals but their sum is identically zero; conditional independence excludes this case.

## 3. The quotient leakage inequality requires no extractor

For any finite secret S and countable observation Y, write

    P_guess(S|Y)=sum_y max_s Pr[S=s,Y=y].

Fix k=(c,h) of positive mass. The conditional (S,Y) law is unchanged by k. Let f_k(s)=pi_J(s), whose range has at most |R/J| values. Directly,

    P_guess(S|Y,f_k(S))
      = sum_y sum_z max_{s:f_k(s)=z} Pr[S=s,Y=y]
      <= |R/J| sum_y max_s Pr[S=s,Y=y].                  (5)

An empty fiber contributes zero. Averaging (5) over k proves

    P_guess(S|C,H,Y,pi_J(S)) <= L P_guess(S|Y).           (6)

This is a cardinality bound on an arbitrary leakage function. It never asserts pi_J(S) is uniform, close to uniform, collision-flat, or independent of Y. A nonuniform quotient is allowed. The same single quotient suffices for all m multiplications because every U_i annihilates the same J. There is no product over target samples.

Guessing probability is 1-Lipschitz in the total variation of the full witness/transcript law: for any fixed decoder its success is an event, and then one takes the supremum over decoders. Combining (3), (4), and (6) proves (1).

At T's uniform source endpoint, its complete witness/transcript law is exactly the target law, so its acceptance is epsilon. At its planted endpoint the complete law is (S,X_pl), so acceptance is at most (1). The difference in endpoint acceptance is bounded by Adv_Source(T), proving (2). No sign-preservation, target-decision hybrid, or success-amplification argument is used.

Residual verification would be a different test. A decoder may always return a valid preimage while rarely returning the sampled S. The source test here knows its locally sampled S and uses exact equality. The exact dual-number controls below show residual verification can accept both source worlds with probability 1 while exact-witness acceptance has a nonzero source gap.

## 4. Exact iid noisy-bit guessing and wrapping

Write D_tau(k)=exp(-pi k^2/tau^2)/Z_tau on Z, with Z_tau=sum_k exp(-pi k^2/tau^2). Let B be a uniform bit, G~D_tau independently, and Y_Z=B+G as an integer. For one bit,

    P_guess(B|Y_Z) = (1/2) sum_{y in Z} max(D_tau(y),D_tau(y-1)).

The discrete Gaussian is symmetric and nonincreasing in absolute value. For y<=0 the maximum is D_tau(y); for y>=1 it is D_tau(y-1). Both sums equal (1+D_tau(0))/2, so

    P_guess(B|B+G over Z) = (1+D_tau(0))/2.              (7)

More generally (7) holds for any symmetric unimodal integer mass function p, replacing D_tau(0) by p(0). It need not hold for an arbitrary multimodal noise law.

For S uniform in {0,1}^n and G with fully independent D_tau coordinates, the JOINT law is

    Pr[S=s,Y_Z=y] = 2^(-n) product_j D_tau(y_j-s_j).

The maximum over s factorizes coordinatewise because the support of S is the full Cartesian cube, and Tonelli factorizes the nonnegative sum over y. This exact factorization proves

    P_guess(S|S+G over Z^n) = ((1+D_tau(0))/2)^n.        (8)

No sequential conditioning is involved. If Y is reduced coefficientwise modulo q, it is a deterministic function of Y_Z, so

    P_guess(S|Y) <= ((1+D_tau(0))/2)^n.                 (9)

S remains a distinct ring element for every binary coefficient vector when q>=2. Wrapping can strictly decrease guessing probability, so equality must not be asserted without a separate wrapped calculation.

Poisson summation in one dimension gives Z_tau=tau sum_k exp(-pi tau^2 k^2)>=tau. Therefore

    D_tau(0)<=1/tau,
    q^D P_guess(S|Y)
       <= exp(D ln q - n ln 2 + n ln(1+1/tau))
       <= exp(D ln q - n ln 2 + n/tau).                (10)

The trivial D_tau(0)<=1 is always available at very small tau. Equation (10) is useful for tau growing or tau>=1; it is a legitimate upper bound even when greater than 1. A sufficient entropy budget for loss exp(-kappa) is

    D ln q <= n ln 2 - n ln(1+D_tau(0)) - kappa.        (11)

There is no leftover-hash or quotient-mixing hypothesis in (11).

## 5. Exact rectangular completion, with H used only in the proof

Let M be an integer p-by-n matrix; here p=mn and M stacks the m negacyclic multiplication matrices M_Fi. Fix sigma,tau>0 and assume

    B=sigma^2 I_p-tau^2 MM^t > 0,
    Theta=tau^2 I_n-(tau^4/sigma^2)M^t M > 0.

For positive definite B define the discrete Gaussian on Z^p

    Pr[H=h]=exp(-pi h^t B^(-1)h)/Z_B.

It exists because B is positive definite. Sample G~D_tau^n independently of H. Let

    delta(Theta)=sum_{k in Z^n, k!=0} exp(-pi k^t Theta k).

Then

    TV(MG+H,D_sigma^p) <= e_conv(delta),
    e_conv(x)=min(1,x/(1-x)) if 0<=x<1, and 1 if x>=1. (12)

The guard is essential. A negative denominator is never used as a bound.

Proof: for z in Z^p and g in R^n, completing the square gives

    ||g||^2/tau^2 +(z-Mg)^t B^(-1)(z-Mg)
      = ||z||^2/sigma^2 +(g-mu_z)^t Theta^(-1)(g-mu_z),
    mu_z=(tau^2/sigma^2)M^t z.                           (13)

The identities behind (13) are

    Theta^(-1)=tau^(-2)I_n+M^t B^(-1)M,
    Theta^(-1)mu_z=M^t B^(-1)z,
    B+tau^2MM^t=sigma^2 I_p.

They are valid for rectangular M, including zero and rank-deficient matrices; singular value decomposition verifies each singular direction and the orthogonal complement. Summing the exact independent integer law over g yields

    Pr[MG+H=z] = C exp(-pi ||z||^2/sigma^2) r_z,
    r_z = rho_Theta(Z^n-mu_z)/sqrt(det Theta).

Poisson summation yields the absolutely convergent identity

    r_z=sum_{k in Z^n} exp(-pi k^t Theta k) exp(-2pi i<k,mu_z>).

Thus 1-delta<=r_z<=1+delta. If P=D_sigma^p, the NORMALIZED convolution law is exactly Q(z)=P(z)r_z/E_P[r]. For delta<1, E_P[r]>=1-delta and |r_z-E_P[r]|<=2delta. Hence

    TV(P,Q)=(1/2) E_P[|r_z-E_P[r]|]/E_P[r]
            <= delta/(1-delta).

When delta>=1 use the universal TV<=1. This proves (12). No covariance matching, continuous-Gaussian replacement, or independent-marginal completion is substituted for this normalized integer calculation.

If M is fixed by latent C, G keeps its stated iid law conditional on C, and H has the displayed kernel independently of G conditional on C, the same bound holds retaining C whenever it holds uniformly on C. This follows by averaging conditional TV. Wrapping modulo q contracts TV. Thus (12) establishes exactly (N), with all source witnesses retained and H integrated out.

The proof never samples H in an executable algorithm. Consequently it needs no H_seq approximation, no eta_seq term, no efficient matrix-Gaussian sampler, and no finite precision implementation of B^(-1). Defining H mathematically is sufficient. This is a narrower analytic dependency than historical NC1 v2's sampler claims.

## 6. One and two samples: full stacked matrix and explicit widths

Let R=Z_q[X]/(X^n+1), n a power of two, q odd. Treat each F_i as an integer coefficient vector with |(F_i)_j|<=b, b>0. Its negacyclic multiplication matrix satisfies

    ||M_Fi||_op <= ||F_i||_1 <= nb,

because it is a sum of coefficient-weighted signed orthogonal shifts. For the VERTICAL STACK M,

    ||M||_op^2 = ||sum_i M_Fi^t M_Fi||_op
                <= sum_i ||M_Fi||_op^2 <= m n^2 b^2.

Set

    sigma_m=2 sqrt(m) n b tau.                          (14)

Then tau^2||M||_op^2<=sigma_m^2/4, B>=3sigma_m^2 I_(mn)/4, and Theta>=3tau^2 I_n/4. In particular all positivity hypotheses hold even when one or every F_i is zero. The b=0 case can instead choose any positive sigma and H~D_sigma^(mn); the formula (14) intentionally assumes b>0.

For t>0 define

    kappa(t)=2 sum_{j>=1} exp(-pi t j^2)
            <= 2exp(-pi t)/(1-exp(-3pi t)),
    Delta_N=(1+kappa(3tau^2/4))^n-1,
    eta_N=e_conv(Delta_N).                             (15)

The geometric bound uses j^2>=1+3(j-1). Since Theta>=3tau^2I_n/4, delta(Theta)<=Delta_N by comparison with the product theta sum. This proves (N) with the explicit guarded (15).

For m=1, H is n dimensional and sigma_1=2nbtau. For m=2, H is 2n dimensional and sigma_2=2sqrt(2)nbtau. Its parameter matrix is

    B = [ sigma_2^2 I_n-tau^2 M_1M_1^t, -tau^2 M_1M_2^t;
          -tau^2 M_2M_1^t, sigma_2^2 I_n-tau^2 M_2M_2^t ].

These off-diagonal blocks are present because the **same G** is used in both responses. Independent separately completed H_1,H_2 would generally leave cross-sample dependence. The desired E in (12) is genuinely iid D_sigma_2 over all 2n coefficients; its samples are independent as well as its coefficients. The smoothing sum still has dimension n, which is the number of shared G coordinates. There is one use of (N), one quotient charge, and one source challenge for either sample count.

The abstract proof works for any fixed m for which a complete source tuple exists. The claimed hardness instantiation below remains m in {1,2}; the actual source only provides two elements. Repetition, extra target samples, and any expansion are excluded unless separately proved.

## 7. Actual equal-small-noise source and finite search inequality

For a fully split prime q, index the n CRT roots of X^n+1. Fix 0<=D<=n and draw T uniformly among all D-element subsets. Let I_T be the CRT ideal supported on T, and J_T=Ann(I_T), so |R/J_T|=q^D. Conditional on T, draw U_1,U_2 independently uniform in I_T, including zero coordinates. Draw F_1^infty,F_2^infty independently with iid integer coefficient D_ell law, independent of T,U_1,U_2. The source worlds are exactly

    Base_2: (A_1,A_2)=(U_1+F_1^infty,U_2+F_2^infty) mod q,
    Unif_2: two independent uniform elements of R.       (16)

This is the independently specified two-point same-hidden-ideal HLBDD specialization identified by the coordinator's primary-source audit. It contains no binary secret, target response, auxiliary G or completion H. Computational hardness of (16) is an explicit assumption, not a consequence established here. The relation to primary Section 7 and the canonical/coefficient convention is to be checked independently by the coordinator. In coefficient convention, D_ell becomes canonical spherical parameter sqrt(n)*ell because the power-of-two canonical transform scales Euclidean norm by sqrt(n).

Take ell=ceil(log2 n), b=ell^2, tau=ell. For m=1 use only A_1. For m=2 use A_1,A_2. Condition the USED m source masks on the event B_F that all their coefficients lie in [-b,b]. The resulting conditional law has independent D_ell coefficients truncated to that interval; U_1,U_2 and T retain their original joint law because the box event concerns independent F masks. The unused second mask in the m=1 source may retain its untruncated law. The full relevant tuple comparison costs

    delta_F,m = Pr[not B_F]
              <= mn * exp(-pi ell^2)/(pi ell).          (17)

To check (17): Z_ell>=ell; monotonicity and the Gaussian integral bound give

    Pr[|D_ell|>ell^2]
      <= (2/ell) int_(ell^2)^infty exp(-pi x^2/ell^2) dx
      <= exp(-pi ell^2)/(pi ell).

A union bound suffices; no success/noise-event independence is asserted. One may replace (17) by the exact tail probability or min(1,the displayed upper bound).

Let epsilon_m be success of Q on m independent uniform-a target samples sharing binary S and independent coefficient errors D_sigma_m, where

    sigma_m=2 sqrt(m) n ell^3.

Define the actual source test, accepting the single pair (a_1,a_2), as

    T_m(a_1,a_2):
        sample S uniformly in {0,1}^n;
        sample E_1,...,E_m independently with iid coefficient D_sigma_m;
        s_hat <- Q(((a_i,a_i*S+E_i))_(i=1)^m);
        return [s_hat=S].

The entire second source element is ignored when m=1. Applying (2) to the bounded conditional source and then paying (17) once gives the finite theorem

    epsilon_m <= Adv_Base_2(T_m)
                 + q^D ((1+D_ell(0))/2)^n
                 + eta_N + delta_F,m,   m in {1,2}.    (18)

All quantities have been defined, and eta_N is exactly (15), with tau=ell. In particular there is no eta_iso, delta_act, eta_X, eta_seq, source broadening, or second computational hybrid. The exact same source assumption (16) supports both sample counts, with their different target widths.

The source distinguisher samples its own S and verifies exact Q output. It never tries to recover F_i, choose active U_i, identify T, construct a quotient, draw a source challenge, simulate a conditional posterior, or sample H. The source provides two independently noised ideal points; neither of them is relabelled a completion noise.

## 8. Finite implementation and explicit bit complexity

Equation (18) is an exact distributional statement. A Turing machine uses a finite approximation to the target-error sampler. Let xi_alg bound TV between its entire fresh (S,E_1,...,E_m) law and the exact product law, uniformly and independently of its source input. Binary S uses n exact fair bits, so xi_alg can consist solely of the Gaussian error. Let xi_source bound TV between the supplied planted pair and (16), while its comparator remains exact Unif_2. Let xi_target bound TV of the full target witness/transcript law from the mathematical target. Then a safe executable inequality is

    epsilon_actual <= Adv_actual-source(T_m,impl)
       +q^D ((1+D_ell(0))/2)^n+eta_N+delta_F,m
       +xi_source+2xi_alg+xi_target.                    (19)

Reason: approximating the test's local sampler changes acceptance in each source world by at most xi_alg; approximating the planted source changes one endpoint by at most xi_source; and the actual target changes success by at most xi_target. No completion-sampler error is present. If the source comparator is also approximate, its own TV error must be added. If target success is defined using the identical implemented sampler as T, one can save one xi_alg term; (19) keeps the conservative exact-target convention.

At the proposed polynomial-width parameters all required public samplers have deterministic polynomial bounds. sigma_m^2=4m n^2 ell^6 is an integer, so no irrational Gaussian-width input is required. For each target coefficient, truncate to integer |e|<=B_E with

    B_E=2m n^2 ell^3 >= n sigma_m.

The omitted mass per coordinate is at most exp(-pi n^2)/(pi n), by the same monotone-integral argument and Z_sigma>=sigma. For mn coefficients the tail is at most m exp(-pi n^2)/pi. Enumerating the O(B_E) weights exp(-pi e^2/sigma_m^2), approximating them to suitable dyadic accuracy, normalizing and sampling a dyadic table gives any chosen error 2^(-poly(n)) in polynomial time. Precision O(poly(n)+log(mnB_E)) bits suffices for total absolute probability error after summing the finite table. Elementary interval evaluation of pi and exp to that precision is polynomial in input size; all exponents have polynomial-size descriptions. The machine can use exact finite dyadic sampling and never run an unbounded Gaussian rejection loop.

Naive ring multiplication uses O(n^2) operations on O(log q)-bit modular integers. With m fixed, the arithmetic overhead is polynomial in n,log q and the error-table precision, and input length is O(mn log q). Source sampling is not part of the reduction; an efficiently generated source family can use exact uniform subset sampling, CRT arithmetic and negligible-error Gaussian tables, with any implementation distance charged as xi_source. A public primitive 2n-th root or full CRT description is permitted as public parameter metadata, shared identically by both source worlds and target. At q<=n^K even deterministic enumeration of field elements is polynomial in n; no hidden ideal information is thereby supplied.

## 9. A coherent polynomial-modulus family

Fix n through growing powers of two, ell=ceil(log2 n), m in {1,2}, and

    D=d=floor(sqrt(n)/ell^4),
    tau=ell, b=ell^2, sigma_m=2sqrt(m)n ell^3.

Take q the least prime congruent to 1 modulo 2n^3. The inherited PR1 import states q<=C(2n^3)^5.18, hence q<=n^16 eventually, while q>=2n^3+1. This primary prime theorem must receive the coordinator's fresh import check; it is not certified by this author note. These bounds imply q fully splits X^n+1, q/sigma_m>=n eventually (c=1), and O(log n)-bit modulus representation. Constants c=1 and K=16 are fixed before choosing any solver or its success exponent.

At these parameters,

    D ln q = O(sqrt(n)/(ln n)^3)=o(n),
    q^D ((1+D_ell(0))/2)^n <= exp(-n ln 2+n/ell+o(n))
                              = exp(-Omega(n)),
    Delta_N <= exp(-Omega((ln n)^2)),
    eta_N <= exp(-Omega((ln n)^2)),
    delta_F,m <= exp(-Omega((ln n)^2)).                  (20)

The completion estimate uses n*kappa(3ell^2/4)=exp(-Omega(log^2 n)); eventually Delta_N<1/2, so the guarded denominator is positive and eta_N<=2Delta_N. All implementation distances can be chosen negligible with polynomial resources as above. Thus (19) yields

    Adv_Base_2(T_m,impl) >= epsilon_m-negl(n).            (21)

If the explicit two-point source (16) is computationally indistinguishable from Unif_2 for every uniform randomized polynomial-time test along this fixed parameter family, then every such target solver's recovery success is negligible. This is a full asymptotic PPT search-hardness implication for exactly one or exactly two target ring samples, at polynomial q and q/sigma_m>=n. It is conditional on the source assumption and on the imported existence of the parameter family; it is not unconditional binary-RLWE hardness. Whether (16) follows from a more standard assumption is not proved here.

The lossiness calculation allows larger quotient dimension: for any fixed delta>0, condition D ln q<=(ln 2-delta)n and growing tau=ell eventually makes (10) exp(-Omega(n)). This is solely a mathematical entropy range. Changing D changes the source assumption and its plausible difficulty. The main concrete consequence (21) retains the historical rich-support d rather than asserting hardness for every larger support.

## 10. Exact finite controls, failed shortcuts, and literature comparison

The authorized experiment `exact_controls_v1.py` ran once with exact fractions, no randomness, and a 120-second external timeout; it finished in 0.017 seconds. Inputs and complete outputs are in `exact_controls_v1.json`. Finite enumeration is evidence against local mistakes, not proof of the asymptotic implication.

- Symmetric triangular noise p(-2),...,p(2)=(1,2,3,2,1)/9 gives one-bit unwrapped guessing 2/3, modulo-3 guessing 1/2, and modulo-5 guessing 11/18. Dimensions 1,2,3 match exact coordinate products.
- For all 16 two-label leakage maps on two bits with a nonuniform noisy observation, baseline guessing is 25/64 and maximum revealed guessing 21/32, below the charged bound 25/32. This tests arbitrary, nonuniform leakage functions without extraction.
- In R=F_2[t]/(t^2), take J=(t), U_i independent uniform {0,t}, F_i=H_i=E_i=0, and S,G independent uniform R. Full retained witness simulation is exactly equal by enumeration. Planted guessing is 3/8 for one sample and 7/16 for two, both below the single quotient budget 1/2. The fixed lexicographic valid-preimage solver has target success 11/16 and 55/64 respectively, with source acceptance gaps 5/16 and 27/64. Checking residual consistency instead accepts both worlds with probability 1.
- Shared G with F_1=F_2=1 and H_1=H_2=0 yields exactly uniform marginal errors but a diagonal joint pair at distance 3/4 from the independent product. This rejects separate marginal completion as a two-sample proof.
- H=S leaves zero marginal noise distance from independent uniform E but creates witness-retaining distance 3/4. H=-G makes the sum deterministic. Both violate the declared product law.
- The historical CP-1 normalization is reproduced: posterior A_b=21/2000, C_b=1/20, D=879/1000; the selected event is 21/2000>1/100 although the later residual incidence is 21/221<1/10. Its invalid sequential product is rejected. Our only product of success terms is the direct Cartesian maximization and summation in (8), with full independence explicitly given.

Other imported regressions are addressed as follows. R01's binomial ideals are not used; T is a rich uniform subset. R02's hidden G coins are excluded by the full C,S,G independence. R03–R05 remain counterexamples to marginal or pairwise assumptions; the full source tuple and iid target E are explicit. R06 entropy-only extraction and R07 field kernel/Boolean-fiber shortcuts are not invoked: (5) is the exact finite leakage-cardinality bound and the residual entropy is computed through noisy bits. R08 and C02 latent/public projection controls survive because (4) upper-bounds public recovery using more latent information; no lower-bound transfer is asserted. R09–R10 strict uniqueness/norm gates are unused. R11's sometimes-lossy shortcut and R12's verified-preimage shortcut are avoided by direct average guessing and equality with the sampled witness. R13's signed-advantage issue is absent from the single exact-success source test. R14's active zero coordinates are allowed and tested. R15/common-K and separate-Y controls are handled by the full rectangular completion of the actual available tuple; no source expansion is claimed. R16–R17's structural surrogates are not used. NC1-v1's negative denominator is guarded. C03's adaptive H_seq normalization and nonexact discrete covariance do not enter because H is exact proof-only D_B and the convolution uses Poisson normalization. Signed or wrapped deconvolution is never assumed.

The proof method follows the noise-lossiness idea in Brakerski–Dottling, *Hardness of LWE on General Entropic Distributions*, especially the lossiness viewpoint and Section 4 search reduction. Its public matrix source is different here: a specified hidden-ideal tuple replaces an ordinary lossy matrix, and the independent-summand discrete comparison is proved directly. No ordinary-LWE theorem is imported onto ring multiplication matrices. [Primary paper](https://eprint.iacr.org/2020/119.pdf).

The supplied ring paper's Theorem 6.9 uses DSPR plus Ring-LWE and has an entropy cost involving a full-degree short-basis determinant; its introduction explains why that instantiated threshold excludes binary secrets. Our conditional claim uses the explicit hidden-ideal source (16) and charges only the chosen quotient cardinality. It does not claim that the supplied paper already proves this source assumption or the new implication. [Primary paper](https://eprint.iacr.org/2020/1185.pdf).

Local `pdftotext` and Python PDF libraries were unavailable; ordinary source access was recovered through the approved primary-PDF web tool. No package was installed. The local reading notes and public primary statements were consulted. These were source-access limitations, not content-policy interruptions. No content-policy interruption occurred in this assignment.

## 11. Dependency closure still required

The elementary finite proof, exact noisy-bit identity, rectangular convolution derivation, and parameter substitution above are author derivations, not final certifications. Fresh nonauthor review must check their exact current versions, the finite controls, and all probability interfaces. The coordinator separately owns primary verification of the same-ideal HLBDD interpretation and the polynomial split-prime family. The computational source assumption remains explicitly assumed even if those imports are checked. No extra target samples, decision hardness, ordinary-RLWE source reduction, or worst-case hardness is asserted. The theorem-only packet omits this proof so a blind reviewer can reconstruct or refute it independently.
