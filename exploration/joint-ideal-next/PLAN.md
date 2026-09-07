# Proposed five-hour investigation: computational foundations of the noisy-ideal source

**Status: launched and verified healthy on 2026-09-06 at 19:54 UTC; hard deadline 2026-09-07 at 00:54 UTC.** This is a new finite research run, using the consolidated earlier work as evidence. It is not a resume of the interrupted session, a goal run, or a commitment to prove a theorem. Model: `gpt-6-astra`, reasoning: `ultra`, coordinator plus at most three active workers. The maximum duration is five hours, including review, synthesis, and shutdown.

## What the earlier work gives us

The [consolidated report](../consolidated/joint-ideal-20260906/CONSOLIDATED.md), [claim ledger](../consolidated/joint-ideal-20260906/claims.json), and [review reconciliation](../consolidated/joint-ideal-20260906/reconciliation.md) supersede the interrupted run's partial summary for purposes of this plan. Original proofs, reviews, corrections, and logs remain unchanged. Reviewed mathematical statements retain their actual certification limits.

The conditional one-sample reduction bounds target distinguishing advantage by two source distinguishing advantages plus extraction and noise errors. A2 supplies a common asymptotic analytic regime with binary coefficient secrets, polynomial split prime modulus, quotient dimension approximately sqrt(n)/log^4(n), and a specific noise-completion law depending on the hidden perturbation F. This establishes neither pseudorandomness of that source nor hardness of binary RLWE under a separately supported assumption.

The exact source assumption P0-A2 is the principal open obligation. Its first marginal has a reviewed deterministic exp(O(d)) times polynomial-time distinguisher, which is subexponential but superpolynomial at A2's dimension. The independent public-shear candidate is retired only within the proved negligible-error completion scope. Multiple target samples require a common-K source experiment and a full joint noise analysis; one-pair pseudorandomness does not supply them.

## Limited research objectives

1. Determine whether an independently specified, non-binary computational assumption supports A2's precise joint source, with an efficient public reduction and one common parameter regime.
2. Test the most consequential structural weaknesses of that source, or prove a scoped obstruction to a concrete proposed reduction. A failed attempt to find an algorithm is never counted as hardness evidence.
3. If the exact A2 law prevents progress, develop at most one substantive alternative public simulation or coupling, keeping its computational and statistical obligations together. Address multiple samples only after a credible single-source route or a clearly separate common-K assumption is identified.

The expected output is a decision about what to pursue next: a checked reduction, a checked counterexample or restricted impossibility result, or a precisely isolated open lemma with a record of failed approaches. There is no positive-result quota.

## Frozen baseline and intake

Read [SOURCE_CONTRACT.md](SOURCE_CONTRACT.md) and copy its exact baseline into the run's `target.md`. Retain all source conditioning, algorithmic inputs, and parameter bounds. Treat the consolidated claims as reviewed inputs with explicit limitations, rather than importing a blanket ACCEPT label.

The first twenty minutes are for checking the consolidated dependency graph, importing historical counterexamples into `regressions.json`, and recording the first actionable questions. Recheck the corrected finite guards on NC1 and the AN dependency of S0 before relying on them. Retain the supplied-public-CRT-roots condition in the generic ATT-v3 statement and the separate polynomial-q preprocessing argument for A2.

## Parallel questions

**W1 — Public reduction and hidden-noise dependence.** Start with an exact independently noised hidden-ideal source and the relevant HLBDD/Order-LWE and DSPR formulations. Can a public polynomial-time transformation produce the A2 challenge distribution, including active-unit U and the F-dependent canonical H_seq law, without learning the hidden perturbation F? State the challenge interface, both worlds, every source-oracle use, sampler accuracy, and advantage loss. If a proposed transformation fails, identify the exact missing capability. A restricted impossibility claim must first freeze its allowed transformation class; failure of the old independent shear does not exclude arbitrary public maps.

**W2 — Structural distinguishers and computational interpretation.** Begin with the corrected grouped-orbit algorithm and the exact first-marginal uniqueness argument. Examine whether the particular random-support distribution or the second component supplies a polynomial algorithm, a materially better runtime, or a reduction to a separately defined average-case ideal-decoding problem. Candidate tools include algebraic relations among CRT coordinates, structured decoding, and conditional dependence in the complete pair. A relabeling of P0 is not an independent foundation. Preserve the difference between information-theoretic identifiability, efficient computation, and subexponential computation.

**W3 — Alternative observable simulation.** Test whether a public-transcript comparison can discharge the bridge without requiring its stronger retained-latent-variable noise condition. Another option is a different publicly samplable auxiliary channel or source coupling with independently motivated computational support. Start from complete joint probability laws and derive a full replacement hybrid before claiming an improvement. Neither correctness of marginals nor a covariance calculation alone suffices. This stream may develop only one alternative to the frozen A2 candidate.

At the ninety-minute gate, rank the three streams by the specific implication still missing, and select at most two developed directions. If every route fails, use the remaining time to strengthen the most useful scoped obstruction or clarify the smallest remaining lemma. Do not reopen the old broad disciplinary survey merely to fill the clock.

Retire a proposed source transfer if it needs hidden F, J or challenger coins, silently changes the challenge law or parameter regime, assumes P0 itself, or leaves a nonnegligible error without an adequate finite-advantage theorem. Retiring that transfer is not an impossibility theorem about all reductions. A public polynomial-time distinguisher refutes P0 only after its advantage is proved for the exact A2 law. Larger-quotient extraction and unchanged-width sample expansion remain deferred unless a specific development result makes one necessary to the selected computational route.

## Timetable and review

| Elapsed time | Work and required artifact |
| --- | --- |
| 0:00–0:20 | Freeze baseline, imports, dependency graph, regression registry, and initial report. |
| 0:20–1:30 | W1–W3 in parallel; incorporate results and objections as they arrive. |
| 1:30–3:00 | Develop at most two candidates; keep a separate worker available for falsification and interface checks. |
| 3:00–4:00 | Fresh nonauthor reviews of frozen versions, including one blind review. Repairs immediately reopen downstream claims. |
| 4:00–4:30 | Recheck repairs and reconcile every material objection. Unchecked repairs remain pending. |
| 4:30–4:45 | Verify report against claim graph and saved evidence; complete final assessment. |
| 4:45–5:00 | Stop workers and experiments, save final checkpoint, verify shutdown. |

These are latest boundaries, not instructions to defer review or idle. Review each substantive result as soon as a slot is available. Record each review's exact input hashes. A blind reviewer receives the research scope, frozen statement, definitions, assumptions, boundary examples, and permitted primary sources, without the proposed proof or prior verdict. Same-model reviewers provide complementary checks, not statistically independent confirmation.

Multiple-sample work is conditional: at most one development slot may address it after the ninety-minute gate, and only if the coordinator records why it changes the source assessment. It must specify m, the common K, the joint H kernel, target width, modulus, and reduction cost. Do not claim unrestricted polynomial-sample hardness from a one-sample result.

## Continuous preservation and interruption handling

Every worker assignment includes the full [research scope](RESEARCH_SCOPE.md), exact inputs, permitted outputs, and UTC deadline. This includes blind assignments; the scope contains no proposed proof or verdict.

The coordinator updates `claims.json`, `reconciliation.md`, `progress.md`, `final.md`, and `agents.json` after each worker result or material objection and at least every five minutes when execution permits. It then runs:

```sh
python3 exploration/runner/bounded_run.py checkpoint --run-file /absolute/path/to/run.json --reason 'five-minute update or integrated result'
```

Each checkpoint records what changed, unresolved objections, invalidated descendants, and the next step. Workers save their own partial note every five minutes and before potentially long calls. A tool invocation that prevents a timely checkpoint is recorded as such; a filesystem copy is never represented as new mathematical progress.

The external supervisor polls every five seconds, takes preserved filesystem snapshots every five minutes, and reports a coordinator checkpoint older than ten minutes. It recognizes explicit error evidence separately from quoted research text. It writes local alerts and a final interruption manifest even when the research model cannot produce a response. It observes the coordinator session and worker sessions whose UUIDs are available in agents.json; canonical worker names alone do not identify their persisted sessions. Local alert/status files and the run log are the notification surfaces; automatic delivery to a closed chat or email is not promised. A confirmed content block observed by the supervisor stops the run; it is not automatically retried, rerouted, or resumed.

The systemd timer remains independent of the research process: termination begins at 17,990 seconds with five seconds of forced-stop grace inside the 18,000-second cap. The run has no automatic restart, goal, recurring task, or continuation. Host sandbox and process-containment preflights will be performed only after launch approval. The launch request does not change the existing sandbox-only permission profile.

## Experiments, evidence, and deliverables

Use public primary sources and installed local tools. At most two CPU experiments may run concurrently; default timeout 120 seconds, maximum 300 seconds, also bounded by the task deadline. Prefer exact small finite models for probabilistic counterexamples. Preserve code, parameters, precision or tail bounds, seeds when applicable, and negative results. Import historical controls before testing revised claims. Apply the cached-prefix regression when any new argument multiplies sequential conditional probabilities.

Write research only into the new run directory. Required outputs are `final.md`, `target.md`, `claims.json`, `claim-history.jsonl`, `dependencies.md`, `reconciliation.md`, `regressions.json`, `parameter-table.md`, `source-comparison.md`, `progress.md`, `agents.json`, complete `criticism/` packets, and `experiments/registry.json`. Up to two `candidates/` dossiers may be developed. The supervisor owns runtime status, snapshots, checkpoint receipts, alerts, and the exit manifest; the coordinator separately writes its mathematical `shutdown.json`.

The final report answers: what supports the exact source premise; which public reductions work or fail and why; whether any efficient distinguisher was obtained; whether one common regime survives; what changed about the multiple-sample question; and the single next question most likely to change the assessment. Every open assumption remains visible. Scientific completeness and successful process exit are recorded separately.

## Approval

The user approved this concrete package with “please go ahead and start the run”. The configuration records `launch_authorized=true`, `launch_confirmation_received=true`, the exact approval, and its UTC recording time. Host preflights and startup verification passed for brlwe-joint-foundations-20260906-astra-ultra; exact timestamps and session identification are in launch-receipt.json. This authorization is separate from the earlier interrupted run.
