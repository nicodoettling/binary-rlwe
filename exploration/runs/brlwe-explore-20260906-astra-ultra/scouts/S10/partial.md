# S10 partial record

Started 2026-09-06 10:00 UTC. Scope: at most two independent average-case source experiments and first encodings into the reference binary rank-one RLWE distribution. Read target.md and context/barriers.md; reading-notes used solely to find source leads. No other scout/coordinator inventory inspected. No experiments requested or run.

Initial candidate mechanisms: (1) independently studied quasi-cyclic decoding / Ring-LPN, testing whether a binary field planted source can be lifted into odd-q Gaussian observations; (2) NTRU key recovery, testing whether direct planted key transport differs from the supplied lossy use of ratios. These are discovery candidates, not claims of reductions.

Access note: initial rg included nonexistent root related.bib and reported that absence. Local supplied source extracts are readable.

Reference ledger: rank 1; n growing power of 2; q odd poly(n); R_q=Z_q[X]/(X^n+1), coefficient basis; S_j iid Bernoulli(1/2); E_ij iid D_sigma, independent across ring samples; m poly(n); q/sigma >= n^c; wrapped coefficient law W_sigma,q. Rotations remain correlated.

## 10:03 update: selected mechanisms

NTRU was screened but dropped: direct transport starts from h f=g and gives (h,0), not the required uniform public transcript; using ratio lossiness is already the baseline. The final two mechanisms will be quasi-cyclic decoding and planted compact ring knapsack. No third mechanism will be developed.

Primary-source access: arXiv 1612.05572 (Aguilar et al., 2016), arXiv 2306.03488 (QA-SD), author-hosted Micciancio Cyclic.pdf and Lyubashevsky–Micciancio IdealHash.pdf are readable through built-in web. https://eprint.iacr.org/2021/1352.pdf returned internal error; no technical claim will depend on that paper. Primary paper locations will be cited in source-notes.md.

A useful diagnostic emerged: the planted two-block binary ring knapsack normalizes to one-sample binary-secret/binary-error RLWE, so its relevance is exact but does NOT independently establish hardness. Adding discrete Gaussian noise gives a quantitative oracle implication with additive statistical loss. Existing compact-knapsack results cover other block count / coefficient width regimes. This is a source-regime obstruction, not a new hardness claim.

## Completion at 10:11 UTC

Final report is ../S10.md (578 words at initial write; minor formula correction follows). Durable details are calculations.md and source-notes.md. The coordinator suggested replacing additive TV success transfer by an order-two Renyi comparison; the exact integer-shift calculation verifies that improvement, and the final report uses it. The coding mask also has a unit-conditioned one-sample information-theoretic recovery obstruction. Source-regime bridge remains unresolved; no claim of independent binary RLWE hardness is made. No experiments, other services, subagents, or continuation sessions were used.
