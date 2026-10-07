# Search candidate parameter table

| Quantity | Exact choice or scope |
|---|---|
| Ring | R_q=F_q[X]/(X^n+1), n growing powers of two; rank one |
| ell | ceil(log2 n)=log2 n on this sequence |
| Source masks | Both points use independent iid integer coefficient D_ell, wrapped modulo q |
| Hidden ideal | Uniform d-subset T of all CRT roots; U_1,U_2 independently uniform supported ideal I_T, zeros allowed |
| Source budget | One challenge pair containing exactly two ring elements |
| Target | m in {1,2}; independent uniform a_i, one common iid coefficient-binary S, independent coefficient Gaussian E_i |
| Auxiliary width / mask bound | tau=ell, b=ell², used only in proof |
| Target width | sigma_m=2sqrt(m)n ell³; sigma_m² is integer4m n²ell6 |
| Modulus | Least prime1 mod2n³; eventually2n³+1<=q<=n16 |
| Ratio | q/sigma_m>=n eventually; no practical threshold |
| Main d example | floor(sqrt(n)/ell4), eventually positive |
| Larger explicit d example | floor(n/(64ell)); different exact source assumption |
| Algebraic d allowance | d<=n/(64ell) makes guessing term<=2^(-3n/4+n/(ell ln2)); source plausibility not asserted for every d |
| Completion | Exact proof-only D_B with full stacked mn-by-n M; cross blocks retained; no H_seq sampler |
| Finite loss | q^d((1+D_ell(0))/2)^n+eta_N+delta_F,m; eta_N guarded as in statement |
| Precision loss | xi_source+2xi_alg+xi_target; all complete joint law errors |
| Cost | One solver call, n binary bits, mn independent Gaussian draws, m ring multiplications/additions, equality check |
| Bit complexity | Polynomial in n and log q; target table O(n²ell³) entries and O(n+log n) probability bits at xi_alg<2^-n |

All parameter functions precede the adversary. The concrete d examples are efficiently computable. A generic merely computable d sequence need not have efficient setup; that broader conditional wording is not used to claim an efficiently generated family. Small d can make the source easy. The m1/2 result does not imply the original polynomial-sample task.
