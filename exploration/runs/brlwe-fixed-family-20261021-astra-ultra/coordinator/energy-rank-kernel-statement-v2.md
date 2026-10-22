# FF3-ENERGY-RANK-v2

PROVISIONAL author candidate. A known-residual noise kernel preserving full input direction; no full binary-cube modulus-transfer theorem is asserted.

Let I,J be finite consecutive integer coefficient alphabets of sizes Q,q, and define energy E(x)=sum_i x_i^2 on I^n and F(y)=sum_i y_i^2 on J^n. Let M_e,N_f be the numbers of vectors in each nonempty energy class. Let U,V be uniform on these Cartesian powers. Let P,N be probability laws constant on each respective energy class; in particular, the exactly normalized finite centered coefficient discrete-Gaussian products qualify. Write alpha_e=M_e/Q^n,beta_f=N_f/q^n,p_e=P(E=e),n_f=N(F=f).

Suppose a Markov table h(e,f) maps alpha to beta and p to n. Given x in source energy class e, let r in{0,...,M_e-1} be its lexicographic rank. Draw f according to h(e,.), draw T uniformly from{0,...,N_f-1}, and output the target energy-f vector of rank

                       j=floor((N_f*r+T)/M_e).                        (R)

This normalized kernel H satisfies UH=V and PH=N EXACTLY. It generally retains the full lexicographic input rank, so output does not factor through a polynomial energy class alone. A fixed permutation of the source ranks in each class (e.g. reversal) may be applied before(R) without changing either endpoint.

If Q,q and the maximum absolute alphabet entries have polynomial NUMERICAL value in n, shell counts, lexicographic ranking and unranking have polynomial time and bit complexity by integer dynamic programming. Every count has at most n*log2(max(Q,q))+1bits. A given rational h with polynomial table size and entry bit length can be sampled in expected polynomial time. If instead a sampler approximates each h(e,.) within TV epsilon, the resulting H row is within epsilon of the exact row; the rank stage is exact. No exact finite sampler for arbitrary real h is assumed.

The same statement holds for a PAIR of residuals, using joint class(e0,e1), size M_e0*M_e1, lexicographic pair rank r0*M_e1+r1, and target pair rank j0*N_f1+j1. Pair-shell products have at most2n*log2(max(Q,q))+1bits; the single-vector bound above is not asserted for these products. The table h may map the relevant joint class distributions. A general full-cube endpoint still requires a separate proof; preserving one or two residual noise/uniform laws does not suffice.

For wrapped discrete Gaussians modulo Q and q, use fixed centered coefficient intervals I_Q,I_q. Replacing the wrapped law by the corresponding independently truncated and renormalized coefficient Gaussian costs at most n*Pr[D_Z,sigmaQ outside I_Q] on input and n*Pr[D_Z,sigma0 outside I_q] on output. Thus exact H for the finite centered laws yields the sum of these two errors for the wrapped noise endpoint, plus its declared sampler error. The uniform endpoint is exact for the ideal H. When Q/sigmaQ and q/sigma0 grow at least linearly in n with fixed constants, standard Gaussian tail bounds make these costs negligible at polynomial-value widths; no moment match is used.

An energy table may be obtained from FF3-TWOEVENT when C is a union of energy classes and the two likelihood inequalities hold. That is a conditional construction, not an assertion that they hold for every parameter family. The exact real h table then exists; finite precision/sampling costs must be charged separately.
