# Frozen target T0 — 2026-09-06

This is a finite investigation, at most five hours from the launch clock. It is not a goal or proof-until-success run. The absolute authorized manifest is `/home/nico/projects/research_projects/binaryRLWE/exploration/runs/brlwe-joint-ideal-20260906-astra-ultra/run.json`; validation is in `launch-validation.json`. Launcher files are read-only.

For growing power-of-two n, R_q = Z_q[X]/(X^n+1) in its coefficient basis. Baseline q is an odd polynomially bounded fully splitting prime, q = 1 mod 2n. S has n independent uniform {0,1} coefficients. One target sample is (a,aS+E), with a uniform in R_q and independent E having wrapped iid coefficient D_sigma law, D_sigma(z) proportional to exp(-pi z^2/sigma^2). Require q/sigma >= n^c for fixed c>0. This reference regime is not a universal hardness assertion. The original eventual task allows explicitly m=poly(n) independent ring samples sharing S. Begin with m=1; search and decision are separate.

Source interface SC0: without any binary secret as input, efficiently sample hidden (J,U,F,H), where I=Ann(J) and U induces an isomorphism R_q/J -> I. Conditional on J draw V uniform in I, independent of (U,F,H). Challenge consists only of (A,C)=(U+F,V+H), compared with two independent uniform ring elements. Any change in support, U law, F/H correlation, widths or precision changes the source experiment.

Independently of the entire source tuple draw S and a fixed public-law iid coefficient G. Set Y=S+G mod q. The public reduction can sample Y using its own fresh S0,G0 without hidden challenge data. This independence is an algorithmic requirement of SC0, not optional latent bookkeeping.

Bridge obligations B0 (unproved at freeze): extraction TV between (J,U,F,H,Y,pi_J(S)) and (J,U,F,H,Y,Z) is at most eta_ext, where Z is uniform in R_q/J conditionally independent of the retained variables. Noise TV between (J,U,F,FG+H) and (J,U,F,E) is at most eta_noise, with independent target E. H is integrated out in noise comparison and retained for extraction. These are sufficient stronger latent-variable hypotheses; public-only correctness would require a new full hybrid.

Proposed finite endpoint: for every PPT one-sample test D, explicitly construct two potentially different PPT source tests B1,B2 such that target distinguishing advantage is at most Adv_source(B1)+Adv_source(B2)+eta_ext+eta_noise plus explicitly budgeted implementation/bad-event errors. Quantifiers, signed differences, samplability and computational overhead are to be checked by F01 and a later nonauthor. This theorem assumes the exact source's joint pseudorandomness; it cannot justify that assumption.

Four required outcomes: checked conditional one-sample bridge; at most two defensible or explicitly retired source/coupling families; separate multiple-sample and task analysis; critical final assessment with all material objections disposed. A gap or no viable family is acceptable. Primary source comparison is required for any novelty distinction.

Frozen latest boundaries UTC: setup 14:36:13.181175; foundations 15:21:13.181175; development 16:36:13.181175; refinement 17:36:13.181175; criticism 18:16:13.181175; reconciliation 18:36:13.181175; synthesis/workers stop 19:06:13.181175; hard stop 19:21:13.181175. Advance early when obligations are done, never extend these times.
