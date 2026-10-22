# FF3-TWOSECRET-v1 proof

Fix label0. Then u=e and v=e+a(s0-s1). Since s0-s1 is a unit, conditional on every e, v is uniform. Thus (u,v) has exact product law nu_Q × Uniform. Applying independent H calls gives nu_q × Uniform. The inverse linear transformation has c=(u'-v')/(t1-t0), so conditional on every u', c is uniform and d-c*t0=u'. This is the claimed target law. For label1, the same argument gives Uniform × nu_Q and after H, Uniform × nu_q; now d-c*t1=v'.

Under the source comparator the map(a,b)→(u,v) is a bijection because s1-s0 is a unit. Thus u,v are independent uniform; applying H gives independent uniform u',v', and the target inverse is a bijection. Both endpoint normalizers are exact.

For multiple samples, condition first on the common label i. The input pairs and all fresh H random tapes are independent conditional on i, so their joint output is the product of the exact fixed-i target laws. Mixing the same one retained label on both endpoints then gives the full shared-secret law. This is a pointwise conditional product identity; no success-event posterior, hidden secret advice, or cached-prefix independence assumption occurs.

At n1, the binary secret set is exactly {0,1}; choose both pairs s0=t0=0, s1=t1=1. The theorem then applies to the entire n1 binary experiment. Existence of H is a one-dimensional transport question. For rational finite laws it is exactly the finite LP row constraints sum_y H(x,y)=1, uniform pushforward N_Q^-1 sum_x H(x,y)=N_q^-1, and noise pushforward sum_x nu_Q(x)H(x,y)=nu_q(y). These are sufficient as proved; no Gaussian smoothing assumption is hidden.

This construction has no immediate cube extension. For three or more candidate secrets, the residuals b-a*s satisfy deterministic affine relations. Applying independent H kernels to all residuals generally violates those relations and need not yield any pair(c,d). Supplying the true s to select one residual would violate the unknown-secret interface, even if an outer wrapper happens to know a secret in a different experiment.
