# AM-MAIN-v3: restricted ideal decoding from averaged-modulus binary RLWE

PROVISIONAL: v3 adds explicit per-modulus coefficient widths and repairs the polynomial-value corollary. Exact-version review remains required. This is an averaged-modulus target with a single shared binary secret per batch. A distinguisher supplied only for one fixed modulus does not satisfy its premise. The unrestricted worst-case ideal-family foundation is not asserted.

## 1. Target, input representation and prime list

Let n>=2 be a power of two, R=Z[X]/(X^n+1), with coefficient Euclidean norm and canonical infinity norm max over all complex embeddings. Let J be an ordinary-basis represented nonzero integral ideal, D=N(J)<=2^(rho n), 0<=rho<1. All scalars are represented rationals or have fixed certified polynomial-bit evaluation routines; their full encodings and evaluation costs are charged.

Supply k0>=1, rational 0<epsilon0<=1, and a fixed master list Q0 of M+n DISTINCT odd primes, all congruent1 modulo2n, in [Qmin,Qmax], where Qmin>=3 and M>=ceil(2n/epsilon0). The master list is fixed independently of J. Set epsilon=epsilon0/2. Compute D, delete primes dividing D, then keep the first M surviving primes in master-list order, forming Q. Fewer than n primes divide D, so this is possible. No factorization of D is needed.

Let D_alg be supplied all-input bounded randomized Boolean code taking q and k0 ordered ring samples, with any specified fixed metadata identical in both worlds. The target experiments choose q uniformly from Q0, one uniform S in {0,1}^n, independent uniform A_i in R/qR, and independent integer coefficient errors E_i with all k0*n coefficients D_(Z,sigma_q). The planted responses are A_i S+E_i modq; the comparator responses U_i are independent uniform R/qR, with exactly the same q,A and metadata law. The absolute difference in D_alg acceptance is at least epsilon0. Every D_alg execution uses fresh coins. If metadata includes J or its basis, the premise is pointwise for that supplied J. An average over ideals is insufficient.

A rational width sigma_q>=1 for every q in the master list is supplied by a finite table or a bounded rational evaluation routine, with its costs charged. The lower width floor below depends on the actual source batch count K. The exact per-modulus widths are part of the target promise even though D_alg itself consumes k0 samples. No coherent access is required for this classical decoder.

## 2. Extraction and source parameters

Set eta_ext=nu_ext=epsilon/64 and

    Lcal=ceil(log2(4(n+1)/eta_ext)),
    Ltest=ceil(log2(4Qmax/eta_ext)),
    Ncal=ceil((2048n^2/epsilon^2)Lcal),
    Ntest=ceil((2048n^2/epsilon^2)Ltest),
    K=k0(Ncal+Ntest),  ell=ceil(log2(2nK)),
    t=2n^2 ell,  s=sqrt(2)ell^2,
    sigma_floor=8n^2 ceil(sqrt(Kn))ell^4.

All integer ceilings here are computed by exact integer/rational comparisons. Require Qmin>=n sigma_floor and, for EVERY master-list q, sigma_floor<=sigma_q<=q/n. Widths are fixed independently of the sampled secret/public data and are identical in the two comparisons at that q.

For each q in Q use precisely the finite extractor DD1-EXTRACT-v1 (workers/DD1/extraction-theorem-v1.md): Ncal independent k0-sample calibration blocks, reused across all CRT prefixes; a DISJOINT Ntest-block test bank, reused across all q candidate values at the selected root. It returns one root/value pair or FAIL. All field draws have the specified bounded rejection implementation with Bext=ceil(log2(Tfield_max/nu_ext)), where

    Tfield_max=k0 Ncal n(n+1)/2+k0 n Qmax Ntest.

At most N_D,max=(n+1)Ncal+Qmax Ntest calls to D_alg occur. Its source input is K samples, not N_D,max samples. Root/idempotent computation by bounded enumeration in F_q is charged in q in VALUE.

Define the following finite real quantities, with natural logarithms in analytic inequalities:

    mu=n log(n)/(2M log(Qmin)),
    Gamma=exp((pi/8+1/4)/(n ell)),
    Bfun=min(1,Gamma*(sqrt(D/2^n)+sqrt(mu))),
    delta_tail=min(1,4Kn exp(-pi ell^2)),
    theta_A=2 sum_(j>=1) exp(-pi(3ell^2/4)j^2),
    Delta_A=(1+theta_A)^n-1,
    eta_A=min(1,Delta_A/(1-Delta_A)) if Delta_A<1, and eta_A=1 otherwise,
    eps_B=nu=eta_cap=2^(-ell^2), P=2^(2ell^2), r_B=w_B=ell^2,
    E_bridge=2K eps_B/(1-eps_B)+2pi Kn/(P r_B)+3Kn nu+2eta_cap.

Assume the explicit numerical guard

    Bfun+delta_tail+eta_A+E_bridge <= epsilon/8.                 (G-AM)

This is a supplied true inequality on represented quantities, not an instruction for an unbounded exact comparison at a transcendental equality boundary.

## 3. Bounded Gaussian-periodic test and inherited interfaces

For each q, let Lambda=J^-1, L_q=qLambda, h=1/(DP), and F_q=h Z^n/L_q, with fixed ordinary HNF/SNF representatives. Define A_q on K points of F_q as follows: apply the exact B-GP-v2 public bridge to every point, with its finite scalar samplers and caps; draw ONE fresh uniform binary S and approximate independent coefficient D_(Z,sigma_q) errors with per-coordinate TV<=nu; complete the K resulting public multipliers with responses A_i S+E_i; run the finite extractor above; accept iff its returned selected root/value pair is correct for this actual S. FAIL rejects. No auxiliary ideal Gaussian, latent G or H is supplied to or sampled by this executable wrapper.

Use the same full wrapper caps as the accepted same-J interface with k=K: K_B=ell^2+6, L_+=40(ell^2+6)(ell^2+4), U_all=Kn(1+2L_+), Bcap=ell^2+ceil(log2 U_all). These count the bridge/error sampler uniform proposals. The extractor's field caps are separately counted by Bext. Both endpoint full laws retain S, all K samples, all common metadata and the chosen modulus. The scalar rejection trial count depends on nu, not sigma_q; its proposal interval N_B=ceil(sigma_q K_B)+1 and associated integer bit costs do depend on sigma_q and are charged. Thus the displayed cap counts remain common over q without pretending the widths are equal.

The designated inherited dependencies are B-GP-v2 and C-OHCP-v8CORE, at the exact mathematical interfaces in OLD/workers/RF4/same-j-composition/interface-statements-v1.md, and C8 theorem-v8/algorithm-v2/proof-v9 as listed there. OLD means exploration/runs/brlwe-standard-hardness-20261017-astra-ultra. A-FRAC's full-law Gaussian completion, rather than its whole-secret guessing conclusion, is also used. No changed-premise acceptance is inferred from those references.

Under the assumptions, the average over q in Q of

    E[A_q(uniform(F_q)^K)] - E[A_q((Q_h(G_(w/sqrt(n))) mod L_q)^K)]

is at least 11epsilon/32, where G_(w/sqrt(n)) denotes the continuous COEFFICIENT Gaussian, and w=sqrt(n)ell^2 is canonical width. In particular at least one q in Q has this difference >=delta, where delta=epsilon/4.

## 4. Common C8 parameters and the decoder

Choose rational 0<zeta<=1/8. Instantiate C8 with k=K, width w, delta=epsilon/4 and each q, using COMMON parameters chosen from Qmax as follows:

    h0=delta*w/(32nK),
    a0,max=D^(1/n)*w^(1-2/n)*h0^(2/n)/(n Qmax),
    Smax=max(0,(n/2)log(1/a0,max)).

Choose integer kappa satisfying

    kappa>=max(4Smax+4n+4log(K+1)+20,2K,2/delta,20log3,log(8n/zeta)),
    3w exp(-kappa)<Qmin/(8D).

Compute the finite C8 loop bounds Q_H,Q_*=nQ_H from this kappa exactly as defined in the C8 interface/algorithm-v2. Then set

    epsilon_C=min(1/16,zeta/(64KQ_*)),
    a=Up(sqrt(log(8n/epsilon_C)/pi))+1,
    chi=a, v0=2sqrt(n)chi,
    d0=delta*ell^2/(64nKchi), r=d0/Qmax.

Up is C8's fixed certified upper ceiling (one evaluation to error1/8, then an exact rational ceiling). Require also d0<Qmin/(4D^(1/n)); if needed choose a larger integer chi with an explicitly charged value. The polynomial-value corollary below uses chi=a and verifies the guard. All definitions precede execution. Loop counts use Qmax only through these common parameters, so they are valid for every q in Q.

Given a rational target T=lambda+e with lambda in J^-1 and ||e||canonical,infinity<=r, run the all-input bounded C8 decoder for EVERY q in Q on target qT in L_q, with oracle A_q and the parameters above. Retain its candidates, divide each by q, and accept a candidate lambda' only if lambda' is exactly in J^-1 and the exact rational coefficient squared distance ||T-lambda'||_2^2<=r^2. Output the first accepted candidate, or FAIL if none. Run the complete fixed schedule; no statistical selection of a favorable modulus or unavailable fractional-source sampler is used.

The output is the unique lambda with probability at least 1-p, where

    p=(n/2)exp(-kappa)+zeta<=17zeta/16.

At most M Q_* A_q executions and

    M Q_* ((n+1)Ncal+Qmax Ntest)

executions of D_alg occur, plus the explicit arithmetic, source/bridge samplers, C8 finite-precision routines, finite coin caps, input reading and root/idempotent setup. Every bound is all-input, including bad-modulus/incorrect-orientation calls. Runtime is polynomial in the full represented input lengths, M,Qmax,K,k0,epsilon0^-1,log(zeta^-1),kappa,logP, and the supplied D_alg runtime, with actual certified evaluation costs charged. No query count is silently substituted for sample count.

## 5. Nonempty polynomial-value families and limits

Fix rho<1, INTEGER constants b>=0 and c>=1. Let k0<=n^b, epsilon0=n^(-c), M=ceil(2^20 n^(2c+4)), Qmin=ceil(n^(b+2c+12)). Construct the fixed master list of M+n split primes independently of J by the auxiliary-congruence construction in DD2-PRIMES-v1, using its effective Linnik bound; let Qmax be the actual largest prime obtained. Then Qmax is polynomial in n in VALUE. Define all remaining parameters in the above order, taking sigma_q=sigma_floor for this particular family. For all sufficiently large powers-of-two n, Qmin>=n sigma_floor and (G-AM) hold uniformly over every J with D<=2^(rho n), as does the chi=a uniqueness guard. For fixed or inverse-polynomial zeta, choose a polynomial-value integer kappa satisfying the displayed guards (such a choice exists). Then M,Qmax,K,k0,epsilon0^-1,kappa and chi are polynomial in n in VALUE, log P and the other explicitly represented scalar bit lengths are polynomial, and r is inverse polynomial. P itself need not be polynomial in value. The operation count is polynomial in n AND the full ideal/oracle input lengths, certified evaluation costs and supplied D_alg runtime; it is polynomial in n alone only when those costs/lengths are polynomial in n. Prime-list computation itself is polynomial in numeric n,M,Qmin and the ideal filtering costs are polynomial in the basis encoding.

The numerical and restricted source-ideal families are nonempty; no existence of an efficient promised distinguisher is asserted. The excluded epsilon0=1 endpoint has no such distinguisher for full-support discrete Gaussian target laws. The decoder is a quantitative conditional extension of the inherited restricted same-J direction to this averaged-modulus decision target. It does not supply an arbitrary-ideal hardness foundation, a reduction from a distinguisher at one prescribed fixed q, practical security estimates, or a proof that the restricted source family itself is computationally hard. Existing elementary sampling criteria may cover parts of that family. Subsequent quantum DGS composition would require full bounded executable code and a separate exact composition review; it is not claimed here.
