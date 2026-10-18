# Exact C9 repair and full integration review

Worker A, 2026-10-17 22:06 UTC. Nonauthor review; not a blind referee. This report evaluates the current bytes and does not inherit acceptance from C7 or C8. C8 was rejected. No author file was edited, no blind material was accessed, and no experiment was run. File hashing and exact-diff preservation were ordinary read/documentation operations.

## 1. Frozen inputs and verdict

The coordinator freeze manifest and independently recomputed hashes agree:

| File in coordinator/c8-repair | SHA256 |
| --- | --- |
| multiplier-ohcp-theorem-v8.md | 857a62e9f4a937a80e5cb3b115c8b132abf122c16665d29b39dcb62bde86fe0a |
| multiplier-ohcp-algorithm-v2.md | 4361c90a7fa7cfe25d0ab3e8cd5c5333fb474cf1fb764375e10c29fca5102735 |
| multiplier-ohcp-proof-v9.md | e9b3023715a3d4ec90c474aba6945223aa376248b1fa216134964a5643fb4c5f |

**PASS for this exact classical, conditional, pointwise finite BDD theorem and its algorithm/proof integration. C8-FV1 is repaired.** Coordinator reconciliation and the separate blind gate remain independent obligations. This verdict supplies no standard arbitrary-ideal hardness edge, no new acceptance of external dependencies, and no quantum coherent-access theorem.

The original C8 defect remains preserved in workers/A/c8-review/finite-verification-gap-before-repair-v1.md and the coordinator copy C8-FV1-before-repair.md. The original full C8 report, SHA256 ae42d46e2e17b09886a17511e60adb14e2aafdf4371bf5c7a838f8deeebf7c95, remains a rejection of its original triple. It is not retroactively relabeled.

## 2. Complete diff audit

The three complete unified diffs are saved as theorem-exact-diff-v1.patch, algorithm-exact-diff-v1.patch and proof-exact-diff-v1.patch. diff-manifest-v1.json binds every old/new file hash and each diff hash. All differences were read. They consist of version labels, scope/dependency references, the new algorithm Section 8 rational test, and its matching proof Sections 7.4–7.5. No source law, Gaussian width, guard, sampler, walk, oracle-call count, approximation budget, promise, or claimed success probability changes.

The current theorem and algorithm were read completely; the current proof was read in bounded chunks, with the complete diff checking the unchanged portions against their original bytes. The mathematical dependencies below were rechecked against this current statement. A whole-file read initially exceeded the combined output budget; subsequent bounded reads covered the omitted middle of the proof. No unseen truncated output is treated as reviewed.

## 3. Independent arithmetic for the rational repair

Write d=d0>0, x=log2(64/d), p=max(0,Up(x)+2), epsilon=2^-p. Since Up(x)>=ceil(x)>=x, one has p>=x+2 for every x, including when x+2<=0. Therefore

    epsilon <= d/256.

There is no special unproved case when p=0. That case forces d>=256 and hence epsilon=1<=d/256. The possible one-unit extra value from Up only strengthens the inequality.

For any certified rational c with |c-d|<=epsilon, the defined rational lower bound and threshold satisfy

    d_lower=c-epsilon in [(127/128)d,d],
    threshold=3c/2 in [(765/512)d,(771/512)d].

In particular d_lower is strictly positive. The residual interval width d_lower/8 is a positive rational. Every final branch compares two exact rationals. Equality of those rationals is decidable by ordinary integer arithmetic and the specified <= rule; there is no refinement until an unknown real sign becomes nonzero.

On the BDD promise, the true lattice point has every residual modulus <=d. Its certified interval upper endpoint is at most d+d_lower/8<=9d/8. Since 9/8=576/512<765/512, it passes even at the worst permitted threshold approximation.

The canonical infinity distance between distinct lattice points is at least q/D^(1/n)>4d. Consequently a wrong lattice candidate has at least one residual modulus >3d. Its certified upper endpoint is at least that modulus, whereas the threshold is at most771d/512<3d. It fails. These are deterministic statements; the repair adds neither a failure probability nor an oracle call.

The implemented test is not claimed to decide exactly whether an arbitrary off-promise residual is <=d or <=2d. It is a bounded rational acceptance rule with the needed completeness and uniqueness on promised inputs. That scope is sufficient for the theorem.

## 4. Finite boundary falsification attempts

These are exact hand calculations, not machine experiments or evidence of exhaustive testing.

| Exact d | Possible p from the defined Up | Largest epsilon/d | Disposition |
| --- | --- | --- | --- |
| 1/256 | 16 or 17 | 1/256 | Small-width precision has the required relative error. |
| 1 | 8 or 9 | 1/256 | Both extreme c values give the displayed threshold interval. |
| 256 | 0 or 1 | 1/256 | The transition to the max-with-zero branch is safe. |
| 512 | 0 | 1/512 | No positive precision is needed for the relative guarantee. |

For d=1 and the extreme c=255/256, threshold=765/512 while the true residual upper bound is only9/8; there is positive slack. For c=257/256, threshold=771/512 while every wrong residual exceeds3. These are the two worst threshold directions.

The C8 finite-precision obstruction used U=1 and real thresholds x_+=1 versus x_-=1-2^(-B-2), which can have identical certified B-bit approximations but opposite exact comparison outcomes. The new algorithm never asks for that predicate. For d=x_+/2 or x_-/2, its rational threshold is below1, so U=1 is rejected in both cases without distinguishing the two real values. A final interval upper endpoint exactly equal to the computed rational threshold is accepted immediately by a rational comparison. Thus both the near-equality and equality stopping regressions are explicitly resolved.

## 5. Input evaluation and all-target runtime

The repair uses the already specified certified logarithm and Up routine once to obtain an integer precision, then one evaluation of d at that precision. It does not run a sign-detection loop. The rational threshold and positive rational interval tolerance then completely determine the remaining arithmetic. All operations remain finite for arbitrary rational targets and arbitrary oracle answer transcripts, while the scalar-domain/evaluation premises stay in force.

The needed precision has an explicit bound from the existing parameter promises. The formula for a0 simplifies to

    a0=D^(1/n) w [delta/(32nk)]^(2/n)/(nq).

From kappa>=4S one gets a0>=exp[-kappa/(2n)]. Since n>=2, D>=1, nq>=1 and 32nk/delta>=1, this implies the coarse bound w>=2^(-kappa)/D. Also kappa>=2/delta implies delta>=2/kappa. Obtain any certified positive integer V>=v0 by evaluating v0 to absolute error1 and taking an ordinary rational upper ceiling. Then

    d0 >= 2^(-kappa)/(16 kappa n k D V).

It follows that p_test is at most kappa+ceil(log2(1024 kappa n k D V))+4. The size of V is already charged through the scalar evaluation/output-bit contract. At the other end, the uniqueness parameter gives d0<q/4, so c_test's integer part also has a bound from ordinary input bits. Thus this repair does not introduce an unaccounted arbitrarily deep relative-precision request.

Each residual is the modulus of a finite canonical embedding of a rational coefficient vector. Certified fixed-width intervals follow from finite-precision arithmetic in roots of unity and square root; near zero does not require an equality test. Their required precision is bounded by the rational vector's bit size and log(1/d_lower), which is covered above. All computations are deterministic postprocessing, so the transcript's existing TV budget contracts rather than increases.

## 6. Current dependency and regression dispositions

| Current dependency or regression | Recheck on the frozen current triple |
| --- | --- |
| Exact source and comparator | k iid Q_h(G_w) mod qJ^-1 versus iid uniform in F, same public ordinary J. Pointwise advantage is required. No changed endpoint or added advice. |
| Quotient and coefficient normalization | |F|=q^n D^(n-1)P^n; canonical width w becomes coefficient width w/sqrt(n); rounding is a common observation kernel. |
| Integral cancellation and Gaussian completion | r lambda in qJ^-1 holds on every fallback. Both original and translated posterior theta normalizers remain in the density ratio; TV bound epsilon0/(1-epsilon0) is uniform in the selected width. |
| Conjugate dual and full spectrum | L*=conjugate(J)/(nq); algebraic norm plus packing bounds the complete theta sum. Exact Haar convergence belongs only to the continuous proxy. Persistent physical characters remain allowed. |
| Shifted centers and global orientation | Center2+e_j/d0 covers zero coordinates. The origin gap differs from the same spherical benchmark by <delta/16 for all pairs, so two global orientations suffice. |
| Finite comparisons and deterministic counts | Grid/endpoint/Hoeffding allowances retain the same slack; each comparison uses2(G+1)N calls, each walk T_walk+1 comparisons, totalQ_*=nQ_H. |
| Causal walk / CP-1 | The corrected process is adapted to its complete past. Fresh proposals have conditional progress probability >=1/(10Kd_H). Azuma and a first-bad-event union avoid conditioning on future correctness. The CP-1 posterior/support counterexample is not bypassed by marginal multiplication. |
| Near-center event | The positive interval endpoints on a chosen line have product r^2-epsilon^2; the radial line maximizes their ratio. The minimum-step and union bounds remain valid. |
| Std, scalar and ellipse samplers | Std supplies positional coupling, not impossible discrete-to-continuous raw TV. Both convolution normalizers are retained. Capped rejection and integer fallbacks are included; multiplier numerical loss <=tau/4 plus its fixed theta term. |
| GridGaussian and mean error | Actual rounded-law sampling is checked by the true-CDF boundary union; no monotonicity assumption is imposed on bad approximate thresholds. Mean/tail/grid errors and global counter sums fit their budgets. |
| Finite walk coupling | The physical kernel is globally Lipschitz. Analytic-to-physical, real-to-dyadic, then finite-sampler coupling avoids a continuity assumption on the analytic patch. |
| Success/noise dependence | Exceptional mass is subtracted additively. No recovery-success times noise-good product is used. |
| Reconstruction | Existing coefficient error plus q/(64D) stays below q/(2D), giving exact lattice-grid rounding. The repaired rational test has the strict margins proved above. |
| C8-FV1 | RESOLVED for these new bytes; original rejection and comparison countercontrol remain preserved. |

The causal progress count, fixed two-normalizer charge 2kQ_*epsilon0/(1-epsilon0)<zeta/16, summable numerical charges, and walk-position perturbation were rechecked together. The revised deterministic final test preserves the claimed success probability at least1-(n/2)exp(-kappa)-zeta. No unchanged claim is accepted merely because an earlier version named it.

The earlier C-OHCP-2 finite profile/adaptive-TV controls remain supplementary bounded controls, not proof of the Gaussian or walk estimates. The new repair is deterministic, so the targeted boundary calculations above add no probabilistic premise requiring a fresh random experiment.

## 7. Scope after this pass

This closes A's exact repair/reintegration gate for the frozen theorem-v8 / algorithm-v2 / proof-v9 triple. It does not certify B's separate Gaussian-periodic simulation, A's separate actual-secret composition, or a coherent quantum implementation. The theorem's quantum BDD-to-DGS paragraph remains a conditional same-ideal normalization statement with separate error obligations. No class-changing reduction into the bounded-index family has been established. The original standard computational foundation remains OPEN.
