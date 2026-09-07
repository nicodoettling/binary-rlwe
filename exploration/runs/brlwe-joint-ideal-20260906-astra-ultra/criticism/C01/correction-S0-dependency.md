# C01-O1: S0 v2 requires AN in its instantiated A2 dependency record

Reviewed snapshot: review-v1, frozen 2026-09-06T15:36:43.466709+00:00. The reviewed claims.json SHA256 is 4c1194bb72d934fd2207182999a6eb72a7a82b47da6e314c3989d38cd563274d.

This is a dependency-record correction, not a change to the bridge, extraction theorem or recovery inequality. The coordinator identified the omission during C01's independent check; C01 confirms it. No canonical author file has been edited.

S0 v2 lists B0 v1 and REC v1, conditionally on P0 v2. Those suffice to describe an abstract finite recovery implication only while all statistical terms in B0 remain explicit. The instantiated A2 consequence with negligible statistical errors also uses AN v1. A conditional bridge does not prove its statistical premises merely because P0 is assumed.

Suggested replacement record:

```json
{
  "id": "S0",
  "version": 3,
  "statement": "Under AN and P0-A2, the one-sample A2 decision implication from B0 gives negligible exact planted-recovery success through REC in the baseline residual regime. More generally, the finite REC inequality retains all B0 statistical and implementation losses. Larger sample budgets require their own decision premise; verification does not identify the original witness.",
  "dependencies": [
    {"id": "AN", "version": 1},
    {"id": "B0", "version": 1},
    {"id": "REC", "version": 1}
  ],
  "conditional_on": [{"id": "P0", "version": 2}]
}
```

Use the reconciled version of AN if its noise or implementation dependency changes. This proposed metadata repair is mathematically checked here; its acceptance still inherits AN's completion/implementation review. It does not resolve P0. Until the record is repaired, C01 marks S0 v2's instantiated dependency closure GAP while accepting the finite recovery mathematics.

Exact footprint: S0's A2 negligible-error consequence, its claim-graph path, and any final recovery statement using it. B0 v1, REC v1, XG1 v1, X1 v1, PR1 v1, and A0 v2's already-present AN dependency require no mathematical modification for this objection.
