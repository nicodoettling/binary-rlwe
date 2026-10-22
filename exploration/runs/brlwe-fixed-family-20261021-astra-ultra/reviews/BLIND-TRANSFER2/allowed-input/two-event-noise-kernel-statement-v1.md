# FF3-TWOEVENT-v1: theorem-only statement

Let X,Y be nonempty finite sets with uniform probability laws U,V. Let P be any law on X and let N be a strictly positive law on Y. Let C be a subset of X, with p=P(C),u=U(C), and0<u<p<=1. Define L(y)=N(y)/V(y). Assume

 (1-p)/(1-u) <= min_y L(y),
 max_y L(y) <= p/u.

Then the following rows are probability distributions:

 g1(y)=[(1-u)N(y)-(1-p)V(y)]/(p-u),
 g0(y)=[p V(y)-u N(y)]/(p-u).

The Markov kernel H(x,.)=g1 for x in C and H(x,.)=g0 otherwise satisfies PH=N and UH=V exactly.

If p>=3/4 and u<=1/4, an ideal sampler for g1 proposes y~N and accepts with probability1-[(1-p)/(1-u)]/L(y); a sampler for g0 proposes y~V and accepts with probability1-(u/p)L(y). Both have acceptance probability at least2/3, so expected trials at most3/2. Capping at ell trials and using any fallback adds per-input TV at most3^(-ell). Numerical evaluation or proposal-sampling errors require separate explicit accounting; the statement does not claim a finite exact implementation for arbitrary real probabilities.

Gaussian instantiation claim: let X=R_Q,Y=R_q in coefficient degree n, and let P,N be exact wrapped independent coefficient D_Z,sigmaQ and D_Z,sigma0 laws. Suppose sigmaQ,sigma0>=1, q>=n*sigma0, and these quantities have polynomial numerical value in n. Choose T=ceil(sigmaQ*n*q/sigma0), Q>=4q(2T+1), and C the centered coefficient box[-T,T]^n moduloQ. Then for all sufficiently large n the two likelihood inequalities hold, p>=3/4 and u<=1/4. Thus the exact mathematical kernel H exists. Here

 u=((2T+1)/Q)^n,
 p=(Pr[E modQ has centered representative in[-T,T]])^n,
 L(y)=q^n product_j Pr[E0 modq=y_j],

with independent scalar E~D_Z,sigmaQ and E0~D_Z,sigma0. These are explicit one-dimensional theta normalizers. Finite n needs certified checking of the stated inequalities. A polynomial finite-precision implementation is not part of this claim.

This theorem is solely a noise-law kernel. It does not choose unknown binary-secret residuals or imply the full fixed-family modulus-transfer reduction. Its use in a two-secret transfer additionally requires the exact two-secret theorem assumptions.
