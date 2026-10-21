# AM-MAIN-v2 complete composition proof

PROVISIONAL; binds am-main-theorem-v2.md. Component source statements/proofs remain separately frozen. No full-main acceptance has occurred.

## 1. Master-list filtering and extraction lower bound

For q in Q0 let d_q be the signed target acceptance gap. The ordinary averaged-modulus premise gives |average d_q|>=epsilon0 and therefore sum |d_q|>=(M+n)epsilon0. At most n master-list entries are discarded when retaining exactly M coprime primes. Since |d_q|<=1,

    average_(q in Q)|d_q| >= ((M+n)epsilon0-n)/M
                           >=epsilon0-n/M>=epsilon0/2=epsilon.

The complete list and both worlds retain identical metadata; no secret-dependent selection occurs. The bound uses the exact final list for the source analysis. All q in it are coprime to D.

Apply DD1-EXTRACT-v1 with the common counts computed using Qmax. For q drawn uniformly from Q and S uniform binary, the probability of |p0(q,S)-pU(q)|>=epsilon/2 is at least epsilon/2. On each such fixed (q,S), conditional calibration/test analysis gives success at least1-eta_ext. The finite field cap changes the full extractor output law by at most nu_ext for every input. Consequently the average uniform-multiplier actual selected-root success u_q satisfies

    average u_q>=epsilon/2-eta_ext-nu_ext=15epsilon/32.

This is a single success event per extractor. The raw K-sample bank is reused by many calls but all full-law changes are applied to that K-sample input before postprocessing. Data processing does not multiply its TV error by the number of extractor calls.

## 2. Full-observation functional guessing bound

For q fixed, define N_q(c,j,v) and K_q as in DD2-AM1-SNF-v1. Under independent uniform binary S and exact G~D_(J,t), the full success of an optimal predictor selecting one pair from Y=S+G is exactly

    [2^n rho_t(J)]^(-1) sum_y max_(j,v)
      sum_(b modJ=y modJ, b(zeta_j)=v) rho_t(y-b).

The cube center u=(1/2,...,1/2) and the pointwise completed-square inequality give, for any r0>0,

    rho_t(y-b)<=exp(pi n/(4r0))*rho_sqrt(t^2+r0)(y-u).

Each inner selected sum contains at most max_(j,v)N_q(c,j,v) terms. Sum the common envelope on each occupied J coset. The centered theta maximum and the exact Poisson ratio

    rho_sqrt(t^2+r0)(J)/rho_t(J)<=(1+r0/t^2)^(n/2)

retain both Gaussian normalizers. Taking r0=t yields p_selected<=K_q*Gamma, capped by1. This proof does not claim the full posterior S|Y is uniform within a residue class. An optimal residue-only predictor attains K_q, so the envelope's baseline interpretation is exact.

DD2-AM1-SNF-v1 applies to the fixed partition b modJ and the exact final distinct-prime list. Its determinant/nullity argument proves

    average K_q<=sqrt(C_J/2^n)+sqrt(mu)<=sqrt(D/2^n)+sqrt(mu).

Every pair's root multiplicities consume factors of its nonzero integer norm; no equidistribution of roots or primes is assumed. The list may depend on J; the partition must remain common while q varies, as it does here.

## 3. Fractional completion and complete endpoint errors

For q fixed, the fractional source supplies K independent a_i~D_(J^-1,s), reduced modulo qJ^-1 and identified canonically with R/qR. The wrapper samples one fresh binary S and independent target errors of width sigma. The inherited A-FRAC proof's full stacked matrix M has Kn rows. On its good-source event, ||M||op<=s sqrt(Kn)ell and the chosen sigma satisfies sigma>=2ts sqrt(Kn)ell. The existing proof constructs LATENT G~D_(J,t) and H, independent of S,G conditional on source state, such that the full law with S and responses differs by eta_A from M(S+G)+H; source bad events cost delta_tail. H is integrated out before the independent-error endpoint comparison. It is never executable advice.

The completed extractor output is a randomized function of source state,H,Y. Revealing those variables can only increase the success of selecting one correct root/value. Conditional on source state,H, the same independent product law S,G remains, so Section2 applies pointwise. Averaging over q gives fractional success at most Bfun+delta_tail+eta_A. No uniform-A promise for D_alg is applied on these source inputs.

B-GP-v2 with k=K supplies the full planted TV charge

    Delta_B+Kn nu+eta_cap,
    Delta_B=2K eps_B/(1-eps_B)+2pi Kn/(P r_B)+Kn nu,

and full uniform TV charge Kn nu+eta_cap. The first includes the finite bridge error plus separately generated approximate target errors; the second retains the exact uniform-multiplier endpoint before those implementation charges. Both preserve the actual S, all samples and metadata. The extractor is already a bounded postprocessing kernel, so these errors are paid once per whole test, despite bank reuse. The extractor's own field cap cost was charged in the uniform success lower bound; fractional functional guessing bounds any resulting capped extractor and needs no second such charge.

Subtracting endpoints yields average U-minus-GP gap at least

    15epsilon/32 - Bfun - delta_tail - eta_A - E_bridge
       >=15epsilon/32-epsilon/8=11epsilon/32.

Thus some fixed q_* in the final list has gap at least11epsilon/32, in particular delta=epsilon/4. This is an existential analysis choice; the executable decoder does not need to find q_* or simulate its fractional source.

## 4. Common inherited decoder parameters and exact verification

For q<=Qmax, C8's scale parameter S(q) is at most Smax; for q>=Qmin the coefficient-reconstruction guard 3w exp(-kappa)<q/(8D) follows from the common lower endpoint. Other C8 inequalities use only common n,K,w,delta,zeta and the chosen chi. Therefore its exact bounded finite algorithm is valid for every q for which the source gap premise holds, while remaining bounded without any promise for all others.

Let input T=lambda+e with lambda in J^-1 and canonical infinity norm of e at most r=d0/Qmax. For q_* the scaled target q_*T belongs within canonical infinity distance d0 of q_*lambda in q_*J^-1. C8 therefore returns that lattice point with probability at least1-p. Dividing by q_* gives the true lambda.

Parseval gives ||e||coef,2^2=(1/n)sum_sigma |sigma(e)|^2<=r^2, so the true candidate passes the exact rational coefficient-distance verifier. Every nonzero x in J^-1 has |N(x)|>=1/D, hence by AM-GM/Parseval ||x||coef,2>=D^(-1/n). The common guard implies r<1/(4D^(1/n)). If two different candidates both pass, their coefficient distance is at most2r<D^(-1/n), contradiction. Since the true lambda is within r, any accepted candidate must equal it. This argument is unconditional on the bad-q oracle behavior.

Run all M fixed decoder schedules. Failure of the final procedure implies failure of the one fixed good-q execution; hence final failure is at most p. There is no product of marginal success probabilities, favorable future conditioning, or assumption that good q can be recognized. All C8 adaptive physical-kernel/finite-precision bounds remain its inherited exact conditional transcript guarantees.

## 5. Resource accounting and asymptotic nonvacuity

The K physical challenge components per A_q cost K bridge applications, K ring completions and Kn scalar errors. The extractor makes (n+1)Ncal+qNtest calls but reuses those K components. Every D_alg execution is bounded even on hybrids and bad source inputs. The field caps use a pointwise first-failure coupling; the source/bridge caps are separate. C8 bounds all A_q calls including wrong orientations, hence M Q_* N_D,max is a valid D_alg-call bound. Full bit encodings, finite arithmetic, numerical samplers and evaluation routines are charged as stated.

For the displayed family, DD2-PRIMES-v1 constructs Q0 before the target sigma is defined, using Qmin=n^(b+2c+12) and M=ceil(2^20n^(2c+4)). Effective Linnik gives Qmax=n^O(1), so logQmax=O(logn). Therefore

    Ncal+Ntest=O(n^(2c+2)logn),
    K=O(n^(b+2c+2)logn), ell=O(logn),
    sigma=O(n^((b+2c+7)/2)(logn)^(9/2)).

The Qmin exponent b+2c+12 exceeds the exponent of n sigma by a positive constant, so Qmin>=n sigma for sufficiently large n. The source entropy term is exponentially small for fixed rho<1; sqrt(mu)=O(n^(-c-3/2)); Gamma tends to1. The tail, eta_A and all bridge implementation terms are negligible compared with epsilon=Theta(n^-c), because ell>=log2(2nK) and eps_B=2^(-ell^2). Thus (G-AM) eventually holds uniformly in the eligible J family.

C8 admits polynomial-value kappa satisfying all displayed guards: logD=O(n), logQmax=O(logn), K and1/delta are polynomial. Its fixed loop bounds are polynomial in kappa; logQ_* is O(logn). Hence chi=a=O(sqrt(logn)) for fixed/inverse-polynomial zeta. The d0 uniqueness guard follows from large Qmin, and r is inverse polynomial. Large fixed exponents and the effective Linnik constant do not imply practical efficiency, but they do give a nonempty asymptotic polynomial-value regime.

Prime-list generation, the fixed master-list target distribution, the restricted ideal family and oracle input law are all explicit. This proof does not convert fixed-q advantage into average-modulus advantage, certify arbitrary-ideal hardness, or reuse classical service access as coherent quantum code.
