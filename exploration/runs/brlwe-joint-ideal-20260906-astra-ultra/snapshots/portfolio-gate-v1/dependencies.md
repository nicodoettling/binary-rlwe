# Dependency diagram, version G0

```mermaid
flowchart TD
  T[Target T0 and exact source SC0] --> B[Conditional bridge B0]
  X[Joint extraction X0, retaining H and Y] --> B
  N[Noise N0, retaining J U F, integrating H] --> B
  U[Active-unit law U0] --> B
  Y[Public independent Y sampler Y0] --> B
  P[Exact joint source pseudorandomness P0] --> C[Conditional one-sample decision consequence]
  B --> C
  R[Random CRT support extraction] --> A[Candidate slot A: common feasibility]
  N --> A
  U --> A
  P --> A
  Q[Distinct coupling or restricted obstruction] --> D[Candidate slot B: disposition]
  M[New joint source, extraction and noise for m samples] --> MC[Multiple-sample decision consequence]
  MC --> S[Search conversion with held-out verification]
  C -. insufficient alone .-> S
```

Every node is initially OPEN. Changes to a source law or noise/auxiliary hypothesis reopen dependent claims. Exact statements, evidence labels, versions and reviewer dispositions are maintained in `claims.json`; frozen snapshots precede criticism. An assumed source node remains an assumption even if the bridge is checked.
