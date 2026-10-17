# Track A checkpoint — 2026-10-16, first wave

All new claims are **PROVISIONAL**. I read SC-v1, the assignment, PLAN/run-config, mathematical-proof-audit and its two references, September A-PPT v2 statement/supplement and the relevant source/parameter review. No experiment has run and no computation reservation is held.

## Frozen first tests A-H1 v1 and A-H2 v1

A-H1: For two ordinary primal integral RLWE samples `(a_i,b_i=a_i*s+F_i)`, with `s` uniform in `R_q`, consider the public map `K((a_i,b_i)_i)=(b_1,b_2)`. Compute both endpoint laws exactly. Compare with fixed-d Base2; do not condition on a hidden event as if the map could observe it.

A-H2: Try the public projected variant: independently choose a uniform d-support `T`, form its CRT idempotent `e_T`, and output `(e_T*b_1+G_1,e_T*b_2+G_2)` with independent local coefficient noise. Compute its comparator as well as its planted law. Projection may collapse both endpoints into hidden-ideal laws.

## First calculation in progress

Conditional on a secret `s`, the `a_i*s` are independent uniform points of the ideal supported on `supp_CRT(s)`, including zeros. If `s` is uniform in `R_q`, its CRT support has binomial size with parameter `1-1/q`, and conditional on the size its support is uniform. Consequently K's planted endpoint is a mixture of Base2 over d, dominated by d=n, where the endpoint is exactly uniform. The intended fixed small d occurs only with probability `binom(n,d)(q-1)^d/q^n`. On the event `s` is a unit, K's pair is exactly product uniform despite the shared s and independent errors. Thus its distance from uniform is at most `1-(1-1/q)^n <= n/q`. This is the first discriminating obstruction; precise derivation and scope follow in experiment-directions-v1.md.

The primary ePrint PDF URL returned HTTP 403 on direct open. Search indexing identifies it; alternate primary access is being attempted. This is an access failure, not a content-policy interruption. Historical exact-source extracts remain allowed corroborating input.

## Remaining obligations

Verify Order-LWE Section 7 directly, freeze the exact experiment/direction table, calculate H2, and decide whether a narrow independently motivated source assumption supplies a substantive connection or merely restates Base2. Investigate affine maps only after preserving H1/H2 failures. No general reduction impossibility or hardness claim is asserted.

## 21:20 UTC update — A-H3 v1 frozen

Hypothesis A-H3 v1: Let ordinary primal RLWE provide k samples with one uniform ring secret, uniform independent multipliers and independent source error. For any public randomized Markov kernel taking the full 2k ring elements to m ring elements, if it sends the entire uniform comparator EXACTLY to product uniform, its output on planted RLWE cannot approximate sparse Base_m within o(1) total variation when k<=m and m,k are fixed. The proposed finite entropy gap is

    g = (m-k+1-q^(-k)) n log q
        - log binom(n,d) - m d log q - m H(F),

and any output distance epsilon should satisfy `h2(epsilon)+epsilon*m*n*log(q)>=g`. Here H(F) is the entropy of one full wrapped coefficient-error vector in Base_m, logs are natural. Negative g is vacuous. This statement is frozen before the full derivation and finite controls. It has no claim for an approximately uniform comparator or for adaptive source queries.

The coordinator has requested a targeted source/ancestry review of its separate expansion EX-v1. I will preserve H3 and then switch to that assigned check. No additional experiment is running.

## 21:23 UTC update — initial task preserved; EX ancestry found

A-H3 author proof is saved separately. One authorized 30-second/256-MiB finite control finished in 0.144 seconds, exit 0, with exact mixture/rank and 6,240 linear-kernel controls; original output and command are preserved. Reservation released. No general hardness connection has been proved.

Targeted primary checking found LPR2013 Toolkit Theorem 7.4/Corollary 7.5, the normal-form ring regularity theorem. Its identity-column plus random-seed construction already avoids common-divisor rank failures. Gaussian inputs could exploit three total columns `(1,A1,A2)` at q^(1/3) scale; the coordinator's frozen EX-v1 instead uses box coefficients and Gaussian W at sqrt(q) scale, with a direct proof. The new scientific contribution must be assessed as the composition with hidden-ideal common-quotient lossiness and full joint sample extension, not generic ring regularity. Awaiting the coordinator's immutable review packet while preserving initial hypotheses separately.
