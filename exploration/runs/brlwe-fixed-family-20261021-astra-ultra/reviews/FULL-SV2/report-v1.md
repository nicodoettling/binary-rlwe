# FULL-SV2 exact source and complexity review

Reviewer disposition: **PASS at the exact deterministic source-classification scope** for SV-SYMDESC-v2 and SV-SUBFIELD-v2. No mathematical defect was found in the four reviewed v2 files. The unique definition `a=2^{v_2(e)}` repairs the recorded literal v1 failure. This is a nonauthor full review, not a blind review, programme-wide acceptance, or a hardness result. Coordinator reconciliation and the required fresh blind review remain separate gates. The exact file hashes, complete assignment, primary-source accesses, inherited regression dispositions, controls, failures, and seal are preserved in this directory.

## Frozen scope and dependency boundary

The reviewed field is Q[X]/(X^n+1), where n>=2 is a power of two, with the ordered coefficient basis 1,X,...,X^(n-1). R is its full integer ring; the ring, ramification, prime-transitivity, norm, and Frobenius inputs were checked in [Milne, Algebraic Number Theory, Propositions6.2/4.1/4.2, Theorem3.34, Example8.18](https://www.jmilne.org/math/CourseNotes/ANT.pdf). J is a nonzero integral ideal supplied by a nonsingular integer column basis A, with N(J)<=2^(rho n), fixed 0<=rho<1. Correctness is pointwise for every rational target T=lambda+w, lambda in J^-1, with the displayed canonical-infinity error bound. All algorithms are deterministic, use no oracle or sampler, and charge the complete basis, target, scalar and output encodings.

The symmetry algorithm computes the odd ideal J_o, its full Galois stabilizer H, the integral fixed lattice R^H, and its contraction index d_H. It obtains a nonzero f in J with coefficient norm <=2sqrt(n), in time polynomial in numeric d_H and complete input lengths. The subfield algorithm computes all standard power-of-two contraction indices d_g, chooses a minimum over d_g<2^g, obtains norm <=2sqrt(g_*), and has time polynomial in numeric d_* and complete input lengths. Its asymptotic polynomial family fixes rho,t,C before n, assumes at most t distinct odd prime-ideal factors and e<=n^C, and requires no such factorization or constants at execution time.

The source dependencies SV-BDD-CLASS-v1 and SV-FROB-PRIME-v1 were read in full. They do not require the repaired symmetry statement to establish their own multiplier, index-collision, and Frobenius assertions. The BLIND-SV1 report was read explicitly to assess the v1 repair; this reviewer is not blind. The old ambiguity is not silently retroactively accepted.

For the connection to DD, the exact FIXED-MAIN-v2 and AM-MAIN-v3 statements and acceptance-v1.json were read. All 23 theorem/proof/inherited-dependency hashes designated by that acceptance matched current bytes. The acceptance record explicitly makes its exact hashes authoritative despite stale PROVISIONAL banners in frozen author files. This review uses DD only to identify its represented radius and explicit guards; it does not reprove the accepted probabilistic reduction. The additional prime-list theorem is used only to substantiate the example's polynomial-value split characteristics. No inherited wide-DGS criterion is converted into BDD.

## Claim graph and local results

| ID | Obligation | Dependencies | Reviewer result |
|---|---|---|---|
| E | Exact additive exponent from ordinary basis | Integer linear algebra | Pass |
| O | Unique 2-primary removal and aJ_o subset J | E, cyclotomic ramification | Pass for v2 |
| C | Congruence index from rectangular Smith form | Exact integer normal forms | Pass |
| H | Effective stabilizer and saturated fixed lattice | Signed permutations, Galois theory | Pass |
| D | Odd invariant ideal descends; d_H^h=D_o | H, unramified valuations and prime transitivity | Pass |
| M | Collision gives an acquired small nonzero member | C/H, cardinality and disjoint supports | Pass |
| B | Pointwise multiplier decoder and bit bounds | M, Fourier orthogonality, field division | Pass |
| R | Exact DD radius satisfies both strict guards | Exact accepted DD formulas | Pass |
| F | Bounded-support subfield family | O/C, odd residue degrees, merged valuations | Pass |
| X | Exponential norm and trivial stabilizer are compatible | Odd prime over 3 and split prime construction | Pass asymptotically |

Changing E/O/C/H/D/M/B/R/F reopens the corresponding downstream statements. X is an example, not a premise of the finite algorithm. FF and source hardness do not occur in this graph.

## Ordinary input, exponent, and odd part

For any integer k>0, kR subset J holds exactly when kA^-1 is integral. The least such k is the lcm of the reduced denominators. Each denominator divides det(A), so e divides |det(A)|. The computation uses exact rational inversion and gcd/lcm, with polynomial bit bounds from determinant/cofactor estimates. In the specified upper-column HNF, its first column spans J intersect Q*1, so H11=e; each diagonal divides e by triangular back-substitution on eX^j. This also verifies the unchanged classification dependency's HNF assertion.

Write the 2-primary component of J as P_2^b. Since N(P_2)=2 and (2)=P_2^n, eligibility gives b<n and the quotient's 2-primary exponent is either 1 or 2. The exact v2 definition fixes a to that exponent and m=e/a. There is no remaining arbitrary factorization choice. At an odd prime P, v_P(mR)>=v_P(J); at P_2, m is a unit. Therefore valuations of J+mR give exactly J_o, and aJ_o is contained in both the 2-primary and odd components of J, hence in J. This works for J=R, a pure ramified ideal, a mixed ideal, and an odd prime power.

An HNF basis of the column span [A | mI] computes J_o. The calculation is not a factoring algorithm. Exact polynomial-time normal forms are an external algorithmic input; merely using an arbitrary implementation called HNF would not establish the bit bound. The [primary Kannan–Bachem abstract](https://epubs.siam.org/doi/abs/10.1137/0208040) explicitly asserts polynomial arithmetic and intermediate bit bounds, including transformation matrices. The theorem may use those algorithms. The finite SymPy test is only an implementation control, not evidence of that asymptotic theorem.

The old ambiguity is rejected by the saved n=8, J=(17,X-3), e=17 example. Choosing a=17,m=1 is no longer permitted. The legal values are a=1,m=17, so J_o=J, and the old false norm/radius calculation cannot arise. This is an actual definition repair, not a consequence deduced from m being odd.

## Congruence indices and stabilizer computation

Let V have the integral columns of either the fixed-lattice basis or the standard inclusion R_g into R. Choose a positive common denominator s for A_o^-1 V (or for A_o^-1 itself), and put C=sA_o^-1 V. Then Vz is in J_o iff Cz=0 mod s. For a Smith form UCV=diag(c_i), both unimodular matrices are invertible modulo s. The image of multiplication by c_i on Z/s has size s/gcd(s,c_i), so the exact image size, and hence the contraction index, is their product. Extra rows impose no new conditions after Smith diagonalization. Zero diagonal entries, if ever present, contribute 1; the actual inclusion has full rational column rank. No saturation factor is missing.

This proof applies to s=1, where all indices are 1. It also applies to a nonminimal common denominator; the formula must not depend on which s was selected. The output index divides the finite quotient order, so log d<=log D_o. Inversions, denominator clearing and normal forms therefore have polynomial encodings. The test checks the independent identity d=s^n/|det HNF([C|sI])|, including deliberately sheared ordinary input bases. Its initial library-domain failure and one-line explicit integer reconstruction are preserved, rather than deleted.

Every automorphism X->X^u is a signed permutation for odd u mod2n. Testing integrality of A_o^-1 P_u A_o proves containment. Equal covolumes then prove equality. Thus n exact tests recover H; this is polynomial in n and complete basis bits.

For the fixed lattice, each graph component of the signed permutation equations is either consistent and contributes one signed indicator, or has a negative cycle and forces every coefficient on that component to zero. The nonzero indicators have disjoint supports. Every invariant integral vector is a unique integral linear combination of them, so this is the full integral fixed lattice, not a sublattice of unknown index. Clearing denominators shows it spans the fixed field, hence its rank is n/|H|. This includes noncyclic stabilizers, for which all subgroup edges must be imposed. Constants ensure the fixed rank is never zero.

## Descent and acquisition by collisions

Let L be the H-fixed field. Integrality gives O_L=R intersect L=R^H. Every rational prime dividing J_o is odd, so its ramification index in K/Q is 1; multiplicativity in the tower forces relative ramification indices in K/L to be 1. Galois transitivity puts exactly the primes over a given L-prime into one H-orbit. H-stability of J_o gives a common exponent on that orbit. Assigning that exponent downstairs constructs I with IR=J_o and I=J_o intersect O_L. Norms then give N_K(J_o)=N_L(I)^h=d_H^h.

The ramification exclusion is necessary. In Z[i], J=(1-i) is stable under the full group but J intersect Z=2Z, so its unstripped index relation would say 4=2. The actual odd-part construction gives J_o=R and d_H=1. The reviewed proof never applies unramified descent to J's 2-part.

Eligibility now yields d_H<=2^(rho g)<2^g. Let t0=ceil(log2(d_H+1)); it is at most g, and d_H+1 binary combinations exist. Their residue keys A_o^-1 v mod Z^n lie in a set of cardinality d_H. A collision difference is nonzero by independence and ternary by disjoint supports. Multiplying by a gives a nonzero member of J with norm <=2sqrt(n). A deterministic ordered dictionary or sorting gives polynomial cost in numeric d_H and input bits. Only O(d_H) keys are stored; polynomial log d_H is not asserted sufficient.

For an odd prime power P^b, the stabilizer is the decomposition group because ideal factorization is unique. Its size is f_res in the unramified case. D=p^(bf_res), d_H=p^b, and e=p^b. This checks the prime-power claim and agrees with the direct Frobenius dependency. The latter independently maps invariant residues into the p roots of z^p=z, giving a p+1 collision without an explicit finite-field representation.

## Subfield contraction and family bound

For g a power of two with 2<=g<=n, Y=X^(n/g) has Y^g=-1 and generates the full cyclotomic ring R_g. Its coefficient inclusion has columns e_(jn/g), so it is explicit and isometric in the coefficient norm. There are exactly log2 n candidate values. At g=n the contraction is J_o itself, with d_n=D_o<2^n; thus feasibility is guaranteed at every eligible finite n. Comparisons and deterministic tie breaking are exact integer operations.

The same collision method now uses monomials of R_g and returns norm <=sqrt(ceil(log2(d_g+1)))<=sqrt(g), before multiplying by a. Choosing the minimum feasible d_g bounds its enumeration by any exhibited feasible index, even if its own selected degree is larger than the witness degree. No claim that g_* itself is O(log n) is needed for polynomial time or for the DD radius.

For the family proof, factor J_o mathematically as product P_i^(b_i), i=1,...,t'<=t. Factorization is not an input to the algorithm. With n=2^(N-1), g=2^(G-1), the exact odd-prime degree formulas follow by successive squaring: for p=1 mod4, v2(p^(2^k)-1)=v2(p-1)+k; for p=3 mod4 and k>=1, it is v2(p+1)+k. This yields the two displayed order formulas for L>=2. In both cases f'_i=max(c,2^(G-v)) and f_i=max(c,2^(N-v)), with c=1 or 2. Consequently f'_i<=max(2,(g/n)f_i)<=(g/n)f_i+2. This also covers G=N and g=2. The additive term cannot simply be removed, or even replaced uniformly by 1: n=8,g=2,p=7 gives f_i=f'_i=2, whereas (g/n)f_i+1=3/2.

For x in the lower field, v_(P_i)(x)=v_(Q_i)(x) because relative ramification is 1. Thus P_i^(b_i) contracts to Q_i^(b_i). A product of distinct prime powers is their intersection; contraction preserves intersection. If several Q_i coincide, the exponent becomes max b_i, not their sum. Therefore the norm of the contraction is at most product p_i^(b_i f'_i), and

    log2 d_g <= rho*g + 2*sum_i b_i log2 p_i
             <= rho*g + 2*t*log2 e.

The last step uses p_i^(b_i)|e for every individual unramified prime ideal, including repeated rational characteristics. Counting only distinct rational primes would not justify that t-bound. The exact finite test includes unequal exponents at two distinct primes over193 which merge below: n=32, D=193^3, e=193^2, d_16=193^2, and the full stabilizer is trivial.

Choose the smallest power of two g>=2 strictly above A log2 n, where A=2tC/(1-rho). For all sufficiently large n, g<=n and g<=max(2,2A log2 n). Strictness gives log2 d_g<g. Thus d_g<2^g<=max(4,n^(2A)), a polynomial numeric bound with constants fixed before n. The minimizer satisfies d_*<=d_g. For the finitely many smaller powers of two, d_*<=D_o<2^n is a constant depending on the fixed family, while arbitrary basis bit lengths remain charged polynomially. No computational knowledge of the asymptotic cutoff is required by the algorithm. These observations close the finite/asymptotic quantifier distinction.

## Rounding, exact DD radius, and source simulation

For the embedding matrix U, Fourier orthogonality gives U*U=nI. Therefore ||fw||_coef,2<=||f||_coef,2 ||w||_can,infinity. Every coefficient error is bounded by the left side. Since f lambda is integral, strict error <1/2 makes floor(x+1/2) recover it exactly; nonzero f is invertible in the number field. Negacyclic convolution and inversion of the multiplication matrix have polynomial bit cost in n, T, f and their full encodings. There is no numerical-embedding oracle or approximate rounding step. Output size is controlled by the same rational linear algebra.

For symmetry, 2sqrt(n)r<1/2 suffices. For subfield, 16r^2 g_*<1 is precisely the squared sufficient guard from norm <=2sqrt(g_*). These sufficient bounds need not be necessary for a particular returned member. The equality counterexample for the general member decoder does not claim the coarser subfield sufficient guard is sharp.

In FIXED-MAIN, epsilon0=epsilon_*/2, epsilon=epsilon_*/4, delta=epsilon_*/16. Substituting AM-MAIN-v3 gives exactly

    r=epsilon_* ell^2/(1024 n K chi Qmax).

The guards give Qmax>=Qmin>=8n^3 ceil(sqrt(Kn))ell^4, K>=1, chi>=1, ell>=2, and 0<epsilon_*<1. Hence

    r < 1/(8192 n^4 K ceil(sqrt(Kn))ell^2)
      < 1/(4sqrt(n)).

Both required strict guards hold for every full DD instance. Neither K nor Qmax has been dropped; no asymptotic replacement is used. As a separate feasibility observation, G-AM fails for n=2,4,8, because Bfun>=2^(-n/2)>epsilon_*/32. Thus the actual-DD corollaries at those dimensions are vacuous, while the independent algebraic decoders and their explicit r guards remain meaningful.

This is an actual direct BDD algorithm on every promised rational target. It does not infer BDD from easy wide DGS, does not sample a latent Gaussian, and does not call the target distinguisher. There is no probability space, posterior, success event, or adaptive schedule in the new proof. The inherited DD reduction retains its original separate probabilistic scope.

## Exponential norm, examples, and scope limits

For powers of two n>=4, ord_(2n)(3)=n/2. Choose a prime P over3 and a completely split prime Q over p_n=1 mod2n, with p_n polynomial in n. The accepted prime-list construction, or [Xylouris, Theorem1.1, printed p.66](https://www.impan.pl/shop/en/publication/transaction/download/product/83078), supplies such p_n. P and Q have different rational characteristics, so any automorphism stabilizing PQ must stabilize each factor. Q has trivial decomposition group; therefore PQ has trivial stabilizer. Its norm is 3^(n/2)p_n and its exponent is 3p_n. For fixed rho>log2(3)/2, log2 p_n=O(log n) is eventually smaller than the linear slack. This proves the example under its stated asymptotic rho range, without assuming infinitely many Fermat primes or ignoring split-prime acquisition.

Failure of d_H or d_* to have polynomial value is not hardness. A useful sharpness control is preserved in `new-negative-controls-v1.md`: consecutive split-prime factors give polynomial exponent but exponential d_* once prime support grows. It refutes a possible stronger algorithmic guarantee, not the present bounded-support theorem, and may still be solved by the separate scalar/member criteria. The hand-derived extension is proposed for separate fresh review if integrated into the coordinator's results.

## Controls, regression scope, and delivery

The first preregistered experiment exited1 at a SymPy HNF domain check after two successful fixtures; it did not produce a mathematical counterexample. Its complete code, stdout, stderr and receipt remain immutable. A separately granted second job changed only reconstruction of the already-integral C into the integer domain. It exited0: seven ideal fixtures, all normal-form crosschecks, 8149 exact residue-degree inequalities, acquired-member checks where under the declared numeric cutoff, and strict/ambiguous-definition controls passed. GNU time reports 0.83s wall and 49152KiB peak RSS. The larger unequal-merge collision loops were explicitly skipped at the preregistered cutoff20000. Finite tests do not certify the infinite theorem, the full DD parameter system, or asymptotic hardness.

All203 inherited references were resolved against the exact DD registry. All source-registry and entry hashes match; six entries required the registry's default ASCII JSON serialization rather than a Unicode-preserving serialization. Per-reference dispositions are in `regression-dispositions-v1.json`. The retained probability/quantum/distribution controls are outside these new deterministic proofs and are not recertified. Relevant algebraic, representation, strict-boundary, radius, numeric-value and source-scope controls are checked directly here. During review the live root registry gained applicability metadata and grew from2 to21 new entries. Its203 underlying source references and hashes were unchanged. The exact final snapshot and `supplemental-regression-dispositions-v1.json` preserve this reconciliation; the five added SV controls and explicit2-primary repair pass, while unrelated FF/CRT/iid/Gaussian controls remain outside scope. The frozen mathematical inputs did not change. CP-1's old invalid product remains rejected: posterior hit21/2000 exceeds1/100, later incidence21/221 is below1/10, and support restriction/normalization explains the failure. No step of the new proof uses such a product.

The reviewer did not spawn, install, change goals, launch nested Codex, alter tiers, edit git, publish, or communicate externally. Both experiments had individual root grants and released their slots. The read configuration states service_tier=default; this is configuration evidence only, not backend billing telemetry. Separate same-model reviews remain correlated scrutiny. This completed bounded review does not terminate the protected parent investigation.

Substantive next source-scope tests are: freshly review the unbounded-support counterfamily; investigate acquisition of small members when every standard contraction is large; compare all explicitly enumerable subfields against only the standard chain; and determine whether high-support ideals escaping these algorithms admit another direct decoder. Those are frontier tasks, not an exhaustion or hardness claim.
