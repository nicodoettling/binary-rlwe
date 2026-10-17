# B-FC-v1 exact joint calculation and limited conclusion

Status PROVISIONAL. This supports joint-lattice-v3, but is not itself a new source-hardness or attack result.

Let V be the CRT evaluation matrix. A coefficient frequency v transforms to CRT-dual frequency a=V^(-T)v. Conditional on T, uniform U in I_T has character expectation 1 exactly when a vanishes on T and 0 otherwise: every active amplitude is uniform F_q including zero. Write Z(v)={root indices where a=0} and

  p(Z)=C(|Z|,d)/C(n,d).

For coefficient-iid D_ell error, psi(v)=product_j phi_ell(v_j/q), where

  phi_ell(theta)=[ell/Z_ell] sum_m exp(-pi ell^2(m-theta)^2)>0

by the one-dimensional Poisson identity. It is at most 1 by the triangle inequality. Therefore the exact same-T pair character is

  E chi_v(A_1) chi_w(A_2)=psi(v)psi(w) p(Z(v) intersect Z(w)).

For independently redrawn supports it is instead psi(v)psi(w)p(Z(v))p(Z(w)). The independent uniform comparator is zero at any (v,w)!=(0,0). All these calculations condition on the whole T once; no conditional Gaussian-independence replacement is used.

If v is nonzero, the same-T joint bias is at most psi(v)p(Z(v)), the first marginal's character bias; the corresponding statement holds for nonzero w. Thus the maximum over nontrivial joint characters equals the maximum over marginal characters, with equality obtained by setting the other frequency zero. This does not imply equality of full-law statistical distances.

A fixed real acceptance function f on R_q^2 has an exact finite Fourier expansion. If its nonconstant Fourier coefficients have l1 mass L, its absolute expectation discrepancy from uniform is at most L times the maximum nontrivial marginal character bias. This is only a bound for that declared Fourier mass. Adaptive frequency selection and nonlinear threshold tests require their entire acceptance-function expansion; a small number of queried characters by itself does not bound that mass.

For v=w with 0<p(Z(v))<1, the same-T versus redrawn-T character difference is exactly psi(v)^2 p(1-p)>0. The acceptance rule (1+Re chi_v(A_1)chi_v(A_2))/2 has uniform probability 1/2 and planted probability (1+psi(v)^2 p)/2; implementing its real acceptance coin to finite precision adds its explicit bounded approximation error. Character evaluation at chosen precision is polynomial in n,log q and precision bits, with polynomial memory. No algorithmic advantage over optimized ATT follows.

Finite evidence is fc-output-v1.json with code fc_controls_v1.py and command/limits fc-command-v1.txt. The 787 exact checks use rational coefficient product noise, expressly not D_ell. They validate the full character algebra and ideal zeros. The n=2,q=5,d=1 full-law control has marginal TV=1/25, pair TV=31/625 and same-T/redrawn-T TV=1/800. The separate D_1 diagnostic uses radius 6 with four-coordinate analytic tail <=1.62e-50 but unbounded floating-rounding error; it is evidence only. No finite calculation here proves asymptotic hardness or absence of nonlinear attacks.
