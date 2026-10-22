# FF3-SELECTOR-PUBLIC-v3

Use the finite proposal/class/output setting and pointwise normalized selector of FF3-COMPRESSED-SELECTOR-INFORMATION-v2. Let Z be a finite or countable DISCRETE public random variable. At every atom z with Pr(Z=z)>0, permit proposal mu_z, class map and selector weights G_z to depend on z, but require the base theorem's normalization for every possible input x conditional on z and the same bounds M,L. The output depends only on(Z,accepted E,accepted C) and independent fresh coins; input-dependent hidden state is not an allowed additional output input.

For any joint prior on an N-valued secret S and this Z, the conditional accepted channel satisfies

    P_guess(S | output,Z) <= M L E_Z[max_s Pr(S=s|Z)].

In particular, if S is uniform and independent of Z, the upper bound is ML/N. The conclusion permits arbitrary dependence of the underlying input on(S,Z), provided the stated conditional pointwise normalization and output factorization hold. It includes finite public multipliers independent of S in a promised experiment. It does not apply to an unrestricted nonatomic Z, a nonnormalized rejection rule, uncharged secret-dependent advice, or output retaining additional response/residual state outside the displayed factors.

If the class is randomized, each retry uses a fresh draw from its declared conditional kernel R_z(.|x,e), as in the base v2 algorithm; no persistent hidden class seed is allowed.
