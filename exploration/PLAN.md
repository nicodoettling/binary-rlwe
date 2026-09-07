**A broad, time-limited exploration of binary-secret RLWE**

Status: launch authorized on 2026-09-06 with gpt-6-astra and ultra reasoning for all agents. Maximum duration: six hours from the run's start. This is an exploratory session with a finite work schedule, not a goal run. Actual launch and deadline status are recorded in the run directory.

The purpose is to discover mathematical structure that could support a new hardness argument. A useful outcome may be a reformulation, a falsified conjecture, an independently motivated assumption, or a small structural lemma. Establishing hardness is not a completion requirement. There is no quota of successful approaches.

**Three limited objectives**

1. Find substantially different mathematical descriptions of binary-secret rank-one RLWE, including descriptions imported from other fields.
2. Turn the most interesting descriptions into a few explicit mechanisms, missing lemmas, or discriminating experiments, with the connection to cryptographic hardness made clear.
3. Produce a compact portfolio of at most three developed directions, together with the strongest objections, discarded ideas, and the next question that would change our assessment of each direction.

Novelty is assessed by what mathematical step becomes possible, not by the vocabulary used. A sharper understanding of an old obstruction can count as progress. A familiar technique with a better bound can be retained if it changes the feasible regime.

**Reference problem and permitted variations**

The initial reference problem is search RLWE over

\[
R_q=\mathbb Z_q[X]/(X^n+1),\qquad
s=\sum_{j=0}^{n-1}s_jX^j,\quad s_j\overset{\$}{\leftarrow}\{0,1\},
\qquad (a_i,b_i=a_is+e_i).
\]

Here \(n\) is a growing power of two, \(a_i\) are independent uniform ring elements, and \(e_i\) have a specified discrete Gaussian distribution. Start with odd polynomial-size moduli and coefficient noise in a nontrivial small-noise regime; the baseline for exploration is \(\sigma=\operatorname{poly}(n)\) with \(q/\sigma\ge n^c\) for some fixed \(c>0\), and up to polynomially many ring samples. This is a starting comparison point, not a conjecture that every such parameter choice is hard.

Track ring degree, module rank, coefficient basis, modulus, error normalization, and sample count separately. Decision hardness is a valuable stronger outcome. Gaussian versus binary versus ternary versus sparse secrets must remain distinct. One ring sample provides structured scalar equations; rotations do not create independent samples.

Agents may investigate other rings, modulus regimes, bounded sample counts, or alternate priors when that exposes structure. Every such departure must be recorded together with what is needed to return to the reference target. Finite examples are diagnostics; fixed degree or noise approaching uniform modulo \(q\) is not a solution to the target problem. Use feasible splitting patterns: do not assume that an irreducible modulus polynomial exists in a power-of-two cyclotomic family when its factorization rules exclude it.

**Team and information flow**

Use one coordinator and at most three concurrent workers, matching the four available slots. The twelve scouting assignments below are logical roles run in four waves, not twelve simultaneous agents. Use gpt-6-astra with ultra reasoning for the coordinator and all workers, explicitly setting these options for each fresh worker context.

The coordinator maintains the clock, target contract, source index, and candidate inventory while workers explore. It also checks transformations and searches for accidental changes of problem.

Each scouting task starts in a fresh context. Six scouts initially receive only the formal problem and their assignment; six also receive the literature barrier inventory. The former spend their first ten minutes developing a representation before checking prior work. All scouts see the baseline before submitting. They do not read one another's speculative notes during discovery. This reduces anchoring but does not make outputs statistically independent.

Workers do not spawn further workers. The coordinator controls the entire queue and gives each task a deadline and a private output directory. Later stages explicitly exchange notes. Critics never review their own proposals.

**Scouting assignments**

These are starting questions, not assertions that a field already supplies the answer. A scout may replace its initial question with a better one, explaining the change.

| ID | Perspective | Concrete object or question | Useful first check |
|---|---|---|---|
| S01 | Statistical mechanics and planted constraint systems | Write the exact posterior on the Boolean cube using wrapped-Gaussian likelihoods. Examine overlaps, clusters, and conditional free energies under ring-structured disorder. Can interpolation or a planting construction yield a distribution comparison usable in a reduction? | Compare exact small-degree posterior statistics for ring samples and independent-matrix controls. Separate typical-instance, average-over-instances, and heuristic calculations. |
| S02 | Information theory and comparison of statistical experiments | Treat changing the secret prior as a channel-simulation problem. Seek an efficient randomized map between experiments, or a useful sufficiency/deficiency bound that preserves the target distribution. | Write an explicit simulator or prove why the natural candidate cannot exist. Distinguish Shannon information from guessing probability and computational indistinguishability. |
| S03 | Coding theory, shaping, and ring towers | Look for encodings, trace maps, or field extensions that trade ring degree or code structure for secret alphabet size while keeping a rank-one target. | Expand one proposed map coefficient by coefficient. Require a simulator that does not know the source secret and produces uniform multipliers over the full target ring, then check error correlations, recovery, and reduction direction. |
| S04 | Harmonic analysis and additive combinatorics | Study Fourier coefficients and concentration of binary polynomials under ring evaluation and reduction modulo ideals. Can an inverse theorem classify the multipliers or ideals causing bad behavior? | Compare full splitting with feasible low-splitting cases. Test a claimed bound on explicit exceptional ideals and binary differences. |
| S05 | Algebraic and arithmetic geometry | Translate multiplication, resultants, norms, and exceptional fibers into a precise arithmetic family. Can an efficiently sampled family have unusual Boolean fibers while retaining plausible pseudorandomness? | Produce a small explicit family and test its claimed fiber behavior. Check that dimension arguments actually give finite-ring counts and say something about binary points. |
| S06 | Geometry of numbers and discrete probability | Replace ambient lattice-index estimates by the actual intersections of lattice cosets with the Boolean cube. Identify when information loss is intrinsic and when it comes from giving the analyst excessive side information. | Count occupied cosets and fiber sizes exactly in a small unwrapped model, then check whether that model is justified by the real modular transcript. |
| S07 | Structured random matrices and universality | Study multiplication operators on directions relevant to binary differences, rather than only through global singular values. Can a comparison principle preserve enough ring dependence to be useful? | Find the first joint moment or correlation at which a proposed independent-matrix replacement fails. Track uniformity over all relevant differences versus a typical difference. |
| S08 | Dynamics, group actions, and exact sampling | Search for efficiently simulatable moves on secret/sample pairs that alter the prior in a controlled way. Explore Markov kernels, invariant measures, and symmetry beyond ordinary sample rerandomization. | Require a transition executable from public samples alone, and verify its transformed secret law, sample law, and noise. Dynamics that require the hidden secret are insufficient. A mixing claim must specify the stationary distribution and rate. |
| S09 | Computational algebra and restricted algorithm models | Use polynomial systems, elimination, low-degree methods, statistical queries, or sum-of-squares to locate structural differences between ring and ordinary LWE. | Exhibit a low-degree statistic or small algebraic attack that falsifies a proposed comparison. Clearly label lower bounds as applying only to the stated algorithm class. |
| S10 | Average-case complexity and alternative assumptions | Consider independently motivated source problems from planted models, coding, or arithmetic. Seek a real reduction arrow, not an assumption that restates binary RLWE. | State the source experiment independently and construct the first sampler/encoding. Account for planted versus uniform distributions and both directions of any claimed equivalence. |
| S11 | Open disciplinary search | Choose an area outside the main lattice/LWE literature, such as representation theory, quantum information, ergodic theory, or a field not listed here. Import one actual mathematical mechanism. | Supply a translation dictionary and a falsifiable question. A negative finding that the analogy has no mathematical content is acceptable. |
| S12 | Control: sharpen the existing obstruction | Revisit the strongest old framework without assuming it must fail. Identify the exact first inequality or simulation step that loses the binary regime. | Separate necessary loss from convenient upper bounds. Produce either a concrete improvement target or a counterexample to the proposed relaxation. |

Balance the waves so each contains different perspectives. One possible ordering is (S01,S05,S12), (S02,S04,S09), (S03,S07,S11), (S06,S08,S10). The coordinator may reorder for dependencies or source availability.

An elementary diagnostic for S06 is worth fixing in advance. For uniform \(S\) on \(\{0,1\}^n\), if its exact coset modulo an integer lattice \(L\) is disclosed, then

\[
\widetilde H_\infty(S\mid S\bmod L)
=n-\log_2 N_{\mathrm{occ}},\qquad
N_{\mathrm{occ}}=|\{s+L:s\in\{0,1\}^n\}|.
\]

Each occupied coset contributes \(2^{-n}\) to the optimal average guessing probability. This identity is a toy-model diagnostic, not a new hardness result. A modular transcript does not automatically disclose that coset, and the real adversary need not know a trapdoor that the proof analyst knows. The task is to determine which observation the reduction actually needs to expose.

**Six-hour schedule**

The absolute deadline is fixed before launching the coordinator. Phase boundaries are latest completion times and do not move when a task overruns. Advance early when a stage finishes; the timetable is not an instruction to wait or generate unnecessary work.

| Elapsed time | Work | Expected output |
|---|---|---|
| 0:00–0:15 | Establish the target, distribute context, initialize files and deadlines. | Target contract and task queue. |
| 0:15–2:15 | Four 30-minute waves of three fresh scouts. Reserve the last five minutes of each task for writing. | Up to twelve short scouting notes, including negative findings. |
| 2:15–2:30 | Compare mechanisms and choose up to three directions. | Selection reasons and a record of minority views. |
| 2:30–3:45 | Three deeper investigations, combining fields where a concrete connection exists. Small proofs, source checks, or experiments are allowed. | Mechanism sketches, exact missing steps, and initial probes. |
| 3:45–4:45 | Rotate authorship and attempt to falsify each direction. | Independent objections, counterexamples, or qualified survival. |
| 4:45–5:15 | Resolve the highest-value objections or retire the direction. | Revised dossiers and explicit unresolved issues. |
| 5:15–5:50 | Synthesis only; no new investigations. Workers finalize their notes. | Final report, comparison table, bibliography, and next questions. |
| 5:50–6:00 | Stop workers and experiments; finalize status. Forced termination backstop is at 6:00. | Complete or explicitly partial report; no continuing research. |

For a later choice of duration, rescale exploration and investigation, preserving a substantial synthesis/shutdown reserve. Do not increase concurrency to compensate. If all useful work finishes early, return early; do not manufacture activity to fill the clock.

**Selection and criticism**

Select for mathematical clarity, potential relevance, structural novelty, plausible assumptions, and ability to distinguish success from failure. Do not collapse these into a spurious numerical probability of success. Prefer different mechanisms over three variants of one idea. Reserve a place for an unconventional proposal when it has mathematical content, even if it has weaker initial evidence. Select fewer than three when appropriate.

A scout is not required to present a full reduction. By the deeper-investigation stage, each dossier must identify the relevant bridge: a reduction step, a structural lemma, a candidate source assumption, or evidence limited to a class of algorithms. A missing bridge is a result to record, not a gap to conceal. Classify proposed assumptions as established and independently studied, new but independently motivated and testable, or tailored to this construction. A restatement of binary-RLWE hardness is not a hardness explanation.

Each critic should find the most damaging objection, not write a generic checklist. Useful attacks include incorrect reduction direction, nonuniform public samples, illicit independence assumptions, coefficient/embedding confusion, a change of secret distribution, excessive sample requirements, vacuous noise parameters, or a source assumption equivalent to the desired conclusion. A known polynomial-time algorithm that contradicts the proposed regime outranks a suggestive numerical result.

Do not infer cryptographic hardness from posterior clustering, an algorithm's failure, low-degree evidence, or finite experiments. Conversely, do not reject a structural observation merely because its eventual cryptographic use is not yet known.

**Small experiments**

Choose experiments because their outcomes discriminate between hypotheses. For tiny rings, exact enumeration can measure fibers, posterior mass, likelihood ratios, and correlations. Use dense binary secrets as the reference, and clearly label sparse or ternary controls. Verify implemented multiplication and error normalization on hand-computable examples. Record seeds, parameters, code, and failed runs.

Default limit: at most two concurrent CPU experiments across the team, each with a two-minute timeout. Larger experiments require a concrete justification within the remaining stage budget; no experiment may outlive its task or the overall deadline. No GPU jobs or large infrastructure setup are part of this exploratory plan. A numerical threshold is evidence to investigate, not an asymptotic theorem.

**Evidence and outputs**

Use separate evidence labels: source-verified result; fully written small calculation; experiment; heuristic; conjecture; refuted; unresolved. Cite primary sources with theorem/section references where available. Record access failures rather than filling them from memory. Mark our deductions separately from the authors' claims.

Create one new run directory at launch:

```text
exploration/runs/<run-id>/
  run.json                 # actual start, deadline, phase, agent/session identifiers
  target.md
  progress.md
  scouts/S01.md ... S12.md
  candidates/C01.md ... C03.md
  criticism/C01.md ... C03.md
  experiments/
  sources.bib
  rejected-or-deferred.md
  final.md
```

The final report should be approximately 1,500–2,500 words, with links to supporting notes. It should contain the approach map, at most three developed directions, the strongest negative findings, and one concrete next test or lemma per retained direction. A report with no surviving candidates is acceptable. Preserve unsupported but interesting ideas in a clearly marked deferred section.

Checkpoint incrementally. The coordinator updates status after each wave and major task completion; there should already be a partial final report before synthesis begins. Agreement among agents is not mathematical evidence.

**Execution and hard termination**

Use ordinary Codex execution and bounded agent tasks. Do not call goal creation, goal update, or goal-resumption tools. Do not create a scheduled recurring task, continuation loop, or automatic restart. Finishing means delivering the finite exploration's report, not proving a theorem.

A prompt is not a reliable time limiter. At launch, a supervisor outside the research agent must record a monotonic start time, calculate the hard deadline, and own cancellation of all run-specific workers and subprocesses. The coordinator receives the corresponding UTC deadline and checks remaining time at task boundaries. Time spent waiting for tools counts toward the limit.

At 5:15 the coordinator enters synthesis. At 5:50 it stops delegated work and cancels remaining experiments. Termination grace must fit inside the six hours. At the deadline, the supervisor terminates any remaining run-owned process tree and records an interrupted/partial outcome if necessary. It must not stop unrelated sessions. Remote or managed agent sessions must have verified cancellation behavior; killing only a detached launcher is insufficient.

The bundled tmux helper supplies sandbox preflights, logging, and heartbeat monitoring. The local `runner/bounded_run.py` adds a systemd user service around the actual Codex runtime. Its runtime timer and forced shutdown cover the entire service cgroup, including local managed agents and detached experiment descendants. Runtime expiration occurs ten seconds before the advertised cap, with a five-second forced-shutdown grace. Remote execution and independent background worker services are prohibited. Verification evidence is saved under `runner/verification/`; research launch requires verified mock and managed-agent cancellation tests. Each run has a launcher-owned `run.json`, a `deadline-status.json`, and helper status/log files.

Official documentation supports ordinary scripted execution and bounded delegation patterns: [non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents). The four-agent limit comes from this session's available capacity. Any future launch must also follow the installed runner's required sandbox/preflight workflow.

**Starting material**

Read the supplied papers `literature/2020-119.pdf` and `literature/2020-1185.pdf`, the [literature review](../literature/reading-notes-2026-09-05.md), and the [bibliography](../literature/related.bib). The local 2026 manuscripts are under `literature/related/`. Use the review as an index and verify any technical claim that a proposed mechanism depends on in the primary paper.

The initial barrier inventory is intentionally small: ordinary lossy-matrix arguments spend a lower-dimensional projection; the ring short-basis argument spends information about lattice cosets; binary Module-LWE reductions increase module rank; information-theoretic phenomena and computational hardness require separate arguments. These are questions to interrogate, not axioms constraining all future approaches.
