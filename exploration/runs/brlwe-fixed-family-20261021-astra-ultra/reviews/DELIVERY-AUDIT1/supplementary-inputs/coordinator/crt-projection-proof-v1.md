# CRT-PROJ-v1 proof candidate

PROVISIONAL. Binds crt-projection-statement-v1.md. Full/blind review and finite checks pending.

For a nonzero character u∈F_q^h of the projected error distribution, write z_i as the centered representative of sum_(alpha in T) u_alpha alpha^i modq. The full character is exp(2pi i sum_i z_i E_i/q). Let Z(X)=sum_i z_i X^i. At each root beta^-1, evaluating the coefficient formula modulo q gives Z(beta^-1)=n u_beta when beta∈T and zero otherwise: the geometric sum of (alpha/beta)^i is n for alpha=beta, zero for distinct roots. Since q does not divide n, the vector z is nonzero modulo q and hence as an integer polynomial. The multiplication matrix of Z in R has nullity at least n-h modulo q. Integer Smith normal form gives q^(n-h) dividing its nonzero algebraic norm; this uses q prime, separability, and irreducibility of X^n+1 over Q. The scaled-unitary canonical evaluation matrix and AM-GM give |N(Z)|≤||z||₂^n. Therefore ||z||₂≥q^(1-h/n). Centering makes sum_i dist(z_i/q,Z)²=||z||₂²/q²≥q^(-2h/n).

For theta∈[-1/2,1/2], Poisson summation for the one-dimensional Gaussian gives

    |E exp(2pi i theta E_0)|
      = [sigma/rho_sigma(Z)] sum_(m∈Z) exp(-pi sigma²(m-theta)²)
      ≤ 3 exp(-pi sigma² theta²).

Here rho_sigma(Z)=sigma rho_(1/sigma)(Z)≥sigma. For theta∈[0,1/2], divide the sum by exp(-pi sigma² theta²). Terms m=0 and m=1 contribute at most2; the sum of m≤-1 and m≥2 is at most 2 sum_(j≥1)exp(-pi j²) <1 when sigma≥1. The case theta<0 follows by symmetry. Thus the constant3 is valid including endpoints; the exact Fourier coefficient is nonnegative and real under the Poisson representation. Independence of the n COEFFICIENT errors, not of CRT errors, now bounds every nontrivial projected Fourier coefficient by 3^n exp(-pi sigma² q^(-2h/n)). Finite-group Parseval and Cauchy-Schwarz imply TV≤(1/2)(sum_(u≠0)|hat P(u)|²)^(1/2), yielding the displayed bound.

Uniformity in T is deterministic: the norm argument uses only its cardinality. Conditional on fixed s and public A, the projected response is translated by the fixed A_T s_T, so TV is unchanged; A has the same law in both endpoints. For a k-sample product conditional on s, replace one error tuple at a time and use the triangle inequality (or failure-event coupling), giving k times the error. No multiplication of marginal event bounds is used. With a disjoint selection bank, condition on s and its complete transcript before invoking independence of the new bank; all conditional normalizers are those of a positive-probability history. Choosing T after inspecting the same bank is outside this statement.

For binary-certificate injectivity, if distinct b,b' agree at r distinct roots then f=b-b' is nonzero with coefficients in {-1,0,1}. As above q^r divides |N(f)|, while |N(f)|≤||f||₂^n≤n^(n/2). But r>n log n/(2log q) makes q^r>n^(n/2), a contradiction. This statement involves multiple DISTINCT roots at ONE prime. It does not replace the inherited averaging of distinct primes by repeated primes; it uses multiplicity in the norm at distinct CRT roots, justified by Smith normal form.

In the illustrative family and h≤r-1, 2h log q/n≤log n, so sigma² q^(-2h/n)≥n³; also (h/2)log q≤(n/4)log n. This gives the final negligible bound. Numeric q remains polynomial with fixed exponent; reduction costs may depend on that exponent, while no target choice depends on sample/advantage exponents.
