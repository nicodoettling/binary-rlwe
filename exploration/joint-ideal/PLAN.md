**Five-hour investigation: joint noisy-ideal distributions and binary-secret RLWE**

Status: the user confirmed launch on 2026-09-06 with “please go ahead and launch”. Authorization is recorded in run-config.json; actual startup and deadlines are recorded in the new run directory. Continue with gpt-6-astra and ultra reasoning for the coordinator and every worker, following the user's earlier model choice.

This is a finite investigation with a five-hour maximum, not a goal run. It may finish early after completing the specified investigations and criticism. It must not finish merely because one attractive lemma has been written or a nearby assumption has been renamed. A supported obstruction or a precise explanation of the remaining gap is an acceptable result; there is no quota of viable constructions.

**The question**

Can an efficiently sampled distribution of two noisy points in a hidden ring ideal be both computationally plausible and compatible with a conditional-extraction reduction for binary-secret RLWE?

The proposed source has the form

\[
(A,C)=(U+F,V+H),\qquad U,V\in I,
\]

where the same hidden ideal I is used twice. The joint law of F and H is part of the assumption. Its two marginals being pseudorandom would be insufficient. The reduction sketch uses auxiliary Y=S+G, a noise coupling E=FG+H, and extraction of S modulo the annihilator of I. Read [BRIDGE_CONTRACT.md](BRIDGE_CONTRACT.md) before changing any of those dependencies.

The run has four limited objectives:

1. Write a correct conditional one-sample theorem with explicit source inputs, algorithms, distributions, errors, and advantage accounting.
2. Investigate at most two concrete source/coupling families, and determine whether their extraction, noise, and computational requirements can hold in the same parameter regime.
3. Attack those families and examine the separate obstacles to multiple samples and a search-hardness conclusion.
4. Deliver a critically reviewed assessment: a qualified candidate, a restricted impossibility result, or an exact list of missing statements. A theorem assuming the desired source pseudorandomness does not itself justify that assumption.

**Reference target and permitted departures**

Start with R_q=Z_q[X]/(X^n+1), growing power-of-two n, dense independent coefficient-binary S, rank one, uniform public multipliers, and independent coefficient errors D_sigma(z) proportional to exp(-pi z²/sigma²). Use the wrapped law modulo q. The baseline is odd polynomially bounded q and q/sigma at least n^c for a fixed positive c. This is a comparison regime, not an assertion of hardness for all such choices. Fully split primes are the initial algebraic model.

First establish exactly what one sample would imply. The original objective concerns polynomially many independent ring samples sharing S, so a one-sample endpoint must retain that limitation. Rotations and repeated added noise are not fresh public samples. Search, decisional indistinguishability, weak search, average success, and recovery of the original planted witness must be distinguished.

Other modulus/noise regimes, general ideals, and alternative auxiliary channels may be explored when motivated, but record every departure and its cost. A result for superpolynomial q can be a qualified theoretical result; it must not be reported as satisfying the polynomial-q baseline. Prior completed reports and source files are read-only inputs.

**Team and timetable**

One coordinator and at most three concurrent workers; workers may not spawn agents. Every fresh worker uses model gpt-6-astra, reasoning_effort ultra, and fork_turns none. All receive the exact contract and known counterexamples; this focused run does not repeat the previous blind disciplinary scouting exercise. Later critics must be different from the authors of the claims they review.

| Elapsed time | Work | Required checkpoint |
|---|---|---|
| 0:00–0:15 | Freeze distributions, target, source packets, and deadlines. | target.md, dependencies.md, claim ledger, partial final.md. |
| 0:15–1:00 | Three foundational assignments F01–F03. | Conditional bridge, noise constraints, source/attack comparison. |
| 1:00–2:15 | Three development assignments D01–D03. | At most two explicit source families and a separate sample-extension analysis. |
| 2:15–3:15 | Targeted refinement and attempts to break the candidates. | One shared parameter table and a decisive test or explicit unresolved obstruction for each candidate. |
| 3:15–3:55 | Three fresh nonauthor reviews of the bridge, source hardness, and sample/noise claims. | Critic reports tied to exact claim versions. |
| 3:55–4:15 | Coordinator reconciles objections; bounded author responses if useful. | Corrected claims and retain/retire/defer decisions. |
| 4:15–4:45 | Synthesis only, no new mathematical investigations. | Final report and reproducible supporting files. |
| 4:45–5:00 | Interrupt remaining workers and experiments before collecting their saved notes; finalize status. | Zero active research work, completed or clearly partial report. |

These are latest phase boundaries, frozen at launch. Advance early if phase obligations are satisfied. Do not extend later boundaries after a delay. Before an early final answer, document the disposition of both candidate slots, the sample-extension question, and every material critic objection. No automatic continuation follows this run.

**Foundational assignments**

F01 — Conditional reduction and source interface. Reconstruct the one-sample hybrid from the generative model. State the joint extraction law, exactly which variables accompany each distance bound, the isomorphism condition on U, and both efficient computational reductions. Track two potentially different distinguishers against the same source. Distinguish a mathematical coupling from an implementable source sampler. Treat the previous conversation's sketch as a conjectural contract to check, not authority. Produce a finite advantage statement or the first precise defect. Inventory what can be concluded about search, including any held-out-sample verification requirement.

F02 — Noise completion and dependence. For an explicit F distribution, investigate whether H can be sampled in polynomial time without knowing S or G so that FG+H matches the target noise with the required conditioning. Use the unwrapped continuous Gaussian covariance complement as a diagnostic, then address discrete and wrapped distributions directly. A covariance obstruction in the unwrapped Gaussian subclass does not automatically exclude all wrapped or nonlinear simulators. Explore finite-group Fourier deconvolution/positive definiteness, discrete Gaussian convolution and quantitative likelihood comparison where justified. If a Rényi bound replaces TV, rederive the actual advantage or success transfer; search-event bounds do not automatically preserve decisional advantage. Record source samplability, precision, truncation error and public/latent correctness separately.

F03 — Source families, prior work and attacks. Give exact source experiments with no binary secret in their input definition. Compare their two-sample task and F/H correlations to hidden-lattice BDD, the relevant Order-LWE construction, DSPR/NTRU-style sources, and partial Fourier/ideal decoding work. Identify any actual reduction or theorem in the matching regime; otherwise classify the new hypothesis as independently motivated or tailored. Build an attack inventory for the entire pair, including ideal-support enumeration, block/code decoding, short multipliers, source-pair combinations, and correlations introduced by completion. Do not interpret failure of one algorithm as evidence of hardness.

**Development assignments and candidate choices**

At the one-hour boundary, the coordinator combines F01–F03 into an initial compatibility gate. Admit at most two precisely stated families whose hypotheses can be posed together without a known contradiction; an explicitly missing theorem is permitted. If none qualifies, dedicate development to the strongest obstruction and one smallest justified relaxation within this program. Record the change before working on it.

D01 — Rich hidden supports and extraction. The principal candidate to examine uses genuinely many possible CRT supports, initially a random subset of the appropriate size. State the required extraction jointly with the chosen support and all relevant auxiliary observations. Try to extend the run's Fourier collision calculation using applicable primary-source estimates. A random support alone proves neither extraction nor computational hiding. The known binomial family is a regression/control, since its matching small-perturbation sampler is distinguishable. Inspect not only uniformity of individual CRT coordinates but their joint distribution and the resulting complementary ideal.

D02 — Alternative source/coupling. Develop a second family only if it differs substantively in ideal distribution, noise construction, or computational source. Possibilities include a correlated but efficiently generated completion justified by a source reduction, or an auxiliary channel avoiding the independent-additive template. State precisely how a modified channel keeps Y efficiently samplable from the public source challenge. If no distinct defensible family exists, use this slot to attack the first family and derive a restricted obstruction. Do not populate it with another name for binary RLWE.

D03 — Multiple samples and task conversion. With shared Y, track K=Z-pi_J(Y), V_i=U_iK, and E_i=F_iG+H_i jointly. The V_i are not independent fresh ideal points. For the continuous diagnostic use a stacked covariance matrix, including cross-sample blocks. With separate Y_i, extraction must hold given the entire leakage collection; quantify its information cost. Compare justified sample-expansion methods, with source assumptions and noise/sample losses explicit. Separately assess how a decision result would rule out secret recovery for the intended sample budget. A one-sample theorem remains valuable, but cannot silently discharge this assignment.

During 2:15–3:15, the coordinator allocates at most three bounded follow-ups to the most discriminating unresolved points. Prefer the first failed compatibility condition to polishing a peripheral lemma. At least one available slot is assigned to a worker whose task is to break a proposed source or coupling, rather than improve it.

**A common feasibility test**

Every candidate must have one table covering all of the following at once:

- The ideal/support law, degree, modulus, quotient dimension and actual input/output entropy budgets.
- How U is sampled, active-unit probability, and the cost of conditioning; changing its law changes the source assumption.
- The exact joint source law of U,V,F,H and which variables are public. Can it be sampled in polynomial time at the claimed precision?
- The auxiliary G law, its independence requirements, and a public algorithm to sample Y without hidden challenge data.
- The perturbation needed to obscure the ideal versus the operator/noise constraints needed for completion.
- Extraction error, noise-comparison error, bad-event mass, and computational reduction loss, all at the same parameter values.
- The number of correlated source components and target samples, and the claimed decision/search implication.
- Known attacks and the exact hypotheses that make them succeed or fail.

Do not combine a valid extractor at one width, a plausible assumption at another, and a simulator at a third into a claimed construction. Inverse-polynomial statistical errors are not negligible. They may only be accepted with an explicitly adequate advantage calculation and quantifiers.

**Evidence and experiments**

Maintain claims.json with identifiers, exact statements, dependencies, source/derivation/experiment/conjecture labels, critic, and current status. Preserve reviewed snapshots; changes to a hypothesis must propagate to all dependent claims. No consensus vote or numeric confidence score substitutes for evidence. The focused reviews are bounded mathematical checks, not formal proof certification or an autonomous theorem-proving goal.

Use at most two concurrent CPU experiments, default timeout 120 seconds; an explicitly allocated larger experiment may use at most 300 seconds and never exceed a task deadline. No GPU jobs, package-installation project, external compute, or large parameter sweep. Exact small finite rings can test deconvolution probabilities, full joint TV, conditional covariance, support/decoder attacks, and the shared-K correlations. For every experiment save code, parameters, seed, precision/tail bounds, runtime and failures. Include known failing binomial and correlated-error cases as controls when relevant. Small examples are diagnostics, not asymptotic evidence of hardness. Avoid experiments that only confirm an already elementary identity.

If all candidate families fail, complete a useful negative portfolio: exact obstruction, scope, minimal hypothesis that would need to change, and whether that change still admits the computational reduction. Do not start an unrelated broad disciplinary search to fill time.

**Deliverables**

Write only under the new launcher-designated run directory. Required outputs are final.md (about 1,500–2,500 words), target.md, dependencies.md, bridge.md, claims.json, sources.bib, sources-and-assumptions.md, parameter-table.md, multi-sample.md, rejected-or-deferred.md, progress.md, agents.json, experiments/registry.json, criticism/, reconciliation.md, and shutdown.json. Up to two candidate dossiers belong in candidates/. The final report must answer:

1. Is the conditional one-sample theorem correct, and under exactly which hypotheses?
2. Is any matching source distribution supported beyond asserting its hardness? Which attacks were checked?
3. Is there a nonempty common parameter regime for extraction, completion, source plausibility and the desired task?
4. What is established for multiple samples, and what remains missing?
5. Which one next mathematical question would most change the assessment?

Retain a partial final report throughout. If the clock interrupts work, identify the interrupted claim and its dependencies. Report neither a formal certificate nor a completed hardness theorem unless every necessary implication has actually been checked.

**Execution and confirmation**

The existing tested launcher now accepts this plan directory. Five hours means max_wall_seconds=18000. Its systemd service begins termination at 17990 seconds and allows a five-second forced-stop grace, so both fit within the cap. The timer covers local Codex managed agents and experiment descendants. No goal tools, scheduled recurring tasks, automatic restart, or resume; no contact with researchers or publication. Keep the sandbox-only profile and built-in public web tools. The installed tmux helper's host preflights and startup verification must run at actual launch.

`run-config.json` records the user's explicit confirmation for this package with launch_authorized=true. This is separate from the preceding run's authorization. The research clock starts at the new timed service entry, after host preflights.

**Starting sources**

Read the prior [C01 dossier](../runs/brlwe-explore-20260906-astra-ultra/candidates/C01.md), [source checks](../runs/brlwe-explore-20260906-astra-ultra/candidates/C01/source-checks.md), [completion obstruction](../runs/brlwe-explore-20260906-astra-ultra/criticism/C01/additive-obstruction.md), [C03 noise comparison](../runs/brlwe-explore-20260906-astra-ultra/candidates/C03/transport.md), and [reconciliation](../runs/brlwe-explore-20260906-astra-ultra/reconciliation.md). Recheck every load-bearing claim in the primary source.

Primary search anchors: [Breuillard–Varju affine walks](https://arxiv.org/abs/1909.09053), [Order-LWE and entropic secrets, Section 7](https://eprint.iacr.org/2018/494), [ideal-SVP and partial Vandermonde knapsack](https://eprint.iacr.org/2022/709), the two original PDFs in literature/, and the locally saved ring leftover-hash manuscript. The search should explicitly examine whether the proposed paired/correlated source has appeared previously; do not claim novelty from a renamed distribution.
