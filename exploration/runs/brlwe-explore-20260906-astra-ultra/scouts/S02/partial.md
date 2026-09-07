# S02 partial development

Started 2026-09-06 09:29:20 UTC. Initial input: context/formal-only.md only. No baseline packet or other scout notes read. No experiments requested or run.

## Representation before release

**Fully written small calculation (in progress).** Let P_s be the ring experiment on (A_i,B_i): A_i uniform in R_q and B_i=A_i s+E_i. An unconditional channel from the source mixture sum_s mu(s)P_s to the binary mixture sum_t nu(t)P_t exists trivially: ignore input and generate a fresh binary secret and transcript. It transfers no search hardness. The nontrivial object must retain a coupling between the original hidden secret and the target hidden secret, together with an efficient decoder after target recovery.

Independently defined candidate source: U uniform in R_q, m independent uniform ring multipliers, and the same coefficient discrete Gaussian errors. This source is not assumed hard throughout the reference parameter range.

Natural affine channel: for known unit t in R_q and known r in R_q, V=tU+r; set A_i'=A_i t^{-1}, B_i'=B_i+A_i'r. This preserves rank one, uniform public multipliers, and the complete coefficient error law. For fixed t,r independent of source observations, U uniform implies V uniform. It therefore cannot produce the coefficient-binary target prior. Rejection on V being binary has probability (2/q)^n and depends on the unknown source secret. Choosing t,r adaptively from the transcript needs a new proof of the complete joint law.

**Unresolved.** Identify an exact parameter-indexed deficiency formulation and determine whether a posterior-resampling construction is efficiently implementable without already solving a posterior search problem. Distinguish such existence from mutual information or guessing comparisons.

## Additional pre-release calculations

**Fully written small calculation.** On a common parameter set, the deficiency object is delta(P,Q)=inf_K sup_u TV(KP_u,Q_u), with K independent of the unknown u. Prior-weighted joint closeness is a weaker, sufficient average-case variant, but the target must still encode u through a specified coupling. A bare comparison of mixtures is vacuous because K can discard the input and sample the target mixture.

A useful explicit coupling: draw V uniformly from C={0,1}^n and R uniformly from R_q independently, then U=V-R. U is uniform in R_q. Conditional on U=u, however, R must be distributed as V-u, a translated binary cube. Desired target-side state is (R,Y), where Y is a fresh reference transcript with binary secret V. Decoding U=V-R is efficient. Implementing this conditional channel would be a meaningful source-to-target reduction; simply drawing R uniform given the original source U instead makes V=U+R uniform, not binary. This is a concrete place where matching unconditional marginal R and source prior conceals the wrong joint coupling.

**Fully written small calculation.** For x=(a,b), use L_s(x)=product_{i,j} W_{sigma,q}((b_i-a_i s)_j), with all factors positive. Let p_mu(x)=sum_s mu(s)L_s(x), suppressing the common multiplier probability. A transcript-only acceptance rule alpha(x) keeps conditional U|x unchanged. Exact accepted joint density nu(u)L_u(x) would require alpha(x)mu(u)=c nu(u) for every u,x. Positivity forbids changing full-support mu to binary-supported nu this way. In contrast alpha(x) proportional to p_nu(x)/p_mu(x) fixes only the transcript marginal. Sampling V from the nu-posterior afterwards gives a correct target joint law, but need not recover original U.

**Fully written small calculation; cheap diagnostic, no experiment.** Let theta be uniform on {0,1,2}; X=1_{theta=0}, Y=1_{theta=1}. Both have mutual information h(1/3) and optimal full-theta guessing probability 2/3. Nevertheless, no garbling of X produces Y: X has the same conditional law at theta=1 and 2, whereas Y has opposite deterministic values. In fact delta(X,Y)=1/2, because K(1|X=0)=p forces errors 1-p and p, and choosing p=1/2 attains the bound. Thus equal Shannon information and equal optimal guessing do not supply a parameterwise simulator.

## Exact posterior transport (second mechanism)

**Fully written small calculation.** Given a source transcript X=(A,B), sample Uhat from the exact source posterior

p(u|A,B) = L_u(A,B) / sum_{w in R_q} L_w(A,B),

then sample an independent V uniformly from C. Put R=V-Uhat and Y=(A,B+A R). Since (Uhat,A,B) has exactly the same joint marginal as (U,A,B), the residual Ehat=B-A Uhat has the independent wrapped coefficient Gaussian law and is independent of (Uhat,A). Thus Y=(A,A V+Ehat) is exactly the target experiment jointly with V. No parameter, rank, sample-count, basis or noise change occurs; the source secret prior alone changes from uniform R_q to uniform C. Ring rotations are never used as independent data.

The simulator itself knows Uhat, so using the binary solver to obtain V does not magically create source information. Conditional on X, true U and Uhat are independent posterior samples; source recovery success is E_X sum_u p(u|X)^2. This lies between (p_guess(U|X))^2 and p_guess(U|X): pointwise sum p_u^2 >= (max p_u)^2 and <= max p_u, followed by Jensen on the lower bound. Therefore in statistically identifiable regimes, an efficient exact posterior sampler already solves source search well. The missing efficient posterior sampler is a serious, explicit computational obstruction. Exact simulation of (V,Y) does not assert a correct joint coupling with the original U.

Falsifiable question: is there a polynomial-time kernel which samples the required shift R and target transcript with negligible joint error while retaining an efficiently decodable coupling to original U, without implementing source posterior search? Neither a Shannon entropy inequality nor binary/full-secret transcript marginal closeness proves this.

## Precise sufficient channel obligation

For each n, independently define source P_u as in the formal model but with u ranging over all R_q; its average-case prior is mu=Unif(R_q). Define the ideal comparison family Q_u by choosing V uniformly from C, setting R=V-u, and independently generating a fresh target transcript Y conditional on V. The reduction observes (R,Y), passes Y alone to a binary solver, then outputs V-R. The ideal source prior is uniform and the ideal Y law is precisely the reference target law.

The sufficient average-case obligation is a **single uniform polynomial-time simulator family** K such that

TV( Law[U, K(X)] , Law[U,R,Y] ) <= epsilon(n), U~mu, X~P_U,

for negligible epsilon, with K outputting (R,Y). Parameterwise sup_u TV(KP_u,Q_u) <= epsilon is stronger and gives a standard deficiency bound. The average joint bound transfers a binary solver's success probability with at most epsilon loss by comparing the event decoded secret equals U. Merely comparing transcript marginals is inadequate. Replacing joint TV with computational indistinguishability requires an appropriate joint experiment (or a separate efficient verification argument), not just indistinguishable public transcripts.

There is no claim here that the source is hard at every reference parameter, and no inference from small unrestricted deficiency to a uniform PPT implementation. At each fixed n, minimizing over arbitrary finite kernels says nothing about uniform asymptotic efficiency.

## Cheap diagnostic on the ideal secret-preserving family

**Fully written small calculation; no experiment.** Take the toy scalar ring n=1, q=3, m=1, sigma=1. This is only a diagnostic with explicitly changed dimension/modulus; it is not asymptotic evidence for the growing-n reference. Write t=W_{1,3}(0), h=W_{1,3}(1)=W_{1,3}(2), so t+2h=1 and t>h>0. For example t>h follows from W(0)>=1/Z while W(1)<=2/[Z(e^pi-1)]<1/Z.

Source U is uniform on Z_3 and A is uniform on Z_3. Given A=0, optimal source guessing is 1/3; given A nonzero, it is t. Therefore g_P=1/9+2t/3.

For the ideal target coupling Q_U, R is uniform and independent of the binary V, and recovering U from (R,A,B') is equivalent to recovering V from (A,B'). If A=0, guessing is 1/2. If A nonzero, summing the larger of the two likelihoods over B' gives guessing t+h/2. Hence g_Q=1/6+2t/3+h/3. For any kernel K, data processing prevents its guessing success from exceeding g_P; target joint TV error epsilon would force success at least g_Q-epsilon. Consequently average joint deficiency is at least

 g_Q-g_P = 1/18+h/3 > 1/18.

Thus the specified ideal coupling does not automatically admit even an unrestricted exact channel for every parameter choice. This lower bound does not exclude approximate channels in asymptotic identifiable regimes, and it is not a cryptographic lower bound.

Pre-release synthesis: retain at most two mechanisms (affine ring-unit transport and exact source-posterior transport). The ideal shift-coupling family makes the missing implication to search hardness concrete. The scalar Bayes-risk calculation is the preferred cheap diagnostic. The three-state example separately documents that matching Shannon information and optimal guessing is not sufficient for Blackwell order. No computer experiment, no new independent rotations, and no claim of complete reduction.
