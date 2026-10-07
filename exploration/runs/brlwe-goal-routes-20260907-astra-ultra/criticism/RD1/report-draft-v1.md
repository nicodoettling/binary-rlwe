# RD1 delivery and scientific-scope audit — draft pending integrated-byte pass

The frozen mathematical packet and the delivered first-pass scope agree, subject to the claim-graph wording issue RD1-D1 recorded below. No counterexample to the frozen theorem or omitted analytic assumption was found in this bounded delivery audit. The first-pass core remains provisional, correctly so. A terminal delivery verdict is reserved for the coordinator's integrated bytes and current accepted dependency graph.

This is academic theoretical cryptography research on binary-secret Ring Learning with Errors (RLWE). Every source and target is a formal distribution of synthetic ring elements. RD1 was a fresh nonauthor delivery reviewer, with no goal, descendants, mathematical experiment allocation, remote computation, publication or messages to other people. Work was confined to criticism/RD1. The mathematical-proof-audit skill and both references were read. Assignment and exact common scope are saved in assignment.md. Shared cap authority came from launcher-run.json and its exact cap.status_file, not a new clock; RD1 deadline is 2026-09-07T22:38:00Z and the inherited hard deadline is 2026-09-08T00:34:27.111419+00:00.

## Inputs and precedence

1. Exact candidates/search/theorem-only-v2.md, SHA-256 bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124.
2. Exact candidates/search/proof-v1.md, SHA-256 198c36bce9a73b87f2e1f5cf644d7e96b13cda063922f1ab10b0b2ee60114042, and supplement-v1.md, SHA-256 71752406e81e327b5c47d0d118ea9bc6aa0f87566d23345daf290a7b8322410a.
3. Root rectangular-completion-v1.md, SHA-256 d66a1ea3e1c61990c77380de60c39b00a3097ab111407aedc610cfbe34c70163, and source-and-parameters-v1.md, SHA-256 131e6a3feec87010007a30ddc1e37bdec44687648120bfe1e8c5187e6e779f50.
4. Frozen complete mathematical reports: RB1 blind-report-v1.md, SHA-256 c95e83a3a53cd589d2f2bf731ead33b35857af33edea28f1f3a0f8b722061b2d; RS1 report-v1.md, SHA-256 f04881cf65af51b7079fd59b785e9ca2d8cbc53fb710c06e0b823ae31cc20785; RF1 report-v1.md, SHA-256 ff7a034fa2d8be726a0940801a45697f082c342e786d3fd47a7674bd87b91c64.
5. Current delivery and claim graph, with timestamped read copies, then the plan endpoint rule and historical evidence only for provenance/regression applicability.

The first delivery snapshot is input/2026-09-07T222059.021823Z/manifest.json. The first report/support snapshot is input/support-first-pass/manifest.json, read at 2026-09-07T22:21:33.097789+00:00. The administrative interim snapshot is input/interim-check/manifest.json, begun at 2026-09-07T22:25:25.957674+00:00. These preserve actual read bytes; no mutable header is retroactively treated as the current proof's status. Administrative scripts record every source path, read time, byte size and SHA-256. Hashing an artifact does not mean every line was substantively reviewed.

## First falsification test and mathematical scope

| Item | Exact frozen requirement and comparison |
|---|---|
| Ring | n grows through powers of two; R_q=F_q[X]/(X^n+1), coefficient representation, odd integer prime q=1 mod 2n. No extension-field target or rank change. |
| Source | One uniform d-subset T of the CRT roots, two independently uniform U_i in I_T conditional on the same T, zeros allowed, all 2n integer source-mask coefficients independently D_ell, then reduction modulo q. Only the pair is released. Uniform comparator is the independent product on R_q^2. |
| Computational premise | Every uniform randomized PPT bit test has negligible absolute acceptance gap for the exact chosen Base_2 family. This is assumed, not derived from its syntax, HLBDD literature, ordinary RLWE or worst-case lattices. |
| Target | Exactly m=1 or m=2 independent uniform multipliers, one common uniform coefficient-binary S, and mn fully independent integer coefficient D_sigma_m errors, jointly independent of S and multipliers. Exact recovery of the sampled S, not any small-residual preimage. |
| Gaussian convention | D_t(k) proportional to exp(-pi k^2/t^2); t is the exponent width, not an asserted standard deviation. Coefficient source width is ell. Canonical width sqrt(n)ell refers to the primal coefficient lattice under the power-of-two transform, not an unstated torus or dual-lattice conversion. |
| Source/solver budget | One challenge pair, no source oracle, one Q invocation, one local fresh S and independent E tuple. For m=1 the entire second element is ignored. Reusing or rotating multipliers cannot silently produce more independent target samples. |
| Statistical loss | q^d((1+D_ell(0))/2)^n + eta_N + delta_F,m. The quotient is charged once, the full stacked comparison once, and the mask-tail event once. There is no additional unproved extractor, unit-conditioning, eta_iso or source broadening step. |
| Guard and tails | Delta_N=(1+kappa(3ell^2/4))^n-1; eta_N=min(1,Delta_N/(1-Delta_N)) only when Delta_N<1, and 1 otherwise. delta_F,m=min(1,mn exp(-pi ell^2)/(pi ell)). No negative denominator or success/bad-mask independence assumption. |
| Implementation | xi_source+2xi_alg+xi_target for the declared full joint laws. xi_alg is uniform and independent of the challenge; xi_target retains the witness. The source comparator remains exact; an approximate comparator needs its own error. |
| Completion | The auxiliary H is exact mathematical D_B and is used only in the coupling. For m=2 the full 2n-by-n stack and off-diagonal blocks are retained. No efficient matrix Gaussian, hidden-kernel sampling, or H_seq implementation is claimed. |

The checked retained-witness argument has the right order: first append independent S to retained-source noise TV and map to the witness/transcript; only then reveal C,H,Y and one quotient in the loss world to upper-bound guessing. It never transports the realized H through the target TV comparison. The noisy-bit product is a maximization and summation under a complete Cartesian product law, not a sequential conditional-product inference. RF1's applicable historical-regression table and finite rational controls address precisely those forbidden alternatives.

## Parameters, uniformity and costs

The specified q is the least prime 1 mod 2n^3. The checked published prime statement has exponent 5.18; substitution gives q<=C 2^5.18 n^15.54<=n^16 eventually, while q>=2n^3+1. The margin 16-15.54 is positive. At sigma_m=2sqrt(m)n ell^3,

    (q/sigma_m)/n >= n/(sqrt(m)ell^3) -> infinity.

Thus q/sigma_m>=n eventually. The finite-prefix threshold is neither practical nor claimed explicit here. Arithmetic and source/target descriptions have polynomial bit size in security parameter n. Polynomial time means polynomial in n, not merely in log n.

Both concrete dimensions floor(sqrt(n)/ell^4) and floor(n/(64ell)) are polynomial-time computable. For the square-root formula, integer comparison d^2 ell^8<=n computes the floor without a real oracle. Each formula defines a separate source assumption. A merely uniformly computable generic d sequence may require superpolynomial setup; the conditional theorem can still be formulated because B_m need not compute d. The delivery must not assert efficient generation for the entire generic clause.

For the larger range, d log2 q<=n/4 specifically uses q<=n^16. Together with D_ell(0)<=1/ell it gives

    q^d((1+D_ell(0))/2)^n <= 2^(-3n/4+n/(ell ln 2)).

This is at most 2^(-n/2) for ell>=6. The completion and mask tails are exp(-Omega(log^2 n)). No solver success exponent is used to select q, d, widths, or sampler precision. All losses are negligible for each concrete family, so the conclusion concerns every uniform PPT Q, not a promised fixed advantage.

B_m's cost is T_Q plus n exact fair secret bits, the full local E sampler, m negacyclic multiplications/additions and one equality check. Source generation, finding the hidden ideal, and completion sampling are not reduction costs. An independently executable approximate source family at either concrete d has polynomial setup by enumeration/CRT/subset sampling and coefficient Gaussian tables, with its full-law error charged. Exact uniform finite sampling from odd-cardinality sets and exact infinite Gaussian laws remain mathematical idealizations unless approximation or another random-bit runtime convention is supplied.

For local target sampling, sigma_m^2=4mn^2ell^6 is integral, B_E=2mn^2ell^3>=n sigma_m, and the table has O(n^2ell^3) entries. The supplement accounts for raw-weight errors, their normalization, final dyadic rounding, and product coupling; O(n+log n) probability bits and polynomial preprocessing give xi_alg<2^-n. This is a proved implementation bound, not a executed cryptographic benchmark. The precise 2xi_alg factor is conservative because the local approximation affects both source endpoints.

## RD1-D1 — claim-graph wording scope

At the first snapshot A-PPT v1 said “At fixed polynomial q(n) and either explicit growing d family”. Read alone, that description is broader than the actual reviewed consequence, since arbitrary polynomial exponent K need not satisfy the larger-family entropy budget. For q near n^K and d near n/(64ell), d log2 q is near Kn/64; for K>64 that exceeds n. This falsifies the inference that polynomial modulus alone certifies the displayed negligible guessing loss; it does not refute the frozen theorem. The PRIME-POLY dependency and parameter table identify the intended modulus, so the surrounding exposition already selects the correct regime.

The coordinator was immediately notified to bind the A-PPT node to the specified least-prime q(n). No author proof or source file was edited by RD1. The interim administrative snapshot records A-PPT v1 as REJECTED during integration; this status is a tracked wording correction and must not be misreported as rejection of the exact frozen theorem. Final narrowed wording and version linkage still require inspection in this draft.

## Evidence graph and acceptance limits

RB1 reconstructed F, I and A from the frozen statement without the author proof, conditional on the supplied prime theorem and explicit source premise. Its manifest declares report freeze at 2026-09-07T22:15:09.955862+00:00 before proposed-proof or historical-objection disclosure. RF1 checked the exact author proof, supplement, root completion and parameter files, including retained-witness laws, rectangular normalization, finite sampler, fixed asymptotics and historical controls. RS1 checked the source interpretation, published prime interface, parameter effectiveness, bounded novelty comparison and source-premise limitations. The reports' roles are complementary; all agents share the model family and agreement is correlated scrutiny, not independent statistical evidence.

The initial provisional graph cannot support a final acceptance merely because these reports exist. Current accepted status must be attached to the exact version of every dependency and to the matching raw review evidence. SOURCE-2 can be accepted as a definition and literature-motivation interface; its computational hardness must remain an explicitly assumed premise. A-PPT additionally needs the supplement's large-d substitution and finite sampler, not just the theorem-only statement's prose. Reconciliation must map these exact accepted objects and preserve all historical rejected shortcuts and applicable test outcomes.

The administrative interim check ran in a fresh Python process and passed 14 checks over 105 archived inputs: cap identity, unique/acyclic graph, current dependency versions, available proof paths and accepted review receipts, exact author/delivery bytes, frozen theorem/support/report hashes, RB1 blind declarations and complete artifact hashes, complete RF1 artifact hashes, RS1 input equality, coordinator evidence manifest, local Markdown target existence, history parsing, and read stability. These are administrative checks only. No new finite mathematical search was allocated or run; existing exact controls and their reviewer reasoning supply that evidence. The checker does not infer mathematical truth from passing hashes or file existence.

## Scientific endpoint and material caveats

PLAN.md explicitly permits a modest new fully checked conditional implication, with exact task/sample scope, to qualify as a scoped goal achievement. It prioritizes search and polynomial q; a fixed promised-advantage result or unproved analytic bridge is only partial progress. The current result, if the graph and delivery gates close, meets that scope with polynomial q and all negligible reduction losses, under an independently specified and substantively literature-motivated nonbinary Base_2 premise. This is a new implication relative to the checked project record and selected sources, not a claim of exhaustive priority across all literature.

The full list of material exclusions/limitations to keep visible is:

- Exactly one or two target samples. Polynomially many shared-secret samples remain open.
- Computational hardness of each chosen growing-dimensional Base_2 family is assumed. No standard-RLWE or worst-case reduction is proved, and no practical security claim is justified.
- The general d range is an entropy range, not universal source plausibility. d=1 admits an elementary polynomial distinguisher; RS1's cited scoped attack also covers d=O(log n). Neither fact refutes the literal conditional theorem.
- The two explicit growing d families are efficiently computable; generic computability alone supplies no efficient setup. Different d values require separate source assumptions.
- Primary HLBDD gives motivation and the intended same-ideal/two-point interface. Terse printed notation is resolved explicitly; this is not a claim of a verbatim fully specified source or imported hardness at the new parameters.
- Independent coefficient errors, the width convention, exact uniform comparator, one source pair and exact sampled-witness equality are load-bearing. Approximate implementation changes require the full-law TV charges.
- H is proof-only; matrix Gaussian sampling is not certified or required.
- No target decision hardness, nonuniform-circuit or quantum hardness, arbitrary extra samples, or return to a different modulus through an unstated reduction is implied.
- Polynomial complexity is asymptotic in n with a coarse exponent; there is no practical parameter threshold or benchmark.
- Numerical Gaussian diagnostics use explicit finite-tail bounds and ordinary floating arithmetic rather than directed-rounding certification. The analytic proof and exact rational identities carry the claim.
- Same-model reviewer agreement and bounded finite searches are supporting review evidence, not probabilistic independence or unrestricted theorem proofs.
- Native goal completion, service exit and process cleanup are distinct from mathematical/artifact acceptance. RD1 did not inspect host process cleanup or modify goal state.

## Administrative errors and final-pass work remaining

The initial `python` invocation failed with command not found, exit 127; installed `python3` performed the administrative writes. A batched tool output was truncated, so omitted portions were read in smaller ranges. A requested sed range beyond proof EOF returned empty output and the actual closing sections were subsequently read. No content-policy interruption occurred, no new literature survey was conducted, no package was installed, and no old file was edited.

Await coordinator integrated-byte notification, then archive/review those exact bytes, rerun the administrative checker with a new snapshot label, resolve RD1-D1 against the final A-PPT node and version history, and freeze a final report with its exact input manifest. Do not turn this draft into a final ACCEPT before that pass.
