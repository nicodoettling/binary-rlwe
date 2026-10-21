# Direct decision hardness for binary RLWE

Version 1, 21 October 2026. The user approved preparation and immediate launch of the preceding four-hour, three-total-agent Astra ultra Standard-tier proposal. This is a new bounded native-goal run. Historical runs and their unfinished goals are not resumed or relabeled.

## Objective

Establish a quantitatively useful reduction from ideal decoding to decision binary-secret RLWE, either directly or through an explicit intermediate oracle. The intended target is rank-one RLWE over the power-of-two cyclotomic ring, with one uniform coefficient-binary secret shared across polynomially many samples, uniform public multipliers and independent coefficient discrete-Gaussian errors. A positive result must specify a nonempty asymptotic parameter regime, supplied inputs, oracle access, success, cost and both distributional endpoints. Restrictions on the source ideal family must remain visible.

The full standard worst-case foundation is still open. A decision bridge on the inherited restricted ideal family would be valuable but would not establish arbitrary-ideal hardness. Negative outcomes must concern defined constructions or classes of transformations, not all possible reductions.

## Execution and schedule

- One coordinator and at most two active workers/referees, three total across all descendants. Every role uses `gpt-6-astra`, reasoning `ultra`, explicit `service_tier="default"`.
- Four-hour externally enforced cap from service activation, with no automatic restart, extension or successor. New native goal in the new coordinator thread, with no token budget. Only genuine achievement of the mathematical objective can complete the goal.
- Elapsed 0–45 minutes: exact interfaces, inherited coverage and first tests. The 45-minute checkpoint redirects allocation; absence of an immediate construction cannot authorize scientific early termination.
- Elapsed 45–165 minutes: constructive exploration, alternatives after failure, parameter checks and cross-examination. Investigate all three avenues below substantively.
- Elapsed 165–215 minutes: adversarial review and focused repairs. Discovery stops at 165 minutes, except targeted repairs and counterexamples needed to assess existing candidates.
- Elapsed 215–240 minutes: delivery. Workers and experiments stop by 225 minutes; final checkpoint by 235 minutes. Actual graceful shutdown and hard deadline come from the live cap sidecar.
- Checkpoint every ten minutes and after material findings. Small local experiments: default 120-second wall limit, maximum 300 seconds, at most two simultaneous and one heavy, at most 16 GiB address space per job, normally much smaller. The standard helper enforces aggregate elapsed time, not aggregate memory containment; no aggregate memory claim is made.
- Sandbox-only workspace writes and primary-source web reading. Research writes only in the new output directory. No Git mutation, publication, outside messages, installation, detached/remote computations, extra services or nested Codex sessions.

## Research avenues

### DD1: Decision gaps for the existing lossy construction — worker A

For a binary-RLWE distinguisher D define

    Delta_D(P) = E[D(A,A S+E)] - E[D(A,U)], A drawn from P,

where S is a fresh uniform coefficient-binary secret shared across the batch, E has the exact target product Gaussian law, and U is an independent uniform response vector. Both terms retain the SAME public-multiplier distribution P and metadata. The known decision advantage concerns uniform P. Investigate whether a useful separation can be proved for the fractional-Gaussian multiplier distribution, or whether explicit witnesses defeat this sufficient mechanism. Secret guessing bounds alone do not imply any such decision bound.

First test: reconstruct the precise completed joint law and try elementary linear/character/Fourier witnesses at valid parameters. If the naive statement fails, identify the surviving observable, conditional distribution or hybrid that might yield a weaker sufficient bridge. Failure of this statement is not permission to stop the entire run.

### DD2: Binary-compatible PRS17 sampling — worker B

Read PRS17 Section 6.1, especially Lemma 6.8 and the proof of Lemma 6.6, against the original model. Its uniform secret randomization hides the unknown target-induced secret, leaving a geometric error profile. Find an alternative mechanism preserving the exact binary promise or a rigorously transferable nearby promise, and retain a usable acceptance profile. Consider changes to the query construction, not just replacing the uniform mask by a binary mask.

First test: freeze all known and unknown variables in an explicit proposed transformation. Check the shared-secret law, public multiplier law, error independence and the profile's dependence on geometric distance. An unknown translate of the binary cube is not the target distribution. Charge dimension, degree, sample, modulus and noise changes. Continuous or elliptical errors are not the target discrete errors without a proved conversion.

### DD3: Weaker intermediate oracles and synthesis — coordinator

Identify the minimum decision information needed by decoding/hidden-center search. Seek an intermediate oracle, controlled hybrid, averaged profile or joint query law that can be obtained from binary decision advantage even when a full PRS17-style simulation is unavailable. Make a specific construction or falsifiable claim; names alone do not count as an avenue explored. Integrate DD1/DD2 failures into subsequent assignments. The existing hidden-center machinery is inherited work, not a new result to rediscover.

## Evidence and predecessor checks

The supplied `literature/2017-258.pdf` is PRS17, *Pseudorandomness of Ring-LWE for Any Ring and Modulus*, revised June 2020. It is available locally in full. The original two papers and `literature/2026-2443.pdf` are also local. Prefer precise source reading to another broad literature survey.

Use these relative roots:

- OLD: `exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/`
- RECENT: `exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/`

Read RECENT/final.md and programme-decisions.md for the current frontier. The root HANDOFF.md is historical and stale: it does not supersede October records. Trace inherited claims to exact statements and acceptance records before use:

- OLD/workers/RF4/same-j-composition/same-j-theorem-only-v1.md and interface-statements-v1.md; OLD/coordinator/samej-acceptance-v1.md.
- OLD/workers/A/fractional-composition/proof-v1.md: recovery test and full-law Gaussian completion; latent G and H are proof variables, not samplers supplied to the executable reduction.
- OLD/coordinator/c8-repair/multiplier-ohcp-theorem-v8.md, multiplier-ohcp-proof-v9.md and multiplier-ohcp-algorithm-v2.md: PRS17-inspired periodic-Gaussian decision-to-decoding machinery already present.
- OLD/workers/B/supersvp-mining/binary-fixed-secret-root-test-v1.md: provisional single selected CRT-coordinate result for decomposed inputs, not recovery of all coordinates or ordinary binary RLWE.
- RECENT/workers/B/theorem-only-v1.md and proof-v1.md; RECENT/coordinator/ab-acceptance-v1.md: full-observation cube-image guessing bound, not decision pseudorandomness.
- RECENT/regressions.json: all 164 inherited entries and their exact provenance remain part of the regression baseline. Import by reference or compact ID registry; do not make bulk archive copies. Record applicable/inapplicable/pending dispositions rather than silently dropping entries.
- The September one-pair conditional decision bridge assumes a distinct hidden-ideal source. It does not supply the present worst-case connection. Consult it only where a specific transfer might apply.

## Continuation and termination contract

The 45-minute checkpoint is nonterminal. A failed lemma closes only its exact statement; a failed sufficient inequality is not an impossibility result. Completing assignments, obtaining an auxiliary theorem, or finishing one referee wave does not terminate exploration.

Before the discovery cutoff, early scientific termination is exceptional and requires either (a) reviewed achievement of the stated mathematical objective with useful parameters, or (b) ALL of the following:

1. Each of DD1–DD3 has a substantive documented outcome: explicit calculation, construction attempt, counterexample or precise dependency, not a paragraph restating difficulty.
2. Each obstruction states its exact scope and potential escape routes. At least one materially different repair/alternative prompted by each initial failure has been attempted or ruled out by an explicit argument. This does not mandate repetitive variants.
3. A fresh nonauthor exhaustion reviewer challenges scope, proposes ways around the obstructions and checks that unused time cannot support a worthwhile concrete next test. Preserve its full input and report.
4. The coordinator evaluates every proposed escape with evidence and records why none is worth pursuing within remaining resources.
5. No promising unresolved candidate, pending worker/referee, or actionable repair remains. The early-stop certificate links all evidence and gives the exact elapsed time.

Lack of a construction after the first hour is not exhaustion. Inconclusive branches should trigger broader ideas within the objective. These rules are cooperative research controls; the external runtime cap is separate. Operational interruption or user stop is a separate termination category and must be reported honestly. If the native goal remains active after terminal delivery, do no new research outside the authorized phase/cap; do not falsify its status to make the process stop.

## Review and deliverables

Follow mathematical-proof-audit: freeze exact statements and joint laws; preserve rejected versions; invalidate descendants after changes; perform relevant finite-support falsification and conditional-law checks; obtain nonauthor full-proof/source/complexity review and at least one fresh blind referee before accepting a new main claim. Blind readers receive only statements, definitions, assumptions, permitted primary sources and boundary cases, not proposed proofs or prior verdicts. Repairs require fresh exact-version checks. Same-model agreement is correlated scrutiny, not formal verification.

Deliver in `exploration/runs/brlwe-direct-decision-20261021-astra-ultra/`: `final.md`, `claims.json`, `reconciliation.md`, `regressions.json`, `reduction-attempts.md`, `progress.md`, `resume.md`, `programme-decisions.md`, `gate-45m.md`, experiment provenance, complete review packets/reports, exact-version acceptance records, and startup/usage/shutdown evidence. The programme update must distinguish positive bridge, scoped obstruction, overlap with prior work, and inconclusive outcomes. Explain what each enables or retires and what exact next artifact would justify more work. No automatic successor.
