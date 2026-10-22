# FF3-ENUM-v1 proof candidate, corrected proof v2

REPAIRED-PENDING-RECHECK. This additive version corrects FULL-FF3-ENUM-SIGN-1 recorded in enum-repair-ledger-v1.md; the theorem-only exhaustive-kernel-statement-v1.md is unchanged. No review verdict on the frozen proof-v1 is inherited.

Fix two distinct coefficient-binary secrets s,t and d=s-t. The integer negacyclic multiplication matrix M_d is nonsingular: X^n+1 is irreducible over Q for power-of-two n, while d is a nonzero polynomial of degree<n. Every column of M_d has Euclidean norm ||d||2<=sqrt(n), so Hadamard gives

    1<=|det M_d|<=n^(n/2).

Write r for its rank modulo the prime Q. Smith normal form shows Q^(n-r) divides det M_d, because n-r invariant factors vanish moduloQ. Hence Q^(n-r)<=n^(n/2). For uniform A, A*d is uniform on the image of M_d, a set of size Q^r. Therefore for ANY coefficient subset Bbox of cardinality at most h^n,

    Pr[A*d in Bbox]<=h^n/Q^r<=h^n*n^(n/2)/Q^n.       (1)

This holds for every pair of distinct binary secrets, without excluding nonunits or selecting good primes. No CRT-coordinate independence of errors is assumed.

For E~D_(Z,sigmaQ), the denominator rho_sigmaQ(Z)>=1. Monotonicity of exp(-pi*x^2/sigmaQ^2) on positive x and the elementary Gaussian integral tail bound give, for T>0,

    Pr[|E|>T]
      <=2 sum_(m>=ceil T) exp(-pi*m^2/sigmaQ^2)
      <=(2+sigmaQ^2/(pi*T))*exp(-pi*T^2/sigmaQ^2).

The first sum deliberately overcounts when T is integral. A union bound over the n independent coefficient errors gives tailQ; independence is not even needed for this bound. Conditional on any fixed E in the coefficient box[-T,T]^n, the actual s passes the residual test. If a competitor t also passes, then A(s-t) moduloQ belongs to [-T,T]^n-E, a set of cardinality at most(2T+1)^n, contained in the centered box[-2T,2T]^n. We use the looser latter size(4T+1)^n. Apply(1) conditional on this E, then union bound over all2^n-1 competitors. This gives etaQ uniformly for every actual s. Thus with probability at least1-tailQ-etaQ, the unique retained t equals the actual s. On that event fresh target randomness yields the exact desired conditional law. Couple output and target using that randomness on success; on failure use any coupling. This proves the planted TV bound without conditioning the desired target law on the success event.

Under the comparator, for each candidate t and each fixed A, B-A*t is uniform in R/QR. Because2T+1<Q, its coefficient-box probability is exactly((2T+1)/Q)^n. A union bound gives betaQ for existence of any accepted candidate. On the complement the channel outputs the exact target comparator, independently of the source input. The same coupling argument gives the comparator TV bound. There is no assumption that the candidate returned on the rare accepted comparator event is uniform binary.

For a batch, condition on the actual shared s before applying the per-sample construction. Source samples and all channel random tapes are conditionally independent. The coupled mismatch probability is bounded by the union of k per-sample mismatch events, at most k(tailQ+etaQ); this does not require multiplying marginal failure probabilities. Retaining the same s and averaging gives the full planted bound. The comparator argument is identical with betaQ. CP-1's forbidden posterior-product inference does not occur.

For T=ceil(sigmaQ*n), T/sigmaQ>=n and T<=sigmaQ*n+1. With sigmaQ of polynomial value, the prefactor in tailQ is polynomial and exp(-pi*T^2/sigmaQ^2)<=exp(-pi*n^2). If Q>=16*n*(4T+1), then

    etaQ <= 2^n (1/(16 sqrt(n)))^n=(1/(8 sqrt(n)))^n,
    betaQ <=2^n (1/(16n))^n=(1/(8n))^n.

Both are negligible, as are their products with every fixed polynomial k. Also Q>=64*n*T>=64*sigmaQ*n^2, giving sigmaQ/Q<=1/(64n^2). If the target normalized width is still smaller, enlarge Q polynomially so Q>q0*sigmaQ/sigma0; all error bounds improve. The target parameters are not chosen after k, while the source and auxiliary polynomial exponents may depend on it.

The proof demonstrates statistical simulability with a fully normalized nonlinear kernel and exact target Gaussian conditional laws. Its enumeration over2^n candidate secrets is exponential; information-theoretic uniqueness is not an efficient inverse. This outstanding computational edge is explicit and prevents the main FF theorem.
