# Public information extension of FF3-COMPRESSED-SELECTOR-INFORMATION-v1

PROVISIONAL. Let Z be public side information independent of the uniform N-valued secret S. Permit the proposal mu_Z, the class map and G to depend on Z, subject to the theorem's pointwise normalization and uniform bounds M,L for every positive-mass z. Permit the output to depend only on(Z,accepted E,accepted C) and fresh coins.

Conditioning on Z=z preserves the uniform secret prior. The accepted-law proof applies with mu_z, so the conditional optimal guessing probability is at most ML/N for every z. Averaging preserves that bound. Thus retaining full public A, independent of S in the promised source experiment, does not by itself evade the compressed-class obstruction. An algorithm must retain additional input-correlated response/residual information outside the polynomial class, or violate another stated hypothesis.

If Z is correlated with S, the correct general bound is

 P_guess(S|Y,Z) <= M L * E_Z[max_s Pr(S=s|Z)].

The expectation is the prior optimal guessing probability after the supplied advice. It may be much larger than1/N. The actual secret known in an external completion wrapper cannot be inserted as a free Z inside a recovery bound. For Z=S this bound becomes vacuous, as it must. For randomized public sources, the conditioning includes their entire physically retained transcript; hidden input-correlated random state is not treated as fresh output randomness.

No new probability product is used: each z applies the existing pointwise conditional accepted-law calculation. The Gaussian target corollary still depends on corrected ENUM proof-v2 and its pending fresh review.
