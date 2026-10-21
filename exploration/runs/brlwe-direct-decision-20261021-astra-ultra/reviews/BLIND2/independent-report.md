# BLIND2 independent statement-only report

Review target: the immutable statement hashes in verified-input-hashes.json. Scientific exposure is recorded completely in exposure-log.md. This report was reconstructed without current author proofs, repair records, coordinator scientific logs, or other reports. Mathematical claims in the packet were treated as claims to prove, not accepted premises. The expressly designated historical interfaces are used only in their stated scopes.

## Verdict and exact scope

I find no counterexample to the displayed quantitative bounds in MR-v1, SFUNC-v2, DD1-EXTRACT-v1, DD2-AM1-SNF-v1, DD2-PRIMES-v1, AM-MAIN-v3, or the mathematical reduction asserted by FIXED-MAIN-v1. Proof reconstructions follow below. The new analytic component claims are locally accepted. AM-MAIN-v3 and the fixed-target reduction follow conditionally on the exact inherited B-GP-v2, C-OHCP-v8CORE, and A-FRAC full-law completion interfaces. This is not a fresh proof of C8, certification of unrestricted ideal hardness, a claim that the restricted source family is hard, or a quantum composition certificate.

There is one wording gate for an unqualified acceptance of the complete FIXED-MAIN-v1 text. Its final sentence says that “all target calls” use the independent coefficient discrete-Gaussian law. If this means the actual distributions passed to D0, it is false: deterministic rounding produces only the TV comparison proved in MR-v1, and public multipliers can already be nonuniform. What is correct is that D0's distinguishing promise concerns exactly one fixed-modulus target law, and every actual code execution is on a valid input at that modulus; the full rounded law is compared to the promised law statistically. The explicitly required all-input code access is enough for the reduction. Replace the final sentence's exact-call reading with that precise distinction. No quantitative bound needs weakening.

For example, if q0 is even and the auxiliary q is odd, a deterministic map from one uniform coefficient in Z/qZ to Z/q0Z cannot have an exactly uniform output: each output probability is an integer divided by q, whereas 1/q0 is not. This persists at auxiliary primes satisfying every large-parameter guard. Consequently no claim of exact physical target-law simulation can be inferred from the valid TV theorem.

Local claim graph:

| Claim | Local verdict | Dependencies and restrictions |
|---|---|---|
| SFUNC-v2 | ACCEPTED | Exact joint law, Gaussian envelope, Poisson summation |
| DD2-AM1-SNF-v1 | ACCEPTED | Distinct listed primes; one fixed partition; nonzero ternary norms |
| DD1-EXTRACT-v1 | ACCEPTED | All-input code; fresh coins; shared S; disjoint test bank; Hoeffding |
| MR-v1 | ACCEPTED | Both full endpoints; scalar Gaussian normalizers retained |
| DD2-PRIMES-v1 | ACCEPTED conditional on cited effective Linnik theorem | Primary publisher source checked; numerical, not logarithmic, runtime |
| AM-MAIN-v3 | CONDITIONAL ACCEPT | Exact historical B-GP/C8 interfaces and A-FRAC completion; true supplied guards |
| FIXED-MAIN-v1 mathematical reduction | CONDITIONAL ACCEPT | AM, MR, same pointwise J premise, bounded D0 code |
| FIXED final exact-physical-law reading | REJECTED | Rounded calls need not equal the target law; wording clarification required |

These are local review verdicts. Global final acceptance additionally requires the coordinator's current dependency graph, all historical regressions, edited-text reconciliation, and clean artifact checks. Same-model review agreement is correlated review, not formal verification or independent statistical evidence.

## 1. MR-v1 reconstructed with both endpoints and all normalizers

Write f_sigma(x)=sigma^(-1) exp(-pi*x^2/sigma^2), so its integral is one. Set lambda=q/Q<=1 and T=lambda*sum_e f_sigma(lambda*e). Poisson summation gives T>=1. By layer-cake integration, the number of lambda-grid points in any interval differs from its length divided by lambda by at most one. Applying this to every superlevel interval of the Gaussian yields

    0 <= T-1 <= lambda/sigma.

Fix any real shift c and let I_m=[m-1/2-c,m+1/2-c). The unnormalized mass of rnd(lambda*E+c)=m is

    V_m=lambda*sum_(lambda*e in I_m) f_sigma(lambda*e),

where E has the EXACT law D_(Z,sigma/lambda). Thus its actual normalized probability is V_m/T. Let W_m=integral_(I_m) f_sigma. For every height, the intersection of a Gaussian superlevel set with I_m is an interval; the same grid-count discrepancy gives

    |V_m-W_m| <= lambda*sup_(I_m) f_sigma.

For any unit-interval partition, sum_m sup_(I_m) f_sigma <= 1+integral|f_sigma'|=1+2/sigma. Therefore

    TV((V_m/T)_m,(W_m)_m)
      <= [sum_m |V_m-W_m|+(T-1)]/(2T)
      <= lambda/2+3lambda/(2sigma) <= 2lambda.

This explicitly retains the source discrete-Gaussian normalizer; it does not assume it equals its continuous integral.

Next, TV(G_sigma+c,G_sigma)<=|c|/sigma, by integrating the derivative of the translated density. Deterministic rounding cannot increase this distance. To compare rounded G_sigma with the EXACT D_(Z,sigma), put g(x)=f_sigma(rnd(x)). Integration over each nearest-integer cell shows

    integral |g-f_sigma| <= (1/2) integral |f_sigma'|=1/sigma.

Its integral is Z=sum_m f_sigma(m)>=1, and Z-1<=1/sigma. Normalizing g and using data processing by rnd gives

    TV(rnd(G_sigma),D_(Z,sigma)) <= 1/sigma.

Consequently, for every c,

    TV(rnd(lambda*E+c),D_(Z,sigma))
       <= 2lambda+(|c|+1)/sigma.                         (MR-scalar)

Reduction modulo q can only reduce this distance.

Now fix S and every original public coefficient representative Abar. Put Ahat=rnd(lambda*Abar), before its final reduction modulo q. Because rnd is integer-translation equivariant and lambda*Q=q is an integer,

    rnd(lambda*Bbar) = Ahat*S + rnd(lambda*E+C) mod q,
    C=(lambda*Abar-Ahat)*S.

Negacyclic multiplication merely inserts signs in each coefficient sum. Binary S and individual rounding errors in [-1/2,1/2] give |C_l|<=n/2. Conditional on S and all Abar, all error coordinates remain independent. Apply (MR-scalar) to the kn coordinates, couple or telescope the conditional product laws, and then average over S,Abar. This is a full-law comparison retaining S and every sample, not a comparison of one-sample marginals after averaging S.

Each public output coefficient has a bucket count differing from Q/q by at most one, hence its TV from uniform Z/qZ is at most lambda (indeed lambda/2 suffices). Replacing all public output coefficients by independent uniforms loses at most kn*lambda. The planted full-law distance is thus bounded by the stronger expression

    min(1,kn*(3lambda+(n/2+1)/sigma)),

which implies MR-v1's stated kn*(5lambda+(n/2+2)/sigma).

In the comparator, all 2kn public/response coefficients are originally independent uniform modulo Q, and deterministic separate rounding preserves independence. The same bucket estimate gives the claimed min(1,2kn*lambda). Summing the TWO endpoint losses proves (MR). Neither the target q nor sigma needs a primality or splitting hypothesis.

Under the stated width and auxiliary-modulus guards, the two terms in (MR) are each <=epsilon/8, so the signed gap moves by at most epsilon/4. This proves the common orientation and absolute gap >=3epsilon/4 pointwise in Q. The derivation permits fixed identical metadata and any distribution on binary S; retaining uniform shared S in particular is valid. The auxiliary width is exactly sigma/lambda, not a rounded surrogate. All Gaussian interpolation in this argument is analytical; the actual comparison laws are discrete.

## 2. SFUNC-v2: selected index is covered by the joint posterior formula

Let C={0,1}^n, c0=(1/2,...,1/2), and m(c)=max_(j,v) N(c,j,v). The exact Bayes success is

    p_selected = [2^n rho_t(J)]^(-1)
      sum_y max_(j,v) sum_(b in C: b mod J=y mod J, F_j(b)=v)
                                  rho_t(y-b).           (S1)

Randomization cannot improve the pointwise maximum. With u=sqrt(t^2+r0), completion of a square gives

    rho_t(y-b) <= exp(pi*n/(4r0))*rho_u(y-c0)

for every y,b. The norm |b-c0|^2=n/4 is exact. Apply this pointwise BEFORE maximizing in (S1), so the inner maximum is at most m(y mod J) times that common envelope. For each occupied coset c, Poisson summation gives rho_u(J+c-c0)<=rho_u(J). Also the exact Poisson normalizer ratio satisfies

    rho_u(J)/rho_t(J)
      =(u/t)^n * [sum_(z in J*) exp(-pi*u^2|z|^2)]
                 /[sum_(z in J*) exp(-pi*t^2|z|^2)]
      <=(u/t)^n.

Summing over c proves the stated upper bound with K_F. In the residue-only experiment, P(S mod J=c)=|C_c|/2^n and S is uniform within C_c; optimal selected success within it is m(c)/|C_c|. This proves the lower bound exactly. Taking r0=t and log(1+1/t)<=1/t gives the displayed overhead at t=2n^2*ell.

The maximizing j in (S1) may depend on all of y. No independence between function values is assumed. Additional metadata is legal precisely when its conditioning leaves the original independent law of S,G unchanged. In particular, revealing H after defining H=E-MG would not be a legal substitute for the independent H in A-FRAC.

## 3. DD2-AM1-SNF-v1: distinct-prime collision accounting

Fix one occupied fiber c of size m_c, and put m_qc=max_(j,v)N_q(c,j,v). For distinct b,b' in that fiber, f=b-b' is a nonzero ternary polynomial of degree<n. Since X^n+1 is irreducible for the stated n, f is nonzero in the number field and N(f) is a nonzero integer. Parseval and AM-GM give

    1<=|N(f)|<=|f|_coef^n<=n^(n/2).

If f vanishes at any split root modulo q, q divides N(f). Thus, over the distinct listed primes, a fixed ordered pair can collide at any root for at most n*log(n)/(2*log(Qmin)) primes. This counts a prime only once even if multiple roots collide.

For every q,c,

    m_qc^2 <= m_c + sum_(b!=b' in C_c) 1{some root collides modulo q}.

Averaging q yields E_q m_qc^2<=m_c+nu*m_c^2. Therefore

    E_q K_q <= 2^-n sum_c sqrt(m_c+nu*m_c^2)
      <=2^-n[sum_c sqrt(m_c)+sqrt(nu)*sum_c m_c]
      <=sqrt(C_pi/2^n)+sqrt(nu).

The trivial bound one completes the claim. This argument permits a selected root depending on c, and permits the fixed partition and list to be chosen jointly. It does not permit replacing the partition by a different partition for each q inside the pair sum.

For the optional ideal refinement, f in J implies D divides |N(f)|. With gcd(q,D)=1, the product of colliding listed primes divides |N(f)|/D. The same argument substitutes log(|N(f)|/D) for log|N(f)|. Non-singleton fibers ensure D<=n^(n/2); singleton fibers contribute only their exact diagonal count. This verifies the optional refinement, though the main decoder only needs the simpler bound.

## 4. DD1-EXTRACT-v1: exact hybrids, filtration and sample accounting

Fix s throughout this paragraph. Conditional on S=s, the raw blocks are independent, although they share s. For each fixed prefix j, the Ncal calibration outputs are independent Boolean variables of mean p_j. Outputs for different prefixes can be dependent because the bank is reused; no independence across prefixes is needed.

Set a=epsilon/(64n). The displayed Ncal satisfies 2*Ncal*a^2>=Lcal. Hoeffding and a union bound show that every calibration mean is within a of its true mean except with probability at most 2(n+1)e^(-Lcal)<=eta/2. The last inequality follows from log2(x)>=ln(x) for x>=1 and the chosen ceiling.

Condition now on s and the ENTIRE calibration bank, masks and algorithm coins, hence also on the selected j*. The disjoint raw test bank is still the original product law conditional on s. At the chosen root write the field shift as p. Since A is uniform, (A+p,p) is a pair of independent uniforms. After the transformation, the residual at this root is

    E+(t-s(r_j))*p.

For the correct t it is precisely E; for every other t it is a fresh uniform mask independent of the new public A and all original errors, including other CRT error coordinates. Prefix masks then give exactly the (j-1) or j hybrid. This holds for arbitrary within-ring error correlations. Across raw samples the required independence is preserved.

For each fixed candidate t the Ntest outputs are independent conditional on this calibration transcript and s. Different candidates share their bank and need not be independent. Hoeffding plus a union bound over all q candidates gives test failure probability at most eta/2. Using Qmax in Ltest only strengthens this estimate.

On the two good concentration events, if calibration proceeds its observed endpoint separation is at least epsilon/(4n)=16a. Each candidate mean is within 2a of its corresponding calibrated endpoint, so exactly the correct candidate is strictly closer to the first endpoint. This proves E1 even for s with zero distinguishing gap. If |d(q,s)|>=epsilon/2, telescoping gives an adjacent true separation at least epsilon/(2n)=32a, hence an observed separation at least30a and calibration necessarily proceeds. This proves E2, with ample strict-threshold margin.

For the average guarantee let X=|d(q,S)|<=1. The hypothesis implies E X>=epsilon. Hence P(X>=epsilon/2)>=epsilon/2 (the sharper ratio is epsilon/(2-epsilon)). Multiply only this event probability by the POINTWISE success guarantee, or equivalently subtract the concentration failure probability; success is at least epsilon/2-eta. Signs may vary with s and with q. No common sign across q is required for this extractor.

Calibration draws number k0*Ncal*sum_(j=0)^n j. Each test block draws one field shift and j-1 masks per sample, hence at most n field draws per sample. This proves Tfield. Each bounded rejection draw couples to an ideal independent field draw with failure probability <=2^-B conditional on its full past. A union bound, not a product estimate, proves the full-output distance <=nu, pointwise for every raw input. Fallback0 is legal. The physical raw source count is K=k0*(Ncal+Ntest); D-call count is (n+1)Ncal+q*Ntest. Reusing blocks cannot be relabeled as obtaining new source samples.

## 5. DD2-PRIMES-v1 and the primary source

The publisher PDF of Xylouris, Acta Arithmetica150.1(2011), printed page66, Theorem1.1, gives least-prime exponent5.18 with an effectively computable constant. The weaker exponent6 used here is valid. The [publisher's primary source](https://www.impan.pl/shop/en/publication/transaction/download/product/83078) verifies the cited statement, not a numerical value for its absolute constant.

In the construction, p>B=R0+t0+2 implies t<=t0+R0=B-2<p. Thus each a_t=1+2nt is already a positive representative smaller than m=2np and is >=Qmin. All a_t are coprime to2n. The R0+1 indices form fewer than p consecutive residues modulo p; since2n is invertible modulo p, at most one a_t is divisible by p. At least R0 progressions survive, with distinct residues modulo m, so their least primes are distinct. Each lies in [Qmin,C*m^6], and m<4nB. They are odd and1 mod2n.

Enumerating these bounded progressions and using exact trial division is polynomial in the NUMERIC values of n,M,Qmin, with an absolute effective constant. It is not polynomial in only logM or logQmin. An explicit practical numerical value of C is neither supplied nor needed for the asymptotic polynomial-value statement; one must not present the displayed upper bound as a numerically instantiated estimate without such a value. The master-list construction does not inspect J. Since D<2^n, fewer than n distinct primes divide D. Divisibility tests suffice to filter; factorization is unnecessary.

## 6. AM-MAIN-v3: full composition under the declared interfaces

### 6.1 Filtering, unknown signs and extraction

Let d_q be the signed k0-sample target gap. Keeping M out of M+n entries removes exactly n entries, irrespective of how many were divisibility exclusions. Since |d_q|<=1,

    |sum_(q in Q) d_q| >= (M+n)*epsilon0-n,
    |E_(q in Q)d_q| >= epsilon0-n/M >= epsilon0/2=epsilon.

Consequently E_q |E_S d(q,S)|>=epsilon. The extractor with eta_ext=nu_ext=epsilon/64 has ideal uniform-multiplier average actual-selected-value success at least

    epsilon/2-eta_ext-nu_ext=15epsilon/32.              (A1)

The same secret is reused across all K raw samples. A new secret per calibration/test block would invalidate this argument. Fresh secrets across separate executions of A_q are both allowed and required by its specified execution law.

### 6.2 Fractional completion and selected-function bound

Use the inherited A-FRAC full-law proof with k=K and L=ell, not its whole-secret guessing conclusion. Its source event has failure at most delta_tail. Its multiplication matrix M has operator norm at most s*sqrt(Kn)*ell on that event. The floor ensures

    sigma_q>=8n^2*ceil(sqrt(Kn))*ell^4
           >=2*(2n^2*ell)*(sqrt(2)*ell^2)*sqrt(Kn)*ell.

For every good unwrapped source state, the completion introduces analytical independent G~D_(J,t) and H with covariance parameter C=sigma_q^2 I-t^2 MM^T>=3sigma_q^2 I/4. Both Gaussian normalizers are retained. If r_e is the normalized shifted theta factor, the completed error mass is EXACTLY

    D_(Z,sigma_q)^(Kn)(e) * r_e / E_(D_(Z,sigma_q)^(Kn))[r].

This is the normalization needed for the TV estimate; replacing the denominator by1 is not licensed. The general inherited short-basis existence bound gives tau2<=n^2*D^(1/n)<2n^2. Hence the theta parameter is at least3ell^2/4, and the displayed eta_A dominates the completion error.

After completion, the entire extractor transcript is a function of the source, H and Y=S+G, with its own fresh coins. Conditional on the source and H, S and G retain exactly the independent original laws. Thus SFUNC-v2 applies to the n functions S->S(root_j mod q), even if the selected root depends on the entire transcript. Neither G nor H is physically sampled or supplied.

For fixed J the partition S mod J is the SAME across all retained q. Its number of fibers is <=D. DD2-AM1-SNF-v1 therefore bounds average fractional-source actual-selected-value success by Bfun+delta_tail+eta_A. The selected q list may depend on J through filtering; the deterministic fiber bound explicitly permits this. No averaging over ideals is substituted for a pointwise promise.

### 6.3 Bridge, variable widths and both implementation endpoints

Take B-GP-v2 with coefficient w_B=r_B=ell^2, so s=sqrt(2)*ell^2 and canonical width w=sqrt(n)*ell^2. Since ell>=2, its lower r_B smoothing guard holds: ell^4 exceeds [log(8n)+ell^2 log2]/pi. Also eps_B=nu<=1/4. The finite quotient is the inherited F=hZ^n/(qJ^-1), with h=1/(DP) and gcd(q,D)=1 after filtering.

The uniform endpoint loses at most Kn*nu+eta_cap from target-error sampling and capped elementary uniforms. The Gaussian endpoint loses at most

    2K eps_B/(1-eps_B)+2pi Kn/(P r_B)+2Kn nu+eta_cap.

Their sum is exactly E_bridge. These bounds retain S and all K samples. They are applied to the implemented A_q's source advantage once; they are not later multiplied by Q_* as an additional simulation loss.

K_B=ell^2+6 is exact. The inherited trial cap L_B=ceil(40K_B*(ell^2+4)*ln2) is at most the chosen integer L_+=40K_B*(ell^2+4). Uniform proposals total at most Kn(1+2L_+), and Bcap gives failure <=eta_cap. The SAME trial-count bound works for every sigma_q because acceptance/rejection analysis depends on the accuracy parameter; proposal intervals and arithmetic encodings do depend on sigma_q and are charged. The lower floor and upper sigma_q<=q/n are checked for every master-list entry. No implicit fixed-width substitution occurs.

Combining (A1), the fractional upper bound and both implementation endpoints gives

    average_q (E A_q(U)-E A_q(GP))
      >=15epsilon/32-(Bfun+delta_tail+eta_A+E_bridge)
      >=11epsilon/32.

At least one fixed q has advantage >=delta=epsilon/4. Favorability is an analytic property of the fixed code and source distributions, not an adaptively selected lucky sample transcript.

### 6.4 Common C8 parameters, final verification and success

For q<=Qmax, a0(q) is at least a0,max, so the common Smax and kappa satisfy each retained q's lower bound. The guard with Qmin gives each q's exponential accuracy guard. Q_* is computed from kappa before epsilon_C and chi; h0=v0*d0 is independent of chi. Thus there is no circular dependence. Taking chi an integer makes d0=delta*ell^2/(64nKchi) and r=d0/Qmax rational, even though some intermediate C8 parameters involve square roots or logarithms.

C8 is invoked as its exact declared interface, including the finite algorithm-v2 and its rational final test. Its all-input bound covers bad moduli and wrong orientations. The favorable q runs on qT and has canonical error <=q*r<=d0. Thus it outputs q*lambda with failure probability at most p=(n/2)e^(-kappa)+zeta.

For nonzero x in J^-1, the integral ideal (x)J has positive integer norm. Therefore |N(x)|>=1/D, and Parseval plus AM-GM imply |x|_coef>=D^(-1/n). The outer guard gives4r<D^(-1/n). Any TWO candidates passing the coefficient Euclidean radius-r test would differ by at most2r, which is impossible. Hence no earlier bad-modulus candidate can cause an incorrect acceptance. Conversely, canonical infinity error <=r implies coefficient Euclidean error <=r, so the correct candidate passes, including equality at the requested radius. Membership and the squared-distance test compare rational data exactly.

Only the success event of one fixed favorable q is needed. There is no multiplication of independent-modulus success probabilities and no union loss M*p. Since kappa>=ln(8n/zeta), p<=17zeta/16. Running the complete fixed schedule gives exactly the advertised upper bounds on A_q and D_alg executions. Q_* counts calls, while each A_q execution physically needs K source points. These are different resource quantities.

## 7. Fixed-modulus bridge and parameter families

For every auxiliary prime q, MR-v1 applies with target(q0,sigma0) and source width sigma_q=(q/q0)*sigma0. The explicit guards imply signed-gap change <=epsilon_*/4. Every auxiliary signed gap therefore has the same unknown sign and magnitude >=3epsilon_*/4. Its average over Q0 is >=epsilon_*/2 in absolute value, establishing AM's epsilon0 premise. The wrapper uses classical execution of the supplied all-input D0 code; it needs no multi-modulus target oracle. The ideal metadata must remain precisely that of D0's pointwise premise.

The upper width bound follows from q0>=n*sigma0. The two explicit lower guards ensure that AM's actual K-dependent sigma_floor is met. Defining the master list before K makes its resulting Qmax and logarithms fixed inputs to Ntest and K. The master list does not depend on J, S or public challenge data.

For AM's stated family, effective prime construction gives polynomial VALUE Qmax and logQmax=O(log n). Therefore

    Ncal,Ntest=O(n^(2c+2) log n),
    K=O(n^(b+2c+2) log n), ell=O(log n),
    sigma_floor=O(n^(b/2+c+7/2) (log n)^(9/2)).

Its Qmin dominates n*sigma_floor. Since M is a constant times n^(2c+4), sqrt(mu)=O(n^(-c-3/2))=o(epsilon), and sqrt(D/2^n)<=2^(-(1-rho)n/2). Every remaining error term is superpolynomially small because ell grows proportionally to log n. Thus (G-AM) holds uniformly in the stated ideal family for sufficiently large n.

For FIXED's family, sigma0=n^(b+c+4) dominates the MR width requirement O(n^(b+c+2)). Qmin=q0*n^(b+2c+12) dominates the MR modulus requirement. Its minimum auxiliary width is n^(2b+3c+16), far above the same asymptotic sigma_floor. The constants epsilon0=epsilon_*/2 and M=2^24*n^(2c+4) change only absolute factors. Any fixed polynomial-value family q0 gives polynomial-value Qmax; its polynomial degree may depend on that family. This is not a bound uniform over unspecified superpolynomial q0.

Choose kappa of polynomial value large enough for the displayed guards: Smax=O(n log n+logK+log(1/epsilon)), and logD=O(n). With fixed or inverse-polynomial zeta, Q_* is polynomial in kappa, chi=O(sqrt(log n)), and the chi=a uniqueness guard holds eventually. Hence r is bounded below by an inverse polynomial. P need not have polynomial VALUE, but logP=2ell^2 is polynomial and the inherited finite routines charge that bit length. Full ideal-basis lengths, target encodings, D0/D_alg runtime, and certified evaluation costs remain charged. This is a nonempty asymptotic parameter/source regime, not a practical bound or an assertion of efficient distinguishers.

## 8. Boundary and probability regressions

* n=2,J=R: every split q>=5 makes each root evaluation injective on the four binary vectors, since nonzero ternary norms are1 or2. Thus K_q=1/4, consistently with the fiber and selected-function bounds. The main numerical guard is empty here: Bfun>=sqrt(1/4)=1/2, while epsilon/8<=1/16. The theorem is conditional and makes no decoding conclusion from a failed guard.
* Singleton fibers: K_F=1 and S is known from its residue, so p_selected=1 exactly. The bounds classify this without a false smoothing argument. Such a partition cannot be exploited to satisfy the small-error main guard.
* Constant functional: K_F=p_selected=1. “Optimal Bayes” in SFUNC is essential: an arbitrary predictor can intentionally fail, so its success need not satisfy the lower bound.
* Repeated primes: the distinctness premise is essential. Let n=8,q=17 and partition the256 vertices by evaluation at one root modulo17. Repeating q100 times gives K_q=1 at every position, C_pi<=17, and the proposed distinct-prime RHS would be <sqrt(17/256)+sqrt(24/400)<1. This is excluded by the actual statement. Likewise a different evaluation partition for each distinct q could make every K_q=1 and is not covered.
* Exactly-radius rational target: r is rational; coefficient error <=canonical-infinity error implies the correct point passes the closed rational squared-distance threshold. No indefinite equality refinement is required.
* Varying q signs: AM uses E|d| and absolute adjacent hybrid separation, so it does not silently cancel advantages or presume a common orientation. FIXED obtains a common sign by the pointwise MR bound, while still not learning it.
* Fixed-q-only availability: AM alone does not follow from it; FIXED does, through deterministic wrappers and all-input code execution. An oracle defined only on exact target-distribution samples would be a different computational model and is not sufficient as stated.
* Gaussian normalizers and support: source completion retains E_D[r], scalar rounding retains T and Z, and the selected-function proof retains rho_t(J). No positive-mass posterior branch is discarded. Off-promise algorithm calls are allowed only because supplied programs and inherited C8 routines are all-input bounded.

The mandatory CP-1 regression was checked analytically. The initial event has probability10/11; conditioned trace masses are21/2000 for each A_b,1/20 for each C_b,879/1000 for D. Initial incidences are p(x)=1/10,p(e_b)=121/2000=0.0605,p(f_b)=21/2000=0.0105, all light under strict threshold1/10. The selected two-hit event has probability21/2000=0.0105>1/100. After the matching prefix the second incidence is21/221<1/10; transferring the cached prefix can increase the first-stage envelope from121/2000 to221/2000. The invalid product conclusion is therefore rejected. The failure is removal of sibling support and Bayes renormalization, not merely dependence of fresh oracle values.

The new proofs above do not infer a sequential product estimate from these local facts. Extractor concentration conditions on S and the complete CALIBRATION transcript, then uses the disjoint bank; candidates are combined by a union bound. Scalar and capped-sampler TV losses use pointwise conditional bounds and telescoping sums. Gaussian guessing uses the exact joint posterior before maximizing. The favorable-modulus conclusion uses a deterministic average and one fixed successful decoder. Latent hit or cache status is never added to an algorithm's branch filtration. The inherited C8 conditional-budget guarantee is an explicit dependency, not something re-proved from local independence in this review.

## 9. Finite evidence and remaining gates

The exact preregistration, source code hash, parent slot authorization, full stdout/stderr and resource record are preserved separately. One deterministic run completed with exit0 in1.52 seconds and maximum RSS16384KiB under a512MiB address-space limit and120-second descendant-killing timeout. It verified55,664 negacyclic rounding identities (including midpoint and wrap cases),1,000 exact hybrid distribution laws at n=2,q=5 for every fixed CRT error, and all6,560 nonzero n=8 ternary vectors against primes17,97,113. The largest observed norm was2401 and largest product of colliding listed primes1649. These finite checks passed. They are structural regression evidence, not proofs of unbounded claims.

The local mathematical proofs close the new-lemma obligations I was assigned. Residual global gates are: preserve the declared historical-interface scope; clarify the fixed-target final sentence's actual-call/target-promise distinction; reconcile this blind report against current author material only after sealing; and complete the coordinator's historical-regression and final-artifact checks. No current proof was read merely to compare, no unrestricted hardness foundation was certified, and no quantum or efficient-sampler extension was inferred.
