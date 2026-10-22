# FF3-ENUM-v1: a normalized negligible-error channel with explicit exponential cost

Let n>=2 be a power of two; R=Z[X]/(X^n+1); Q an odd prime; T a positive integer with 4T+1<Q. The source has one uniform coefficient-binary S, uniform A in R/QR, and B=A*S+E modQ, with independent coefficient errors D_(Z,sigmaQ), sigmaQ>=1. Let q0>=2 and sigma0>=1 be arbitrary target parameters; the target law uses uniform C in R/q0R and D=C*S+F modq0 with exact independent coefficient D_(Z,sigma0) errors. The comparator at each modulus is uniform independent public/response pairs.

Define a secret-independent normalized channel: enumerate every t in {0,1}^n and keep those for which every centered coefficient of B-A*t modQ has absolute value at most T. If exactly one t survives, generate a fresh exact target sample with secret t; otherwise generate a fresh target comparator sample. This algorithm receives no true-secret advice. It has exponential worst-case arithmetic cost O(2^n poly(n,logQ)) per sample, plus target sampling, and can stream candidates using polynomial memory. The declared exponential enumeration is essential to the present implementation.

Put

    betaQ = 2^n ((2T+1)/Q)^n,
    etaQ = (2^n-1) ((4T+1)*sqrt(n)/Q)^n,
    tailQ = n (2 + sigmaQ^2/(pi*T)) exp(-pi*T^2/sigmaQ^2).

For every fixed binary S=s, the planted output is within min(1,tailQ+etaQ) TV of the exact target conditional law at s, including its independent uniform public multiplier and independent coefficient Gaussian errors. The comparator output is within min(1,betaQ) TV of the target comparator. For k independent invocations on conditionally iid source samples with one shared retained S, the full planted joint TV is at most min(1,k(tailQ+etaQ)); the comparator batch TV is at most min(1,k betaQ).

For any polynomial-value source width sigmaQ(n)>=1, choose T=ceil(sigmaQ*n), and an odd prime Q>=16*n*(4T+1). Then tailQ,etaQ,betaQ are negligible in n; this one channel family consequently works statistically for every fixed polynomial sample exponent. Its normalized source noise sigmaQ/Q<=1/(64 n^2), and increasing Q also permits any fixed target reserve requirement sigmaQ/Q<sigma0/q0. A prime Q of polynomial VALUE may be supplied; its construction is a separate routine and is not needed for this conditional finite statement. q0,sigma0 may be fixed before sample/advantage exponents. Source sigmaQ,Q may depend on them.

This provides an explicit nonlinear positive kernel with both endpoints, but not an efficient implicit kernel. Finding the unique surviving t is a binary-RLWE bounded-error search problem; there is no claim that its uniqueness gives polynomial-time recovery. Replacing enumeration by a supplied decoder changes the assumptions and is not an FF proof. The elementary coefficient-box test is used here only to define an exponential simulator, never to identify the actual secret in an information upper bound.

Exact discrete-Gaussian target sampling defines a mathematical kernel. If implemented with all-input bounded finite scalar samplers of total TV xi per output, add k*xi to the displayed endpoint bounds and charge their bit cost. No continuous Gaussian or Gaussian moment replacement occurs.
