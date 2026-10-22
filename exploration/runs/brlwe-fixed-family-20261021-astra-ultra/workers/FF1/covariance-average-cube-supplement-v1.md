# FF1-COV average-cube supplement, version 1

PROVISIONAL author claim. This supplements, without editing, FF1-COV-v1. It is still an exact covariance result, not a lower bound on approximate total variation.

Under the same additive model W_S=Z-M_S Delta, with the joint finite-variance law of (Delta,Z) independent of S and n>=4 a power of two, suppose a single matrix V_* equals Cov(W_S) for MORE THAN3/4 of all binary S. Then Cov(Delta)=0.

Proof: partition the binary cube into disjoint four-corner faces by holding every coefficient except coefficients0 and1 fixed. If no face had all four corners good, at most3/4 of the cube could be good. Therefore one face consists of T0,T0+1,T0+X,T0+1+X with the same covariance V_*. The second difference of the covariance formula is again TC+CT^t, independent of T0 and of the response/public cross covariance. The Fourier/PSD argument in FF1-COV-v1 gives C=0.

This addresses the fact that the four specific low-weight secrets in v1 have exponentially small probability in a uniform cube. Exact covariance equality on almost all secrets is also impossible in that additive model. However negligible-TV approximation does NOT imply exact covariance equality, and TV alone does not bound second moments without a tail condition. Thus neither v1 nor this supplement is an average-cube TV impossibility theorem. A nonlinear normalized rounding kernel, or an approximate additive law with carefully controlled nonzero covariance errors, remains outside the conclusion.

Potential quantitative continuation: if four corners each have covariance operator error<=eta from V_*, then ||TC+CT^t||op<=4eta. In a Fourier basis its diagonal gives 2|Re(zeta_j)| C'_(j,j)<=4eta. This yields a trace bound by summing1/|Re(zeta_j)|, but turning it into a transfer-TV bound additionally requires full error-tail control and a nonnegligible set of suitable faces. No such main transfer lower bound is asserted here.
