# RF4 full-proof review of F-QFINITE v2

Verdict: **SUPPORTED, independent NONBLIND full-proof recommendation; not coordinator acceptance.** I found no counterexample to the frozen theorem and no unresolved load-bearing mathematical gap in its specified circuit model. This recommendation covers the standalone finite theorem and its exact same-J substitution, with the explicit hypotheses below. It does not establish standard-family hardness. Blind review and coordinator reconciliation are separate gates.

I independently read every line of theorem-only v2, algorithm v2 and proof v2, then the complete current C8 theorem-v8/algorithm-v2/proof-v9, the A-FRAC theorem/proof, B-GP theorem/proof-v2 and bounded-wrapper/ceiling addenda, and the F v1 integration/adapter packet. I did not read or contact BT17 and did not edit any frozen input. This review shares the team's model family and is not statistical independence evidence.

Exact main input hashes:

| Input in workers/F/finite-quantum-integration | SHA256 |
|---|---|
| finite-quantum-theorem-only-v2.md | ce7f5992b071f7d82e5e034a7dc323f69a85d0f4969afa0530603527bc7338e2 |
| finite-quantum-algorithm-v2.md | 1ea3e1ab1c297773d591a3bd983ff278f31cdafcd459acd29076a3867ede2545 |
| finite-quantum-proof-v2.md | 1430f62a7c670c682fef2cfc2b14d15f17c45e877fe3d598cc7a040cc1a69144 |
| integration-addendum-v2.md | 144ba40df83ab4c70f13d090c3a637a55f031fe2145dd90c06e887bf17dbd3cb |

The complete inspected-input/hash record and packet-manifest verification are in [artifact-consistency-v1.json](artifact-consistency-v1.json). The separate [source-parameter-complexity-report-v1.md](source-parameter-complexity-report-v1.md) records source versions, resources and effective parameter ranges.

## 1. Frozen statement and dependency graph

The standalone theorem has arbitrary integer dimension n>=2, rational nonsingular coefficient basis B, L=B Z^n, Gamma=L*, rational positive d², lambda_1(L)>4d, rational 0<epsilon<=1/16, and 0<=p<=1. Its decoder is supplied bounded code, pointwise correct with probability >=1-p on every rational target in the promised radius. It is total on all inputs and every coin string. An average-input guarantee or classical answer service is insufficient. Correct answers have exact finite lattice representations. All finite target widths are fixed before compiling the actual decoder C_dec.

All rows below are supported by this review; none is a grant of project acceptance.

| Claim | Dependencies | Frozen proof location | Finding |
|---|---|---|---|
| FQ-GEO | rational basis, det(A) nonzero integer | section1, lines7–15 | H and signed registers cover actual support and retained reference ball |
| FQ-ARITH | fixed exact-rational loops | section1, lines17–32 | specified fixed polynomial bit/gate allowance suffices |
| FQ-PREP | phase-average identity, fresh whole attempts | section2 | correct selected state, normalization and cap mixture |
| FQ-COSET | Poisson formula, FQ-GEO/PREP | section3 | uniform ideal conditional bound plus whole-channel finite comparison |
| FQ-TAIL | centered theta ratio | section4, lines92–100 | explicit tau_n bound without smoothing |
| FQ-PERIOD | positive amplitudes, separation, FQ-TAIL | section4, lines102–125 | exact norm/cross terms retained; uniform c_n bound |
| FQ-BDD | FQ-GEO/TAIL and actual retained-work adapter | section5 | one coherent decoder on finite promised reference support |
| FQ-QFT | Poisson identity, finite resource circuit | section6 | complete adaptive channel with bounded preprepared resources |
| FQ-ALIAS | FQ-GEO/PERIOD/TAIL | section7, lines157–159 | coordinate centering correct throughout retained dual ball |
| FQ-SUM | all previous rows, channel contractivity | section7, lines161–169 | every displayed error paid once; call count preserved |
| FQ-SAMEJ | ordinary coefficient dual identity | section7, line171 | output on the same supplied J, at the claimed width |
| FQ-INTEGRATION | accepted A/B-bounded/C8 premises and all above | integration-addendum-v2 | exact endpoint and pointwise-BDD substitution matches |

## 2. Geometry and normalization audit

A=bB is integral, so |det A|>=1 and every inverse entry is bounded by V. The actual chosen H gives cd>=2^(W+20)nU, hence r/U>=2^(W+20) for n>=2. Also lambda_1(H Gamma)>=H/||B||>=c/U>4n/d. The proof does not infer this from an unsupported dual transference claim. The representative y=A{A^-1 x} has norm at most sum_j||Ae_j||<=U. Both the finite actual u and every reference vector with ||Bu/H||<d have each coordinate strictly below C_u in magnitude; the extra ceil(cd) term is necessary and present. Modular two's-complement erasure is therefore compatible with the exact promised answer.

The scalar filter is a phase average over 2^p_g auxiliary strings, so its zero outcome amplitude is exactly 1-2m_x/2^p_g. Its successful state is the normalized dyadic vector, not a vector of unnormalized squared masses. At least r/2 interior integers have squared amplitude at least1/4 after rounding, giving probability >1/(32W), stronger than the used1/(512W). Each entire attempt is restarted with fresh x and auxiliary bits. For its actual probability P, first success at j has weight (1-P)^(j-1)P and the same conditional state for every j. Summation pays the cap-failure mixture rather than conditioning on later events. R_g yields failure <=exp(-8W)<=2^(-8W).

I independently checked the scalar tail integral, normalized-vector inequality and rounding constants. They give the claimed3n2^(-W) successful-product vector error and n2^(-8W) cap contribution.

For an ideal coset y, the law is P_y=rho_r(K+y)/rho_r(Z^n). The shifted theta normalizers lie in [(1-delta),(1+delta)] times r^n/det K with delta<=2^(-4W). Completing the square gives exactly the overlap written in proof-v2 lines74–76. Both normalizers occur in its denominator. Therefore ||psi_y-psi_0||<=2^(-W) uniformly for every coset, independently of P_y. The finite preparation is compared before conditioning; small marginal error is never used to claim a small rare-branch conditional error.

For precision of exposition, the pure vector in proof-v2 line84 is a purification/coherent record of the measured experiment. The actual measured state is sum_y P_y |y><y| tensor |psi_y><psi_y|. If one writes a purification literally, use an extra copied label: sum_y sqrt(P_y)|y>_Y|y>_E psi_y. Orthogonality gives the same stated norm bound, and discarding E,Y contracts distance. The line's retained-copy wording supports this reading; no estimate or theorem change is needed. Interpreting a measured classical register as an unmeasured pure state without the record would be incorrect.

## 3. Tail and periodization audit

Poisson summation makes rho_s(K)/rho_r(K)<=(s/r)^n for centered lattices when s>=r. Markov at parameter pi/(2r²) gives tau_n=2^(n/2)exp(-pi n) at radius sqrt(2n)r. It applies at both specified probability widths, without a smoothing assumption.

For F(v)=sum_(x in v+M)rho_a(x), direct pair grouping gives

    ||F||² = sum_(mu in M)rho_(sqrt(2)a)(mu)rho_(a/sqrt(2))(K+mu/2).

The diagonal contribution is Z. The centered-theta maximum bounds the full sum by Z(1+C_M), and unique retained representatives give ||G||²>=(1-tau_n)Z. Nonnegative amplitudes imply <G,F>>=||G||². Hence normalized overlap is at least sqrt((1-tau_n)/(1+C_M)); the squared vector distance is at most2(tau_n+C_M). This argument survives arbitrarily fine K and does not use an invalid L1/L2 deletion shortcut.

The shell bound is also adequate: separation lambda>=4sqrt(n)a gives exp(-8pi n j²), the packing count is at most(2j+3)^n<=5^(nj), and each shell is <=exp(-22nj). The geometric sum is below2^(-16n) for n>=2. Strict versus non-strict boundaries do not create collisions: the retained ball is open and separation exceeds twice its radius.

The new exact negative control [RF4-PERIOD-NEG1](failures-before-controls-v1.md) shows why small squared tail alone is insufficient. Its large cross-term ratio prevents it from satisfying the small-C premise. This tests the replacement invariant directly.

## 4. Coherent BDD, finite Fourier transform and aliases

On the retained input ball, lambda=Bv/H-Bu/H lies in L and is within d of the rational target. Thus v-HB^-1lambda=u exactly. Pointwise decoder correctness applies to every basis input in this support. Its fresh coherent coins and retained compute/copy/uncompute circuit give vector error2sqrt(p), including arbitrary external entanglement. Work and coins are not prematurely discarded. Off-promise mass is already paid in the state comparison to the ball; it is not charged a second time inside p.

The mathematical reference erasure is an isometry because at most one retained u lies above each v. Actual decoding is a finite channel on all signed bit strings; arbitrary off-promise behavior cannot enlarge the previous trace distance. The infinite comparison state is used only in a common Hilbert-space embedding, while both the actual input and retained reference fit the finite registers.

Poisson summation transforms F on Z_H^n to the normalized dual periodization with amplitude width1/a. Sign conventions only reflect a centered symmetric target. I checked the controlled-phase decomposition and both teleportation Kraus operators. A failure branch requires the double-angle correction, which terminates in available S/Z powers for the specified dyadic phases. The count M_ph dominates every possible correction chain.

Resource preparation has exact c0=1/2, |c1-exp(i theta)/2|<4/M, probability>=1/8 and normalized resource error<=32/M. Actual success probabilities need not coincide between phases. The resources are prepared independently before their data interaction; accepted states are independent of retry count. Tensor-product telescoping followed by the complete adaptive channel, with its measurements retained or averaged, gives eta_ph<=M_ph(32*2^(-p_ph)+2^(-8p_ph))<=2^(-W). No future-success product or arbitrary rotation is assumed.

Every retained dual vector has norm<n/d and integer coordinates B^T gamma strictly inside(-H/2,H/2). Hence coordinatewise centering is exact on the retained support. Tail aliases need no decoding guarantee; output periodization and tail charges handle them. Every actual output, including fallback0, is in Gamma.

## 5. Complete quantum error ledger

| Stage | Charge | Metric before final measurement |
|---|---:|---|
| finite successful product preparation | 3n2^(-W) | vector bound |
| scalar exhaustion mixture | n2^(-8W) | trace bound |
| ideal coset shift | 2^(-W) | purified vector bound |
| input restriction to ||x||<d | 2sqrt(tau_n) | vector bound, with slack |
| clean pointwise decoder | 2sqrt(p) | vector bound |
| input periodization | sqrt(2(tau_n+c_n)) | vector bound |
| complete finite QFT resource channel | eta_ph<=2^(-W) | trace bound, resource caps included |
| dual output periodization | sqrt(2(tau_n+c_n)) | vector bound |
| output conditioned-to-full Gaussian law | tau_n | total variation |

Pure-state vector bounds dominate trace distance; common channels contract it. The finite precision/preparation terms are <=(3n+3)2^(-W)<=5n2^(-W)<epsilon. The remaining sum is exactly2sqrt(p)+E_n. Capping by1 is valid. Independent full executions give product coupling error at most t times this quantity; for negligible total error one must choose epsilon and p negligible and take at most polynomial t. The theorem does not call a constant epsilon negligible.

## 6. Exact A/B-bounded/C8 substitution

The full capped planted law is within Delta_B+kn nu+eta_cap of A's exact planted completion. The full capped uniform comparator is within kn nu+eta_cap of the original exact binary-recovery target. Expanding Delta_B therefore gives THREE kn nu terms and TWO eta_cap terms. The stated delta gap retains all of them. It is the gap of one fixed implemented A_J, used as C8's actual oracle; it is not a per-query replacement and is not multiplied by Q_*.

The source in C8 is exactly k iid rounded coefficient-width w_B Gaussians modulo qJ^-1 against uniform F=hZ^n/(qJ^-1), h=1/(DP). The canonical parameter is w_C=sqrt(n)w_B. Same J, metadata, binary S and independent coefficient integer target errors are preserved. A's short basis/G/H remain proof-only. B's capped comparator is approximate; the expected-time exact comparator is not substituted.

C8 theorem-v8/algorithm-v2/proof-v9 gives a pointwise rational-target BDD guarantee and all-input finite caps, including the wrong orientation. Its causal global numerical counter and fixed two-normalizer charge are unchanged. The ordering zeta, then kappa/Q_*, then epsilon0/a/v0/d0 is noncircular. For zeta=2^(-4n-10), kappa>=log(8n/zeta) gives p_BDD<=17zeta/16<1. The new d0 uses that actual confidence choice.

Coefficient radius d=d0/sqrt(n) is covered by C8's canonical infinity promise. The supplied uniqueness bound gives lambda_1(qJ^-1)>4d. In the explicit parameter family d0=delta ell²/(64nk a) is rational, so d²=d0²/n is rational as required. The exact ordinary coefficient dual is conjugate(J)/q. Scaling by q and conjugating gives coefficient width nq/(sqrt(2)d0) on J itself; canonical width is larger by sqrt(n).

One clean coherent decoder traverses Q_* executable Rec blocks forward and Q_* inverse blocks. The call-slot dispatcher and retained work are part of the actual S_dec. A mere pathwise classical call bound would not justify this; the frozen algorithm supplies the needed construction.

## 7. Controls and unresolved scope

The reserved [RF4-FV1](RF4-FV1.stdout) job passed3,303 exact checks: normalized periodization/cross-term identities, unequal-success retry laws, entangled adaptive injection identities and complete imperfect-resource channels, and the ORIGINAL CP-1 prior/posterior enumeration. Exit0; wall/user0.12s; peak RSS11,264KiB; empty stderr; exact fractions/Q(i); no randomness. Code, input, command and resource report are preserved. These controls are new discriminating checks, not a rerun of the author's9,288 checks. They do not execute the enormous sampler, prove analytic Gaussian estimates, or certify arbitrary circuits. The injection test's terminal ideal phase is an algebraic reference, not an additional gate allowed by the theorem; finite dyadic termination was checked in the proof above.

Historical FQ-COND/NORM/PERIOD/RETRY/MODULUS, FQ-R1–R4, CP-1, full joint-law/actual-secret, bounded-comparator, complete rational-encoding, independent-confidence, physical-versus-proxy and rational-verifier controls remain active. Their application is recorded separately in [regression-review-v1.md](regression-review-v1.md). No failed approach has been erased or silently upgraded.

No unresolved mathematical obligation was found within the frozen standalone theorem. Practical circuit emission/execution was not attempted. The standard-family connection is unresolved: neither duality, conjugation nor the Fourier transform maps arbitrary ideals into N(J)<=2^(rho n). This favorable same-J review does not fill that boundary, supply a hard ideal distribution, or complete the binary standard-hardness foundation.
