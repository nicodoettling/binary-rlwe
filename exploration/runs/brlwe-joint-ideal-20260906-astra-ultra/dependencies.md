# Dependency diagram, version G2

Arrows show mathematical dependence, not evidence of source hardness. Exact statements, versions and critic dispositions are in claims.json. New derivations remain provisional until fresh criticism. Original inputs are preserved in the portfolio-gate snapshot.

```mermaid
flowchart TD
  SC[Exact source interface SC0] --> B[Conditional bridge B0]
  Y[Independent public Y sampler Y0] --> B
  U[Bijective U or charged rank defect U0] --> B
  NX[Strong joint noise and extraction premises] --> B
  BV[BV Prop 23 and Voutier Cor 2] --> X[X1 rich-support extraction]
  NC[NC1 completion and exact H_seq] --> AN[A2 analytic compatibility]
  X --> AN
  PR[PR1 split-prime regime] --> AN
  A[Exact A2 source law] --> AN
  A --> P[P0-A2 source hardness OPEN]
  B --> C[Conditional one-sample decision]
  AN --> C
  P --> C
  C --> R[REC same-budget recovery consequence]
  SH[BSH exact public shear reduction] --> BS[B1 source map retained]
  BN[BNG wrapped two-fiber obstruction] --> BR[B1 negligible-noise route retired]
  MK[New common-K source Pm OPEN] --> MC[KM conditional m-sample decision]
  MN[Full stacked H_seq with cross blocks] --> MC
  X --> MC
  MC --> MR[REC at its own sample budget]
  LY[Separate Y_i leakage and consistency] --> ML[No automatic sample extension]
```

The bridge is a conditional implication: its proof can be accepted while P0-A2 remains open. A2 analytic feasibility combines one specified d,q,F,H,G law; it is not the stronger claim of a supported computational construction. Uniform-U HLBDD and active-U A2 are different sources. B1's inherited source map and A2's noise cannot be combined.

For m samples, KM needs the new common-K source, full vector noise comparison and one full retained extraction statement. It does not tensor one-sample copies. Search conversion is separate: same-budget verification needs no held-out samples in the baseline, whereas held-out verification consumes additional independent samples.

Source or auxiliary changes reopen statistical premises and computational assumptions. Critic-induced changes must list downstream dispositions in reconciliation.md and the ledger history. No formal proof certificate is claimed.
