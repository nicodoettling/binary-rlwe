# A1 result — direct search route survives author checks

**Provisional theorem, ready for fresh review.** From the explicitly assumed two-point same-hidden-ideal source

    (U_1+F_1,U_2+F_2) versus uniform R_q^2,

where U_1,U_2 are independent uniform points in one random rich ideal and F_1,F_2 are independent coefficient D_ell masks, a solver recovering independent coefficient-binary S from exactly m in {1,2} target ring samples gives one source distinguisher with

    Adv_source >= epsilon_m
        -q^d ((1+D_ell(0))/2)^n-eta_N-delta_F,m
        -xi_source-2xi_alg-xi_target.

The target errors are independent coefficient D_sigma_m across every sample and coefficient, with sigma_m=2sqrt(m)n ell^3. The source test samples its own S and errors and verifies equality to that exact S. It uses one source challenge pair and one solver invocation. No source expansion or more-than-two-sample result is claimed.

The full witness-retaining noise edge is valid: S may be appended because the source witnesses, G and proof-only H have the stated full product law. H is integrated out at that edge. Revealing H only in the completed loss world is valid for the upper bound; (C,H) adds no secret information beyond Y=S+G and the charged quotient. This yields a single q^d leakage factor even for two target samples. Uniformity of pi_J(S), invertibility/active coordinates of U, and quotient extraction are unnecessary.

Exact proof-only H~D_B permits the rectangular Poisson completion directly. No matrix-Gaussian implementation or H_seq correction is needed. For m=2, B contains the off-diagonal blocks -ell^2 M_F1 M_F2^t; separate marginal completions would not suffice.

For ell=log2 n, q the least prime 1 modulo 2n^3, and the explicit least-prime import, eventually q<=n^16 and q/sigma_m>=n. Both the historical d=floor(sqrt(n)/ell^4) and each separately assumed source family with 1<=d<=floor(n/(64ell)) have negligible total analytic loss. The latter has guessing term at most 2^(-3n/4+n/(ell ln2)). Source assumptions remain distinct for distinct d choices.

The complete proof is `proof-v1.md`, with `supplement-v1.md` for the larger-d corollary and a fully bounded dyadic Gaussian sampler. The clean blind packet is **`theorem-only-v2.md`**, SHA256 `bba5d89bc2658228f9cdb7c3c9f325349f864bbe9a24c03be414ae7eee221124`. Do not send the earlier packet to a blind referee. `artifact-manifest-v1.json` records exact proof/packet/experiment hashes.

The authorized exact rational script `exact_controls_v1.py` passed all assertions in 0.017 seconds; `exact_controls_v1.json` preserves inputs and results. It checks strict wrapping contraction, all two-label maps on a finite noisy-bit model, one/two-source witness simulation including zero U branches, exact-witness versus residual verification, the shared-G marginal trap, secret/G-dependent H failures, and historical CP-1. These finite checks do not certify the asymptotic theorem.

Remaining coordinator obligations: fresh nonauthor and blind checks of the exact theorem/proof; primary verification of the explicit HLBDD specialization and least-prime import; integrated regression/dependency closure. The computational source hardness is an assumption throughout. No worst-case source justification, target decision theorem, or arbitrary-sample binary-RLWE theorem was proved here. All claims remain PROVISIONAL until the coordinator completes the prescribed review gates.

All writes were confined to workers/A1. No agent or goal was spawned, no package installed, and no content-policy interruption occurred. The single experiment slot was released immediately after its bounded run. Ordinary PDF-reader access limitations were handled through the approved primary-PDF web tool and recorded below.
