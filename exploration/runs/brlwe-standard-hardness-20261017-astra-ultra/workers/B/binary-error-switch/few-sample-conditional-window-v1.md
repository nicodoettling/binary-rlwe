# A concrete few-ring-sample conditional window

2026-10-17 22:08 UTC. PROVISIONAL; uses switch-gaussianize-theorem-v1 and its unreviewed proof. This is not a standard-hardness theorem. No new experiment.

Fix an integer c>=1 and power-of-two n>=4. Let q be a supplied odd fully split prime satisfying n^2<=q<=n^C for some fixed C>=2. Set

    t=1, M=1, k=c+2, N=c+4,
    L=ceil(log_2 n),
    sigma=2 ceil(sqrt((c+6)L)),
    eta=n^(-c)/8.

All ceilings here have exact integer/rational implementations. Suppose an oracle recovers the coefficient-binary secret from ONE rank-one ring sample with coefficient D_{Z,sigma} error and probability at least n^(-c). Then the frozen reduction distinguishes the explicitly declared BE(c+4) source from c+4 independent uniform ring pairs with advantage at least n^(-c)/2. It invokes the oracle once and runs in polynomial bounded time, including the finite additive sampler. The target modulus/noise ratio q/sigma is polynomially large.

Proof. The pivot succeeds with probability u=(1-1/q)^n>=1-n/q>=1-1/n>=3/4. Because pi>ln(2),

    delta_sigma<=3 exp(-pi sigma^2/4)
               <=3 n^(-(c+6)).

The frozen product bound therefore gives

    Delta<=2n delta_sigma+eta
          <=n^(-c)(6n^(-5)+1/8)
          <=n^(-c)/4

for n>=4. Since q>=n^2 and n>=2, 2/q<=1/n, and the untouched validation comparator accepts with probability at most

    (2/q)^(n(c+2))<=n^(-n(c+2))<=n^(-c)/16.

Thus source advantage is at least

    (3/4)(1-1/4-1/16)n^(-c)=33 n^(-c)/64>n^(-c)/2.

The input budget consists of ONE reserved binary-error pivot, ONE untouched output pair, and c+2 untouched binary-error validation pairs. Each pair is one whole ring equation, and all share the same original uniform secret. The result does not assume the n scalar rows inside a pair are independent. The full planted/comparator law, private metadata convention, zero-secret inclusion, exact uniform comparator, and finite-sampling loss are those of the parent theorem.

What this preserves: the source requirement can be a constant number of binary-error ring samples for fixed c. Therefore the O(n^2)-sample attack does not by itself eliminate this conditional edge. What remains missing: a standard Gaussian-RLWE or worst-case ideal-lattice reduction to this exact BE(c+4) challenge family at these q,n. Neither an ordinary-LWE theorem with a scalar sample limit nor an arbitrary-sample binary-error assumption supplies it. A decision oracle on the one-sample Gaussian target would need only the pivot and output pair (two source ring samples), but source decision hardness is equally unproved.
