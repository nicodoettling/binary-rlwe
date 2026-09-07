# Shared parameter feasibility table — P2

Exactly two slots: A2 and B1. Every row uses the same law within its column. Results are provisional pending fresh criticism. Here ell=ceil(log2 n), L=ln n, kappa(s)=2 sum_(j>=1) exp(-pi*s*j^2). Gaussian exponent matrices are not exact integer covariance matrices.

| Requirement | A2: dense F-dependent completion | B1: inherited public shear |
|---|---|---|
| Ring/rank/basis | R=F_q[X]/(X^n+1), power-of-two n, rank one, coefficient basis | Same reference |
| Target | S has n iid fair bits; one (a,aS+E), uniform a; E wrapped iid D_sigma | Same desired target |
| Degree and quotient | d=floor(sqrt(n)/ell^4); eventually L²<=d<=sqrt(n)/L⁴ | Comparison at same d; no successful full regime |
| Prior dimension | A1 d=floor(n/ell³) archived; its extraction deferred | No source claim borrowed from A1 |
| Modulus and widths | gamma=tau=ell, b=ell², sigma=2n ell³; sigma n^c<=q<=n^K, q=1 mod 2n | Main gamma=tau=ell and same sigma; H00 width eta arbitrary in the obstruction |
| Nonempty prime sequence | Example c=1,K=16: least prime 1 mod 2n³, eventually by Xylouris; polynomial-in-n generation exists, no practical claim | Same availability does not repair noise |
| Ideal law | Uniform all d-subsets T; J zero on T, I=Ann(J) supported on T | Actual base law fixed; nearest HLBDD uses uniform d-subsets |
| Support entropy | log2 binom(n,d); quotient output d log2 q=Theta(sqrt(n)/L³)=o(n) | Same necessary budget, no sufficiency inference |
| U law | Direct independent uniform nonzero active coordinates; d log2(q-1) bits; isomorphism exact | Uniform I for exact nearest HLBDD law; d log2 q bits |
| U failure/conditioning | eta_iso=0; changing to uniform I changes the source | eta_iso=1-(1-1/q+1/q²)^d, nonnegligible at polynomial q. Active conditioning changes source |
| V law | Independent uniform I given J; d log2 q bits | V=V0+LU remains independent uniform I given J |
| F law | Exact iid integer D_ell conditioned on [-b,b]; entropy n H(F_scalar)<=n log2(2b+1) | Exact base iid D_gamma, independent H00,L,W; wrapped fiber masses used |
| H law | Exact sequential DG kernel H_seq from canonical coefficient-order LDL of B=sigma²I-tau² M_F M_F^T | H=H00+LF+W; main iid L=-G', independent of bridge G; H00,W independent of F,L,G given J,U |
| H entropy/support | True conditional sequential entropy; integer support unbounded. Finite approximation has polynomial bounded centers and radius n sigma+2 | True joint shear law; no marginal-width replacement |
| Public transcript | Only (U+F,V+H) plus parameter descriptions | Exact public map (a,c0)->(a,c0+La+W) |
| Efficient source sampling | Uniform CRT/support operations and polynomial-precision DG tables; exact mathematical law approximated within xi_src | Public transform of specified base; inherits its precise U/noise law |
| Auxiliary / Y | G iid D_ell independent of source; public fresh Y=S0+G0 uses no challenge secrets | Same; source's private G' cannot be reused |
| Operator and smoothing | ||M_F||<=n ell², tau²||M_F||²<=sigma²/4; B>=3sigma²I/4, Theta>=3ell²I/4 | Unwrapped PSD increase only diagnostic; actual retirement uses wrapped character inequality |
| Noise condition | Retain J,U,F; integrate H. eta_N<=delta/(1-delta)+eta_seq; delta<=(1+kappa(3ell²/4))^n-1 | At main widths eta_N >= (1-pi/16)exp(-2pi)/(96 n²ell⁴(1+ell)), even with arbitrary independent broadening |
| Noise scope | Negligible strong latent error for exact H_seq | Inverse-polynomial lower bound retires negligible-error independent iid-shear route; not every public simulator or finite-advantage route |
| Extraction condition | Retain J,U,F,H,Y. eta_X <= .5 exp(-c_K n/(d L⁶)), uniform every T | Same extraction theorem cannot repair failed noise |
| Statistical event costs | No support rejection, no exceptional prime/support mass, no U failure. F is defined as truncated; compare untruncated only with its tail | Uniform-U rank defect and independent sampling errors explicitly charged |
| Implementation cost | Add 2xi_src+2xi_1+xi_Y+xi_target at bridge level. Eta_seq only in noise, no double charging | Same implementation accounting plus uniform-U defect if that source is retained |
| Computational source evidence | P0-A2 OPEN: exact active-U, F-dependent H_seq pair has no matching established source reduction | Exact public source reduction retained; base HLBDD assumption is nonstandard and its original width/regime differs |
| Attacks | Grouped-orbit exp(O_c(d)) route with solver-success probability explicit; unique first-mask decomposition does not give an efficient decoder; fixed-character tests separately checked | Noise obstruction is not a public source distinguisher |
| Bridge advantage | Two potentially different source advantages + eta_N + eta_X + implementation costs | Same formula, but nonnegligible eta_N and possibly eta_iso remain |
| Multiple samples | NEW common-K source, full stacked H_seq and cross blocks; sigma_m=sqrt(m)*sigma; one shared Y | No expansion follows from a single source pair |
| m and q | Prescribed m(n); sigma_m n^c<=q. For m=n^r numerical K>1+c+r/2; split-prime example needs sufficiently larger K | No compatible polynomial-m source established |
| Separate observations | A2: m=C tau² ln n, C>2/pi, already forces extraction TV to 1-o(1); auxiliary exposure only | Cannot replace shared secrets by independent quotient variables |
| Task consequence | REC gives Adv_dec,m>=epsilon_rec-m delta_T-2^n v_T^m. Baseline residual box makes losses negligible; zero held-out samples suffice IF decision premise holds | Retired noise route gives no completed decision/search hardness theorem |

A2 has a provisional nonempty **analytic** regime. No common regime including independently supported exact source hardness has been established. A1 dimensions, B1's source inheritance, A2's H kernel and m-sample variants cannot be assembled into a single construction.
