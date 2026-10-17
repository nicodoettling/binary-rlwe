EX-v2 is ACCEPTED in its exact conditional scope after full proof, source/parameter/complexity, fresh blind and artifact reconciliation. Let n be a power of two, ell=log2(n), and P(1,M) the least prime congruent to1 moduloM. Every computational premise below is separate and unproved.

| Quantity | Historical accepted A-PPT v2 | EX-v2 accepted result |
| --- | --- | --- |
| Source samples | One pair, same hidden T | The same two-point budget |
| Target sample budget | m=1 or2 | Fix integer h>=0 first; efficiently computable1<=m(n)<=n^h |
| Modulus | q=P(1,2n^3), eventually2n^3+1<=q<=n^16 | K=h+10; q=P(1,2n^K), eventually2n^K+1<=q<=n^(6K) |
| First support family | d=floor(sqrt(n)/ell^4) | Same formula, at the changed q |
| Second support family | d=floor(n/(64ell)) | d=floor(n/(24Kell)) |
| Source coefficient Gaussian width | ell | ell |
| Expansion coins | None | Rj1,Rj2 coefficient-uniform in{0,...,L-1}; Wj coefficient D_L; L=ceil(n sqrt(q)) |
| Expanded mask bound on good event | ell² | b=(2n+1)L ell² |
| Target coefficient Gaussian width | 2sqrt(m)n ell³ | sigma=2sqrt(m)n b ell=2sqrt(m)n(2n+1)L ell³ |
| Ratio | Historical fixed-family conclusion | q/(n sigma)>=sqrt(2)n/(12ell³) eventually; hence q/sigma>=n eventually |
| Entropy charge | q^d | q^d once for all m rows; eventually <=2^(n/4) |
| Source assumption | Base2 at September q,d | Base2 at each NEW h,q,d family; no inheritance from September |

For m=3 take h=1,K=11 and n>=4 in the finite sample policy. The finite theorem itself allows any positive integer m, q>=n² split prime, and0<=d<=n; its probability bounds may be vacuous. The asymptotic theorem chooses h and the m policy before the adversary. It does not prove arbitrary polynomial sample budgets at one fixed modulus family. Both support families eventually have d/log(n) tending to infinity, avoiding the immediate small-d polynomial ATT upper bound without proving hardness.

The target width is enlarged by (2n+1)L compared with the baseline expression at equal n,m. In the actual comparison q also changes. This is a sample-budget extension with substantial modulus/noise cost, not a practical parameter recommendation.

The exact finite losses are in [the frozen theorem](coordinator/expansion-theorem-only-v2.md), with derivation in [canonical proof v2](coordinator/expansion-proof-v2.md). In particular, delta_exp=min(1,m/2 sqrt(16^n q^n exp(-2pi n²)+(2/n)^n)); delta_mask=min(1,(m+2)n exp(-pi ell²)/(pi ell)); the normalized completion error eta is guarded at Delta<1. Actual-secret guessing contributes q^d((1+D_ell(0))/2)^n. Implementation adds full-law xi_source+2xi_alg+xi_target.

The executable wrapper calls Q once and uses3m ring multiplications, O(mn²) schoolbook modular operations,2mn interval draws,mn D_L draws,mn D_sigma draws andn bits. [RS1's explicit sampler](criticism/RS1/sampler-budget-v1.md) gives xi_alg<=3*2^(-n²)/8 with table size O_h(n^(7h/2+34)ell³) and storage O_h(n^(7h/2+36)ell³) bits. These very large polynomial existence bounds are not experimental resource claims or practical costs. The proof-only dense completion Gaussian is not sampled by the wrapper.

[RS1](criticism/RS1/report-v1.md) verifies the effective least-prime import, entropy/range inequalities and implementation scope. The old q128/old-d counterexample remains rejected; tying d toK is essential. No numerical threshold for the effective prime constant is claimed.
