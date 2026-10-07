# RF1 full nonauthor review of theorem-only-v2

**Disposition: PASS for the frozen finite inequality F, implementation inequality I, and conditional asymptotic implication A, with the source premise and setup scope stated below. No counterexample satisfying the frozen theorem's hypotheses was found.** This is one bounded, complementary review by the same model family as the author and coordinator. It is not statistical independence, formal verification, a source-hardness proof, or a replacement for the coordinator's blind-review and delivery gates.

The broad dimension range is a conditional entropy range. It includes false source premises: the d=1 Base_2 assumption is rejected by an elementary polynomial-time enumeration test, independently reconstructed in `source-d1-limitation-v1.md`. An arbitrary uniformly computable d also need not have polynomial-time setup. Neither fact refutes F or A, because the source hypothesis is separately assumed for each d and the reduction never computes d. Efficient generation is verified here for the two explicit formulas floor(sqrt(n)/ell^4) and floor(n/(64ell)); their source hardness remains assumed.

## 1. Exact scope and frozen inputs

I am RF1, a fresh nonauthor referee. I read the mathematical-proof-audit skill and both required references, saved the complete assignment, followed `launcher-run.json` to its exact cap status file, and checked the stated service deadlines. I created no goal or agent, read no RB1 blind files, sent no proof context to RB1, and edited no author files. All research outputs are confined to RF1. No installations, remote computation, services, commits, publishing or messages to people occurred. No content-policy interruption occurred. The primary-PDF tools worked; a text search for “Poisson” in Peikert returned no match, and the relevant Gaussian definitions and dependent-summand experiment were read directly instead.

The exact mathematical packet is:

| Input | SHA-256 |
|---|---|
| workers/A1/theorem-only-v2.md | bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124 |
| workers/A1/proof-v1.md | 198c36bce9a73b87f2e1f5cf644d7e96b13cda063922f1ab10b0b2ee60114042 |
| workers/A1/supplement-v1.md | 71752406e81e327b5c47d0d118ea9bc6aa0f87566d23345daf290a7b8322410a |
| coordinator/rectangular-completion-v1.md | d66a1ea3e1c61990c77380de60c39b00a3097ab111407aedc610cfbe34c70163 |
| coordinator/source-and-parameters-v1.md | 131e6a3feec87010007a30ddc1e37bdec44687648120bfe1e8c5187e6e779f50 |

All five match the assignment. `input-hashes-v1.json` froze these and the auxiliary A1/root inputs before review. `historical-input-hashes-v1.json` froze the historical evidence before its substantive review. Hashing an indexed historical file does not assert that every page of it was read: complete evidence was read for applicable controls; nonapplicable mechanisms are classified explicitly below. The final integrity record checks the exact inputs again. The first partial was saved around 22:03 UTC although its header mistakenly said 22:07; this was openly corrected in partial-v2 without changing the original.

The precedence order is the frozen theorem-only-v2 statement, its expressly identified proof and supplement, the root supporting derivations, then historical evidence as regression fixtures. Earlier author status labels and historical certificates were not used as proof evidence.

## 2. Frozen experiment, variables and resource model

For every power-of-two n>=2, odd prime q=1 mod 2n, 0<=d<=n, and m in {1,2}, the theorem is a statement about the coefficient ring R=F_q[X]/(X^n+1). A source challenger chooses one uniform d-subset T of the CRT roots. Conditional on T, it draws U_1,U_2 independently uniformly in I_T, including zeros; all integer mask coefficients F_i,j have independent D_ell law and are jointly independent of T,U_1,U_2. It publishes exactly A=(U_1+F_1,U_2+F_2) modulo q. Its comparator is exactly two independent uniform ring elements. There is one challenge pair and no source oracle.

The target's full law is the product of uniform binary S, independent uniform multipliers a_1,...,a_m, all mn independent D_sigma_m integer errors, and the solver's independent random tape. The transcript is X=((a_i,a_i S+E_i))_i. Success is equality to the actual sampled S. Invalid outputs fail. The finite theorem includes every such solver Q; efficiency is used only for the computational consequence.

The source test B_m samples its own independent S,E, calls Q once, and compares Q's output to that S. It knows the challenge pair, public parameters, its own S,E and Q's output. Q sees only X and its own tape. Neither algorithm receives T,U,F,G,H, the secret quotient, a noise decomposition, or a conditional sampler. For m=1 the entire second source element is ignored; for m=2 each supplied element is used once. Local generation of responses supplies no new source multipliers.

For the analysis, condition only the used m integer masks on the box event B_F={|F_i,j|<=ell^2 for every used i,j}. This event has positive probability and depends only on the masks. The latent source information C can retain T,U and the chosen integer mask lifts, so the multiplication matrix has an unambiguous bounded integer representation even when different lifts reduce to the same ring element. All these are latent source variables, never algorithm inputs.

Conditional on C, draw an exact integer Gaussian H from the displayed positive-definite B(C) kernel, and draw a single independent G with iid D_ell coordinates. Draw S independently of the entire source/G/H construction. For the comparison experiment, E has the independent product D_sigma_m law. The full measure is

    mu(dC) K_C(dH) P_G(dG) P_S(dS) P_E(dE).

Define Y=S+G modulo q. The full product kernel, not pairwise independence, gives (C,H) independent of (S,Y). H may reveal C almost completely and may correlate its output coordinates; this does not change that independence.

## 3. A1-WITNESS and leakage cardinality: PASS

The first attempted falsification was a latent dependence attack. H=S, H=-G and C=G can make superficially correct marginal comparisons fail after retaining S or conditioning on C. All violate an explicit factor in the actual law above. More subtly, the historical F,S independent uniform F3 with E=-F-S has independent pairwise marginals but joint TV 2/3 from the product law. It also violates the actual premise.

Under the stated law, N=(F_iG+H_i)_i is jointly independent of S together with C. Thus appending S to TV((C,N),(C,E)) preserves that TV exactly. The deterministic map (s,C,e)->(s,((U_i+F_i,(U_i+F_i)s+e_i))_i) then contracts TV. On the completed side its response is U_iS+F_iY+H_i. This establishes the full witness/transcript comparison; no posterior of S is silently changed.

Only after this comparison, in the completed world alone, reveal W=(C,H,Y,pi_J(S)). Since U_iJ=0, W determines U_iS and hence the transcript. Guessing from the public transcript is therefore at most guessing from W. Neither H nor Y is appended through the preceding TV comparison. That order is essential: retaining H or a correlated Y on both sides would be a stronger, generally false claim.

For a fixed positive-mass k=(C,H), the (S,Y) law is unchanged. Writing p(s,y)=Pr[S=s,Y=y], one has

    sum_y sum_z max_{s:pi_J(s)=z} p(s,y)
      <= |R/J| sum_y max_s p(s,y).

Empty fibers and zero-mass y contribute zero; there is no conditional denominator on a zero branch. The quotient need not be uniform, mixed, flat, independent of Y or efficiently computable. A single quotient determines every U_iS, so it is charged once. Averaging over k gives L P_guess(S|Y), or E|R/J| times that common baseline when the varying-cardinality version is used. Guessing probability is 1-Lipschitz in joint witness/transcript TV because each fixed decoder's success is an event and taking a supremum preserves the bound.

The new `exact-search-v1.py` tested 11,664 full-product models over F3. C has probabilities 1/3,2/3; F(C) ranges over all nine maps; H|C ranges over all 36 pairs of denominator-two distributions; G and E range over all 36 pairs of denominator-two distributions; S is uniform {0,1}; J=R and U=0. Every distribution is exactly normalized. Appending S preserves TV, mapping contracts it, and the recovery inequality passes. There are 648 nontrivial right sides below one and 72 equality cases. This includes source-dependent H kernels; it does not just test independent H marginals.

The new leakage search exhausts 64,152 cases: all 792 denominator-five joint laws on four secrets/two observations and all 81 maps to three labels. It includes nonuniform priors, empty fibers, zero-probability observations and rare observations. All pass. In a separate hidden-map example with independent rare source and observation branches of probability 1/100, baseline guessing is 103/400, leakage guessing is 10199/20000, and the expected-cardinality bound is 10403/20000. These bounded searches support the algebra; they do not replace it.

## 4. A1-BIT: PASS

For a uniform bit and a symmetric unimodal integer mass p, the optimal success is (1/2)sum_y max(p(y),p(y-1)). At y<=0 the maximum is p(y), while at y>=1 it is p(y-1). Each half-line sum is (1+p(0))/2, and the leading 1/2 gives exactly (1+p(0))/2. The proof's wording about these half sums is consistent with this factor.

For n independent bits and independent noise coordinates, the complete joint mass is 2^-n product_j p(y_j-s_j). Maximizing over the Cartesian secret cube factorizes pointwise; the subsequent nonnegative integer sum factorizes by Tonelli. This is a fixed product law, with no adaptive or selected-stage multiplication. Coefficient reduction modulo q is deterministic postprocessing of Y over Z^n and can only decrease guessing. The binary vectors remain distinct in R since q>=2. Therefore the wrapped inequality, rather than an unjustified wrapped equality, is correct.

The copied author controls were rerun in RF1 with unchanged code bytes. For triangular p=(1,2,3,2,1)/9, the one-bit unwrapped success is 2/3, modulo 3 it is 1/2, and modulo 5 it is 11/18. Exact dimensions 2 and 3 give the corresponding products. The elementary identity Z_ell=ell sum_k exp(-pi ell^2 k^2)>=ell gives D_ell(0)<=1/ell with the stated convention.

## 5. A1-RECT and full independent target errors: PASS

Let M have p=mn rows and n columns. For B=sigma^2 I_p-tau^2 MM^t>0 and Theta=tau^2 I_n-tau^4 M^tM/sigma^2>0, multiplication verifies

    Theta^-1=tau^-2 I_n+M^t B^-1 M,
    Theta^-1 (tau^2 M^t/sigma^2)=M^t B^-1,
    B^-1-(tau^2 M/sigma^2)Theta^-1(tau^2 M^t/sigma^2)=sigma^-2 I_p.

These identities include rectangular matrices and their output nullspace. Completing the square consequently has exactly the stated constant ||z||^2/sigma^2. For every integer z and g, h=z-Mg is an integer vector; this is where integer M matters. Summing the independent G,H mass over all g produces the Gaussian target weight times a translated theta sum.

The Fourier transform of the positive-definite Gaussian and Poisson summation give r_z=1+sum_{k!=0}exp(-pi k^tTheta k)exp(-2pi i<k,mu_z>). Absolute convergence justifies the operations. Pairing k and -k shows the expression is real, and |r_z-1|<=delta. The actual normalized output is P(z)r_z/E_P[r], not P(z)r_z alone. For delta<1 the denominator is at least 1-delta, and

    TV(P,Q)=E_P|r_z-E_P r|/(2 E_P r)<=delta/(1-delta).

TV<=1 covers delta>=1 and also caps a ratio above one. The theorem's piecewise guard is correct. Normalizers are positive because the Gaussian quadratic forms are positive definite. Conditional source retention follows by averaging the conditional TV for every C, and wrapping contracts it. There is no need to retain the realized H on the target side.

The parameter matrices are exponent parameters, not exact discrete covariance matrices. The Gaussian convention agrees with Peikert's Section 2.4. His Theorem 3.1 uses a shifted second draw whose law depends on the first, so it is not imported as the current independent-summand theorem. The current square/Poisson calculation supplies its own proof. [Peikert primary PDF, Sections 2.4–3](https://sites.cc.gatech.edu/fac/cpeikert/pubs/pargauss.pdf).

For negacyclic multiplication M_i, each signed shift is orthogonal, hence ||M_i||<=sum_j|F_i,j|<=nb. Vertical stacking gives ||M||^2<=mn^2b^2. With sigma_m=2 sqrt(m) n b tau, B>=3sigma_m^2 I/4 and Theta>=3tau^2 I/4. This remains true for zero/rank-deficient masks. Here b=ell^2>0, so no zero-width branch is invoked. Comparing each positive dual summand gives delta<=(1+kappa(3tau^2/4))^n-1. The scalar geometric estimate follows from j^2>=1+3(j-1); this is not a probability-product shortcut.

For m=2, B has off-diagonal blocks -tau^2 M_1M_2^t and their transpose. They are required because one G appears in both responses. The final comparison is to the entire D_sigma_2^(2n) product law, which really has independent samples and coefficients. Independent separate completions would generally fail the joint law. No H sampler is executed, so no H_seq normalizer, approximation or matrix-precision cost can be smuggled into the implementation.

New rectangular control: M=[[1,1],[1,0],[0,1]], tau^2=4, sigma^2=16; B=[[8,-4,-4],[-4,12,0],[-4,0,12]] has eigenvalues 4,12,16, and Theta=[[2,-1],[-1,2]] has eigenvalues 1,3. All three matrix identities and 3,125 completed-square substitutions pass in exact fractions. Qualified binary64 sums give delta approximately 0.011204695537690093 and TV approximately 0.002104312365688408, below 0.011331663375750976. The explicit normalizer E_P[r] is approximately 1.000013949442395, agreeing with Z_G Z_H/(Z_sigma sqrt(det Theta)); four direct independent-summand masses match the normalized formula.

The numerical record distinguishes arithmetic error from truncation. Conservative analytic omitted unnormalized sums are at most 3.68e-27 for the G box, 9.20e-26 for H, 3.57e-20 for the target output box, and 2.78e-48 for the dual box. Floating exp/cos are not directed-rounding intervals. The numerical result is supporting evidence; the exact algebra and analytic uniform bound carry the proof.

## 6. A1-FINITE, implementation I and sample accounting: PASS

The used-mask box event has complement probability at most mn exp(-pi ell^2)/(pi ell), capped at one. Indeed monotonicity bounds the positive integer tail by the integral from b=ell^2; the Gaussian integral inequality and Z_ell>=ell give the displayed one-coordinate tail. Conditioning on this event leaves T,U and independent S,G unchanged, and the used mask coordinates become an independent product of truncated Gaussians. The full source/witness/transcript law changes by at most that event probability. This is paid once by subtraction; success need not be independent of the bad-mask event.

For the bounded source, A1-WITNESS, A1-BIT and A1-RECT give planted recovery at most q^d((1+D_ell(0))/2)^n+eta_N. At the uniform source endpoint, the test's complete witness/transcript distribution is exactly the target, so acceptance is epsilon_m. At the planted endpoint it is at most that guessing bound plus delta_F,m. Taking the absolute endpoint difference proves F. There is no signed-advantage transfer, active-unit loss, extractor, second source hybrid or amplification step.

Boundary d=0 gives the zero ideal I=0 and quotient cardinality one. Boundary d=n gives quotient cardinality q^n and may yield a trivial bound, which is valid; there is no claimed statistical lossiness in every finite parameter regime. Uniform ideal zero coordinates are always allowed. New exact F2 zero-ideal tests enumerate every deterministic decoder on the reachable transcripts: 8 decoders for m=1 and 128 for m=2. All endpoint inequalities hold; planted guessing is 1/2 and optimal uniform-target success is 3/4 or 7/8. The old varying dual-number quotient control is recomputed from primitive variables: public endpoint TV is 9/32 and exact planted guessing is 17/32, below the expected-cardinality charge 3/4. These are positive controls for the abstract proof, not instances claiming an odd-prime asymptotic hardness assumption.

The copied author dual-number test also reproduces planted guessing 3/8 and 7/16, target success 11/16 and 55/64, and source gaps 5/16 and 27/64 for m=1,2. Residual verification accepts both worlds with probability one; equality to the sampled witness has the claimed gap. Thus exact-witness checking is doing real work.

For I, approximating the local sampler changes each source endpoint by at most xi_alg; approximating the planted source changes one endpoint by at most xi_source; target witness/transcript approximation changes success by at most xi_target. The absolute-value triangle inequality gives exactly xi_source+2xi_alg+xi_target. The full local sampler law is required to remain independent of the challenge; independent coordinates or marginals alone would not suffice. A nonexact uniform comparator would require another term, as the proof says.

The runtime includes one Q invocation plus n fair secret bits, mn independent error draws, m multiplications and additions, and canonical equality checking. No source sample, CRT support, G or H is generated by B_m. Naive ring multiplication costs polynomial time in n and log q. The theorem correctly labels its displayed bound as overhead, so omitting T_Q from that overhead does not omit the single solver call.

For the finite sampler, sigma_m^2=4mn^2ell^6 is an integer and B_E=2mn^2ell^3>=n sigma_m. The full truncation tail is at most m exp(-pi n^2)/pi. The finite table has N_E=2B_E+1=O(n^2ell^3) atoms for fixed m. Setting xi=2^-n and approximating each raw weight to absolute error xi/(8pN_E), keeping the zero weight exactly one, gives L1 raw-weight error at most xi/(8p), with both normalizers at least one. Expanding the normalization difference gives TV at most that same raw L1 bound; no normalizer error is omitted.

Rounding down the first N_E-1 normalized probabilities to denominator 2^r and assigning the remainder to the last atom gives a valid exact dyadic distribution with TV at most (N_E-1)2^-r. The stated r suffices. Independent product coupling across p=mn coordinates costs at most xi/4 for the two table errors, plus the tail, which is less than xi/2 for n>=2,m<=2. Thus xi_alg<xi. New exact checks exhaust 384 finite rounding tables and reproduce positivity, exact normalization and the TV bound.

The raw exponents are at most pi m n^2. Precision O(n+log(pN_E)) plus O(log n) guard bits is enough for the displayed error; pi and exp can be evaluated by elementary rational interval algorithms in polynomial time at these arguments and precision. Exact integer division computes the final rational-to-dyadic floors. Each draw uses exactly r bits and finite lookup; there is no unbounded rejection tail. This certifies existence of the bounded polynomial sampler, not a benchmark or an executed high-dimensional Gaussian implementation.

## 7. A1-PARAM and A1-ASYMPTOTIC: PASS in the conditional scope

I checked Xylouris Theorem 1.1 directly: for coprime positive a,M the least prime is bounded by C M^5.18 with effective C. Substitution a=1,M=2n^3 gives q<=C 2^5.18 n^15.54<=n^16 eventually, and q>=2n^3+1. Hence q=1 mod 2n, and q/sigma_m divided by n is at least n/(sqrt(m)ell^3), which tends to infinity. The claimed ratio q/sigma_m>=n eventually is correct. [Xylouris primary PDF, Theorem 1.1](https://www.impan.pl/shop/publication/transaction/download/product/83078).

This is a nonempty effective family. Deterministically enumerating progression candidates and testing divisibility through their square roots is polynomial in n because q is polynomially bounded in n; no practical bound is asserted. Primitive roots and the root list can likewise be enumerated with polynomially many modular operations. Common coefficient encodings have O(n log n) bits. B_m itself does not require roots. The parameter bounds and sampler accuracy are fixed before the solver or its inverse-polynomial success exponent.

For n a power of two, ell=log2 n exactly. In the broad d<=n/(64ell) range and q<=n^16,

    d log2 q<=n/4,
    log2(1+D_ell(0))<=1/(ell ln 2),
    q^d((1+D_ell(0))/2)^n<=2^(-3n/4+n/(ell ln 2)).

At ell>=6 this is at most 2^(-n/2). The smaller explicit d formula is eventually positive and within this range. Moreover n kappa(3ell^2/4)=exp(-Omega(ell^2)), so Delta_N has the same negligible order; eventually Delta_N<1/2 and eta_N<=2Delta_N. The source tail is exp(-Omega(ell^2)). Their sum and the finite sampler error are negligible independently of Q. Consequently a uniform PPT Q with nonnegligible exact recovery gives a uniform PPT B_m with nonnegligible source advantage, proving the conditional statement A.

An arbitrary uniformly computable d may require superpolynomial setup. The frozen theorem does not charge computing d to B_m and does not infer efficient setup from that adjective. The two explicit growing formulas can be computed with integer arithmetic in polynomial time. Each requires its own Base_2 indistinguishability premise. The d=1 attack in the separate note shows why the broad range must not be advertised as a family of supported hardness assumptions. No claimed implication between different source dimensions is present.

I do not certify a derivation of either growing-dimensional Base_2 premise from ordinary RLWE, DSPR, Order-LWE, worst-case lattices, or the cited HLBDD literature. Those are OPEN source-hardness/provenance questions, not unproved dependencies hidden inside the explicitly conditional mathematical implication. I did not independently reread all motivating cryptographic literature and make no final bibliographic-equivalence claim. The direct coefficient/canonical norm relation used only as context follows from the orthogonality of the power-of-two evaluation transform; it supplies no source-hardness transfer.

## 8. Historical regression dispositions

PASS below means the current exact proof handles or explicitly excludes the recorded mechanism; REJECT refers to the historical shortcut or a separately stated false source premise, not the current theorem. No earlier certificate is imported.

| Registry controls | Reproduction and current disposition |
|---|---|
| R02: C=G, H=E-FG | Exact hand substitution gives N=E while G becomes deterministic conditional C. REJECT the weakened conditional-independence rule. Current C independent of G and fixed conditional G law exclude it; PASS. |
| R03, R04, R05; C03-HC5; PAIRWISE-SE-F3; SE-CORRELATION-F3 | Exact shared-G/common-K F3 TV=2/3; all pair marginals of F,S,E are product but full TV=2/3; correlated-secret target TV=2/9. For the Gaussian sign control, odd q makes nonzero r and -r distinct, giving guessing 1-W(0)/2 with the sign tape and 1/2 without it. Current target and noise comparison specify the full product law; PASS. |
| NC1-v1; C03-HC1 | M=0,tau=1/3,sigma=1 has true TV=0 but delta>82/63>1, so the old ratio is negative. REJECT old guardless formula; current piecewise bound returns one; PASS. |
| C03-HC2: H_seq | M=(1,1)^t,tau=1,sigma^2=3 gives parity-dependent second normalizers. Exact Poisson odd terms make Z_(3/2)(0)-Z_(3/2)(1/2)>0; numerical reproduction gives 0.0440089584. REJECT exact H_seq=D_B. Current H is proof-only exact D_B; PASS. Positive scalar complements alone would also miss a negative stacked eigenvalue; current full B guard excludes that. |
| C03-HC3 | Discrete covariance need not be B/(2pi); at small scalar width variance is asymptotic to 2exp(-pi/t^2). No covariance identity is used. Current proof uses exact quadratic mass and normalizers; PASS. |
| C03-HC4 | The exact rational signed inverse has entries -1/20 despite positive Fourier ratios; reproduced. The archived wrapped-Gaussian residue inequalities force t2>=7.11e-5 while t2<2e-7, so fixed narrow exact deconvolution fails. Current statement supplies a positive D_B law, sufficient PSD/smoothing hypotheses and an approximation loss; it does not assert arbitrary exact wrapped deconvolution; PASS. |
| R08; C02-LATENT-PUBLIC; PUBLIC-ENCODED-F | F5 control independently gives latent TV=1/2 and public TV=0. Reverse projection lower bounds remain rejected. Current latent reveal is solely a guessing upper bound; whether public projection can preserve encoded F is irrelevant to that direction; PASS. |
| R11; C03-HC6 success/bad-error correlation | The two-atom model success=bad-error makes multiplication by good-error probability false. Current proof pays a union/TV subtraction once. The half-zero/half-identity model remains a rejection of sometimes-lossy-to-negligible-average reasoning; current source loss bounds average guessing directly; PASS. |
| R12 exact witness vs residual | Author-code rerun and new zero-ideal controls show residual checking can accept every transcript while exact sampled-witness success differs. Current B_m compares to its own S; PASS. |
| R13; C03-HC4 Renyi orientation | Positive-event change of measure does not preserve a signed difference. Current proof uses a single absolute acceptance gap with no Renyi transfer; PASS by explicit nonuse. |
| R14; N02-DUAL-NUMBER | Zero ideal multipliers included throughout; new primitive enumeration reproduces TV 9/32, and planted guessing 17/32 respects the cardinality bound. No active-unit conditioning, rank defect or eta_iso is invoked; PASS. |
| R15; C03-HC5 common K; C03-HC7 separate Y | Common K gives three diagonal points instead of nine independent points in F3, TV 2/3. Current source genuinely supplies the two multipliers; correlated completion handles the shared G only inside the proof. It does not convert common K to independent ideal points, expand a source, or reveal several separately noised Y values; PASS. |
| R18/CP-1; C03-HC6 | Independently recomputed normalizer 10/11, posterior A_b=21/2000,C_b=1/20,D=879/1000; incidences 1/10,121/2000,21/2000. Selected event 21/2000>1/100, later 21/221<1/10. Support restriction and renormalization, including latent cached information, invalidate the old product. Current fixed-coordinate products have full unconditioned product laws and no adaptive filtration/cache branch; PASS. |
| R06, R07 | Entropy-only extraction and field-kernel-to-Boolean-fiber shortcuts remain rejected. Current quotient lemma uses only cardinality, allowing arbitrary fibers; noisy-bit loss is computed directly. Exhaustive new leakage controls cover the relevant replacement; PASS. |
| R01; R09; R10; C01-ATT | Binomial-support decoders, strict norm/injection thresholds, Lucas occupancy, and residual boxes filling all centered residues remain valid warnings for their old claims. No structured-support pseudorandomness, strict norm uniqueness, full quotient occupancy or residual-box distinguisher is asserted here. Inapplicable to the proof, retained as source-premise limitations. |
| R16; R17; C02-CHAR | Statistical source pseudorandomness, posterior transport, tower packing, independent-matrix moments, symmetry-orbit hardness, QCSD masking and fixed-character-to-pseudorandomness arguments are absent. Base_2 indistinguishability is computational and expressly assumed. No verdict about those retired methods is reused. |
| W2-SUBGROUP-BOUNDARY; W2-CONSTANT-COMPARISON | No all-subgroup coverage bound or comparative attack-runtime improvement appears in the frozen theorem. Their n=8,d=2 coverage-one boundary and optimized-constant qualification are inapplicable to this proof, retained for source-security work. |
| UNIFORM-APPROX-COLLAPSE | No exact-uniform entropy no-go is extended to approximate preservation. The source-test uniform endpoint is exactly the target by its explicit sampler. Inapplicable to the present argument. |
| S0-dependency | No historical AN/NC1 acceptance is inherited. A1-FINITE depends on the newly checked witness, bit and rectangular lemmas; A1-PARAM additionally depends on the fresh prime check; PASS for this explicit graph. |
| N03-PV-CONDITIONING; N03-SCAL-POSTERIOR | No active-PV search transfer or prior law of ratios after conditioning on public data is used. The current only selected event is the mask box, whose conditional law is written explicitly. Their decision-cancellation and fixed-ratio posterior controls are inapplicable to the new chain. |

## 9. Claim graph and terminal review scope

| Exact claim | RF1 disposition | Dependencies and limitations |
|---|---|---|
| A1-WITNESS, proof-v1 Sections 1–3 | PASS | Full product-kernel premise and retained S,C TV; no extractor or public latent lower bound. |
| A1-BIT, proof-v1 Section 4 | PASS | Uniform Cartesian binary secret, independent integer noise; wrapped upper bound only. |
| A1-RECT, proof-v1 Sections 5–6 and root NC-RECT v1 | PASS | Integer rectangular M, exact D_B, positivity and piecewise guard; no implemented H sampler claim. |
| A1-FINITE / theorem F | PASS | The preceding three claims, the exact two-point source definition and one mask-tail loss. Exactly m=1 or 2. |
| Implementation I / supplement table sampler | PASS | Full challenge-independent sampler law; exact uniform comparator; bounded polynomial implementation at the stated widths. |
| A1-PARAM / supplement large-d range | PASS | Fresh Xylouris import; statistical bounds hold over the full stated range. Efficient setup verified for the two explicit growing formulas, not inferred for arbitrary uniformly computable d. |
| A1-ASYMPTOTIC / theorem A | PASS, conditional | Every selected d requires its own explicit Base_2 computational assumption. Uniform PPT B_m follows from uniform PPT Q without computing d. |
| Base_2 computational hardness for either explicit growing d | OPEN / ASSUMED | Not proved or certified by this review. No standard-assumption or worst-case derivation is supplied. |
| Base_2 computational hardness at d=1 on the specified polynomial-q family | REJECT | Independent nq-enumeration test; frozen limitation note. This is not a rejection of the conditional theorem. |
| More than two target samples, target decision hardness, exact efficient H sampling | OPEN / OUT OF CLAIM | No such consequence is asserted or inferred. |

The mathematical review is complete for the exact packet above. No repair to F, I or A is requested. The coordinator must keep the source assumptions, the broad-d setup qualification, the explicit sample count and the proof-only status of H visible in any final result. Blind reconciliation and clean final-artifact verification remain coordinator responsibilities.

## 10. Commands, evidence and reproducibility

The following four experiments were run sequentially, never concurrently, in allocated slot 2. Each used `timeout 120s`; all exited zero and finished below two seconds. No longer experiment allocation was used.

    timeout 120s python3 exploration/runs/brlwe-goal-routes-20260907-astra-ultra/criticism/RF1/exact-search-v1.py
    timeout 120s python3 exploration/runs/brlwe-goal-routes-20260907-astra-ultra/criticism/RF1/rectangular-control-v1.py
    timeout 120s python3 exploration/runs/brlwe-goal-routes-20260907-astra-ultra/criticism/RF1/author-controls-copy-v1.py
    timeout 120s python3 exploration/runs/brlwe-goal-routes-20260907-astra-ultra/criticism/RF1/interface-controls-v1.py

The author-code copy has SHA-256 09fa4d72a73705561cdb08ee68929b250d5418b4bcc200006523c6b15a16353e, exactly matching the frozen author script. Its output was written only to RF1/exact_controls_v1.json. The three new scripts refuse to overwrite their JSON outputs; reproduction should use a fresh RF1 subdirectory with copied scripts, rather than deleting original evidence. The copied author script lacks that guard, so likewise run it only in a fresh directory. Complete commands, exit dispositions, elapsed times and scope qualifications are preserved in the JSON outputs and `commands-and-results-v1.json`.

| New artifact | SHA-256 |
|---|---|
| exact-search-v1.py | 6a20bb60a805806edb8afe4bbaacb741c9afd9d549d4fdaefe0d2243b37b8119 |
| exact-search-v1.json | 124e8fda394b7b42d0b9a911c0fdd4fbd08d2310dab6f5bfdb0fecbee376a9dd |
| rectangular-control-v1.py | e5e9ed0875c6fd2134d3eb26c035a9cbe532693438ca2e5be105edbc1621ddc9 |
| rectangular-control-v1.json | 28f7b0cf2d2da66e5c43472f72b5a7283e98009799b9a0508cd57cfc4a75462f |
| interface-controls-v1.py | 2fee329796cadff12fa72056e684c5fd7d057f835c8383951f04ec20f65d07fb |
| interface-controls-v1.json | 49e325521afb279bfcba31f480ff05a7f24f0fa21ac3b5b9013aa9fd2add1bf6 |

`artifact-manifest-v1.json` freezes this report, complete assignment, partials, source notes, all code/results, source limitation and final integrity evidence. No statistical independence of reviewers or unrestricted conclusion from a finite search is claimed.
