# Long-Run Mathematical Audit Protocol

Use this protocol to organize a proof-producing or proof-auditing run. Adapt
the number of workers and artifact paths to the project, but preserve the
certification gates.

## 1. Freeze the target

Write a frozen claim block before proving anything. It must state:

- the theorem in full, including finite and asymptotic forms;
- all objects, probability spaces, and algorithmic models;
- quantifier order and which choices may be adaptive;
- correctness, success, and adversarial notions;
- resource accounting and worst-case versus expected bounds;
- all effectiveness, finiteness, uniformity, and representation assumptions;
- intended examples, boundary cases, and explicit exclusions; and
- authoritative inputs in precedence order.

Assign the block an immutable version such as `T0`. A later theorem change is
`T1`, not an unnoticed edit. Record whether it strengthens, weakens, or merely
clarifies the claim.

## 2. Build the claim graph

Give every load-bearing statement an ID. Record at least:

| Field | Meaning |
|---|---|
| ID | Stable claim identifier |
| Statement | Exact statement, not a nickname |
| Dependencies | Other claim IDs and external results |
| Assumptions | Model hypotheses used locally |
| Status | One status from the list below |
| Evidence | Proof location, computation, or counterexample |
| Regressions | Tests that this claim must pass |
| Downstream | Claims invalidated if this one changes |
| Reviewer | Who checked which version with what inputs |

Use these statuses consistently:

- `OPEN`: no accepted argument.
- `PROVISIONAL`: candidate argument, not adversarially checked.
- `REJECTED`: false statement or invalid proof step.
- `REPAIRED-PENDING-RECHECK`: edited after a rejection.
- `ACCEPTED`: exact current version passed all required gates.
- `BLOCKED`: a precisely stated unresolved obligation prevents progress.

The final theorem cannot be more certified than its weakest dependency.

## 3. Preserve a regression registry

At intake, collect every historical counterexample, failed construction,
quantifier objection, bad parameter regime, and edge case. Give each a stable
ID and record:

- exact assumptions and finite data;
- the claim version it falsified;
- the expected outcome;
- a hand calculation and, where feasible, executable reproduction;
- which replacement claims must still reject or survive it; and
- provenance to the complete report that discovered it.

Never delete a regression because a lemma was replaced. Mark which versions it
rejects and why the current version survives. New failures are appended before
repair work begins.

## 4. Run complementary work streams

Use roles with different objectives. Suitable roles include:

- **Constructive prover:** derive the strongest valid statement and expose
  every assumption used.
- **Red team:** try to falsify statements, starting with small finite models,
  degenerate cases, and adversarial quantifier orders.
- **Finite-model builder:** encode assumptions and the negated conclusion using
  exact enumeration, SAT/SMT, LP, or symbolic algebra.
- **Probability and filtration auditor:** reconstruct every conditioning step,
  likelihood ratio, stopping argument, and product/union bound.
- **Quantifier and complexity auditor:** check uniformity, adaptivity, worst-case
  accounting, constants, and asymptotic substitutions.
- **Literature referee:** verify imported theorems against primary sources and
  check that their hypotheses match the frozen model.
- **Blind referee:** work from the theorem and definitions without seeing the
  proposed proof or its claimed status.
- **Delivery auditor:** compare the final artifact with the accepted claim graph
  and rerun build, consistency, and regression checks from a clean state.

Agents sharing a model, parent context, or coordinator summary are correlated.
Use role diversity and withheld context to reduce common-mode error, but never
describe agreement as statistically independent evidence unless independence
was actually engineered and justified.

## 5. Blind-referee protocol

At least one referee receives only:

1. the frozen theorem and definitions;
2. explicit model assumptions and allowed primary sources;
3. boundary examples that any valid theorem must classify; and
4. a request to prove, refute, or isolate the minimal missing hypothesis.

Do not reveal the candidate proof, suspected bug, previous verdicts, coordinator
confidence, or desired outcome. Preserve the complete prompt and report. After
the blind report is frozen, compare its proof obligations and attack ideas with
the canonical argument.

## 6. Probabilistic-lemma gate

For each probabilistic lemma:

1. Name every random variable and its joint law.
2. State which event is measurable in which filtration.
3. Write the exact conditional law after each revealed value or selected event.
4. Track normalization, support loss, likelihood ratios, and zero-probability
   branches.
5. Distinguish information physically available to an algorithm from
   information admitted to the proof filtration.
6. Justify adaptive scheduling, stopping, cache reuse, and repeated samples.
7. Replace every informal multiplication by a pointwise conditional bound or a
   proved potential/charging argument.
8. Run a finite-support falsification search as described in
   [probability-regressions.md](probability-regressions.md).

A calculation under the original marginal law does not certify the same bound
under a selected or posterior branch.

## 7. Repair and invalidation protocol

When a flaw is found:

1. Mark the exact claim `REJECTED` before drafting a fix.
2. Record the smallest counterexample or invalid implication in full.
3. Traverse the dependency graph and reopen every downstream claim, theorem,
   optimization, calibration, and exposition statement.
4. State whether the theorem is false, needs a new assumption, or may survive
   through a replacement lemma.
5. Give the replacement a new version and status
   `REPAIRED-PENDING-RECHECK`.
6. Rerun all historical regressions plus a search targeted at the new invariant.
7. Send the exact edited proof, not a summary of it, to a fresh adversarial
   reviewer.
8. Recompute constants, resource bounds, and asymptotics from the repaired
   finite statement.

Do not inherit an earlier `ACCEPT` through a changed dependency.

## 8. Coordinator learning loop

After each wave, update a short frontier record:

- what was attempted;
- the exact point of failure or success;
- which assumptions were unexpectedly necessary;
- new counterexamples and regressions;
- disagreements between roles;
- claims reopened or closed; and
- the next tests selected because of those results.

Later agent prompts should include relevant failures and artifacts, not merely a
coordinator conclusion. Preserve blind-review isolation by omitting prior work
from the designated blind thread.

## 9. Acceptance checklist

Final `ACCEPT` requires all of the following:

- The frozen theorem and model match the final artifact.
- Every dependency is `ACCEPTED` in its current version.
- Every probabilistic lemma passed its filtration audit and finite-support
  counterexample search.
- Every historical and newly discovered regression has the expected outcome.
- At least one blind referee report is complete.
- Every repair was freshly rechecked; no verdict predates its dependency.
- Imported results were checked against authoritative sources.
- Constants, edge cases, query/runtime bounds, and asymptotics were recomputed.
- Complete reports and exact test commands are durable project artifacts.
- The final document or code builds and passes checks from a clean state.
- Scope restrictions and residual risks are plainly stated.

If any item fails, report `PROVISIONAL`, `REJECTED`, or `BLOCKED`; do not use
paper-style language that implies certification.

## 10. Stopping rule

Continue through new proof attempts, counterexample searches, and repair waves
until one of these occurs:

- the acceptance checklist closes;
- a checked counterexample refutes the target;
- the target is reduced to an explicit open lemma and no remaining in-scope
  method makes progress; or
- an externally imposed budget ends, in which case write a checkpoint and leave
  all unresolved claims non-accepted.

Do not stop solely because some progress was made, a draft was produced, a
referee reconciliation occurred, or the current subagents terminated.

