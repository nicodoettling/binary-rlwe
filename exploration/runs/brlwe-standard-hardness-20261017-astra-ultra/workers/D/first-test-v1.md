# D first discriminating test and scope audit v1

Status: **PROVISIONAL**. This report audits a restricted information argument and rejects named endpoint shortcuts. It establishes no computational hardness and is not self-certified. Frozen baseline is SC-v1; inherited EX-v2 is used only in its accepted conditional scope. The first executable control completed before the initial checkpoint deadline.

## 1. Prior entropy argument: what the proof actually supports

Read prior workers/A/entropy-budget-{theorem-only,proof}-v1.md and experiment-directions-v1.md, together with the prior final, claims, reconciliation, source/parameter comparison, regression registry, full EX-v2 proof and recorded reviews. The prior A-H3 argument appears mathematically sound within its stated scope; it remains PROVISIONAL until the coordinator's review gates close.

Let P_k be k ordinary integral RLWE pairs (a_i,a_i s+e_i), uniform shared s and iid uniform multipliers, with the full error tuple independent of all a_i,s. Let Q_k be the uniform law on all 2k ring entries. Conditional on the complete multiplier tuple, the secret multiplication map has rank r(a), where each CRT root contributes one unless all k multipliers vanish there. Thus E r(a)=n(1-q^-k), including every zero branch. Independent additive noise increases the entropy of the image-uniform law by concavity, so

    D(P_k || Q_k) <= (k-1+q^-k)n log q.

For any randomized channel K with input-independent coins and KQ_k exactly uniform on R^m, KL contraction gives

    H(KP_k) >= (m-k+1-q^-k)n log q.

The sparse source entropy satisfies H(Base_m)<=log binom(n,d)+md log q+mH_F. A maximal coupling with epsilon=TV(KP_k,Base_m) then gives

    h2(epsilon)+epsilon mn log q
      >= (m-k+1-q^-k)n log q-log binom(n,d)-md log q-mH_F.

For independent coefficient D_ell masks, H_F<=n[log(1+ell)+1/2]; wrapping only lowers entropy. The proof of this bound uses the Gaussian theta identity and a nonpositive derivative of its dual theta sum, with absolutely convergent series. No problematic sequential product is present. For fixed k,m with k<=m, polynomial q>=n² and either frozen sparse family, the resulting lower bound is epsilon >=(m-k+1)/m-o(1). The change from the old q family to the present q family does not alter this scoped entropy conclusion.

The obstruction does **not** cover computational planted simulation, arbitrary reductions/oracle access, input k>=m+1, or merely TV-close comparator preservation. More standard input samples are allowed by the current task. The output source budget m=2 is not the input RLWE sample budget k, and neither is the target recovery sample budget. A lower bound for two input samples is therefore not a barrier to the current goal.

The only density-controlled extension needed for comparison is elementary. If KQ_k(y)<=exp(alpha)/q^(mn) at every output y, the same argument gives the displayed bound with alpha subtracted on the right. Mere TV distance delta supplies only alpha<=log(1+q^(mn)delta), generally too large to preserve the obstruction. See the separately frozen theorem and proof files.

## 2. Exact erasure, projection, rank and noise controls

The executable finite model uses n=2,q=5, roots 2 and 3, k=m=2,d=1. It uses either zero source errors or independently uniform {0,1} coefficient errors; the latter is explicitly a finite surrogate, not D_ell. Every probability is an exact rational. Algebraic endpoint identities themselves hold with the original coefficient Gaussian law.

Erasure K((a_i,b_i)_i)=(b_1,b_2) maps the uniform comparator exactly to uniform R². Under planted ordinary uniform-secret RLWE it produces the exact mixture

    sum_(t=0)^n binom(n,t)(q-1)^t q^-n Base2_t.

For each fixed secret support T(s), multiplication by s maps uniform a_i to independent uniform I_T points, including zeros. The error law is unchanged and independent of these points. The resulting law depends only on T(s), so there is no posterior substitution. In the finite model the weights are (1,8,16)/25. With finite coefficient noise, TV(erased,uniform)=1521/15625 and TV(erased,Base2_1)=507/3125. Noiseless TV(erased,uniform)=5184/15625. All obey the nonunit upper bound 1-(1-1/q)^n=9/25. Selecting a fixed sparse support rank is a hidden rare event of weight binom(n,d)(q-1)^d/q^n; no public rejection sampler has been provided.

Projection chooses a fresh uniform d-set T, computes its CRT idempotent e_T, and outputs C_i=e_T b_i+G_i for independent fresh coefficient noise G_i. The comparator is exactly Base2_d, not ambient uniform. Conditional on the secret being nonzero at every selected root, e_T a_i s is independent uniform I_T and absorbs the entire projected source error e_T e_i. This event has probability (1-1/q)^d independently of the chosen T, so the planted output is within 1-(1-1/q)^d of the same Base2_d comparator. In the finite control, comparator-to-ambient-uniform TV is 144/625 and the two projected endpoints have TV 117/2000<=1/5. This rejects only this explicit projection construction, not all hidden-ideal simulators.

The complete input multiplier-rank distribution has counts (1,48,576) at ranks (0,1,2), among 625 multiplier pairs, giving mean 48/25=2(1-5^-2). This checks the exact zero branch in A-H3.

The finite iid coefficient noise has four CRT joint outcomes, while the product of its CRT marginals has sixteen. Their TV distance is 3/4. Thus even this smallest model strongly rejects silently replacing coefficient noise by independent CRT noise. No Gaussian surrogate assertion is inferred from this number.

## 3. Approximate comparator countercontrol

For noiseless ordinary uniform-secret k-sample RLWE, define the publicly testable event C that b lies in the image of s -> (a_i s)_i. Membership is polynomial-time linear algebra or CRT arithmetic and includes the all-zero multiplier branches. The planted law satisfies C with probability one. Under Q_k,

    gamma = Pr[C] = [q^(1-k)(1-q^-k)+q^(-2k)]^n.

At each root, a!=0 has q possible image b vectors, while a=0 has only b=0. These exact root counts multiply under the original independent uniform CRT input law, before any selection; this is not a CP-1 style posterior product.

Fix any independently samplable distribution B on R^m. On C output a fresh B draw; outside C output a fresh uniform draw. The planted endpoint is exactly B and the comparator is gamma B+(1-gamma)Uniform. Hence its comparator TV is gamma TV(B,Uniform)<=q^(-(k-1)n). For k=m=2 this is exponentially small while planted simulation is exact, directly falsifying an extension of A-H3 from exact preservation to merely negligible comparator TV. Choosing B=SC-v1 Base2 is legitimate for this endpoint construction because the local sampler can choose its own T,U,F; this does not reveal any challenge latent. Ideal exact Gaussian sampling can be replaced by bounded full-law approximations if an executable PPT claim is desired.

The actual finite experiment chooses the previously defined finite-noise Base2_1. It obtains gamma=14641/390625 and comparator TV 2108304/244140625, with planted endpoint exactly Base2_1. These finite values are regression evidence for the analytic formula, not a hardness statement. **Noiseless RLWE is not a standard hard input regime**, and this channel solves its own membership problem. No reduction from hard noisy RLWE is supplied.

For completeness, the input-budget threshold also has a sharp unrestricted-kernel control. When k>=m+1, gamma<q^(-mn). For any distribution B on R^m, let H=(Uniform-gamma B)/(1-gamma), which is a nonnegative normalized law. Output B on C and H otherwise. This maps noiseless P_k exactly to B and Q_k exactly to uniform. Computing/sampling H efficiently for general B is not asserted. This suffices to show that the information-theoretic claim cannot extend to arbitrary k without further hypotheses. The fixed-point-mass B case has an elementary efficient H sampler; it is not the requested Gaussian source.

## 4. Direction, losses, parameters and next tests

If a genuine map had planted law within epsilon of source B and comparator within delta of uniform, composing a source distinguisher with it would give ordinary-RLWE decision advantage at least Adv_B-epsilon-delta, with the map's exact input sample/runtime costs. For computational simulation, the discrepancy must instead be stated for the relevant composed distinguisher class and proved computationally. Erasure/projection above do not supply the required endpoints. The approximate control uses an easy noiseless input, so it also does not supply the desired implication.

The inherited exp(O(d)) hidden-ideal first-marginal attack remains a control: at the current q families, r the least power of two >=2d satisfies q^(1-d/r)>2n ell² eventually; for d=O(log n) this can give a polynomial attack. Both selected d families eventually grow faster than log n, which only avoids this immediate upper-bound regime. It proves no security or runtime lower bound. A known-ideal attack can use the revealed T; its failure also proves no hidden-ideal hardness.

B's communicated unit-pivot elimination was hand-checked: C_j=U_j+b_j-(a_j/a_p)b_p has an exact uniform comparator using fresh response rows. Its planted masks e_j-(a_j/a_p)e_p become iid uniform conditional on the pivot error e_p being a unit, after fresh uniform ratios are discarded. Thus dense cancellation destroys the narrow-mask goal. The noise-unit probability estimate is B's separate claim, not certified here. This hand-check did not consume an experiment reservation.

Next: audit B's short partial-syndrome mechanism for actual short-relation algorithms, full comparator rank and source-noise cost; audit C's concrete known-ideal chain for distribution, advice and noise hypotheses. No new experiment is authorized yet. Missing hypotheses for a positive result remain an efficient source simulator or direction-correct established hardness theorem in a compatible parameter range.

## 5. Reproducibility and resource record

Code, input, prelaunch estimate/command, stdout and stderr are under experiments/endpoint-control-v1.*. The single authorized LIGHT process enumerated 448044 primitive states, used exact integers/Fraction, and recorded 0.1856662500067614 seconds and 12288 KiB peak RSS. SIGALRM=60 seconds and RLIMIT_AS=536870912 bytes were installed before enumeration. Exit status was zero and stderr is empty. Resource wall timing is diagnostic and can differ from tool-reported wall time. No random seeds, numerical tolerances, packages, solvers, background jobs, external sessions or second experiment were used.

Code SHA256: 5be23f4dac47b35003d545a3f59690cbe81e3242006ae24f355ddb39b3211384.

Original stdout SHA256: 509d8d64132e11f2e98d20a5c45a903fcea8a4e4a98c6ddc7c2cfcb67f50ce4a.

All new mathematical claims and this audit verdict remain PROVISIONAL pending nonauthor reviews. No experiment establishes asymptotic hardness.
