# Source sample budget and the missing reverse direction

2026-10-17. PROVISIONAL mathematical checks, not accepted. No experiment is needed or claimed. This note qualifies the conditional switch in switch-gaussianize-theorem-v1.md.

## 1. An actual large-sample binary-error attack

Let n>=1, q>=5 an odd prime, and let m ring samples share an arbitrary secret s in R_q=F_q[X]/(X^n+1), with iid uniform multipliers and independent coefficient-binary errors. Set

    D=n(n+3)/2.

There is an elementary polynomial-time search algorithm with failure probability at most

    (q^D-1)(2/q)^m.

In particular, m=2D+2lambda ring samples suffice for failure at most 2^{-lambda}, for any positive integer lambda. This uses only the constant coefficient from each ring response; it never treats the n correlated equations within a ring sample as independent.

Proof. The constant coefficient of a*s is the inner product of the coefficient vector of s with the row

    (a_0,-a_{n-1},...,-a_1).

This is a signed permutation of the iid uniform coefficient vector a and is therefore uniform F_q^n; these rows are independent across ring samples. Write the scalar equation as b=<a,s>+e with e in {0,1}. The polynomial

    P(x)=(b-<a,x>)(b-<a,x>-1)

vanishes at x=s. Expand it as a linear equation in the D nonconstant monomials x_j and x_j*x_k for j<=k, with constant term moved to the right side. Solve the resulting m-by-D linear system. If its row rank is D, its unique solution is the genuine monomial vector of s, so the first n entries recover s exactly.

It remains to bound rank failure rather than assume genericity. Translate x=s+y. Then

    P(s+y)=<a,y>^2+(1-2e)<a,y>.

The row a'=(1-2e)a is uniform F_q^n, even for any independent biased bit e, and this polynomial is <a',y>^2+<a',y>. Translation induces an invertible linear transformation on the D nonconstant coefficient coordinates of polynomials vanishing at s: it preserves quadratic coefficients and changes the linear coefficients triangularly. Thus it preserves rank.

For each nonzero dual vector v in F_q^D, its inner product with the translated coefficient row is a nonzero polynomial in a' of total degree at most two. It is nonzero because the linear, square, and cross monomials are distinct and 2 is invertible. The elementary Schwartz–Zippel bound gives probability at most 2/q that this inner product vanishes. Independence across the m ring samples gives (2/q)^m. Union bound over the q^D-1 nonzero v proves the rank bound. Finally, q>=5 implies 2/q<=q^{-1/2}; substituting m=2D+2lambda gives failure <=q^{-lambda}<=2^{-lambda}.

The runtime is polynomial in m,n,log q by finite-field linear algebra; for example the straightforward solve uses O(mD^2) field operations. The input sample count is in ring pairs, not scalar equations.

A decision attack uses one additional untouched ring sample. Recover shat from the first m pairs if possible, and test whether every coefficient of the fresh residual b-a*shat is a bit modulo q. Planted acceptance is at least 1-(q^D-1)(2/q)^m. On the uniform comparator the test accepts with probability at most (2/q)^n, because its response is fresh independent uniform conditional on the candidate. This gives the corresponding explicit decision advantage.

Scope. This is a sufficient large-sample attack threshold, not an optimal attack bound. It leaves one/few-ring-source regimes unresolved. A possible source theorem must permit the actual t+M+k ring pairs consumed by the conditional switch while avoiding its applicable attack regime. Arbitrary polynomial target M cannot be imported from a bounded-sample source theorem. In particular, an assumption declaring binary-error RLWE hard for every polynomial number of ring samples is false in this model, whereas ordinary Gaussian-error RLWE permits arbitrarily many polynomial samples under its standard formulation.

## 2. Why deconvolution does not run backwards publicly

The constructive scalar identity is

    Bernoulli(1/2) * F_sigma = Q_sigma ~ D_{Z,sigma}.

It implements addition of F_sigma to an already binary, unknown error. It does not give a public algorithm for splitting an unknown Gaussian error into a binary variable plus a correlated F_sigma component.

A precise limited obstruction: let G have iid coefficient D_{Z,tau} law, and let Z be any independently sampled integer vector, even with correlations among its coordinates. For each fixed z,

    Pr[G-Z in {0,1}^n | Z=z]
       = product_j (Pr[G_j=z_j]+Pr[G_j=z_j+1])
       <=(2/rho_tau(Z))^n <=(2/tau)^n.

Averaging over Z preserves the bound. In the modular variant, let h_tau,q be the wrapped scalar Gaussian mass. Then the exact upper bound is

    [max_c (h_tau,q(c)+h_tau,q(c+1))]^n,

which is at most [2(1/tau+1/q)]^n using the standard unimodal arithmetic-progression bound. One proof is to bound the sum of exp(-pi x^2/tau^2) on any q-spaced translated grid by its maximum 1 plus its integral tau divided by q, then divide by rho_tau(Z)>=tau. This applies whether or not Z itself is reduced modulo q.

For a designated unit pivot with uniform original secret, its public pair (a_0,b_0) is independent of the pivot error conditional on a_0, because b_0=a_0s+e_0 is uniform. Therefore sampling Z from that pivot pair and independent coins is still within this conditional independent-shift calculation. Using additional challenge responses to correlate Z with the unknown error is a different algorithmic obligation; the bound makes no claim about such adaptive reductions.

Thus the new exponentially accurate forward Gaussianization does not evade the earlier Gaussian-pivot-to-bits mass problem by reversing its formula. A posterior sampler conditioned on the actual hidden error, or exact hints revealing a component of that error, is not supplied by the standard public challenge. Source hardness remains OPEN.
