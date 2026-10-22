# WEIGHT-COV-v1: revealing Hamming weight does not remove the affine covariance obstruction

Provisional author theorem; full and fresh blind review required.

Let n>=4 be a power of two and let T be the real negacyclic shift matrix, T^n=-I. For coefficient vector s define M_s=sum_j s_j T^j. Fix an integer w with2<=w<=n-2. Let (Delta,Z) be any joint real random vector pair with finite second moments, whose law may depend on n,w but is the SAME for every binary s of Hamming weight w. Put W_s=Z-M_s Delta and C=Cov(Delta).

If Cov(W_s) is the same matrix for every binary s of Hamming weight w, then C=0. If the entire distributions of W_s are equal for all these s, then Delta=0 almost surely. Thus a nontrivial affine random perturbation cannot produce a common exact error law even when the kernel receives the Hamming weight as advice. This is a finite-second-moment statement and does not require Gaussian perturbations.

The restrictions are substantive: for w=1, isotropic centered Gaussian Delta and Z=0 give a nontrivial common W_s distribution; for w=n-1, take Z=M_1 Delta where1 denotes the all-ones coefficient vector. At w=0,n there is only one secret. This theorem does not refute nonlinear kernels, secret-dependent perturbations beyond the weight, approximate transformations, or the hidden-secret marginal experiment. It supplies no TV lower bound for arbitrary finite-variance distributions.
