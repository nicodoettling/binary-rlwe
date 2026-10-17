# Frozen candidate EX-v1: noisy public expansion from two seeds

Status: PROVISIONAL. Frozen before detailed proof and finite tests. This is a candidate for falsification, not an accepted result. Base2 computational hardness remains an assumption.

Let n>=2 be a power of two and q>=n^2 an odd prime 1 modulo 2n. R=F_q[X]/(X^n+1) has its coefficient representation. Let ell=ceil(log2 n), L=ceil(n sqrt(q)), b=(2n+1)L ell^2. D_t(z) is proportional to exp(-pi z^2/t^2) on Z.

Given a single pair (A1,A2), for each j=1,...,m independently choose Rj1,Rj2 with all coefficients uniform in {0,...,L-1}, and Wj with iid coefficient D_L. Output Cj=A1 Rj1+A2 Rj2+Wj modulo q. All local coins are fresh and independent of the pair; the pair and coins are not given to the target solver. This is an executable public randomized map, not a source oracle.

Define delta_exp=min(1,(m/2)*sqrt(16^n q^n exp(-2 pi n^2)+(2/n)^n)). Claim EX-REG: for independent uniform A1,A2, TV((A1,A2,C1,...,Cm),(A1,A2,Z1,...,Zm))<=delta_exp, where Zj are iid uniform R and independent of A1,A2. This is a full joint law including the seed, not a marginal claim. A finite parameter value with a vacuous bound is permitted.

Now let (A1,A2) follow exact SC-v1 Base2(n,q,d), with one uniform d-subset T, Ui uniform I_T including zeros, independent iid coefficient D_ell masks Fi. Set sigma=2 sqrt(m)n b ell. Target has m iid uniform multipliers aj, one uniform coefficient-binary S, and fully independent iid coefficient D_sigma errors Ej, independent jointly of all multipliers and S. Exact success is recovery of actual sampled S.

The public source test samples the expansion above, its own S and target errors, invokes target solver Q once on ((Cj,Cj*S+Ej))_j, and accepts exactly when Q outputs S. It receives only the original pair and public parameters.

Put kappa(t)=2 sum_{j>=1} exp(-pi t j^2), Delta=(1+kappa(3ell^2/4))^n-1, eta=min(1,Delta/(1-Delta)) when Delta<1 and eta=1 otherwise; delta_mask=min(1,(m+2)n exp(-pi ell^2)/(pi ell)). Claim EX-REC:

 epsilon_m <= Adv_Base2(B_Q)+q^d((1+D_ell(0))/2)^n+eta+delta_mask+delta_exp.

No claim that expanded planted Cj form Base_m is made; their ideal parts and masks may be correlated. No additional source premise is required beyond the single original Base2 pair at the specified n,q,d.

Candidate effective family: fix integer h>=0 before adversaries, choose 1<=m(n)<=n^h polynomial-time computable (m=3 covered eventually when h>=1); set K=h+10 and q the least prime 1 modulo 2n^K. Published least-prime bound exponent 5.18 implies 2n^K+1<=q<=n^(6K) eventually. Take separately d=floor(sqrt(n)/ell^4) or d=floor(n/(24K ell)). Under the exact Base2 hypothesis at this NEW q,d family, claim negligible uniform-PPT actual-secret recovery with q/sigma>=n eventually, and all overhead polynomial in n for fixed h. Each h fixes its own q/noise/source family; this does not establish arbitrary sample exponents at one fixed q family. It does not transfer hardness from September q least 1 mod 2n^3.

Required outstanding gates: direct regularity proof; exact mask bound and arbitrary-m stacked completion; primary prime check and finite sampling; finite rare/zero/posterior/witness controls; nonauthor proof/source/complexity and fresh blind review; historical regressions; exact artifact reconciliation.
