# RF1 exact proof-v2 recheck v1

This supplement was performed AFTER RF1/report-v1.md was frozen at SHA256
`721f72bac4ded7e13054fe14ea69c95678b414b4dd31d1ce3f6e545155f25e90`.
That original report and its proof-v1 input remain unchanged. This is a
separate nonblind recheck of a new proof artifact, not a silent input switch.

Verified exact inputs:

- Theorem-v2: `44b3154f650f43022e7720484f185c27890fb56c695b2b5303d73970463ebb51`.
- Proof-v1: `38c43826a936f69a775a97f19dfb3aeb90256cd03d8953d47fd54f82da27c8ae`.
- Proof-v2: `234d9e69af04fcddc68af7eba08e508d309eecffcf87203f81b2bac79d611909`.

The exact proof-v2 bytes are preserved as `input/proof-v2.md`. I independently
recomputed the diff against the original frozen proof-v1, saving
`proof-v2-local-diff.txt`; I did not rely solely on the coordinator's diff.
The live canonical theorem-v2 bytes were also compared with the frozen input
and match exactly.

Mathematical sections 1 through 9 are byte-identical, with shared SHA256
`178049b147f2ea55640973ba015c5428f3dfb56783be89169efd80a9659dcc72`.
The scientific-boundary paragraph's actual claim/scope prefix is identical.
The only edits are:

1. The title now identifies the EX-v2 theorem.
2. The opening paragraph links theorem-only-v2 instead of the stale v1 name
   and delegates review status to the ledger/reconciliation.
3. The final sentence likewise moves certification status out of the proof
   artifact while retaining all scientific scope exclusions.

I checked that these edits neither change a probability law, quantifier,
constant, algorithm, dependency, computational premise, nor claim a completed
blind/global gate. In particular, the two-point Base2 premise at the NEW
family and the exclusion of iid planted Base_m production remain explicit.
The initial report's administrative stale-header observation is closed by
this exact edit.

**Disposition: PASS for theorem-v2 with exact proof-v2 in the same conditional
mathematical/parameter/uniform-PPT scope audited by RF1/report-v1.** This
conclusion follows from the verified complete identity of all load-bearing
proof sections and direct reading of all modified prose. No new experiment
or mathematical repair was needed. Source pseudorandomness remains assumed;
fresh blind review and final coordinator integration remain separate gates.
Same-model scrutiny is correlated. No RB2 material was read or communicated.

The machine-readable byte-comparison record is
`proof-v2-comparison-receipt.json`. No author artifact or earlier report was
modified during this recheck.
