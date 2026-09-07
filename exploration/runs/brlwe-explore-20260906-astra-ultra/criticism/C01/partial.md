# C01 critic checkpoint

Started 2026-09-06 10:30 UTC. Critic is a fresh nonauthor but received the candidate proof and the coordinator's suggested Fourier obstruction; this is not a blind review or statistically independent evidence. Deadline 11:00 UTC. No experiment was allocated or run.

Read target.md, candidates/C01.md, candidates/C01/calculations.md, candidates/C01/source-checks.md, candidates/C01/partial.md, and scouts/S04.md. Read the mathematical-proof-audit skill and its audit protocol and probability regressions. Primary PDFs checked directly: Breuillard–Varju arXiv:1909.09053v2, printed pp.3 and 7–9; Order-LWE ePrint 2018/494, printed pp.11 and 37–41.

No defect found in the exact wrapped posterior factorization, averaged collision identity, effective Bernoulli comparison, or uniform asymptotic deduction. The imported Theorem 5 really is uniform over qualifying primes, multipliers, and prime-dependent two-point step laws. The polynomial-time binomial-mask decoder is valid even with hidden a and correlated bounded perturbations. Thus extraction remains a diagnostic and the matching public sampler's hardness premise is refuted.

The proposed additional Fourier obstruction works for auxiliary widths in a fixed compact positive interval, under explicitly independent sampler coins and independent additive completion H. A finite bound on every centered coefficient is

`max_k |center_q(F_k)|^2 <= (pi*sigma^2 + 2*q^2*epsilon)/(16*D_tau(1))`.

Here epsilon is conditional TV from the desired wrapped product error law. Joint TV with sampler coins gives a high-probability version by Markov's inequality. Details and scope will be preserved in additive-obstruction.md. This does not yet resolve the original next lemma uniformly for growing tau, or simulators needing only the public transcript marginal to be correct.

Additional precision: under the actual fixed polynomial q bound, uniform active-coordinate noninvertibility is inverse polynomial rather than merely potentially non-negligible. Rounding log^3 n to a power of two guarantees some fixed factor-two size band, not an arbitrary preassigned narrow band; the candidate's conditional quantifiers remain valid.

## Completed 10:41 UTC

The complete report is [../C01.md](../C01.md), and the bounded calculation is [additive-obstruction.md](additive-obstruction.md). Both were reread for signs, constants, conditioning, asymptotics, and scope. The report adds the requested residual-entropy distinction: an elementary leakage chain rule already preserves linear average conditional min-entropy for an o(n)-bit quotient; C01 contributes the stronger distributional near-uniformity useful only if a decision hybrid can be supplied. An exact `C=G` counterexample records why the completion lemma requires coins that preserve the conditional iid Gaussian law. No external experiment or further investigation was performed. No candidate, runner, manifest, or coordinator file was edited.
