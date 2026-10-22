# FRAC-INFO-v1: fixed-noise fractional experiments eventually identify the binary secret

Let n>=2 be a power of two, R=Z[X]/(X^n+1), J a nonzero integral ideal, Lambda=J^-1 in coefficient Euclidean space, and D=N(J). Let q>=3 be an integer coprime to D. Identify Lambda/qLambda with R/qR by v/D -> v D^-1 modq. Let s,sigma>0 be real Gaussian widths. Independently draw K source vectors a_i from D_(Lambda,s), expose their identified residue classes A_i, draw one coefficient-binary S uniformly from {0,1}^n, and independent exact coefficient D_(Z,sigma) errors E_i. Observe (A_i,B_i=A_i S+E_i modq) for all i. Every law below includes the one retained S and all its conditional sample laws.

Put

    U(s,n) = (sum_(z in Z) exp(-pi*s^2*z^2/2))^n,
    mu = max(0, 1-exp(-pi*s^2/(2q^2))*U(s,n)),
    gamma = exp(-pi*sigma^2/q^2) / sum_(z in Z) exp(-pi*sigma^2*z^2),
    delta = gamma*mu/2.

If mu>0, then for every two distinct binary secrets b,c, the one-sample conditional laws P_b,P_c satisfy TV(P_b,P_c)>=delta. There exists a deterministic maximum-likelihood estimator from the K observed samples (ties fixed) whose conditional failure probability for every S=b is at most

    min(1,(2^n-1)*exp(-K*delta^2/2)).

No efficient maximum-likelihood implementation or exact finite transcendental comparison is asserted. This is a statement about the optimal statistical success probability on a finite observation alphabet.

For any one fixed polynomial-value family q(n) with n^4<=q(n)<=n^B, sigma(n)=n^2, let K(n)=n*q(n)^4, ell=ceil(log2(2nK)), and s(n)=sqrt(2)*ell^2. For all sufficiently large powers-of-two n, mu>0, delta=Omega(s(n)^2/q(n)^2), and the displayed failure bound is exp(-Omega(n*(log n)^8)). The constants may depend on the fixed B, not on J. Thus this precise family has statistical secret recovery probability tending to1 even in the fractional source experiment, uniformly for eligible J coprime to q. The statement also holds for any restricted eligible ideal family, including D<=2^(rho n); this restriction is not needed in the proof.

Consequently an extension that upper-bounds **every** recovery algorithm's fractional-source success by a fixed small information bound, at this fixed q,sigma and for all polynomial physical sample exponents, cannot be true. Revealing additional latent variables cannot restore such an upper bound. This conclusion does not refute a computational comparison restricted to specific efficient extractors, a different source distribution, a nonlinear reduction, or a direct decision advantage argument. It does not establish an efficient attack on either the source experiment or target RLWE and does not change the actual delivered BDD radius.
