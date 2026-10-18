# B-SUP-PT-T v1: canonical ring hints to decomposed challenges

Status: PROVISIONAL author theorem. This is a new ring proof of the mechanism of2026/2443 Lemma8.8, with larger dimensions and explicit losses; it is not an invocation of its general-matrix hardness theorem. Proof: ring-preimage-transport-proof-v1.md. The two-row Gaussian image lemma is new and still awaits an exact finite control and independent review.

Let R=Z[X]/(X^n+1), n a power of two, q>=5 split prime. Let m,h,L,t,g be positive integers, g>=ceil(log2q), and Lm+h>=3Lceil(log2q). Let G be the padded integer-constant binary gadget row of lengthg. Put Ddim=n(Lm+h). The input canonical ring experiment publishes

  A uniform Rq^(1 by m), W uniform Rq^(L by h), independently;
  T: Lg independent integer Gaussian ring columns of width sigma_T>=2,
     conditioned on [I_L tensor A | W]T=I_L tensor G;
  b=sA+e, or b uniform Rq^m independently,

where s has any fixed specified law Secret independent of public variables and e has iid coefficient D_tau. Unreachable preimages use a common failure convention. Define a deterministic efficient ring matrix F(W) in Rq^(L by t), independent of all future preimage coins. No arbitrary challenge-dependent error hints are supplied.

The desired output publishes (W,Rout,c), with Rout in R^(h by t) iid coefficient D_sigma_V, W uniform and independent, and either

  c_i=s(Wi Rout+Fi(W))+eout_i, i<=L,
  or all Lt ring entries of c independently uniform.

The output errors have iid coefficient D_chi. The same Secret is retained. Standard degree-L decomposed challenges are the special case t=Lg, F=[delta_ijG]_(i,j), with Rout partitioned into L blocks.

For width u>=2 set mu_u=min(1,1/u+1/q), and define for r=1,2

  K_r(u)=(1+(q^r-1)mu_u^m)^n-1,
  beta_r(u,epsilon)=min(1,q^(rn) K_r(u)/epsilon²).

Fix epsilon in(0,1/2), cutoffs B_T>=sigma_T and a_V>=1, and widths satisfying

  sigma_V>=Ddim B_T log(nL),
  tau>=2 eta_epsilonN(Z^(nm)),
  B_V=n sigma_V a_V sqrt(mLt), chi>=2tau max(1,B_V).

Define

  alpha_T=min(1,2 Ddim Lg q^(nL)(1-epsilon)^(-L)
                        exp(-pi(B_T/sigma_T)²)),
  alpha_V=min(1,2nmLt q^n(1-epsilon)^-1 exp(-pi a_V²)),
  delta_pre=t 2^(-nL),
  delta_R=min(1,t[((1+epsilon)/(1-epsilon))^L-1]),
  delta_img=min(1,Lt epsilon/(1-epsilon)),
  delta_noise=epsilonN/(1-epsilonN)+delta_F.

An explicit public simulator produces the target planted/comparator laws within respective distances

  E_P=beta_1(sigma_T,epsilon)+beta_1(sigma_V,epsilon)
       +alpha_T+alpha_V+delta_pre+delta_R+delta_noise+delta_impl,
  E_Q=E_P+beta_2(sigma_V,epsilon)+delta_img.

Bounds may be capped at1. Delta_impl covers all finite implementation errors other than the separately counted correlated Gaussian sampler error delta_F. A target distinguisher transfers advantage delta-E_P-E_Q; a target secret-recovery solver transfers success delta-E_P, recovering the SAME secret. The simulator needs only the m input responses already supplied, one target call, and no additional secret-dependent samples. All original A,T and sampled V are discarded from the final target view.

The simulator aborts on ||T||max>B_T, samples a preimage T' of F using T at width sigma_V, writes T'=(V1,...,VL,R) vertically, and sets Rout=-R. Thus A[ V1|...|VL ]= [Wi Rout+Fi]_i. On ||V||coefficient,max<=sigma_V a_V, it outputs c=bV+f, with covariance parameter chi²I-tau² V_c^T V_c for f. The next proof gives both endpoints, actual marginal normalizers and all selection/tail charges.

All requirements admit polynomial parameters. For example choose epsilon=2^-lambda/(100Lt), and

  m>=8[(2n+2)ceil(log2q)+3lambda+3ceil(log2(100Lt))
       +ceil(log2(2n))+1].

For any sigma_T,sigma_V>=2 the two beta terms are negligible using mu<=.7. Choose B_T/sigma_T and a_V as polynomial square-root upper bounds making the displayed alpha expressions <=2^-lambda, then choose sigma_V and chi by their displayed inequalities. This causes only polynomial growth in n,L,t,m,h,lambda,logq and the original widths. Finite samplers can be bounded with delta_impl explicitly charged. No restriction q=poly in VALUE is needed here; that separate restriction enters ring-decision-search-theorem-v1.md.

This preserves a binary input law if one was already supplied, but establishes no uniform-to-binary conversion. It is a search and decision transport edge, not a complete worst-case theorem for the original fractional source or SC-v1.
