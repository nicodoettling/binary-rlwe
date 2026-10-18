# Fixed binary gap to finite ideal BDD and approximate DGS: integration v2

PROVISIONAL integration of separately reviewed components. This note does not alter their accepted scopes or certify the newly frozen C repair. It uses A-FRAC theorem/proof v1, B-GP-v2 and B's bounded composition v1, and C theorem7 + standalone algorithm-v1 + full proof8. All exact-version review dependencies remain with the coordinator. The standard source-hardness objective is OPEN.

Fix0<rho<1, polynomial sample countk, ell=ceil(log2(2nk)), and an integral ideal J with D=N(J)<=2^(rho n), gcd(D,q)=1. Let q be a supplied permitted split prime with q>=n^c sigma_target, where

    sigma_target=8n^2 ceil(sqrt(kn)) ell^4,
    r_B=w_B=ell^2, s=sqrt(2)ell^2,
    epsilon_B=nu=eta=2^(-ell^2), P=2^(2ell^2).

Let Rec be the fixed bounded original binary recovery circuit, ignoring J metadata, with success epsilon_rec on the exact target law. Its fixed finite GP distinguisher samples a fresh binary witness and fresh target errors internally, uses B's bounded bridge, invokes Rec, and checks witness equality. B's cap/approximation errors enter its distinguishing advantage at the two exact GP-input endpoints. The resulting explicit lower bound is

    delta_C=epsilon_rec-delta_tail-beta-eta_A
       -2k epsilon_B/(1-epsilon_B)
       -2pi kn/(P r_B)-3kn nu-2eta,

where delta_tail=4kn exp(-pi ell^2), beta<=min(1,exp(-(1-rho)n ln2+1/(2n ell))), and eta_A is the exact completion error in A-FRAC. Supply an explicit positive delta<=delta_C. When all deductions are below epsilon_rec/2, delta=epsilon_rec/2 is permitted. A merely asserted positive advantage without a known usable lower bound is insufficient to instantiate the reduction's parameters.

This SAME bounded algorithm A_J has that gap pointwise for every eligible J, because the original target recovery law and epsilon_rec are independent of J when Rec ignores its metadata. Its exact input experiments are

    (J,Q_h(G_w)^k mod qJ^-1), versus (J,uniform(F)^k),
    w=sqrt(n)w_B, h=1/(DP), F=hZ^n/qJ^-1.

The uniforms are independent and the public metadata is identical. The ideal distribution is not randomized or hidden by this statement. An average-family premise would yield only good-ideal conclusions. The coprimality restriction belongs to the A/B composition; standalone C-BDD itself does not require it.

The internal bounded bridge's cap loss2eta and all other deductions in delta_C are paid ONCE to establish the fixed actual algorithm's endpoint gap. They are not additional errors to multiply by C's Q_*. C invokes this fixed algorithm with fresh internal coins on arbitrary physical queries; its own normalizer, finite-walk, and numerical-sampler errors are separate per-query/conditional quantities charged by C's displayed budgets. The source remains exact finite GP versus exact finite uniform even though A_J internally uses bounded approximate samplers.

C theorem7 with its full standalone definitions and proof8 then gives exact recovery of lambda from rational T=lambda+e, lambda in qJ^-1, ||e||canonical,infinity<=d0, with

    d0=delta*w/(32nkv0),
    Pr[correct]>=1-(n/2)exp(-kappa)-zeta.

Use the ACTUAL conservatively rounded a and chosen v0 from the new specification. Q_* is explicitly polynomial in kappa and accounts for both orientations and every pair. The exact Haar endpoint used in this proof is that of the continuous proxy only; the physical discrete query need not converge to Haar. No additional physical-limit assumption is available or needed.

For the separate quantum gate, use rational coefficient lattice M=conjugate(J)/q, whose coefficient dual is qJ^-1, and Euclidean BDD radius d0/sqrt(n). Given actual circuits suitable for reversible compute/copy/uncompute, the primary BDD-to-DGS construction yields an APPROXIMATE Gaussian on the SAME J with coefficient width

    s_J=nq/(sqrt(2)d0),
    TV error<=delta_prim+2Q_D sqrt(eta_BDD),
    eta_BDD=(n/2)exp(-kappa)+zeta.

Delta_prim includes primary Gaussian-state truncation/reference-state and finite-gate errors. The source quantum theorem's reference-state support is why no correctness promise is required off the BDD radius; bounded off-promise behavior alone would not remove that primary error charge. Opaque classical remote-oracle access does not supply the necessary coherent circuit. Choose confidence so Q_D sqrt(eta_BDD) is negligible, for example zeta=exp(-kappa/2) with kappa>=2log(8n) and sufficiently large polynomial confidence. The invalid old choice zeta=exp(-kappa) is not reused.

With minimal v0=2sqrt(n)a when it satisfies uniqueness, a coefficient output radius is

    R_out=sqrt(n)s_J=(64/sqrt(2))n^(5/2)kaq/(delta*w_B).

Otherwise use the actual larger v0 and corresponding d0. The ideal smoothing/nonzero and norm-tail bounds in the separate restricted-SuperSVP packet apply to the ideal Gaussian, and the actual sampling TV error is added. This may give a nontrivial restricted K_T(q0) consequence when q0^d<=2^(rho n), gcd(q,q0)=1 and q0>R_out. It does not normalize arbitrary standard ideal lattices into the eligible J family and does not establish its standard worst-case hardness.

B's frozen bounded-composition hash is6ff55f5926ae639deb30985f009a3898a2da05e1accab4682e022c258122f225. The C repaired packet hashes are recorded in periodic-hardness/v7-v8-freeze-manifest-v1.json. The quantum approximate-law source note is supersvp-mining/quantum-source-gate-v2.md. No new experiment was run for this integration.
