# FIXED-MAIN-v1: restricted ideal BDD from fixed-modulus decision binary RLWE

PROVISIONAL. This binds the exact AM-MAIN-v3 and MR-v1 statements and their definitions. No new component or main claim is accepted before complete exact-version review.

## Fixed target and supplied input

Let n>=2 be a power of two and R=Z[X]/(X^n+1). Supply an ordinary integer basis of a nonzero integral ideal J with D=N(J)<=2^(rho*n), for a fixed 0<=rho<1. The desired output is bounded-distance decoding in J^-1, in the canonical infinity norm, with radius r defined below. Neither an ideal Gaussian sampler nor a short basis/trapdoor is supplied.

Fix an integer target modulus q0>=2, rational coefficient Gaussian width sigma0>=1, integer sample count k0>=1, and rational advantage lower bound 0<epsilon_*<1. Supply all-input bounded finite randomized Boolean code D0 with a charged worst-case runtime bound on every valid k0-sample input and every random tape. In the target planted experiment, a SINGLE S is uniform in {0,1}^n; A_1,...,A_k0 are independent uniform R/q0R; all k0*n error coefficients are independent D_(Z,sigma0); and B_i=A_i*S+E_i modq0. In the comparator, the same A and metadata law is retained, while all responses are independent uniform R/q0R. The absolute signed acceptance gap of D0 is at least epsilon_*. The sign is not supplied.

If D0 receives J or its basis as metadata, its premise is pointwise for that same supplied J. Otherwise the target promise is independent of J. No averaged-ideal premise is substituted. The target modulus q0 need not be prime or split; the auxiliary moduli below are split primes. No target secret randomization by an unknown cube translate is performed.

## Auxiliary list, exact widths and guards

Supply or construct independently of J a master list Q0 of M+n DISTINCT odd primes q congruent1 modulo2n, with Qmin<=q<=Qmax, using the exact DD2-PRIMES-v1 construction if desired. Require

    sigma0 >= 8*k0*n*(n/2+2)/epsilon_*,
    q0 >= n*sigma0,
    M >= ceil(4n/epsilon_*),
    Qmin >= max(3,56*k0*n*q0/epsilon_*).

For every master-list q define the represented rational width

    sigma_q=(q/q0)*sigma0.

Instantiate AM-MAIN-v3 with epsilon0=epsilon_*/2, hence epsilon=epsilon_*/4, this master list, and these sigma_q. Use its exact definitions of Ncal,Ntest,K,ell,sigma_floor, all finite error terms, common C8 parameters, delta=epsilon_*/16, Q_*, chi,d0 and r=d0/Qmax. In addition to its finite numerical guard (G-AM) and C8/uniqueness guards, require explicitly

    Qmin>=n*sigma_floor,
    (Qmin/q0)*sigma0>=sigma_floor.

Then every sigma_q lies between sigma_floor and q/n. All input lengths, rational evaluation routines, scalar samplers, root enumeration and uniform-draw caps are charged exactly as in AM-MAIN-v3. These inequalities are mathematical premises on supplied represented parameters, not instructions to perform unbounded tests at transcendental equality boundaries.

Define the all-input bounded auxiliary code D_alg(q,((A_i,B_i))_i) by coefficientwise deterministic scaling and rounding of every pair from modulus q to q0, with representatives0,...,q-1 and rnd(x)=floor(x+1/2), followed by one fresh execution of D0 on the resulting k0 pairs. Its only access to D0 is classical finite code execution. Both auxiliary worlds give it exactly the same q and public metadata. The wrapper can keep q private from D0; the fixed q0,sigma0 remain its prescribed parameters.

## Conclusion, costs and scope

Execute the complete AM-MAIN-v3 decoder with this D_alg: filter the master list by divisibility of D, retain M primes in its fixed order, run all M bounded C8 decoders on qT, and verify divided candidates by exact J^-1 membership and coefficient squared distance at most r^2. For every rational input T=lambda+e, lambda in J^-1, with canonical infinity norm of e at most r, it outputs the unique lambda with probability at least

    1-p,  p=(n/2)*exp(-kappa)+zeta<=17zeta/16.

The total number of calls to the original FIXED-target code D0 is at most

    M*Q_* * ((n+1)*Ncal + Qmax*Ntest).

Every such call uses exactly k0 q0-samples. The K auxiliary raw samples within one A_q execution share one binary secret; the known wrapper secret is fresh across executions. The complete reduction is all-input bounded, including wrong orientations and unsuccessful auxiliary moduli. Runtime is polynomial in full represented input lengths, numeric M,Qmax,K,k0,epsilon_*^-1,kappa, logP,log(zeta^-1), charged certified evaluation costs, and D0's supplied runtime. The added rounding cost is polynomial in k0,n,logQmax,logq0 per D0 call. There is no oracle assumption at multiple target moduli.

For a concrete nonempty asymptotic parameter/source family, fix integer b>=0,c>=1 and rho<1. Take k0<=n^b, epsilon_*=n^-c, sigma0=n^(b+c+4), and any polynomial-VALUE integer q0>=n*sigma0. For example q0=n^(b+c+6) is allowed; alternatively a split prime q0 of polynomial value above this threshold can be constructed using DD2-PRIMES-v1. Set

    M=ceil(2^24*n^(2c+4)),
    Qmin=ceil(q0*n^(b+2c+12)),

and construct the master list before defining K. For all sufficiently large powers-of-two n, every guard above and in AM-MAIN-v3 holds uniformly in the eligible ideal family. Choose a polynomial-VALUE kappa satisfying the C8 guards. For fixed or inverse-polynomial zeta, r is inverse polynomial and the reduction has polynomial bit complexity in n, the full ideal/oracle input lengths and their charged evaluation/runtime costs. P can have superpolynomial value; logP is polynomial. This is a conditional reduction and a nonempty parameter/source family, not an assertion that an efficient distinguisher with the promised advantage exists.

The result preserves the norm-restricted source family D<=2^(rho*n). It does not prove unrestricted worst-case hardness, practical security, hardness of this restricted ideal family, or quantum sampling composition. Its new decision bridge uses an averaged auxiliary functional bound; all target calls nevertheless use the ONE prescribed fixed modulus and independent coefficient discrete-Gaussian error law above.
