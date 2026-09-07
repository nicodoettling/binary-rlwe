# Shared parameter feasibility table — P1, development checkpoint

The portfolio has exactly A1 and B1 (selection.md). No row may borrow another source's marginal noise law or parameter regime. Statements remain provisional until fresh review. Let ell=ceil(log2 n), and retain the coefficient basis throughout.

| Requirement | Candidate A1: correlated completion | Candidate B1: inherited public shear |
|---|---|---|
| Ring/rank | R_q=F_q[X]/(X^n+1), power-of-two n, rank one | Same |
| Modulus/target | Fully split prime q, 2n ell^3 n^c <= q <= n^K; target sigma=2n ell^3 | Same baseline; other public sigma choices require explicit inequalities |
| Secret/sample | n iid fair coefficient bits; initially one ring sample | Same |
| Support/quotient | Uniform d-subset of n roots; J vanishes on support, I=Ann(J) supported there; quotient and I dimension d | Same support comparison, actual base-source law fixed |
| Current d | Initial d=floor(n/ell^3) has OPEN extraction. D01 proposes replacing it by log^2 n <= d <= sqrt(n)/log^4 n; no support rejection, pending frozen proof | No independently successful full regime yet |
| Support entropy | log2 binom(n,d) bits; polynomial enumeration fails at chosen growing d, but exp(O(d)) attack exists under its stated margin | Same support entropy; source inheritance is not extraction |
| U law/entropy | Direct nonzero active coordinates: d log2(q-1) bits, eta_iso=0 | Uniform I for exact nearest HLBDD import: d log2 q bits, eta_iso=1-(1-1/q+1/q^2)^d. Active conditioning changes source |
| V law/entropy | Independent uniform I given J; d log2 q bits | V=V0+LU is independent uniform I given J after the public shear |
| F law/entropy | iid D_ell restricted to abs(F_j)<=ell^2. At most n log2(2ell^2+1) bits; actual conditioned-DG entropy used where needed | Base iid D_gamma, main gamma=ell; independent of base H00, L and W |
| Exact H law | H_seq has the explicit adaptive LDL DG kernels for B=sigma^2 I-tau^2 M_F M_F^T; H_impl is its specified approximation, with source-law convention being clarified | H=H00+LF+W, all base/public randomness specified; L=-G' is the main failed-cancellation test |
| H entropy/support | Actual conditional sampler entropy, not n independent DG entropies. For truncation radius n sigma+2, abs(H_j) <= (1+sqrt(n/a))(n sigma+2), a=3/4, so its finite support gives an explicit entropy upper bound | Must use the true convolution/shear joint law; widths alone do not determine entropy/correlation |
| Public variables | Only (A,C)=(U+F,V+H), public parameter descriptions; J,U,V,F,H hidden | Same; public map can generate L,W without hidden challenge data |
| Auxiliary law | G iid D_tau, tau=ell, independent of source; reduction samples fresh Y=S0+G0 | Same; cannot reuse the source's private G' |
| Entropy budget | d log2 q=o(n) in proposed smaller range; exact conditional extraction must still be proved | Same necessary budget does not repair completion |
| Operator/slack | norm(M_F)<=n ell^2; tau^2 norm(M_F)^2 <= sigma^2/4; exponent matrices B>=3sigma^2 I/4 and Theta>=3tau^2 I/4 | Unwrapped covariance adds PSD terms; wrapped obstruction is being derived separately |
| Noise comparison | Retain J,U,F and integrate H. eta_noise <= delta/(1-delta)+eta_seq+eta_impl; delta <= (1+kappa(3ell^2/4))^n-1 = exp(-Omega(log^2 n)) | D02 two-F-fiber character inequality gives a proposed inverse-polynomial lower bound even with independent broadening W |
| Extraction comparison | Retain J,U,F,H,Y; source independence extends a bound jointly with J,Y. D01's proposed theorem is uniform over support, averaged over Y | Same extraction cannot compensate for a failed noise edge |
| Statistical/bad-event costs | No U-conditioning failure. F restriction vs untruncated law and finite sampling precision are charged if comparison is made. Exact implemented-vs-ideal convention cannot be ignored | Uniform-U eta_iso is nonnegligible; independent source-map Gaussian sampling errors must be charged; noise lower bound is not a harmless negligible term |
| Source evidence | Exact correlated pair hardness OPEN/tailored; no checked reduction from independently noised HLBDD | Public transform inherits the exact base-source advantage; base HLBDD is an existing nonstandard assumption in its own law/regime |
| Bridge losses | Two potentially distinct source advantages + eta_ext + eta_noise (+ explicit implementation terms) | Same, plus eta_iso when retaining uniform U |
| Attacks | Binomial control broken; grouped-super-support exp(O(d)) decoding if q^(1-d/r)>=8n^(1+epsilon)b, r=Theta(d); short multipliers, pair combinations and true Fourier correlations checked as criteria | Same source attacks plus a proposed finite wrapped-noise incompatibility |
| Multiple samples | D03 requires a NEW common-K source, full mn-dimensional H kernel and explicitly sigma_m≈sqrt(m)sigma_1 for conservative slack | No sample expansion inherited from a single source pair |
| Search/decision | One-sample decision plus residual self-verification bounds one-sample exact recovery; polynomial m needs its own m-sample decision premise | A failed/noisy conditional edge is not a search hardness result |

Here kappa(s)=2 sum_(j>=1) exp(-pi s j^2). Gaussian exponent matrices are not the exact covariance matrices of the integer distributions. All asymptotic statements use fixed polynomial exponents and qualifying split-prime sequences; no practical concrete security estimate is supplied. A common analytic extraction/completion regime, if D01 survives, would still leave exact source pseudorandomness as an unproved requirement.
