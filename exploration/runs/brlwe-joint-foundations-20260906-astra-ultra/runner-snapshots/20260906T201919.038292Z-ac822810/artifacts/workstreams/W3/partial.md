# W3 checkpoint

Assignment W3-v1; canonical agent ID `/root/w3_observable`. No session/thread UUID is exposed by the available interface; none is inferred. Start observed at 2026-09-06 20:00:30 UTC; task deadline 2026-09-06T21:19:15Z. No CPU experiments allocated or run.

Checkpoint 2026-09-06 20:05 UTC (approximate minute label). Intake includes frozen target/source, audit skill/references, full bridge and theorem packet, A2/B candidate definitions, completion, D02 and review packet, R01, C02 review, C03 hand controls, and the consolidated report/reconciliation. Consolidated claims JSON and imported detailed controls are being completed in bounded output chunks; no unread truncated output is counted as read.

Material result W3-OBS-v1, PROVISIONAL: use the independent-noise source `(A,C)=(U+F,V+E_sigma)`, rather than publishing the F-dependent completion kernel. Public source tests are `B1(a,c)=D(a,aS0+E0)` and `B2(a,c)=D(a,aS0+c)`, with fresh binary S0. A full public pair chain is

`(a,aS+E) -> (U+F,(U+F)S+E) ~ (U+F,US+F(S+G)+H_seq) ~ (U+F,UZ+F(S+G)+H_seq) ~ (U+F,V+F S0+E) = B2(source) -> uniform`.

The first and last computational edges use B1 and B2. The statistical costs are `2 eta_N+eta_X` for active U. After extraction the original S is discarded; only the independent public marginal Y survives, so one can represent it as a fresh S0+G0 independent of the source and Z, then apply the second completion comparison. No posterior resampling with the old S retained is used. H_seq is proof-only and is never part of the assumed source; its own mathematical law still obeys the checked NC1-v2 guard.

For uniform U, the same construction pays exactly the usual averaged image defect `eta_iso=1-(1-1/q+1/q^2)^d`. A primary-source read of Order-LWE 2018/494 Definitions 7.3–7.4 and Lemma 7.7 confirms uniform ideal points and independent equal-width Gaussian noise; its original H3 uses super-polynomial q for negligible unit failure. Public Gaussian broadening of the second component can reach E_sigma with negligible convolution error, preserving the comparator and U law. Thus the correlated-source gap can be removed from a conditional finite comparison, but the present route has not eliminated active-unit/rank loss in the fixed polynomial-q regime. An active-HLBDD variant would remain a new unsupported premise until independently reduced. The scope is one sample only.

Sent this material result to the coordinator. No experiment requested or run; no policy interruption observed in this task.

Additional material result W3-RANK-v1, PROVISIONAL: the residual rank cost can be proved to survive the actual public projection in the subregime `c>1/2`, including the previously selected c=1. Let `R=ceil(sigma ell)`, `B=nb+R`, and `delta_E<=2n exp(-pi ell^2)`. Under strict gates `q^(1-2d/n)>2b sqrt(n)` and `q^(1-d/n)>2B sqrt(n)`, the public pair laws P=`(U+F,(U+F)S+E)` and Q=`(U+F,V+F S0+E)` for uniform-in-I U obey

`TV(P,Q) >= max(0, eta_iso-2 delta_E)`.

The public test is unbounded: find the unique box-bounded F decomposition of A, recover U and its actual CRT support W, require |W|<d, and test whether the response lies in I_W+Box(B). In P it accepts on every deficient branch with bounded E. In Q and on bounded E, acceptance implies V in I_W: otherwise the difference of two B-bounded coefficient vectors would be a nonzero integer polynomial supported modulo q on at most d roots, contradicting cyclotomic norm divisibility by q^(n-d). Conditional on U,T, V lies in I_W with probability q^(-(d-|W|)). Averaging yields exactly the old eta_iso, now via an explicit public observable rather than a latent lower-bound assertion. This is not a PPT attack. For 0<c<=1/2 this particular norm gate is not established; no universal public-map impossibility follows.

The full independent-noise observable hybrid remains valid and removes the correlated H_seq computational source obligation. Its uniform-U literal HLBDD instantiation is a finite transfer with an inverse-polynomial statistical gap in c>1/2; the active-U independent source is still an unsupported computational assumption. The coordinator has received both claims for prompt reconciliation and fresh review.
