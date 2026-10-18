# RT2 source, parameter, and bit-complexity review v1

Scope: the same frozen inputs as `full-review-v1.md`, with hashes in `input-manifest-v1.json`. No external retrieval, BT20 report, or blind output was used. Standard Minkowski, Poisson, power-two arithmetic, and elementary probability were reconstructed in the full review. No unprovided source theorem has been treated as established. This is a nonauthor report, not coordinator acceptance.

## 1. What the source interface actually supplies

ROOT-SAMEJ is treated solely as a conditional interface providing a finite implemented sample on the same supplied eligible J, with the promised full-law TV error eta relative to D_(J,W). It is not an oracle on arbitrary ideals. The source must be valid in dimension m, on this supplied J, with its actual modulus/width/error schedule, and with fresh binary secrets where an upstream recovery wrapper requires them. Ordinary ideal bases are input, not free short bases or short-vector advice.

The weighted theorem itself assumes this sampling interface and an additional algorithm producing the short complementary multiplier. It does not derive either from a recovery success probability. Consequently, there is no numerical recovery advantage or advantage-to-TV formula in the allowed theorem input to verify. Root's product text mentions at most 2 sum_j Qstar_j coherent recovery executions, but Qstar_j and the finite recovery/sampler construction are not defined in the provided specification. That expression remains a conditional external accounting symbol; this review neither validates its numerical cost nor invents a source schedule for it.

Likewise, no standard worst-case ideal-SVP/ideal-DGS theorem is imported here, and no search-to-decision or decision-to-recovery step is supplied. The review does not silently add one. The exact law/advantage obligations for an eventual upstream reduction include its success definition, uniformity in J and m, common admissible modulus where needed, width in value, conditional TV composition, fresh randomness, full setup/circuit cost, and finite execution/output bounds.

## 2. The complementary multiplier is additional algorithmic power

The exact module is C=IS J^(-1), of norm M^t/D. Its ordinary basis and membership predicates can be computed by exact rational/integer lattice arithmetic. This does not compute a vector satisfying

    0<||a||<=C0 sqrt(m) A/D^(1/m).

Minkowski gives existential C0=1. A polynomial factor C0 still requires a polynomial-approximation short-vector procedure in the generally ineligible complementary ideal. No such procedure is given. Advice containing a suitable a would change the computational model and must be charged as advice, not relabeled ordinary input preprocessing.

The scale obstruction is exact. Since D^(1/m)<=2^rho,

    N(C)^(1/m)=A/D^(1/m)>=A/2^rho.

When A>2^(2rho), C exceeds the source's eligible norm cap. The same-J oracle cannot be applied to C under its current promise. Splitting C into new eligible ideals and multiplying independently sampled outputs reintroduces the product method and its certificate growth; it does not obtain the short multiplier for free. This is a statement about the specified source and certificate, not an impossibility theorem for all stronger sources or constructions.

Taking an obvious multiplier such as a small rational p can work for easy families, but p already belongs to a prime ideal over p. Such examples do not establish a hard family or an arbitrary-input complementary short-vector algorithm. Merely observing that a's desired norm has polynomial value in a family does not make it computable in polynomial time.

## 3. Finite postprocessing and actual encoded sizes

In Claim 3, C is integral, so a and valid X have integer coefficient vectors. Let b_a and b_X bound their coefficient bit lengths. Direct negacyclic multiplication uses O(m^2) integer products and additions. Each output coefficient has absolute value at most m times the product of the input coefficient maxima, so its bit length is at most b_a+b_X+ceil(log_2 m)+O(1). Selecting n coefficients for Pi is exact and requires no division by t. Thus this postprocessing has polynomial bit cost in m,b_a,b_X.

Given an ordinary basis matrix B_J, checking X in J amounts to solving B_J u=X exactly over the rationals and testing u integral, or using an integer normal form. The same applies to I. Membership of a in C can be checked without ideal factorization by testing Pi(a b_j) in I for every vector b_j in an ordinary J basis. By Claim 1 these m membership tests suffice. Ideal closure itself is checked by multiplying basis vectors by z. Exact determinants give the norm indices. These are finite polynomial-size linear algebra tasks in the encoded input sizes. Prime/divisibility assumptions are promises in the theorem; no omitted prime-factor search is smuggled into this postprocessing.

A basis of C may also be obtained from rational linear integrality constraints B_I^(-1) Pi M_(b_j) a in Z^n using integer normal forms, or standard ideal inversion/multiplication. These operations produce an ordinary basis, not a short one. Their bit costs depend on the actual supplied basis encodings.

An exact infinite Gaussian is a mathematical reference distribution, not a fixed finite implementation with bounded random tape and bounded output. A concrete finite sampler must specify its support or execution/output-bit bounds, numerical precision and truncation/rejection errors, and include those errors in the full-law eta budget. A sampler's large output representations cannot be omitted from runtime. An unbounded expected-time sampler needs its expected-versus-worst-case resource claim and any timeout failure to be stated explicitly.

Real parameters W and h in a mathematical probability statement do not themselves provide a finite encoding or access algorithm. A finite implementation needs encoded computable parameters or rigorously bounded rational substitutes. Testing an analytic radius with pi in it can use a conservatively rounded rational upper certificate; no exact comparison with an arbitrary uncomputable real is justified. This is standard implementation bookkeeping, not a gap in the real-valued probability theorem.

## 4. Parameter values, representations, and success

The approximation expression is

    B_a/A <= C0 sqrt(nm/(2pi h)) W/D^(1/m).

Since D>=1, polynomial **values** of m,W,C0,h^(-1) suffice for its polynomial growth. Polynomial bit length of W alone does not suffice: W=2^n has O(n) bits but produces an exponential factor. Similarly C0=2^n or h=2^(-n) has a compact encoding while ruining the polynomial certificate. The theorem explicitly avoids those substitutions.

Large A cancels in the normalized certificate, but the encoded I,J,a and all construction/source costs must still be polynomial for a polynomial-time statement in n. Arithmetic polynomial in input bit length does not automatically mean polynomial in n when the supplied basis encodings are larger. The coefficient bound on a gives an output-length bound once log A is controlled; it still gives no algorithm for finding a.

Let delta=1-eta-4sqrt(m)/W-h. The finite bound guarantees success at least max(0,delta). At the permitted floor W=4sqrt(m), the stated bound is vacuous for every positive h. A nonvacuous claim therefore requires eta+h<1 and W>4sqrt(m)/(1-eta-h). A **merely positive** delta can be exponentially small, so it is insufficient for a conventional polynomial-time solver obtained by repetition. Efficient amplification needs delta>=1/poly(n), or a stronger separately proved success bound, together with fresh conditional source guarantees for repeated executions.

For example, the purely conditional schedule W>=16sqrt(m), eta<=1/8, h=1/4 gives delta>=3/8 while retaining polynomial width whenever m is polynomial. This illustrates compatibility of the numerical inequalities; it does not prove that a given upstream source realizes that schedule. With per-attempt success delta and fresh conditional guarantees, O(delta^(-1) log(1/epsilon)) attempts give failure epsilon; all source/setup/recovery and multiplication costs must be included. Verification of nonzero ideal membership and a conservatively represented radius is finite.

For a randomized multiplier with failure probability beta, include beta in the error budget. Conditional sampling after a good multiplier must be justified pointwise; an unconditional marginal sample guarantee is insufficient. The frozen theorem requires this explicitly. If multiplier selection and fresh sampling are coupled, the new RT2-NC1 control shows the moment argument can fail even though every multiplier is nonzero and belongs to C.

## 5. Source-normalization and evidence boundaries

The full normalizer rho_W(J) includes zero and all tails. The covariance argument uses a ratio of translated and centered full theta functions. The subspace argument uses disjoint complete lattice lines; truncating the distribution destroys that proof's denominator comparison unless separately analyzed. TV controls a bounded event after the deterministic postprocessing, not the implemented source's unbounded second moment. The new finite contamination control makes this latter distinction explicit.

RT1's finite controls and RT2's new controls are exact rational laws on bounded supports. Their covariances and complete masses were checked directly; they are not substituted for full Gaussians, for a source's delivered width, or for computational hardness evidence. The root's source family and recovery model are conditional inputs, not conclusions supported by those small examples.

## 6. Dependency disposition

The conditional algebra/probability/certificate statements are PROVISIONAL with no mathematical defect found in this review. The independent report and exact finite controls support them, but final acceptance belongs to the coordinator after all gates close. The ordinary-basis arithmetic is justified at polynomial cost in encoded sizes. The existence-to-algorithm step for a remains BLOCKED; any arbitrary-ideal standard-hardness implication remains BLOCKED. Upstream sampler/recovery advantage, exact parameter compatibility, and uniform finite code/cost claims remain unverified unless their full source artifacts are supplied and checked. None is inferred from the conditional weighted theorem.
