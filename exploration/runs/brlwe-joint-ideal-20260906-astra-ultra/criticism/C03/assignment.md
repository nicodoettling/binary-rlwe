# C03 — discrete noise, implementation, multiple samples and tasks critic

Output directory: /home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-joint-ideal-20260906-astra-ultra/criticism/C03/
Exact task deadline: 2026-09-06T16:15:00Z. Read ../REVIEW_INSTRUCTIONS.md first.

Read review-v1 foundations/F02-review-packet.md/F02-completion.md/F02.md and F01-theorem-v1.md, development/D03.md/D03-common-k.md, refinement/R03-interface-audit.md, canonical candidates/A.md, parameter-table.md, multi-sample.md, bridge.md and claims.json. Audit NC1, NO1, DEC, MN, KM, LEAK, REC, M0v2/S0v2 and the sampler/noise parts of AN. You did not author them.

Independently check complete-square and Poisson normalization, actual discrete-versus-continuous covariance, H_seq exact law versus D_B, adaptive LDL centers and pointwise conditional normalizers, uniform pivot/center bounds, rational bit complexity, finite table errors/capped rejection/tails and the 2xi_src+2xi_1+xi_Y accounting. Retain J,U,F and integrate H in noise; retain full H,Y in extraction. F truncated and G full iid laws must not be confused. Check NO1's theta product monotonicity uniformly for growing tau and finite deconvolution/Renyi controls, with primary theta identity if imported.

Reconstruct the full common-K source hybrid, conditional ideal tuple distance, rectangular stacked covariance INCLUDING cross blocks, input smoothing dimension n vs output sampler mn, sqrt(m) sigma growth and prescribed polynomial m with polynomial q. This new source is not a tensor product of the old assumption. Verify separate-Y likelihood/MGF/wrapping/Fano estimates and A2 threshold C>2/pi separately from A1 threshold. Verify same-budget planted recovery/self-verification (no independence of solver success from errors) and held-out alternative with exact budget; planted witness versus valid preimage and mild-search/oracle distinctions. Directly check cited sample expansion interfaces where load-bearing. Do not demand an executable implementation project: the task is to verify the stated approximation construction and its errors.

Save review.md, exact objections and any small hand controls, tied to claim versions. Bound the audit; no new family or unallocated CPU experiment.
