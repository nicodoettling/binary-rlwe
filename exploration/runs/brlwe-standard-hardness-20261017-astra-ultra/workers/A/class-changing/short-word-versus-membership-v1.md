# Short class words exist; the checked membership primitives do not find them

2026-10-17 22:03 UTC. PROVISIONAL scoped continuation after the C8 review. No experiment. This records the coordinator's distinction, not a general impossibility theorem.

## 1. The improved mixing length is real

Let H=Cl(K), h=|H|, K=Q(zeta_(2n)), and B=2^(rho n). Jao–Miller–Venkatesan Theorem 1.1 gives, under GRH, degree 2li(B)+O(n sqrt(B) log(B Delta)) and nontrivial eigenvalues O(n sqrt(B) log(B Delta)) for the multiset of prime-ideal classes of prime norm <=B and their inverses. The constants in these two estimates are absolute. Thus, since Delta=n^n, the normalized eigenvalue bound is

    theta = O(n log(B) log(B Delta)/sqrt(B))
          = exp[-(rho log(2)/2)n+O(log n)].

This uses the explicit degree-dependent estimate, not the paper's corollary with degree fixed. [Primary theorem](https://web.williams.edu/Mathematics/sjmiller/public_html/crypto/handouts/JaoMillerVenkatesan_ExpanderGraphsGRHEllCurveCrypto.pdf), printed page 3. Removing the at most 2n directed steps over the fixed split target prime q changes the normalized estimate by only O(n log B/B), so coprimality does not change this asymptotic conclusion.

Here is the inference relevant to this run. Fourier expansion of the r-step transition law mu_r gives

    |mu_r(g)-1/h| <= theta^r.

Therefore r>=log(2h)/log(1/theta) gives EVERY g probability between 1/(2h) and 3/(2h). The elementary bound log h=O(n log n) then gives r=O(log n). One way to see that class-number bound is to combine a Minkowski representative of norm <=sqrt(Delta) with the count of such ideals <=Delta*zeta_K(2)<=Delta*zeta(2)^n. This is indeed a short signed word in eligible primes for every target class. It improves the word-existence scale relevant to the saturated-join packet.

## 2. The endpoint law retains the target-search cost

Even granting an efficient exact fresh-neighbor sampler, testing a random r-step word for one PRESCRIBED class succeeds with probability mu_r(g), of order 1/h. Repeating independent complete walks has this full success/failure law; the short word length does not make the endpoint probability constant. Conditional on success, the word law is the original word law restricted to the fiber with endpoint g, divided by mu_r(g). Its normalizer cannot be dropped.

An exact finite control is H=Z/5Z with one-step distribution already uniform. Every target has a length-one representation, and membership/equality is trivial. A fresh sampled word still hits the fixed target with probability exactly 1/5; after t independent samples success is 1-(4/5)^t. More generally a uniform sampler on H has fixed-target mass exactly 1/h, regardless of how short its represented words are. This control refutes the sampling inference only; it does not rule out exploiting the group presentation directly.

Quantum amplitude amplification of this particular coherent sampling-and-test procedure would change its search dependence to order sqrt(h), assuming its coherent implementation and inverses are actually available. It does not turn the displayed procedure into polynomial time in log h. This is not a lower bound against all quantum class-group algorithms.

## 3. Exact membership and short membership are different outputs

Biasse–Song's detailed 2025 version, Section 8.4 and Proposition 9, supplies exponents and compact principal generators by S-unit computations and integer linear algebra under GRH. It does not impose an O(log n) word length or bounded weighted exponent sum. Algorithm 7 has the editorial output-label defects already recorded in C's packet; the algebraic interface, rather than that label, is used here. [Primary source](https://arxiv.org/pdf/2510.02280), printed pages 31–32.

CDW explicitly separates group representation from short representation: after finding an exponent vector alpha, shortening requires finding a nearby point in the relation lattice ker(phi). Their arbitrary-ideal route additionally uses a walk into the relative class group with expected h^+ dependence and a separate factor-base assumption. Faster mixing of the walk does not change that subgroup's proportion 1/h^+. [Primary source](https://ir.cwi.nl/pub/30736/30736.pdf), printed pages 4–5 and 22–24. These are statements about the checked primitives, not a claim that no future short-word algorithm can exist.

The bound B=exp(rho n) also does not permit explicitly listing the whole generating multiset in polynomial time. Replacing it with a polynomial number of sampled generators preserves no automatic short-word guarantee. A quantum group decomposition can find coordinates relative to a supplied finite list, but the coordinate magnitudes may remain large. Knowing the abstract class-group invariant factors does not invert the map from short words of prime ideals to a prescribed class.

## 4. Consequence for the actual oracle reduction

If an algorithm found the O(log n) eligible word, the saturated-join contract would give a quasipolynomial JOIN loss from polynomial per-leaf normalized bounds. Principal-generator balance remains a distinct archimedean factor; the checked general balancing result still only gives the previously recorded exp(tilde O(sqrt(n))) guarantee. Neither factor is supplied by uniform endpoint coverage alone.

The present low-index DGS oracle acts on an explicitly chosen eligible ideal and supplies no short-relation preimage oracle for a prescribed class. Applying it to the relation lattice is not an automatic substitution: the Galois relation ring and the low-index power-two ring have different allowed quotients, as preserved by class-relation-ideal-query-test-v1.md and its exact 5-torsion control. Thus the checked membership algorithms do not close the family-transfer edge. The remaining constructive need is an actual short-word/preimage algorithm or a direct controlled geometric transfer using the eligible DGS oracle. Standard arbitrary-ideal hardness remains OPEN.
