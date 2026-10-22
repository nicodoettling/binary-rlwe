# Exact source parameters and direct algorithms, v1

Author reconstruction, 2026-10-21. PROVISIONAL new classification; accepted DD inputs are reused only at their recorded scope. DD means `exploration/runs/brlwe-direct-decision-20261021-astra-ultra`.

## Accepted radius, without suppressing losses

From DD/coordinator/fixed-main-statement-v2.md and am-main-theorem-v3.md:

```
epsilon0 = epsilon_*/2
epsilon  = epsilon_*/4
delta    = epsilon_*/16
eta_ext  = epsilon_*/256
Lcal  = ceil(log2(1024(n+1)/epsilon_*))
Ltest = ceil(log2(1024 Qmax/epsilon_*))
Ncal  = ceil((32768 n²/epsilon_*²) Lcal)
Ntest = ceil((32768 n²/epsilon_*²) Ltest)
K     = k0 (Ncal+Ntest)
ell   = ceil(log2(2nK))
d0    = epsilon_* ell²/(1024 n K chi)
r     = epsilon_* ell²/(1024 n K chi Qmax)
B     = 1/(2r) = 512 n K chi Qmax/(epsilon_* ell²).
```

The source is ordinary-basis J with D=N(J)<=2^(rho n), rho<1, and target T=lambda+e with lambda in J^-1 and canonical infinity error <=r. The pointwise success is 1-p, p=(n/2)exp(-kappa)+zeta<=17zeta/16. Auxiliary Qmax is a NUMERIC parameter; K counts physical samples, not D0 calls. The full D0 call bound is M Q_* ((n+1)Ncal+Qmax Ntest).

The auxiliary widths are sigma_q=(q/q0)sigma0, with sigma_floor=8n² ceil(sqrt(Kn))ell⁴ and Qmin>=n sigma_floor. Thus Qmax>=8n³ ceil(sqrt(Kn))ell⁴, and the displayed r is strictly below 1/(2sqrt(n)) throughout the finite accepted parameter domain. This inequality needs no asymptotic estimate.

For fixed k0<=n^b, epsilon_*=n^-c, fixed/inverse-polynomial zeta and polynomial-value auxiliary list, K=O(n^(b+2c+2)log n), ell=O(log n), chi=O(sqrt(log n)). Retain actual Qmax in every comparison. A big-O upper bound on K alone must not be inverted into a two-sided radius estimate. When k0=Theta(n^b), Qmax=n^Theta(1), the exact counts give K=Theta(n^(b+2c+2)log n) and r=Theta(n^(-b-3c-3) sqrt(log n)/Qmax), up to the chosen chi=Theta(sqrt(log n)); the finite expression is authoritative.

## Direct deterministic decoding table

| Source regime | Available ordinary-input algorithm | Exact sufficient radius | At accepted r |
| --- | --- | --- | --- |
| Quotient exponent e (least positive integer in J) | Compute e by HNF/SNF; round eT coefficientwise and divide by e | 2er<1 | Easy whenever e<B |
| Upper-column HNF maximum diagonal h | For ideals h=e, since H11=e and every diagonal divides e | Same 2hr<1 | Same region, not a stronger ideal test |
| A computed/supplied nonzero f in J | Round fT coefficientwise, divide by f in Q[X]/(X^n+1) | 2r||f||_coef,2<1 | Easy whenever ||f||<B; acquisition cost charged |
| Polynomial NUMERIC D | Enumerate D+1 binary vectors in h0=ceil(log2(D+1)) coordinates; obtain nonzero ternary f in J | 2r sqrt(h0)<1 | Always easy at accepted r, even if D>=B; time polynomial in D and input bits |
| Exponential D but e<B | Same exact exponent algorithm | 2er<1 | Includes entire small-characteristic high-index families |
| Prime ideal of characteristic p, degree f | Its exponent and HNF maximum are p; D=p^f | 2pr<1 | Easy for p<B regardless of f; p>=B remains unclassified by this test |
| Polynomial BIT LENGTH D or e only | No numeric enumeration bound follows | None | Not classified by encoding length |
| Existential short f/basis only | No acquisition algorithm supplied | None | Not classified by existence |

These are BDD algorithms, proved directly, not reversals of a DGS simulation. They do not use a distinguisher or a Gaussian oracle. New theorem/proof versions will state exact algorithms and useful remaining-family restrictions. No hardness conclusion follows from failing a row.

## DGS boundary

No DGS comparison is used to justify the table. If the accepted finite quantum interface were newly composed, coefficient radius r/sqrt(n) for L=J^-1 would give coefficient width W_new=n/(sqrt(2)r) on conjugate(J), then J after conjugation. Its error and code-access conditions must be re-instantiated and reviewed; this sentence is a dimensional calculation, not an accepted new sampler theorem. Even a proved easy sampler at W_new would not imply a BDD algorithm.
