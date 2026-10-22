---
name: research-project-map
description: Create or maintain evidence-linked research maps and, when requested, adaptive work programmes with versioned milestones and outcome-driven priorities. Use to recover a project's frontier, prevent repeated failed approaches, and plan or reconcile a series of bounded investigations. Mapping and planning do not authorize new proofs, experiments, or background runs.
---

# Research Project Map and Work Programme

Build a map that lets a new researcher answer: What survives? Under which
assumptions? What failed, and why? Which exact obligation remains? What would
the next investigation add beyond work already done?

When a work programme is requested, also answer: Which bounded investigation
should run next? What decision can it change? What would each possible outcome
enable, retire, or leave on hold? The programme is an evidence-driven decision
process, not a presumed ladder of successful lemmas.

Use this for initial consolidation, bounded updates, and map-based preparation
for research. Follow existing project formats and authority rules. Read
[the record contract](references/record-contract.md) when defining or interpreting
records, and [maintenance and retrieval](references/maintenance-and-retrieval.md)
when establishing checks or integrating a delta. Templates in `assets/` are
starting points for a new project, not migrations for an existing map. Use
[the catalogue template](assets/catalogue-template.json) when a new structured
catalogue would help.

## Select the requested mode

- Map creation/update or a next-target shortlist: use the mapping workflow
  below. Do not create a programme or impose longrun obligations by default.
- Programme design/update or planning a series of investigations: additionally
  read [work programmes](references/work-programmes.md). Reuse the map as the
  evidence hub; maintain planning state separately from mathematical status.
- Completed-run reconciliation: perform the authorized bounded update. This
  does not authorize resuming research or launching a successor.

Read only the mode-specific references needed by the task. Existing project
authority, formats and explicit user choices take precedence over templates.

## Evidence and status discipline

- Exact statements, definitions, and scoped adjudications are authoritative.
  The map supplies navigation and interpretation. Preserve frozen historical
  artifacts and link later corrections separately.
- Record **source-claimed status**, **effective status**, and **this mapping's
  check depth** separately. An inherited acceptance must cite the exact reviewed
  version and verdict. A fresh catalogue entry or hash supplies no new acceptance.
- Discovery, reading, documentary reconciliation, mathematical review, experiment
  reproduction, and formal verification are different activities. State what
  was actually done. Same-model referee agreement is correlated review.
- Keep a refuted proof step, a failed attack, an insecure diagnostic example, a
  secure counterconstruction, and an open conjecture distinct. Failure of one
  sufficient mechanism does not refute its intended conclusion.
- Changed premises reopen dependent claims until a scoped recheck establishes
  that they survive. Preserve logical dependencies separately from supersession,
  refutation, scope containment, analogy, and historical influence.

## Establish scope

Read the project's current specification, model, notation, handoff, and existing
map/protocol first. Identify the motivating question, quantitative target,
success notion, allowed computation, resource measures, and significant model
variants. Keep distinct parameters distinct; avoid rewriting a claim in a
nominal parameter when the project measures an invariant quantity.

For a new map, agree with the available project context on what counts as source
material. For an update, identify relevant existing IDs, dependency graphs,
regressions, and validation/freshness commands before relying on the old map.
Preserve local exclusions and disclose their limits.

Mapping does not itself authorize a new theorem-proving run, experiment,
literature campaign, or tmux launch. Carry out such work when the user's task
includes it; otherwise record the needed audit or investigation as a target.
Programme design likewise supplies no launch, Git, publication or billing
authority. Use `codex-tmux-runner` for an authorized background launch and
`mathematical-proof-audit` for authorized proof work when those skills are
available; otherwise state the required separate procedure. Do not silently
substitute documentary checks for proof certification.

## Discover, then reconcile

Inventory the actual filesystem, including dirty and untracked research. Git
metadata supplements this inventory. Group sources into research families,
including manuscripts, discussion notes, experiments, formalizations, and
external literature. Do not rely solely on final reports or filenames.

Start from final summaries, handoffs, claim graphs, and referee reconciliations.
Trace central claims back to their exact statements, quantitative guards,
supporting lemmas, and later scoped verdicts. Search long historical notes for
buried predecessors and stronger claimed variants before declaring novelty or
ranking a new extension. A final-looking banner or recent date does not settle
an exact-version conflict. Preserve unresolved disagreements visibly.

Give every discovered family and every known graph branch a disposition:
mapped, grouped with a named record, superseded, refuted, or pending. Grouping
provides navigation, not blanket certification. Record unread material and
selected excerpts honestly. Prioritize deep tracing of claims that determine
the current frontier, invalidate other results, or alter research priorities.

## Build an accessible map

Keep one canonical representation of repeated claim/status/source fields. For
a large archive, prefer a structured catalogue with deterministic views; for a
small project, a single maintained Markdown table may suffice. Reuse existing
local tooling. Do not force the source project's schema or terminology onto a
different domain.

A useful default layout is:

- `PROJECT_MAP.md`: concise current frontier, main routes and their limitations,
  navigation, and maintenance commands.
- `notes/project-map/catalogue.json`: canonical versioned records and relations.
- `RESULTS.md` and `OBSTRUCTIONS.md`: evidence-linked claims and failed routes.
- `TARGETS.md`: a small ranked shortlist, reserves, and retired investigations.
- `COVERAGE.md`: discovery, reading depth, unresolved conflicts, and omissions.
- `UPDATE_PROTOCOL.md` and an inventory: repeatable checks and delta integration.

Write the human entry point around the problem, rather than the chronology of
runs. Show where each restricted result applies, what it excludes, and what
bridge would extend it. State the overall open status plainly. Make exact
sources reachable in a few links. Add a short AGENTS/HANDOFF pointer when useful;
keep detailed research status in the map rather than duplicating it there.

## Choose high-value targets

Rank by scope gained, importance to the main question, a genuinely new
ingredient, usable existing tools, cheap falsifiability, value of a negative
result, and likely effort. Recency, polish, and another technical sufficient
condition do not establish priority. When a promising extension appears
covered by a historical claim, reconcile that claim before proposing a duplicate
campaign. Distinguish an audit target from a new research target.

Keep the shortlist small; three active recommendations and a few reserves are
useful defaults, not fixed requirements. Each target needs an exact obligation,
nearest result and obstruction, substantive advance, first test, useful positive
and negative outcomes, stop/pivot condition, suggested effort, and uncertainty.
Preserve retirement reasons and historical IDs for completed or redundant work.
Retire or redirect associated launch briefs as well.

## Optional work programme

For a requested programme, convert selected map targets into versioned
milestones with exact prerequisites, first discriminating tests, positive/
negative/inconclusive branches, review and delivery criteria, proposed effort,
and stop or hold conditions. Check novelty, scope and useful parameter regimes
before allocating deep proof work. Separate an accepted auxiliary result from
its still-unproved application.

Use [the programme template](assets/programme-template.md) and
[outcome receipts](assets/outcome-receipt-template.md) as adaptable starting
points. Keep a short active portfolio rather than a speculative exhaustive
proof ladder. Reconcile outcomes with map dependencies and next-run briefs;
unchanged priorities need an explicit reason, not invented progress.

If requested, add a [longrun-only contract](assets/longrun-contract.md) to the
project's instructions and authorized run prompts. It is OFF in ordinary
sessions; being in tmux, using agents, or discussing research cannot activate
it. Keep run execution, proof review and programme maintenance distinct.

## Make maintenance reliable

For a substantial map, establish structural validation, discovery freshness,
deterministic rendering checks, and focused retrieval. Validate IDs/aliases,
typed relations, logical cycles, evidence paths/versions, required model fields,
dependency invalidations, branch coverage, and local links/anchors.

Check evidence content and discovery drift separately. A fresh inventory can
acknowledge an unread source; it cannot repair changed canonical evidence.
Hashes identify bytes, not truth. Review drift before accepting a new baseline;
never refresh evidence hashes merely to clear a failing check. Explicitly record
source exclusions, including how telemetry and build caches are handled.

Test new maintenance tooling with isolated fixtures for changed/deleted evidence,
new sources in old and new families, invalidated transitive prerequisites,
logical cycles versus historical links, stale views, and irrelevant log growth.
Describe tooling limits: structural checks do not verify formulas, review every
proof, rerun experiments, or build formalizations.

## Validate usability and deliver

Use realistic retrieval questions: strongest surviving general claim; exact
restricted scope; why a flagship argument failed; missing implication; nearest
predecessor of a proposed target; unresolved review conflict; and next test.
Check each answer against primary artifacts. A few-link retrieval target tests
navigation; it does not substitute for evidence review. Preserve failed retrieval
questions and resulting ranking corrections. If a separate reviewer is used,
record what they saw and avoid claiming independence beyond the actual setup.

Deliver the map or a small evidence-linked delta, a dated integration receipt,
verification results, and explicit check-depth/coverage limits. The receipt
names reviewed versions, affected descendants, unresolved disagreements, and
why priorities changed. Use [the delta template](assets/delta-template.json)
for updates. Explain what remains pending without promoting it to a result.
