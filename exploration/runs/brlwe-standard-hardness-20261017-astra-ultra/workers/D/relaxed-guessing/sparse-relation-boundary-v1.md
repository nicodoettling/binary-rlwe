# Growing sparse relations: actual guessing and the standard-family boundary

D; after tool clock2026-10-17T21:50:36Z. PROVISIONAL new proof, requiring independent review. No second experiment. This follows the concrete r8 control and treats the coordinator's sparse-support alternative. It supplies a CP1-safe guessing argument, not a new hardness assumption disguised as a standard source.

## 1. Conditional Gaussian law for disjoint relations

Fix an integral ideal J in R=Z[X]/(X^n+1). Suppose v_1,...,v_M belong to J, have disjoint coefficient supports T_i, and every nonzero coefficient is+1 or-1. Let w_i=|T_i|<=w. Put L=sum_i Z v_i, an orthogonal rank-M sublattice of J. Let S be independent uniform binary and G~D_(J,t). The actual observation is Y=S+G.

For an upper bound only, disclose C=G mod L, a possibly infinite countable quotient. This disclosure is independent of S because G is independently sampled. Fix a coset C=g_C+L. Write c_i=<g_C,v_i>/w_i and g_perp for its orthogonal component. The EXACT conditional law is

    G | C = g_perp + sum_i Z_i v_i,
    Z_i independently distributed on c_i+Z,
    Pr[Z_i=z] proportional exp(-pi w_i z²/t²).

Orthogonality factorizes the actual Gaussian normalization on that coset. No claim is made that G has independent coefficient marginals before conditioning.

Given C, every coordinate outside the supports is decoded exactly. In block T_i, orthogonal projection to v_i reveals the binary block except for one pair: its positive and negative indicator vectors. They differ by v_i. Indeed a nonzero difference of two binary blocks parallel to v_i must equal+v_i or-v_i. These two secrets have prior probability2/2^w_i. In that pair, the optimal test compares a one-dimensional translated lattice Gaussian P_i and P_i+1. Therefore the EXACT conditional block guessing probability is

    1-2^(-w_i)(1-TV(P_i,P_i+1)).

Different blocks remain independent conditional on C, including both the secret and Gaussian variables. Optimal actual-secret guessing given(Y,C) thus factors into the product of these expressions. This is a justified conditional product, not a restored product of unconditional marginal success probabilities.

For a one-dimensional unimodal mass sequence, TV(P,P+1)=max_z P(z), by telescoping the positive and negative differences. Put tau_i=t/sqrt(w_i). Poisson summation gives uniformly in the translate c_i

    rho_tau_i(Z+c_i)>=tau_i(1-epsilon_i),
    epsilon_i=2 sum_(j>=1) exp(-pi tau_i² j²).

For tau_i>=1, epsilon_i<1/4. Hence max P_i<=4/(3tau_i). If t>=4sqrt(w), every TV is <=1/3, uniformly in the disclosed coset. Averaging over C yields the rigorous bound

    p_guess(S|S+G)
      <= p_guess(S|S+G,C)
      <= product_i [1-(2/3)2^(-w_i)]
      <= exp[-(2/3) M 2^(-w)].                         (S1)

The disclosure C need not be computable and is never part of the actual source or wrapper; it only increases the hypothetical adversary's power. For A-FRAC, apply this conditional on the fixed source state and the independent proof H. The required S/G independence survives those conditionings, exactly as in its original proof. This is the essential CP1 check.

## 2. One sparse ideal element gives enough disjoint rotations

If f belongs to J and has ternary coefficient support T of size w, all negacyclic rotations X^j f belong to J. Their supports are cyclic translates of T; signs at the wrap do not matter. A greedy disjoint packing picks at least n/|T-T| >= n/w² rotations, because each selected shift conflicts with at most|T-T|<=w² shifts. Applying(S1), for t>=4sqrt(w),

    p_guess(S|S+G) <= exp[-2n/(3 w² 2^w)].              (S2)

Thus w<=c log2 n for any fixed c<1 gives exp[-Omega(n^(1-c)/log²n)], a negligible actual-secret bound. It is not necessary to assume that the entire ideal lattice is a product. The coarse index bound may be vacuous while(S2) is strong.

## 3. An explicit growing-support family, and why it stays easy

Let F0=f8(X^(n/8)) be the verified r8 polynomial from fixed-block-theorem-proof-v1.md. For a power of two ell=2^a<n/8 put

    H_ell(X)=product_(j=0,...,a-1)(1+X^(2^j))
            =1+X+...+X^(ell-1),
    F=F0 H_ell, J=F R.

The8 blocks of ell consecutive coefficients do not overlap, so F has exactly w=8ell ternary coefficients. Choose ell to be a power of two within a factor2 below c log2(n)/8. Then w<=c log2 n, and(S2) proves negligible guessing at t>=4sqrt(w).

For d=2^j<n, N(1+X^d)=2^d in this power-two cyclotomic field. Hence

    N(F)=2176^(n/8) * 2^(ell-1) > 2^n.

The source is nevertheless easy: F is explicitly public, ||M_F||<=w, and for a~D_(J^-1,s), Fa is integral with each coefficient tail bounded at scale s sqrt(w). If gcd(N(F),q)=1, the comparator F A is exactly uniform. The coefficient-box test has planted acceptance >=1-2n exp(-pi U²) and comparator acceptance <=min(1,(2floor(s sqrt(w)U)+1)/q)^n. It distinguishes whenever s sqrt(w log n)<<q. The useful A-FRAC noise budget, with t at least this scale and sigma<<q, falls in that region. The short public multiplication basis also makes ordinary Gaussian sampling easy at its corresponding width.

Randomizing the positions in products of odd binomials does not automatically hide this easy ideal. Every1+X^a with odd a generates the same unique prime ideal above2, up to a unit. More generally a power-of-two valuation determines that binomial's ideal. Thus merely hiding such sparse factors can leave an explicit short associate of the product ideal. A purported hidden-generator source needs a genuine hardness argument for its exact public ideal law.

## 4. Hidden sparse generators and standard input families

If f is only guaranteed to exist and is not supplied, the public short-source test above is conditional on finding f. Enumerating all ternary vectors of weight<=w takes at most exp(O(w log n)) candidate membership tests. At w=O(log n) this is quasipolynomial, not polynomial; failed polynomial attacks do not establish security. A distribution of HNF ideals generated by a hidden sparse polynomial would be a NEW sparse-principal-ideal premise unless a reduction to that exact law is proved. Principal ideals also occupy only the principal class, so arbitrary-class standard input is not imported by syntax.

There is a stronger exact norm obstruction for ANY ideal containing such a relation. If0!=f belongs to J then (f) is contained in J, so

    D=N(J) <= |N(f)| <= ||f||_coef^n = w^(n/2).        (S3)

The second inequality is AM-GM over canonical embeddings. For w=O(log n), D is at most exp(O(n log log n)). Therefore standard ideals of larger norm cannot themselves contain the required sparse ternary relations. In particular the cited FPSW prime norms p>=n^(2n) exclude every ternary vector, even dense ones; already D>n^(n/2) makes the binary quotient map injective. These are exact containment obstructions, not statistical guesses.

This enlarges the permissible norm bound beyond exp(O(n)) but still does not normalize arbitrary ideal classes. Conditionally on the coordinator's separately frozen class-number premise h_K>=exp((1/4+o(1))n log n), the elementary count

    # integral ideals of norm<=w^(n/2)
      <= w^n zeta(2)^n = exp(O(n log log n))

shows that only a vanishing exp(-(1/4+o(1))n log n) fraction of classes can contain any such sparse-relation ideal. The class-number premise remains owned/reviewed separately in coordinator/same-class-count-{theorem,proof}-v1.md. This application concerns SAME-CLASS normalization only. It is no barrier to an actual class-changing, dimension-changing or oracle-assisted reduction.

## 5. Frontier disposition

Refined actual-secret lossiness really does extend above D=2^n; the fixed and growing concrete families establish this. The explicit examples have public short-source attacks. Hiding an arbitrary sparse generator could remove that particular polynomial attack, but introduces a new distribution-specific hardness premise, retains a quasipolynomial enumeration attack, and cannot cover high-norm standard families directly. No standard-family intersection has been enlarged by a verified reduction.

A mathematically different next test would need dense overlapping ternary relations with a directly proved conditional guessing law at much larger norm, or an actual class-changing/source simulator that creates the required sparse relations while preserving both endpoints. Simply weakening the numerical D cutoff, repeating one full-support relation, or calling a sparse-principal family standard does not supply that step. No further experiment or security conclusion is claimed.
