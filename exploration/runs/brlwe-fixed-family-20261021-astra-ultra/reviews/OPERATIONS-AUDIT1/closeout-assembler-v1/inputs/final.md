# Fixed-family binary RLWE: bounded investigation report

Mathematical content follows the delivery-audited draft v4. Exact statements and acceptance records control scope. Final operational closeout is pending the scheduled checkpoints; this is not a declaration of scientific achievement or exhaustion.

| Obligation | Result |
|---|---|
| Fixed-family decision reduction | **OPEN.** No polynomial-time reduction with one target family fixed before arbitrary polynomial sample bounds and inverse-polynomial advantages was established. |
| Source diagnostic | **Substantive reviewed algorithmic classification at the inherited DD radius.** No new FF-delivered radius exists in this run. |
| Established source hardness | **NOT ESTABLISHED.** No reviewed compatible map from an independently established hard problem. |
| Protected investigation and challenge | **210-minute cooperative investigation completed.** Fresh challenge leaves material routes open; scientific exhaustion is rejected. |
| Bounded package | Final operational closeout pending within the original cap. |
| Native goal | **ACTIVE and unresolved.** No completion, pause or blocked status is justified by delivery or cap expiry. |

Activation: 2026-10-21 17:48:10.636448 UTC. Protected-period end/discovery cutoff: 21:18:10.636448. Consolidation: 22:18:10.636448; worker/experiment stop: 22:33:10.636448; final checkpoint: 22:43:10.636448. Scheduled graceful shutdown: 22:47:05.636448; scheduled kill: 22:48:05.636448; hard deadline: 22:48:10.636448 UTC. These are original deadlines, not observed shutdown events. No successor, extension, commit, push or publication.

## What changed beyond FIXED-MAIN-v2

The accepted predecessor requires

    sigma0 >= 8 k0 n(n/2+2)/epsilon_*.

It therefore fixes resource exponents before choosing its target parameters. This run's objective reverses that quantifier order: first choose one target family, then quantify over all efficient distinguishers, all polynomial sample bounds and all inverse-polynomial advantages. Reduction costs, precision, auxiliary moduli and source approximation may depend on those resources; the target distribution may not. No better constant or remaining positive power of k0/epsilon_* resolves that difference.

New reviewed results include fixed-modulus Gaussian projection bounds and an adaptive identifying certificate; exact nonlinear transfer examples and an exponential-cost full-secret Gaussian construction; scoped obstructions to certain affine or compressed transformations; and direct source-decoding classifications substantially beyond scalar rounding. These are accepted auxiliary or diagnostic claims, not a renamed main reduction. The exact claims, proof versions, full/blind review bindings and dependencies are in claims.json, claim-dependencies.json and coordinator/acceptance-v1.json through acceptance-v7.json.

At the illustrative fixed split-prime target q(n)=1 mod2n, q(n)>=n^4 of polynomial value, sigma(n)=n^2, CRT-PROJ-v1 gives for h distinct evaluation roots

    TV(E_T, U) <= min(1, (1/2) q^(h/2) 3^n exp(-pi sigma^2 q^(-2h/n))).

For h below the least r_c with q^(2r_c)>n^n this is negligible for every polynomial batch count. A correct tuple at r_c roots identifies a binary secret. CERT-EXTRACT-v2 makes the adaptive, disjoint-bank finite-code argument explicit. Injectivity can be used through an unbounded inverse in an information-only comparison; it is not an efficient inversion algorithm. Efficient inversion, source comparison and sample-dependent completion are separate obligations. The distinct-prime norm-divisor argument still requires distinct primes and a common partition.

The constructive transfer work found exact finite n=2 kernels with all per-secret planted endpoints and the uniform comparator endpoint, including33-weight compact selectors and47-weight joint-rank tables. TWOSECRET gives an exact channel for two labels with unit difference. ENUM defines exact-Gaussian source and target laws and a full-secret statistical channel with explicit whole-batch TV bounds, but enumerates2^n secrets. Its planted tail/competitor loss and comparator beta loss are all charged, in addition to any finite-sampler error. Thus the explored affine failures do not imply general statistical impossibility. No scalable polynomial-size all-dimensional kernel was proved. Exact n=4 Farkas certificates exclude only their specified forward-rank, target-class and cyclic/reversal symmetrized models; they do not exclude other couplings, classes or full residual directions.

The reviewed negative statements preserve their hypotheses. GAUSS/WEIGHT/BOUNDED-AFFINE (the last for n>=4 a power of two) compare distributions retaining S and use a common S-independent correction pair; tail/no-wrap conditions are explicit where needed. They do not prove separation of hidden-secret mixtures or impossibility of every nonlinear transfer. FRAC-INFO is statistical recovery at sufficiently high polynomial sample count in its exact fractional-source experiment, assuming gcd(q,N(J))=1; it is not an efficient attack. The compressed-selector bound requires exact pointwise normalization, fresh randomness on every retry, bounded class size and output factoring through the accepted proposal/class. Retaining additional residual state falls outside that bound.

## Exact source significance

Use R=Z[X]/(X^n+1), n>=2 a power of two, and a nonzero integral ideal J supplied by an ordinary integer basis, with N(J)<=2^(rho n) for fixed0<=rho<1 and all inherited parameter guards. The available inherited endpoint is

    r = epsilon_* ell^2 / (1024 n K chi Qmax),
    K = k0(Ncal+Ntest),   ell = ceil(log2(2nK)).

The inherited constraints imply r<1/(4sqrt(n)). Physical raw samples and all advantage losses remain charged. Here epsilon=epsilon_*/4 is a different historical symbol. These classifications use an ordinary integral basis of J and rational target T in J^-1 plus canonical-infinity error at most r; they do not assume a short generator is supplied.

| Reviewed source regime | Effective algorithm and boundary |
|---|---|
| Quotient exponent e with2er<1 | Compute e from exact normal forms/denominators, round eT and divide. A large e failing this sufficient guard is not hardness. |
| Polynomial numeric ideal index below2^n | Enumerate enough binary representatives for a collision; acquire a short member and multiply-round-divide. Polynomial bit length alone does not pay for this enumeration. |
| Prime ideals with polynomial numeric characteristic | Frobenius fixed-lattice collision gives a ternary member, even when norm is exponential and scalar rounding fails. The prime-ideal promise and numeric characteristic cost are explicit. |
| Small feasible symmetry or standard-subfield contraction | Compute signed fixed lattices and exact contraction index, then acquire a collision. The repaired2-primary definition is explicit. Weighted per-characteristic support extends the covered families, including growing total support and trivial full stabilizer cases. |
| Consecutive split-prime Fourier support of size t | Direct RS decoding succeeds when8p^2r^2<n-t+1 and r<1/2. Maximum spectral gap replaces n-t+1 for the GAP algorithm. LIST has separate interpolation, root-recursion and exact-lattice uniqueness guards and retains numeric-p work. |
| Fixed sparse member class | Enumerate at most(1+2nB)^h candidates and test ordinary-basis membership. For fixed h and polynomial numeric B, this is polynomial;4r^2hB^2<1 ensures decoding. |

The all-subfields theorem compares only the binary-collision contraction criterion: when feasible, the best arbitrary-subfield index and best standard-chain index differ by at most a square. It is not a comparison against every decoder.

DENSE-SPLIT gives eligible ideals with exponential norm and exponential feasible contraction index. The RS algorithm nevertheless decodes a nonempty exact inherited-radius family. ACTUAL-v3 chooses rational rho, uniform preliminary bounds and an explicitly charged enlarged chi to obtain1/2<pr<=1 while RS succeeds. This separates RS from scalar rounding and contraction enumeration at that endpoint; it does not assert the same separation at minimal chi=a. Failure of one algorithm's guard therefore cannot serve as a hardness argument.

SPARSE-ACQ supplies another useful separation. For J=(X^2-X-1)R, n>=4 a power of two,

    R/J ~= (Z/L_(n/2)Z)^2,
    e(J)=L_(n/2),   N(J)=L_(n/2)^2,

where L_j is the Lucas sequence. Both exponent and norm grow exponentially, yet a fixed h=3,B=1 ordinary-basis search acquires a decoder at the actual inherited radius. This family is eventually eligible for every fixed rational log2((1+sqrt(5))/2)<rho<1. For inverse-polynomial r, scalar exponent rounding eventually fails. This result concerns an entire effectively searchable sparse class, not just an isolated supplied easy ideal.

RS-BIT-v2 separately proves bounded primitive-root acquisition with failure at most eta and bit cost polynomial in n,log p,log(1/eta) and input lengths under a prime promise. The implementation omits the earlier trial-division check and full field scan. LIST's separate field-root enumeration is not accelerated by that lemma. At inverse-polynomial r the RS/GAP guard already forces polynomial-value p; this upgrade is not a new hardness result.

No compatible established-hardness transfer or new BDD-to-DGS composition was certified. Classical simulation of a wide DGS oracle does not reverse BDD-to-DGS into a classical BDD algorithm. Earlier short-complementary-multiplier and integral-map obstacles retain their exact scopes.

## Review, rejected arguments and finite evidence

New main auxiliary/source statements received nonauthor full proof/source/complexity review and fresh theorem-only reconstruction, with frozen assignments, allowed reads, complete reports and seals. Exact repair dependencies were reopened. All reviewers used the same Astra model, so their scrutiny is correlated and is not formal verification. Hash agreement identifies bytes, not truth.

Preserved defects include the ambiguous2-primary definition, rho=0 existence overstatement, ENUM's intermediate sign error, RS's epsilon versus epsilon_* substitution, nonatomic public side information, persistent hidden retry seeds, the old LIST bit-cost wording, arbitrary-n worst-case fair-bit sampling, the pair-shell count bound and unencoded real rejection bound M. Corrected versions do not erase their originals. A resource-repair packet accidentally exposed author verification labels; that exposure is recorded and its final strict gate assigned to a different fresh referee.

The203 DD regression references retain exact IDs, source pointers and hashes, with scoped per-ID review dispositions. Local counterexamples and controls are indexed separately. CP-1 remains binding: a product of marginal success rates is not a conditional sequential-law proof. Bounded exact Fraction/integer controls check finite examples, conditional laws, normalization and negative cases; they do not prove infinite Gaussian laws or asymptotic claims. Floating solver outputs, failed code versions, UNKNOWN outcomes and independently reconstructed exact certificates remain distinguishable. See experiments/registry.json and experiments/evidence-index-v1.json; original worker/reviewer receipts preserve declared limits, exits, precision and available timing/RSS measurements. BLIND-SV1-E01 did not measure peak RSS; its512MiB address-space limit is not a peak measurement.

## Open routes and concrete next tests

The fresh FRONTIER-CHALLENGE1 review proposed fourteen escape routes plus a precision-tuning correction. Root replies address each with evidence and resource estimates. Material routes remain open, so this package cannot honestly claim scientific exhaustion.

1. Specify a polynomially represented nonlinear channel K_eta with pointwise conditional planted and comparator laws and error eta. The target family stays fixed; eta and reduction cost may depend polynomially on sample count and inverse advantage. Test a genuinely new n=4 model after fixing its equations. Do not repeat the already excluded rank/symmetry systems. Estimated initial proof/interface work2–4 hours.
2. Prove an explicit computational source comparison for the selected or centered functional, including all synthetic advice, adaptive/off-promise calls and shared-secret correlations. A statistical guessing obstruction does not exclude a code-dependent reduction. Estimated initial work2–4 hours.
3. For source foundations, choose one independently established premise and write the exact effective map, oracle direction, distortion and radius before claiming hardness. Alternatively specify a finite menu of source algorithms and resource bounds and classify a remaining explicit family against that menu. Neither no attack found nor failure of every tested sufficient guard is hardness. Estimated initial audit3–6 hours for a hardness map,2–4 hours for a finite-menu classification.

These are unlaunched future tests, not authorization for a successor. The versioned evidence-linked programme remains within this output directory. It records useful alternatives without changing the repository-wide research map.

## Evidence and operational closeout

The [delivery audit](reviews/DELIVERY-AUDIT1/full-report-v1.md) passed the mathematical scope of draft v4 and resolved all six findings. The [operations audit](reviews/OPERATIONS-AUDIT1/report-v1.md) supports the recorded one-goal, clock, capacity and configuration history with explicit qualifications. All 448 artifacts in their final seals were verified in [final-audit-integrity-v1.json](coordinator/final-audit-integrity-v1.json).

The final original-evidence index is [evidence-index-v2.json](experiments/evidence-index-v2.json); v1 remains an earlier working snapshot. [Regression integrity v2](coordinator/regression-integrity-v2.json) verifies all 203 inherited references and 609 exact current review dispositions; 74 local controls remain separately scoped. An artifact count is not an experiment count. No historical theorem was promoted by importing its reference.

Root launch argv explicitly requests `service_tier=default`. The child API has no tier parameter; child settings inherit the root preference. Twelve actual local settings events across root and six children explicitly record Astra, ultra, default tier and approval policy never; remaining child records support inheritance. The available model catalogue's priority label was disclosed and no Fast selection was requested. The serialization flag `features.fast_mode=true` is not a Fast request. Configuration evidence is not backend billing telemetry. Runtime receipts preserve capacity failures and the maximum two active children.

[Operational deviations](coordinator/operational-deviations-v2.json) preserve actual checkpoint timestamps: the longest audited interval was 819.513 seconds and greatest scheduled lateness 251.527 seconds; some checkpoints were slightly early. The 210-minute obligation is evidenced by substantive work records, not OS productivity enforcement. BLIND-SV1-E01 did not measure peak RSS; its 512 MiB address-space cap is not a peak measurement. SYM-RANK-FV2's script elapsed time was 26.469 seconds and process wall time 26.69 seconds. Per-job limits do not establish aggregate memory containment or a complete independently observed concurrency history. Original failed and aborted experiments remain preserved.

The operations auditor's metadata extraction briefly displayed five short encrypted assignment prefixes. The lapse is disclosed in its sealed report; retained reviewer artifacts were sanitized and the extractor corrected. No decryption or plaintext secret access was reported. A previous resource-review packet exposed author verification labels; its repaired mathematical gate used a different fresh blind referee and different fresh full reviewer.

The live systemd query was denied by sandbox bus access and was not retried or bypassed. The cap file's running state is a startup snapshot. Local process observations therefore report only sandbox-visible state, completed tool sessions and worker completion evidence; they cannot certify a future external service kill. Final usage must be the native counter delta from this goal's zero baseline, not weekly quota or backend billing.

Final worker-stop, goal/usage, checkpoint and observed cleanup receipts will be bound here at the scheduled closeout. The unresolved mathematical goal must remain active. After terminal delivery or cap, stop scientific work; no automatic successor.
