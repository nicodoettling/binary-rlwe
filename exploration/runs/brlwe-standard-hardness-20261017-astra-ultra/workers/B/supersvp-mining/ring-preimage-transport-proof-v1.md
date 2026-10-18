# Proof of B-SUP-PT-T v1

Status: PROVISIONAL, awaiting independent probability/source/complexity review. All Gaussian widths use density exp(-pi||x||²/u²) on the coefficient lattice. Ring multiplication uses the fixed negacyclic coefficient representation.

## 1. Uniform Gaussian coset masses from a ring-specific two-row calculation

Let H be uniform in Rq^(r by m), r=1 or2, and let x in R^m have iid coefficient D_u. Its image distribution P_H on Rq^r satisfies

  E_H chi²(P_H||U)=sum_(empty!=S subset[n]) (q^r-1)^|S| c_S^m
                 <=K_r(u),

where c_S is the collision probability of the projection of one ring entry of x onto root set S. To see the identity, expand chi-square in additive characters. At each root an r-tuple of characters is either all zero or nonzero, giving respectively1 or q^r-1 choices. Averaging the r independent uniform key entries at that root forces equality of the two source evaluations. Across the m independent source ring entries the collision probability is raised to the m-th power. The coefficient-pivot argument gives c_S<=mu_u^|S|. No independence of CRT evaluations inside one x entry is asserted.

For any finite distribution P on a group of size Q,

  max_y |Q P(y)-1|²<=Q chi²(P||U).

Markov therefore gives, except probability beta_r(u,epsilon) over H, the SIMULTANEOUS bound

  q^(-rn)(1-epsilon)<=P_H(y)<=q^(-rn)(1+epsilon)

for EVERY y. For r1 this proves all Gaussian A-coset masses are flat; for r2 it proves the same for the augmented random two-ring-row matrix [A;u]. The q^(rn) factor is paid explicitly in beta and the choice of m. An average leftover-hash bound alone would not imply these pointwise statements.

## 2. Input hint cutoff and canonical preimage sampling

Suppose A has the r1 flatness property at sigma_T. For a fully independent coefficient Gaussian vector z=(v1,...,vL,r) of width sigma_T, condition on r. The block constraints Av_i+Wi r=target_i have joint probability at least q^(-nL)(1-epsilon)^L, since the vi blocks are independent. Averaging over r preserves that lower bound. Therefore each conditional input T column has any coefficient-tail event bounded by its unconditioned Gaussian probability divided by q^(-nL)(1-epsilon)^L. A union bound over Ddim Lg coordinates, with scalar tail2exp(-pi(B_T/sigma_T)²), gives alpha_T. Bad A costs beta_1(sigma_T,epsilon).

On the cutoff event T is an integer gadget trapdoor of maximum entry B_T for the nL by Ddim coefficient-expanded matrix. The checked general integer preimage SAMPLER, at sigma_V>=Ddim B_T log(nL), replaces its t output ring columns by independent canonical Gaussian preimages of F with total distance delta_pre=t2^-nL. This sampling invocation is valid for the supplied structured matrix and trapdoor; it does not assume that the coefficient-expanded matrix is uniform. All finite numerical errors are additional. The canonical law depends only on A,W,F, not on the original T; this permits T to be discarded. Its integer representative is retained until all norm/lifting operations finish.

## 3. Exact shared-R marginal and its normalizer

For one canonical preimage column, partition T'=(v1,...,vL,r). Its R marginal is the unconditioned coefficient Gaussian D_(R^h,sigma_V) reweighted by

  Z(r)=product_(i=1)^L P_A(F_i-Wi r),

and divided by the ACTUAL expectation E_r Z(r). Conditional on r, the vi are independent prescribed A-coset Gaussians. On A's r1 flatness event at sigma_V, Z(r) lies between q^(-nL)(1-epsilon)^L and q^(-nL)(1+epsilon)^L for every r. Thus replacing r by an independent unconditioned Gaussian changes the full (r,v1,...,vL) law by at most ((1+epsilon)/(1-epsilon))^L-1, using the SAME conditional vi kernels. Hybrid over t independent columns gives delta_R. This preserves all shared-R correlations between row blocks and every F(W) dependence.

After this replacement, R is independent of A,W and has exactly the stated iid coefficient Gaussian law. Its negative Rout has the same law. The identity A V=F-WR=F+W Rout holds in every branch. On A's same flatness event, each conditional V ring column has Gaussian coordinate tail bounded by2q^n(1-epsilon)^-1 exp(-pi a_V²). Union over nmLt coordinates gives alpha_V. The coefficient expansion satisfies

  ||V_c||<=||V_c||F=sqrt(n)||V||coefficient,F
                        <=n sigma_V a_V sqrt(mLt)=B_V.

Both cutoffs are executed, not assumed. Their probabilities and the A failure probabilities are charged. A finite sampler's noncanonical exceptions are coupled and separately charged.

## 4. Rectangular Gaussian noise completion, with the actual normalization

Conditional on every retained or discarded public variable and V, let e~D_(Z^(nm),tau) and independently f~D_(Z^(nLt),F),

  F=chi²I-tau² V_c^T V_c.

The width assumption gives F positive definite and F>=3tau²I. Completing the square in the sum over the ORIGINAL e variables shows that eV+f has desired Gaussian mass exp(-pi||y||²/chi²), reweighted by

  rho_P(Z^(nm)-m_y), P=(tau^-2I+V_c F^-1 V_c^T)^-1.

The reweighting denominator is its ACTUAL expectation under D_(Z^(nLt),chi). Since F>=tau² V_c^T V_c in the singular-value sense and chi>=2tau||V_c||, P>=(tau²/2)I. The assumption tau>=2eta_epsilonN(Z^(nm)) makes its shifted theta factor uniformly1±epsilonN times its constant term. Consequently the output error is within epsilonN/(1-epsilonN) of D_chi, jointly with every public variable and V. This works for rectangular or rank-deficient V; no false unimodularity is used. The finite correlated Gaussian sampler adds delta_F.

In the planted case b=sA+e, so bV+f=s(F+W Rout)+(eV+f). Every comparison above retains s, which is independent of all public sampling. Discarding A,T,V gives the specified planted target. Adding the bad-event, sampling, reweighting and noise losses yields E_P.

## 5. Comparator, retaining the shared public tuple

If b is uniform independent of the public input, introduce an independent e0~D_tau and define u=b-e0 moduloq. Then u is uniform Rq^m and independent of A,W,T,e0 and all preimage coins. This is an analysis coupling; u and e0 need not be supplied by an oracle. The same completion compares bV+f to uV+eout with independent prescribed eout.

The augmented matrix [A;u] is uniform in Rq^(2 by m). On its Section1 flatness event, for every fixed A-coset syndrome y, the extra image z=u v of a conditional Gaussian v has mass

  Pr[u v=z | Av=y]=P_[A;u](y,z)/P_A(y).

The numerator and denominator bounds place this between q^-n(1-epsilon)/(1+epsilon) and q^-n(1+epsilon)/(1-epsilon). Its TV from uniform is at most epsilon/(1-epsilon). Conditional on A,u,W,Rout, all Lt V columns are independent with their actual respective syndromes, so a column hybrid gives delta_img. Thus uV is jointly uniform retaining W,Rout after A,u,V are discarded. Adding independent eout preserves that uniform law. The augmented flatness failure contributes beta_2(sigma_V,epsilon), giving E_Q. No fresh product law is inferred after key selection without its conditional proof.

## 6. Runtime and composition scope

F is computed from W before the new R is sampled; setting F=-WR to enforce a later condition would violate the theorem. SamplePre is invoked only with the available valid trapdoor T and its cutoff. Ring multiplication, coefficient expansion and PSD covariance arithmetic have polynomial complexity in all dimensions and rational input lengths. Gaussian/uniform samplers must be bounded with total delta_impl, or the conclusion is only expected polynomial time. Approximate covariance square roots and continuous auxiliaries are governed by the finite elliptical sampler-v2 accuracy budget; integer output remains integer.

The input m can be chosen O(n logq+lambda+log(Lt)), with a sufficiently large fixed constant, so all beta terms are negligible even using only mu<=.7. The conditional tail penalties q^(nL) and q^n increase the cutoff radii by polynomial square-root factors, not by q itself. All remaining widths may therefore be chosen polynomial in the original parameters. This supplies the needed search direction for a potential larger chain, but that chain's ideal family, source norm, final noise and binary law must still be checked. The construction does not imply arbitrary coefficient matrices are ring matrices and imports no SuperSVP hardness premise.
