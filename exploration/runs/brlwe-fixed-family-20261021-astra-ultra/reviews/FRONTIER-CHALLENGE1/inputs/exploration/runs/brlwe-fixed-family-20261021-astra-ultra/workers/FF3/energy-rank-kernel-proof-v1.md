# Proof of FF3-ENERGY-RANK-v1

Fix source class size M and target class size N. For uniform source rank r in[0,M), independent uniform T in[0,N), the integer K=Nr+T is uniform on{0,...,MN-1}. Every j in[0,N) is the quotient floor(K/M) for exactly M values of K. Therefore j is uniform on[0,N). For each fixed input r the formula also defines an ordinary normalized row, because T is sampled from a finite nonempty set.

Both U and P are uniform conditional on a source energy class. For every(e,f), the preceding calculation makes the output rank uniform conditional on e,f. The class transition h maps the U class masses to beta and the P class masses to n. Summing these exact conditional laws gives V and N on the full coefficient vectors. In particular the independent target Gaussian coefficient law is recovered because N is that stated full product law; it is not inferred from energy moments. Source rank permutations preserve conditional uniformity and therefore both endpoints.

For the pair extension, conditional on a joint energy class, each relevant product endpoint has uniform pair rank in a set of size M_e0*M_e1. Apply the same integer argument to this one rank. If other input laws are not uniform in that joint class, this argument does not determine their pushforward. They must be tested or proved separately, as required for a full binary cube.

For exact dynamic programming, define C_0(0)=1 and C_0(t)=0 otherwise. For ell>=1,

                       C_ell(t)=sum_(a in I) C_(ell-1)(t-a^2).

This counts all length-ell coefficient vectors of energy t. There are O(n*B^2) possible energies at each layer when |a|<=B, hence O(n^2*B^2*Q) integer additions suffice for the full source table. Counts are at most Q^n, so their bit lengths are O(n log Q). Target counts are analogous. Rank a vector by scanning coordinates in lexicographic order and adding counts of all lexicographically earlier choices with the required remaining energy. Unranking reverses this process. Both use polynomially many exact count operations. Uniform integers in[0,N_f) can be sampled by binary rejection in expected fewer than2trials, with O(log N_f) bits per trial; the fact that N_f may be exponential as a number does not make its representation or uniform sampling exponential.

For a rational h row, clear its denominators and sample a uniform integer over their sum; its common denominator has polynomial bit length when the number and sizes of the entries are polynomial. Approximate class sampling propagates through the fixed rank channel by TV contraction, pointwise in every input x.

Finally let E be an integer discrete-Gaussian coefficient and let E' have its distribution conditioned on the centered interval. Their total variation is exactly Pr[E outside that interval]. A maximal coupling, followed by reduction modulo the modulus, costs no more than that amount. Applying a union bound over coefficients gives the stated vector costs. Applying H contracts input TV, and the analogous output comparison adds its cost by the triangle inequality. Fresh independent H calls conditional on a fixed secret can be composed by a union bound; no posterior multiplication is asserted.

The full input rank is physically available to this H and may correlate strongly with the unknown secret when the residual comes from a wrong candidate edge. It is explicitly part of the algorithm's retained state. This is why FF3-COMPRESSED-SELECTOR-INFORMATION does not prohibit the construction, while also why the two-secret endpoint proof cannot automatically be applied to a selected wrong edge.
