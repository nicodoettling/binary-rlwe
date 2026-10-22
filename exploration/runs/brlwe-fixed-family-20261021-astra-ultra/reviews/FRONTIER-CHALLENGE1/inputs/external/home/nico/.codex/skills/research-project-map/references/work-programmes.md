# Adaptive work programmes

Read this for programme design, revision, or an explicitly authorized run-outcome
reconciliation. Ordinary mapping and single-target advice do not require a
programme. A programme selects the next informative investigation; it does not
predict that a particular proof route will succeed.

## Keep evidence and planning separate

The map is the central evidence hub. Exact statements and scoped adjudications
remain authoritative. Programme cards link map IDs and frozen source versions
instead of duplicating theorem statuses or proof text. A programme is not a
second results catalogue.

Suggested files, adapted to existing local layout:

- `PROGRAMME.md`: objective, boundaries, small milestone portfolio and routing.
- `PROGRAMME_DECISIONS.md`: append-only decision/outcome receipts.
- Existing target/brief metadata: current recommendations and proposed runs,
  reconciled with the programme rather than ranked independently.

Use [the programme template](../assets/programme-template.md) and
[receipt template](../assets/outcome-receipt-template.md). A compact project
may keep these sections in one file. Do not require a JSON catalogue, new
automation, or a separate planning run merely because this mode is used.

Planning status, mathematical status and process/native-goal status are separate.
Reuse local vocabulary. A useful planning set is `planned`, `active`, `achieved`,
`falsified`, `inconclusive`, `blocked`, `retired`. Define the deliverable that
each status refers to. `HOLD` is an action: allocate no repeat while awaiting
a named entry artifact or decision. A failed sufficient mechanism does not
falsify the main question. A completed documentation task can report open math.

## Design milestones around decisions

Start from the map's strongest exact frontier, known failures and unresolved
dependencies. Identify the central missing implication and competing routes.
Do not convert every open lemma into an automatic next task.

For each selected milestone record:

- Stable ID/version, exact obligation and finite/asymptotic model boundaries.
- Reviewed prerequisites, open dependencies and relevant regressions.
- Scope or capability gained, nearest predecessor and strongest obstruction.
- First discriminating test and evidence required before deeper allocation.
- Complete deliverable, review depth, proposed effort/team and uncertainty.
- Positive, negative, overlap, inconclusive and interruption outcomes, with
  conditional next actions and a stop/hold rule.

Change the version when the target, assumptions or success criterion changes;
preserve the old card and outcome. A clarification must state whether it changes
scope. Do not retrospectively declare an old run to have achieved a new contract.

Rank by importance to the main problem, scope gained, genuine new ingredient,
cost of falsification, value of a negative outcome and usable existing tools.
Keep the active shortlist small, with reserves needing explicit entry artifacts.
Every route recommendation is conditional on that version still being eligible
and unexhausted. If all routes are exhausted, name what could reopen one; do
not cycle between failed proposals or invent an automatic escalation ladder.

## Admission before deep investment

Use a short gate when scope or novelty could make the rest of the run wasteful.
Choose its duration and review margin for the task, not by a universal ratio.
The gate should ask:

1. Does an earlier exact result already cover the proposed statement?
2. Do all quantifiers, objects and operational interfaces match, including
   exceptional or malformed cases relevant to the conclusion?
3. Is the promised improvement nonvacuous in the intended resource regime?
4. Is there a concrete new identity, example, method or falsifiable test?

A restricted probability theorem is not yet an attack; an attack is not yet
a useful lower bound without matching success/resource calibration. Analogous
gaps arise between an abstract algorithm and a realizable implementation.
Make these bridges explicit milestones rather than silently inheriting them.
For example, an upper bound on attack cost does not demonstrate a family with
growing achieved security; unused padding does not establish new scope.

Passing a gate permits only the authorized in-scope work. Failing it should
produce a reviewed overlap/empty-regime/obstruction or precise inconclusive
receipt, not unrestricted exploration until the budget runs out. If the gate
is inconclusive, record the missing comparison instead of silently waiving it.

Do not enforce admission timing or new stop rules retroactively on a live run.
Budgets, agent counts and review allocations are proposals until authorized.

## Reconcile each authorized outcome

Read the latest receipt, exact artifacts, full reviews and handoff. Establish
what was proved, falsified, reproduced or only proposed; preserve disagreements
and check-depth limits. Shared-model referees are correlated reviewers.
If new proof work is needed, it is a separate authorized activity, not mapping.

Append an evidence-linked receipt before changing milestone state. Then
reconcile affected map records/dependencies, programme cards, rankings and
current briefs as one reviewed delta. Retain the old exact sources and their
claimed statuses. Evidence hash refresh is not adjudication.

The receipt names changed and unchanged dispositions, scope limits, budget
used, disabled next actions and any remaining integration work. An auxiliary
theorem stays achieved if its application fails. No new acceptance follows
from a milestone label. Recommend another branch only if its own prerequisites
are satisfied and it remains unexhausted; never launch it automatically.

An expired/interrupted run preserves a handoff labelled `integration pending`
when reconciliation is incomplete. Do not claim full delivery or reset its
cap. Resume requires separate authorization and a new explicit budget; start
from the last verified gate and exact version rather than repeating intake.

## Longrun contract without ordinary-session side effects

When requested, adapt [the contract](../assets/longrun-contract.md) into project
instructions and each authorized run prompt. It applies only to an explicitly
authorized autonomous run with its own durable prompt and manifest/deadline.
The marker alone cannot activate it or authorize execution. It is OFF for
normal Q&A, brainstorming, editing, coding, Git, launch preparation, status
checks and ordinary subagent use. A separate reconciliation request authorizes
only that bounded maintenance task. Foreground launch preparation does not
inherit the coordinator's delivery obligations.

Coordinator owns central integration; workers return evidence/reports rather
than concurrently editing shared planning files. Successful longrun delivery
requires the receipt and reviewed delta, or a precise incomplete handoff if
capped. This is an instruction-level contract, not a runner-enforced gate.
Neither contract nor recommendation grants Git, publication, billing or
successor-launch authority. Use specialized runner/audit procedures when
authorized and available; do not copy their operational details into this skill.

## Validate decisions, not just document shape

Check links/IDs/versions, prerequisite status, current briefs, branch eligibility
and agreement between map priorities and programme actions. Use existing tooling;
if automation is warranted, add isolated fixtures rather than silently exempting
old hardcoded checks. Structural validation cannot certify mathematics.

Exercise these decision cases against the actual programme:

- Positive auxiliary, failed application: preserve the auxiliary; no unsupported
  main result; name the failed bridge and independently eligible next action.
- Counterexample to a sufficient route: retire that version, not the conjecture.
- Proposed new result covered by old evidence: record overlap and redirect or hold.
- Inconclusive search: require a named new ingredient before another allocation.
- Two unavailable branches: hold for an entry artifact, not circular reruns.
- Changed prerequisite: review/reopen descendants and update dependent plans.
- Interrupted before integration: incomplete receipt/handoff, no full delivery.
- Ordinary edit/status request: no programme maintenance duties are activated.

Deliver an accessible programme, exact evidence-linked milestones, initial or
updated receipt, consistent shortlist/briefs and check-depth limits. State
whether launch authorization exists separately. Do not silently attach this
programme to a live run or migrate an established project into these templates.
