# Binary-RLWE work programme

Version 1, 21 October 2026. This is a bounded programme update integrating the collaborator's question about high-entropy binary secrets, not a complete reconciliation of the research archive. Exact statements and acceptance records govern mathematical status; this file governs planning and navigation.

| Item | Planning status | Obligation and evidence |
| --- | --- | --- |
| FF — fixed target family | Assigned to the existing October 21 run | Remove dependence of target parameters on the distinguisher's sample and advantage exponents. See the [frozen plan](fixed-family-20261021/PLAN.md) and [run's programme ledger](runs/brlwe-fixed-family-20261021-astra-ultra/programme-decisions.md). This update does not adjudicate that run's evolving claims. |
| SV — source significance | Assigned to the same run | At the reduction's actual radius or sampling width, establish a hardness connection or an exact algorithmic classification, with remaining cases explicit. Classification alone does not establish hardness. Same plan and ledger as FF. |
| ENT1 — entropic binary-secret extension | **Proposed successor; not launched** | Replace uniform binary secrets by an efficiently samplable joint distribution with min-entropy at least h. Investigate the tradeoff between h and log₂ N(J), first for the accepted restricted decision reduction. See the [work package](entropic-binary-20261021/WORK_PACKAGE.md). |

ENT1 is a near-term extension candidate because the selected-functional and prime-averaging bounds appear to admit weighted versions, while several other steps use only binary support. Its value is broader secret distributions, including correlated bits. It does not remove the source-hardness gap or, by itself, solve FF. Preserve FF and SV as the ongoing run's priorities; select the next investigation after reconciling its final evidence. ENT1 can begin from the accepted predecessor even if FF remains open.

The baseline is [FIXED-MAIN-v2 and its dependencies, accepted with explicit scope](runs/brlwe-direct-decision-20261021-astra-ultra/coordinator/acceptance-v1.json): a classical reduction to decision binary RLWE with prescribed sample/advantage/noise restrictions and small-index ideals. That verdict covers uniform secrets. It supplies no acceptance for ENT1's proposed weighted extension.

No running assignment, protected investigation period, deadline, frozen prompt, or completion condition is changed by this update. No new research run, experiments, commit, or push are authorized by this document. The [original September exploration plan](PLAN.md) remains historical.

Maintenance: after the current run closes, reconcile its exact accepted versions before choosing whether ENT1 composes with an improved FF result. Record changed dependencies and fresh review obligations in the ENT1 work package. Documentary validation and source fingerprints for this update are recorded in the [integration receipt](entropic-binary-20261021/integration-receipt.json).
