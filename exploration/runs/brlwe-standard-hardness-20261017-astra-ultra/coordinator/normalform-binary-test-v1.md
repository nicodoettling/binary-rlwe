# Normal-form Gaussian secret to binary: first endpoint test

Status PROVISIONAL, not a new hardness theorem. This is a scoped direct-query calculation within R1; adaptive simulation with new samples or dimension changes is not excluded.

Consider the favorable idealized normal-form secret X whose independent coefficients lie in Z and have masses proportional to exp(-pi(x-1/2)^2/t^2). This centered half-integer Gaussian is an explicitly hypothetical input law here; no standard RLWE theorem has yet been imported for it. Write p_t=Pr[X_i in{0,1}]. Conditional on X in{0,1}^n, X is exactly uniform binary, so a direct binary recovery call can be on-promise on this branch if all other target laws match.

The complete branch probability is p_t^n, with

    p_t = 2 exp(-pi/(4t^2)) / sum_(z in Z) exp(-pi(z-1/2)^2/t^2).

The next two Gaussian masses, at z=-1,2, have ratio exp(-2pi/t^2) to the binary pair. Therefore

    p_t^n <= (1+exp(-2pi/t^2))^(-n).

For every fixed positive t this is exponentially small as n grows. Keeping even an inverse-polynomial branch probability requires t=O(1/sqrt(log n)). The ratio of the uniform-binary probability to the Gaussian probability is exactly p_t^(-n) on the binary cube. Thus both the likelihood-ratio and order-two Renyi change-of-measure loss for this direct restriction are exactly p_t^(-n). A statement that the one-coordinate distributions look similar does not remove the product loss.

This can be witnessed by the success event itself: extend a binary recovery algorithm so that it always outputs a binary vector on every input. Direct recovery of the actual Gaussian X then has success zero outside the cube, regardless of target-error width. No invocation of off-promise guarantees is legitimate.

A separate finite-modulus bound applies to the usual centered integer Gaussian. Let X have n independent D_t coefficients reduced modulo odd q, let rho_t(Z)=sum_z exp(-pi z^2/t^2), and h=max_(a in Z/qZ) sum_k exp(-pi(a+kq)^2/t^2)/rho_t(Z). For any fixed bijection phi of (Z/qZ)^n, Pr[phi(X) in{0,1}^n]<=2^n h^n, because the preimage has exactly2^n elements and every atom of X has mass at most h^n. This statement is purely finite and does not replace h by an unproved Gaussian approximation. The same union bound applies to L maps fixed independently of X, giving min(1,L(2h)^n). Maps selected from observations correlated with X require a posterior analysis and are outside this assertion.

Known normal-form transformations, a choice of exact Gaussian representation, coefficient/canonical conversion, and published source hardness must be checked before composing either calculation with a standard RLWE premise. The constructive gap is an executable transformation that changes the secret law with polynomial loss while preserving the full target response law. Merely shifting a Gaussian center or renaming its width does not supply it.
