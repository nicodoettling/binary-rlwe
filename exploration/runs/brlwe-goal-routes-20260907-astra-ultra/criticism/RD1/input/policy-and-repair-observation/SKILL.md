---
name: mathematical-proof-audit
description: Run or review extended mathematical proof efforts that need adversarial counterexample search, dependency-aware referee reconciliation, and durable certification. Use for autonomous theorem-proving or proof-audit runs, especially with adaptive probability arguments; do not invoke for routine exposition or a small local calculation unless an audit is requested.
---

# Mathematical Proof Audit

## Objective

Drive a mathematical claim to one honest terminal state:

1. proved under an explicit frozen model and assumptions;
2. refuted by a checked counterexample; or
3. unresolved at a precisely isolated gap, with failed approaches and evidence preserved.

Partial progress, a promising repair, or completion of one referee wave is not a
terminal state. Do not polish an unresolved argument into theorem prose.

## Required Reading

Always read [references/audit-protocol.md](references/audit-protocol.md) before
organizing the run.

Also read
[references/probability-regressions.md](references/probability-regressions.md)
whenever a claim uses conditioning, adaptivity, posterior sampling, sequential
events, transcript exposure, caching, stopping, union/product bounds, or a
change of measure. Run its cached-prefix regression whenever a proof multiplies
per-stage bounds or argues that local independence survives sequential
conditioning.

Import every counterexample and failed lemma already recorded by the project.
Treat them as mandatory regression tests, not historical commentary.

## Non-Negotiable Gates

- Freeze the exact theorem, model, quantifier order, success notion, resource
  measure, and assumptions before auditing the proof.
- Maintain a dependency graph from foundational lemmas to the final theorem.
  Changing or replacing a lemma immediately reopens every downstream claim.
- Never infer a sequential product bound from marginal bounds. Supply an
  explicit filtration and conditional estimate, a valid change-of-measure
  calculation, or a supermartingale/charging invariant that survives support
  restriction and normalization.
- For every probabilistic lemma, search finite-support models for a
  counterexample before certification. Prefer exact rational enumeration,
  SAT/SMT, linear programming, or exhaustive scripts over random testing when
  feasible. A bounded negative search is evidence, not a proof.
- Give at least one blind referee only the frozen theorem, definitions,
  assumptions, and permitted source material. Withhold the proposed proof,
  claimed status, coordinator summary, and suspected failure.
- Preserve complete referee reports and their inputs. Coordinator summaries do
  not replace raw reports.
- Treat separate agents using the same model and context lineage as correlated
  reviewers. Report agreement as repeated review, not independent statistical
  confirmation.
- A repaired claim remains `REPAIRED-PENDING-RECHECK` until a fresh reviewer
  checks the edited statement and proof against all old counterexamples and at
  least one newly targeted search.
- Permit final `ACCEPT` only after the claim graph is closed, all regressions
  pass, constants and quantifiers are rechecked, and the generated artifact is
  verified from a clean state.

## Coordination

The coordinator owns the claim graph, ledger, integration, and final verdict.
Use separate roles for constructive proof, red-team falsification, finite-model
search, probability/quantifier checking, and blind review. Recycle completed
agent slots and feed concrete failed attempts and counterexamples into later
work, while preserving blindness where required.

Do not let multiple agents silently rewrite the same proof. Ask reviewers for
claim-addressed reports, exact counterexamples, or replacement lemmas; the
coordinator reconciles them into the canonical artifact.

## Durable Outputs

Follow existing project conventions when present. Otherwise keep:

- an append-only audit ledger with claim IDs, dependencies, statuses, evidence,
  and invalidations;
- complete referee reports, including the material each referee received;
- a regression registry containing executable fixtures or exact finite models;
- the canonical proof or counterexample; and
- a final scope statement listing assumptions, exclusions, residual risks, and
  verification commands.

Do not erase rejected approaches after a repair. Mark them superseded and retain
why they failed so later revisions cannot reintroduce them.

