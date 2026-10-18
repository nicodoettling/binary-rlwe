# Exact Renyi cost for coefficient-uniform plus Gaussian errors

2026-10-17. PROVISIONAL analytic theorem for independent review. No experiment. This is a scoped distribution-change calculation, not an impossibility theorem for arbitrary reductions.

Let U be uniform on E=[-B,B], B>0, and G have density w^(-1) exp(-pi x^2/w^2), w>0. Let Q=law(U), P=law(U+G), and define the exponentiated order-two Renyi divergence

    R2(Q||P)=integral q(x)^2/p(x) dx.

For D independent coordinates, R2(Q^D||P^D)=R2(Q||P)^D.

## Theorem

For0<w<=B,

    exp(c D w/B) <= R2(Q^D||P^D) <= exp(C D w/B),

where c=exp(-pi)/4 and C=exp(pi/4)/pi. Forw>=B the lower bound is exp(cD). Hence, for D=nm with m polynomial and n growing, polynomial Renyi loss is possible only if w/B=O(log n/(nm)); for w<=B that condition is also sufficient, up to the fixed constants above.

## Proof

For x in E, write

    F(x)=Pr[G in[x-B,x+B]],  p(x)=F(x)/(2B).

Then R2(Q||P)=(2B)^(-1) integral_E 1/F(x) dx. The escape probability satisfies the exact identity

    L=Pr[U+G notin E]
     = E[min(|G|/(2B),1)]
     = (2B)^(-1) integral_E (1-F(x)) dx.

The first equality after L follows by conditioning on G: the overlap of E and E-G has relative length max(1-|G|/(2B),0). The second follows from integrating the convolution density on E.

Cauchy–Schwarz on E gives R2(Q||P)>=1/P(E)=1/(1-L)>=exp(L). The event w/2<=|G|<=w has probability

    2 integral_(1/2)^1 exp(-pi u^2)du >= exp(-pi).

On this event min(|G|/(2B),1)>=min(w/(4B),1). Therefore

    L >= exp(-pi) min(w/(4B),1)
      >= c min(w/B,1).

This proves the lower bounds after taking D independent coordinates.

For w<=B, F(x) is minimized at x=+-B: differentiating the symmetric unimodal Gaussian integral shows it decreases with |x|. Thus

    F(x)>=Pr[0<=G<=2B]
         >=integral_0^(1/2) exp(-pi u^2)du
         >=(1/2)exp(-pi/4)=:c0.

Since1/F-1=(1-F)/F,

    R2(Q||P)-1 <= L/c0.

Also L<=E|G|/(2B)=w/(2pi B). Hence

    R2(Q||P)<=1+C w/B<=exp(C w/B),

where C=exp(pi/4)/pi. Taking powers proves the upper bound. All densities are normalized; no lattice theta term is involved. Q is absolutely continuous relative to P, while P is not absolutely continuous relative to Q.

## Exact application to the candidate

For R=Z[X]/(X^n+1) with n a power of two, canonical G_alpha has independent coefficient G_w with w=alpha/sqrt(n). A coefficient-uniform error cube has independent uniform coordinates. The actual joint change of measure for m samples therefore has D=nm and is exactly the divergence above. This calculation includes the latent errors and consequently any deterministic response map; forgetting errors may reduce divergence, so the lower bound is specifically for this latent-noise change-of-measure method. It is not a lower bound on the public transcript divergence.

For a favorable shifted interval whose rounding yields iid bits, B=1/2. Polynomial loss through this particular method NECESSARILY forces w=O(log n/(mn)), not merely because of a conservative sufficient estimate. At that width, the original primal continuous-Gaussian rank-one source is easy by coefficient rounding:

    Pr[some coefficient error has |e|>=1/2]
       <=2mn exp(-pi/(4w^2))=negl(n).

With a designated unit multiplier, recover s from its rounded response and check the remaining equations. The exact comparator rounds from Haar on K_R/qR to uniform R_q and passes those m-1 independent checks with probability q^(-n(m-1)). For q>=n^2, pivot success is(1-1/q)^n. With m>=2 this gives a polynomial distinguisher with advantage tending to1. This does not show anything about the original binary target's security; it rejects a purported hard-source instantiation of this particular Gaussian-plus-uniform/Renyi route.

Shifts of the uniform interval leave the divergence unchanged. Arbitrary adaptive oracle transformations, correlated noise simulations, changes in rank/degree, and other comparison measures are outside this theorem. Rounding the broad uniform law is not the original iid Gaussian error target; that further interface would also need proof.
