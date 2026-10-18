# BT15 complete blind reconstruction and falsification report

## Identity, scope, and disposition

This is an independent reconstruction from the frozen assignment and its four permitted input files. I did not read any supplied proof, external source, other referee report, project status, ledger, summary, native session, parent-directory listing, or C8 material. No agents, goals, external services, or detached computation were created. The only messages received after the assignment were administrative. The sole experiment was reserved by root as BT15-FV1 before execution. The report is complete at the time of its separate freeze receipt; its bytes must not be edited after that receipt.

**Disposition:** I find no counterexample to the quotient-pair theorem v2, the fixed-map theorem v3, or the generic finite coherent-adapter theorem v1 under their supplied definitions. The reconstructions below establish their displayed probability/error bounds. The adapter's C8 paragraph is justified only as a conditional substitution of a pointwise error bound and an executable-program call bound. It does not establish those application premises, a query-state preparation procedure, a DGS law, or hardness. The elementary-gate count is valid in the explicitly stated Boolean-circuit model; a count of coherent Rec executions is a count of executions of executable reversible circuits, with their work retained, not of calls to a classical answer or sampling service.

The scrutiny is mathematically substantive but is not formal verification. Same-model role diversity is correlated scrutiny. Finite controls below test particular constructions and failure mechanisms; they are not proofs of infinite-lattice statements or hardness.

## Frozen inputs

All paths below are relative to this BT15 directory. SHA-256 digests were computed on the exact input bytes before writing this report.

| File | SHA-256 |
|---|---|
| `assignment-v1.md` | `5bb493fcddf916cd1382a1dd2a4c51373ee25083bcf11d15586e62610bd3d9df` |
| `input/pair-theorem-v2.md` | `80cd0798a135eea545bfd1a4dd2226eb7b3b47789999bfb810002c6f8aef77f3` |
| `input/fixed-map-theorem-v3.md` | `d5508d295102673ac44b897f30f68b6dc6ad23ac31672443f5f394f19985fd99` |
| `input/coherent-adapter-theorem-v1.md` | `66d889b189b4193d0e07be3e9baa0b3ce78803ba824e9aedea7f622e9cada3cc` |
| `input/definitions-v1.md` | `8bc7f1fb091d31dc607c3178e20fbd7ac6db4634348664341ed57c486b845f81` |

The supplied definition explicitly restricts the adapter's p and tau to [0,1]. The CP1 datum supplied is the selected-hit mass 21/2000 and second residual incidence 21/221. No fuller original CP1 sample space was provided, and I do not invent one or claim to have reconstructed an unseen original experiment.

## Common ideal-lattice and Gaussian facts, independently reconstructed

Write delta = D_I^(1/n). All covolumes and norms here use the coefficient Euclidean space in the statement, not an unscaled canonical embedding.

1. The power basis identifies R with Z^n, so det(R)=1 and det(I)=D_I. Ideal norm multiplicativity and scaling by 1/c give

       det(J) = D_I D_H / c^n.

   The nonzero fractional ideal J is a full-rank lattice. Also cR subset I implies D_I <= c^n, hence delta/c <= 1. The assumption c is an integer is consistent with these inclusions and with c being the public nonzero coefficient vector (c,0,...,0).

2. Every nonzero a in I has |N_K/Q(a)| >= D_I. Indeed, (a) subset I, and [R:(a)] = [R:I][I:(a)]. For the power-of-two cyclotomic field, the embedding evaluation matrix is the Fourier matrix on the n odd 2n-th roots. Orthogonality gives

       sum_sigma |sigma(a)|^2 = n ||a||^2.

   Applying the arithmetic-geometric mean inequality to the n nonnegative embedding squared magnitudes gives |N(a)|^(1/n) <= ||a||. Consequently

       a in I, a != 0  ==>  ||a|| >= delta.

   This is the only algebraic separation bound needed. In particular, there is no missing sqrt(n) in coefficient coordinates.

3. If a set E is contained in a ball of radius R and its distinct points have differences in I, its points are delta-separated. Disjoint open balls of radius delta/2 around those points lie inside the concentric ball of radius R+delta/2. Volume comparison yields

       |E| <= (1+2R/delta)^n.

   The containing center can be any point of V. This argument does not require E itself to be a subset of I. It also applies at R=0, when the cardinality is at most one. Bounded lattice intersections are finite, and boundary contacts between the open balls have zero volume.

4. Let rho_W(J)=sum_{z in J} exp(-pi ||z||^2/W^2). Poisson summation for this Gaussian, with dual J* in coefficient Euclidean coordinates, gives the exact centered normalizer

       rho_W(J) = W^n/det(J) * sum_{u in J*} exp(-pi W^2 ||u||^2)
                >= W^n/det(J).

   The series converge absolutely. The dual zero term proves the inequality; all other terms are nonnegative. Thus every atom of the stated centered law satisfies

       D({x}) <= 1/rho_W(J) <= D_I D_H/(cW)^n.

   This uses the actual discrete Gaussian law and its normalizing sum. A covariance statement alone does not supply this atom bound.

Combining the packing count at R=gamma*c with this atom bound gives

    (1+2gamma*c/delta)^n * D_I D_H/(cW)^n
      = D_H ((delta/c+2gamma)/W)^n.

After the trivial probability cap this is exactly b in the pair theorem. The same expression is the fixed-map bound.

## Quotient-pair theorem v2

### Uniform small-ball sections and the independent statement

For an arbitrary a in V define the Borel set

    E_a = {x in J : x-a in I and ||x-a|| <= gamma*c}.

Distinct elements of E_a differ by an element of I and are delta-separated. The preceding calculation therefore proves

    sup_{a in V} D(E_a) <= b.

This is uniform over all ambient centers, not merely centers in J. Conditional on X_i=a, a later independent exact sample has probability at most b of forming the tested pair. Union over the binom(m,2) pairs gives (1), with the cap at one. This derivation includes X_j=X_i; neither separation nor the Gaussian atom bound discards the zero difference.

For exact samples in J, equality of G=J/(I intersect J) labels is equivalent to X_j-X_i in I: their difference is already in J, so membership in I is membership in I intersect J. The quotient is finite: cJ=IH is contained in both I and J, hence cJ subset L. A measurable selector's successful signed output is pointwise contained in the union of tested pair events. Its use of all labels, norms, fixed advice, or private randomness does not change this containment. The sign preserves norm and I-membership. Requiring a nonzero output only shrinks the event.

### Sequential statement, including null histories and arbitrary X_1

At stage j let z denote the complete preceding history. On attempted histories define

    B_j(z) = union over i<j with A_i(z)=1
             {x in V : x-X_i(z) in I and ||x-X_i(z)|| <= gamma*c}.

The history assumptions imply that the previous attempted values and indicators are measurable functions of Z_(j-1), up to the usual almost-sure versions. The relation x-a in I is Borel because I is a countable closed lattice; the norm inequality is closed. Consequently the set of pairs (z,x) with x in B_j(z) is measurable. The kernel integral K_j(z,B_j(z)) is therefore a legitimate measurable conditional probability. The same holds for D(B_j(z)). This is a conditional-section calculation, not informal conditioning on a singleton of probability zero.

If k(z) previous stages were attempted, the uniform small-ball result gives

    D(B_j(z)) <= min(1,k(z)b) <= (j-1)b.

On the almost-everywhere set of attempted histories where the supplied TV premise holds,

    K_j(z,B_j(z)) <= D(B_j(z)) + eta_j.

There is one TV payment for the union section at a stage, not a separate eta_j payment for each previous index. Multiplying by the predictable A_j and integrating yields

    Pr[A_j=1 and a matching prior attempted pair occurs at j]
       <= (j-1)b + eta_j.

Summing j=2,...,m proves (3). More precise bounds could retain attempt probabilities and min(1,k(z)b), but are unnecessary for the displayed conclusion.

No atom of the history law was assumed to have positive probability. Null histories impose no requirement, because their kernel sections do not affect the integral. The premise applies to the actual regular conditional law given the complete retained state. A countable generating algebra for Borel V suffices to express TV to the fixed reference as a measurable supremum, so the premise itself has the usual measurable meaning.

There is no step using a Gaussian premise on X_1. Its value merely supplies one possible center a in the uniform section bound. The attempt decision at j is measurable before the fresh value; a generated value cannot be removed retroactively from the count. Dummy values are omitted from B_j unless their stage was actually attempted. Rejecting or deleting an observed value can influence future attempts, but does not erase the current event or its charge.

This proves the stated useful-output bound by event containment. For approximate samples, all laws live on V. If an implementation requests a quotient label, it first rejects an out-of-J input; if it tests the difference directly, the Borel difference condition remains meaningful everywhere on V. The latter can actually use an arbitrary out-of-J first center, as the explicit example below shows.

### Constants and sample lower bound

For gamma=1,

    b <= D_H (3/W)^n <= (3*2^rho/W)^n <= (6/W)^n.

Only the first two inequalities use delta/c<=1 and D_H<=2^(rho*n); rho<1 is stronger than needed for the final weak inequality. W>=32*sqrt(2)*n^2 makes (6/W)^n negligible along powers of two. Multiplication by polynomially bounded m^2 preserves negligibility. Adding a negligible sum of deterministic eta_j preserves it as well.

When the eta_j are zero, success >= epsilon and the upper bound imply

    binom(m,2) >= epsilon*(W/6)^n.

Since m(m-1) <= m^2, the claimed m >= sqrt(2epsilon)*(W/6)^(n/2) follows. With nonzero errors the conclusion does not follow unchanged; a bound would have to subtract their total from epsilon. The theorem correctly restricts its displayed lower bound to zero errors or the independent exact statement.

## Fixed-map theorem v3

### Nonzero R-linearity gives the required injection

Every nonzero R-linear map T:J->I extends to multiplication by a nonzero scalar in K and is injective. One direct verification avoids a basis assumption on the ideal: choose a nonzero a in J and an integer d clearing the denominators of a and x. R-linearity gives

    (da) T(x) = T(dax) = (dx) T(a).

Because the ring is a domain, this identifies T(x)=x*T(a)/a. If T(a)=0 then the identity would force T to vanish on J; for nonzero T it does not. Thus distinct x have distinct T(x).

For fixed y in I, the successful images T(x)+y lie in I and in the radius-gamma*c ball about zero. Their cardinality is at most (1+2gamma*c/delta)^n. Injectivity makes this also the number of successful preimages. Multiplying by the exact Gaussian maximum-atom bound proves the first inequality. The inclusion cR subset I gives delta/c<=1 and proves the second inequality. A possible image equal to zero is counted, exactly as stated.

The proof needs neither an operator-norm estimate nor a lattice basis for T(J), and it does not assert efficient construction of T or efficient sampling from arbitrary J. Although additional algebraic bounds on a scalar multiplier are possible, they are unnecessary here.

### Approximate and adaptive uses

For an approximate law on V, define the success set only on J. The output is failure outside J, and failure is not assigned norm zero. Since J is countable and the map on J is measurable, this is a Borel output rule after adjoining a failure symbol. TV therefore adds at most eta to the reference probability.

For each attempted stage, fix a complete prior history outside the relevant null set. At that history the current parameters, T and y are fixed, the preceding argument bounds the current reference success probability by the supplied b, and conditional TV adds eta_j. Integration followed by a union bound over at most Q attempted slots gives min(1,Qb+sum eta_j). Independence of outputs is not required. The decision to attempt is part of the preceding transcript, so the same predictability issue as in the pair theorem is resolved. Random parameters and maps must have the stipulated measurable dependence; with the stated standard Borel transcript this is the ordinary conditional-section argument.

Selecting T or y from a prior transcript is allowed only while the conditional fresh law retains the stated reference/TV property. Selecting either after seeing that stage's X is outside the assertion. The concrete output-dependent-translate counterexample below shows why this distinction matters even for a useful nonzero output.

At gamma=1 the same constant calculation gives (6/W)^n, including zero outputs. The already-public c has coefficient norm c and belongs to I. The theorem's interpretation is therefore accurate: this specified extraction process almost never produces any vector of that length under its Gaussian premise and polynomial attempt/error budget. It does not rule out other extraction mechanisms or claim that the public c is a newly discovered vector.

### Contextual algebra and source scope

The inclusions and inverse identity stated for context are correct:

    cR subset I ==> H subset IH/c = J,
    J^-1 = c I^-1 H^-1.

They use invertibility of nonzero ideals in this ring of integers. Also I^-1 subset (1/D_I)R and H^-1 subset (1/D_H)R, since D_I R subset I and D_H R subset H. Thus J^-1 has rational coefficient denominators dividing D_I D_H after multiplication by the integer c; when q is coprime to c D_I D_H these denominators are invertible modulo q, giving the stated natural reduction to R/qR. The condition also makes the ideal data trivial after localization at the primes dividing q. This algebra does not establish pseudorandomness, statistical closeness, a reduction, or computational hardness of that proposed source. No GP/BDD/DGS theorem is reconstructed or used here.

## Finite coherent adapter v1

### Construction with complete target/reference entanglement

Use r coin qubits C, initialized to zero, and workspace W containing the S newly computed Boolean wires. Apply H to all r coin qubits. Let B reversibly compute the deterministic function of (x,c) implemented by the fixed program, retaining its input and all intermediate wires. Copy its m answer bits by CNOT into the arbitrary target Z, apply B inverse to clear the computation workspace, then apply H to all r coin qubits again. This is one fixed unitary V. No correctness test or favorable-tape selection is used.

Write an arbitrary pure input, including an untouched reference, as

    |psi> = sum_x |x> |psi_x>,     sum_x ||psi_x||^2 = 1.

The vector |psi_x> includes both target and reference; its target need not be a basis state, zero, or unentangled. Let P_a denote XOR by bit string a on the target, tensored with identity on the reference. After compute/copy/uncompute but before the final coin Hadamards, the actual and ideal states are respectively

    2^(-r/2) sum_{x,c} |x,c> P_{A(x;c)} |psi_x> |0_W>,
    2^(-r/2) sum_{x,c} |x,c> P_{f(x)}   |psi_x> |0_W>.

The input x and tape c distinguish mutually orthogonal summands. Unitary invariance of vector norm, including the final coin Hadamards, consequently gives

    error^2 = 2^(-r) sum_{x,c}
                ||(P_{A(x;c)}-P_{f(x)}) |psi_x>||^2.

Correct tapes contribute exactly zero. Every other term is at most 4||psi_x||^2, since the difference of two unitaries has operator norm at most two. Pointwise correctness on each promised x gives error^2 <= 4p and hence error <= 2sqrt(p). No common tape correct for all x is required. The exact finite control below has no such common good tape and attains this bound.

The computation workspace W clears exactly. The coin register need only be approximately restored to zero, in the vector-norm sense of the theorem. The stated comparison to all-zero ancillas is precisely what the above calculation proves. Calling the construction approximately clean must not be read as an assertion that the ancillas are exactly zero for p>0.

Mixed inputs are covered by purification into a larger untouched reference. Nothing in the derivation depends on the reference dimension, and those reference qubits are properly excluded from the resource count.

### Off-promise mass, measurements, and hybrids

Extend f to every relevant b-bit basis string outside P, including invalid strings if necessary; the program itself is total on all b-bit strings. If the actual off-promise squared mass is t<=tau, the same orthogonal decomposition gives the stronger inequality

    error^2 <= 4[(1-t)p+t] <= 4(p+tau).

This proves the displayed off-promise result even when p+tau>1; that bound is simply loose, and every vector difference is also at most two.

For normalized pure vectors u,v, their trace distance is sqrt(1-|<u,v>|^2), which is at most ||u-v||. This follows from |1-<u,v>|^2>=0. Trace distance contracts under any common quantum channel, and classical TV of any common measurement is at most trace distance. Thus the stated postprocessing/measurement bound follows. There is no assertion that the circuit error is the original classical p in TV.

For a sequence of replacements, expand the difference between the complete actual and ideal circuits using ideal prefixes and actual suffixes. In the j-th summand, the input to the differing query is exactly the j-th ideal query state; all prior query ancillas are ideal zeros and the new ancillary registers are fresh zeros. The single-call result therefore applies with p_j and the stipulated ideal-query off-promise mass tau_j. The common actual suffix preserves norm, so the triangle inequality gives

    total vector error <= 2 sum_j sqrt(p_j+tau_j).

This orientation of the hybrid is important: it requires no premise about the promise mass of an actual, already perturbed query state. Intermediate operations and reference entanglement are included in the global state; measurements can be purified if needed. The bound does not condition on a future successful event. For measurements it also yields a TV bound, capped trivially at one.

Negligible p gives negligible sqrt(p) for a single call: apply the defining bound for the square of any desired polynomial. A polynomial number of calls with a negligible total error budget is compatible with negligible accumulated error; an arbitrary superpolynomial number of calls is not covered by that inference. Merely supplying an inverse-polynomial or constant p is insufficient to certify negligible coherent error. Off-promise mass and all separately named approximation budgets must still be paid.

### Elementary gates and qubits

Allocate one initially zero workspace qubit for each Boolean gate's new wire, including the designated computed output wires as specified by S. An AND is computed by one Toffoli. An XOR is computed by two CNOTs. A NOT of an existing wire is computed into its fresh wire by one CNOT and one NOT. Constants, routing, padding, and output conventions must be included in the chosen Boolean circuit; they are not unspecified free numerical operations.

Thus B uses at most 2S elementary gates, B inverse uses at most 2S, copying uses m CNOTs, and the coin preparation/erasure uses 2r Hadamards. The total is at most

    4S + m + 2r.

There are b input, r coin, m target, and S work qubits, hence at most b+r+m+S qubits excluding the untouched reference. The target register is independent of the program workspace even if an output wire is also an input wire of the Boolean circuit. Copying into an arbitrary quantum target is valid CNOT action; it is not copying an unknown target state. Keeping all S work wires until the global uncompute is the reason no repeated cleanup of subroutines is needed.

For a standard bounded multitape bit-machine, one may unroll the all-input time cap, simulate the finite control and tape-head selection by Boolean gates, and pad the output. At most O(T+b+r+m+|code|) relevant cells/description bits are needed per layer, for at most that many layers, giving the stated conservative quadratic Boolean size in these numerical bounds under the usual fixed finite alphabet/tape conventions. The exact implementation determines S; the theorem does not give a universal small constant or a bit-complexity claim polynomial in log(T). An arithmetic instruction of unbounded precision cannot be treated as one finite gate: its given deterministic implementation and encoding bounds must enter T and S. Fixed r fair bits can be supplied as one padded tape even if the original program consumes a data-dependent prefix.

If the forward compiled computation has at most Q Rec executions, retain their coins, inputs, outputs, branch records, and intermediate wires. The forward computation then invokes those reversible computations at most Q times, and global inversion invokes their inverses at most Q times. Adaptive branch behavior requires the fixed bounded program to be compiled with coherent control/dispatch and totalized inactive cases; those gates are part of the chosen S. If Q denotes a runtime call bound, a finite implementation can arrange at most Q such call slots by bounded dispatch to the next call. The size of any chosen dispatch construction must be included in S; one must not assume an arbitrary naive branch expansion both preserves Q and realizes an independently quoted smallest S. The universal 4S+m+2r count is for the actual chosen circuit.

The call accounting is therefore valid as executable-circuit accounting. It is not a claim that an irreversible classical sampler, a remotely supplied classical answer, or a circuit with inaccessible garbage can be inverted. If one elects to clean and reuse Rec workspace at every call, additional forward/inverse executions may be needed; that is a different implementation from the all-wires-retained construction establishing the stated upper bound.

### Conditional C8 substitution and what is not established

Without reading C8, the following implication is valid: if the fixed finite program has the stated pointwise promised-target error at most p=(n/2)exp(-kappa)+zeta, and its chosen executable implementation has at most Q_*=Q Rec calls, substitute those quantities into the generic adapter. The forward/backward accounting yields at most 2Q_* coherent Rec executions. The stated fixed GP wrapper's one-Rec property is part of that application premise, not independently verified here. The supplied definition requires the resulting p to lie in [0,1]; if a numerical formula exceeds one, the usable error-probability bound can be capped at one but gives no useful small coherent error.

A fixed target-encoding bound and an all-input runtime cap are essential. A failure symbol can be mapped to a fixed padded output string; doing so cannot worsen the assumed correctness probability on successful inputs and provides a total Boolean output. Finite approximate numerical operations can be compiled because their implementations are fixed. None of this proves correctness or efficiency of an unspecified GP/Rec program, a promised-target reduction, rational-target coverage of a prepared quantum state, preparation of that state, or an ordinary DGS law. Gate approximation, truncation/aliasing, state preparation, and off-promise mass remain separate budgets. There is no standard-family hardness conclusion.

## Preserved falsification attempts and boundary counterexamples

These are retained as counterexamples to tempting weakenings or extensions. They are not counterexamples to the frozen statements, whose relevant exclusions are explicit. No repair to those exact probability statements is required by these controls.

### CP1: residual incidences cannot be multiplied

The exact supplied arithmetic is

    21/2000 - 1/100 = 1/2000 > 0,
    1/10 - 21/221 = 11/2210 > 0.

Thus the supplied selected-hit mass exceeds the proposed 1/100 product while the supplied second residual incidence is below 1/10. This rejects the claimed multiplication in that control. The definitions do not expose the original first-stage space, so these are the full original facts preserved here; the finite job checks them exactly. Neither reconstructed sequential proof multiplies marginal/residual hit rates. Both integrate the actual past-conditional law and take additive unions. The quantum hybrid likewise adds norm errors. CP1 therefore identifies no defect in these statements or reconstructions.

### Correlation, nonatomic histories, and uncharged acceptance

Take n=2, I=H=R=Z[i], c=1, W=8, gamma=0, m=2. Then b=1/64.

* If X_1=X_2=U with U distributed as D, both marginal laws are exactly D but the zero-difference event has probability one. This refutes replacing independence/complete-history conditional freshness by a marginal-law premise. The actual conditional second law is a point mass, so it does not satisfy eta_2=0.
* Let X_1=X_2=0 and include an independent uniform U on [0,1] in every complete history. All history atoms have probability zero. A test of conditional freshness only on positive-mass atoms would be vacuous and would incorrectly imply the same 1/64 bound on an event of probability one. The supplied regular-conditional premise instead sees delta_0 almost surely and fails, as it should. In fact TV(delta_0,D)=1-D({0})>=63/64.
* Keep X_1=0 and draw from D until a zero is found, reporting only that final accepted draw as stage 2. The eventual zero occurs almost surely because D({0})>0. This would again give success one if all rejected fresh values were erased from the attempt count. It violates both the conditional law of the accepted output and the explicit charge-every-generated-value rule. Bounded predictable attempts obey the proven union bound.

These examples preserve why the stated null-history, complete-law, and predictability qualifications are needed.

### Output-dependent choices and zero maps

Take n=2, I=H=R, c=1, W=8, gamma=1. The fixed-map bound is at most 9/64. With T equal to the identity, choosing y after seeing X as y=1-X yields the useful nonzero output 1 with probability one. The choice y=-X similarly forces zero with probability one. Both violate the requirement that y be fixed before its own fresh sample. This is a direct counterexample to an output-dependent extension, not a claim that the theorem rules out that extension.

Allowing T=0 and y=0 would also give norm success one. With y=1 it would give a fixed public nonzero short output one. This confirms the necessity of the displayed nonzero-map restriction and the distinction between outputting an existing public vector and obtaining information through X.

### Covariance does not determine the needed law

In the preceding Z[i] Gaussian at W=8, let v>0 be its one-coordinate variance. The exact centered law has covariance v times the identity. Choose an integer M with M^2>=4v. The finite distribution giving each of +/-M e_1 and +/-M e_2 mass v/(2M^2), and giving zero the remaining mass 1-2v/M^2, has exactly the same mean and covariance. Its zero atom is at least 1/2, exceeding the gamma=0 bound 1/64. The algebra is exact and no numerical value of v is needed. This refutes deriving the theorem from covariance alone; the theorem itself insists on the entire Gaussian/TV law.

### Fractional support and an out-of-J first center

An allowed out-of-J first sample need not make every pair event empty. Take n=2, I=R, H=3R, c=2, so J=(3/2)R. Let X_1=(1/2,0), W=8, gamma=1/2. Then X_1 is outside J, yet X_2=(3/2,0) gives difference (1,0) in I of norm one. It is the only reference-lattice point satisfying the event: writing X_2=(3k/2,3l/2), integrality requires k odd and l even, and the radius-one condition leaves k=1,l=0. Its probability is

    exp(-9pi/256)/rho_8((3/2)R).

Since det(J)=9/4, it is at most 9/256. The displayed theorem bound is b=81/256, so the example is consistent and verifies the need for ambient-space sections rather than a tacit X_1 in J assumption. A label implementation rejects the first value; the direct difference implementation can test it.

For approximate samples, (1-eta)D+eta delta_v with v outside J has TV eta from D. The fixed-map convention returns failure at v, and direct pair testing remains defined there. In particular, with X_1=v the fresh contamination atom can create the zero difference with probability eta. A TV charge cannot be silently discarded by claiming all sampled values belong to J.

### Pointwise quantum correctness and square-root loss

Let x and c each range over {0,1,2,3}, f(x) be its low bit, and A(x;c)=f(x) XOR 1[c=x]. Each x has error p=1/4, but every tape c fails for x=c. There is no tape correct on all x. On the normalized state proportional to

    sum_x |x> (|0>-|1>) |x>_reference,

the squared vector error is 4p=1. Thus the 2sqrt(p) bound is attained, and a generic vector error bound of 2p would be false. The exact circuit control verifies this claim without floating-point arithmetic.

Average correctness over classical x would be insufficient. With two inputs, no random coins, f=0, A(0)=0 and A(1)=1, the uniform-average error is 1/2. The query concentrated on x=1 with target |-> has vector error two, greater than 2sqrt(1/2). The frozen theorem assumes correctness for every promised x and avoids this counterexample.

Similarly, if the program is correct everywhere on the promise but flips the target for one off-promise input carrying squared mass tau, the same |-> calculation gives squared vector error 4tau. Off-promise amplitude must be charged on a square-root scale in general. No additional numerical job is needed for these exact symbolic vector identities.

## Reserved finite controls and original records

Root granted BT15-FV1 for one foreground job with a 10-second wall cap, a 64-MiB address-space cap, and at most four input values times four tapes. No other finite job ran. The code uses only Python's standard library and Fraction arithmetic, is exhaustive, and has no random seed. Unnormalized rational state vectors are divided by their exact squared input norm; this avoids approximate square roots while giving exact normalized squared errors. The reference register is retained explicitly in the state keys. Hadamards on two coin qubits are implemented as their exact rational 4-by-4 Walsh matrix.

The single job performed:

* The exact CP1 arithmetic above.
* A pointwise-p=1/4 adapter with no common good tape, obtaining squared error 1 and saturating the theorem.
* A target/reference-entangled input with unnormalized amplitudes 3 and 4, squared input norm 25, obtaining normalized squared error 1/2 <=1.
* An off-promise case with p=tau=1/4, obtaining squared error 7/4, equal to the sharper 4[(1-tau)p+tau] and below the stated squared bound 2.
* Boundary controls p=0 and p=1, obtaining squared errors 0 and 4.
* An explicit six-Boolean-gate implementation of the equality-based answer, with 11 forward elementary gates, 27 total gates including copy and Hadamards, and 11 non-reference qubits. The stated upper bound is 29 gates. All 32 combinations of four inputs, four tapes, and two target basis values were checked for unchanged input/tape, correct XOR action, and exactly cleared Boolean workspace.
* A separate four-point uniform-law conditioning control. X_1=0; the second and attempted third laws each have exact TV 1/16 from uniform; the third attempt is omitted predictably if stage 2 already hit. The exact success is 179/256 <= 7/8 = 3*(1/4)+2*(1/16). The iid three-draw collision probability is 5/8. This control tests additive TV and predictable attempts, not the Gaussian geometry.

The foreground job exited 0 and printed `ALL_EXACT_CONTROLS_PASS`. Original stderr is empty. `/usr/bin/time -v` recorded 0.02 seconds elapsed, 0.01 seconds user time, 0.00 seconds system time, and peak RSS 12,288 KiB. The shell enforced `ulimit -v 65536` and `timeout --signal=KILL 10s`. No installs, network calls, detached descendants, or external data were used. The complete invocation is preserved in the command artifact.

| Artifact | SHA-256 |
|---|---|
| `control-v1.py` | `437776603ae9ac4c27d0966a34ec8075b37cb741dad8ad85d7bfcfbc22f3b6ef` |
| `control-input-v1.json` | `5b206ad15b64d8f764fe1ee22713f844bdc37eb49cd393da9a43454e3f47f944` |
| `control-command-v1.sh` | `7f2f769f8206326b6e43edf89ad2bfd93dd7f23a867518deb5303d05ac7b9255` |
| `control-stdout-v1.txt` | `09a73375813fe41c2f6afc92470eb62eed4431342a660eb1576c4d62bfe135f7` |
| `control-stderr-v1.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `control-resources-v1.txt` | `a4ade96f1f9da6d60a212ef3ea61c8e523eac453180e19e83e8773129889d536` |
| `control-exit-v1.txt` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |

## Final claim ledger and limitations

| Claim | Result of this reconstruction |
|---|---|
| Pair theorem (1), exact independent samples | Proved from uniform affine-coset packing, the exact centered Gaussian normalizer, and a pair union bound. |
| Pair theorem (3), adaptive/approximate attempts | Proved from measurable history sections and one conditional TV payment per attempted stage. Arbitrary first law and nonatomic histories are covered. |
| Pair selectors, zero differences, quotient labels, and ambient output domain | Checked explicitly; successful selectors are contained in the stated event, and out-of-J behavior is well-defined. |
| Pair constants and zero-error sample lower bound | Algebraically verified as stated. |
| Fixed nonzero R-linear extraction with prior map/translate | Proved by injection into a separated ideal and the same maximum-atom bound, including zero outputs. |
| Fixed-map TV and successive attempts | Proved by conditional sections and additive union bounds. Output-dependent maps/translates and unbounded trials are not covered. |
| Fractional-ideal context identities and natural modular reduction | Algebraically justified; no source-hardness or reduction claim follows. |
| Generic coherent adapter, arbitrary target/reference | Proved by orthogonal x/tape decomposition; finite exact controls include saturation and entanglement. |
| Off-promise error, measurements, multi-call hybrids | Proved; the ideal-prefix hybrid uses only ideal-query promise masses and fresh ancillary registers. |
| 4S+m+2r gates and b+r+m+S qubits | Proved for the actual explicit Boolean circuit with all computation wires retained. |
| Bounded-machine unrolling and Rec resource accounting | Valid in the stated executable bit-program model, with the chosen construction and dispatch overhead included in S; not an oracle-service conversion or a log(T)-complexity bound. |
| C8 error/call substitution | Conditional implication only. No C8/GP implementation, correctness premise, or target-state premise was inspected or certified. |
| Gaussian state preparation, ordinary DGS output, and standard-family hardness | Not proved, assumed, or experimentally supported by this review. |

The remaining application work cannot be supplied by these statements alone: it would need the actual bounded executable programs, their pointwise promised-target guarantees and bit bounds, the required quantum query state with controlled off-promise mass, and the downstream output-law/error accounting. No requested assertion beyond the frozen scope has been adopted. All negative examples above are preserved before any possible later amendment; they show the necessity of scope restrictions rather than a need to amend these exact displayed bounds.
