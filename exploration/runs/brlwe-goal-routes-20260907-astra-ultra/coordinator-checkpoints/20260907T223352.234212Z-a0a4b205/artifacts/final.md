A new conditional search-hardness implication has passed full mathematical, blind, and source review: assuming pseudorandomness of the exact two-point nonbinary hidden-ideal source below, coefficient-binary rank-one RLWE recovery from **one or two samples** is hard for uniform probabilistic polynomial-time algorithms, at polynomial modulus and with negligible reduction loss. Final acceptance is pending the ledger-scope repair recheck and delivery audit. This does **not** resolve the original polynomially-many-samples recovery question.

## Exact source, target and computational premise

Let n grow through powers of two, ell=ceil(log2 n), and R_q=F_q[X]/(X^n+1). Write D_t(k)=exp(-pi k²/t²)/Z_t on the integers. The source **Base2(n,q,d)** chooses a uniform d-subset T of the n CRT roots once; conditional on T, it chooses U_1,U_2 independently and uniformly in the ideal I_T supported on T, including zero coordinates. It independently chooses all 2n integer coefficients of F_1,F_2 from D_ell and publishes (U_1+F_1,U_2+F_2) modulo q. The comparator consists of two independent uniform R_q elements. The challenger supplies one pair and no oracle, support, witnesses, binary secret, correlated completion or target responses.

The explicit computational hypothesis is that these two source worlds are indistinguishable by every uniform randomized polynomial-time test, for the separately selected parameter family below. It is **assumed, not proved**. The source specializes the same-hidden-ideal noisy-point problem motivated by Order-LWE Section 7; its exact comparator and shared-ideal law are made explicit using that paper's final hybrid. Its polynomial modulus and small noise are additional parameter choices for the assumption, not a worst-case or standard-RLWE consequence proved by the cited paper. Coefficient D_ell agrees exactly with canonical spherical width sqrt(n)ell by Parseval. See the [source review](criticism/RS1/report-v1.md) and [source comparison](source-comparison.md).

For each fixed m in {1,2}, the target chooses independent uniform a_1,...,a_m in R_q, one common uniform coefficient-binary S in {0,1}^n, and **fully independent** coefficient D_sigma_m errors E_i, jointly independent of S and the multipliers, where sigma_m=2sqrt(m)n ell³. It publishes ((a_i,a_iS+E_i))_i. Success means returning the actual sampled S, not merely any residual-consistent secret. The solver gets no additional samples.

## Finite implication and costs

For every target solver Q with exact success epsilon_m, the source test B_m uses its single supplied source pair as the first m multipliers, samples its own independent S and target errors, invokes Q once, and accepts exactly when Q returns that S. For m=1 it ignores the entire second source component. With absolute source distinguishing advantage,

    epsilon_m <= Adv_Base2(B_m)
                 + q^d ((1+D_ell(0))/2)^n + eta_N + delta_F,m.

All constants are explicit. Put

    kappa(t) = 2 sum_(j>=1) exp(-pi t j²),
    Delta_N = (1+kappa(3ell²/4))^n - 1,
    eta_N = min(1, Delta_N/(1-Delta_N)) if Delta_N<1,
            1 otherwise,
    delta_F,m = min(1, mn exp(-pi ell²)/(pi ell)).

For a finite implementation, add xi_source+2xi_alg+xi_target. These are total-variation errors for the full planted pair, the entire challenge-independent local (S,E) sampler, and the target witness/transcript law respectively; the source comparator is exact uniform. An approximate comparator requires its own additional error. One can choose xi_alg<2^-n with bounded polynomial runtime. The exact theorem is [theorem-only-v2.md](candidates/search/theorem-only-v2.md); complete derivations are the [proof](candidates/search/proof-v1.md) and [sampling/dimension supplement](candidates/search/supplement-v1.md).

Beyond the one Q call, B_m uses n fair secret bits, mn independent Gaussian coefficient draws, m ring multiplications and additions, and a canonical equality check. At these parameters, a shared table with O(n²ell³) entries and O(n+log n) probability bits gives the stated Gaussian approximation; naive ring multiplication uses O(n²) modular operations per sample. The total bit complexity is polynomial in the security parameter n. No source sampling, hidden-ideal recovery, matrix-Gaussian sampler, G sampler or completion oracle is executed by B_m.

## Fixed asymptotic parameter families

Choose **q(n) as the least prime congruent to 1 modulo 2n³**. The checked Xylouris least-prime theorem gives

    2n³+1 <= q <= C(2n³)^5.18 <= n^16 eventually,
    q/sigma_m >= n eventually.

This is one specified polynomial-modulus sequence, not a conclusion for every polynomial q. Deterministic progression enumeration with trial-division primality testing, and even exhaustive public root enumeration, run in polynomial time in unary n under this bound. Input length is O(n log n); no practical parameter threshold or benchmark is asserted.

Either of the following concrete, polynomial-time computable choices supports the consequence, **under its own Base2 hypothesis**:

- d(n)=floor(sqrt(n)/ell^4), eventually positive;
- d(n)=floor(n/(64ell)), eventually positive.

Both eventually satisfy d<=n/(64ell). Since D_ell(0)<=1/ell,

    q^d ((1+D_ell(0))/2)^n
       <= 2^(-3n/4+n/(ell ln 2)) <= 2^(-n/2) for ell>=6.

The completion and mask-tail losses are exp(-Omega(log² n)), hence negligible against every fixed inverse polynomial. Widths, modulus sequence, d and sampler precision are fixed before the adversary. Therefore every uniform PPT target solver has negligible exact recovery under the chosen source premise. The implication has a full asymptotic negligible-success conclusion; it is not limited to a promised advantage exponent. See the [parameter table](parameter-table.md).

The general entropy interval in the frozen theorem is purely conditional. It does not assert plausible source hardness at every d, and merely computable d does not imply efficient setup. In particular d=1 has a polynomial distinguisher: enumerate n*q ideal points using the first source component and test a coefficient residual box. Its planted acceptance is 1-negl(n), while uniform acceptance is at most nq(2ell²+1)^n/q^n. The reviewed existing ATT method also gives a polynomial source attack at d=O(log n); for the two displayed growing choices its exp(O(d)) bound is superpolynomial. This bounded attack comparison supplies no proof of the remaining source hypotheses.

## Why the argument closes its analytic obligations

On the event |F_i,j|<=ell², stack the integer negacyclic multiplication matrices into M of shape mn by n. Then ||M||²<=mn²ell^4. For proof-only G~D_ell^n, choose H conditional on F as the exact integer Gaussian with positive exponent matrix B=sigma_m² I-ell²MM^t, independently of S,G. Completing squares and using a normalized Poisson sum gives the full retained-source comparison MG+H versus the iid mn-dimensional target error, with exactly eta_N. The normalizer and the piecewise guard are retained. For two samples the off-diagonal blocks of B are essential; Gaussian marginals alone are insufficient.

After retaining S in that comparison, reveal source coins and H only in the completed world. They are independent of (S,S+G). The completed transcript is determined by these variables, S+G and one quotient of S with at most q^d values. Revealing this quotient multiplies average guessing probability by at most q^d. The exact unwrapped noisy-bit probability is ((1+D_ell(0))/2)^n; wrapping can only reduce it. This argument needs no uniform quotient, invertible ideal point or extractor. The Gaussian completion is proved directly in the [rectangular note](coordinator/rectangular-completion-v1.md) and frozen proof, so no historical analytic certification or unimplemented conditional source sampler is assumed.

The lossiness/projection idea has ancestry in ordinary entropic LWE. The new implication here is its explicitly stated ring-source specialization, exact-witness recovery test, discrete joint completion, and one/two-sample parameter consequence. The [source referee](criticism/RS1/report-v1.md) compares the checked primary papers and repository outcomes; this is a claim of a new implication in that checked record, not an exhaustive literature-priority claim.

## Review, retained evidence and remaining scope

The [blind report](criticism/RB1/blind-report-v1.md) was frozen and hashed before any proposed proof or prior objection was disclosed, and independently reconstructs the finite and asymptotic argument. The [full mathematical report](criticism/RF1/report-v1.md) checks the exact proof/supplement, probability laws, constants, finite sampler, primary prime import and all historical regression IDs. The [source report](criticism/RS1/report-v1.md) checks the primary HLBDD interpretation, concrete parameter effectiveness, source attacks and scientific scope. These are complementary same-model reviews, not independent statistical confirmation or formal verification. Frozen author status headers are preserved; the current [ledger](claims.json) and [reconciliation](reconciliation.md) control disposition.

The delivery review found an imprecise modulus clause in A-PPT ledger v1. That exact version and its [failure of the broader bound substitution](coordinator/A-PPT-ledger-v1-scope-defect.md) were saved before repair. Ledger v2 names the exact least-prime family; the theorem and proof bytes did not change. Fresh parameter recheck and final delivery disposition are tracked in reconciliation.

Exact controls include 1,560 rational rectangular identities, 11,664 full-product probability models, 64,152 arbitrary-leakage models, 712 small ideal tuples, rare/posterior branches, actual-witness interfaces, dyadic rounding and the cached-prefix counterexample. Qualified Gaussian numerical sums remain diagnostics, with tails and floating-point limitations recorded. All code and original results are retained in the [experiment registry](experiments/registry.json). Historical records, including rejected probability claims, are preserved by [complete provenance hashes](imports/historical-file-index.json) and [regression dispositions](regressions.json). Finite tests do not establish asymptotic hardness.

Only A was selected for detailed development before the 50-minute boundary. [B partial splitting](workers/B1/final.md) preserves an exact packing/algebra candidate with an explicit 2f-source-point budget; [C computational transfer](workers/C1/final.md) preserves a larger-modulus decision candidate and scoped obstructions. Both remain provisional and deferred under [selection.md](selection.md). They are not dependencies of the search result.

The original polynomially-many-samples problem remains open. No target decision hardness, standard-RLWE or worst-case source reduction, quantum/nonuniform security, practical bit-security estimate or efficient hidden completion sampler is established. A useful future test is a rigorously budgeted extension to more independent source points, or a source-hardness justification at the concrete growing d. Future work requires a new user decision after this capped service ends; no automatic restart is authorized.

## Service, goal and preservation record

Session/goal thread: `01a07dcb-40ad-7231-8540-1675639ae41b`. The exact native objective and creation receipt are in [goal-created.json](goal-created.json). No token budget was requested. The goal is still active at this delivery-preparation checkpoint.

- service: codex-cap-brlwe-goal-routes-20260907-astra-ultra-c5bc23d93e2c.service
- started_at: 2026-09-07T21:34:27.111419+00:00
- wrapup_at: 2026-09-08T00:14:27.111419+00:00
- graceful_shutdown_at: 2026-09-08T00:33:22.111419+00:00
- scheduled_kill_at: 2026-09-08T00:34:22.111419+00:00
- hard_deadline_at: 2026-09-08T00:34:27.111419+00:00

Initial Git revision was `174e0a2ca47dcb1e09ba8c5ae48117b698e2f2ed` on main, with an existing HANDOFF modification and untracked plan/run directories; exact intake worktree evidence is in [intake-verification.json](intake-verification.json). No research, literature, historical run, runner code or Git history was edited. All 1,902 indexed historical files passed the interim preservation check. HANDOFF and run-config received external launch-state updates after intake, matching a 21:37:37 startup receipt; both observed states, unchanged approval/cap identity and the initially failed preservation checks are retained in [metadata-change-observation-v1.json](coordinator/metadata-change-observation-v1.json). The coordinator did not overwrite them.

[Operational notes](coordinator/operational-notes.md) disclose late checkpoint intervals, two imperfect local assignment archives and restricted host-service visibility. A1's locally paraphrased scope and C1's altered heading are preserved, with later clearly dated exact-scope addenda; no missing original plaintext archive is reconstructed. The cap sidecar, fresh worker heartbeat and populated cgroup are available, while host service inspection is restricted. Actual launcher exit and descendant cleanup remain unobserved by this coordinator. File consistency checks certify saved-artifact consistency only; mathematical disposition comes from the claim-specific reconciliation.

Prepared 2026-09-07T22:30:08.949573+00:00


Update 2026-09-07T22:33:52.229517+00:00

RD1 integrated delivery-scope check passes; RP1 reports327680 exact parameter cases and applicable controls passed. An initial RP1 whole-node comparison failed solely because coordinator review metadata was added; its original code/failure are preserved and the v2 load-bearing-field check passes. Both final reports are being frozen. A-PPT v2 remains pending until exact reports and final artifact gate close; native goal remains active within original cap.
