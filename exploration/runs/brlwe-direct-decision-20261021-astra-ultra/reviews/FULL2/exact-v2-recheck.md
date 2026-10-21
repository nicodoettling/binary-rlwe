# FULL2 exact FIXED-MAIN-v2 recheck

PASS within the stated restricted-source, fixed-sample/advantage-exponent, all-input bounded classical-code scope. This is a separate post-seal amendment audit. The complete mathematical, source and complexity audit remains in `full-report-v1.md` and `source-complexity-report-v1.md`, sealed by `seal-v1.json` with SHA256 `72fc3e7fae66041f0d9b23b4c5e36634963daa504bfff828bf700d00303b5d5d`. The v1 rejection is preserved; it is not retroactively relabeled.

The exact new statement is `coordinator/fixed-main-statement-v2.md`, SHA256 `25da2502104e746d3e9f2ca10e3d070372ff95b853b1fd2b0e6c96b1b909ecb6`. The exact new proof is `coordinator/fixed-main-proof-v2.md`, SHA256 `2e98d25b0f349e22dfeb23ba5ea18ebe339039fa08fb39f92cf45afa9f50f0c7`. Full contents were read after the v1 seal. The saved unified diff establishes that the statement changes only its version title and closing scope paragraph; the proof changes only title and exact-version binding. All thirteen mathematical inputs in the v1 manifest were rehashed unchanged. All twenty sealed v1 artifacts were independently rehashed unchanged before this recheck and will be checked again at its seal.

## Resolution of FULL2-WORDING-1

The rejected v1 sentence claimed that all target calls use the independent coefficient discrete-Gaussian error law. This is false for transformed auxiliary inputs, CRT hybrids and finite approximations. The new paragraph correctly states that all D0 calls have the one modulus q0, while the assumed advantage is on the specified exact target law. Actual execution laws are governed by the all-input runtime bound and the explicit statistical transfer.

This amendment agrees with the already-audited proof. For each auxiliary prime q, MR compares both rounded endpoints with the exact fixed-q0 target endpoints. Conditional on the entire public bank and shared binary secret, its error coupling yields the stated whole-batch TV bound, and both public-multiplier biases are charged. The resulting signed-gap difference is at most epsilon_*/4, pointwise in q, so every auxiliary signed gap has the target orientation and magnitude at least 3epsilon_*/4. AM-MAIN-v3 then receives its actual required epsilon0=epsilon_*/2 premise. Nothing requires the off-promise queries to have the target error law. Therefore FULL2-WORDING-1 is RESOLVED for exact v2 and remains REJECTED for exact v1.

The additional b,c sentence is necessary scope clarity, not a new bound. The guard sigma0 >= 8 k0 n(n/2+2)/epsilon_* fixes the admissible sample/advantage window for a prescribed target family. The displayed family chooses fixed integer b,c before sigma0 and q0. It does not give a universal implication for every polynomial sample count and inverse-polynomial advantage exponent at one fixed noise exponent. This was already enforced by the mathematical quantifiers and retained in the v1 review.

## Exact dependency and resource disposition

MR-v1, DD1 extraction-v1, DD2-AM1-v1, selected-functional-v2, AM-MAIN-v3, the DD2 prime-list construction, and the inherited exact A/B-GP/C8/cube interfaces retain the independently established dispositions in the sealed reports. The unchanged-byte verification is recorded in `input-manifest-v2.json`; the inherited accepted-source hashes and compatibility checks remain in `dependency-hash-check-v1.json`, `read-register-v1.json` and the sealed source report. This is not acceptance by an earlier reviewer's banner.

The v2 wording does not change the shared secret, the scaled discrete coefficient width sigma_q, Gaussian completion, caps, evaluator requirements, prime schedule, C8 common parameters, candidate verifier, radius, success probability or any call count. The all-input bound already covers every transformed/hybrid query, wrong orientation and unsuccessful prime. The D0-call bound remains M Q_* ((n+1)Ncal + Qmax Ntest), with exactly k0 fixed-q0 pairs per call. Physical raw auxiliary samples remain K per A_q execution. Width growth changes proposal bit lengths, not trial counts. Polynomial bit complexity is conditional on all the displayed numeric-value and charged evaluation/runtime bounds; it is not an uncharged oracle model.

No new experiment was run for this amendment. The exact finite identity, tie, shared-secret, CP-1 and width-bit-cost evidence remains sealed. Root MR-FV1's logging failure and MR-FV2's evidence limitations are unchanged. Their preservation is part of the current verdict.

## Optional nonvacuity note: analytic check

The optional `coordinator/nonvacuity-and-radius-note-v1.md` has SHA256 `1f0bcde15cfa7dabdb2e522e0749ea714a8c2f1dafd49bbc8c659cf51de7a574`. Its two elementary claims PASS and are not added as dependencies of FIXED-MAIN-v2.

For E distributed as D_(Z,sigma), complete the square in the exact normalized moment generating function:

    E exp(t E) = exp(sigma^2 t^2/(4 pi))
                 * rho_sigma(Z - sigma^2 t/(2 pi))/rho_sigma(Z)
              <= exp(sigma^2 t^2/(4 pi)).

The centered-theta inequality follows directly from Poisson summation: the absolutely convergent Fourier expansion of rho_sigma(Z-u) has nonnegative coefficient magnitudes sigma exp(-pi sigma^2 m^2), so replacing cos(2 pi m u) by 1 gives its maximum at u=0. Thus the normalizer is retained. Chernoff at t=2 pi L/sigma gives P(E>sigma L) <= exp(-pi L^2); symmetry gives P(|E|>sigma L) <= 2 exp(-pi L^2). The strict event causes no boundary problem.

For power-of-two n>=128, L=log2(8n) is an integer at least 10 and B=ceil(sigma0 L) is computable from rational data. Enumerating all binary s and accepting if B1-A1s mod q0 lies in the interval image is a deterministic finite all-input bounded algorithm, using no ideal metadata. The true shared secret is one of the candidates. A union bound on the n first-sample errors gives planted acceptance at least 1-2n exp(-pi L^2)>=3/4, because pi L^2 >= L log 2 and 2^L=8n. This needs no claim about independent CRT error coordinates.

For uniform responses, condition on arbitrary A1. Each fixed s accepts at most (2B+1)^n responses. Union over 2^n candidates and B<=sigma0 L+1, q0>=n sigma0, sigma0>=1 yields

    P_uniform(accept) <= 2^n ((2B+1)/q0)^n
                      <= ((4L+6)/n)^n.

At n=128, (4L+6)/n=46/128<1/2. Doubling n increments L by one and adds only four to the numerator, so the ratio remains below 1/2 for all later powers of two. The comparator acceptance is at most 2^-n, and the signed gap is at least 3/4-2^-n>1/2. Composite q0 is harmless. Ignoring the other k0-1 samples is allowed. The code takes 2^n times polynomial represented-input arithmetic; charging that bound makes the premise class nonempty for the c>=1 numerical family. The reduction instantiated with this code has correspondingly exponential cost. This is not evidence of an efficient distinguisher or of restricted-ideal hardness.

For nonzero x in J^-1, xJ is a nonzero integral ideal. Its positive integer norm is |N(x)| D, hence |N(x)|>=1/D. The product over the n embeddings is at most ||x||_(can,infinity)^n, giving ||x||_(can,infinity)>=D^(-1/n)>=2^(-rho)>1/2. Since J is integral, 1 belongs to J^-1 and has canonical infinity norm 1. Discreteness gives a shortest nonzero length lambda_inf in (1/2,1]. Therefore r/lambda_inf lies in [r,2r), so the inverse-polynomial absolute radius is an inverse-polynomial fraction of the separation. This uses the restricted norm hypothesis and says nothing about finding a shortest vector.

## Regression provenance and limits

The current root registry still contains 164 inherited exact references and 29 local entries, at the same SHA256 `037b02345edde7ee018bc2e73f57f5a890efbd7cbf3cf929dc6ba407d5d01967`. All local entries were reread. `regression-dispositions-v2.json` retains every v1 row, its historical source status and its exact provenance, adds exact-v2 applicability, resolves only FULL2-WORDING-1 for the new version, and adds the two optional-note checks. It does not delete any historical failure or accept unrelated descendants.

This acceptance does not prove hardness of the restricted source family, unrestricted/arbitrary-ideal worst-case hardness, practical security, coherent/quantum composition, or a single target family covering all polynomial sample/advantage exponents. External primary-source and finite-evidence limitations remain exactly those in the v1 report. This is a nonauthor mathematical review, not formal proof verification or coordinator acceptance. BLIND2 was neither read nor contacted.
