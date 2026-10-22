# FF1-COV-v1: shared Gaussian correction obstruction

Status: PROVISIONAL author candidate. This excludes a precisely stated additive correction model. It does not exclude nonlinear normalized rounding kernels, S-dependent latent couplings, or all modulus-transfer methods.

Let n>=4 be a power of two and T the real n-by-n coefficient matrix of multiplication by X in R=Z[X]/(X^n+1). For binary S, let M_S be its negacyclic multiplication matrix. Let Delta,Z be any jointly distributed real n-vectors with finite second moments, with a law independent of S. Define the additive residual W_S=Z-M_S Delta. Suppose Cov(W_S) is the SAME matrix for S=0,1,X,1+X. Then Cov(Delta)=0. In particular no nondegenerate secret-independent Gaussian perturbation of the public multiplier, even correlated with the response perturbation, can produce a secret-independent residual covariance for every coefficient-binary S in this ring.

The statement permits arbitrary covariance of Z and arbitrary Delta/Z cross covariance. Gaussianity, scalar response noise and isotropy are not needed for the obstruction. Independence from S and the exact affine residual formula are needed. It concerns unconditional covariance of that stated correction model; covariance equality alone would still be insufficient for the full independent coefficient-discrete-Gaussian target.

A concrete isotropic example: at n=4, S_1=1+X and S_2=1+X^2 have the same Hamming weight two, but M_(S_1)M_(S_1)^T=2I+T+T^T whereas M_(S_2)M_(S_2)^T=2I. Thus equal binary Hamming weight does not fix the ring error covariance. Coefficient centering to +/-1 does not remove the general obstruction.

The degree n=2 is excluded deliberately: T+T^T=0, and appropriately correlated perturbations can equalize the four binary-secret covariances. This boundary case is a required regression.
