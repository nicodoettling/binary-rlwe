# Self-contained resume checkpoint

The goal is active and not achieved pending fresh review. Do not create another goal. Read goal state, exact cap sidecar named by launcher-run.json, claims.json and this checkpoint before scheduling work. Authorization covers only the current live service; after termination/expiry any further work needs a new user decision and explicit duration.

No new hardness implication has yet passed all review gates. The strongest candidate is a new conditional polynomial-modulus search implication for exactly one or two coefficient-binary rank-one RLWE samples. Fresh blind, full-proof, and source/scope reviews are in progress.

Let n grow through powers of two, ell=ceil(log2 n), and R_q=F_q[X]/(X^n+1). Base2 samples one uniform d-root support T, independent uniform U_1,U_2 in the ideal supported on T, and independent coefficient D_ell masks F_1,F_2; it publishes their two sums modulo q, versus two independent uniform ring elements. Pseudorandomness of this exact nonbinary source is assumed. The source's relationship to primary HLBDD and its limitations are in [source-comparison.md](source-comparison.md).

For m=1 or2, the target has independent uniform multipliers a_i, one common independent uniform coefficient-binary S, and fully independent coefficient D_sigma_m errors, sigma_m=2sqrt(m)n ell³. The source test samples S and target errors locally, calls the target solver once, and checks equality to the sampled S. Its finite bound is

    epsilon_m <= Adv_Base2(B_m)+q^d((1+D_ell(0))/2)^n+eta_N+delta_F,m.

Here D_t(k) is proportional to exp(-pi k²/t²), kappa(t)=2 sum_(j>=1)exp(-pi t j²), Delta_N=(1+kappa(3ell²/4))^n-1, eta_N=min(1,Delta_N/(1-Delta_N)) for Delta_N<1 and1 otherwise, and delta_F,m=min(1,mn exp(-pi ell²)/(pi ell)). A finite implementation adds xi_source+2xi_alg+xi_target for the specified full joint laws. See the [exact statement](candidates/search/theorem-only-v2.md), [complete proof](candidates/search/proof-v1.md), and [dimension/sampling supplement](candidates/search/supplement-v1.md).

Choose q as the least prime1 mod2n³. The checked primary prime theorem gives2n³<q<=n16 eventually, hence q/sigma_m>=n. Both d=floor(sqrt(n)/ell4) and d=floor(n/(64ell)) have negligible total loss; each choice is a separate exact source assumption. The latter's guessing term is at most2^(-3n/4+n/(ell ln2)). Small-d source assumptions are not generally plausible. The concrete functions are efficiently computable; a merely computable generic d family is not being advertised as efficient parameter generation.

The reduction uses one source pair, one solver call, n exact secret bits, mn independent Gaussian coefficients, m ring multiplications/additions and one equality check. Polynomial tables give xi_alg<2^-n; coefficient ring arithmetic and all bit lengths are polynomial in n. The auxiliary matrix Gaussian is proof-only. The new proof rederives rectangular completion with its normalizer and guard; it does not rely on unclosed quotient extraction or a matrix-Gaussian sampling implementation.

These are author/coordinator derivations pending independent-context mathematical scrutiny. [claims.json](claims.json) gives current exact dependencies; [reconciliation.md](reconciliation.md) will record complete referee dispositions. The original polynomially many shared-secret sample problem remains open. There is no target decision claim, ordinary-RLWE source reduction, or worst-case hardness claim.

B partial splitting and C larger-modulus decision are preserved as provisional initial candidates and deferred under [selection.md](selection.md). Their full notes and exact controls remain in [B1](workers/B1/final.md) and [C1](workers/C1/final.md). Historical rejected versions and provenance are imported by [reference hashes](imports/historical-file-index.json). New experiments are in [registry](experiments/registry.json); finite checks are evidence, not asymptotic proofs.

Session and native goal thread: `01a07dcb-40ad-7231-8540-1675639ae41b`; exact objective and creation receipt: [goal-created.json](goal-created.json).

- service: codex-cap-brlwe-goal-routes-20260907-astra-ultra-c5bc23d93e2c.service
- started_at: 2026-09-07T21:34:27.111419+00:00
- wrapup_at: 2026-09-08T00:14:27.111419+00:00
- graceful_shutdown_at: 2026-09-08T00:33:22.111419+00:00
- scheduled_kill_at: 2026-09-08T00:34:22.111419+00:00
- hard_deadline_at: 2026-09-08T00:34:27.111419+00:00
- state: running

The goal remains active and was not achieved at this checkpoint. No service restart or post-cap continuation is authorized. Host-service inspection is restricted; actual launch exit and descendant cleanup remain unobserved. [Operational notes](coordinator/operational-notes.md) disclose checkpoint and local assignment-archive limitations.

Next discriminating test: reconcile RB1 blind reconstruction, RF1 exact-proof controls, and RS1 primary-source/scope findings against the frozen candidate. Preserve rejected versions before repair, then obtain a fresh nonauthor recheck of any changed bytes. Do not call1/2-sample success the original polynomial-sample theorem.

Update 2026-09-07T22:12:07.509879+00:00

RB1 reports a complete independent reconstruction in its still-unfrozen blind partial; proof/objections remain withheld. RF1 reports11664 exact product-kernel models and64152 leakage instances passing, plus a qualified rectangular Gaussian diagnostic below the proved bound. RS1 confirms primary source and prime interfaces, and supplies a d=1 polynomial source distinguisher, limiting source plausibility to chosen growing examples. No final verdict is assigned before raw reports freeze. An artifact consistency checker is saved for fresh-process delivery verification.


Update 2026-09-07T22:16:46.734016+00:00

RB1 full blind report frozen before proof disclosure and hash verified; it reconstructs F/I/A. RS1 full source report frozen and verified; primary prime and exact two-point source interfaces pass with computational hardness explicitly assumed and small-d/efficiency qualifications. RF1 full proof report remains pending. No theorem is accepted yet.


Update 2026-09-07T22:19:59.258387+00:00

Fresh RD1 delivery/scope audit is active alongside RF1 final proof reconciliation. RB1 and RS1 are completed with frozen reports. All scientific claims remain provisional; source hardness is expressly assumed. The coordinator is checking historical applicability and exact delivered scope before final acceptance.
