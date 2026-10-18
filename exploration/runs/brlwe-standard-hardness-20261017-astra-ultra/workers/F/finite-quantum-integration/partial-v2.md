# F finite quantum continuation: partial v2

Status: new construction, PROVISIONAL / UNACCEPTED. All v1 files remain unchanged. This is the original same-integral-J bridge, not a standard-family transfer.

The selected construction now has a concrete finite candidate. Clear denominators B=A/b of the rational coefficient lattice, choose a sufficiently large power-of-two H, and prepare an n-fold integer Gaussian at width r=bHd/sqrt(2n). A dyadic phase-average filter prepares each truncated scalar Gaussian without its normalizer. Its zero-Fourier-outcome probability is bounded below by 1/(512W); a fixed 4096W^2 retry cap suffices. Measurement modulo A Z^n followed by exact coset subtraction is compared on the complete joint state. Poisson summation gives a uniform shift bound for every ideal coset, so rare conditional branches are not discarded.

The finite Fourier transform can also avoid arbitrary-angle gates. Dyadic phase resource states are prepared by averages of the four phases 1,-1,i,-i; each attempt succeeds with probability at least 1/8. Exact bounded gate teleportation corrects dyadic angles after finitely many doublings. The finite gate set is H,S,CNOT,Toffoli,X, with measurements/reset/classical control. Normalization and capped retries are charged before conditioning. The remaining written obligation is to finish the standalone theorem, finite algorithms, explicit rational-evaluation gate bound and proof; none is accepted by its author.

One coherent BDD uncomputation remains, costing at most 2Q_* coherent executions of the supplied bounded recovery code. A direct periodization estimate gives the explicit proposed analytic error with tau_n=2^(n/2) exp(-pi n), c_n=2^(-16n):

    2 sqrt(tau_n) + 2 sqrt(2(tau_n+c_n)) + tau_n.

Add the finite synthesis/preparation allowance epsilon and 2 sqrt(p_BDD). The output is ordinary D_(L*,sqrt(n)/(sqrt(2)d)), hence the same J at coefficient width nq/(sqrt(2)d0).

Reservation F-QFINITE-FV1 was granted before the single foreground job. All 9,288 exact finite algebra/conditioning controls passed in 0.18 seconds, max RSS 12,288 KiB. The complete input, source, command, stdout, empty stderr and time/resource record are retained. These controls do not certify the transcendental Gaussian estimates or a complete quantum circuit. Rare-branch and normalization failures were recorded before running the controls.

The prime-size addendum will separate the old factorial construction's polynomial bit length from polynomial value. The supplied A lemma uses a least-prime-in-progression result for the stronger value bound, with the gcd(N(J),q)=1 condition retained. No factoring algorithm or arbitrary-ideal normalization is inferred.
