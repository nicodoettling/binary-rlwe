# RF1 partial review, 2026-09-07 22:13 UTC

All planned bounded experiments have finished successfully, sequentially in slot 2 under individual 120-second caps. The original author control code was copied into RF1 and rerun without altering its bytes or author outputs. New RF1 source-interface tests checked all 8 and 128 deterministic decoders in zero-ideal one/two-sample models. A varying hidden dual-number ideal reproduces public TV 9/32 and has exact planted guessing 17/32 below its expected-cardinality bound 3/4. All 384 exact dyadic rounding controls pass.

The finite implementation accounting is correct: one source approximation changes one acceptance endpoint, local sampler approximation changes two endpoints, and target approximation changes exact-witness success, yielding xi_source+2xi_alg+xi_target. The supplementary normalized-weight and final dyadic-table estimates have no omitted normalizer. The cutoff, precision and exact-bit draw counts are polynomial for fixed m and polynomial q.

Prime and entropy substitutions check out: 3*5.18=15.54<16; q/sigma_m>=n eventually; d<=n/(64ell) charges at most n/4 bits when q<=n^16; ell>=6 makes the guessing term at most 2^(-n/2). The explicitly growing d formulas are efficiently computable. An arbitrary uniformly computable d need not have polynomial setup, but the reduction does not compute d.

The d=1 source premise is independently refuted by enumerating the nq singleton-ideal points and checking a coefficient box; the finite count and asymptotic bound are frozen in source-d1-limitation-v1.md. This is expressly not a rejection of F or A, which make a separate conditional source assumption for each d. No efficient-setup or hardness plausibility certification for arbitrary d is warranted.

The report is being assembled with claim-addressed PASS/REJECT/OPEN scope distinctions and a complete historical regression disposition table. No valid counterexample to the frozen theorem/proof has been found. Final artifact-hash and input-immutability checks remain.
