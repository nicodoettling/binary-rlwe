# Maintenance and retrieval

## Initial consolidation

1. Read project authority files and note local formats, model boundaries, and
   preservation requirements. Inventory current filesystem sources, not only
   committed files. Preserve the discovery snapshot and its explicit policy.
2. Triage by research family. Read summary/handoff/final graph material and trace
   material claims to exact statements and effective verdicts. Keep a read
   register distinguishing whole documents, selected sections, and indirect
   references. Expand discovery if a read source points to a missing family.
3. Reconcile records, dependencies, invalidations, and branch dispositions.
   Preserve conflicting source statuses and expose missing adjudications.
4. Write the current-frontier narrative and evidence-linked views. Challenge
   priorities against older notes before settling the shortlist. A historical
   overlap can turn a proposed new theorem into an audit target.
5. Check navigation and tooling, freeze unresolved gaps, and deliver a receipt
   describing coverage and the actual review depth.

For a bounded task, prioritize the high-impact frontier and mark the remaining
archive pending. Finishing a documentation task does not settle its research
question. Do not claim exhaustive consolidation when only final reports were read.

## Incremental update

Start with the existing validation/freshness commands and relevant map IDs.
Review both changed canonical evidence and newly discovered sources. Produce a
small delta using [the template](../assets/delta-template.json); a whole-map
reconsolidation is unnecessary for an ordinary update.

Reconcile exact claim/version changes, current verdicts, model guards, and
historical conflicts. Identify all affected downstream claims and consult full
source graphs where the catalogue groups microlemmas. Keep new proof proposals
unreviewed until an appropriate separate review occurs. Documentation can
incorporate a prior exact verdict without creating a new mathematical verdict.

Edit canonical fields first, then regenerate dependent views. Update the human
entry point when the frontier changes. Re-evaluate active targets and retire
completed/redundant targets with linked reasons. Preserve the previous version
and change rationale in the integration record.

Compare a candidate discovery inventory to the reviewed baseline before
replacing it. Record dispositions for new, changed, and missing relevant files.
Acknowledging an unread source requires visible pending coverage. Accepting a
new discovery baseline must not update canonical evidence hashes or claim
statuses. Change a canonical fingerprint only after reviewing that exact version
and documenting its impact; a passing hash check is not recertification.

## Inventory policy

Persist included roots, file categories, explicit exclusions and their reasons,
symlink policy, hash method, and baseline-review provenance. Include research
source code, formalization source, PDFs, notes, and report/graph metadata when
relevant. Prune dependencies, build caches, and generated map views appropriately.
Do not broaden exclusions silently as the archive grows.

Separate volatile operational telemetry from research evidence. Logs may be
indexed by path/size/mtime for targeted provenance searches instead of making
every append a freshness failure. A file explicitly cited as canonical evidence
still receives content checks even if its general category is excluded.
If reasoning exists only in a transcript, catalogue that transcript or freeze
the relevant extract with provenance; do not discard it as telemetry. Symlinks
need a stated traversal policy that avoids cycles and hidden external sources.

Record Git HEAD/status as supplementary context. Externally stored logs or
transcripts need explicit access and scope; do not claim to have inspected them
because local metadata names their sessions.

## Tooling contract

When the archive warrants automation, use the project's language and existing
parsers; a standard-library script is often enough. Suggested commands are
`validate`, `check-freshness`, `render`, `render --check`, `find`, and `inventory`.
The names are illustrative. Define actual commands in the project's protocol.

- Validation checks schema, unique IDs/aliases, typed edges, logical cycles,
  exact evidence existence/content, scope fields, links/anchors, coverage, and
  accepted claims with unsupported or invalidated prerequisites.
- Freshness compares current discoveries with a reviewed baseline and reports
  new/changed/missing sources and affected claims without rewriting statuses.
- Rendering is deterministic from canonical data. Keep mutable rankings and
  coverage exceptions in that data rather than hard-coded in the renderer.
- Inventory writes a candidate snapshot by default; replacing an existing
  baseline requires an explicit review note or equivalent reviewed transaction.
- Find supports claim IDs, aliases, model restrictions, methods, and failures.
  Retrieval must expose source evidence, not just the generated summary.

Do not provide an automatic evidence-hash refresh that conceals drift. Test new
tool behavior in temporary fixtures: changed/deleted evidence; a new source in
an old family; a completely new family; a newly invalidated prerequisite and
transitive descendants; logical cycles versus harmless historical cycles;
missing guards; stale generated views; broken local anchors; harmless log growth.
Checks should fail for the intended reason and leave original research intact.

## Retrieval and priority challenge

Use questions with source-checkable answers. Examples:

- What is the strongest surviving claim for the general model, and its guards?
- Which extra restriction enables the closest stronger result?
- Where does the intended full conclusion depend on an unproved step?
- Which exact counterexample defeats that step, and what does it not refute?
- Is the proposed next extension already covered by an older exact claim?
- Which artifacts are only summary-traced or have unresolved review conflicts?
- What first test could discriminate the leading new mechanism?
- What changed since the last integration, and which descendants were rechecked?

Aim for answers reachable in a few links, often at most three, without hiding
important qualifications. Test truth against exact sources as well as ease of
navigation. Preserve initial failures and corrections rather than reporting only
the final successful answers. If a separate reviewer is authorized, give them
the map and sources without the intended answers; record disclosure before
describing the check as blind or independent.

## Completion receipt

Name the integration date, source delta, reviewed artifacts/versions, changed
statuses, descendant dispositions, priority changes, exclusions, unread sources,
and validation commands/results. State what was not independently rechecked.
Distinguish documentary maintenance from proof review, experimental reproduction,
and formalization checking. A complete map can honestly contain unresolved claims
and pending coverage if these limits are explicit and usable.
