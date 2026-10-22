# FF2 affine symmetry amplification: exact scope and remaining escape

Exploratory author argument, not accepted and not a general amplification impossibility.

The exact binary-secret experiment has a useful family of public symmetries. Let U be a signed permutation of the coefficient basis that normalizes the multiplication algebra: U M_a U^-1=M_phi(a) for every a in R. Suppose phi is the induced unital ring automorphism. Then U(f)=v*phi(f), where v=U(1) is a signed monomial. Also U(X) is a signed monomial, so phi(X)=U(X)/v is a signed monomial. Because phi(X) has order2n and n is a power of two, it is X^k for an odd k modulo2n. Consequently

    U(f)=v*phi_k(f), v in{+/-X^j:0<=j<n}, k odd modulo2n.

There are at most2n^2 such transformations. Conversely all of them are signed coefficient permutations and normalize the multiplication algebra. This class includes the usual Galois maps and negacyclic shifts.

For each U there is a unique coefficient translation c_U that maps U{0,1}^n back onto{0,1}^n: c_U has coefficient1 at rows where U has negative sign and0 elsewhere. The transformed secret S'=U(S)+c_U is uniform binary. Given a raw sample B=A*S+E, set

    A'=phi_k(A)/v,
    B'=phi_k(B)+A'*c_U.

Then B'=A'*S'+phi_k(E); public A' is uniform and the coefficient discrete-Gaussian error is unchanged in law. Fresh samples preserve one shared transformed secret. Repeated use remains in the same finite affine group because c_(UV)=U*c_V+c_U.

Therefore a secret orbit under this exact class has at most2n^2 elements. Any distribution obtained from a fixed secret by these transformations has TV distance at least1-2n^2/2^n from uniform binary secrets (when the bound is positive). Repeating transformations or fresh decision coins does not make this orbit uniform over the whole cube. This is a support argument, not a statement about the efficiency or existence of a distinguisher whose good-secret set avoids a particular orbit.

The normalizer hypothesis matters. The argument does not classify arbitrary nonlinear transformations, input-dependent stochastic kernels, non-conjugacy sample maps, or code-dependent amplification that generates genuinely fresh shared-secret experiments. It does not assume that every exact Gaussian-preserving sample transformation has the displayed linear form. Those are separate possible escape routes.

Another exact positive route is a divisible auxiliary modulus Q with q dividing Q: reduction (A,B) modulo q preserves every shared secret and the exact same coefficient Gaussian errors, and sends independent uniform public multipliers/comparator to their q endpoints. However a distinguisher used through this projection only depends on the q component. Averaging over additional prime factors of Q does not by itself make its selected information depend on those distinct primes. The inherited common-partition norm-divisor bound cannot simply be reused. This separates the exact transfer edge from the unresolved source comparison rather than declaring the route impossible.
