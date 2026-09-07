# Baseline source and computational obligation

This document freezes the intake baseline. A candidate change must receive a new version and reopen every dependent claim. The consolidated ledger controls the review status of imported statements; this definition does not certify them.

Let n grow over powers of two and R_q=F_q[X]/(X^n+1), in the coefficient basis. Let ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2, gamma=tau=ell, and sigma=2n ell^3. For fixed c>0 and K, choose an odd split prime with sigma*n^c <= q <= n^K. All asymptotic claims require sufficiently large n and an explicit nonempty parameter choice. The prior numerical choice c=1,K=16 has a separate source-checked prime-existence argument.

Choose T uniformly among the d-element subsets of the CRT roots. Let I be the elements supported on T, J=Ann(I), and Q=R_q/J. Sample U with independent uniform nonzero coordinates on T and zero coordinates off T. Multiplication by U identifies Q with I. Sample V uniformly in I, independently of U and the noise conditional T.

The integer coefficient vector F is independent of (T,U,V) and has independent D_ell coefficients conditioned on [-b,b], where D_s(z) is proportional to exp(-pi*z^2/s^2). Let M_F be its integer negacyclic multiplication matrix. Define B=sigma^2 I_n - tau^2 M_F M_F^T. Conditional on F, sample H with fresh coins independent of (T,U,V,S,G), from the exact canonical coefficient-order sequential discrete-Gaussian law H_seq(F) defined in the prior [A2 dossier](../runs/brlwe-joint-ideal-20260906-astra-ultra/candidates/A.md) and [completion proof](../runs/brlwe-joint-ideal-20260906-astra-ultra/foundations/F02-completion.md). Preserve its fixed LDL convention and adaptive one-dimensional centers. H_seq is not exactly the multivariate mass D_B; finite approximations require their own distance accounting.

The source publishes only (A,C)=(U+F,V+H) modulo q. It has no binary-secret input. P0-A2 asserts that this exact pair is computationally indistinguishable from two independent uniform ring elements. Active-unit conditioning and the joint F/H law are part of the assumption. The new run seeks support for this premise, a refutation, or a precisely scoped obstruction; it must not cite the premise itself as independent evidence.

For the target, S is coefficientwise fair binary, E is wrapped iid D_sigma, and a is uniform in R_q independently of S,E. One target sample is (a,aS+E). The auxiliary channel uses independent G with iid D_tau coefficients and Y=S+G modulo q. The source variables are independent of S,G. Required statistical comparisons in the existing sufficient bridge are:

    TV((J,U,F,FG+H), (J,U,F,E)) <= eta_N,
    TV((J,U,F,H,Y,pi_J(S)), (J,U,F,H,Y,Z)) <= eta_X,

where Z is uniform in Q and conditionally independent of (U,F,H,Y) given J. On the first right-hand side E is independent of the retained (J,U,F); FG+H is reduced modulo q for comparison with wrapped E. H is integrated out in the first comparison and retained in the second. The public source tests are B1(a,c)=D(a,aS0+E0) and B2(a,c)=D(a,aY0+c), with freshly sampled public-law S0,E0,Y0. Consequently the conditional advantage bound is the sum of the two source advantages plus eta_N+eta_X, with additional implementation terms as specified in the [bridge](../runs/brlwe-joint-ideal-20260906-astra-ultra/bridge.md).

A new public-only noise comparison must supply a revised full hybrid, not just assert that a stronger latent condition is unnecessary. Any replacement assumption must define its source experiment without using the desired binary-RLWE hardness as an input. State the direction and parameters of every reduction.

For m samples sharing Y, the source is ((U_i+F_i,U_iK+H_i)) with one common K uniform in Q and independent of the entire source tuple Gamma_m=(J,(U_i,F_i,H_i)_i) conditional on J. Its ideal products cannot be replaced by fresh independent V_i. The existing sufficient completion changes the width to sigma_m=sqrt(m)*sigma and uses the full stacked covariance complement and joint H sampler. This changes the source assumption. Fix m before claiming a reduction and retain sigma_m*n^c<=q for that m.

Required inherited controls include active-unit rank loss; marginal-versus-joint nonuniformity; same-Y posterior replica coupling; the unguarded NC1 negative-bound counterexample; independent-shear retained-noise mismatch; common-K support constraints; leakage from many separate Y_i; and ATT-v3's strict rounding radius and root-setup input. Import the complete recorded examples into the new regression registry.

Primary starting points are the user's two PDFs in literature/, [Order-LWE/HLBDD](https://eprint.iacr.org/2018/494), [DSPR entropic RLWE](https://eprint.iacr.org/2020/1185), [ideal decoding and partial Vandermonde work](https://eprint.iacr.org/2022/709), and the previous run's exact source comparison and critic reports. Verify newly load-bearing quotations and hypotheses against the primary source. This list is not evidence that any source already implies P0-A2.
