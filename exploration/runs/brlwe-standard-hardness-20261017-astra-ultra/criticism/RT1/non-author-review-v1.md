# RT1 full independent NONAUTHOR review of frozen root tower artifacts, v1

Role and scope: this is a review of the exact root-authored `endpoint-test-v1.md` and `product-transfer-v1.md`, with complete source/control/resource inspection. It does not accept a claim, close the native goal, or certify standard hardness. The constructive moment and weighted-trace lemmas in separate RT1 files are new RT1-authored PROVISIONAL material and are not covered by this nonauthor verdict. No blind reports or other referee reports were read.

## Frozen inputs, probability space, and verdict

All eight root tower-lift files were read completely and their SHA-256 values matched `author-input-freeze-v1.json`. The supplied same-J theorem-only interface was read solely to unpack the conditional sampler and resource promises; its proof was not independently reaudited here. The live manifest was inspected solely for the original cap. No clock reset, external session, service, network lookup, or unauthorized experiment occurred.

Fix R⊂S a power-two cyclotomic tower with degrees n,m=tn and relative coefficient projection Π=Tr/t. The root statements quantify over supplied integral ideals F_j, their ordinary bases, their norm bounds, and a supplied eligible product cover. These objects, any metadata, and sampler randomness are independent of each fresh binary secret used upstream. The ideal reference probability space is the product of all full infinite centered coefficient Gaussian laws D_(F_j,W_j). The implementation law has joint TV distance at most eta from that reference; alternatively every fresh conditional kernel, on every possible preceding history, has TV error eta_j with eta≤Σeta_j. All zero, off-ideal, norm-tail, and implementation failures remain in the ambient law.

Review conclusion: the two projection endpoints, the stated P1/P2 probability-radius bound, and the P3 factor-count norm budget withstand this reconstruction. No mathematical counterexample to those frozen assertions was found. The source-family coverage and useful-radius gaps remain open. Any assertion of a successful polynomial-time approximation procedure needs a numerical error schedule making P1 strictly below one by at least an inverse-polynomial margin; the bound as written can be vacuous. No actual-output lower bound follows from a large displayed radius certificate.

## Claim-by-claim reconstruction

### E1. Integral normalized trace and both prime-lift endpoints

With z=ζ_(2m), S=⊕_(j=0)^(t-1) R z^j. The t relative embeddings send z to z times the t-th roots of unity, so Tr(z^j)=0 for 1≤j<t and Tr(1)=t. Thus Π selects the j=0 coefficient exactly, is integral R-linear, and has coefficient operator norm one.

For odd prime I⊂R, the tower is unramified above I. In IS=∏_(a=1)^r J_a, the residue degrees are equal because L/K is Galois, and t=rf. Consequently N_S(J_a)=M^f, N_S(IS)=M^t, and their normalized determinants are M^(1/(nr)) and M^(1/n), respectively. The degree and norm conventions in the root text are consistent.

Modulo I, S/IS≅∏_a k_a, with k_a/k=R/I finite fields of degree f. The reduced normalized trace is t^(-1)Σ_a Tr_(k_a/k); t is invertible in odd residue characteristic. If r≥2, the image of J_1 in the CRT algebra is zero only in coordinate one, so a free second coordinate and surjectivity of finite-field trace give Π(J_1)+I=R. Constants from I already lie in Π(J_1), hence Π(J_1)=R. If r=1, J_1=IS, and direct R-module decomposition gives Π(J_1)=I. No determinant gain remains in the latter endpoint.

The uniform quotient statement works for every integer q≥2, including q sharing factors with M, provided the targets are exactly the stated modules: the induced surjection J_1/qJ_1→Π(J_1)/qΠ(J_1) sends uniform to uniform because all finite fibers have equal size. The targets are R/qR when r≥2 and I/qI when r=1. One must not silently identify I/qI with its image in R/qR when q is not coprime to M.

For a full centered Gaussian, every x∈J has positive weight. The fiber-sum formula is exactly the pushforward law. In the split case every y∈R has a nonempty fiber, hence positive projected mass, including outside I. This rules out equality with D_(I,s). It does not by itself quantify rejection success or exclude an approximate transfer. The explicit n=2,m=8,p=17 witness is correct: 3^8=-1 mod17, 3^4=13, and Π(z-3)=-3∉(17,i-13). The listed roots 3,5,12,14 are the four lifts over that contraction.

### E2. Eventual tower norm floor

For odd p, exactly one of p-1,p+1 has 2-adic valuation one and the other has c≥2. After the threshold a≥c+1, repeated squaring gives ord_(2^a)(p)=2^(a-c), so dividing by field degree 2^(a-1) yields 2^(1-c). The finite order table matches this formula and is correctly labelled a control, not its proof. For p=5, c=2 and residue degree n/2 for every power-two degree n≥2, giving normalized prime norm √5>2. These fixed-prime examples are easy families and do not support a hardness barrier beyond the named tower construction.

### P0. Containment and short rotation directions

The product sample Z=∏X_j lies in ∏F_j⊂IS, so Y=Π(Z)∈I. This is exact integral arithmetic. It remains true for zero samples. An off-ideal implemented sample must trigger the declared failure output; it must not be used under ideal arithmetic promises.

For an integral coefficient lattice F of determinant D, Minkowski applied to a slightly enlarged centered coefficient cube gives a nonzero f with ||f||≤√m D^(1/m). A limiting argument is justified by finiteness of lattice points in each bounded region. Eligibility D≤2^(rho m), rho<1, gives ||f||<2√m. Its m rotations z^k f are lattice elements of the same norm. They span the real coefficient space because multiplication by nonzero f is an invertible field-linear map and the power basis spans. Therefore every proper real linear subspace H omits at least one such rotation v.

### P1a. Subspace anti-concentration

For distinct x,y∈F∩H, the sets x+Zv and y+Zv are disjoint: equality would put a nonzero multiple of v in H. For each x, completing the square yields

    Σ_k ρ_W(x+kv)/ρ_W(x)
      = exp(π〈x,v〉²/(W²||v||²)) ρ_(W/||v||)(Z+〈x,v〉/||v||²).

The prefactor is at least one. Scalar Poisson summation and the triangle inequality give

    ρ_a(Z+u) ≥ a[1-2Σ_(h≥1)e^(-π a²h²)] ≥ a/2  (a≥1).

The last numerical bound is safely slack: at a=1 the error is less than 0.087. Summing the disjoint lines gives

    Pr_D(F,W)[X∈H] ≤ 2||v||/W < 4√m/W.

Root's W≥4√m is sufficient. At the minimum width this displayed estimate is vacuous, which affects guaranteed success but not validity. The argument uses the full Gaussian normalizer; truncating the law without TV accounting would invalidate the line-sum proof.

### P1b. Filtration and nonzero product projection

Under the exact product reference law, reveal X_1,...,X_(r-1). Union-bound the events X_j=0 for j<r with the subspace H={0}. On the remaining histories A=∏_(j<r)X_j is nonzero because S is a domain. Multiplication M_A is invertible on the real extension of L, while Π has rank n, so ker(ΠM_A) is a proper real linear subspace. The final X_r remains an independent fresh D_(F_r,W_r) conditional on these exact revealed values. Apply P1a once to that history-dependent subspace and then average. This proves Σ_j 4√m/W_j; it does not multiply marginal events or reuse a success-conditioned source law. For r=1 set A=1.

The finite counterexample in `preserved-failures-v1.md` shows why the final subspace step is essential: three nonzero inputs can give Y=0. It is retained by this proof.

### P1c. Gaussian norm tail and joint TV

For every real vector u, completing the square in the Gaussian sum gives

    E exp(〈u,X〉)=exp(W²||u||²/(4π))·ρ_W(F-W²u/(2π))/ρ_W(F).

Poisson summation gives translated-theta maximality ρ_W(F-c)≤ρ_W(F): all Fourier coefficients of the Gaussian are nonnegative and phases have real part at most one. Thus every coefficient is subgaussian, without assuming independent coefficients. Chernoff gives Pr[|X_i|>WL]≤2e^(-πL²), and a coefficient union bound gives Pr[||X||>W√m L]≤2m e^(-πL²). Summing over j gives the root tail term.

Map the full tuple by exact membership tests, product, projection, zero/tail tests, and the declared failure map. TV contracts under this common measurable map. The actual failure probability is at most the ideal failure probability plus eta. A per-history conditional-kernel bound implies the joint bound by successive coupling/hybrid replacement; purely marginal error statements do not. The simple correlated-bit regression in the preserved failures file rejects that shortcut.

The audit protocol's cached-prefix example is not a counterexample to this argument. Its 21/2000=0.0105 event exceeds (1/10)^2=0.01 after sequential support selection, despite the later 21/221<1/10 conditional incidence. The rejected step there is multiplication of uncharged marginal/prefix estimates. Here a union bound and one fresh exact conditional law are used, and every implementation deviation is charged at the full-joint level. No latent cache variable or selected prefix is treated as newly independent.

### P2. Radius and approximation direction

Negacyclic convolution satisfies ||xy||≤√m||x||||y||: each output coordinate is an inner product with a signed rotation, and summing m coordinate squares proves the inequality. Iterating r-1 multiplications, inserting ||X_j||≤W_j√m L, and using ||Π||=1 gives exactly

    ||Y||≤m^(r-1/2) L^r ∏W_j.

For any nonzero y∈I, (y)⊂I implies |N_K/Q(y)|≥M. Arithmetic-geometric mean over all canonical embeddings and coefficient/canonical Parseval yield |N(y)|^(1/n)≤||y||_coeff. Hence λ_1(I)≥M^(1/n), and B/M^(1/n) is a valid upper approximation certificate on successful outputs. It is not a claim that this certificate is sharp, nor that all actual outputs are long.

### P3. Factor-count budget and edge cases

Integral-ideal containment reverses index: ∏D_j=N_S(∏F_j)≥N_S(IS)=M^t. Since each D_j≤2^(rho m) and m=tn, M^(1/n)≤2^(rho r). For rho>0 the logarithmic lower bound on r follows. If rho=0, every F_j=S and M≤1; thus I=R and no growing norm family occurs. Noncoprime or repeated factors do not escape multiplicativity. Nor does taking a larger tower change the right-hand normalized budget.

The root statement appropriately distinguishes a poor certificate from an output lower bound. The new RT1 moment lemma strictly improves the bound but its W floor still forces a superpolynomial certificate when M^(1/n)=n^alpha. Neither calculation proves a general impossibility theorem.

## Complete source and bit-complexity audit

The conditional source is the supplied same-J theorem in dimension m, separately instantiated for each F_j. It requires more than norm eligibility: a supplied odd prime q≡1 mod 2m, gcd(q,D_j)=1, q≥mσ_m, pointwise executable recovery success with the same metadata, its exact fresh binary target and error width, numerical gap G, the entire finite parameter/circuit construction, and per-sampler output/TV costs. A premise at dimension n, a different modulus, average-over-ideals success, or classical black-box access to recovery is not interchangeable.

The coefficient width delivered by that interface is

    W_j=mq/(√2 d0_j),
    d0_j=delta_j ell²/(64 m k chi_j),
    W_j=32√2 m² k q chi_j/(delta_j ell²).

For polynomial-value W_j one needs polynomial-value q,k,chi_j,delta_j^(-1) relative to the desired asymptotic parameter, as well as the other source bounds. Merely polynomial bit-length of W_j or q is insufficient for a polynomial approximation radius. The theorem-only interface does not automatically make these promises true for arbitrary input ideals or all fresh metadata.

With independent finite executions, joint TV is at most the sum of sampler errors min(1,epsilon_j+2√p_j+E_m). Fresh preparations and coins are required. Off-ideal outputs are already absent for the provided same-J sampler because its fallbacks output zero, but a more general approximate oracle needs the declared membership rejection. A numerical success budget must be checked; for example eta≤1/4, W_j≥16r√m, and 2mr exp(-πL²)≤1/4 give root P1 at most 3/4. This is only an illustrative sufficient schedule, not an assertion that the upstream source realizes it.

One actual sample per factor uses at most 2Σ_j Q*_j coherent executions of the supplied recovery code. Total source cost must additionally sum the actual finite setup, compiled decoder/call-slot gates, working registers, measurements, and ordinary arithmetic. Infinite exact samples are a mathematical reference, not finite executable code. If a success probability s>0 is used to repeat, every attempt and its full source calls must be charged; either expected attempts 1/s or an explicitly bounded repetition schedule is needed.

Given finite coefficient outputs of bit bounds b_j, sequential negacyclic multiplication needs polynomially many integer operations in r,m,Σb_j: coefficients of a product have bit length at most Σb_j+(r-1)ceil(log_2 m)+O(r). Product-ideal containment can be verified by successive ideal multiplication, using at most m² generator products at each stage followed by HNF reduction; an exponential enumeration of all m^r basis products is unnecessary. Integral full-rank ideals and ideal closure can be checked by rational/integer arithmetic. Actual costs include basis bit lengths and determinant computations. If t or r makes m or the input list superpolynomial in n, polynomiality in n does not follow from polynomiality in the full represented input.

The failure output should be an explicit tagged failure or zero; conditioning the returned distribution on success would require a new law and normalizer. The present solver claim needs no target Gaussian law.

## Source-code, output, and resource receipts

The root control is an exact finite endpoint check with config n=2,m=8,p=17,q=3. It checks the explicit wrong-ideal witness, exhaustively maps 3^8 ordinary J/qJ representatives, and obtains nine equally weighted quotient outcomes of count 729 each. Its two weighted finite supports each have 385 points, with the complete projected laws and normalizers retained. The outside-I masses 180/241 and 2765/7921 are exactly the TVs to their own success-conditioned restrictions. These finite masses are not full-DGS outside-mass theorems. The count 2·3^8+3^8=19683 is within its 20000 cap.

The order loop enumerates seven fixed odd primes at eleven conductor exponents; it is not part of the support counter but is tiny, deterministic, and bounded. No random seed or Monte Carlo uncertainty is involved. The script uses exact integers and Fractions for its stated finite laws, imposes a 128MiB address-space limit, and has no unbounded descendants. Root receipts show timeout30s, exit0, wall0.05s, maxRSS12288KiB, and empty stderr. I inspected these receipts without rerunning the root control.

RT1's separately reserved control RT1-MOMENT-FV1 ran once under the same 30s/128MiB limits. It enumerated exactly 13122 triples at n=2,m=4,r=3, checked ideal containment, retained zero branches, computed full exact finite projected laws, checked conditional covariance-trace identities, and attained the moment bound in both finite schedules. Receipts show exit0, wall0.15s, maxRSS12288KiB, empty stderr. Full source and all results are preserved, not just this summary. It supplies finite regression evidence for algebra and probability bookkeeping, not an infinite-Gaussian proof or hardness assertion.

## Dependency disposition and remaining obligations

Reviewed root dependencies: E1 integral trace/prime/uniform/Gaussian endpoints; E2 tower norm floor; P0 containment/short rotations; P1a subspace bound; P1b fresh filtration; P1c tail and joint TV; P2 convolution/approximation; P3 norm budget. Each has a reconstructed argument above. They remain subject to coordinator reconciliation and any required independent/blind gates; this report does not mark them ACCEPTED.

Unresolved: an effective eligible factor cover for an appropriate arbitrary worst-case ideal family; a nonvacuous finite source/parameter schedule across that family and dimension change; and a polynomial approximation radius. The supplied easy finite examples establish none of these. RT1's moment improvement and complementary weighted multiplier are new provisional lemmas requiring fresh review. The weighted multiplier explicitly adds a short-vector computation in an ineligible complementary ideal when normalized target norm grows. No standard hardness reduction has been established.
