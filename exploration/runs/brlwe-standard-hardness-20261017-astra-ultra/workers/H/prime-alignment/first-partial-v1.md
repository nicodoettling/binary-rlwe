# H prime alignment: first partial, 2026-10-18

Status PROVISIONAL author derivation, not accepted and not a standard-hardness result. Assignment SHA256 32524c80a4fdce8b23f6a014ec79df3abdaed82fbadc37a0ab1f889630fb8120 is unchanged. Read the mathematical-proof-audit skill, audit protocol, probability regressions, A's replacement, balanced-join-v2, small-index simulation and fractional theorem/proof. No reviewer material or BT17 access.

The proposed all-width estimate appears valid, with an elementary stronger constant. For K=FI, r=N(K)^(1/n), coefficient norms satisfy lambda_1(K)>=r and lambda_1(K*)>=1/r, because K*=conjugate(K)^-1 and algebraic norm is bounded above by coefficient norm to the nth power. If s>=4 sqrt(n) r, dual packing shells imply rho_(1/s)(K*)<2 and hence the original, zero-excluded alignment probability is <=2/N(I). Otherwise, the disjoint-ball bound N_K(t)<=(1+2t/lambda_1(K))^n and layer-cake integration imply

    rho_s(K) <= [4 sqrt(n) max(1,s/lambda_1(K))]^n
             <= (16n)^n.

Using rho_s(F)>=s^n/N(F) and N(F)<2^n gives

    Pr[0!=X in FI] <= min(1, 2/N(I)+(32n/s)^n),

which implies the requested constant256 statement. This has no smoothing hypothesis on F and does not condition out X=0. All constants and dual conventions will be frozen in a standalone theorem/proof.

The adaptive extension is a conditional estimate for each fresh draw given its complete pre-draw history, followed by a union/expected-count bound over every attempt actually made. Arbitrary selection after observation costs the whole attempt budget; selecting one successful draw does not give it the original small conditional success probability. Nonzero rejection changes the denominator from rho_s(F) to rho_s(F)-1 and has charged expected cost.

The C-v6 statement explicitly supplies v0>=2 sqrt(n) a. Together with w=sqrt(n) w_B and d0=delta*w/(32nkv0), this gives delivered coefficient width s_J>=32 sqrt(2) n^2 k a q/(delta w_B). Whether s_J>=512n^2 is a separate parameter substitution, not an unconditional consequence of the abstract oracle. A's concrete parameter file will be checked next.

Reservation H-ALIGN-FV1 was granted by root for one exact-rational finite-control job, <=120s and256MiB; not run yet. Controls will retain original finite denominators and CP-1, and will not pretend a finite truncation proves the full Gaussian theorem. Next constructive test: integer short relations among actual reductions of independent F-Gaussians modulo FI, with their exact pushforward law and full uniform comparator retained.
