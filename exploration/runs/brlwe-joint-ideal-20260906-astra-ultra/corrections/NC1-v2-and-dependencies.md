# Proposed reconciliation correction: NC1 v2 and dependency propagation

The reviewed snapshot remains immutable. This correction responds to C03-O01 and C01-O1; it is not a new candidate or refinement workstream. Final critic dispositions remain pending.

## NC1 version 2: guarded finite convolution and sequential comparison

Let M be an integer p-by-n matrix, tau,sigma>0, B=sigma² I_p-tau² M M^T positive definite, and Theta=tau² I_n-tau⁴ M^TM/sigma² positive definite. Let independent G~D_tau on Z^n and H_* have mass proportional to exp(-pi h^T B^(-1)h) on Z^p. Define

    delta=sum_(k in Z^n, k!=0) exp(-pi k^T Theta k),
    e_conv = min(1,delta/(1-delta)) if delta<1; otherwise e_conv=1.

Then TV(MG+H_*,D_sigma^p)<=e_conv. For the exact canonical sequential H_seq law associated with B, put beta=lambda_min(B), kappa(beta)=2 sum_(j>=1)exp(-pi beta j²), and

    e_seq = min(1, [((1+kappa(beta))/(1-kappa(beta)))^p-1]/2)
            if kappa(beta)<1; otherwise e_seq=1.

Then TV(H_seq,H_*)<=e_seq and TV(MG+H_seq,D_sigma^p)<=min(1,e_conv+e_seq). A common wrapping map cannot increase these distances. Finite implementation error is a separate comparison with H_seq and retains the bridge's stated accounting. This generic statistical theorem makes no finite-PPT claim for arbitrary real input parameters; the explicit A2 approximation regime is in R03.

C03's counterexample to the unguarded ledger v1 is n=p=1,M=0,sigma=1,tau=1/3. Its actual output equals D_1, so TV=0, but delta>=2exp(-pi/9)>1 makes delta/(1-delta) negative. The detailed F02/D03 proofs already required delta<1. A2 and MN meet delta<1 and kappa(beta)<1 for sufficiently large n; their applications are unchanged.

## Proposed exact version propagation

- NC1 v1 -> v2 adds the mandatory finite guards above.
- AN v1 -> v2 changes its NC1 dependency to v2; its A2 mathematical statement and parameter regime stay the same.
- MN v1 -> v2 and CHAR v1 -> v2 likewise point to NC1 v2; their actual regimes satisfy the guards.
- A0 v2 -> v3 points to AN v2 and remains deferred on P0 v2.
- M0 v2 -> v3 points to MN v2 and remains deferred on Pm v1.
- S0 v2 -> v3 explicitly depends on AN v2 in addition to B0 v1 and REC v1, conditional on P0 v2. This repairs C01-O1's omitted instantiated-statistical dependency. It does not change the general REC theorem or the bridge.

All previous claim versions and raw critic reports will be preserved in ledger history and the review-v1 snapshot. The proposed deterministic ATT repair, if retained after a different critic checks it, has its own version and is not included in this correction.
