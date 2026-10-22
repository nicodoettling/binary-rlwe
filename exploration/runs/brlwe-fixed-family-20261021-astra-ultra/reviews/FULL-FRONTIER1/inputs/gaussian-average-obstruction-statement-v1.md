# GAUSS-AVG-v1: quantitative average-cube additive Gaussian obstruction

PROVISIONAL. This is a restricted-model diagnostic, not a lower bound for every modulus-transfer kernel.

Let n≥4 be a power of two, T the real negacyclic coefficient shift, S uniform in {0,1}^n, and M_S=sum_i S_i T^i. Let (Delta,Z) be any jointly Gaussian real n-vectors, possibly degenerate and with arbitrary means, independent of S. Write C=Cov(Delta), B=Cov(Z), and W_S=Z-M_S Delta. Let W_* have a fixed Gaussian law N(m_*,V_*), independent of S. Choose L>0 such that

    ||V_*||op≤L and ||Cov(W_s)||op≤L for every binary s.

A sufficient explicit bound is L≥max(||V_*||op,2 tr(B)+2n² tr(C)). Then

    TV(Law(S,W_S), Law(S,W_*))
      ≥ exp(-1/2) tr(C)/(16 n² L).

Thus when the public perturbation has inverse-polynomial nonzero covariance trace and all variances have polynomial bounds, this class has inverse-polynomial retained-secret discrepancy. It cannot achieve negligible full joint error at a fixed polynomial parameter family by changing an auxiliary modulus alone while those covariance scales remain as stated.

Scope: the perturbation law is SECRET-INDEPENDENT and the residual is exactly the displayed affine expression. Both residuals compared here are continuous Gaussian laws. No assertion is made about a final integer-rounding operation, exact coefficient discrete-Gaussian laws, center-dependent theta normalizers, secret-dependent Gaussian choices, nonlinear rejection kernels, unretained-secret marginal TV, or a polynomial-time sample-only distinguishing test. Data processing may decrease this discrepancy. The target source-to-decision theorem remains OPEN.

This strengthens the exact covariance diagnostic by using all four-corner faces of the cube. Exact failure at four exponentially rare secrets alone would not prove this conclusion. Degree n=2 is excluded, and the exact equal-covariance example in FF1-COV-v1 remains a regression.
