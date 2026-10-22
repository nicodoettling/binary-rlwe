# WEIGHT-GAUSS-v1: quantitative obstruction with Hamming-weight advice

Provisional author candidate; full and fresh blind review required.

Let n>=4 be a power of two,2<=w<=n-2, and S uniform on the binary vectors of Hamming weight w. Let (Delta,Z) be jointly Gaussian real vectors, independent of S within this weight slice, with arbitrary means/cross covariance, C=Cov(Delta), B=Cov(Z). Let W_S=Z-M_S Delta, using negacyclic multiplication. Let V_* be any positive semidefinite target covariance; target Gaussian means may depend on S. Choose L>0 bounding both ||V_*||op and every ||Cov(W_s)||op. The explicit choice max(||V_*||op,2tr(B)+2n^2 tr(C)) is valid when positive.

Define the exact rational weight-slice coverage

    p_w=4*w*(w-1)*(n-w)*(n-w-1)/(n*(n-1)*(n-2)*(n-3)).

The joint laws retaining the SAME uniform S satisfy

    TV(Law(S,W_S), Law(S,targetGaussian_S))
       >= exp(-1/2)*p_w*tr(C)/(n^3*L).

A target Gaussian_S here has covariance V_* and any specified mean depending on s; its conditional law is compared pointwise. For a uniform binary S and a perturbation law allowed to depend on w=|S|, apply the bound conditionally at each interior weight and average with weights binom(n,w)/2^n. The target covariance and positive L may also depend on w. No claim is made at boundary weights0,1,n-1,n, where nontrivial exact examples exist.

This supplies an inverse-polynomial retained-secret TV obstruction if the weighted normalized trace is inverse polynomial. It applies ONLY to continuous jointly Gaussian affine perturbations with advice restricted to the weight. It does not rule out arbitrary nonlinear kernels, different secret-dependent advice, non-Gaussian tails or the hidden-secret marginal experiment. Finite floating diagnostics cannot certify the infinite Gaussian law.
