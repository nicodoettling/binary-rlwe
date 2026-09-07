# Multiple samples and recovery — M2 synthesis checkpoint

This is a separate conditional result, not repetition of the one-sample source assumption. Full proofs and exact interfaces are in [D03](development/D03.md) and [common-K theorem](development/D03-common-k.md); A2 leakage update is in refinement/R03-interface-audit.md. Fresh criticism is pending.

With one common Y, the full source must publish ((U_i+F_i,U_i K+H_i)) for one independent uniform K in R/J. Conditional on bijective U_i, the ideal tuple has q^d possible values; its distance from independent ideal points is 1-q^(-d(m-1)). This retained-variable fact is not a lower bound on public transcript distance. A separate common-K source assumption is required, including the full H kernel.

For this newly defined source, B1 samples one binary secret and m independent target errors; B2 samples one independent Y and maps every row to (a_i,a_iY+c_i). The conditional advantage bound is two common-K source advantages plus one full joint noise error and one full extraction error. No automatic factor m is needed for extracting a single quotient. Uniformity holds pointwise for every Y. The source contains no binary secret input or hidden data needed by the reduction.

Let M stack the m negacyclic F_i matrices, with p=mn. The complement is B=sigma_m² I_p-tau² M M^T; its off-diagonal block is -tau² M_Fi M_Fj^T. The Poisson smoothing matrix Theta=tau² I_n-tau⁴ M^TM/sigma_m² has input dimension n, while H_seq has p adaptive coordinates in fixed sample-then-coefficient order. All cross blocks are necessary. With sigma_m=2n ell³ sqrt(m), both completion and sequential-normalizer errors are negligible for each fixed polynomial sample bound. The finite implementation cost remains polynomial and is charged against this exact source law. This changes the target width; no growing-m claim at unchanged sigma_1 has been proved. At fixed q the condition sigma_m n^c<=q restricts m. Even H_i marginals are not silently identified with one-sample H_seq.

Separate Y_i=S+G_i observations retain one S. Extracting its repeated quotient into independent secrets fails by diagonal consistency; using one replacement Z leaves K_i=Z-pi(Y_i), whose differences depend on the entire observations. The old independent source challenge does not supply that joint law. Varying ideals introduces overlap consistency and a larger leakage budget, requiring a new complete hybrid.

The exact Gaussian likelihood thresholds sum_i Y_i at m/2. Centered modular observations recover all S bits with failure at most n exp(-pi m/(4tau²))+2nm exp(-pi(q-3)²/(4tau²)). This is an auxiliary-exposure obstruction, not an RLWE attack. Conditional entropy additionally gives eta_ext >=1-[H(S|Y_vec)+1]/[d log2 q]. For A2's output entropy Theta(sqrt(n)/(ln n)³), m=C tau² ln n with C>2/pi forces eta_ext=1-o(1). The earlier tau² log log n threshold belongs only to A1's larger quotient.

For a solver seeing exactly m target samples, let epsilon_rec be its exact planted-secret success, delta_T=Pr[E outside T], v_T=|T|/q^n. Self-verification on those m samples gives

    Adv_dec,m >= epsilon_rec-m delta_T-2^n v_T^m.

The uniform bound unions over all binary candidates; no independence of the adaptive answer from its inputs is assumed. With T the coefficient box of radius ceil(sigma log n), the baseline makes both losses negligible. Hence a separate m-sample decision theorem would rule out nonnegligible m-sample exact recovery with **zero held-out samples**. One-sample decision supports only the corresponding one-sample consequence.

Alternatively, fixing the candidate before h fresh verification samples gives Adv_dec,m+h >= epsilon_rec*(1-delta_T)^h-v_T^h. This consumes m+h independent samples. A verified preimage need not be the original planted secret. Neither formula imports unrestricted sample-oracle amplification, mild-search success, or rotations as fresh samples.

Order-LWE sample expansion requires extra ordinary-RLWE hypotheses, width changes and swallowing ratios incompatible with a silent import to this baseline. DSPR subset-sum expansion has its own conditional error and sample-oracle interfaces. These were compared in D03; neither establishes the missing exact common-K pseudorandomness.
