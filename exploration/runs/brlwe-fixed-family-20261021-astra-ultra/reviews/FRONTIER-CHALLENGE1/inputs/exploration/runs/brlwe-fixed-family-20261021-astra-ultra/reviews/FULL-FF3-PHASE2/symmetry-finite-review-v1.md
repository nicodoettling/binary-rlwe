# Independent full review of SYM-RANK-FV1/FV2

Recommendation: PASS for the reconstructed exact finite model exclusions. No asymptotic or unrestricted FF exclusion is supported. Input code, arrays, registrations, resource reports and integer witnesses are frozen in input-manifest-addendum-v1.json. The reviewer did not import author/root code and did not run an optimizer. independent-certificate-check-v2.py rebuilt the systems from signed shift multiplication and exact probability numerators.

At n4, the legal group consists of sigma_k:X->X^k for odd k modulo8, and monomial multiplication T=X^j for j in0,...,7. The real coefficient matrix L=T sigma is a signed permutation. Let v_i=1 precisely in rows whose nonzero entry is-1. Then g(s)=Ls+v maps the binary cube bijectively to itself. For source input(a,b), the forward map is

    a'=sigma(a) T^-1,
    b'=sigma(b)+a'v.

Indeed b'=a'g(s)+sigma(e) when b=as+e. Signed coefficient permutations preserve the exact symmetric source rational coefficient law (7/8,1/16,1/16); sigma preserves multiplication, and the public map preserves uniformity. On target pairs(c',d'), the inverse is c=sigma^-1(c'T), d=sigma^-1(d'-c'v). Thus its error is sigma^-1(e'), whose Bernoulli target law modulo2 is preserved, and its public variable is uniform with the full required independence. The input and output maps are bijections, so the uniform comparator also transforms exactly. These are legal source and target conjugations, not arbitrary signed secret permutations without compensation.

The independently generated32 endpoint row permutations close under composition. Every row orbit has uniform multiplicity under the32 transforms. The fixed-secret target RHS is invariant under these row permutations, as is the comparator RHS. Averaging the conjugated kernel therefore gives one constraint per orbit, equivalently the SUM of the original endpoint equations within that orbit. There are178 endpoint orbits. The125 per-class normalizations remain explicit, so the reduced FV1 system has303rows and3125columns. The original n4 base system has4477rows and3125columns. Every coefficient and RHS entry of both saved systems matched the independent reconstruction.

The source point numerator for fixed s is14^(zero_count(b-as)) over3^4*16^4. The target point probability is3^(zero_count(d-cs))/8^4. Source and target comparator atoms are3^-8 and2^-8. For edge residual source pair class(z0,z1) with joint shell size M, pair rank R and target pair class size N, the probability of a particular target rank J is the integer length of

    [N R,N(R+1)) intersect [M J,M(J+1))

divided by N. Summing these lengths over each target class gives N for EVERY source input and edge. The independent checker used these half-open overlaps and integer grouped sums, not weighted floating bincounts. LCM scaling clears all rank denominators. This reconstructs the actual full fixed-secret/comparator matrices, rather than merely verifying a witness against untrusted saved arrays.

For FV2, eight branch ranks are R'=(direction*R+floor(quarter*M/4)) modM, direction in{1,-1},quarter in{0,1,2,3}. For each fixed class this is a permutation, including the reversal at M1 and other small M. The branch/class weights are nonnegative and their sum over all eight branches and target classes is1 for every source class. There is one combined125-row normalizer, not eight independent normalizers demanding total mass8. Each branch is then uniformly conjugated by the same legal32-element group. All eight303-by3125 blocks were rebuilt and compared in full. The resulting303-by25000 system matched the saved FV2 matrix and RHS exactly.

The integer Farkas verifications give:

| Model | min A^T z | b^T z |
| --- | ---: | ---: |
| original FV17 n4 forward pair rank |0|-35194066605710036481552480|
| SYM-RANK-FV1 uniform legal conjugation |0|-216559748042911765046919168|
| SYM-RANK-FV2 eight cyclic/reversed branch ranks and legal conjugation |0|-199649553351913799471971008|

All witness entries and all products were treated as arbitrary-precision integers. Nonnegative A^Tz and negative b^Tz exclude a nonnegative solution to Ah=b by direct multiplication. The independent FV13 broader joint-target-class model was separately rebuilt, with4650rows and3125columns, and has min A^Tz=0,b^Tz=-196771185659488205839872. Its constraints and meaning differ from the pair-rank model; neither exclusion is inferred solely from the other.

The successful verifier ran44.46s with479448KiB peak RSS under120s/2GiB. The initial v1 syntax/path failure occurred before computation and is preserved; it is neither a mathematical failure nor hidden evidence. The v2 correction was separately registered and root-authorized. Exact outputs, code hashes, resource measurements and cleanup are retained.

These results extend only the specified finite rational-law ansatz. They do not exhaust arbitrary input-dependent selector weights, arbitrary direction-sensitive couplings, other class maps, all rank permutations, other dimensions, Gaussian laws, or asymptotic uniformly effective tables. The original FV16 n4 UNKNOWN and FV17 primal solver ERROR remain their actual statuses; the independently exact dual establishes the finite infeasibility separately. One common secret is retained across a batch. Fresh group draws per sample give a product of averaged one-sample kernels conditional on that secret. Reusing one shared group element instead gives an average of products, and no equality with the product of averages follows. A shared fair bit yields pair TV1/2 from two fresh fair bits despite identical one-sample marginals.
