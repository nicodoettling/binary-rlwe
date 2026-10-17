# Noisy public expansion from two seeds: finite and asymptotic statements

Let n>=2 be a power of two and q>=n^2 an odd prime 1 modulo 2n. R=F_q[X]/(X^n+1) has its coefficient representation. Let ell=ceil(log2 n), L=ceil(n sqrt(q)), b=(2n+1)L ell^2. D_t(z) is proportional to exp(-pi z^2/t^2) on Z.

Given a single pair (A1,A2), for each j=1,...,m independently choose Rj1,Rj2 with all coefficients uniform in {0,...,L-1}, and Wj with iid coefficient D_L. Output Cj=A1 Rj1+A2 Rj2+Wj modulo q. All local coins are fresh and independent of the pair; the pair and coins are not given to the target solver. This is an executable public randomized map, not a source oracle.

Define delta_exp=min(1,(m/2)*sqrt(16^n q^n exp(-2 pi n^2)+(2/n)^n)). Claim EX-REG: for independent uniform A1,A2, TV((A1,A2,C1,...,Cm),(A1,A2,Z1,...,Zm))<=delta_exp, where Zj are iid uniform R and independent of A1,A2. This is a full joint law including the seed, not a marginal claim. A finite parameter value with a vacuous bound is permitted.

Define Base2(n,q,d) for d in {0,...,n}: choose one uniform d-subset T of the n CRT roots, and conditional on T choose U1,U2 independently uniform in I_T, the ideal supported on T, including zeros. All 2n coefficients of F1,F2 are iid integer D_ell, jointly independent of T,U1,U2. Publish only (A1,A2)=(U1+F1,U2+F2) modulo q. Its comparator is exactly independent uniform R elements. A test gets this sole pair and public parameters, with no source oracle or witnesses. Adv_Base2(B) is the absolute difference of its bit acceptance probabilities. Now let the input pair follow this Base2 law. Set sigma=2 sqrt(m)n b ell. Target has m iid uniform multipliers aj, one uniform coefficient-binary S, and fully independent iid coefficient D_sigma errors Ej, independent jointly of all multipliers and S. Exact success is recovery of actual sampled S.

The public source test samples the expansion above, its own S and target errors, invokes target solver Q once on ((Cj,Cj*S+Ej))_j, and accepts exactly when Q outputs S. It receives only the original pair and public parameters.

Put kappa(t)=2 sum_{j>=1} exp(-pi t j^2), Delta=(1+kappa(3ell^2/4))^n-1, eta=min(1,Delta/(1-Delta)) when Delta<1 and eta=1 otherwise; delta_mask=min(1,(m+2)n exp(-pi ell^2)/(pi ell)). Claim EX-REC:

 epsilon_m <= Adv_Base2(B_Q)+q^d((1+D_ell(0))/2)^n+eta+delta_mask+delta_exp.

No claim that expanded planted Cj form Base_m is made; their ideal parts and masks may be correlated. No additional source premise is required beyond the single original Base2 pair at the specified n,q,d.

Effective family: fix integer h>=0 before adversaries, choose 1<=m(n)<=n^h polynomial-time computable (m=3 covered eventually when h>=1); set K=h+10 and q the least prime 1 modulo 2n^K. Published least-prime bound exponent 5.18 implies 2n^K+1<=q<=n^(6K) eventually. Take separately d=floor(sqrt(n)/ell^4) or d=floor(n/(24K ell)). Under the exact Base2 hypothesis at this NEW q,d family, claim negligible uniform-PPT actual-secret recovery with q/sigma>=n eventually, and all overhead polynomial in n for fixed h. Each h fixes its own q/noise/source family; this does not establish arbitrary sample exponents at one fixed q family. It does not transfer hardness from September q least 1 mod 2n^3.

For a finite implementation, add xi_source+2xi_alg+xi_target to EX-REC, where xi_source is the full planted pair TV error, xi_alg is the TV error of the entire challenge-independent local expansion/secret/error sampler, and xi_target is the complete target witness/transcript TV error. The uniform source comparator remains exact. All local samplers can achieve negligible xi_alg with bounded polynomial runtime for the effective family. The wrapper uses one Q call, 2mn interval draws, mn D_L draws, mn D_sigma draws, n secret bits, 3m ring multiplications and O(m) ring additions.

The claims are conditional on Base2 pseudorandomness and the stated published least-prime theorem. No standard-RLWE source hardness, target decision hardness, quantum/nonuniform conclusion or practical security estimate is asserted. Small finite n where the displayed bounds are vacuous are included.
