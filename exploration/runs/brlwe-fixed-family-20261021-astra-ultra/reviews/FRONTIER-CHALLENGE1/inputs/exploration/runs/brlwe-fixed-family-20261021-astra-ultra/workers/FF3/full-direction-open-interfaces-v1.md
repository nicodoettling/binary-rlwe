# Full-direction frontier and untested symmetry extension

PROVISIONAL analytic interfaces, not an FF theorem. These remain open when this constructive worker completes; completion of the worker is not programme exhaustion.

## Legal ring-equivariant affine symmetrization

Let n be a power of two, let sigma be X->X^k for odd k modulo2n, and let T=X^j. The integer coefficient map L=T*sigma is a signed permutation. Let v have coefficient1 exactly at the negative-sign output positions of L. Then g(s)=L(s)+v is a bijection of the coefficient-binary cube, independently of the modulus.

For a source sample(a,b), the computable transformation

 a'=sigma(a)*T^-1,
 b'=sigma(b)+a'*v

sends a planted sample with secret s to one with secret g(s). The error is sigma(e), so symmetric independent coefficient Gaussian errors (and the finite rational symmetric errors used here) retain their exact law. Uniform public multipliers and the independent uniform comparator are preserved. No secret is supplied to this transform.

For a target output(c',d'), the inverse transformation

 c=sigma^-1(c'*T),
 d=sigma^-1(d'-c'*v)

sends secret g(s) back to s, preserving the stated target noise law and comparator. These formulas use actual ring automorphisms and monomial units; they do not import independent column signs.

Thus a per-sample kernel K can be symmetrized by sampling a transform g, applying the source transform, K, and the target inverse. Its fixed-s endpoint is exactly

 (1/|G|) sum_g F_g,out^-1 [K(P_(g(s)))].

The group has at most2n^2 signed-monomial/automorphism maps, and an online transform has polynomial cost. Requiring this explicit average to equal T_s gives a new linear endpoint system for a fixed parametric K. It may cancel errors between orbit members; this has NOT been proved for the joint-rank tables, and no experiment was run. A uniform group average is a different candidate, not an assertion that every original kernel is improved.

For an eventual batch, draw fresh symmetrization coins for each source sample and first condition on the one original secret s. Then exact averaged per-sample endpoints compose by literal conditional independence. One shared group element across the batch would generally give a mixture of products; one-sample average correctness would not justify replacing it by the product of averages. This is an explicit CP-1-style regression obligation for any extension.

## Remaining construction obligations

1. For full-direction joint rank transport, establish exact feasible tables for the intended growing-degree Gaussian family, with polynomial bit complexity and construction cost. n2 finite positives do not provide that family. A particular forward lexicographic n4 model and its solver statuses do not rule out all rank couplings.
2. Test the legal affine symmetrization above against the complete n4 fixed-secret/comparator system, using exact certificates. No result is asserted here.
3. Explore ring-compatible alternative rank orderings or couplings that preserve the two noise/uniform normalizers while retaining sufficient input information. Energy-class size alone is not enough: the output must actually carry full rank information to escape the compressed-selector guessing theorem.
4. Supply a bounded finite-precision Gaussian sampler for the real energy/noise class table, with per-input error and whole-batch accounting. Integer shell DP and rank transport are exact; this does not silently certify the real table sampler.
5. If using a homomorphic modulus Q divisible by target q, separately rebuild the selected-information/source bridge. Exact coefficient reduction modulo q preserves the corresponding planted/comparator laws when the source noise projects to the target noise, but the old auxiliary-prime averaging does not follow merely because Q contains new prime factors.

The completed wave has not produced a PPT full-binary-cube Gaussian kernel or an alternate source extraction theorem. No claim of general modulus-transfer impossibility or scientific exhaustion is made.
