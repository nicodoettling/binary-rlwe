# FULL2 exact-version full proof review

This is a nonauthor review of FIXED-MAIN-v1, MR-v1, AM-MAIN-v3, SFUNC-v2, DD1-EXTRACT-v1, DD2-AM1-SNF-v1 and DD2-PRIMES-v1. The assignment is preserved verbatim. Exact input hashes and read scopes are in read-register-v1.json and input-manifest-v1.json; inherited acceptance matches are in dependency-hash-check-v1.json. This reviewer read prior FULL1 and BLIND1 material after reconstructing the principal current arguments, and never read or contacted BLIND2. Same-model review is correlated scrutiny, not independent statistical confirmation.

**Verdict: the mathematical reduction, changed variable-width edge, and repaired AM polynomial-resource corollary pass this review. The exact FIXED-MAIN-v1 packet is not accepted as literally written because its last sentence falsely describes every executed D0 input as having the promised discrete-Gaussian law.** FULL2-WORDING-1 was preserved and sent to the coordinator before any revision. It affects scope prose, not the proof: the proof already uses exact target promises, TV comparisons, hybrids and an all-input runtime bound correctly. No unseen repair or descendant inherits this verdict. Coordinator blind, regression and delivery acceptance remain separate gates.

## 1. Frozen model, dependency graph and scope

Fix power-of-two n>=2, an ordinary-basis represented integral ideal J, D=N(J)<=2^(rho n), rho<1, target q0>=2, rational sigma0>=1, sample count k0, advantage lower bound epsilon_* and bounded randomized Boolean code D0. If D0 sees J, its target promise is pointwise for this J. The planted target uses a single uniform coefficient-binary S across all k0 samples, independent uniform ring A_i and independent coefficient D_(Z,sigma0) errors. The comparator keeps public/metadata laws and uses independent uniform responses. Executions are fresh code executions with fresh private coins, not a stateful service.

The master list is independent of J and consists of M+n distinct odd split primes. After divisibility filtering and truncation, exactly M remain; widths sigma_q=(q/q0)sigma0 are fixed per modulus before sampling. G, H, the short ideal basis, occupied cube fibers and a favorable q are proof objects, never supplied executable advice.

The reviewed graph is: exact fixed-target gap -> MR pointwise auxiliary gaps -> filtered average -> DD1 selected-value success; DD2 root fibers + SFUNC + A-FRAC full completion -> fractional selected-value upper bound; B-GP and both finite endpoint charges -> average finite GP gap; one fixed favorable q + common C8 parameters -> a q-scaled lattice candidate; exact outer verification -> the unique J^-1 solution. DD2 prime generation and asymptotic substitutions separately establish compatible polynomial-value parameter families.

| Exact edge | Review disposition | Essential check |
|---|---|---|
| MR scalar normalization/coupling | PASS | Actual discrete normalizer, unconditional coupling marginals, shift and boundary losses |
| MR full batch and signed gap | PASS | Negacyclic identity, fixed tie rule, conditional errors, both endpoint biases |
| Fixed target -> AM-v3 variable widths | PASS | Pointwise common orientation; exact sigma_q; no oracle promise at other target moduli |
| DD1 extraction and finite caps | PASS | CRT bijection, complete fixed-secret conditioning, disjoint banks and additive failures |
| SFUNC-v2 | PASS | Optimal Bayes definition, selected max inside sum, positive theta normalizers |
| DD2-AM1-SNF-v1 | PASS | Root nullity consumes norm valuation; distinct primes and common partition |
| A-FRAC -> variable-width selected completion | PASS | Full Kn-row covariance and source-only conditioning; monotone lower bounds |
| B-GP-v2 -> bounded A_q | PASS | Exact original kernel and natural-log ceiling, both endpoint caps |
| AM-v3 -> common C8 and exact verifier | PASS | Canonical/coefficient scales, fixed schedules, rational radius, uniqueness |
| DD2-PRIMES and both numerical families | PASS | Effective primary bound, polynomial numeric values, noncircular order |
| AM-v3 repaired polynomial prose | PASS | logP rather than P, chosen polynomial kappa, full input/code/evaluation costs |
| FIXED-v1 final universal execution-law sentence | REJECT | D0 executions include rounded and hybrid inputs; only its promise has the exact target law |
| Arbitrary-ideal hardness, coherent DGS, one family covering all PPT exponents | NOT ESTABLISHED | Explicitly outside the mathematical conclusion or quantitative guards |

The inherited A-FRAC, B-GP and C8 theorem/proof hashes match their exact acceptance records. Their old provisional file banners are not the acceptance source. The recent cube-theta acceptance is also hash-matched; its selected-functional extension is reviewed anew. C8's accepted scope is finite classical same-ideal GP-to-BDD, not its excluded quantum or arbitrary-family discussion.

## 2. Modulus rounding, full laws and constants

Let lambda=q/Q. With full integer coefficient representatives, C=rnd(lambda Abar) and Delta=C-lambda Abar. Write Bbar=Abar*S+E-QZ in the integer negacyclic ring. Because qZ and C*S have integer coefficients and rnd(x)=floor(x+1/2) commutes with every integer translation,

    B' = C*S + rnd(lambda E-Delta*S) mod q.

This identity includes negative wrap contributions and the possibility C_j=q. Every Delta coefficient lies in[-1/2,1/2], so each coefficient of Delta*S has absolute value<=n/2. Nearest-even rounding would not support the identity: FULL2-FV1 gives Q4,q2,n1,a2,s1,e=-3 with mapped output0 and claimed residual output1. The prescribed upper-tie rule survives45,052 exact independent checks, including composite target moduli4,6,8, n4 negacyclic products and12,480 half-integer coordinates.

For g_s(x)=s^-1 exp(-pi x^2/s^2), integral |g_s'|=2/s. Summing the cell integral discrepancy gives L1<=2/s before normalization. If A=sum_z g_s(z), then |A-1| is at most that discrepancy and sum_z|g_s(z)/A-g_s(z)|=|1-A|. Thus TV(D_Z,s,rnd(G_s))<=2/s. This explicitly retains rho_s(Z); no exact rounded-continuous/discrete equality is asserted.

For s>=1, Poisson summation bounds the periodized density by rho_s(Z)/s<=1+1/s<=2. Under a maximal coupling E with rnd(G_(sigma/lambda)), failure costs at most2lambda/sigma. On a match, |lambda E-G_sigma|<=lambda/2; a rounding disagreement implies G_sigma+c lies within lambda/2 of a half-integer, costing at most2lambda. The failure event and boundary event may be dependent; the proof only uses their unconditional union bound. Translation changes continuous Gaussian TV by at most |c|/sigma, and a final normalization comparison costs2/sigma. Consequently

    TV(rnd(lambda E+c),D_Z,sigma)
      <=2lambda/sigma+2lambda+(|c|+2)/sigma
      <=4lambda+(n/2+2)/sigma.

Now condition on the entire public A bank and the one S. All shifts are deterministic and the original kn error coefficients remain independent; product TV is valid at this conditioning. Integrate the complete law, retaining S. The intermediate target-error law is a kernel of (A',S) with fresh independent target errors. Only then replace A' by uniform. Each cyclic public fiber has floor(Q/q) or ceil(Q/q) points, including exact ties, so its TV is at most q/(2Q)<=lambda. This yields planted TV<=kn[5lambda+(n/2+2)/sigma]. In the comparator, all2kn original A,B coefficients are independent uniform, so its loss is<=2kn lambda. Both worlds are paid in the signed-gap bound7kn lambda+kn(n/2+2)/sigma, capped by2.

The two fixed guards bound these summands by epsilon_*/8 each. At every auxiliary q, the wrapped code therefore has the same gap sign as D0 and magnitude>=3epsilon_*/4. Averaging preserves that sign and exceeds epsilon0=epsilon_*/2. There is no secret-dependent favorable-prime conditioning or assumption that the fixed q0 is prime. Only auxiliary primes enter CRT extraction; MR itself is valid for every integer target modulus>=2. All rounding arithmetic is exact rational/integer arithmetic with polynomial bit cost.

The identity and complete law are the point at which shared-secret grouping matters. Our independent q0=4,n1,k2 zero-error control has equal one-sample marginals under common and independent secrets, but full joint TV9/32. The proof never makes that replacement.

## 3. Extraction and filtered advantage

An integer D<2^n has fewer than n distinct prime divisors. Keeping exactly M entries from M+n deletes exactly n, including surplus coprime entries. If d_q is a signed gap, |sum_Q0 d_q|>=(M+n)epsilon0 implies sum_Q0|d_q|>=(M+n)epsilon0. Each deleted term costs<=1. Thus E_Q|d_q|>=epsilon0-n/M>=epsilon0/2=epsilon. Both metadata laws and the fixed partition remain unchanged.

At fixed q,S=s, (A,p)->(A+p e_j,p) is a bijection. Thus A' is uniform and independent of p,E,W, and

    B'=A's+E+(t-s(r_j))p e_j+W.

The correct t gives hybrid j-1; every wrong t gives hybrid j by the field permutation. This retains the entire possibly CRT-correlated error vector. It does not use the target promise on a nonuniform-A source.

Put a=epsilon/(64n). Each fixed calibration prefix has independent block outputs conditional on s, although different prefix estimates reuse a bank. Hoeffding followed by a union bound gives error<=eta_ext/2 because2Ncal a^2>=Lcal>=ln(4(n+1)/eta_ext). On simultaneous calibration accuracy, a passing empirical gap16a has true gap>=14a>4a. A good secret with |d(q,s)|>=epsilon/2 forces a true adjacent gap>=32a and empirical maximum>=30a, so it passes.

Condition on the complete calibration transcript and s. The disjoint test bank retains its original independent-block law. Each t estimate is concentrated about the correct endpoint; reuse across guesses is handled by a union bound, not independence between estimates. The true candidate is within2a of its calibrated endpoint and at least12a from the other; all wrong candidates reverse this. Thus one marked candidate is correct except for the summed failure events. The4a equality counterexample remains rejected.

For X=|d(q,S)|<=1, EX>=epsilon gives Pr[X>=epsilon/2]>=epsilon/(2-epsilon)>=epsilon/2. Losing eta_ext+nu_ext gives15epsilon/32. The capped field sampler couples to ideal draws until its first failure and costs at most Tfield_max*2^-Bext<=nu_ext pointwise for every input/history. This is the only field cap charge needed: on the fractional endpoint, the whole capped extractor is simply an arbitrary predictor.

The raw bank is K=k0(Ncal+Ntest). Its D_alg call count is (n+1)Ncal+qNtest. These are different quantities; the Gaussian completion correctly uses Kn rows. Whole-bank TV is contracted under the entire reused-bank extractor, not multiplied by its oracle call count.

## 4. Selected functional and distinct-prime arithmetic

SFUNC-v2 explicitly defines optimal Bayes success. Its exact formula has max_(j,v) inside the sum over every observed y. With cube center u and a^2=t^2+r0,

    rho_t(y-b)<=exp(pi n/(4r0))*rho_a(y-u).

For residue c, each selected sum has at most max_(j,v)N(c,j,v) terms. Sum the common envelope on that occupied coset, bound its shifted theta by rho_a(J), and retain the ratio

    rho_a(J)/rho_t(J)
       =(a/t)^n rho_(1/a)(J*)/rho_(1/t)(J*)<=(a/t)^n.

Both normalizers are positive. The residue-only optimum is exactly K_F, giving the lower bound for the defined optimum, not for a deliberately incorrect predictor. Taking r0=t=2n^2ell yields Gamma. Arbitrary secret-dependent metadata, including revelation of S, would violate the required conditional product premise.

For nonzero ternary f=b-b', the negacyclic multiplication determinant is its nonzero integer algebraic norm. Parseval and AM-GM give |N(f)|<=n^(n/2). At a split prime, the number m_q of vanished roots is the modular matrix nullity. Its Smith form proves q^m_q divides |N(f)|. Distinct q give sum m_q logq<=log|N(f)|. This charges every vanished root, including multiple roots of f at one q, without equidistribution or independent root assumptions.

For a fixed binary fiber B_c of size m_c, max bin squared is at most m_c+T_c(q), where T_c counts all ordered distinct collisions over roots. The diagonal m_c appears once. Jensen, the norm budget and Cauchy-Schwarz yield average K_q<=sqrt(C_J/2^n)+sqrt(mu). The same pairs are used across q: a q-dependent partition is not silently permitted. The repeated-q97 control remains outside the distinct-prime premise. C_J<=D gives the used coarse bound; no algorithm enumerates C_J or K_q.

## 5. Variable-width completion and finite endpoints

For every retained q, source state z contains the unwrapped a_i~D_(J^-1,s). The lattice MGF from shifted-theta maximality gives the declared source-only tail. On its good event, the complete Kn-by-n multiplication matrix obeys ||M||op<=s sqrt(Kn)ell. The floor guarantees

    sigma_q>=sigma_floor>=2ts sqrt(Kn)ell.

Hence C_q=sigma_q^2 I-t^2MM^T>=3sigma_q^2 I/4 and Theta_q=t^2I-(t^4/sigma_q^2)M^TM>=3t^2I/4. These inequalities improve as sigma_q increases; equal widths were never needed. The existential basis norm<=n^2D^(1/n)<2n^2 makes the uniform theta exponent at least3ell^2/4. Therefore the same eta_A works at all sigma_q.

A-FRAC's exact completed mass is proportional to rho_sigma_q(e)rho_Theta_q(J-mu_e); its normalized expression divides by the actual expectation of the theta ratio. H is integrated out before comparing to the independent-error endpoint. In the completed experiment only, H is independent of S,G conditional on z. Revealing z,H,Y=S+G can enlarge predictor power while retaining the original conditional S,G law. Thus SFUNC applies pointwise, and averaging DD2 yields fractional success<=Bfun+delta_tail+eta_A. No source ideal Gaussian or H is sampled by the executable wrapper.

B-GP uses coefficient widths w_B=r_B=ell^2, source width s=sqrt(2)ell^2 and canonical w=sqrt(n)ell^2. Its smoothing guard follows from ell>=2 and n<=2^(ell-1). The exact finite scalar kernel is the accepted v2 kernel, including its exact natural-log ceiling addendum. Changing target-error sigma_q changes proposal interval N_B and bit cost, not trial count. Width>=1 makes normalized acceptance uniformly Omega(1/K_B), since both the normalizer and interval size scale linearly with width. The uniform-draw cap success remains>=1/2 at every interval size.

The complete two endpoint losses are:

| Endpoint | Charge |
|---|---|
| Uniform GP input -> uniform-A completed target | Kn nu+eta_cap |
| Rounded GP -> exact fractional completed source | 2K eps_B/(1-eps_B)+2pi Kn/(P r_B)+2Kn nu+eta_cap |
| Sum | E_bridge |

Quotient cap failures are paid in both endpoints; exact uniformity belongs only to the uncapped quotient version. With the functional/tail/completion losses, G-AM leaves average U-minus-GP gap>=15epsilon/32-epsilon/8=11epsilon/32>delta. At least one fixed retained q is favorable. Its existence is analytic; no unavailable source experiment or statistical favorable-modulus selection is required.

## 6. C8 composition, verifier and useful radius

The exact C8 theorem8/algorithm2/proof9 were read. Substituting k=K, canonical w=sqrt(n)ell^2 and delta=epsilon/4 gives h0=v0d0 independent of chi. The a0 value decreases with q; choosing Qmax gives the largest S guard. Qmin gives the strongest reconstruction and uniqueness guards. Loop counts precede epsilon_C and chi, so there is no circular choice. Wrong orientations and bad-modulus executions retain the same finite bounds.

For the fixed favorable q*, input q*T is within canonical infinity distance q*r<=d0 of q*lambda. C8 succeeds with probability at least1-p. Its exact rational final threshold and all physical-kernel numerical charges remain the accepted ones. Running all M schedules requires no independence between their successes: failure of the outer algorithm implies failure of that one fixed favorable execution.

For nonzero x in J^-1, xJ is an integral ideal, so |N(x)|D>=1. Parseval/AM-GM imply coefficient norm>=D^(-1/n). The outer radius r=d0/Qmax<1/(4D^(1/n)) is rational because canonical sqrt(n) factors cancel and chi is integer. True error has coefficient norm<=canonical infinity norm<=r; hence it passes exact squared-distance<=r^2. Two accepted distinct candidates would differ by coefficient norm<=2r<D^(-1/n), impossible. Arbitrary bad-q outputs therefore cannot cause a wrong result.

Also1 belongs to J^-1. Its minimum nonzero canonical infinity norm lies between D^(-1/n)>=2^(-rho)>1/2 and1. Thus the asymptotic inverse-polynomial absolute r is an inverse-polynomial fraction of the lattice's canonical separation, not merely a scale-dependent positive number. This is an interpretation of existing hypotheses, not an additional hardness theorem.

kappa>=log(8n/zeta) gives p=(n/2)e^-kappa+zeta<=17zeta/16. Calls are bounded by M Q_* wrappers and M Q_*[(n+1)Ncal+Qmax Ntest] D0 executions, each receiving k0 fixed-modulus ring pairs. Total physical GP components are<=M Q_* K. Their generation, all repeated input copying/evaluation, root setup and full D0 code runtime are additional charged work.

## 7. Probability regression and finite evidence

FULL2-FV1 was preregistered and code-hashed before its granted light slot. It ran under120s wall,110s CPU,512MiB address space and process-group timeout cleanup, completed exit0 in1.97s with12MiB maximum RSS, and preserved code, stdout, stderr, resources and receipt. There was no mathematical failure or inline test repair.

CP-1 was independently enumerated over all160 prior trace/oracle atoms. The vk normalizer is10/11; posterior masses are A_b=21/2000,C_b=1/20,D=879/1000. Initial incidences are x=1/10,e_b=121/2000,f_b=21/2000, all light under strict >1/10. The two-hit event has mass21/2000>1/100, while after the selected cached-prefix transfer the later incidence is21/221<1/10. The competing envelope mass rises from121/2000 to221/2000. Support restriction and posterior normalization cause the failure; fresh local oracle independence does not repair it. Current proofs use pointwise conditional laws, additive couplings or an adapted martingale; none branches on hidden cache-hit status or multiplies marginal survival probabilities.

Our additional exact controls cover composite-target fibers, n1/n2/n4 identities and tie failures, a complete retained (S,A',B') two-sample law, the shared-secret negative control, and widths up to257 numerator bits whose proposal lengths grow while trial caps remain common. These are finite falsification evidence, not proofs of infinite Gaussian estimates.

Root MR-FV1/MR-FV2 were inspected through code, preregistrations, complete outputs, receipts and resources. The first failure is solely large-rational decimal logging; a one-line digest change explains the successful rerun. MR-FV2 has68,200 identity cases,12 retained-bank cases,20 exact rational truncated-Gaussian controls and9 floating scalar controls. The rational controls' bounds exceed1; the useful small-TV numeric controls are floating, not rigorous intervals. The analytic normalized coupling, not those tests, establishes MR's infinite claim.

regression-dispositions-v1.json preserves all164 inherited exact references and statuses, verifies every source-registry and canonical-entry hash, and gives scoped current dispositions for those164, all29 new root entries and5 FULL2 findings. Retired tower, class/order, weighted and quantum constructions are expressly retained outside this graph; their rejection is not erased or promoted to a current success. No wholesale reexecution of historical jobs is claimed.

## 8. Final scope and required repair

The sigma0>=8k0 n(n/2+2)/epsilon_* window remains explicit. Fixing b,c before sigma0 gives a nonempty family of numerical/source parameters for those exponents, not one noise/modulus family covering all polynomial sample counts and inverse-polynomial advantages. This is a quantitative conditional reduction, not a claim that an efficient promised distinguisher exists. The restricted ideal-family foundation remains open; simple/easy eligible ideals do not establish it. No arbitrary-ideal transfer, practical security estimate, coherent-code composition or quantum sampler follows.

The repaired AM-v3 corollary correctly charges logP and may have superpolynomial P; it chooses polynomial-value kappa and chi=a and retains input/evaluation/oracle costs. Its older literal all-parameters assertion stays rejected. The AM finite epsilon0=1 endpoint is merely vacuous; the current asymptotic families use c>=1 and FIXED uses epsilon0=epsilon_*/2<1.

The remaining current rejection is the exact final FIXED-v1 execution-law sentence. All D0 calls do use q0. Their distributions are not all exact planted target distributions: the construction uses transformed inputs, CRT hybrids and finite approximations. The correct statement is that the **assumed advantage** concerns the prescribed exact target laws, while every executed transformed/hybrid input is handled by bounded code. The proof already follows this distinction. Seal this review against v1, then review any replacement exact bytes separately.
