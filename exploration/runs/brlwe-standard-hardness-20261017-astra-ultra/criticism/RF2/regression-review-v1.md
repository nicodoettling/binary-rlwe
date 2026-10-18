# RF2 per-ID regression dispositions

PROVISIONAL. Exact registry-entry bytes as parsed, JSON pointers, entry hashes and registry provenance are preserved in regression-review-v1.json. All51 inherited IDs are addressed;7 current-run controls and3 RF2 controls follow. CHECKED means the named mechanism is explicitly handled by the reviewed proof; it is not global certification. Historical counterexamples are retained. No experiment was rerun.

| ID | Disposition | Claim-specific reason |
|---|---|---|
| R01 | NONUSE | A/B use lattice Gaussians, not binomial ideal supports; the old structured-support attack remains valid and supplies no present hardness premise. |
| R02 | CHECKED | A fixes source-only z; G has D_(J,t) law and H is independent of S,G conditional on z. C=G or H=E-MG would violate this premise. |
| R03 | CHECKED | B proves full conditional-J product comparator using independent inputs and fresh local coins; uniform marginals alone are not used. |
| R04 | CHECKED | A samples the full product error vector independently of S and source. Its proof compares complete S/transcript laws after integrating H; Gaussian marginals alone are insufficient. |
| R05 | CHECKED | Fresh S and target E are jointly independent of each other and J/source; pairwise independence is not substituted for the full kernel. |
| R06 | CHECKED | A uses exact max-mass guessing and theta coset counting, not entropy-only extraction or uniformity of binary quotient images. |
| R07 | CHECKED | No field-rank-to-Boolean-fiber inference: A sums actual binary-secret posterior numerators and relaxes membership pointwise. |
| R08 | CHECKED | A reveals z,H,Y only to upper-bound recovery; neither A nor B constructs a public decoder from a latent precursor or reverses data processing. |
| R09 | NONUSE | No Lucas occupancy or binary injection threshold is used. C decoding uniqueness uses a separately stated strict radius and field norm; it is not this old occupancy claim. |
| R10 | SCOPE_LIMIT | No source hardness follows from no-wrap. Public short ideal bases may distinguish FG; A uses basis existence only analytically and B supplies no such basis. |
| R11 | CHECKED | A bounds average planted acceptance directly by additive bad-source probability plus eta+beta; no sometimes-lossy-to-negligible inference. |
| R12 | CHECKED | A wrapper checks equality with its own ACTUAL sampled S, not any verified preimage. C final verification follows unique rational-grid reconstruction. |
| R13 | NONUSE | No Renyi signed-gap transfer: A compares actual acceptances and B uses statistical distance/data processing. |
| R14 | CHECKED | No unit or active-coordinate conditioning. All Gaussian and uniform quotient points, including zero/nonunits, remain in each endpoint. |
| R15 | CHECKED | B uses k genuinely independent challenge samples conditional on J. A uses one common fresh S and independent target E; no sample expansion by rotations/common factors. |
| R16 | SCOPE_LIMIT | No claim that the binary planted target is statistically uniform; no posterior sampler or tower packing. FG and GP hardness remain unproved premises. |
| R17 | NONUSE | No independent-matrix moments, tiny-orbit randomization, QCSD characteristic-two transfer, or sparse-Fourier quantum speedup. |
| R18 | CHECKED_CP1 | Old .0105>.01 witness retained. A source-only conditioning and B original-J products are explicit; C adaptive kernels use a sum of conditional TV losses, never marginal products. |
| C03-HC1 | CHECKED | A eta is capped and uses Delta/(1-Delta) only when Delta<1; otherwise eta=1. The historical negative bound remains rejected. |
| C03-HC2 | CHECKED | A H is the full exact positive elliptical integer law, not a sequential scalar-complement construction. Its actual theta expectation denominator is retained. |
| C03-HC3 | CHECKED | Matrices are Gaussian quadratic-form width squares, not asserted exact discrete covariances. All comparisons use normalized masses/Poisson sums. |
| C03-HC4 | CHECKED | A defines a positive full-complement law and pays theta TV error; B uses positive sampling kernels. No signed Fourier inverse or arbitrary exact deconvolution. |
| C03-HC5 | CHECKED | Full source/target joints are stated. Shared G exists only in A proof and its correlated stacked effect is completed jointly; no common-K independence claim. |
| C03-HC6 | CHECKED_CP1 | Bad-source recovery can be one and is charged additively; no success/bad-event independence or selected-stage product. CP1 evidence in report section7. |
| C03-HC7 | CHECKED | A reveals only one shared Y=S+G; no multiple separately noised Y values or unexplained scale transfer. M is the full k-block stack. |
| C02-LATENT-PUBLIC | CHECKED | Latent reveal only increases guessing power. B forward channel contraction is used; reverse public/latent TV inference remains rejected. |
| C02-CHAR | CHECKED | B smoothing uses the entire nonzero dual theta sum. C independent smoothing proof sums all scaled-dual vectors, not a fixed-character estimate. |
| C01-ATT | SCOPE_LIMIT | No improvement to deterministic ATT or source-hardness claim is inferred. A/B conditional finite theorems remain valid even for easy source ideals. |
| CP-1 | CHECKED_CP1 | Exact original posterior10/11 and A_b21/2000,C_b1/20,D879/1000 retained; joint21/2000>1/100 rejects old rule. Fresh S/E, proof-only G/H and conditional guessing are checked explicitly. |
| NC1-v1 | CHECKED | A guarded eta handles Delta>=1 by one; negative-denominator version is never imported. |
| S0-dependency | CHECKED | No old AN/NC1 certification imported. A F3 depends explicitly on B; C finite OHCP and low-index standard-family hardness remain separately OPEN. |
| PUBLIC-ENCODED-F | CHECKED | No inverse projection lower bound. Public J is retained consistently; a short basis or unwrapped samples are excluded unless explicitly part of Gen. |
| W2-SUBGROUP-BOUNDARY | NONUSE | No all-subgroup coverage or asymptotic support-occupancy theorem. |
| UNIFORM-APPROX-COLLAPSE | CHECKED | B comparator is proved EXACT for the implemented finite kernel. Planted error is statistical; no entropy no-go is extended to approximate comparators. |
| SE-CORRELATION-F3 | CHECKED | A samples S and all errors independently of source and each other. Full product-kernel law excludes the correlated-secret/error witness. |
| W2-CONSTANT-COMPARISON | NONUSE | No comparative short-vector attack or optimized-constant improvement is claimed. |
| N02-DUAL-NUMBER | CHECKED | B quotient isomorphism is proved from gcd(D,q)=1 and finite quotient order, not inferred from nonzero/unit status; zero points are retained. |
| PAIRWISE-SE-F3 | CHECKED | A full joint S/E/source independence and B fixed-J product law are explicit; pairwise marginals alone are not used. |
| N03-PV-CONDITIONING | CHECKED | No active-PV or signed conditional-mixture transfer. A subtracts source bad probability; same-J pointwise advantage is required before C. |
| N03-SCAL-POSTERIOR | CHECKED | No prior ratio distribution after public observation. Every center-dependent theta is normalized by its actual expectation; adaptive C hybrids condition on history. |
| RECT-ALG-1 | CHECKED | A Schur complement and square-completion identities checked for rectangular M, including rank zero/deficiency; integrality uses M(J) subset Z^(kn). |
| SOURCE-SMALL-D | SCOPE_LIMIT | A/B do not certify hard sources at small D or any D. Easy-source cases satisfy the conditional inequality without establishing standard security. |
| A-PPT-LEDGER-SCOPE | SCOPE_LIMIT | No historical q/d parameter substitution or all-q hardness import. B has explicit log-size runtime; A generic conditions require a separate current instantiation. |
| EX-PURE-MIX-ZERO | NONUSE | No two-seed pure mixing expansion. B consumes k independent inputs and A completes the same k multipliers; no zero-mass dilution shortcut. |
| EX-PUBLIC-TAPE | CHECKED | B retains J/declared metadata but not local coset/Gaussian coins in the uniform comparator. A proof-side disclosures occur solely in planted guessing bound. |
| EX-APPENDED-H | CHECKED | A integrates H out before comparing to independent target E, then reveals H only in the completed guessing experiment; no false joint (H,E) comparison. |
| EX-M3-CROSSBLOCK | CHECKED | A uses full M M^T including cross-blocks and \|\|M\|\|<=sigma/(2t), hence the full C>=3sigma^2I/4; separate marginal positivity is not used. |
| EX-RETAINED-M3 | CHECKED | B conditions on original J, retaining its shared correlations; only conditional sample independence is asserted. No zero/Gaussian atom removed. |
| B-JL-BZERO | NONUSE | No old b-denominator tail formula. Current positive widths and guarded theta denominator have explicit domains. |
| B-JL-REDRAW-T | CHECKED | The SAME J is fixed across all input/output samples and both worlds; no support/ideal redraw within the source tuple. |
| A-ERASURE-RANKMIX | NONUSE | B is a GP-to-FG channel, not erasure of ordinary RLWE multipliers; no fixed-rank ideal source is claimed from erasure. |
| D-THETA-RETAIN-U-v1 | CHECKED | B local offsets/rounding coins are excluded from comparator metadata. A H disclosure occurs only after replacing the planted noise law; no retained-offset uniformity extension. |
| D-LSW-THETA-1 | CHECKED | Original exact LSW factorization remains rejected. B retains both coset and center theta normalizers; A retains its actual completion normalizer; no exact convolution import. |
| C-TOWER-RELATION-1 | NONUSE | No tower or change of cyclotomic degree in A/B/C periodic chain. |
| D-REUSED-PIVOT-1 | NONUSE | No selected RLWE pivot or reuse of failed pivot rows. B fresh local quotient sampling preserves comparator by equivariance. |
| A-TOWER-LAW-1 | NONUSE | No radix multiplication or missing tower response programming. |
| C-SMALL-N-EXISTENCE-1 | SCOPE_LIMIT | No finite-to-asymptotic existence extrapolation. A basis existence is proved for every ideal by Minkowski and a rational lattice flag. |
| D-NORMALFORM-WRAP-1 | CHECKED | A guesses an unwrapped auxiliary Y solely for an information upper bound, then maps forward modulo q. It does not replace wrapped secret events by integer cube restrictions. |
| RF2-OHCP-V1-LOGSHIFT | EXPLICIT_COUNTERCONTROL_REJECTS_V1_PROOF | All separately displayed v1 confidence bounds hold but actual starting decay fails by a constant; new shift repairs different version only. |
| RF2-OHCP-V2-ORIGIN-BALL | REPAIR_REQUIRES_ADDENDUM | Origin-centered ball permits residual beyond6d0; addendum8d0 bound covers both domains. No silent edit of v2 bytes. |
| RF2-IDEAL-SMOOTHING-PACKING | PROVISIONAL_ANALYTIC_POSITIVE_CONTROL | Independent full-spectrum packing proof recovers exp(-nc^2), no finite experiment or unread primary proof import. |
