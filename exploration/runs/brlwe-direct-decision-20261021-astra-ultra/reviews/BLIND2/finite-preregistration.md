# BLIND2 finite structural checks, preregistered before execution

Hypotheses: (H1) deterministic coefficient rounding commutes with modulus reduction and gives a secret-dependent error offset bounded by n/2, including negacyclic signs and midpoint ties; (H2) the extractor's shifted-public-pair law equals precisely one of its two hybrids for every fixed secret and error, including the mismatched candidate; (H3) every collision of binary differences at an auxiliary root contributes a distinct prime divisor of the nonzero algebraic norm.

Code: finite-checks.py in this BLIND2 directory. Its SHA256 is recorded separately before the slot request. No random seeds: exhaustive deterministic loops only.

Inputs and finite bounds: H1 uses n=2, the nine (Q,q) pairs listed in code, every public vector, every binary secret and every error vector in [-3,3]^2. H2 uses n=2,q=5,k0=1, roots 2,3, all four binary secrets, all 25 fixed CRT error vectors, both roots, all candidates, public vectors, scalar shifts and prefix masks. H3 uses all 3^8-1 nonzero ternary vectors at n=8 and primes 17,97,113. Norms are computed by an exact 8-by-8 Bareiss determinant. Source values are small integers (moduli <=113); norm outputs are at most4096, with exact rational rounding comparisons. Intermediate integers and output size are bounded by these explicit finite loops.

Expected outcomes: PASS for all identities, exact distribution equalities, and divisibility/norm checks. Failures produce a complete Python assertion traceback and nonzero exit. These checks cannot prove an infinite theorem or certify the inherited C8 interface. They target only the stated structural failure modes.

Exact intended command, from project root:

```
/usr/bin/timeout --signal=TERM --kill-after=5s 120s python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/reviews/BLIND2/finite-checks.py
```

Execution is forbidden until root grants the experiment slot. The script starts by setting RLIMIT_AS to512MiB, creates no children, uses no network or solver, and writes only its standard output. The timeout terminates its process group; hard runtime budget120s with5s kill reserve, below all current deadlines. Complete stdout, stderr, exit status, wall time and max RSS will be preserved in this directory. No parameter will be changed after observing an outcome without a separately recorded preregistration.
