# Entropy calculation v2 — unfinished derivation supporting W1-ENTROPY

This adds finite inequalities to v1 without replacing its history. Deadline remains 2026-09-06T20:34:15Z. Academic theoretical binary-secret RLWE context and full scope are inputs/RESEARCH_SCOPE.md. The argument is not reviewed.

Let Z be integer noise and V independent uniform I. If (v,z)->v+z modulo q is injective for z in Box(L), set p=Pr[Z outside Box(L)]. The chain rule gives
H(V,Z | V+Z) <= h2(p)+p[log|I|+H(Z | bad)].
The zero-p branch is zero. To bound the remaining conditional entropy, add an independent uniform vector on [-1/2,1/2]^n. Its differential entropy is H(Z|bad). The Gaussian maximum-entropy bound and the raw second moment give
H(Z|bad) <= n/2 log(2pi e[E||Z||²/(np)+1/12]).
Thus polynomial E||Z||² and p<=exp(-Omega(log²n)) make the total entropy loss negligible, including the p log(1/p) term. A mere TV statement would not suffice without this moment bound.

For the exact one-dimensional conditional Gaussian at pivot v and center c, write
Z_v(c)=sqrt(v)(1+R_v(c)),
R_v(c)=2 sum_(k>=1) exp(-pi v k²) cos(2pi k c).
Differentiating at fixed c gives the exact entropy
H(D_{sqrt(v),c})=1/2 log v+1/2+log(1+R_v(c))+v R'_v(c)/(1+R_v(c)).
Both errors are uniformly negligible in c for v>=3sigma²/4, v<=sigma². The chain rule over exact sequential kernels then yields
H(H_seq|F)=1/2 log det B_F+n/2+negl,
without identifying H_seq with D_B. The full-path likelihood-ratio comparison with D_B can separately bound moments and tails.

Using -log det(I-X)>=Tr X, the mean broad-minus-completed entropy gap is at least
n tau² E||F||²/(2sigma²)-negl.
For ell>=1, each F coefficient has second moment >=2exp(-pi)/(1+ell), from its +/-1 atoms and Z_ell<=1+ell. At sigma=2n ell³,tau=ell, the gap is therefore at least
g0=exp(-pi)/[4 ell^4(1+ell)]
minus negligible terms. This intentionally conservative atom bound avoids a sharp asymptotic variance estimate.

An A-preserving stochastic map preserving uniform pairs has doubly stochastic C kernels at each a and cannot decrease H(C|A). If its planted output is within joint TV delta of A2, identical A marginals and conditional entropy continuity give
g <= delta*n log q+h2(delta),
where g is the actual entropy gap after the proved negligible corrections. Since h2(delta)<=2sqrt(delta) and delta<=sqrt(delta) on [0,1],
delta >= g²/(n log q+2)²
whenever g>0. Once corrections are <=g0/2 this gives a concrete inverse-polynomial lower bound.

Still required: verify all uniform discrete moment/tail and entropy derivative bounds, the coefficient-box injection gate, source conditional uniqueness, and comparator class. c>1/2 is used for the gate with L=ceil(sigma log n). W1 is integrating these ideas into a complete source-interface argument; a fresh nonauthor must review the exact final proof.
