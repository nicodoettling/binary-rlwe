Active run manifest: /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/run.json

Coordinate the user-approved finite investigation defined by exploration/joint-ideal-next/PLAN.md, SOURCE_CONTRACT.md, RESEARCH_SCOPE.md, TASK_TEMPLATE.md, and run-config.json. The launcher supplies the absolute active run-manifest path. Before research, verify its specific launch authorization, output_directory, UTC phase deadlines, finite hard deadline, and verified supervisor. Do not infer approval from earlier runs or this prepared package.

Use gpt-6-astra with ultra reasoning for every research agent. At most three workers may be active alongside you, with no grandchildren. For a fresh worker use model="gpt-6-astra", reasoning_effort="ultra", fork_turns="none". If agent capacity is temporarily unavailable, integrate evidence and work locally; do not treat a thread limit as completion. Every task has an exact UTC deadline and output path.

Read the full RESEARCH_SCOPE.md and include it verbatim in EVERY worker assignment, including blind review. Its academic context remains explicit even for a narrow algebraic subproblem. Attach the correct mathematical input packet for that role. Blind reviewers receive the scope and frozen mathematical model but no proposed proof, prior verdict, or coordinator assessment.

Read the consolidated prior report, current claim ledger and reconciliation, and import all historical regressions. Keep all old runs, consolidation, plans, literature and runner code read-only. Write research only under the launcher-designated new output directory. run.json and supervisor output files belong to the runner; register collaborators only in agents.json.

Focus on computational support for the exact correlated source P0-A2. The existing conditional bridge does not establish that premise. Follow W1 public reductions, W2 structural distinguishers, and W3 alternative observable simulation. At ninety minutes select at most two developed directions. Multiple-sample work needs a recorded gate decision, explicit m and common-K source; no tensorization from one pair. A clean negative result or precise remaining lemma is a valid bounded outcome.

Use the mathematical-proof-audit skill and its probability protocol. Version exact statements, assumptions and proofs. Maintain claims.json and append-only claim-history.jsonl with evidence, dependencies, critic input hashes and dispositions. A changed premise immediately reopens downstream claims. A repaired claim stays REPAIRED-PENDING-RECHECK until a fresh nonauthor reviews the exact edited proof against historical and newly targeted controls. Same-model agreement is complementary review, not statistical independence. Never certify an incomplete dependency graph.

Create initial target.md, claims.json, claim-history.jsonl, dependencies.md, reconciliation.md, regressions.json, progress.md, agents.json and partial final.md before dispatch. After each worker result, objection or material revision, integrate it into the claim graph and reconciliation immediately, then checkpoint. Also checkpoint at least every five minutes when execution permits. Include unfinished calculations and explain any delay due to a pending tool call. Do not wait until the final review phase to reconcile.

After updating claims.json, reconciliation.md, progress.md, final.md and agents.json, call the installed project helper:

    python3 exploration/runner/bounded_run.py checkpoint --run-file ABSOLUTE_ACTIVE_RUN_JSON --reason 'integrated result or five-minute update'

This checkpoint acknowledges written content; it does not certify a proof. The external monitor makes separate filesystem snapshots every five minutes, checks stale coordinator checkpoints after ten minutes, and surfaces process errors. Follow the helper README for runner-owned paths. Do not write, delete or edit runner snapshots or alerts yourself.

Keep every tool call and experiment inside its task deadline. Use public primary-source web tools and installed local software. At most two concurrent CPU experiments, 120 seconds by default and 300 seconds maximum. Save exact code/data/precision/parameters and seed where relevant. No packages, GPU project, external execution, independently launched services, publication, or communication with researchers.

The previous run's cybersecurity screening interruption was reported through the documented feedback channel. This plan supplies the genuine research context and preserves progress; it provides no guarantee against another content error. Do not arrange retries, model rerouting, automatic resume or continuation after any such block. Do not call goal tools or create recurring tasks.

Use phase boundaries as latest deadlines. Finish fresh review by hour four, repair rechecks by 4:30, and synthesis by 4:45. At workers_stop interrupt remaining agents and cancel experiments before collecting final saved notes. Write mathematical shutdown.json with remaining obligations and known process status. The independent supervisor records actual exit status separately. Exit early only when each assigned workstream and material objection has a recorded final disposition; unresolved work may remain explicitly open at the time cap.

The final report states what was proved or refuted, which computational premise remains unsupported, the exact shared parameter regime, how prior objections were handled, and one discriminating next question. Preserve partial status where required; neither a successful process exit nor completed critic reports imply a completed hardness theorem. End with links to final.md and the latest research ledger; do not claim an unobserved launcher exit.


# Research context carried into every assignment

This is academic theoretical cryptography research on the hardness of binary-secret Ring Learning with Errors (RLWE). The mathematical objective is to prove reductions between precisely specified probability distributions, identify necessary assumptions, or refute proposed statements by mathematical counterexamples. A cryptographic distinguisher or recovery algorithm in this project acts on a formally defined distribution of locally generated synthetic ring elements.

The methods are reading public research papers, algebraic and probabilistic reasoning, proof review, and bounded local numerical or exact finite-model experiments. The outputs are mathematical notes, complete reduction interfaces, parameter inequalities, counterexamples, and reproducible experiment records. No existing service, deployed cryptographic system, third-party ciphertext, credential, or external machine is a research target.

Keep the actual cryptographic objectives and terminology explicit. This scope supplies context; it is not evidence that a theorem holds or a guarantee against screening errors. The previous run ended with a recorded `cyber_policy` error, reported through Codex feedback. Any new content-policy interruption must be recorded and surfaced, with no automatic retry or continuation.

Every assignment retains the same bounded-run limits: Astra with ultra reasoning, assigned UTC deadline, local workspace output, no goal tools, no external workers, and no further agent spawning by workers. Public literature browsing is permitted. Experiments use installed tools and synthetic inputs within their allocated time.


Execution constraints: use local in-process collaboration only. Do not use remote execution environments, external worker services, tmux, systemd, nohup, or another Codex CLI to launch work. Every research worker must run gpt-6-astra with ultra reasoning: specify model="gpt-6-astra", reasoning_effort="ultra", fork_turns="none" when creating workers. Do not alter runner code, deadline metadata, or service settings. Record agent IDs and available session/thread UUIDs in agents.json; run.json is launcher-owned. After each worker result and every five minutes, update claims.json, reconciliation.md, progress.md, final.md and agents.json, then call python3 /home/nico/projects/research_projects/binaryRLWE/exploration/runner/bounded_run.py checkpoint --run-file /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/run.json --reason "describe the checkpoint update". Runner snapshots do not establish mathematical progress. Read public sources with built-in web tools. No goal tools or automatic resume.
