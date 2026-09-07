# W2 structural results, version 1

Author: `/root/w2_structure`, assigned Astra / ultra. No session or thread UUID is exposed by the available interface; none is invented. Assignment: [assignment.md](assignment.md). All new claims below are **PROVISIONAL**, awaiting nonauthor review. Same-model review would be complementary mathematical review, not statistical independence. No policy interruption occurred in this worker.

The bounded result is a constant-parameter refinement of the grouped-orbit attack, a matching obstruction to using subfields of degree o(d) within that method, an exact limit on scalar cancellation using the second component, and a one-way search reduction from a separately defined average-case PV-Knap problem. These results do **not** give a polynomial distinguisher for exact A2, an exp(o(d)) attack, or independent decisional support for P0-A2.

## 1. Frozen law, input precedence, and inherited scope

The active `target.md` and `inputs/SOURCE_CONTRACT.md` take precedence over the consolidated ledger, which takes precedence over pre-correction author notes. The common regime is one sample, n a sufficiently large power of two, ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2, tau=ell, sigma=2n ell^3, and split prime sigma*n^c<=q<=n^K for fixed c>0,K and a nonempty qualifying parameter sequence. The ring is R_q=F_q[X]/(X^n+1), in its coefficient basis. All algorithms receive public n,q and the ring representation. The generic arbitrary-q attack additionally receives the complete CRT roots or a primitive 2n-th root. A2's fixed polynomial upper bound on q permits deterministic field enumeration in its polynomial factor; this is not a generic poly(log q) root-finding claim.

T is a uniform d-subset of the n roots. Conditional T, U has iid uniform nonzero CRT values on T and zero elsewhere, while V is independently uniform in the ideal I(T), including zero active values. F is independent of T,U,V and has independent D_ell coefficients conditioned on [-b,b], with D_s(z) proportional to exp(-pi*z^2/s^2). Given F, form B_F=sigma^2 I-tau^2 M_F M_F^T. In coefficient order use the unique unit-lower LDL decomposition B_F=L diag(v_i)L^T, and sequentially sample

    c_i = sum_{j<i} L_ij y_j,
    Pr[h_i=z | h_<i,F] proportional to exp(-pi*(z-c_i)^2/v_i),
    y_i = h_i-c_i.

Fresh coins, independent of T,U,V conditional F, define H_seq(F). Only (A,C)=(U+F,V+H_seq) modulo q is public. H_seq is neither replaced by D_B nor by independent isotropic noise here. No argument uses the bridge's binary S or auxiliary G, and no extra sample is produced.

The inherited ATT v3 is deterministic exp(O_c(d))*poly(n,log q), with every planted first-component input accepted and negligible uniform acceptance. Its strict radius and nonzero exact-SVP vector are essential. The imported uniqueness criterion

    2b<q,                    q^(1-2d/n)>2b*sqrt(n)           (U)

determines F, and then T because U is active, but supplies no efficient decoder. Both inequalities hold eventually in the common regime. Fixed nontrivial additive pair characters and polynomial-l1 fixed combinations have negligible bias under the actual conditional noise law; that result does not control arbitrary or adaptive tests. The first marginal still has statistically tiny support. These statements are imported with the consolidated ledger's provisional review status, not newly certified here.

The requested mathematical packet, both audit protocols, and applicable complete historical controls were read. `claims.json` was parsed in full and its current and historical mathematical statements inspected; this is not a re-audit of every unrelated dependency. [input-hashes.json](input-hashes.json) records load-bearing byte reads. The main text read before the initial hash pass was re-read in that byte pass. Web-source hashes identify the returned web representation, not original PDF bytes.

## 2. W2-ORB-v1: random occupancy improves the admissible orbit constant

**Finite statement.** Let n be a power of two, q split and odd, b>=1 integer, 1<=d<n, and r a power-of-two divisor of n. Fix an integer k with 1<=k<=r such that

    q^k > (2nb)^r.                                         (O1)

Choose any public subgroup H of the n-element cyclotomic Galois group with index r. Its regular action gives r root orbits, each of size h=n/r. For a uniform d-support T let E be the number of orbits that T does not meet. There is a deterministic first-component test with time exp(O(r))*poly(n,log q,log b), exponential memory allowed, such that

    Pr_planted[accept] >= Pr[E>=k],
    Pr_uniform[accept] <= min(1, (2b+1)^n
                                      sum_{j=k}^r C(r,j) q^(-jn/r))
                       <= min(1, 2^r(2b+1)^n/q^(kn/r)).     (O2)

The planted guarantee holds for every F in the coefficient box and every active value U once T has the required empty orbits. Hence it applies to the exact A2 law, independently of the complete second component. It does not require r>=2d.

**Complete algorithm.** Enumerate every union Omega of at least k H-orbits. Form the integer ideal L_Omega of polynomials vanishing modulo q on Omega, and its integral complementary ideal D=q L_Omega^{-1}. For t=|Omega|, D has norm q^(n-t), is unramified, contains q O, and is H-stable. Compute its full stabilizer and the integer lattice D intersect K_D in the fixed field. Its rank s is at most r. Use the deterministic exact-SVP policy of corrected ATT v3 on its rectangular integer coefficient basis, then lift its nonzero vector v to w=v/q in L_Omega^{-1}. The inherited lifting and normalization calculation gives

    ||Sigma(w)||_2 <= n q^(-t/n).

For each j=0,...,n-1 take the coefficient dual row coeff(conj(X^j w)), round its inner product with an integer lift of A, and solve the resulting independent rational linear system. Return the candidate F' after checking that every coefficient is integral and in [-b,b], and that A-F' belongs to L_Omega. Accept if any branch verifies. Optionally also check that A-F' has at most d active CRT coordinates; this retains every promised branch and will be used in W2-COVER-v1's stronger scope statement.

Every dual error measurement has magnitude at most

    b ||Sigma(w)|| <= nb q^(-t/n) <= nb q^(-k/r) < 1/2.

Thus if Omega is disjoint from T, rounding exactly recovers the L_Omega point A-F, and the branch accepts. If E>=k such a branch is enumerated. The r>=2d hypothesis in the original statement was used to guarantee a sufficiently large zero set for every support; it is not needed by the branch's algebra or solver. A uniform A has a uniform coset modulo L_Omega among q^t choices. At most (2b+1)^n of those cosets have a box representative, regardless of off-promise behavior. Summing this bound over orbit unions proves (O2). The algorithm and its uniform false-positive proof use no product of adaptively conditioned event probabilities.

**Exact occupancy law.** Define C(a,d)=0 if a<d or a<0. Then

    p1 = C(n-h,d)/C(n,d),      p2 = C(n-2h,d)/C(n,d),
    mu = E[E] = r p1,
    Var(E) = r p1(1-p1)+r(r-1)(p2-p1^2) <= mu.             (O3)

Indeed p1 is the probability of avoiding a fixed orbit and p2 that of avoiding two. When n-2h>=d, termwise comparison in the falling-factorial products gives

    1-2h/(n-i) <= (1-h/(n-i))^2,  0<=i<d,

and hence p2<=p1^2. Otherwise p2=0. This proves the variance bound; independence of empty-orbit indicators is not assumed. In particular, if mu>k,

    Pr[E<k] <= min(1, mu/(mu-k)^2).                        (O4)

The exact finite distribution, useful even when (O4) is vacuous, is

    Pr[E=e] = C(r,e) [x^d] ((1+x)^h-1)^(r-e) / C(n,d).    (O5)

It follows by choosing the empty orbits, then choosing a nonempty subset from every other orbit. The saved dynamic program counts these same choices with integer arithmetic; exhaustive support enumeration cross-checks tiny cases.

**Common-regime consequence.** Choose a fixed rational alpha with 1/(1+c)<alpha<1 and a fixed a>1/ln(1/alpha). Let r be the least power of two at least a d and k=ceil(alpha*r). Eventually r divides n, r=Theta(d), and (O1) follows from q>=2n^(1+c)ell^3. Since d^2/n=o(1), sampling without replacement differs from d independent root draws by at most d(d-1)/(2n)=o(1). Therefore

    mu/r = exp(-d/r)+o(1) >= exp(-1/a)+o(1) > alpha.

Equation (O4) now gives planted acceptance at least 1-O(1/d), while (O2) gives uniform acceptance exp(-Omega_c(n log n)). Time remains exp(O_c(d))*poly(n,log q). For c=1 one may take alpha=2/3 and a=3: exp(-1/3)>2/3. This allows r in [3d,6d), whereas the inherited sufficient constant C0>=8 gives r in [8d,16d). This is an improvement of sufficient orbit/rank parameters only. Hidden O-constants preclude a concrete runtime or bit-security claim, and no exp(o(d)) consequence follows.

## 3. W2-COVER-v1: all small fixed fields still miss random supports

**Finite statement.** For any 0<alpha<1 and integer rmax>=1, let F_alpha,rmax be the family of all root sets Omega of size at least alpha*n which are stable under at least one subgroup of G=(Z/2nZ)^* of index at most rmax. With ell=log2 n and uniform d-subset T,

    Pr[exists Omega in F_alpha,rmax: Omega intersect T = empty]
      <= min(1, n^ell * 2^rmax * (1-alpha)^d).             (C1)

This bound includes the whole family before any algorithm sees A,C. Therefore adaptive selection using the entire public pair does not escape it as long as the chosen zero set remains in that family.

**Proof.** A subgroup of a group of order n=2^ell has a generating list of length at most ell: adjoining an element outside the current subgroup at least doubles its size. Padding with identity gives at most n^ell subgroups. The regular root action of an index-r subgroup has r orbits, so at most 2^r invariant sets. For any fixed Omega of size t>=alpha*n,

    Pr[T avoids Omega] = C(n-t,d)/C(n,d)
                        <= (1-t/n)^d <= (1-alpha)^d.

A union bound proves (C1). Neither failure-conditioned support laws nor local independence is used.

**Application to corrected ATT's strict gap.** Any promised branch satisfying q^(t/n)>2nb under q<=n^K has t/n>1/K. Set alpha=1/K in (C1). At A2, d/ln^2 n tends to infinity. If rmax=o(d), the right-hand side is exp(-Omega_K(d)), hence negligible. Consequently with overwhelming probability **no** strictly decodable, unramified split-prime branch with fixed-field degree at most rmax exists, even allowing every subgroup and an omniscient choice from that family.

The statement is about these branch promises, not general ideal decoding. For the optional fully verified version of the algorithm in Section 2, the implication is stronger: under (U), any accepted F' with support(A-F')<=d must be the actual F. Its congruence modulo L_Omega then forces Omega to avoid T. Such branch-based algorithms restricted to fixed-field degree o(d) therefore have negligible planted acceptance, even if their branch choices use C. This does not constrain algorithms using short vectors outside those fixed fields, different lattices, different public functions, or a decoder which bypasses the branch structure. It is not a computational hardness theorem.

The tiny n=8,d=2 control has coverage one when all index<=2 subgroups are allowed. This is compatible with (C1), whose bound is then vacuous, and rejects any attempt to replace the asymptotic hypotheses by a blanket finite r<=d claim. Rich supports are never replaced by the retired binomial support family.

## 4. W2-SCAL-v1: the exact second component does not give bulk scalar cancellation

Consider the fully public operation

    B_t = C-tA = (V-tU)+(H_seq-tF) mod q,   t in F_q.      (S1)

All q scalar choices can be enumerated in polynomial time at A2. This operation changes the noise and active-coordinate laws; no resulting B_t is silently treated as an A2 sample. We investigate only whether the ideal term loses a substantial part of its support.

For each active root i define R_i=V_i/U_i. Conditional on every T,U,F,H, the d ratios are independent uniform F_q values, because V is independent uniform in I and each U_i is nonzero. Thus

    |support(V-tU)| = d-N_t,   N_t=|{i in T:R_i=t}|,
    Pr[max_t N_t>=k | T,U,F,H]
        <= min(1, C(d,k) q^(1-k)),  1<=k<=d.              (S2)

For a fixed t and fixed k roots, the equality event has probability q^-k. A union over q scalars and C(d,k) root subsets proves (S2). The result holds even if t is chosen after seeing the complete public pair, or even the latent tuple: max_t already includes every choice. The F-dependent H_seq kernel is retained exactly and no moment approximation enters.

For d<=q, the exact no-collision probability is (q)_d/q^d. Hence

    Pr[max_t N_t>=2] <= d(d-1)/(2q)
                      <= 1/(4 n^c ell^11)                (S3)

at the common parameters. This is an o(1), inverse-polynomial bound; it is **not** asserted negligible. On its complement, every scalar shear leaves at least d-1 active coordinates. For every fixed delta>0, taking k=ceil(delta*d) in (S2) gives exp(-Omega_{c,delta}(d log n)) probability of cancelling a delta fraction. Thus this mechanism cannot decrease d to o(d) with nonnegligible probability. Exceptional double cancellations do not change the exp(O(d)) scale.

This is a scoped failed approach, not an exclusion of all uses of C. In particular it does not rule out a test exploiting the conditional joint noise by a nonlinear operation, ring multipliers with independently varying CRT values, or an improved decoder. A ring multiplier interpolating the ratios is an additional hidden-data problem; the scalar calculation does not make it publicly known. The test also cannot read an unwrapped covariance of F,H from centered A,C.

## 5. W2-PV-v1: a noncircular search reduction, with its direction explicit

Define the separate **average-case known-support PV-Knap search experiment** PV(n,q,d,psi): choose Omega uniformly among (n-d)-subsets of the public roots; sample F from psi=D_ell^n conditioned coefficientwise on [-b,b], independently; give the solver Omega and the values (F(r))_{r in Omega}; require recovery of the actual integer vector F. There is no binary secret and no second noise component in this problem. In ideal notation the input is F mod L_Omega. Its canonical error bound is nb, so

    q^(1-d/n)>2b sqrt(n)                                  (P1)

is the strict uniqueness condition. It holds eventually in the common regime. The choice of random Omega and the exact truncated psi are specified here; no checked paper is claimed to prove hardness of this parameter distribution.

Let Rec be any public algorithm which, given only A from the exact A2 first marginal, recovers its planted F with average probability epsilon. Then PV(n,q,d,psi) has a solver of time time(Rec)+poly(n,log q), with the same root-input convention, and success at least

    (1-1/q)^d epsilon.                                    (P2)

**Reduction.** Given Omega,y, set A(r)=y_r on Omega. Fill A(r) independently uniformly in F_q on the complementary d roots, then inverse-CRT interpolate A. Run Rec(A). Check its output is an integer box vector with the supplied evaluations y, and return it if so. Under (P1) every verified output is the actual F.

For analysis only put T=Omega^c and U=A-F. The simulated U is uniform in I(T), including zeros. Let E_active be the latent event that all its active coordinates are nonzero. Conditional on T,F its probability is exactly p0=(1-1/q)^d, independent of those values. Conditioning on E_active therefore gives precisely the active A2 first marginal with its original T,F prior. Consequently

    Pr[Rec(A)=F] >= Pr[E_active and Rec(A)=F] = p0 epsilon.

The reduction neither detects E_active nor samples F. It uses an exact positive-event lower bound, not an uncharged negligible-TV substitution. At A2, p0>=1-d/q tends to one. If finite worst-case runtime over unbiased bits is required, cap each uniform-field rejection sampler at n trials and fail on overflow; the additional success loss is at most d*2^-n. All root interpolation and integer checks are polynomial. There are no Gaussian sampling costs inside this reduction because the PV challenge supplies the F-dependent evaluations.

The direction is

    average known-support PV search <= active first-marginal recovery.

Thus a hardness assumption for this separately specified PV search experiment would rule out a first-component recovery algorithm. It would **not** prove decisional P0, nor rule out recovery using the entire pair. An exact A2 pair simulator from the PV input still needs the hidden F to form B_F and its adaptive H_seq centers. Uniqueness is not such a simulator.

Conversely, a first-component recovery algorithm does give a source distinguisher: verify the box and that A-F' has at most d nonzero CRT values. Its source acceptance is at least epsilon, while uniform acceptance is at most

    delta_box = min(1, (2b+1)^n/q^n
                           sum_{j=0}^d C(n,j)(q-1)^j),     (P3)

which is exp(-Omega(n log n)) at A2. This is recovery-to-decision only. No converse for an arbitrary nonlinear exact-pair distinguisher is proved.

## 6. Reproducible evidence and mandatory controls

Experiments used only installed Python 3's standard library, one process at a time in slot W2-E, exact integers and `Fraction`, no seed, and an external 120-second timeout. No Gaussian approximation, remote computation, exact-SVP implementation or practical parameter benchmark was run. Toy n,d values test universal combinatorial/algebraic statements and are explicitly not finite realizations of the canonical asymptotic d(n), which is zero at small n.

| Record | Exact scope | Result |
|---|---|---|
| [W2-E-01-v1](data/structural_controls.json), [code](code/structural_controls.py) | 13 occupancy distributions; exhaustive support comparison for n=8,16; variance and coverage inequalities | All assertions passed. |
| Same record | All 73,984 active-U/uniform-V pairs at q=17,d=2 induce 289 equiprobable ratio vectors | Exactly 256 preimages per ratio. Maximum scalar cancellation is 2 with probability 1/17 and 1 with probability 16/17. |
| Same record | n=4,q=17, roots (2,8,9,15); all six d=2 supports, all 289 ratio vectors and all 17 scalars | 29,478 public ring shear identities passed, for explicitly fixed F,H. Identities are pointwise and need no H-law replacement. |
| Same record | n=2,q=17,d=1, every tested F in {-1,0,1}^2, both supports, all missing-coordinate fills | Active-event probability 16/17; exact conditional uniformity. This is pointwise in F and does not approximate its Gaussian weights. |
| [W2-E-02-v1](data/subgroup_controls.json), [code](code/subgroup_controls.py) | Every subgroup of the n=8 and n=16 Galois groups and every qualifying orbit union | At n=16,d=4,alpha=1/2, coverage is 103/455 for index<=2 and 33/65 for index<=4. At n=8,d=2,index<=2, coverage is 1. |
| Same record | All 5^4 iid ratio vectors over F_5 | Pr[max multiplicity>=3]=17/125<=4/25; Pr[max>=4]=1/125, matching (S2)'s last bound. |

For occupancy alpha=1/4, n=256,d=16 gives success about .1950 at r=8 and .9542 at r=16. At n=1024,d=32 it is about .0844 at r=16 and .9887 at r=32. These decimal renderings summarize exact stored rational counts; no asymptotic theorem is inferred from them.

The historical n=2,q=17 dual-rounding control was reproduced exactly: measurements 54/17 and -22/17 round to 3,-1 and recover F=(1,1). Strict radius is checked by 17>16 after squaring; equality is never allowed. The n=8 two-orbit exponent control was reproduced. CP-1 again yields 21/2000>.01. The new probability arguments use finite counting, a variance identity, and union bounds, so they do not revive CP-1's failed conditional product inference.

The rich-versus-binomial control remains live: these algorithms average over all d-supports and do not assign a binomial polynomial to the source. Active-unit conditioning is charged as the exact event p0 in (P2); the nonnegligible d/q total-variation issue is not discarded. Uniqueness is used only for verified recovery/coverage conclusions, never as a polynomial solver. Uniform marginals do not imply joint pseudorandomness; C is treated in (S1)-(S3) with its actual conditional law. Fixed-character suppression does not erase the support bound (P3). All these controls remain in the coordinator registry, which this worker did not edit.

Reproduction commands, from the project root:

    timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/workstreams/W2/code/structural_controls.py
    timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/workstreams/W2/code/subgroup_controls.py

## 7. Primary-source check and review boundary

The primary [Boudgoust–Gachon–Pellet-Mary paper](https://eprint.iacr.org/2022/709.pdf) was checked at Definition 2.14, Theorem 3.2/Lemma 3.3, Section 3.2, and Corollary 4.2. These supply the known-ideal problem, unramified stabilizer lifting, effective integer-basis operations, and the strict inverse-ideal decoding interface. The random-support occupancy and hidden-support coverage statements above are this worker's deductions, not attributed theorems of that paper. Its discussion of random known root sets does not reveal A2's hidden T.

[Micciancio–Voulgaris, Section 2 and Corollary 5.5](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download) supplies deterministic single-exponential exact SVP. The rectangular integer input and polynomial dependence on ambient dimension/bit length were checked explicitly. This is the same solver policy as corrected ATT v3; no success rate is assigned to the historical unspecified probabilistic policy. Exact primary response representations are saved in [sources/primary-response.json](sources/primary-response.json).

The strongest objection is the distinction between a method barrier or search reduction and the requested computational conclusion. W2-COVER-v1 covers only stable zero-set branches; W2-SCAL-v1 covers scalar ideal cancellation; W2-PV-v1 has a recovery hypothesis and cannot turn arbitrary exact-pair decision advantage into PV recovery. None closes P0.

The smallest useful remaining reduction lemma is a public procedure which, from the known-support PV challenge (Omega,F mod L_Omega), uses any exact A2 **pair distinguisher** of advantage epsilon to recover F with probability poly(epsilon,1/n), preserving the precise active-U and H_seq laws or proving an advantage-preserving comparison. The current completion step needs F itself. A public simulator or a justified decision-to-recovery mechanism would be new content; naming this PV problem is not that lemma.

For the algorithmic route, a polynomial or exp(o(d)) improvement must leave the enumerated small-fixed-field zero-set mechanism or exploit a different structure. The low-degree modular recurrence idea was triaged against the inherited control: its field-valued coefficients amplify dense integer noise, so noiseless Prony/Berlekamp–Massey recovery is not a noise-tolerant algorithm. It was not developed into a third mechanism or benchmarked. No claim of general algorithmic impossibility follows.

Changed claim IDs for integration: **W2-ORB-v1, W2-COVER-v1, W2-SCAL-v1, W2-PV-v1**. Dependencies: exact T0/A2, corrected ATT v3 for ORB, imported UNIQ only for the strengthened verified-COVER implication and PV verification. New elementary counting arguments and both finite experiments remain provisional. No earlier claim or coordinator file was modified. A fresh nonauthor recheck is required before any amended claim receives a stronger disposition.
