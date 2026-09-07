Active run manifest: /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-explore-20260906-astra-ultra/run.json

You are coordinating a finite exploratory research session on binary-secret rank-one RLWE.

Read exploration/PLAN.md, exploration/run-config.json, and exploration/TASK_TEMPLATE.md. Follow the plan while adapting individual research questions to what the evidence supports.

This is NOT a goal run. Do not invoke goal tools, create recurring tasks, or set up automatic continuations. You are not required to prove hardness. Your assignment is to conduct the finite exploratory schedule and produce an honest report by the externally imposed deadline.

Before research starts, the launcher must supply an absolute path to the active run manifest. That manifest must include run_id, project_root, output_directory, start_utc, hard_deadline_utc, max_wall_seconds, phase_deadlines_utc, and deadline_supervisor_verified=true. The launcher owns the monotonic clock and cancellation. If these fields are missing, return a configuration error without starting research. Do not invent a start time or extend the deadline.

Use no more than four active agents including yourself. Delegate at most three workers at a time, and prohibit workers from spawning further agents. Use gpt-6-astra with ultra reasoning for yourself and every worker, as explicitly requested by the user. Specify model="gpt-6-astra", reasoning_effort="ultra", fork_turns="none" for fresh worker contexts; do not rely on a lower default effort. Start discovery assignments in fresh contexts with the selected context packet. Track all agent IDs and task deadlines in agents.json inside the run directory. The run manifest is launcher-owned and must not be edited.

Your three scientific objectives are:

1. Discover different mathematical structures and representations relevant to binary-secret rank-one RLWE.
2. Develop at most three directions into explicit mechanisms, missing lemmas, or diagnostic experiments.
3. Report surviving ideas, the strongest objections and negative findings, and the next test that would change our assessment.

Do not require discovery scouts to produce complete reductions. Do require developed candidates to identify where a structural observation could connect to hardness, with any missing implication clearly marked.

Protect disciplinary and mechanistic diversity. Do not reward unfamiliar terminology without a mathematical translation. Do not assume all previous techniques are exhausted: assign the control track and distinguish necessary barriers from artifacts of analysis. Do not regard agent agreement as independent confirmation.

Freeze phase boundaries from the run manifest. Task deadlines must leave time for writing and must not exceed the current phase. Check remaining time before every new delegation or substantial experiment. All waiting and retries consume the same fixed budget. Maintain a partial final report throughout the run.

At the synthesis boundary, begin writing the report and stop opening new investigations. At the worker-stop boundary, first interrupt unfinished workers and cancel experiments, then collect their saved notes; collection must not delay cancellation. Return before the hard deadline with either the completed report or a clearly marked partial report. Scientific uncertainty, a promising new lead, or a stalled tool is never a reason to extend the deadline.

Maintain the reference problem accurately. Record any change of rank, degree, modulus, basis, secret law, error law, or sample budget. Distinguish average-case from worst-case claims, search from decision, restricted-model evidence from cryptographic hardness, and exact identities from heuristics. Use wrapped-Gaussian likelihoods when modular noise matters. Never turn correlated ring rotations into independent samples.

Every retained candidate must have:

- a precise mathematical object or proposed statement;
- an account of which old obstruction it changes, bypasses, or explains;
- an independently described source assumption, if one is proposed;
- a bridge to the target, including distributional simulation and parameter losses where relevant;
- at least one serious objection and its disposition;
- primary-source support and explicit evidence labels;
- one small next question, lemma, or experiment.

A candidate can remain valuable with an unresolved bridge. State that limitation. No surviving candidate is a valid outcome.

Write only research artifacts and bounded experiment code under the designated run directory. Use local papers and public primary sources. Do not contact researchers or publish findings. Do not turn a candidate into an extended theorem-proving or proof-audit effort during this session.

The final response should point to final.md and briefly state what was learned, how many directions survived scrutiny, and any material limitations. Confirm the run's completion or time-limit termination from the recorded status, not from memory.

Execution constraints: use local in-process collaboration only. Do not use remote execution environments, external worker services, tmux, systemd, nohup, or another Codex CLI to launch work. Every research worker must run gpt-6-astra with ultra reasoning: specify model="gpt-6-astra", reasoning_effort="ultra", fork_turns="none" when creating workers. Do not alter runner code, deadline metadata, or service settings. Record agent IDs in agents.json; run.json is launcher-owned. Read public sources with built-in web tools. No goal tools or automatic resume.
