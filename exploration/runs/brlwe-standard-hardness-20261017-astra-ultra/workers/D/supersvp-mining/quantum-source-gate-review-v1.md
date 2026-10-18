# Independent review of C quantum source gate v1

PROVISIONAL nonblind review; coordinator alone accepts claims. Frozen 2026-10-17T21:25Z. No numerical experiment. Author input: workers/C/supersvp-mining/quantum-source-gate-v1.md, freshly verified SHA256 2c4e66dc7bffb01be09c1de5218c4b7f266709745e966bcbd052beadd0d76f25. Dependencies retain their individual scopes: A fractional composition, B Gaussian-periodic v2 / elliptical sampler v2, C OHCP v5. No acceptance transfers from this review to those dependencies.

Verdict: the coefficient-dual and width conversion, promise-domain use, and bounded-error coherent implementation survive this audit. Read the output distribution as APPROXIMATE, with the full primary state/truncation approximation and finite precision charged. This produces a conditional same-ideal quantum consequence, not a standard hardness foundation.

## Primary import and exactness qualification

I read Regev's original Lemma 3.14 and its proof, printed pp26–28 of [On Lattices, Learning with Errors, Random Linear Codes, and Cryptography](https://cims.nyu.edu/~regev/papers/qcrypto.pdf). It targets width sqrt(n)/(sqrt(2)d) and constructs a distribution exponentially close to that target. Before the decoder call, the proof compares with a reference state supported on offsets of norm below d; arbitrary behavior outside that promise therefore contributes only the reference-state approximation error. LPR's author-hosted [ideal-LWE paper](https://cims.nyu.edu/~regev/papers/ideal-lwe.pdf), printed p22 after Lemma 4.2, explicitly permits negligible failure over decoder inputs and internal randomness. BRST Lemma 3.4 supplies the same width convention. The imported approximation is not merely an arithmetic-rounding error.

## Independent coordinate calculation

For the power-of-two coefficient inner product, <x,y>_coef=Tr(x conjugate(y))/n and R^vee=R/n. Thus I^*_coef=conjugate(I)^(-1), and M=conjugate(J)/q has M*=qJ^(-1). This uses a rational coefficient basis and avoids claiming that an arbitrary canonical-coordinate finite grid has rational coefficient coordinates.

For any nonzero x in J^(-1), xJ is a nonzero integral ideal. Consequently |N(x)| D is a positive integer, so |N(x)|>=1/D. Parseval followed by AM-GM gives ||x||_coef^2=(1/n) sum_i |sigma_i(x)|^2 >= |N(x)|^(2/n). Hence lambda_1(qJ^(-1))>=q/D^(1/n).

Also ||sigma(e)||_infinity<=sqrt(n)||e||_coef. C's canonical-infinity promise d0 therefore supplies the coefficient-Euclidean radius d=d0/sqrt(n). Its stricter hypothesis d0<q/(4D^(1/n)) ensures d<lambda_1(M*)/2. Applying the imported ideal target width and multiplying by q followed by orthogonal conjugation gives exactly the TARGET parameter s_J=nq/(sqrt(2)d0) on J. These deterministic transformations do not increase statistical error.

## Coherent correctness, including the domain restriction

Let U implement the bounded classical decoder reversibly with its random seed/workspace retained. On a fixed promised input x, separate its coin state into good and bad outcomes; the bad part has squared norm at most eta. Compute/copy/uncompute differs from the ideal deterministic answer operation by at most 2 sqrt(eta), since the two operations agree on the good part and have norm at most one each on the bad part. The input register remains intact. Errors for different x therefore occupy orthogonal input subspaces, yielding the same bound on arbitrary superpositions SUPPORTED ON PROMISED INPUTS, including ancillary entanglement.

This is not an operator-norm guarantee on all inputs. The primary proof's promised reference state is what permits its use: compare with that state before the oracle call, use unitarity to carry its approximation error, then use the bound just proved. In a repeated-use implementation with Q_D such calls, the charge is at most 2 Q_D sqrt(eta), plus all primary reference-state/preparation/truncation/QFT errors. Thus a safe explicit endpoint is

    TV(actual output, D_(J,s_J)) <= delta_prim + 2 Q_D sqrt(eta),

where delta_prim bounds the accumulated primary errors in trace distance (or an upper bounding state norm). No exact discrete-Gaussian sampler is established. The phrase “outputs D” in the composition note must be read as this target-law shorthand, not a zero-loss identity.

C5 has pointwise correctness for every promised rational target and bounded runtime on every input, as required. A merely averaged BDD guarantee, a classical remote-only oracle, or an input-dependent unbounded runtime would not justify this step. Given an actual algorithm circuit, fresh classical random tapes can be prepared coherently and all bounded fallbacks included. Full input encoding lengths and scalar-evaluation costs remain charged as in C5. The rational-grid query lengths used by the primary algorithm are polynomial in the lattice description; exponentially fine grids have polynomial logarithmic precision.

With eta=(n/2)exp(-kappa)+zeta and zeta=exp(-kappa/2), take kappa growing faster than log n (for example a polynomial confidence choice), rather than interpreting the minimum kappa>=2log(8n) alone as negligible error. For polynomial Q_D the decoder error is then negligible. Choosing confidence also changes a,d0 and the output width; those changes must remain in the parameter ledger.

## Output and source scope

Substitution of d0=delta w_B/(64nka) yields R_out=s_J sqrt(n)=(64/sqrt(2)) n^(5/2)kaq/(delta w_B), as stated. Uniqueness implies s_J>2sqrt(2)nD^(1/n), so the previously proved ideal smoothing and Gaussian mass/tail controls apply. Their failure probabilities must be added to the approximate-sampler error when asserting a nonzero vector of norm at most R_out.

The construction begins with BDD on qJ^(-1) and ends on the same J. For an average-family distinguisher it applies only to the corresponding good ideals with the required same-J advantage; it does not promote that average to pointwise advantage on all ideals. A low-index family and a modulus q0>R_out can make the resulting restricted short-vector task nontrivial, but neither class coverage nor hardness follows. No binary-secret conversion is supplied by this quantum step.

## Scope dispositions

- Coordinate/dual factor and output width: survives.
- Pointwise randomized decoder to coherent promised use: survives with explicit error charge.
- Arbitrary outside-promise behavior: covered by the primary promised reference state, not by a universal per-input bound.
- Literal exact output Gaussian: not proved; retain the displayed approximate endpoint.
- Same-family restricted consequence: conditional only.
- Standard ideal-family or original binary foundation: OPEN.
