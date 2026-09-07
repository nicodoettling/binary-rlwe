# Project handoff: binary-secret RLWE

Updated 7 September 2026. This is the entry point for continuing the project. The [discussion record](notes/discussion-summary-2026-09-07.md) provides the fuller history, bibliography, and explanation of the research choices.

## Current state

Nico Döttling is revisiting work with Zvika Brakerski on hardness of Ring-LWE with independent uniform binary coefficients. The original objective concerns recovering the secret from potentially polynomially many independent ring samples sharing that secret.

**No complete hardness theorem has been obtained.** The strongest new result is a reviewed conditional **one-pair decision-hardness implication** from pseudorandomness of an independently noised hidden-ideal source. The precise source-hardness premise needed for negligible loss remains open. There is also a reviewed subexponential distinguishing algorithm for the proposed source family, but no polynomial-time distinguisher at the chosen asymptotic parameters.

All three research runs are over. The latest run, `brlwe-joint-foundations-20260906-astra-ultra`, completed normally on 6 September at 21:10:51 UTC after approximately 1 hour 16 minutes, within its five-hour maximum. Its [exit manifest](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/exit-manifest.json) records success and no failure category. There is no pending launch or automatic continuation.

The repository is on `main`. The initial research snapshot is commit `bb424e7`; this handoff is added in a subsequent commit. Existing research artifacts and evidence snapshots are versioned. Raw launcher logs, Python caches, and one compiled experiment binary are ignored; their source and research results remain tracked.

## Read these first

| File | Purpose |
|---|---|
| [Discussion record](notes/discussion-summary-2026-09-07.md) | The conversation's progression, literature assessment, three runs, corrections, incident, and open questions. |
| [Latest final report](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/final.md) | Current scientific synthesis and scope of the retained results. |
| [Latest claim ledger](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/claims.json) and [reconciliation](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/reconciliation.md) | Exact current versions, dependencies, reviewer dispositions, and rejected or open claims. |
| [Observable-bridge proof](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/candidates/observable/statement-and-proof-v2.md) and [fresh recheck](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N02/review-v1.md) | The main new conditional implication and its repaired probability model. |
| [Source contract](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/inputs/SOURCE_CONTRACT.md), [target](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/target.md), and [parameter table](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/parameter-table.md) | Exact experiments, conventions, and simultaneous parameter requirements. |
| [Initial literature review](literature/reading-notes-2026-09-05.md) | Original papers, follow-ups, assumptions, and limitations of known approaches. |

The two supplied papers are Brakerski–Döttling, [*Hardness of LWE on General Entropic Distributions*](literature/2020-119.pdf), EUROCRYPT 2020, and [*Lossiness and Entropic Hardness for Ring-LWE*](literature/2020-1185.pdf), TCC 2020. Related bibliography and downloaded manuscripts are under `literature/`.

## Mathematical reference and principal result

The reference ring and secret are

$$
R_q=\mathbb F_q[X]/(X^n+1),\qquad
S=\sum_{j=0}^{n-1}S_jX^j,\quad S_j\overset{\$}{\leftarrow}\{0,1\},
$$

with growing power-of-two $n$. The target is $(a,aS+E)$ for uniform $a$, independent secret and coefficient Gaussian error, wrapped modulo $q$. The convention is $D_t(z)\propto e^{-\pi z^2/t^2}$: $t$ is a width, not a standard deviation. The reference modulus is polynomially bounded, with $q/\sigma\ge n^c$ for fixed $c>0$.

The common fully splitting prime regime uses

$$
\ell=\lceil\log_2 n\rceil,\quad
d=\lfloor\sqrt n/\ell^4\rfloor,\quad b=\ell^2,
\quad \tau=\ell,\quad \sigma=2n\ell^3,
\qquad \sigma n^c\le q\le n^K.
$$

A uniform $d$-subset $T$ of the CRT roots defines the ideal $I_T$ supported on $T$ and $J_T=\operatorname{Ann}(I_T)$. The first error $F$ has independent coefficient $D_\ell$ entries conditioned on $[-b,b]$. Conditional on $T$, $V$ is uniform in $I_T$. The two first-point conventions are:

- **Active:** $U$ is independently uniform nonzero on every coordinate in $T$.
- **Uniform:** $U$ is uniform in $I_T$, allowing zeros in $T$.

The improved computational source is

$$
\mathsf{Src}_{\rm ind}=(U+F,V+E_\sigma),
$$

with independent second Gaussian noise. A target distinguisher $D$ gives public source tests

$$
B_1(a,c)=D(a,aS+E),\qquad B_2(a,c)=D(a,aS_0+c),
$$

using fresh independent public-law draws. Under the exact noise-completion and conditional-extraction premises, the bound is

$$
\operatorname{Adv}_{\rm target}(D)
\le \operatorname{Adv}_{\rm ind}(B_1)+\operatorname{Adv}_{\rm ind}(B_2)
+2\eta_N+\eta_X+\eta_{\rm iso},
\qquad
\eta_{\rm iso}=\mathbb E\left[1-\frac{|UR_q|}{|I_T|}\right],
$$

before the separately stated implementation errors. The correlated sequential Gaussian completion is **only a proof coupling**; neither public test needs it, the hidden ideal, or hidden $F$.

For active $U$, $\eta_{\rm iso}=0$, but hardness of that source remains unsupported. For uniform $U$,

$$
\eta_{\rm iso}=1-(1-1/q+1/q^2)^d\asymp d/q.
$$

This is nonnegligible at fixed polynomial $q$. It differs from the latent conditioning cost $\delta_{\rm act}=1-(1-1/q)^d$. A public noise-broadening map connects an explicitly defined ordinary uniform-point, same-ideal HLBDD source to the uniform version, with negligible noise/truncation errors, but does not remove the rank loss. The underlying HLBDD source is itself a computational assumption, not a worst-case hardness theorem established here.

The earlier correlated source $(U+F,V+H_{\rm seq}(F))$, called **P0-A2**, remains independently unsupported. The new implication does not prove P0-A2.

## Best next question

**Can the active-point, same-ideal source inherit hardness from the ordinary uniform-point HLBDD source, or another independently specified assumption, with negligible total distinguishing loss in this fixed polynomial-modulus regime?**

A useful next investigation should begin with exact source experiments and quantify the active-coordinate change. A new source name or the absence of a binary-secret input is not independent computational support. A fixed inverse-polynomial statistical loss cannot simply be absorbed into a negligible-error claim.

The latest run also leaves open public transformations using both components, equal-small-noise starting distributions, and controlled approximate preservation of the uniform comparator. These lie outside the proved source-conversion obstructions. Multiple samples require a separately defined common-quotient-variable source, joint noise completion, and task-conversion accounting; no extension should be inferred from the one-pair theorem.

This is a proposed research question, not authorization to launch another unattended run.

## Claims and pitfalls to preserve

1. **Read the current ledger alongside frozen proofs.** The observable proof's historical header says “pending recheck.” Its edited bytes subsequently passed N02's review; the current entry is W3-OBS v3, corresponding to author proof v2. Do not edit frozen evidence to make its old header look current. Global status remains provisional rather than formally certified.
2. **Full joint laws matter.** A blind packet omitted joint independence of the secret, error, and source tuple and was refuted over $\mathbb F_3$. The repaired product-kernel law excludes that counterexample. Pairwise independence, matching Gaussian marginals, or covariance matching do not substitute for the required joint comparisons. Noise comparison integrates out the completion; extraction retains it.
3. **Sequential discrete Gaussians are distinct laws.** The LDL construction has adaptive centers and normalizers. Its shape matrix $B_F=\sigma^2\operatorname{Id}-\tau^2M_FM_F^{\mathsf T}$ is not the actual discrete covariance matrix. NC1 v2 includes necessary denominator guards. The imported NC1 v2, X1 v1, AN v2, and PR1 v1 remain globally provisional. Preserve the earlier S0 v3 correction, which explicitly includes its AN v2 dependency.
4. **Do not merge the quotient dimensions.** The first run obtained extraction at $d=\Theta(n/\log^3 n)$ for a specified binomial family. The later arbitrary-support theorem works in the smaller approximately $\sqrt n/\log^4 n$ regime. Arbitrary supports at the larger dimension remain open. The obvious small-noise binomial source was efficiently distinguishable.
5. **Keep the attack scope.** ATT v3 gives deterministic $\exp(O_c(d))\operatorname{poly}(n,\log q)$ distinguishing time under strict norm/root-input conditions. It is superpolynomial at A2, not a polynomial-time break. Later orbit calculations did not improve the optimized asymptotic algorithm.
6. **Keep obstruction hypotheses.** The entropy obstruction starts from the specified broad active-point independent-noise source and requires exact preservation of the uniform pair. The entropy and public rank-loss arguments use strict norm gates, satisfied eventually for $c>1/2$, including the common $c=1$ example. The hypothetical latent-kernel sampler requires polynomial time, fresh independent repeated calls, and uniform negligible error. These statements do not exclude arbitrary public reductions. The public rank-loss witness is exponential-time.
7. **Keep quantifiers and sample counts.** Constants such as $c,K$ are fixed before the adversary. The common $c=1,K=16$ example is asymptotic, subject to the recorded prime-existence import; no practical threshold or concrete security estimate was established. Rank one, ring degree, and number of samples are different quantities. Rotations are not independent samples.
8. **Preserve rejected versions and evidence limits.** A repaired claim needs a fresh check of its changed bytes and dependent claims. Agent agreement and finite experiments do not establish hardness. The latest numerical provenance record acknowledges an overwritten pre-correction Gaussian JSON; do not invent its original bytes or hash. See [experiment provenance](exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N01/experiment-provenance.md).

## Project map and precedence

| Location | Contents and use |
|---|---|
| `notes/` | Narrative discussion record. |
| `literature/` | Original papers, related manuscripts, bibliography, and reading notes. |
| `exploration/runs/brlwe-explore-20260906-astra-ultra/` | Completed broad exploration: twelve scouts, three developed candidates, criticism, and experiments. |
| `exploration/runs/brlwe-joint-ideal-20260906-astra-ultra/` | Interrupted first focused run, including completed reviews and corrected proofs. Its partial final report is not the final mathematical synthesis. |
| [Consolidation](exploration/consolidated/joint-ideal-20260906/CONSOLIDATED.md) | Reconciles the interrupted run and supersedes its partial report and precritic ledger for the historical mathematical state. |
| `exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/` | Latest authoritative research ledger, synthesis, frozen inputs, reviews, experiments, and exit evidence. |
| `exploration/joint-ideal-next/` | The plan and authorization for the already completed latest run. Despite the name, it is not an unlaunched next run. |
| `exploration/runner/` | Finite-run launcher, supervisor, tests, and operational documentation. |
| `exploration/incidents/` | Academic-research false-positive report and feedback submission receipt. |
| `exploration/verification/` | Preparation checks with explicit verification scope. |

Preserve old run directories, reviewed snapshots, hashes, and append-only claim histories. New research belongs in a new run directory or a clearly identified new note; it must not overwrite the evidence on which earlier reviews depend. `runner-snapshots/` and `coordinator-checkpoints/` are deliberately tracked because receipts and manifests reference them.

## Bounded-run workflow and user preferences

The user explicitly requested finite exploratory research, not a goal run, and chose **`gpt-6-astra` with `ultra` reasoning**. The focused plans use a five-hour maximum, permit early completion only after assigned obligations have dispositions, allow at most four active agents including the coordinator, and prohibit worker-spawned agents. Default local experiment timeout is 120 seconds, maximum 300 seconds, with at most two concurrent experiments.

Prepare a concrete plan and obtain the user's approval before a new unattended launch, as requested in this discussion. Existing `launch_authorized=true` flags record approvals for runs that already happened; they are not permission to replay those runs. There are no goal tools, automatic resumes/restarts, or recurring continuations. Do not contact researchers or publish externally without explicit authorization. The earlier feedback authorization covered the single submitted incident report.

Use the installed `codex-tmux-runner` skill for launching or supervising unattended sessions, and `mathematical-proof-audit` for extended proof efforts requiring its review workflow. Their local instructions are under `/home/nico/.codex/skills/`; they are external dependencies, not files bundled in this repository. Check the applicable instructions and host prerequisites before a future launch.

The [runner README](exploration/runner/README.md) documents the launcher. It relies on the locally installed helper, Codex CLI, Bubblewrap, tmux, and a systemd user service. The research process uses `workspace-write` with approval policy `never`; host service/preflight access is a separate permission boundary. The independent timer covers research descendants and is not extended by monitoring or snapshot work.

The coordinator maintains `claims.json`, `reconciliation.md`, `progress.md`, `final.md`, and `agents.json`, with five-minute checkpoints and updates after worker results. Nonauthor reviews must address exact claim versions, followed by coordinator reconciliation. Process success, artifact integrity, and scientific completeness are separate records.

### Status and local verification

Read persisted status without launching research:

```sh
python3 exploration/runner/bounded_run.py status \
  --run-file exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/run.json
```

That command reads saved evidence; it does not certify live process state. For a live host check, use the installed helper:

```sh
python3 /home/nico/.codex/skills/codex-tmux-runner/scripts/codex_tmux.py status \
  --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/tmux-run.json
```

If runner code changes, the local suite is:

```sh
python3 -m unittest discover -s exploration/runner -v
```

The recorded preparation run passed 37 tests. Discovery does not launch models or services; the explicitly invoked deadline integration script is guarded from import-time execution. A documentation-only change needs appropriate file/link review, not another research run or a rerun of mathematical experiments.

### Prior interruption and recovery

The first focused run ended on 6 September at 15:59:48 UTC with `cyber_policy`. This was a content-policy termination, **not** an automatic tool-approval review rejection. Its exact trigger is unknown. Mathematical reviewers had finished, but coordinator reconciliation had not. The user emphasized that the task was academic theory and requested incident handling and better preservation.

The [feedback receipt](exploration/incidents/2026-09-06-feedback-receipt.json) confirms submission at 18:09:59 UTC without logs or research attachments. It is not evidence of a support resolution. The subsequent runner changes preserve snapshots, detect structured current-session errors, and write exit manifests without synthesizing mathematical conclusions. Confirmed policy errors stop only the owned run; do not rephrase, retry, or reroute automatically. Alerts are local files/logs, not push messages. These mechanisms do not prevent upstream screening.

For recovery, begin with the latest preserved claim ledger, reconciliation, partial/final report, and checkpoint manifest. Do not infer mathematical completion merely because a file exists or the process exited successfully. The latest run completed without a policy interruption.
