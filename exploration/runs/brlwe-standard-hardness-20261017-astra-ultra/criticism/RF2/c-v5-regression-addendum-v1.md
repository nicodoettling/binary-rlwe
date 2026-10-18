# C-v5 regression addendum

PROVISIONAL claim-specific review of all51 imported regressions and13 current controls. Full exact entries, JSON pointers, registry hashes and entry hashes are preserved in the companion JSON. No experiment and no acceptance authority.

| ID | Disposition | C-v5 application |
|---|---|---|
| R01 | NONUSE | No binomial ideal sampler or structured-support hardness is used. |
| R02 | CHECKED | Fresh integral multipliers and additive Gaussian coins are independent conditional on the current query; the hidden center is fixed, not selected from those coins. |
| R03 | CHECKED | Each oracle call uses k fresh samples conditional on J and the current query; product comparisons occur only under this conditioning. |
| R04 | CHECKED | No scalar marginal Gaussian claim replaces a joint law: the full real multiplier-plus-noise density is completed before rounding. |
| R05 | CHECKED | All local sample coins are jointly fresh given the entire adaptive history; pairwise independence is not substituted. |
| R06 | NONUSE | C makes no entropy-to-extraction inference; its own source is an explicitly defined periodic Gaussian. |
| R07 | NONUSE | No Boolean-fiber bound follows from field rank; binary guessing remains a separate A dependency. |
| R08 | CHECKED | The comparison oracle depends on hidden e only as a proof object; the implemented query uses public T,g and exact integral r. |
| R09 | CHECKED | Decoding uses the explicit strict radius d0<q/(4D^(1/n)) and algebraic norm; no Lucas or occupancy claim. |
| R10 | SCOPE_LIMIT | A short basis is not supplied; existence of a BDD reduction does not certify that a restricted ideal source is hard. |
| R11 | CHECKED | Failures from OHCP, numerical errors and adaptive queries are charged additively; a good-J average is not promoted to every J. |
| R12 | CHECKED | Final verification has a strict uniqueness proof and exact lattice membership; it cannot accept a different nearby lattice point. |
| R13 | NONUSE | No signed Renyi transfer. Acceptance comparisons use TV and explicit orientation. |
| R14 | CHECKED | All integral multipliers, including zero and nonunits, remain in the sampler. Cancellation holds for each. |
| R15 | CHECKED | Fresh independent samples are generated per call; no rotated or repeated sample is claimed independent. |
| R16 | SCOPE_LIMIT | No original binary target is claimed statistically uniform, and no source hardness is inferred from smoothing alone. |
| R17 | NONUSE | No unrelated moment, QCSD, orbit or Fourier-speedup analogy supplies a proof step. |
| R18 | CHECKED_CP1 | Every adaptive loss holds conditionally on the full prior transcript and is summed. Marginal success products remain prohibited. |
| C03-HC1 | CHECKED | epsilon0<=1/16 gives positive denominators; no negative or unguarded theta ratio is used. |
| C03-HC2 | CHECKED | Posterior P is a full positive matrix; both original and posterior Gaussian normalizers are retained. |
| C03-HC3 | CHECKED | V,P,C denote quadratic-form width squares, not exact discrete covariance identities. |
| C03-HC4 | CHECKED | All samplers are positive kernels; the continuous comparison uses square completion, not exact signed deconvolution. |
| C03-HC5 | CHECKED | The full hidden-e conditional query law is used. Fixed nuisance widths are shared parameters, not independent hidden centers. |
| C03-HC6 | CHECKED_CP1 | Adaptive failures are bounded per history and summed; bad events are not assumed independent of successful decoding. |
| C03-HC7 | NONUSE | No repeated auxiliary S+G disclosure or uncharged scale change appears in C. |
| C02-LATENT-PUBLIC | CHECKED | Only forward data processing through modulo, common rounding and A is used; latent coins are not made public in the comparator. |
| C02-CHAR | CHECKED | Full-Haar convergence sums the entire scaled dual theta series using algebraic norm and packing; one character is not enough. |
| C01-ATT | SCOPE_LIMIT | No deterministic attack improvement or standard hardness premise is inferred. |
| CP-1 | CHECKED_CP1 | Original exact counterexample retained. C conditions on J,e,query and entire past before each TV bound; no sequential product rule. Fresh S/E and G/H guessing remain A-only dependencies. |
| NC1-v1 | CHECKED | All current theta denominators have explicit epsilon0<=1/16. Old rejected normalizer bounds are not imported. |
| S0-dependency | SCOPE_LIMIT | C-v5 is reviewed fresh. A/B source bridges and the restricted-family worst-case edge have separate status; no inherited acceptance. |
| PUBLIC-ENCODED-F | CHECKED | Public J is retained in every law; e is not disclosed by the actual oracle. No reverse projection-TV inference. |
| W2-SUBGROUP-BOUNDARY | NONUSE | No all-subgroup support coverage or occupancy theorem is used. |
| UNIFORM-APPROX-COLLAPSE | CHECKED | Benchmark uniform finite quotient is exact. Simulated planted query laws are explicitly approximate with complete charges; comparator and statistical simulation are distinct. |
| SE-CORRELATION-F3 | SCOPE_LIMIT | C uses no secret/error normal form. A-to-C composition requires independently verified fresh S and full target-error law. |
| W2-CONSTANT-COMPARISON | NONUSE | No optimized attack-constant comparison is claimed. |
| N02-DUAL-NUMBER | CHECKED | The finite quotient has exact order from lattice covolumes; C itself does not need gcd(D,q)=1. That condition belongs only to B identification. |
| PAIRWISE-SE-F3 | SCOPE_LIMIT | No pairwise-secret/error shortcut is introduced. Original binary guessing is a separate full-joint A premise. |
| N03-PV-CONDITIONING | CHECKED | Pointwise same-J advantage is assumed. An averaged advantage yields only good-ideal conclusions; no active-PV conditioning transfer. |
| N03-SCAL-POSTERIOR | CHECKED | Center-dependent posterior theta is divided by the actual original normalizer. Adaptive query kernels are analyzed after conditioning on history. |
| RECT-ALG-1 | CHECKED | Completion P=(V^-1+M_h^T M_h/w^2)^-1 remains valid for singular M_h, including zero coordinates; no invertibility of h is assumed. |
| SOURCE-SMALL-D | SCOPE_LIMIT | Even D=1 is allowed analytically; the theorem does not conclude this or another ideal family is hard. |
| A-PPT-LEDGER-SCOPE | CHECKED | C-v5 charges all scalar/basis/target encoding lengths and evaluation costs. Symbolic primary T_H is stated rather than an invented numeric exponent. |
| EX-PURE-MIX-ZERO | NONUSE | No pure-mixture seed dilution or elimination of zero mass. |
| EX-PUBLIC-TAPE | CHECKED | Multiplier, Gaussian and fallback coins remain internal; public transcripts retain only the declared quotient samples and J metadata. |
| EX-APPENDED-H | CHECKED | No comparison retains latent H alongside a supposedly independent completed error. H is a sampler-internal approximation variable. |
| EX-M3-CROSSBLOCK | CHECKED | Every sample comparison uses its full n-dimensional covariance and posterior. Across samples independence is conditional on fixed query, not inferred from marginals. |
| EX-RETAINED-M3 | CHECKED | J and hidden e stay fixed across adaptive calls; comparison bounds are uniform in this retained state. |
| B-JL-BZERO | CHECKED | w,d0,a are positive and epsilon0,delta,zeta have explicit domains; no division by zero or undefined width. |
| B-JL-REDRAW-T | CHECKED | Same ideal J and decoding target are used throughout all calls and orientations; no ideal redraw. |
| A-ERASURE-RANKMIX | NONUSE | C generates periodic queries from a BDD target; it does not erase ordinary RLWE multipliers into a fixed-rank source. |
| D-THETA-RETAIN-U-v1 | CHECKED | No local multiplier or Gaussian tape is retained with quotient samples. The proof-only comparison is not public metadata. |
| D-LSW-THETA-1 | CHECKED | C explicitly retains rho_P and rho_V and charges the separate finite multiplier normalizer error. |
| C-TOWER-RELATION-1 | NONUSE | The ring and degree are fixed; no tower embedding. |
| D-REUSED-PIVOT-1 | NONUSE | No pivot selection or reused failed input rows. |
| A-TOWER-LAW-1 | NONUSE | No radix multiplication or missing response programming. |
| C-SMALL-N-EXISTENCE-1 | CHECKED | All analytic inequalities apply for n>=2; no finite experiment is used to infer asymptotic existence. |
| D-NORMALFORM-WRAP-1 | NONUSE | No wrapped Gaussian secret is restricted to an integer cube. |
| RF2-OHCP-V1-LOGSHIFT | REJECT_V1_PRESERVE_CONTROL | v1 countercontrol remains valid. v5 shift2 yields center norm[1,3] and a nonnegative starting-scale shift. |
| RF2-OHCP-V2-ORIGIN-BALL | CHECKED_REPAIRED | Coherent v5 uses residual8d0 and a local comparison oracle that covers both required balls and equals the actual oracle outside. |
| RF2-IDEAL-SMOOTHING-PACKING | CHECKED_ANALYTIC_CONTROL | Independent full-dual packing bound supports exp(-nc^2); no unreserved experiment. |
| RF2-OHCP-V3-UNBOUNDED-INTEGER-REJECTION | CHECKED_REPAIRED | Each integer rejection has R_j attempts; at most nL_j proposals add <=tau_j/16, charged conditionally. |
| RF2-OHCP-WRONG-ORIENTATION-RUNTIME | CHECKED_REPAIRED | Both orientations have explicit time, logscale, description and call caps. Only the correct one uses the OHCP success promise. |
| RF2-OHCP-SCALAR-ENCODING-LENGTH | CHECKED_REPAIRED | v5 explicitly includes every numerator/denominator and evaluation-procedure input length and actual certified evaluation cost. |
