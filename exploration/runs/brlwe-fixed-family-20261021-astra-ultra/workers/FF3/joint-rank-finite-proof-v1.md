# Proof/certificate audit for FF3-JOINT-RANK-FINITE-v1

Every table row is a probability distribution by the exact rational support certificate. For each fixed source residual pair and chosen target shell pair, the rank formula outputs a legal integer J in[0,N), sampled from a normalized finite distribution. The monomial v-u=X^i is a unit, so every target residual pair corresponds to exactly one(C,D). Hence every input row is normalized, before using any planted or comparator distribution.

FV16 constructs the complete source input space(81pairs), target output space(16pairs), all four binary secrets, and all four monomial cube edges, with exact negacyclic multiplication. For every source input, edge and target shell pair, it verifies that the integer rank-count probabilities sum exactly to the correct denominator N. The rank probability at a target pair of joint rank J is

 max(0,min(N-1,(J+1)M-1-NR)-max(0,JM-NR)+1)/N.

For a fixed secret s, its source input point numerator is14^(zero_count(B-As)) over denominator3^n*16^n. The target point probability is3^(zero_count(D-Cs))/8^n. Comparator point masses are1/3^(2n) and1/2^(2n). The code sums the exact source numerators times rank counts across every input and edge for each target point and table variable. Multiplication by the lcm of all target shell-pair sizes clears the remaining rank denominators. All resulting endpoint constraints are integer equations.

The numerical LP locates a47entry support only. Its weights are then solved over Q from the complete integer system. The code checks nonnegativity and every row equality using Fraction arithmetic. Therefore the finite theorem is based on exact integer/rational endpoint identities, not the floating solver status. Complete certificate, registration, code,stdout andresources are retained under experiments/ff3-joint-rank-fv16-* and joint-rank-n2-certificate-fv16.json.

These identities imply the full fixed-secret target law, including uniform C, independent target error, and the exact coefficient product law. No independence is asserted for the intermediate residual pair on a wrong candidate edge. The source is weighted directly in the endpoint sum, so there is no uncharged conditioning on selected edges or on a guessed secret.

For a batch, first condition on the same secret s. Source inputs and fresh edge/table/integer coins are independent across executions conditional on s. Each output has the exact fixed-s law proved above, so the joint output is its product. Mixing one common uniform s preserves the desired shared-secret law; it does not resample a new secret per sample. The comparator product follows separately. CP-1 is avoided because the only product identity is literal independence conditional on fixed s, not a product of marginal success bounds after posterior selection.

All numbers in this n2 instance have finite rational encodings. Rational table sampling and uniform integer sampling have exact expected finite implementations. This finite resource statement does not bound the construction, encoding, or feasibility of the analogous tables as n grows.
