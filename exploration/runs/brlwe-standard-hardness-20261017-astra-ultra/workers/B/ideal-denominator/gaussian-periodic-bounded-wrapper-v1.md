# B-IDEN-GP-BND v1 — strictly bounded wrapper for GP v2

Status: PROVISIONAL corollary; not accepted. Dependency is the exact expected-time gaussian-periodic-theorem-v2.md and proof-v2.md, with the exact-ceiling complexity addendum. The optional v3 kernel is NOT used here.

Use all v2 hypotheses and its loss

  Delta=2k epsilon/(1-epsilon)+2pi kn/(Pr)+kn nu.

Let0<eta<=1/4 be a supplied rational. Put K=ceil(log2(64/nu)), Lplus=40K ceil(log2(16/nu)),

  Umax=kn(1+Lplus),
  Bcap=ceil(log2(Umax/eta)).

The complete v2 reduction uses at most kn uniform invariant-factor draws for its k coset choices and at most kn Lplus uniform interval draws inside the scalar rejection samplers. Any trivial factor of size one can be output deterministically. The actual scalar trial cap remains the original L<=Lplus.

To sample a uniform integer in an interval of size M>=2, draw ceil(log2 M) fair bits, accept if the integer is below M, and otherwise retry. Replace this elementary loop by at most Bcap trials, returning a fixed valid value if they all fail. Keep every other v2 operation unchanged. This defines ONE fixed bounded randomized map, with caps depending only on the declared inputs/parameters, not on the planted/comparator world or on prior oracle answers.

For every input y, each draw rejects with probability less than1/2. Conditional on every earlier history, its capped and uncapped implementations couple until the cap is hit. A union bound over the deterministic Umax draw bound gives

  TV(K_bounded(y),K_v2(y))<=Umax 2^-Bcap<=eta.

This is an input-uniform bound, including arbitrary valid finite-grid representatives. It does not multiply posterior marginal success probabilities. No exact uniform sampler on a general odd-order quotient is claimed to use a fixed finite number of fair bits.

The BOTH endpoint conclusions are therefore

  bounded planted: TV from FG planted <=Delta+eta;
  bounded comparator: TV from FG comparator <=eta.

In particular, an FG distinguisher of advantage delta_F gives a bounded GP distinguisher of advantage at least delta_F-Delta-2eta. Exact comparator equality belongs to uncapped v2; the bounded wrapper's comparator is approximate. This charge cannot be omitted even though the scalar fallback remains integer-translation equivariant, because capped quotient sampling need not be exactly uniform.

The wrapper makes k input-sample uses and one call to the FG distinguisher. If that distinguisher has a declared worst-case polynomial runtime on all valid inputs, the composite has a strict polynomial runtime in n,k and the COMPLETE binary encodings of the ideal, finite samples and all parameters, including eta. Bcap is polynomial in those lengths. HNF/SNF and rational arithmetic are deterministic polynomial operations; dyadic Bernoulli coins have fixed length; scalar trials and elementary uniform trials are now bounded. Conditional sampling of Gen is unnecessary because J is supplied.

For adaptive invocation by another reduction, this fixed bounded map is the distinguisher whose exact acceptance probability defines the oracle. Its Delta+2eta advantage charge is paid ONCE when establishing that distinguisher's source gap; it is not a per-query approximation to an ideal oracle. Any additional numerical approximation made by the outer reduction is separately charged through its own transcript budget.
