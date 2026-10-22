# BLIND-SV1 — independent statement-only report, version 1

**Reviewer conclusion:** SV-BDD-CLASS v1 and SV-FROB-PRIME v1 are proved under their frozen assumptions. SV-SYMDESC v1 needs one explicit definition: `a=2^{v_2(e)}` and `m=e/a`. Merely requiring `m` odd, as its frozen text does, is insufficient; Section 7 gives an exact counterexample to that literal formulation. With the intended 2-primary decomposition made explicit, the independent proof below establishes all its mathematical conclusions. This is a local blind-review result, not a programme-wide ACCEPT, a review of inherited reduction proofs, or an assertion of source hardness. The coordinator must version and freshly reconcile the definition repair rather than silently inherit approval.

The exact statement versions are the five immutable packet inputs identified in `allowed-read-manifest-v1.json`; all five hashes were recomputed and matched. The assignment is preserved verbatim in `assignment-verbatim.txt`. The three candidates are SV-BDD-CLASS v1, SV-FROB-PRIME v1, and SV-SYMDESC v1. The two inherited statements are used only for definitions and parameter premises. In particular, their historical/status wording is not evidence of a theorem being accepted.

## 1. Frozen model, conventions, and dependencies

Write N for the field degree in this report when needed to avoid confusing the number field K with the inherited physical sample count K. In formulas copied from the statements, n is the field degree and K is the physical sample count. The field is Q(zeta), zeta a primitive 2n-th root, n>=2 a power of two. The coefficient order is 1,zeta,...,zeta^(n-1). Inputs are nonsingular integer column bases of nonzero integral ideals. A prime ideal is proper; a prime power means exponent b>=1. These are standard conventions, not added cryptographic assumptions.

J^-1 means {lambda in the number field: lambda J is contained in R}. All targets have rational coefficient representations. The promise is pointwise: T=lambda+w with lambda in J^-1 and max_sigma |sigma(w)|<=r. The proposed decoders have no oracle, no random coins, and no average over targets or ideals. Complete integer/rational representations and output lengths are charged. An existential small member is not supplied algorithmic information.

The imported algebraic facts are: R is the full ring of integers; only 2 ramifies, with (2)=P_2^n and norm(P_2)=2; ideals factor uniquely; primes over a prime of a fixed field form one Galois orbit; the ramification/residue-degree formula holds; and odd-prime Frobenius is zeta -> zeta^p. These were checked in Milne, Algebraic Number Theory v3.08, Theorems 3.20/3.29/3.34, Propositions 4.2/6.2/8.11, and Example 8.18. The polynomial-bit integer-normal-form theorem was checked in the primary Kannan–Bachem publication abstract. These imported facts are sufficient; no hardness theorem or unlisted historical proof is used.

Primary sources:

- Milne: https://www.jmilne.org/math/CourseNotes/ANT.pdf
- Kannan–Bachem: https://epubs.siam.org/doi/abs/10.1137/0208040?journalCode=smjcat

The claim dependency graph is:

| Claim | Content | Dependencies | Local result |
|---|---|---|---|
| NORM | Canonical/coeff normalization and product error bound | Fourier orthogonality, derived below | Proved |
| EXP | Quotient exponent, HNF identity, scalar decoder | Exact linear algebra, NORM | Proved |
| MEM | Arbitrary acquired ideal member decoder | NORM, definition of J^-1 | Proved |
| COLL | Numeric-index collision construction | Exact quotient keys, pigeonhole principle | Proved |
| RAD | Actual inherited radius is <1/(4sqrt(n)) | Explicit represented width guard only | Proved |
| ODD | Odd-prime degrees, exponent structure, 2-primary bound | Imported cyclotomic facts | Proved |
| FIX | Effective signed invariant lattice | Signed graph construction, fixed-field degree | Proved |
| FROB | Prime-characteristic collision construction | FIX, odd Frobenius, MEM | Proved |
| DESC | Odd stable ideal descends and d_H^h=D_o | ODD, prime orbit/valuation argument | Proved |
| SYM | Effective stabilizer decoder and prime-power corollaries | EXP, FIX, DESC, MEM, RAD, explicit a=2^{v_2(e)} | Proved after definition clarification; literal wording fails |

## 2. Norms, strict rounding, and finite representations

Let U be the n-by-n matrix U_(j,k)=zeta^((2j+1)k). Summing geometric progressions gives U*U=nI. Thus, for every coefficient vector x,

    ||x||_coef,2^2 = (1/n) sum_sigma |sigma(x)|^2.

In particular ||w||_coef,2<=||w||_can,infinity. There is no extra sqrt(n) factor in this inequality. Multiplication and the same identity give the stronger useful estimate

    ||fw||_coef,2^2
       = (1/n) sum_sigma |sigma(f)|^2 |sigma(w)|^2
       <= r^2 ||f||_coef,2^2.

Every coefficient of fw therefore has absolute value at most r||f||_coef,2. If f is a nonzero element of J, then f lambda is integral. When 4r^2||f||_coef,2^2<1, every coefficient of fT lies strictly less than 1/2 from its correct integer. The prescribed floor(x+1/2) consequently returns f lambda, including when coordinates or errors are negative. Division by nonzero f is valid because X^n+1 is irreducible and the quotient is a field. This proves MEM and SV-BDD-CLASS part 2.

All multiplication is exact negacyclic convolution. Division can be done by solving the rational linear system for multiplication by f. The matrix dimension is n; entry bit lengths are bounded by the full f encoding. Determinant/cofactor bounds show its exact inverse, the solution, and intermediate representations in a polynomial-bit linear-algebra algorithm have polynomial length. No numerical embeddings or approximate rounding are needed. The displayed guard is an exact rational comparison, and the output cost is included. Correctness also proves uniqueness under that guard: two promised lattice points would round to the same f lambda and hence coincide.

Strictness cannot be dropped uniformly. Take n=2, J=R, f=1, lambda=0, T=1/2, r=1/2. The norm promise holds at equality, but floor(T+1/2)=1. The same T is also at radius 1/2 from lambda=1. This is a genuine failure at 2er=1 and at 4r^2||f||^2=1, not a failure inside either stated strict guard.

## 3. Quotient exponent, HNF, and direct collision classification

For the supplied basis A, eR is contained in J precisely when e A^-1 is integral. Hence the least positive such e is the lcm of the reduced denominators of all entries of A^-1. Those denominators divide |det A|. Exact inversion, gcd/lcm arithmetic, and the lcm's bit length are polynomial in n and the full basis encoding. This is an ordinary-basis computation; it does not require factoring D.

If H is the specified upper-triangular column HNF, a scalar integer t belongs to J exactly when H11 divides t: triangular back-substitution forces every coefficient of columns 2 through n to be zero. Since J is an ideal, t in J is equivalent to tR contained in J. Thus H11=e. Applying triangular back-substitution to e times the i-th coefficient unit vector shows Hii divides e. Therefore H11=e=max_i Hii. The upper-triangular **column** convention and the basis beginning with 1 matter; no claim about an arbitrary differently oriented diagonal is being made.

Since e is itself in J, e lambda is integral. With 2er<1, scalar rounding is the MEM argument with f=e, and proves part 1.

For part 3, D is the exact number of cosets of J in R. D<2^n implies h0=ceil(log2(D+1))<=n. The D+1 distinct binary coefficient vectors supported on the first h0 coordinates must contain two with the same ideal residue. Their difference is a nonzero ternary element f of J and has squared coefficient norm at most h0. A canonical exact residue key is

    A^-1 x modulo Z^n,

with each rational coordinate reduced to [0,1). Equality of keys is exactly x-y in J. There are D+1 keys, each of polynomial encoding length. A deterministic sorted dictionary or sorting pass gives time and storage polynomial in numeric D and the complete input lengths. This is not polynomial in log D on unrestricted ideals. D=1 causes no exceptional branch: h0=1, and 0 and 1 collide modulo R.

The strict guard 4r^2 h0<1 allows MEM. On families D<=n^C for fixed C the runtime is polynomial in n and the complete input length. A statement of polynomial time in n alone would additionally need input lengths bounded polynomially in n; none is silently substituted here.

## 4. Exact inherited radius, including small dimensions

Use only the inherited explicit premises. They give epsilon_* in (0,1), K>=1, ell=ceil(log2(2nK))>=2, chi>=1, and

    Qmax >= Qmin >= n sigma_floor
         = 8 n^3 ceil(sqrt(Kn)) ell^4.

Consequently the exact stated radius satisfies

    r = epsilon_* ell^2/(1024 n K chi Qmax)
      < 1/(8192 n^4 K chi ceil(sqrt(Kn)) ell^2)
      <= 1/(8192 n^4)
      < 1/(4sqrt(n)).

This is a finite strict inequality for every input satisfying all the inherited guards, not merely an asymptotic estimate. No guard is replaced by an uncharged transcendental comparison. Extra inherited guards can only restrict this domain. In particular r<1/(2sqrt(n)) and r<1/4. Hence B=1/(2r)>2sqrt(n)>2 (indeed B>2sqrt(n) follows directly from the stronger bound). All uses of log2 B in the source classification are therefore legitimate.

The inequality implies every eligible numeric-polynomial-index family is covered by COLL, and every effectively acquired member with norm<B is covered by MEM. The symmetry member bound 2sqrt(n) is also strictly below B.

There is a useful small-dimension qualification. Under FIXED-MAIN, epsilon=epsilon_*/4, so (G-AM) requires Bfun<=epsilon_*/32<1/32. But Gamma>=1, D>=1, and the definition with min(1,...) gives Bfun>=2^(-n/2). Thus the complete inherited guard system has no instances at n=2,4,8. The exact-DD-radius corollaries in these dimensions are vacuous. The general deterministic algebraic decoders, stated for their own explicit r guards, still apply there. This observation neither refutes nor enlarges an inherited theorem.

## 5. Odd residue degrees and the general exponent bound

Write J=P_2^b times its odd part. The norm restriction implies 2^b<=D<2^n, so 0<=b<n. Since (2)=P_2^n, the 2-part of the quotient exponent is 1 if b=0 and 2 otherwise.

For each odd rational prime p, write the p-part of J as the product of P^(b_P) over primes P above p. Odd primes are unramified and their common residue degree is f_p=ord_(2n)(p). Therefore

    e_odd = product_p p^(max_P b_P),
    D_odd = product_p p^(f_p sum_P b_P).

These are identities used to prove a structural statement, not a requirement to factor the supplied input. If every occurring f_p>=F, then

    e <= 2 D_odd^(1/F) <= 2 D^(1/F) <= 2^(1+rho n/F).

Thus the displayed strict structural bound in SV-BDD-CLASS part 6 is sufficient for scalar decoding. Its contrapositive is valid. If e>=B and an integer F satisfies the strict bound, there must be an odd p with f_p<F. Since the set of qualifying integer F, when nonempty, has a least element, one can also choose a prime with residue degree below every qualifying F. A pure2 ideal cannot be an exception: e<=2<B.

For a proper odd prime ideal J above p, the quotient is a field of characteristic p, so its additive exponent is p, and D=p^f. If the exponent test fails then p>=B and

    f log2 B <= f log2 p = log2 D <= rho n.

This proves part 5. Neither this necessary condition nor failure of the sufficient structural bound is a hardness statement. At rho=0, only J=R is eligible, so the proper-prime portions are empty and the other algorithms still work.

## 6. Effective signed invariants and the Frobenius construction

For any odd u modulo 2n, sigma_u(zeta^j)=s_j zeta^(uj mod n), with s_j in {+1,-1} determined by reduction modulo 2n. Thus every automorphism is an explicitly computable signed permutation matrix, using modular integer arithmetic even if p is large.

For one signed permutation, traverse its cycles. On a cycle the invariant coefficient equations determine every coefficient from a single integer c. A positive sign product permits arbitrary c and gives the unique basis vector whose selected initial coordinate is +1. A negative sign product forces c=-c, hence c=0 over Z. This is why inconsistent cycles must be omitted, rather than treated as additional binary choices.

For a subgroup H, build a graph with all edges i -> uj mod n and their signs, for every u in H. A connected component gives one such signed basis vector exactly when all path-sign equations are consistent. Otherwise it gives none. These vectors have disjoint supports, entries in {0,+1,-1}, and form an integral basis of the simultaneous invariant lattice. Clearing denominators shows this lattice spans the fixed field over Q. Hence its rank is [K^H:Q]=n/|H|. The construction uses polynomially many signed edges and never requires a supplied subfield representation. For a noncyclic H, using all H-edges is essential; cycles of one arbitrary element alone are not the proposed simultaneous-invariant construction.

For an odd prime ideal, the automorphism sigma_p acts on R/J by x -> x^p: this follows directly by expanding coefficients in characteristic p. Its order on the cyclotomic field is f_res=ord_(2n)(p). Thus its invariant lattice has g=n/f_res basis vectors. Every invariant residue satisfies x^p=x in the finite field R/J, and so lies in F_p. Constants show the image is exactly F_p, of cardinality p. This proves the collision bound without invoking the general descent theorem.

The norm premise gives p^f_res<=2^(rho n), so p<=2^(rho g)<2^g. Since p is integral, p+1<=2^g and ceil(log2(p+1))<=g. The p+1 indicated binary sums therefore exist. Two collide in a set of p possible residues. Their difference is nonzero because the invariant basis vectors are independent, and ternary because supports are disjoint. Its squared norm is at most n. Exact ordinary-basis keys find the collision deterministically in time and storage polynomial in numeric p and the full encodings. With r<1/(2sqrt(n)), MEM finishes the proof of SV-FROB-PRIME.

The p=2 exception is correctly separate. Sigma_2 is not a Galois automorphism here. Instead 2 belongs to the unique prime over 2, and scalar multiplication gives the stated r<1/4 decoder. The actual inherited radius satisfies that guard.

Concrete inconsistent-cycle examples: for n=2,u=3, the coefficient of X must vanish; the basis is {1}. For n=4,u=3, X^2 maps to -X^2 and is omitted, while X and X^3 form a positive cycle; the invariant basis is {1,X+X^3}. These examples were included in the exact signed-cycle regression.

## 7. Symmetry descent, ramification, and effectiveness

There is a definition defect in the frozen wording. `Write e=a*m with m odd` does not require `a` to be a power of 2. For example, an eligible n=4 prime above 3 has e=3, and a=3,m=1 meet that displayed condition while violating the next claimed consequence a in {1,2}.

A stronger exact counterexample to the literal decoder wording is n=8, rho=3/4, J=(17,X-3). Since 3^8=-1 mod17, evaluation at3 defines a surjection R -> F_17 with this kernel, so D=e=17<=2^6. Choose a=17,m=1, which satisfies the only stated condition that m is odd. Then J+mR=R, H is the full group, h=8, g=1, d_H=1, and the invariant basis is {1}. The collision step returns v=+1 or -1, hence f=+17 or -17, contradicting ||f||<=2sqrt(8). Moreover take lambda=0 and T=r=1/20 as a constant polynomial. This satisfies r<1/(4sqrt(8)), but rounding fT and dividing by f returns 1/17, not0, for either sign. These are hand-derived exact counterexamples; no extra computational job was run. The general symmetry statement's parts1–3 do not require a full DD parameter package, so the separate vacuity of DD guards at n=8 does not remove this counterexample.

The minimal repair is to define a=2^{v_2(e)} and m=e/a, equivalently require a to be a power of2. The following proof is explicitly conditional on that repaired definition; it does not infer the desired a from m being odd. Compute a by repeated division by2. Section5 then proves a in {1,2}. Let J_o denote the odd ideal part mathematically. At every odd prime P dividing J, the valuation of mR is at least the valuation of J; at P_2, m is a unit. Taking prime valuations of the sum of ideals therefore gives

    J+mR=J_o.

The basis of this sum is obtained from the integer column span of [A | mI] using polynomial-bit normal forms. More explicitly, compute a square Smith form U A V=diag(s_i); in U-coordinates the sum has basis diag(gcd(s_i,m)), so U^-1 diag(gcd(s_i,m)) is a basis of J_o. This is a computation from A, not a factorization algorithm.

Let A_o be a resulting basis. For each of the n odd residues u modulo 2n, test whether A_o^-1 sigma_u A_o is integral. That tests sigma_u(J_o) subset J_o; equal absolute determinants make inclusion equivalent to equality. Thus H is computed in polynomial bit complexity. It is a subgroup, h=|H| is available explicitly, and g=n/h. Construct the simultaneous invariant basis by the signed graph above.

Put F=K^H and S=R^H. An element of F is integral over Z precisely when it belongs to R, so S=O_F. Every odd prime of K is unramified over Q and therefore also over F. Factor J_o only for this argument. Its H-stability makes its prime exponents constant on every H-orbit. The primes over one prime q of F form exactly such an orbit. Because the relative ramification indices are 1, if this common exponent is b_q, then

    I=product_q q^(b_q) in O_F

satisfies IR=J_o and I=J_o intersect O_F. It follows from the residue-degree formula, orbit by orbit, that

    N_K(IR)=N_F(I)^h.

Hence d_H=[S:I] obeys d_H^h=D_o exactly. This is an equality of integral norms, not a real-number approximation. Since D_o<=D<=2^(rho n),

    d_H<=2^(rho g)<2^g.

One effective way to obtain d_H is the exact integer h-th root of D_o. Binary search with integer exponentiation, followed by an exact power check, takes polynomial bit complexity in n and log D_o. The just-proved identity ensures the root is integral. This avoids any assumption that a subfield basis or contraction basis is supplied. Alternatively integer intersection computations give the same index.

There are exactly d_H cosets of J_o intersect S in S. Enumerate the indicated d_H+1 binary invariant combinations. The same exact keys modulo A_o produce a nonzero ternary v in J_o with squared norm<=n. The runtime/storage are polynomial in numeric d_H and the full encodings. The method does not enumerate D_o unless its chosen parameter d_H actually equals D_o, as can happen when H is trivial.

If J_2 is the 2-primary part, then aR is contained in J_2. Thus f=a v belongs both to J_2 and J_o, and hence belongs to J=J_2 intersect J_o. It is nonzero and has norm<=2sqrt(n). When r<1/(4sqrt(n)), MEM rounds fT correctly. Section 4 supplies this strict guard at the exact inherited radius. This proves SV-SYMDESC parts 1–3 with their stated numeric-complexity distinction.

Removing ramification is necessary. For n=2, J=(1-X) in Z[i], the entire Galois group stabilizes J. Its fixed ring is Z, J intersect Z=2Z, and h=2. Thus d_H^h=2^2=4 while D=2. This refutes the unstripped variant of the identity. In the actual theorem J_o=R, d_H=1, and the identity holds. More generally b<n is exactly what permits repair by the scalar a<=2; without the eligibility bound, larger powers of 2 could be needed.

For J=P^b at an odd p with b>=1, uniqueness of ideal factorization gives sigma(J)=J iff sigma(P)=P. The stabilizer is the decomposition group, of size f_res. Unramified valuations give e=p^b; D=p^(b f_res) and d_H^f_res=D then yield d_H=p^b=e. For a pure2 eligible ideal, m=1, J_o=R, H is the whole group, g=1, d_H=1, and the constructed member can simply be 2 (or 1 if J=R). Mixed and composite ideals use the same argument without any prime-power assumption. This proves part 4.

## 8. Finite regressions, effectiveness limits, and exponential index

Exactly one finite experiment was run. It was preregistered and separately allocated by the root before launch. Code, hypotheses, fixed inputs, deterministic/no-seed declaration, exact precision, resource caps, grant, stdout, exit status, and result are preserved under `experiment-01*`. It exited 0/PASS in 19.156426609 seconds, under wall 120 seconds, CPU 115 seconds, and RLIMIT_AS 512 MiB. No follow-on job was launched.

The experiment checked all odd automorphisms for n=2,4,8,16,32,64 (126 cases) and ten explicit eligible ideals. It constructed ordinary bases, computed exact inverse-basis residue keys and stabilizers, independently enumerated the image of the fixed lattice, and checked the descent identity, collision members, membership, norm bounds, and exact rounding at a small rational test radius. Its main ideal witnesses are:

| Ideal case | n | D | e | h | d_H |
|---|---:|---:|---:|---:|---:|
| (1-X) | 2 | 2 | 2 | 2 | 1 |
| (1-X)^3 | 4 | 8 | 2 | 4 | 1 |
| (1-X)^7 | 8 | 128 | 2 | 8 | 1 |
| Prime above 3 | 4 | 9 | 3 | 2 | 3 |
| Prime above 31 | 32 | 961 | 31 | 2 | 31 |
| Its square | 32 | 923521 | 961 | 2 | 961 |
| Its square times (1-X) | 32 | 1847042 | 1922 | 2 | 961 |
| Two distinct primes above 31 | 32 | 923521 | 31 | 2 | 961 |
| Product of split primes above 97 and 193 | 16 | 18721 | 18721 | 1 | 18721 |
| Previous product times (1-X) | 16 | 37442 | 37442 | 1 | 18721 |

These finite tests are evidence and implementation-level regressions, not proofs of unbounded assertions. Fixture generation used specified factors/roots to construct examples. The main proof, not this fixture setup, establishes factor-free ordinary-basis effectiveness. The test was supplied separate odd/full bases and therefore is not an independent implementation test of the J+mR normal-form step. Its rational test radius was not a numerically instantiated full DD parameter package; Section 4 proves the exact-DD radius claim symbolically from its true guard.

Exponential index is compatible with the positive classification. For example, for powers of two n>=32, ord_(2n)(31)=n/16. This follows from v_2(31^2-1)=6 and successive squaring. A prime P above 31 has norm 31^(n/16), and P^2 has norm 31^(n/8)=2^((log2 31)/8)n, with exponent (log2 31)/8<1. Thus for fixed rho above that constant, P^2 is an eligible exponential-index family with d_H=e=961. Products of two primes above 31 give another such family. Appending a bounded 2-primary part preserves eligibility for all sufficiently large n after choosing strict rho slack. These examples establish compatibility of exponential index with direct decoding, not that every claimed comparison regime is populated for every fixed DD parameter choice.

If H is trivial, then g=n and d_H=D_o; the symmetry method can still be exponential in n. If p, d_H, or D is only known to have polynomial bit length, the corresponding enumeration need not be polynomial time. No proof here replaces numeric polynomial bounds by encoding-length bounds, assumes an ideal factorization, or grants a short basis.

## 9. Quantifiers, hardness scope, and residual audit limits

Each decoder applies to every promised rational T for each supplied ordinary basis satisfying its specific premises; success is deterministic and pointwise. No auxiliary modulus list, target distinguisher, secret distribution, signed advantage calibration, Gaussian completion, DGS sampler, or averaging over ideals participates in these direct algorithms. The only connection with FIXED-MAIN is substituting its exact represented r and using its explicit parameter guard to bound r.

Therefore these results identify easy portions of the **restricted source family**. They do not establish or refute a fixed-target binary-RLWE advantage premise, do not alter its single-q0 quantifiers, do not audit the correctness of the inherited reduction, and do not establish a hardness reduction for the remaining source family. The finite necessary condition on unclassified prime ideals and the failure of polynomial numeric d_H are not lower bounds. Likewise no implication from easy wide DGS to BDD, or from an existential short vector to an effective one, is used.

No probabilistic lemma is introduced or certified here. The inherited probability statements and their adaptive proof obligations were deliberately outside this packet's review scope. Accordingly CP-1 is conceptually read but need not be rerun for these deterministic source claims; no sequential probability product is used. Historical project regressions were withheld by the blind assignment, so global reconciliation remains the coordinator's responsibility.

The exact SV-SYMDESC wording is not accepted as written: its decomposition definition must be clarified and the edited statement version rechecked under the programme's repair rules. No additional algebraic obstruction was found once a is defined to be the 2-primary part. The other two candidate statements do not depend on that wording repair.

The reviewer did not inspect author proofs, status ledgers, other reviews, or original provenance paths; did not spawn agents, launch Codex, create/change goals, install packages, mutate git, select Fast/priority, or start detached services. No backend billing telemetry is available, so the inherited launch description is not reported as verified billing data. This bounded review returns on completion without terminating the protected parent investigation.
