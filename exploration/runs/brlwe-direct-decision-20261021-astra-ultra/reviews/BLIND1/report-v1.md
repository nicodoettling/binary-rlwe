# BLIND1 independent report on AM-MAIN-v2

This report was derived from the frozen statement packet, the permitted inherited interfaces and historical source proofs, the mandatory audit protocol, and the permitted Xylouris primary source. No current author proof, current verdict, other worker report, coordinator scientific summary, or other current-run scientific material was read. The complete assignment is in `assignment-verbatim.txt`; input snapshots, hashes, experiment code, exact outputs and exposure records are retained alongside this report. Same-model review is correlated review, not independent statistical confirmation.

## Verdict and exact scope

The finite conditional reduction in Sections 1–4 of AM-MAIN-v2 follows from the supplied inherited B-GP and C8 interfaces. I found no new probability, support, Gaussian-normalizer, secret-sharing, modulus-selection, or final-verification defect in those sections. I give a complete independent derivation below rather than relying on the appearance of the statement or on inherited status banners.

The new extractor and fiber statements are valid as stated. The selected-functional upper bound is valid for every predictor. Its lower bound requires `p_selected` to mean the **optimal** success probability; the packet does not explicitly define that symbol as optimal. With that definition, the whole displayed inequality is valid. The prime-list construction is valid using the effective Xylouris bound, which I checked in the publisher source.

I cannot accept the whole literal wording of Section 5. Its sentence that “all parameters and operation counts are polynomial in n” is false for the specified parameter P. Indeed ell >= log2(2n), so

    P = 2^(2 ell^2) >= (2n)^(2 log2(2n)),

which exceeds every fixed polynomial in n. The required encoding length log P is polynomial, as Section 4 correctly charges. Furthermore, only a suitable polynomially bounded choice of kappa yields a polynomial-n schedule; arbitrary larger kappa satisfying the displayed lower bounds does not. Total runtime in n alone additionally needs polynomially bounded input encodings, certified evaluation costs, and D_alg runtime. The Section 4 relative runtime bound already accounts for these and is not contradicted by this objection. Thus the mathematical finite reduction is supported, while the literal unqualified polynomial-value/resource sentence is rejected.

There is also an endpoint caveat: c=0 gives epsilon0=1, for which the distinguisher premise is empty with exact discrete-Gaussian errors. Both target laws have full support on their common finite sample space, so their total variation, and hence every Boolean distinguishing gap, is strictly less than 1. Numerical guards and source ideal families can nevertheless be nonempty at c=0. This is not a refutation of the conditional reduction; “nonempty” must not be read as asserting existence of a promised distinguisher at that endpoint.

The inherited C8 theorem is an explicit supplied dependency here. This report verifies the new composition against its mathematical interface and algorithm definitions; it does not independently recertify the entire inherited OHCP proof. No quantum composition or arbitrary-ideal hardness assertion is established.

## Claim/dependency ledger

| Claim | Finding | Essential dependencies |
|---|---|---|
| DD1-EXTRACT E1/E2, average success and finite caps | Proved below | CRT, fixed-secret conditional iid blocks, Hoeffding, disjoint test bank |
| DD2-AM1-SNF selected-root bound | Proved below | Fixed partition, distinct split primes, nonzero ternary algebraic norm bound |
| Selected-functional upper bound | Proved below for all predictors | Actual joint mass, Gaussian envelope, Poisson summation |
| Selected-functional lower bound | Valid for optimal success; otherwise false | Definition of p_selected as optimal |
| DD2 prime-list construction | Proved relative to checked effective primary theorem | Bertrand, effective least-prime bound, trial division |
| Main filtered target advantage | Proved below | Exactly n discarded list entries, absolute signed gap |
| Main average source advantage 11 epsilon/32 | Proved below relative to B-GP and A-FRAC completion | Shared secret, full-law bridge, selected-functional/fiber bounds |
| Main finite decoder, success and counts | Proved relative to C8 interface | Common conservative parameters, fixed complete schedule, exact outer verifier |
| Section 5 numerical guard and inverse-polynomial radius | Valid for sufficiently large n with suitable polynomial kappa | Effective polynomial-value primes, asymptotic estimates below |
| Section 5 literal “all parameters … polynomial in n” | Rejected | Explicit P already has superpolynomial value |
| Standard arbitrary-ideal hardness / quantum DGS composition | Not asserted and not derived | Outside this theorem's scope |

## 1. Extractor: full conditional law and concentration

Fix q and the actual shared secret s. Work in CRT coordinates. For a selected coordinate j, write a raw sample as (A,As+E), and apply the candidate transform with fresh uniform p and an independent prefix mask W:

    A' = A + p e_j,
    B' = A's + E + (t-s(r_j)) p e_j + W.

The pair (A',p) is independent uniform because A is uniform. It is also independent of E. If t=s(r_j), this is precisely hybrid j-1. If t differs, multiplication by t-s(r_j) is a permutation of F_q; the extra response mask on coordinate j is uniform and independent of A', E and the prefix masks. The law is precisely hybrid j. This is an equality of full sample laws, for arbitrary fixed error distribution, and products give the k0-sample version. It does not assume anything about D_q outside those laws.

Set a=epsilon/(64n). For each fixed prefix j, conditional on S=s, its Ncal block outcomes are independent Bernoulli variables with mean p_j. Reusing the same source bank for another prefix does not affect this within-prefix independence. Hoeffding and the union bound give

    Pr[any calibration error > a | S=s]
      <= 2(n+1) exp(-2 Ncal a^2)
      <= 2(n+1) exp(-Lcal) <= eta/2.

Here 2 Ncal a^2 >= Lcal, and Lcal >= log2(4(n+1)/eta) >= ln(4(n+1)/eta). No product of dependent calibration events is used.

Now condition on S=s and the entire calibration transcript, including every reused raw block, mask, D_q tape and the selected j. The disjoint test bank retains its original iid raw law under this conditioning. For each fixed t, its Ntest block outputs are therefore independent with mean p_(j-1) if t=s(r_j), or p_j otherwise. Reuse of this test bank across different t introduces dependence between candidates, but the union bound still gives conditional probability at most eta/2 that any candidate empirical mean misses its own correct endpoint by more than a. This bound holds on every positive-mass calibration history, so averaging it is valid.

On the combined good event, if calibration does not fail, its selected empirical endpoint gap is at least epsilon/(4n)=16a. The true gap is at least 14a. The correct candidate is within 2a of the first calibrated endpoint and at least 12a from the second; each incorrect candidate has the reverse inequalities. The strict marking rule consequently marks exactly the correct value. This proves E1. If |p_0-p_n| >= epsilon/2=32na, some true adjacent gap is at least 32a. The largest empirical gap is then at least 30a, so calibration does not fail. This proves E2. The gap margins also settle the equality/tie boundaries in the specified comparisons.

For the average conclusion put X=|d(q,S)| in [0,1]. Its expectation is at least epsilon whenever E_q |E_S d(q,S)| >= epsilon. With g=Pr[X>=epsilon/2],

    E X <= epsilon/2 + (1-epsilon/2) g,
    g >= (epsilon/2)/(1-epsilon/2) >= epsilon/2.

Success is at least g(1-eta) >= epsilon/2-eta. This proof permits signs varying across q, across secrets, or across hybrid coordinates.

For the finite field sampler, a rejection attempt succeeds with probability q/2^ceil(log2 q)>1/2. Conditional on every past transcript, a requested draw fails all B attempts with probability at most 2^-B. Coupling to the unbounded ideal draw and summing over at most Tfield requests gives TV at most Tfield*2^-B <= nu, pointwise for every raw input. This is a sequential conditional union bound, not a product claim. The fallback value does not have to be uniform on the exceptional event. All D_q coins remain fresh. E1/E2 and average success lose at most nu as stated.

The physical source count is exactly k0(Ncal+Ntest). Calibration uses (n+1)Ncal oracle calls; the test uses q Ntest. Counting field draws yields k0 Ncal sum_(j=0)^n j plus at most k0 q Ntest n. Thus both the sample/oracle distinction and the stated caps are correct. A new secret per block would invalidate the fixed-s conditional law and this argument.

## 2. Fixed-partition, distinct-prime selected-root inequality

Let N_c be the size of an occupied fiber and m_(q,c)=max_(j,v) N_q(c,j,v). For a nonzero difference f=b-b' of binary vectors, f is a nonzero element of the power-of-two cyclotomic number field. Its coefficients are ternary. Parseval and AM–GM give

    0 < |N(f)| <= ||f||_2^n <= n^(n/2).

For a split prime q, each root of f among the n roots of X^n+1 corresponds to a distinct prime ideal above q dividing (f). If R_q(f) is the number of these roots, q^R_q(f) divides |N(f)|. Distinct rational primes can be multiplied, so

    sum_(q in Q) R_q(f) <= log |N(f)| / log Qmin
                       <= H := n log n/(2 log Qmin).

This is deterministic; no distribution on primes, no independence of roots and no probabilistic genericity is used.

The largest chosen bin supplies m_(q,c)(m_(q,c)-1) ordered distinct collisions at its root. Consequently

    m_(q,c)^2 <= N_c + sum_(b != b' in c) R_q(b-b').

Averaging over q and applying Cauchy/Jensen gives

    average_q m_(q,c)
      <= sqrt(N_c + nu N_c(N_c-1))
      <= sqrt(N_c) + N_c sqrt(nu).

Sum this over occupied fibers, divide by 2^n, and use

    sum_c sqrt(N_c) <= sqrt(C_pi * 2^n).

The result is sqrt(C_pi/2^n)+sqrt(nu); K_q<=1 supplies the outer minimum. Root selection may depend on the entire fiber and q, since m_(q,c) already maximizes over all roots and values. The pairs inside a fiber must remain the same across primes. An independently q-dependent partition would invalidate the displayed summation step and is correctly excluded.

For the optional ideal refinement, a binary difference in one ideal fiber satisfies f in J. The integral ideal (f)J^-1 has norm |N(f)|/D. At primes q coprime to D it retains all the above q-factors. Thus H can be replaced by [(n/2)log n-log D]/log Qmin. A non-singleton fiber ensures this numerator is nonnegative. This proves the optional statement as well.

Distinctness is genuinely essential. For example, take n=16, the one-fiber partition, q=97 repeated M=2^24 times. By pigeonhole K_q>=1/97. Using log97>log2 and log16=4log2, the purported right side for that repeated list is less than

    1/256 + 1/512 = 3/512 < 1/97.

This is a counterexample to the version allowing repetitions, and is outside the present statement's premises.

## 3. Selected-functional bound, exact normalizers and metadata

Define p_selected as the supremum over decision rules. Randomization cannot improve the pointwise maximum. Let h=(1/2,...,1/2), let u=sqrt(t^2+r0), and let m_c=max_(j,v)N(c,j,v). The actual joint mass gives

    p_selected = 1/(2^n rho_t(J))
      sum_c sum_(y in c+J)
        max_(j,v) sum_(b in c, F_j(b)=v) rho_t(y-b).

The elementary square-completion inequality

    ||y-b||^2/t^2 >= ||y-h||^2/(t^2+r0) - ||b-h||^2/r0

has ||b-h||^2=n/4. Therefore the inner maximum is at most

    m_c exp(pi n/(4r0)) rho_u(y-h).

Poisson summation gives the centered-theta maximum rho_u(J+a)<=rho_u(J) for every shift a. It also gives the exact ratio

    rho_u(J)/rho_t(J)
      = (u/t)^n rho_(1/u)(J*)/rho_(1/t)(J*) <= (u/t)^n,

where the final inequality follows termwise and all normalizers are positive. Thus the upper bound is K exp(pi n/(4r0))(1+r0/t^2)^(n/2), capped by 1. This bound applies to every predictor by optimality.

Observing Y mod J reveals S mod J. Choosing the best functional/value for each observed fiber succeeds with probability K, which proves the lower bound for optimal success. The packet's symbol p_selected should explicitly denote this optimum: if it meant an arbitrary predictor, the lower bound would be false. A concrete counterexample is n=2, J=2Z^2, F_1(S)=S_1, and the predictor outputting 1-(Y_1 mod 2). Here K=1 and that predictor's success is 0. Its output is still a valid value of F_1. This definitional issue does not affect the main theorem, which only uses the universal upper bound.

At r0=t=2n^2 ell, use log(1+1/t)<=1/t. The logarithm of the overhead is at most

    pi n/(4t) + n/(2t) = (pi/8+1/4)/(n ell),

which is exactly the declared Gamma bound.

The metadata condition is necessary. It is satisfied in the A-FRAC completion: after fixing the source state z and its proof-only H, S and G retain their independent original laws. The good-source event depends only on z. Revealing arbitrary secret-dependent data would violate this condition; revealing S itself, for example, would force success 1 regardless of a small K. The actual independent-error endpoint must not be augmented by H; only the completion endpoint has the independent H representation. The supplied A-FRAC proof retains that distinction and its expectation normalizer in formula P5.

## 4. Prime-list construction and effective resource bound

The primary publisher PDF, Xylouris, Acta Arithmetica 150 (2011), printed page 66, Theorem 1.1, states the least-prime bound with exponent 5.18 and an effectively computable absolute constant. The exact observed web response is preserved in `inputs/Xylouris-web-response.json`. A direct binary download was attempted but DNS resolution was unavailable; the source was successfully read through the web tool. The exponent 6 weakening for modulus at least 1 is valid.

Set R0=M+n and B=R0+t0+2. Bertrand supplies B<p<2B. Since n is a power of two and p>B>n, p is coprime to 2n. The R0+1 values of t range from t0 through t0+R0=B-2<p, so their residues modulo p are distinct. At most one makes 1+2nt divisible by p. At least R0 remain.

Every retained a_t=1+2nt is already the positive representative less than m=2np; it satisfies a_t>=Qmin, is 1 modulo 2n, and is coprime to p, hence to m. Two retained progressions are distinct modulo m. Each first prime in its progression is at least a_t>=Qmin; no positive prime with a negative progression index was omitted, because 0<a_t<m. The first primes are distinct and at most C m^6<C(4nB)^6.

Finding p and the progression primes by trial division therefore takes polynomial time in numeric n,M,Qmin, with an absolute effective exponent and constant. The bound is about numeric parameters, not only their bit lengths. The ideal is never consulted in constructing the master list. Since D<2^n, it has fewer than n distinct prime divisors; otherwise even the product of n integers at least 2 would be at least 2^n. Testing listed q by D mod q requires no factorization.

## 5. Main target filtering, source completion and advantage

Write dbar(q)=E_S d(q,S). Passing from the master list of M+n to the kept list of M discards exactly n entries, including any surplus surviving entries. Since each dbar is in [-1,1],

    |sum_(q in Q) dbar(q)| >= (M+n)epsilon0 - n,
    |average_(q in Q) dbar(q)| >= epsilon0 - n/M >= epsilon0/2 = epsilon.

This holds for either sign and even when signs vary by q. Dependence of the deleted subset on the fixed ideal is harmless because the original promise is pointwise for that ideal and the inequality bounds every subset of that size. Averaging over ideals would not suffice.

The ideal uniform-multiplier wrapper success is at least

    epsilon/2 - eta_ext - nu_ext = 15epsilon/32.

The finite extractor is just another possibly randomized predictor in the fractional source world; it needs no off-promise correctness there.

For the inherited source-completion interface take k=K and L_A=ell. The stacked multiplication matrix has Kn rows. The specified sigma obeys

    sigma >= 8 n^2 sqrt(Kn) ell^4
          >= 4sqrt(2) n^2 sqrt(Kn) ell^4
           = 2 t s sqrt(Kn) ell.

The inherited existential basis bound is tau2<=n^2 D^(1/n)<2n^2, so the declared theta_A, with exponent 3ell^2/4, conservatively bounds the completion's dual-theta terms. No short basis needs to be computed or supplied. The full-law completion retains S, the entire K-sample transcript and metadata. Its independent proof variables G,H are used only analytically.

For each fixed q, the completion source success is at most delta_tail+eta_A+Gamma K_q, capped by 1 where appropriate. The fixed partition is reduction of the binary cube modulo the same J for every q. Since C_J<=D, the fiber bound gives average source success at most delta_tail+eta_A+Bfun. If Gamma times the coarse fiber bound exceeds 1, the trivial success bound supplies the stated minimum in Bfun.

For the B-GP bridge, coefficient width w_B=ell^2 and r_B=ell^2 give s=sqrt(2)ell^2 and canonical width w=sqrt(n)ell^2. The smoothing prerequisite r_B>=sqrt(log(8n/eps_B)/pi) holds already from ell>=ceil(log2(2nK))>=2: n<=2^(ell-1), so its squared logarithmic right side is at most (ell^2+ell+2)log2/pi, far below ell^4. The scalar error probabilities are within their required range.

The two endpoint implementation losses add to precisely

    E_bridge = 2K eps_B/(1-eps_B)
             + 2pi Kn/(P r_B) + 3Kn nu + 2eta_cap.

The three Kn nu terms are the bridge scalar approximation once plus target error approximation in both endpoints. Each endpoint pays its own global finite-uniform cap allowance. The cap U_all covers quotient-coordinate sampling and the bridge/error scalar proposals. L_+ is a valid common upper bound because log(16/nu)=(ell^2+4)log2<=ell^2+4. The extractor's finite field draws are separately charged; its uniform-world loss nu_ext was already included above. In the fractional source analysis it remains an arbitrary predictor, so no additional extractor loss is necessary.

Applying the guard yields average implemented wrapper difference at least

    15epsilon/32 - (Bfun+delta_tail+eta_A+E_bridge)
      >= 15epsilon/32 - epsilon/8 = 11epsilon/32.

Thus at least one actual kept modulus has a signed difference at least 11epsilon/32>delta. There is no claim that a prescribed q, or every q, is good. The wrapper samples one S per complete physical K-sample batch and shares it across all calibration/test blocks. Fresh wrapper calls draw fresh S. This matches both the extractor and the C8 Boolean-oracle interface.

## 6. Common C8 instantiation, exact verification and all-input costs

The quantity a0 is proportional to 1/q. Replacing q by Qmax makes a0 smaller and S larger, so the selected Smax and kappa bounds cover every q in Q. The exponential coordinate-rounding guard is strongest at Qmin and is imposed there. Likewise d0<Qmin/(4D^(1/n)) covers every q. Taking chi>=a gives v0>=2sqrt(n)a, and the displayed d0 satisfies the exact C8 identity

    v0*d0 = delta*w/(32nK) = h0.

Q_* is computed before epsilon_C and a, exactly as required by the inherited noncircular definition. Its finite loops remain bounded on all answer sequences, including incorrect orientations and bad moduli.

The input to the run for q is qT=q lambda+q e in qJ^-1, with canonical infinity error at most q r<=d0. On at least one favorable fixed q, the inherited C8 success probability is at least 1-p. The argument needs no statistical method to identify q, because the decoder runs the entire fixed schedule. It also needs no independence between success events at different q: success of that one fixed favorable call is sufficient.

For x in J^-1 nonzero, (x)J is an integral ideal and |N(x)|D>=1. AM–GM and Parseval imply ||x||_2>=D^(-1/n). The outer radius satisfies

    r=d0/Qmax < (Qmin/Qmax)/(4D^(1/n)) <= D^(-1/n)/4.

The true error has coefficient norm at most its canonical infinity norm, hence at most r. Every outer-accepted candidate is also within coefficient distance r. A distinct accepted candidate would yield a nonzero difference in J^-1 of norm at most 2r<D^(-1/n), impossible. Therefore failures at bad moduli cannot cause a wrong outer output, even if their internal C8 outputs are arbitrary lattice vectors.

The final comparison is genuinely exact: delta, ell, K, chi and Qmax give rational r, and chi is an integer. Both target and candidate are rational in coefficient coordinates, so squared coefficient distance and r^2 are rational. Equality at r is accepted. A target T=(r,0,...,0), lambda=0, J=R illustrates a rational target exactly on both the coefficient and canonical boundary; no transcendental sign test is required. Exact ideal membership is ordinary rational linear algebra/integer-coordinate testing.

Finally kappa>=log(8n/zeta) gives (n/2)exp(-kappa)<=zeta/16, hence p<=17zeta/16. The total wrapper and D_alg call counts are the stated M Q_* and M Q_*[(n+1)Ncal+Qmax Ntest]. Each physical wrapper consumes K source points, independent of its much larger D_alg call count. Arithmetic, root/idempotent enumeration in q in value, bounded field coins, bridge routines, input reading, and actual D_alg execution cost must all be charged as Section 4 says. There is no need to union-bound the decoder error over all M moduli.

## 7. Polynomial family: what follows and what does not

Fix b,c,rho as in the corollary. The prime construction has B=O(n^(b+2c+11)) and Qmax=O(n^(6b+12c+72)), with constants depending on the absolute prime theorem. Therefore log Qmax=O(log n). The exact extraction parameters satisfy

    Ncal,Ntest = O(n^(2c+2) log n),
    K = O(n^(b+2c+2) log n),
    ell = O(log n),
    sigma = O(n^((b+2c+7)/2) (log n)^(9/2)).

Thus Qmin=n^(b+2c+12) dominates n sigma. Also

    sqrt(mu) = O(n^(-c-3/2)),
    sqrt(D/2^n) <= 2^(-(1-rho)n/2),
    Gamma = 1+o(1).

All remaining guard errors are a polynomial in n times exp(-Omega((log n)^2)), uniformly over D<=2^(rho n). They are o(n^-c), while epsilon/8=n^-c/16. Hence G-AM holds for sufficiently large n.

Writing a0,max in a simplified form gives

    a0,max = D^(1/n) w/(nQmax) * (delta/(32nK))^(2/n).

Accordingly Smax=O(n log n), and one can choose kappa polynomial in n, for example of order K+n log n+delta^-1+log(zeta^-1), with a sufficiently large constant and a conservative certified rounding to cover the strict exponential guard. For such a choice Q_* is polynomial, log Q_*=O(log n), chi=a=O(sqrt(log n)), and d0 is far smaller than Qmin/(4D^(1/n)). The radius r is inverse polynomial. The coefficient grid's encoding length log P=2ell^2 is also polynomial.

What does not follow is a polynomial bound on P itself: its displayed superpolynomial lower bound is unconditional, even before using the much larger actual K. Nor do the lower bounds on kappa prohibit an enormous choice such as 2^(2^n). In addition, an ordinary basis can be encoded with arbitrarily many bits even for J=R, and an all-input bounded D_alg need not itself have polynomial-n runtime. A statement about total polynomial-n operations needs those encoding/runtime qualifications. These are explicit resource-scope issues, not a need to change the source law or extraction argument.

At c=0, epsilon0=1. For each fixed q and every (A,B), the uniform comparator has positive mass and the planted law has positive mass, since the discrete Gaussian puts positive mass on every integer error vector. Their common finite support implies TV<1. Averaging over the same finite modulus law preserves this strict inequality. Thus no supplied Boolean code satisfies gap>=1. The numerical estimates still prove nonempty parameter/ideal instances, for example J=R at sufficiently large n, but not a nonempty oracle-premise class at this endpoint. For c>0 this exact-endpoint obstruction disappears; existence or computational efficiency of a distinguisher is not asserted by the reduction.

## 8. Boundary cases and mandatory probability regression

* **n=2, J=R.** The finite components are meaningful. At any split q>=5, each selected root distinguishes the four binary polynomials, so K_q=1/4. The main coarse Bfun is at least sqrt(1/4)=1/2, whereas epsilon/8<=1/16. Consequently G-AM fails; the main success theorem has no n=2 instance under its stated guard. This is a parameter restriction, not a hidden exceptional successful decoder claim.
* **Singleton cube fibers.** K_q=1 and optimal functional success is exactly 1 because the residue identifies S. The upper bounds cap at 1. The main assumption D<2^n precludes all cube fibers being singleton.
* **Repeated primes.** The explicit n=16, q=97 repeated-list example above violates the bound; present distinctness excludes it.
* **Gap signs varying with q.** Absolute signed filtering and E|d| handle this; no common D_alg orientation is assumed. C8 separately runs both orientations of its own wrapper.
* **Same secret in all physical blocks.** Required and obeyed. Fresh per-block secrets would invalidate the extractor. A fresh secret per full wrapper call is compatible with C8.
* **Fixed-q-only distinguisher.** Insufficient for the premise. Neither the average source bound nor running all moduli manufactures unavailable oracle behavior at the other q values.
* **Exact rational radius boundary.** Accepted by the outer <= test; rational r eliminates an undecidable equality comparison with a general computable real.
* **Failed or empty numerical guard.** No success conclusion. The guard is a supplied true inequality, not an algorithmic demand for an unbounded equality test. The all-input C8 schedule still terminates off promise.
* **Source family.** J remains the same ordinary represented integral ideal throughout. The theorem does not transfer to arbitrary ideals or assert hardness of the restricted family. Simple ideals and elementary sampling subfamilies are not counterexamples to this conditional direction.

I also reproduced CP-1 from the mandatory protocol using exact fractions. After conditioning, A_b=21/2000, C_b=1/20, D=879/1000. Initial incidences are p(x)=1/10, p(e_b)=121/2000 and p(f_b)=21/2000. The two-hit event has probability 21/2000>1/100=gamma^2, while the second residual incidence after transfer is 21/221<1/10. The old sequential product argument is therefore rejected. Its failure is support restriction and posterior renormalization, not merely correlation of a fresh oracle value. The present proof uses full joint Gaussian masses and conditional concentration on a genuinely disjoint bank, with union bounds only; it does not invoke the rejected rule or expose latent cache-hit status.

## 9. Preserved finite falsification checks

Experiment BLIND1-EXACT-01 was registered, code-hashed and granted a slot by the coordinator before execution. Its full code is `experiments/exact_checks_01.py`; the controlled runner enforces 120 seconds wall, 110 seconds CPU, 512 MiB address space and a process-group kill on timeout. There were no random seeds because every loop was deterministic and finite. The command was `python3 experiments/controlled_run_01.py`, from this review directory.

It completed with exit status 0, wall time 0.967681940 seconds, user CPU 0.927988 seconds, system CPU 0.010902 seconds and maximum RSS 12288 KiB. Full stdout, empty stderr, resource status and their hashes are preserved. Code SHA256 is `3ab454cb0bc89cb691fdc820d3910823921d3689753bfce752e5fb717caad495`.

The checks cover:

* 1,000 exact CRT transformation histograms for n=2,q=5, every binary secret, every ring error atom, both selected roots and every candidate value. All transformed laws exactly match their claimed hybrids.
* 88 nonzero ternary norm cases in dimensions 2 and 4, with all split primes through 257; the product of prime powers from root collisions divides the exact algebraic norm. Forty-four parity-ideal cases also satisfy the optional quotient-norm refinement.
* Twenty-five small fixed partitions, including every partition of the four-point n=2 cube, and coordinate/parity/evaluation partitions for n=4. Their computed selected-root averages satisfy the bound. Displayed log/square-root comparisons are exploratory floats, with the unrestricted theorem justified analytically above.
* Twenty-seven small auxiliary-progression prime-list constructions for n in {2,4,8}, M in {1,2,4}, Qmin in {3,10,30}, checking coprimality, lower bounds, distinctness and split congruences.
* The exact CP-1 calculation just described.
* A selected-functional finite approximation with J=Z^2, F_1(S)=S_1, F_2(S)=S_2 and Gaussian weight (16/17)^||g||^2, truncated to [-40,40]^2. Exact integer weights give success approximately 0.5967614195567307, between K=1/2 and the analytic envelope approximately 0.708316955577953. The omitted two-dimensional Gaussian tail has the rigorous-form upper bound 4(16/17)^41^2/[1-(16/17)^83], displayed as approximately 2.218e-44. The rational numerator and denominator are retained in full; the largest integer has 13083 bits. This is evidence for a targeted finite boundary, not proof of the infinite statement.

No failure was hidden or repaired inside the experiment. The preregistered program succeeded on its first execution. The direct source-download failure and the unavailable `python` alias used in an initial archival command are operational failures preserved in the exposure/checkpoint notes; the archival command was rerun with `python3`. No unregistered mathematical experiment was run.

## 10. Certification limits

This is a sealed blind statement audit, not a delivery build or a comparison against a current author proof. The new mathematical construction is justified above relative to the permitted inherited interfaces. The literal whole statement remains non-accepted because of the polynomial-value sentence and the selected-functional optimality definition. The exact endpoint epsilon0=1 needs the stated interpretation of nonemptiness. These findings should be reconciled against a frozen revision, with downstream resource prose checked again. The report must not be represented as fresh independent verification of the inherited C8 proof, a practical parameter estimate, an arbitrary-ideal hardness foundation, or an accepted quantum composition.
