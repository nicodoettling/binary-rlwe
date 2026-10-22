# Record contract

Adapt these fields to the project's domain and existing schema. The purpose is
to retain exact scope, evidence, and the distinction between historical claims
and current knowledge. An empty field is not evidence that no assumption exists.

## Claims

Use stable IDs and explicit versions. Do not silently replace a rejected claim
with an edited statement under the same version. Preserve aliases and old link
destinations when renaming. Separate an underlying mathematical claim from its
particular attempted proof when they have different effective statuses.

For every substantive record retain:

| Field | Meaning |
| --- | --- |
| `id`, `version`, `title`, `family` | Stable identity and provenance group. |
| `kind` | Theorem, conditional implication, auxiliary lemma, imported tool, construction, counterexample, failed method, model definition, open obligation, experiment, or formalization. |
| `claim` | Exact concise statement or precise pointer; include what is and is not concluded. |
| `model` | Objects, access/interfaces, restrictions, distributions, computational allowance, and experiment. |
| `parameters`, `guards` | Distinct resources, quantifiers, ranges, asymptotic regime, correctness/success thresholds, and endpoint cases. |
| `assumptions`, `open_obligations` | Established premises versus premises still to discharge. A conditional theorem can be accepted while its application remains open. |
| `source_claimed_status` | What the named historical artifact asserts. |
| `effective_status` | Current exact-scope conclusion supported by reconciled evidence. |
| `check_depth` | What this mapper or reviewer actually inspected or reproduced. |
| `evidence`, `adjudications` | Exact artifact, version, section/location, role, fingerprint, and reviewer/date where available. |
| `dependencies` | Logical prerequisites, preferably exact record versions. |
| `regressions` | Relevant counterexamples, controls, fixtures, and their checked/executed status. |
| `disagreements`, `limitations` | Conflicts, missing provenance, omitted microdependencies, and unresolved scope. |

Compact schemas may combine fields without losing their information. Give
external results a full citation, primary-source link, exact model and bound,
and transfer relevance. Distinguish an imported theorem from a newly proved one.

## Status and depth

Keep these axes independently searchable. A practical effective-status vocabulary
is `accepted-inherited`, `accepted-reviewed`, `conditional`, `provisional`,
`open`, `rejected`, `superseded`, and `unresolved`. Reuse local vocabulary when
present and define its meaning in the protocol. Status changes need evidence.

- `accepted-inherited`: the exact claim has a traceable prior scoped verdict;
  this integration does not reprove it.
- `accepted-reviewed`: a named current substantive review supports this exact
  version; cite its inputs, report, and outstanding prerequisites.
- `conditional`: the implication is supported, but named premises required for
  its proposed application remain unproved. Do not imply those premises hold.
- `provisional`: a proposed statement or repair still lacks required review.
- `open`: no established positive or negative resolution of the stated question.
- `rejected`: a specific claim or proof step fails at its declared scope.
- `superseded`: another version replaces it; retain the reason and old artifact.
- `unresolved`: conflicting evidence or incomplete reconciliation prevents a
  reliable effective verdict.

Possible check depths include inventory-only, summary-only, statement-traced,
statement-and-verdict-traced, proof-reviewed, experiment-reproduced, and
formalization-checked. Record combinations and limits explicitly. A formal proof
build establishes a statement only relative to its axioms and hypotheses;
inspect admissions, axiom dependencies, and correspondence to the intended model
before claiming the intended theorem was formalized.

Later verdicts override older banners only for the exact version and scope they
address. A positive referee report does not close an interrupted dependency
graph. A conflict is not settled merely by majority vote or a newer filename.
Do not downgrade a theorem because a later informal summary loosely labels a
different supporting proposal pending; resolve the exact references first.

## Relations and dependencies

Represent logical prerequisites separately from `supersedes`, `refutes`,
`specializes`, `covers`, `analogous-to`, and historical influence. Every relation
needs supporting evidence; a proposed relation also needs an explicit reason
and unreviewed status. Shared notation or related proof ideas alone do not
establish containment. Compare assumptions and quantitative conclusions.

Derived downstream lists are navigation aids, not separate authorities. Compute
transitive descendants from logical edges; do not manufacture cycles by treating
historical or refutation links as dependencies. A grouped claim can omit
microlemmas from the coarse graph only if it links the complete source graph and
states that limitation.

When a prerequisite changes, enumerate affected descendants and mark them
pending recheck, invalidated, or otherwise unresolved as appropriate. A descendant
may retain an accepted verdict only with evidence that the change does not
affect its exact proof, or that a supported replacement supplies the premise.
If a claim is conditional on an unproved premise, its conditional status can
survive; its unconditional application cannot inherit acceptance.

## Evidence and coverage

For local sources, record project-relative paths, exact sections/anchors,
reviewed versions and SHA256 fingerprints of the corresponding bytes. For
external sources, retain a stable URL/version and, when available, a local
fingerprinted copy. The evidence role should say whether a document supplies
the statement, proof, verdict, experiment, model, or correction.

A changed file can be an unrelated edit or a changed premise; investigate before
changing mathematical status. Whole-file fingerprints are conservative drift
alarms. Do not substitute an untracked excerpt hash for the reviewed source
without documenting how that excerpt is identified and maintained.

Coverage is its own record system. Track each family/source and known graph
branch, its map IDs or pending disposition, read depth, exclusions, and owner or
review report. Heading extraction does not count as content review. Inventory
counts, branch counts, overlapping historical records, and independent results
are different numbers. Keep high-impact conflicts prominent even when the
remaining unread material is mostly low impact.

## Targets

Targets have stable IDs, a current tier/rank, an exact open obligation, scope and
guards, nearest results/obstructions, first discriminating test, useful positive
and negative deliverables, stop/pivot conditions, effort estimate, and rationale.
Link the source evidence for novelty and dependency claims. Include confidence
qualitatively without inventing probabilities of research success.

Record which restriction a positive result would remove, which proof dependency
it would discharge, or which construction mechanism it would test. A failed
sufficient inequality narrows a route, not necessarily the underlying conjecture.
Retired targets retain their history and evidence-backed retirement reasons.
