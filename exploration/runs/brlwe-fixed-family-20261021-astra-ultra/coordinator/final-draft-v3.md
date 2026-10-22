# Fixed-family binary RLWE: bounded investigation report

Draft v3 frozen for delivery audit, 2026-10-21T21:53:54.004670+00:00. All mathematical candidate gates are reconciled; final delivery/operations audits and runtime/usage/cleanup receipts are still pending. Exact theorem statements and acceptance records control mathematical scope.

## Results and separate statuses

| Obligation | Result |
|---|---|
| Fixed-family decision reduction (FF) | **OPEN.** No polynomial-time reduction with one target ring/modulus/noise family fixed before every polynomial sample bound and inverse-polynomial advantage was established. |
| Source diagnostic (SV) | **Substantive reviewed algorithmic classification at the actual inherited DD radius.** Several ordinary-basis source regimes are proved classically decodable. No new FF-delivered radius exists in this run. |
| Established source hardness | **NOT ESTABLISHED.** There is no reviewed compatible map from an independently established hard problem at these endpoints. Unclassified inputs are not declared hard. |
| Protected investigation/challenge | The cooperative 210-minute investigation was completed. The fresh nonauthor challenge leaves material routes open and rejects scientific exhaustion. |
| Bounded package | Review and delivery are being completed within the original five-hour cap. Report completion is not mathematical achievement. |
| Native goal | **ACTIVE and unresolved.** It must not be marked complete, paused or blocked merely because this cap or delivery ends. |

The run began at 2026-10-21 17:48:10.636448 UTC (19:48:10 Berlin). Its protected period and discovery window ended at21:18:10 UTC. Consolidation starts22:18:10; workers/experiments stop22:33:10; final checkpoint22:43:10. Graceful shutdown is scheduled22:47:05.636448, scheduled kill22:48:05.636448, hard cap22:48:10.636448 UTC. Those final dates/times are22 October00:18–00:48 in Berlin. The external cap bounds runtime; it does not certify productive investigation or theorem truth. No successor, extension, commit, push or publication is authorized by this report.

## What changed beyond FIXED-MAIN-v2

The accepted predecessor requires

    sigma0 >= 8 k0 n(n/2+2)/epsilon_*.

It therefore fixes resource exponents before choosing its target parameters. This run's objective reverses that quantifier order: first choose one target family, then quantify over all efficient distinguishers, all polynomial sample bounds and all inverse-polynomial advantages. Reduction costs, precision, auxiliary moduli and source approximation may depend on those resources; the target distribution may not. No better constant or remaining positive power of k0/epsilon_* resolves that difference.

New reviewed results include fixed-modulus Gaussian projection bounds and an adaptive identifying certificate; exact nonlinear transfer examples and an exponential-cost full-secret Gaussian construction; scoped obstructions to certain affine or compressed transformations; and direct source-decoding classifications substantially beyond scalar rounding. These are accepted auxiliary or diagnostic claims, not a renamed main reduction. The exact claims, proof versions, full/blind review bindings and dependencies are in claims.json, claim-dependencies.json and coordinator/acceptance-v1.json through acceptance-v7.json.

At the illustrative fixed target q(n)>=n^4 of polynomial value, sigma(n)=n^2, CRT-PROJ-v1 gives for h distinct evaluation roots

    TV(E_T, U) <= min(1, (1/2) q^(h/2) 3^n exp(-pi sigma^2 q^(-2h/n))).

For h below the least r_c with q^(2r_c)>n^n this is negligible for every polynomial batch count. A correct tuple at r_c roots identifies a binary secret. CERT-EXTRACT-v2 makes the adaptive, disjoint-bank finite-code argument explicit. Injectivity can be used through an unbounded inverse in an information-only comparison; it is not an efficient inversion algorithm. Efficient inversion, source comparison and sample-dependent completion are separate obligations. The distinct-prime norm-divisor argument still requires distinct primes and a common partition.

The constructive transfer work found exact finite n=2 kernels with all per-secret planted endpoints and the uniform comparator endpoint, including33-weight compact selectors and47-weight joint-rank tables. TWOSECRET gives an exact channel for two labels with unit difference. ENUM defines exact-Gaussian source and target laws and a full-secret statistical channel with explicit whole-batch TV bounds, but enumerates2^n secrets. Its planted tail/competitor loss and comparator beta loss are all charged, in addition to any finite-sampler error. Thus the explored affine failures do not imply general statistical impossibility. No scalable polynomial-size all-dimensional kernel was proved. Exact n=4 Farkas certificates exclude only their specified forward-rank, target-class and cyclic/reversal symmetrized models; they do not exclude other couplings, classes or full residual directions.

The reviewed negative statements preserve their hypotheses. GAUSS/WEIGHT/BOUNDED-AFFINE (the last for n>=4 a power of two) compare distributions retaining S and use a common S-independent correction pair; tail/no-wrap conditions are explicit where needed. They do not prove separation of hidden-secret mixtures or impossibility of every nonlinear transfer. FRAC-INFO is statistical recovery at sufficiently high polynomial sample count in its exact fractional-source experiment, assuming gcd(q,N(J))=1; it is not an efficient attack. The compressed-selector bound requires exact pointwise normalization, fresh randomness on every retry, bounded class size and output factoring through the accepted proposal/class. Retaining additional residual state falls outside that bound.

## Exact source significance

Use R=Z[X]/(X^n+1), n a power of two, and a nonzero integral ideal J supplied by an ordinary integer basis, with N(J)<=2^(rho n) for fixed0<=rho<1 and all inherited parameter guards. The available inherited endpoint is

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

The203 DD regression references retain exact IDs, source pointers and hashes, with scoped per-ID review dispositions. Local counterexamples and controls are indexed separately. CP-1 remains binding: a product of marginal success rates is not a conditional sequential-law proof. Bounded exact Fraction/integer controls check finite examples, conditional laws, normalization and negative cases; they do not prove infinite Gaussian laws or asymptotic claims. Floating solver outputs, failed code versions, UNKNOWN outcomes and independently reconstructed exact certificates remain distinguishable. See experiments/registry.json and experiments/evidence-index-v1.json; original worker/reviewer receipts preserve limits, exits, timing, RSS and precision.

## Open routes and concrete next tests

The fresh FRONTIER-CHALLENGE1 review proposed fourteen escape routes plus a precision-tuning correction. Root replies address each with evidence and resource estimates. Material routes remain open, so this package cannot honestly claim scientific exhaustion.

1. Specify a polynomially represented nonlinear channel K_eta with pointwise conditional planted and comparator laws and error eta. The target family stays fixed; eta and reduction cost may depend polynomially on sample count and inverse advantage. Test a genuinely new n=4 model after fixing its equations. Do not repeat the already excluded rank/symmetry systems. Estimated initial proof/interface work2–4 hours.
2. Prove an explicit computational source comparison for the selected or centered functional, including all synthetic advice, adaptive/off-promise calls and shared-secret correlations. A statistical guessing obstruction does not exclude a code-dependent reduction. Estimated initial work2–4 hours.
3. For source foundations, choose one independently established premise and write the exact effective map, oracle direction, distortion and radius before claiming hardness. Alternatively specify a finite menu of source algorithms and resource bounds and classify a remaining explicit family against that menu. Neither no attack found nor failure of every tested sufficient guard is hardness. Estimated initial audit3–6 hours for a hardness map,2–4 hours for a finite-menu classification.

These are unlaunched future tests, not authorization for a successor. The versioned evidence-linked programme remains within this output directory. It records useful alternatives without changing the repository-wide research map.

## Runtime and shutdown accounting

Runtime receipts preserve the actual launch argv, spawn returns, capacity failures and available child configuration metadata. Root explicitly requested service_tier=default; children inherit it because the child API has no tier field. The fast_mode serialization flag is not Fast selection. A conflicting priority label in the available model catalogue was disclosed; no tier change was requested. Configuration evidence is not backend billing telemetry.

The final usage receipt must report the actual native tokensUsed delta from this thread's zero baseline, not a weekly quota percentage. Final cleanup can report only observed local job/worker state and external cap metadata at observation time. It must not predict that a future graceful/hard kill has already happened. No aggregate memory-containment claim is made beyond recorded per-job limits.


Draft v3 status update 2026-10-21T21:56:11.821124+00:00: all28 accepted auxiliary/source claims have exact full/blind gate reconciliation. Operational audit found checkpoint cadence deviations (longest interval819.513seconds, greatest scheduled lateness251.527seconds); original actual timestamps are preserved. Final compliance and observed cleanup remain to be completed. Cached cap running state is a startup snapshot, not live cleanup evidence.
