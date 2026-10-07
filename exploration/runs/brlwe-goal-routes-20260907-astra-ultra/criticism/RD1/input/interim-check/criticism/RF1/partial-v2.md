# RF1 partial review, 2026-09-07 22:08 UTC

Timestamp correction: partial-v1.md was saved at approximately 22:03 UTC, as confirmed by the immediately following clock result 22:03:14 UTC; its 22:07 header was an editorial mistake. This version preserves that original rather than silently editing it.

The new exact full-product-kernel search passed 11,664 models over F3, including unequal source probabilities and all 36 source-dependent pairs of denominator-two H kernels. Appending the independent secret preserved TV exactly. The witness/transcript comparison contracted TV, and the recovery inequality passed; 648 tested right sides were nontrivial (<1), and 72 models attained equality.

The new leakage search passed all 64,152 combinations of 792 denominator-five joint laws on four secrets/two observations and 81 maps into three labels. It includes empty leakage fibers and zero-probability observation branches. A separate rare-branch hidden-map example has base guessing 103/400, leaked guessing 10199/20000 and expected-cardinality bound 10403/20000. Source-dependent map selection is independent of (S,Y), exactly as required.

New genuinely rectangular completion: M=[[1,1],[1,0],[0,1]], tau^2=4, sigma^2=16. Exact rational matrix identities and 3,125 completed-square substitutions pass. B has eigenvalues 4,12,16 and Theta eigenvalues 1,3. Qualified binary64 sums give delta=0.011204695537690093 and TV approximately 0.002104312365688408, below delta/(1-delta)=0.011331663375750976. Direct independent-summand masses agree with normalized Poisson masses at four specified points. Analytic omitted-mass bounds are recorded; floating arithmetic is expressly not interval-certified.

Historical exact controls independently reproduced: pairwise-but-not-joint F3 distance 2/3; correlated-source-secret target distance 2/9; shared-G/common-K joint distance 2/3; CP-1 normalizer 10/11 and selected event 21/2000>1/100; negative-denominator delta lower bound 82/63>1; signed deconvolution negative entries; latent TV 1/2 erased to public TV 0. H_seq parity normalizers differ by approximately 0.0440089584 in its archived matrix example. These invalidate the old shortcuts, while the current proof uses none of them.

No flaw has been found in the frozen finite candidate. Final work remains: full regression disposition table, source-budget and zero-ideal positive controls, exact finite implementation constants, asymptotic bit complexity, scope review and artifact integrity freeze.
