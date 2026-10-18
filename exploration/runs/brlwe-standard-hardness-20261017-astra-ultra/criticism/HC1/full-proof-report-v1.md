# HC1 independent full-proof review: frozen same-J composition v1

Verdict: FAVORABLE for the exact conditional composition, subject to its four stated mathematical interfaces. No mathematical defect requiring rejection of these frozen composition bytes was found. This is a nonauthor review, not acceptance, certification of every upstream theorem, or an arbitrary-ideal standard-hardness claim. The separate source/parameter/complexity report records the constructive dispatcher cap and the limits of the finite witness.

Exact reviewed theorem SHA256: `96b88a725cc5dc4f8c943275d3b8788fdb9e6ac108c72fe62b383af9614e5e62`.
Exact reviewed proof SHA256: `4821d28fa205d893576b496df7f328f94a4ba111f6d634fd4b338edfea8c522d`.
Exact author freeze-manifest SHA256: `ff917b85c43f1c88dcfc324981fdc8319462ee1bd66ec7cc6cb9207ff76315b3`.
All other exact input hashes are in `input-hashes-v1.json`. Complete theorem, proof, specification, and interface statements were read. Relevant full upstream mathematical statements/proofs/specifications and the original finite parameter code/output were read; no other referee report or status ledger was used as a premise.

## 1. Claim and complete endpoint laws

Fix the same supplied ordinary integral ideal basis J, its norm D, and the supplied prime q throughout. The exact recovery experiment samples uniform ring multipliers, one uniform coefficient-binary secret shared by all k samples, and independent coefficient integer Gaussian errors. Optional J metadata is identical in both worlds. Recovery is actual-secret success, not success at finding any consistent secret. The wrapper privately generates its own S and E and tests the returned answer against that S.

The finite input group is h Z^n/(qJ^-1), h=1/(DP). Its cardinality is the quotient of covolumes, q^n D^(n-1) P^n. Because J^-1/R has order D coprime to q, inclusion induces R/qR ≅ J^-1/qJ^-1; the numerator map v/D ↦ v D^-1 mod q realizes the inverse. These are exact algebraic maps, without rounding a fractional multiplier into a different law.

The exact planted law is k iid rounded coefficient-width-w_B continuous Gaussians modulo qJ^-1. The exact comparator is k iid uniform elements of that same finite group. Before elementary quotient caps, B's kernel has planted error Delta_B and exactly uniform output on the comparator. Its translation-equivariant scalar fallback is included in that statement. After the wrapper's target-noise approximation and elementary caps, the full endpoint bounds are respectively

    Delta_B + kn nu + eta_cap,
    kn nu + eta_cap.

Here Delta_B already contains another kn nu term from the bridge scalar approximations. The comparator is therefore approximate after capping. The advantage triangle inequality charges both endpoints, giving exactly the three kn nu terms and two eta_cap terms in (G). This charge concerns the complete implemented test, including its fresh secret/error variables and equality event. It establishes a property of one fixed A_J; it is not repeated Q_* times in C8.

All infinite Gaussian laws retain their theta normalizers. A's completion proof retains the expectation of its theta ratio in the denominator. B compares normalized shifted scalar Gaussians and uses one full law before reducing modulo the quotient. Neither zeros, scalar fallbacks, malformed recovery outputs, nor cap failures are conditioned away. There is no missing zero-probability residue conditioning in this composition: the comparator is sampled as a complete finite quotient law.

## 2. A and B substitutions

A's short basis is a proof-only existence witness. D^(1/n)<2 gives operator norm below 2n^2, so tau_2=2n^2 is valid without computing that basis. With t_A=2n^2 ell, s=sqrt(2) ell^2 and L_A=ell,

    2 t_A s sqrt(kn) L_A
      =4 sqrt(2) n^2 sqrt(kn) ell^4 <= sigma.

The actual theta argument is 3ell^2/4. Poisson summation gives D_(Z,t_A)(0)<=1/t_A, and hence the entropy term is bounded by exp(-(1-rho)n log2+1/(2n ell)), exactly as stated. Source tails and completion loss are charged only in the planted bound; the comparator target identity is exact before implementation errors.

For B, ell>=2 and log(8n/epsilon_B)<=(ell^2+ell+2)log2<=pi ell^4. Thus r_B=ell^2 meets the smoothing lower bound and s^2=w_B^2+r_B^2. Its exact-ceiling scalar kernel, rather than a silently modified kernel, is used. The scalar trial upper bound L_+ bounds both bridge and target-noise trials. U_all=kn(1+2L_+) counts quotient draws and both kinds of scalar proposals. Conditional cap failure per elementary draw is at most 2^-B_cap, so the full wrapper changes by at most eta_cap on every valid input. This bound applies separately to both endpoints and does not assume cap events are independent after adaptive control.

## 3. C8 substitutions and adaptive probability

The coefficient width ell^2 becomes canonical width sqrt(n)ell^2 by the similarity of the embeddings, including its Jacobian. Thus the exact spherical finite GP law is identical to C8's law. A_J has bounded behavior on every valid input, including wrong orientations and off-promise physical queries.

The choice order is noncircular: zeta, then kappa and Q_*, then epsilon_0,a,chi,v0,d0. The product v0 d0=h0 was already fixed when kappa was chosen. The deterministic Up convention is retained, with chi>=a. The specialization d0=delta ell^2/(64nk chi) is rational. Its uniqueness inequality follows from q>=n sigma and D^(1/n)<2. The error p=(n/2)e^-kappa+zeta<=17zeta/16 is in [0,1].

C8's single counter across both orientations charges conditional errors tau_c=zeta/[16(c+1)^2]. At equal coupled histories the next kernel bound holds conditional on that whole history. First disagreement is then charged once, after which no favorable future conditioning is invoked. The fixed two-normalizer allowance uses kQ_* physical sample components, whereas the number of A_J/Rec calls is Q_*. These are distinct counts. The exact continuous proxy has a Haar endpoint; the discrete physical kernel need only be uniformly close to that proxy. The proof never infers an exactly Haar physical endpoint.

The upstream causal reference walk is a legitimate analysis object: corrected decisions depend on the present state/current coins; its conditional progress estimate is stated before future samples. Its coupling to the actual walk is through the first bad event. This supports the composition's use of C8; a proof conditioned on every future comparison succeeding would not support it.

## 4. Geometry and coherent interface

For x≠0 in J^-1, |N(x)|D>=1. The proof's weaker consequence lambda_1(qJ^-1)>=q/(sqrt(n)D^(1/n)) already gives lambda_1(L)>4d for d=d0/sqrt(n). Every coefficient Euclidean error <=d has canonical infinity error <=d0. Rational target Bv/H is exact; it is not a rounded substitute near a promise boundary.

The trace identity <x,y>_coeff=Tr(x conjugate(y))/n and the codifferent R/n imply the coefficient dual

    (qJ^-1)^* = conjugate(J)/q.

The canonical dual differs by the expected factor n. Applying F with coefficient radius d therefore yields coefficient width sqrt(n)/(sqrt(2)d)=n/(sqrt(2)d0) on Gamma. Scaling by q and conjugating is a bijection Gamma→J and maps the normalized discrete Gaussian term by term to width nq/(sqrt(2)d0). This checks both the exponent and full normalizer. Every fallback maps to zero in J.

Pointwise randomized decoder correctness is sufficient for the coherent replacement: on a reference superposition, squared bad amplitude averages its per-target failure, so the norm error is <=2sqrt(p). No common good random tape is required. The full circuit retains coins, dispatch state, and work until reversal. One forward and one inverse evaluation use at most 2Q_* recovery-code executions. Access to a classical remote recovery service would fail this premise.

F's normalized conditional coset law, input reference truncation, periodization cross terms and measured classical labels are retained. The composition explicitly uses a common purification with a copy of the measured label in an environment, rather than treating a measured mixture as a pure state. The input off-promise tail is paid in the reference truncation, not again in p. Finite phase-resource failures are part of their complete resource states before any adaptive entangled channel is applied. This avoids postselecting successful future branches.

The finite ledger gives epsilon+2sqrt(p)+2sqrt(tau_n)+2sqrt(2(tau_n+c_n))+tau_n, capped at one. The elementary finite preparation/phase allowances fit epsilon by W's definition. For u fresh repetitions, product coupling gives joint TV at most u times the single-sample bound and 2uQ_* code executions. The output claim is ordinary classical samples, not a prepared pure Gaussian state.

## 5. Exact finite falsification and limitations

The reserved HC1-FV1 job used exact fractions, with no theta truncation: 625 common-kernel contraction cases, 15,625 two-stage adaptive-kernel cases, a full 16-outcome capped-uniform law, original CP-1, and six one-slot dispatcher branches. It passed; complete code/input/command/stdout/stderr/resources are preserved. A capped sampler on three points produced (6,5,5)/16, TV1/24 from uniform, below its failure mass1/16. This falsifies any assertion that the capped comparator remains exactly uniform. Equal marginals concealed unequal joint laws in 92 grid cases, so the test suite does not license marginal-to-joint inference.

Original CP-1 was reproduced with its full prior normalizer10/11. The posterior masses are A_b=21/2000, C_b=1/20 and D=879/1000. Initial incidences are 1/10,121/2000,21/2000; selected mass21/2000 exceeds (1/10)^2 while the later posterior21/221 remains below1/10. Cached-prefix support restriction and renormalization, not a mere failure of local independence, cause that invalid product bound. This composition uses conditional total-variation sums and a causal filtration, which CP-1 does not falsify; it never exposes latent cache status or multiplies selected posterior probabilities.

These finite controls are falsification checks, not proofs of infinite Gaussian estimates or executions of BDD/Rec/quantum sampling. No Gaussian truncation was substituted for an infinite law. The four upstream mathematical interfaces remain explicit dependencies; this review does not promote their external certification status. The supplied q and pointwise recovery promise remain fixed, and the missing transformation from arbitrary ideals into the eligible family remains outside the conclusion.
