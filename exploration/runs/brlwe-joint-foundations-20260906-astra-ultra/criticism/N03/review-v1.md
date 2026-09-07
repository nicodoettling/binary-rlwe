# N03-v1 — completed bounded nonauthor W2 review

**Disposition:** the exact finite ORB, COVER, SCAL and PV statements pass this bounded mathematical review within their stated hypotheses. The ORB constant example needs the explicit qualification below. The coordinator's claims remain **PROVISIONAL**, because this review does not close the global dependency graph or certify computational P0. No polynomial distinguisher, exp(o(d)) algorithm, or independent decisional hardness foundation has been proved by W2.

Reviewed proof: `inputs/frozen/W2-final-v1-note.md`, SHA256 **6fdaef8bd1f4aa648bd6e00cc0f443120eba0fad274e074d9f927348b4ea013f**, 24,542 bytes. This exact hash applies to all four verdicts below. No author proof or coordinator file was edited. This is a fresh nonauthor but **nonblind** review, using the same model/context lineage; agreement is complementary review, not independent statistical evidence.

## 1. Assignment, exact inputs, scope and metadata

The full assignment is preserved in [assignment.md](assignment.md). Deadline: **2026-09-06T21:19:15Z**, with no extension. First observed UTC: 20:51:14Z. Assigned model/effort: gpt-6-astra / ultra. Observed environment values, without inference:

- CODEX_THREAD_ID: `01a0787d-2178-70b0-beb4-a255a21099c4`.
- CODEX_SESSION_ID: `01a07849-2b26-7ac1-96c2-c15903ac2341`.

Read the mathematical-proof-audit skill and both its audit and probability protocols. Exact file paths, SHA256 values and sizes are in [input-hashes.json](input-hashes.json). Current claims/reconciliation/regressions were captured at **2026-09-06T20:52:53.579492+00:00** in [inputs](inputs/); these administrative files can subsequently change, so verdicts identify that snapshot. All nineteen complete `imports/regressions` packets were read; their bytes match every `complete_evidence_packets` hash in the registry. Both author experiment programs and their saved data were inspected, and the data's code-hash fields match the actual programs. Author experiments were not rerun in their read-only directories.

Precedence is frozen target/source contract, then versioned ledger, then author notes. The task is academic theoretical cryptography on synthetic distributions, **m=1**. Common-K/multiple-sample work was not opened. No agents, remote workers, services, package installation, goal tools or alternative source model were used. Public primary PDFs were read through built-in web; records are [primary-sources-v1.json](primary-sources-v1.json). These hashes identify returned representations, not PDF bytes.

An intake archive omission was corrected on the coordinator's instruction: [assignment-archive-v1.md](assignment-archive-v1.md) retains the originally saved file; `assignment.md` now contains `inputs/RESEARCH_SCOPE.md` verbatim. The received assignment and mathematical premise never changed. Two short read-only intake commands were submitted concurrently before all later commands were serialized; no numerical experiment was concurrent. The sole numerical process was N03-E-01-v1, under external timeout 120 seconds and an internal earlier deadline. No content-policy interruption occurred, and no retry or continuation around such an interruption occurred.

## 2. Frozen mathematical model and dependencies

For sufficiently large powers of two n, let ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2, tau=ell, sigma=2n ell^3, and choose an odd fully split prime with sigma*n^c<=q<=n^K, for fixed c>0,K along a nonempty qualifying sequence. The ring is F_q[X]/(X^n+1), represented in the coefficient basis. The canonical embedding satisfies ||Sigma(f)||=sqrt(n)||coeff(f)||. Public generic arbitrary-q ORB input includes the CRT roots or a primitive 2n-th root; A2 allows polynomial-q deterministic enumeration. No generic deterministic poly(log q) root-finding result is inferred.

T is a uniform d-subset of the roots. Conditional on T, U has independent uniform **nonzero** values on T and zeros elsewhere; V is uniform on the ideal I(T), independently of U and the noise. F has the exact independent coefficient D_ell law conditioned on [-b,b], independent of T,U,V. Conditional on F, H is sampled using the fixed unit-lower LDL rule for sigma^2 I-tau^2 M_F M_F^T, with its adaptive scalar centers and fresh coins independent of T,U,V. The public pair is (A,C)=(U+F,V+H) modulo q. H is never replaced by D_B or by isotropic independent noise in this review. Every finite control involving fixed F,H establishes an algebraic or conditional statement pointwise; it is not an approximation of the A2 noise law.

The finite claims use the exact statements in Sections 2–5 of the frozen proof. Quantifier order is crucial: ORB fixes a public subgroup and branch family before drawing T; COVER ranges over the entire subgroup-invariant family before any selection; SCAL bounds the maximum over **all** q scalars before an adaptive choice; PV quantifies over any public first-component recovery algorithm with its independent tape and total runtime bound. All success probabilities average over the specified original planted witness. No efficient decoding follows from uniqueness alone.

| Author version | Coordinator version | Load-bearing dependencies | Local final disposition |
|---|---|---|---|
| W2-ORB-v1 | W2-ORB v1 | Exact A2 first marginal; corrected ATT v3 deterministic solver, public root input, lifting/norm and strict rounding; elementary occupancy | **PASS within scope**, with N03-O1 comparison qualification. Global PROVISIONAL. |
| W2-COVER-v1 | W2-COVER v1 | Uniform T; regular group action; fixed-family union bound; q upper bound for ATT application; UNIQ v1 only for strengthened verified-acceptance implication | **PASS within scope**. Global PROVISIONAL. |
| W2-SCAL-v1 | W2-SCAL v1 | Exact active-U and independent-uniform-V joint law; F-dependent H retained; elementary occupancy of ratios | **PASS within scope**. Global PROVISIONAL. |
| W2-PV-v1 | W2-SEARCH v1 | Exact first marginal and specified PV challenge; strict known-support norm uniqueness; public fill/interpolation; positive-event conditioning | **PASS within scope**, search direction only. Global PROVISIONAL. |

No W2 claim depends on computational P0 for its mathematical validity, and none proves P0. Changing ATT invalidates ORB's algorithmic conclusion; changing uniqueness reopens verified COVER and PV's verified-original-witness statement; changing active-U/V or H independence reopens SCAL and exact active-event PV transfer. The elementary COVER family bound does not depend on UNIQ, ATT's success policy, or the H sampler.

## 3. ORB: occupancy, exact dual rounding and constants

For integer 1<=k<=r with q^k>(2nb)^r, any chosen union Omega of at least k orbits has t=|Omega|>=kn/r. Its complementary integer ideal D=qL_Omega^(-1) is integral, unramified, has norm q^(n-t), contains qO, and is fixed by the orbit subgroup. Computing the full stabilizer can only decrease its fixed-field rank s from r. Exact nonzero SVP in the rectangular coefficient lattice D intersect K_D is appropriate: on that subfield, ||Sigma_K_D(x)||=sqrt(s)||coeff_K(x)||, a fixed scalar conversion.

The inherited lifting bound yields a nonzero w=v/q in L_Omega^(-1) with ||Sigma(w)||<=n q^(-t/n). For d_j=coeff(conj(X^j w)),

    <coeff(z),d_j> = Trace(z X^j w)/n in Z,  z in L_Omega.

The equality to the constant coefficient in the power-of-two power basis justifies the division by n. Nonzero w lies in a number field, so its multiplication map is invertible and all n rows are independent. With |F_i|<=b, every dual error is at most b||Sigma(w)||<=nb q^(-t/n)<1/2. The inequality is strict; the algorithm rounds the correct integer measurements, solves a nonsingular rational system, and verifies the resulting box vector. A q-multiple change of the representative changes the lattice point, not recovered F. The full rank and strict radius controls both pass; a zero vector or an exact 1/2 error would invalidate the proof and are expressly excluded.

On a fixed Omega, uniform A has a uniform image in q^t cosets. Verification confines acceptance to at most (2b+1)^n cosets even off promise. Summing over orbit unions yields the exact displayed binomial sum and its 2^r relaxation. No branch-success probability is multiplied across failed branches. Time is exp(O(r))*poly(n,log q,log b), with exponential memory allowed and total deterministic preprocessing charged.

Let Z_i indicate that orbit i is empty. The joint law gives E[Z_i]=p1 and E[Z_i Z_j]=p2. The falling-factorial comparison establishes p2<=p1^2; it does **not** assert independence. Hence the displayed mean and variance are exact and Var(E)<=mu. Chebyshev gives (O4) under mu>k, and the coefficient formula (O5) counts exactly d chosen roots with all other designated orbits nonempty. The newly targeted enumeration covers all d=0,...,n and all power-of-two r|n through n=16, including degenerate extensions outside the theorem; all 142 cases agree with a separate inclusion-exclusion formula. The coordinator's real threshold alpha*r version is also legitimate: E<ceil(alpha*r) is exactly E<alpha*r, and Chebyshev can be applied to that real threshold when mu>alpha*r.

In the asymptotic consequence, the independent-draw coupling error d(d-1)/(2n)=o(1) is used only for an expectation/occupancy estimate, not for a negligible-distance source replacement. Since r=Theta(d), d/r^2=o(1), so (1-1/r)^d=exp(-d/r)+o(1). The fixed strict margin exp(-1/a)>alpha makes mu-k=Omega(r), yielding failure O(1/d), not negligible failure. The uniform false-positive bound is exp(-Omega_c(n log n)) and runtime remains exp(O_c(d))*poly.

### N03-O1 / W2-CONSTANT-COMPARISON

**Material scope qualification.** The author's alpha=2/3,a=3 example improves only the archived sufficient C0=8 range. It does not establish improvement over optimized deterministic ATT, and it supplies no runtime comparison.

Indeed at c=1, for r>=a d and any fixed a>2,

    q^(1-d/r) >= (2n^2 ell^3)^(1-1/a) > 2n ell^2

eventually because 2(1-1/a)>1. A new exact algebraic control is a=5/2: after raising to the fifth power, the sufficient gate reduces to n>4ell. At a=3 it reduces to n>2. At a=2 the same lower-bound substitution instead gives the squared ratio 1/(2ell), so it does not certify the gate. These comparisons need no numerical prime experiment because the bound is monotone in actual q.

The finite ORB theorem itself is not refuted. The broader parameter criterion may be kept exactly as stated, and the final synthesis may describe a random-support occupancy refinement. The label “improvement” must identify its comparator; the example cannot support a claim of improvement over optimized ATT or hidden runtime constants. **Disposition:** qualification required in integration; any author-side rewrite would be a new version pending fresh recheck. No third research direction or new optimization was developed here.

## 4. COVER: all subgroups and adaptive selection

A subgroup of the order-n group has a generating list of length at most ell, padded by identity. This counts at most n^ell subgroups, regardless of duplicate lists. An index-r subgroup has r regular root orbits and at most 2^r invariant sets. For each fixed Omega with t>=alpha n,

    Pr[T avoids Omega] = C(n-t,d)/C(n,d) <= (1-alpha)^d.

Taking the union over the entire family proves (C1). This is an **unconditional inclusion of events**: even an omniscient function of T,U,V,F,H selecting a qualifying Omega can succeed only when some fixed family member avoids T. Conditioning T on the observed pair would generally change its law, but the proof never uses the uniform-subset estimate on that posterior. No support-renormalization product is present.

Under q<=n^K, a branch satisfying q^(t/n)>2nb must have t/n>1/K. The nonempty common sequence implies K>1, so alpha=1/K is admissible. The logarithm of (C1)'s bound is at most

    (ln n)^2/ln 2 + rmax ln 2 + d ln(1-1/K).

Because d/(ln n)^2 tends to infinity and rmax=o(d), this is -Omega_K(d), hence negligible in n. Both asymptotic hypotheses are essential to this deduction.

The strengthened statement for fully verified branches correctly uses the **global** uniqueness gate q^(1-2d/n)>2b sqrt(n), together with 2b<q. If a box F' leaves at most d active residual coordinates, the norm argument forces F'=F. Active U then forces every accepted Omega to avoid actual T. This implication does not constrain other lattices, short vectors outside the named fixed fields, or decoders bypassing that verification structure.

The inherited n=8,d=2,index<=2 control has coverage one and is independently reproduced. New nearby checks have exact coverage 3/7 for d=3 and 3/35 for d=4 at n=8,alpha=1/2,index<=2. The displayed finite union bound is vacuous there. Thus the blanket finite r<=d interpretation is **rejected**, while finite (C1) and its restricted asymptotic application pass.

## 5. SCAL: exact conditional ratios, H retained

Condition on the analysis sigma-algebra generated by (T,U,F,H), not on V or on the public pair. Its conditional law has V_i independent uniform F_q for i in T, while each U_i is fixed nonzero. The bijections V_i -> V_i/U_i therefore give exactly q^(-d) mass to every ratio vector. This conditional statement holds at every positive-mass discrete branch of the actual H_seq law; the adaptive sampler centers do not enter the calculation.

For fixed t and k selected active coordinates the equality event has mass q^(-k). A single union over q scalars and C(d,k) coordinate subsets yields (S2). Any t chosen using A,C, or even using all latent values, is bounded by this already maximized event. The public tuple may reveal information about the ratios; conditional iid ratio assertions after revealing A,C would be false and are **not** used. The new fixed-noise q=3 control makes this explicit: with U=(1,1), F=H=0, observing C=(0,0) fixes ratios=(0,0), although their prior law is iid uniform.

The no-collision probability (q)_d/q^d is exact for d<=q. The union bound d(d-1)/(2q)<=1/(4n^c ell^11) follows from d^2<=n/ell^8 and q>=2n^(1+c)ell^3. This is only an inverse-polynomial o(1) bound; the proof correctly avoids calling it negligible. For 0<delta<=1, k=ceil(delta d) yields the negligible exp(-Omega(d log n)) tail; delta>1 is the trivial impossible event. Cancellation down to o(d) would require a fixed positive fraction eventually, so the scoped negative conclusion follows.

The public identity C-tA=(V-tU)+(H-tF) holds pointwise. The new input is not asserted to have the A2 noise or ideal law. A varying CRT ring multiplier could cancel other coordinates only with additional hidden ratio information; the theorem neither supplies that information nor excludes all nonlinear uses of C. The active-U premise is mandatory: allowing U_i=0 makes the ratio undefined and changes the law.

## 6. PV/SEARCH: precise direction, positive event and witness

The independently specified PV challenge chooses known Omega uniformly of size n-d, draws F from the exact truncated coefficient psi independently, and supplies its evaluations on Omega. Its canonical error bound is nb. The strict known-support criterion q^(1-d/n)>2b sqrt(n) implies that two box vectors with the supplied evaluations coincide: their nonzero difference would have norm divisible by q^(n-d) but absolute norm at most (2b sqrt(n))^n. This is distinct from the n-2d criterion when the support is hidden.

The public solver fills only the missing evaluations uniformly, interpolates A, calls Rec(A), and verifies its returned box vector against the known evaluations. No hidden F or active flag is used by the simulator. Rec receives its usual public parameters and A, not Omega, V or latent coins. Its runtime bound must be a total bound on all inputs it is actually called on; no bound merely averaged on active inputs is promoted to a worst-case bound.

For analysis T=Omega^c and U=A-F. Conditional on every fixed T,F, this U is uniform on I(T), including zeros. For E_active={all d active coordinates are nonzero},

    Pr[E_active | T,F] = p0 = (1-1/q)^d,
    Law(T,F,A | E_active) = exact active A2 first-marginal joint law.

The constant normalizer preserves the original T,F prior. Appending Rec's independent tape yields

    Pr[Rec(A)=F] >= Pr[E_active, Rec(A)=F] = p0 epsilon.

This uses the original planted F throughout. Strict uniqueness makes every verified PV output that F; no fresh posterior witness is substituted. The reduction direction is **known-support average PV search <= active first-component F recovery**. A hardness premise for this specified PV search distribution would exclude that recovery task only; no cited source supplies such a premise here. Capped unbiased-bit field sampling has additional failure at most d*2^(-n); no Gaussian sampling is required inside this reduction.

The newly targeted nonuniform finite-F control at n=2,q=17,d=1 checks the conditional law atom-by-atom: p0=16/17, Rec's active success is 3/4, and raw-fill success is 13/17>=12/17=p0 epsilon. Its rational prior is deliberately not described as D_ell; the equality is pointwise in F and hence tests a stronger algebraic invariance. A separate q=5 known-root collision F=(1,1), F'=(0,-1) at root 2 demonstrates why verification outside the strict gate does not identify the planted witness.

The positive-event inequality cannot transfer a **signed decision gap**: half a Bernoulli(3/4) active law and half a Bernoulli(1/4) bad law equals Bernoulli(1/2), erasing the active gap against that comparator. This targeted control reinforces R13. W2 does not apply the search bound to decision advantage.

Recovery gives a first-component distinguisher by box/support verification and the exact (P3) counting bound, with source acceptance at least epsilon and negligible uniform acceptance. This is recovery-to-decision only. An arbitrary exact-pair distinguisher does not supply Rec, and the known-support PV challenge does not supply hidden F needed to sample the exact H_seq(F) component. The named missing pair-simulation/decision-to-recovery lemma remains open. W2's negative scope is accurate.

## 7. Complete historical regression disposition

Full reports, not the short registry descriptions, supplied the controls. The structured `expected_outcome` / `provenance` fields of R01, R04 and R13 contain pipe-splitting artifacts; their full `exact_record` and complete evidence packet remain intact. This is an administrative issue, not evidence against any W2 formula.

| Control(s) | Applicable W2 claim(s) | Outcome and exact reason |
|---|---|---|
| R01; binomial code attack; 10-C01/11-calculations | ORB, COVER | PASS: T remains a uniform arbitrary d-support; the retired binomial source is not substituted. Orbital candidate zero sets do not change the sampled support family. |
| R02; coins C=G completion counterexample; 08-additive-obstruction | SCAL, PV boundary | PASS: fresh independence of V conditional T,U,F,H is an actual source premise; no hidden-noise cancellation or joint completion is inferred. |
| R03; exact uniform marginals but equal pair | PV and overall conclusion | PASS: first-marginal recovery is not claimed to prove pair hardness; joint source remains explicit. |
| R04, R05; Gaussian marginal correlation and pairwise independence controls | SCAL | PASS: full conditional V law is used; H's exact conditional kernel is retained. No product target is inferred from marginal noise laws. |
| R06; q=3 missing quotient outputs, 14-S04/15-experiment_e02 | All scope | OUTSIDE claimed regime/task: no entropy-only extraction is used. Complete finite counterexample retained, not contradicted. |
| R07; field kernel versus Boolean fibers, 16-S05 | PV, COVER | PASS: actual integer norm uniqueness is used, not field nullity as Boolean lossiness. PV uses truncated integer F, not a binary inversion/collision shortcut. |
| R08; precursor versus public transcript | PV, overall conclusion | PASS: Rec is an explicit public A-only algorithm hypothesis; uniqueness is information-theoretic only. |
| R09; equality injection and Lucas omission, 06/07 packet | ORB, COVER, PV | PASS: every norm/rounding threshold remains strict; finite q=5 collision excluded by gate. No Lucas occupancy result is used. |
| R10; no-wrap false acceptance can be one, 17-S12 | ORB, PV | PASS: explicit false-positive counting bound capped by 1; asymptotic negligibility separately checked. |
| R11; sometimes lossiness versus average success | ORB, PV | PASS: ORB's average support coverage and PV's average epsilon are retained exactly; no mild-hardness amplification. |
| R12; verified nonoriginal preimages | PV, verified COVER | PASS: strict appropriate uniqueness gate supplies original-witness identity; outside-gate new collision reproduces the objection. Recovery-to-decision needs only the one-way success implication. |
| R13; Renyi orientation and signed decision | PV | PASS: exact positive-event decomposition, not an incorrectly oriented divergence transfer. New signed-mixture control erases decision gap. |
| R14; active-unit conditioning cost | SCAL, PV | PASS: SCAL requires nonzero U; PV pays exact (1-1/q)^d, not an uncharged negligible-TV replacement. |
| R15; rotations/repetitions/common K | All | OUTSIDE: m=1, one Rec call; no manufactured additional source samples or independent V_i. |
| R16; statistical support test and hard posterior sampler | ORB, PV, overall conclusion | PASS: existential sparse-support witness is distinguished from polynomial implementation; no posterior sampler supplied by uniqueness. |
| R17; matrix universality, tiny symmetry orbits, XOR carries, sparse quantum sampling | All | OUTSIDE: none of these retired mechanisms is revived. Fixed group orbit counting is not a claim of general symmetry mixing. |
| R18 / CP-1; 18-probability-regressions | ORB, COVER, SCAL, PV | PASS: reproduced posterior masses and 21/2000>1/100; cause is support restriction/normalization. No selected-stage event product or observable latent cache status is used. |
| C03-HC1; NC1-v1; 02-objections/05-NC1-v2 | Exact H scope | PASS by non-use: W2 uses no convolution-denominator bound; inherited guarded NC1 remains untouched. |
| C03-HC2 | SCAL and pair-simulation limit | PASS: adaptive H_seq differs from D_B and is never replaced. |
| C03-HC3/HC4 | Overall noise/source limits, PV direction | PASS by non-use for variance/deconvolution shortcuts; HC4 signed-decision objection explicitly retained. No Gaussian moment approximation enters W2. |
| C03-HC5/HC7; common K and leakage thresholds | All | OUTSIDE m=1; no leakage/many-Y or common-K theorem claimed. |
| C03-HC6 | ORB, PV | PASS: no solver-success/good-noise independence multiplication; CP-1 reproduced; planted witness preserved. |
| C02-LATENT-PUBLIC, C02-CHAR, PUBLIC-ENCODED-F | PV and overall conclusion | PASS: encoding/uniqueness does not provide an efficient decoder; fixed-character control is not general computational pseudorandomness. |
| C01-ATT | ORB | PASS: n=2,q=17 dual signs, trace normalization, representative changes, nonzero rank and strict radius; public roots and deterministic solver policy retained. |
| S0-dependency | Global graph only | OUTSIDE W2: no binary-RLWE bridge theorem is certified or AN dependency removed. |
| UNIFORM-APPROX-COLLAPSE | Global/source-map limits | OUTSIDE: W2 uses no exact-uniform entropy monotonicity claim or its invalid approximate extension. |
| SE-CORRELATION-F3; PAIRWISE-SE-F3; N02-DUAL-NUMBER | Global bridge only | OUTSIDE: W2 introduces no S,E bridge or general finite-ring theorem; these downstream review controls remain retained. |
| W2-SUBGROUP-BOUNDARY | COVER | PASS: full finite coverage reproduced; asymptotic and method restrictions retained. |
| W2-CONSTANT-COMPARISON | ORB | QUALIFICATION REQUIRED as N03-O1: a=3 does not improve optimized deterministic ATT. |

## 8. New targeted evidence, primary imports and final boundary

[controls-v1.py](controls-v1.py), SHA256 **3e263088b7d2b862d843689a1ea383f097583c5c998ebb439f0a928a72a062e8**, ran once as N03-E-01-v1 from 20:56:32.006744Z to 20:56:32.135108Z (0.1284 seconds). It uses only installed Python standard-library exact integers and Fraction; seed=None, no Gaussian approximation, no external execution, no exact-SVP implementation. All parameters and finite models are fully recorded in [controls-v1.json](controls-v1.json). The code is explicitly guarded by both 115 seconds elapsed and 21:18:45Z, inside the external 120-second cap and assignment deadline. Replay command, before its fixed deadline:

    timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N03/controls-v1.py

For later reproduction, the frozen code's body can be reviewed or a separately versioned authorized copy can receive a new administrative deadline; do not silently change this archived experiment. Bounds were proved analytically above. Finite enumeration is evidence and does not prove the unrestricted or asymptotic statements.

The direct primary checks support the exact imported interface. BGP Definition 2.14 specifies known-ideal PV recovery and its strict uniqueness radius; Theorem 3.2/Lemma 3.3 provide unramified stabilizer lifting; Section 3.2 gives integer-basis operations; Corollary 4.2 retains a strict inverse-ideal decoding gap. The random-support distribution and occupancy deductions here are W2's, and no hardness theorem for its psi is imported. [Boudgoust–Gachon–Pellet-Mary, ePrint 2022/709](https://eprint.iacr.org/2022/709.pdf).

Micciancio–Voulgaris Corollary 5.5 supplies deterministic exact SVP in single-exponential rank. Section 2 explicitly accommodates rectangular integer bases with polynomial dependence on ambient dimension and entry bit size. This is the corrected ATT policy; the older unspecified probabilistic solver's success is not upgraded. [Micciancio–Voulgaris, ECCC TR10-014 revision 1](https://eccc.weizmann.ac.il/report/2010/014/revision/1/download).

The material comparison issue is precisely N03-O1; all other reviewed objections are closed **within the frozen finite scopes**, as mapped above. No mathematical author repair was written. Any changed proof remains pending fresh nonauthor review, and this report does not make an incomplete graph ACCEPTED. Exact P0-A2 remains **OPEN**. W2 is completed bounded structural triage with clean negative scope: neither its small-fixed-field barrier, scalar-cancellation obstruction, nor one-way PV search reduction establishes computational hardness or an efficient exact-pair attack.

Final artifact verification completed at **2026-09-06T21:05:10.777536+00:00**, before the assigned deadline. The frozen proof hash is unchanged, all nineteen imported packet hashes match, experiment source/data hashes agree, and the assignment contains the full exact research scope. No further experiments were run.
