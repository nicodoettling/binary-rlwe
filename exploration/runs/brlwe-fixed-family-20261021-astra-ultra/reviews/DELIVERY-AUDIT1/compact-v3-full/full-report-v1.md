# Fresh full review of FF3-COMPACT-SELECTOR-v3

Verdict: **PASS at the exact stated conditional mathematical and expected-cost scope**, with the explicit experiment-path binding in `coordinator/kernel-resource-v3-path-resolution-v1.json`. This is a fresh nonauthor statement-and-proof review, not a blind review or final coordinator acceptance. No unresolved mathematical defect was found in the reviewed v3 claim. The separate fresh theorem-only gate belongs to BLIND-RESOURCE4.

The reviewed statement is `coordinator/compact-selector-statement-v3.md`, SHA256 `20c66a210cfb4821eec35b371fbf7478ec3493d18d656a18a5b06dffc2fed889`; its proof is `coordinator/compact-selector-proof-v3.md`, SHA256 `8625e7453ae8d937ba9b885dd802a065987224862c70becbbc2713046c76a71f`. The proof's retained v1 heading does not identify different bytes. The v3 file contains the expected-bit correction and rational-M clarification. Earlier v1/v2 computational defects remain preserved and rejected at their original scopes.

## Exposure and check depth

The assignment and initial input manifest are preserved beside this report. Before this additional assignment I had read coordinator delivery/status material, the generic compressed-selector statement/proof, and BLIND-TRANSFER2's old fair-bit defect summary. I had not read or passed compact v2/v3's proof and did not author any version. I first read compact v3's statement and proof at 21:47 UTC, reconstructed their argument, then examined earlier complete exact finite-check reports and code to establish that the unchanged finite certificate could be reused. This is a disclosed full review, not a pristine theorem-only reconstruction. All reviewers use the same model; the scrutiny is correlated and is not formal verification.

I read the complete v3 statement and proof; checked the old v1 fair-bit and v2 M-encoding defects; read the original FV11 construction/checker code without executing it; compared the exact coefficient data against the frozen full-review inputs and sanitized theorem-only packets; inspected the full finite-check loops in BLIND-TRANSFER2's independent code; and read the matching full-review output. I did not rerun FV11, a solver, the 81-row endpoint enumeration, or all historical experiments. The new repair-specific checks below are exact hand calculations and a symbolic stopped-kernel invariant. The separate coefficient binding check is documentary exact arithmetic, not another feasibility experiment.

## Reconstructed normalized law and conditional history

Fix the entire input x, all supplied tables, and the rational M. Write e for a uniformly chosen cube edge and c_e=c_e(x). Equation (N) says the sum of G(c_e) over all edges is |E|. Therefore the mean G is 1, so M>=1. Each fresh trial, conditional on x and every previous failure history, has success probability

    sum_e G(c_e)/(|E| M) = 1/M.

This conditional equality is the needed invariant. The proof explicitly requires fresh trial tapes; there is no inference from a marginal rate or from independence before selection. At trial t the mass of accepting edge e and subsequently selecting (j,k) is

    (1-1/M)^(t-1) g(c_e,j,k)/(|E| M).

Summing over t gives g(c_e,j,k)/|E|. Zero-G edges have zero accepted mass; division by G is never attempted on such a branch. Termination is almost sure and the expected number of trials is M.

For every edge, v-u=X^i is a unit even at a composite modulus: X^n=-1 supplies its monomial inverse. The target coordinate map (c,d) -> (d-cu,d-cv) is consequently a bijection. Conditional on x,e,j,k the two H draws have exactly their declared independent full ring laws. Their joint atom is the product in (K). Summing those atoms over target pairs gives 1 for every edge/variant, and then summing the g weights gives 1 by (N). This proves row normalization on every possible input, including inputs having small or zero probability in a particular source experiment.

The separate endpoint equations P_s K=T_s and U K=V are essential. Input-dependent edge or variant selection changes the conditional distribution of the source residuals. The fact that each H_j separately maps noise and uniform correctly does not justify applying a two-secret argument after such selection. The statement explicitly adds the complete endpoint equations instead; its proof respects that distinction. Sampling a cube edge samples candidate labels, not the unknown true secret, and no source decoder or secret advice is used.

For a batch, fix one secret s before examining any samples or tapes. The source samples are iid conditional on that same s, and independent executions use fresh selector and H randomness. The output law is then T_s tensor k. Mixing once over the shared s gives the required shared-secret experiment. Redrawing s per row, reusing one selector/group tape across rows, or deriving endpoint products only after averaging s would be a different law. The comparator uses its own U K=V equation and independent tapes.

## New stopped-kernel invariant and rational-M controls

Let a_L=(1-1/M)^L. With a fixed fallback atom y0, the L-trial truncated kernel has the exact identity

    K_L(x,.) = (1-a_L) K(x,.) + a_L delta_y0.

Indeed each trial contributes the same success kernel K/M after multiplication by its conditional survival probability. This identity is pointwise in x. It yields TV(K_L(x,.),K(x,.))<=a_L<=exp(-L/M), including M=1 and all positive integer L. A one-sample-at-a-time coupling and union bound then yield k exp(-L/M) for the batch. No assumption about the secret posterior after previous outputs is needed. Additional approximate H or coin implementations require their own total row error, including their repeated uses; the statement expressly charges these separately. The exact invariant also confirms that changing the supplied upper bound M changes retry work but not the eventual kernel K.

For a new exact finite repair control, use the four edges of an n=2 cube, with G values (1/2,3/2,1/2,3/2), and supplied rational M=3/2. The normalization sum is 4. Each trial accepts with probability 2/3; the two low-weight edges have total accepted conditional probability 1/4 and the two high-weight edges have probability 3/4. With L=2, the low-edge, high-edge, and fallback masses are respectively 2/9, 2/3, and 1/9. They sum to 1 and agree with the stopped-kernel identity. This explicitly exercises a nonintegral encoded M; an integer-only implementation would not suffice for the literal v3 scope.

Now keep the initially drawn edge across retries, while using fresh acceptance coins. The one-trial marginal acceptance is still 2/3, but after a failure the retained edge is certainly low-weight. Two failures have probability (1/2)(2/3)^2=2/9, not 1/9, and expected trial count is (1/2)3+(1/2)1=2, not M=3/2. The v3 proof excludes this process through its fresh-trial condition. This new countercontrol tests the exact invariant rather than merely rechecking a marginal acceptance rate. It is not a counterexample to v3.

A zero-weight control uses G=(0,0,2,2), M=2. The first two edges are never accepted, the other two each have accepted probability 1/2, and no 0/0 variant distribution is evaluated. At M=1, pointwise G<=1 and average G=1 force G=1 on every edge, so termination on the first trial is consistent with all formulas.

CP-1 remains binding: its selected probability 21/2000 exceeds (1/10)^2 even though the later incidence is 21/221<1/10. Support deletion and renormalization defeat the old product argument. Here the entire fixed input and full previous retry history are conditioned on before the next fresh tape is drawn; the displayed conditional success is always exactly 1/M. No latent cache event or reused random value is called fresh.

## Exact finite coefficient evidence

The full FV11 equations are unchanged by either resource repair. `coefficient-binding-v1.json` independently confirms the following:

- The author selector table has SHA256 `140a8b92c3a772c217801f66f9d7618843330f0ca8264718858c3cfcf679cba8`; it is byte-identical to the FULL-FF3-PHASE2 frozen input.
- The radial kernel table has SHA256 `6d63ee7547c399c361f9883ac7432fee8115911b7c851a10012a83781e175665`; it is also byte-identical to that frozen input.
- Mathematical classes, variants, and coefficients are identical in the sanitized BLIND-TRANSFER2, BLIND-RESOURCE3, and BLIND-RESOURCE4 tables. Removing author status/provenance did not change the finite model. This check does not read or certify the latter reviewers' verdicts.
- There are exactly 33 strictly positive selector entries, 27 classes, and 16 kernel variants. Exact rational addition reproduces the stated maximum G and verifies G<3, so the explicit integer M=3 is a valid encoded choice.

The underlying finite model is n=2,Q=3,q=2. A source atom (a,b), at fixed s and residual zero-count z, has probability 14^z/2304. A target atom (c,d) with residual zero-count w has probability 3^w/64. The comparator masses are 1/81 and 1/16. The four H tables use denominator 43680 and target class multiplicities (1,2,1). These are the same exact coefficients used by both independently written finite checkers, whose loops include every one of the 81 source rows, every one of the 16 target atoms, all four fixed secrets, and the uniform comparator. The two reports record complete exact success, not just floating feasibility; the relevant stdout and code are bound in the supplemental manifest.

As a hand check of the radial data convention, the first kernel's source zero-count-zero row sums as 13020+2*7014+16632=43680. Its uniform-source output numerator at target zero-count zero is 4*13020+4*11550+0=98280=9*43680/4. Its noise-source numerator there is 4*13020+56*11550+196*0=698880=16*43680, giving target per-atom probability 1/16 after division by 256*43680. This checks the source class multiplicities, source normalization, and per-atom rather than per-class interpretation.

The original author checker uses floating optimization to find a support and then verifies exact Fraction equations. It was not executed here. The full and blind independent checkers reconstruct exact equations without relying on the solver status. Their unchanged finite evidence is reused only after the byte/data identity and loop-scope checks above. A finite rational law is not a discrete Gaussian or an asymptotic uniformly generated family.

## Computational accounting and rejected versions

The v2 issue is repaired: M is now a supplied positive rational with numerator/denominator bit lengths charged. For an encoded rational probability a/b, an exact fair-bit implementation samples a uniform integer below b using ceil(log2 b)-bit rejection and compares with a. The outer rejection has expected fewer than two proposals, so this coin has expected polynomial bit cost. No uncomputable real parameter is an algorithmic input. All weight construction, representation lengths, class evaluation, H sampling and rational arithmetic remain charged; efficient sampling of an arbitrary real H is not inferred.

A uniform cube edge can be sampled by choosing an index in {0,...,n-1}, then n-1 unbiased bits for the other coordinates. Rejection sampling for the index uses fewer than two proposals in expectation and O(log n) bits per proposal, hence total expected O(n) bits. For a power-of-two n the index is exactly sampled with log2 n bits and the total is worst-case O(n). At n=3 the 12 equal-probability edges require non-dyadic probabilities 1/12, impossible under any fixed fair-bit cap. The original literal worst-case arbitrary-n v1 reading remains rejected; v3 states the correct distinction.

Expected trial count M and encoded rational coins support the claimed expected cost, polynomial in numeric M and all relevant encoding lengths when the stipulated class/table/H routines are efficient. Merely charging log M would not suffice. The exponential number of cube edges need not be enumerated for one uniform edge draw, but no polynomial construction or bound for an all-dimensional endpoint table follows from that fact.

Capping the number of selector trials alone is **not** an all-tape runtime bound: exact rational coins, arbitrary-n index rejection, or stipulated H samplers may still have unbounded individual executions. The statement claims expected cost and a truncation TV bound, not a universal all-input deterministic time cap. Any implementation inside an all-input bounded reduction would need further routine caps and charged errors. The main draft must not promote this expected-cost result to a complete bounded FF reduction.

The pair-shell integer count defect belongs to ENERGY-v1, not this compact residual-product sampler. No single-shell bound is used to bound a pair-product rank here. Compact v3 samples two declared H outputs and uses a monomial inverse. It neither imports the rejected ENERGY count bound nor claims that arbitrary energy/rank retained state factors through the compact class.

## Dependency and delivery conclusion

No new external theorem or source-hardness assumption is used. The generic result is an elementary normalized-kernel calculation conditional on exact endpoint equations and efficient supplied subroutines. The finite instance uses the exact bound coefficient certificate identified above. The file-path ambiguity found during this review is resolved by the explicit v3 path-binding record; no mathematical statement bytes were silently edited. This exact v3 full review does not inherit the earlier reviewer's v2 computational pass.

There is no unresolved mathematical finding for compact v3 at this scope. Final acceptance still requires the coordinator to bind this report, the pristine BLIND-RESOURCE4 gate, exact inputs, path bindings, and dependencies. FF remains open, no source hardness is established, and this review makes no exhaustion or native-goal-completion claim. I started no experiments, workers, services, detached processes, or goals for this addendum; all foreground read/hash checks completed.
