# Proof of the pointwise same-ideal composition

This is a composition proof from the four explicit mathematical interfaces in interface-statements-v1.md. It verifies their hypotheses and tracks the resulting full laws, errors, and finite resource model. It does not purport to replace their separate proofs. The theorem, specification, and interface statements form a separate theorem-only packet.

## 1. Fixed ideal, normalized laws, and algebraic representations

Fix the supplied ordinary basis of \(J\) throughout. There is no sampled ideal whose distribution can change between hybrids. Since \(J\) is integral of index \(D\), \(R\subset J^{-1}\subset D^{-1}R\). Multiplication by \(D\) followed by \(D^{-1}\bmod q\) identifies \(J^{-1}/qJ^{-1}\) with \(R/qR\): the inclusion \(R\to J^{-1}\) induces an isomorphism because the finite quotient \(J^{-1}/R\) has order \(D\), coprime to \(q\). Thus the explicit numerator formula is independent of representative.

The coefficient covolume of \(J^{-1}\) is \(1/D\). The covolume of \(L=qJ^{-1}\) is \(q^n/D\), and that of \(h\mathbb Z^n\), \(h=1/(DP)\), is \((DP)^{-n}\). Their ratio gives \(|F|=q^nD^{n-1}P^n\). Ordinary rational lattice and HNF/SNF algorithms provide representatives using full finite bit encodings. No factorization of \(D\) or short geometric basis is required.

The canonical embedding satisfies \(\|\sigma(x)\|_2^2=n\|x\|_2^2\), by orthogonality of the \(n\) roots of \(X^n+1\). Consequently the coefficient Gaussian \(G_{w_B}\) has canonical width \(w=\sqrt n w_B\). This changes both the exponent and normalization by the similarity Jacobian; it is the same probability law, not a different density with a missing normalizer.

The target completion uses its own independent binary \(S\), one shared secret across the \(k\) samples, and independent coefficient integer Gaussian errors. For exact uniform multipliers the full completed joint law is exactly the recovery target. Testing equality with the actual secret is meaningful even when several secrets could explain the observed samples. No auxiliary completion variable is adjoined as public information.

## 2. A-FRAC numerical hypotheses and advantage

Because \(D^{1/n}\le2^\rho<2\), interface I's existence bound supplies a basis of operator norm below \(2n^2=\tau_2\). This is only a proof witness. With \(t_A=2n^2\ell\), \(L_A=\ell\), and \(s=\sqrt2\ell^2\),
\[
 2t_As\sqrt{kn}L_A=4\sqrt2\,n^2\sqrt{kn}\,\ell^4
 \le8n^2\lceil\sqrt{kn}\rceil\ell^4=\sigma.
\]
The theta argument becomes \(3\ell^2/4\), so interface I gives exactly the stated \(\delta_{\rm tail}\) and \(\eta_A\).

For the remaining term use the ordinary one-dimensional Gaussian mass identity
\[
 \rho_{t_A}(\mathbb Z)=t_A\rho_{1/t_A}(\mathbb Z)\ge t_A,
 \quad D_{\mathbb Z,t_A}(0)\le1/t_A.
\]
Therefore
\[
 D_{\max}\bigl[(1+D_{\mathbb Z,t_A}(0))/2\bigr]^n
 \le2^{-(1-\rho)n}(1+1/t_A)^n
 \le\exp(-(1-\rho)n\log2+n/t_A).
\]
Here \(n/t_A=1/(2n\ell)\), giving the displayed \(\beta\). In particular the proof width is \(t_A=2n^2\ell\); it is not the reciprocal expression \(2n\ell\).

Interface I now gives the exact fractional-wrapper advantage
\[
 \epsilon_{\rm rec}-\delta_{\rm tail}-\beta-\eta_A.
\]
The hypothesis on recovery success is pointwise for the fixed public metadata. If the recovery code ignores \(J\), its target law is identical for every eligible ideal, so its given success bound is automatically uniform in that metadata-free sense. If it reads \(J\), an average success statement over ideals cannot replace the stated pointwise bound.

## 3. B-GP parameters, complete cap, and both endpoints

Since \(n\ge2\), \(k\ge1\), \(\ell\ge2\), hence \(0<\epsilon_B=\nu\le1/16\). Also \(\log_2n\le\ell-1\). Thus
\[
 \log(8n/\epsilon_B)
 \le(\ell^2+\ell+2)\log2
 \le\pi\ell^4,
\]
where the last inequality follows already from \(\ell\ge2\). Consequently \(r_B=\ell^2\ge\max(1,\sqrt{\log(8n/\epsilon_B)/\pi})\), and \(s^2=w_B^2+r_B^2=2\ell^4\). All B hypotheses hold.

Before capping elementary uniform loops, B's full planted law is within \(\Delta_B\) of the normalized lattice Gaussian source and its comparator is exactly uniform. The scalar fallback remains translation-equivariant, so the exact comparator assertion applies to this uncapped quotient-sampling stage. Completing with exact fresh \(S,E\), and then invoking recovery, is a Markov kernel; it cannot increase TV.

Replacing the \(kn\) exact target-error draws by independent scalar approximations costs at most \(kn\nu\) in either world. This is a product/conditional coupling with fresh coins; it is not a statement that a particular fixed random tape works on every input.

There are at most \(kn\) quotient invariant-factor draws, \(knL_+\) bridge scalar proposals, and \(knL_+\) target-noise scalar proposals. Hence \(U_{\rm all}=kn(1+2L_+)\) bounds all elementary uniform draws in a complete call. Each binary rejection has success probability greater than \(1/2\) at every nontrivial draw; conditional on any previous transcript its cap-failure probability is below \(2^{-B_{\rm cap}}\). First-disagreement coupling and a union bound give \(U_{\rm all}2^{-B_{\rm cap}}\le2^{-\ell^2}=\eta_{\rm cap}\) for the whole wrapper, for every input. The same fixed code and caps are used in both worlds.

The implemented planted and comparator distances are therefore respectively
\[
 \Delta_B+kn\nu+\eta_{\rm cap},
 \qquad kn\nu+\eta_{\rm cap}.
\]
For acceptance probabilities \(p_1,p_0\) and ideal references \(p_1',p_0'\), the triangle inequality gives
\[
 |p_1-p_0|\ge |p_1'-p_0'|-|p_1-p_1'|-|p_0-p_0'|.
\]
Combining the previous section and expanding \(\Delta_B\) yields exactly (G), with three \(kn\nu\) terms and two \(\eta_{\rm cap}\) terms. In particular the bounded comparator is approximate. This constructs one exact finite test \(A_J\) having advantage at least \(\delta\). Further invocations use this same actual test; the source-to-target loss is not multiplied by the number of those invocations.

## 4. C8 pointwise hypothesis, causal confidence, and termination

Its exact finite GP input group, grid rounding, conditional independent sample law, and metadata now match interface III, with canonical \(w=\sqrt n\ell^2\). All valid \(F\) representatives yield valid bounded inputs to \(A_J\), even for a wrong global orientation or unusual adaptive query.

Choose \(\zeta\) before \(\kappa\), and \(\kappa\) before the displayed integer loops defining \(Q_*\). Then \(\epsilon_0,a,\chi,v_0,d_0\) are selected. Since \(h_0=v_0d_0\) is fixed before \(v_0\), none of the lower bounds on \(\kappa\) depends circularly on a precision chosen after \(Q_*\). To choose \(\kappa\) constructively, take certified upper integer bounds for its five lower constraints and also any integer greater than \(\log(24Dw/q)\), plus positive slack. Certified bounded-error evaluation suffices; no equality test at an integer transcendental boundary is needed. The exact natural-log ceiling inside B remains governed by its distinct exact-ceiling interface.

The rational specialization satisfies the extra uniqueness inequality without a further hidden enlargement:
\[
 d_0\le\ell^2/(64nk)
 <q/8<q/(4D^{1/n}),
\]
because \(q\ge n\sigma=8n^3\lceil\sqrt{kn}\rceil\ell^4\) and \(D^{1/n}<2\). Increasing \(\chi\) only improves this inequality. The permitted choice \(\chi\ge a\) preserves C8's specified Up calculation rather than substituting a smaller cutoff.

Interface III applies to the actual implemented \(A_J\), giving its pointwise decoder failure
\[
 p=(n/2)e^{-\kappa}+\zeta
 \le\zeta/16+\zeta=17\zeta/16<1.
\]
Its fixed posterior/multiplier allowance is at most
\[
 2kQ_*\epsilon_0/(1-\epsilon_0)
 \le\zeta/[32(1-\epsilon_0)]<\zeta/16.
\]
The single global sample counter's conditional errors sum below \(\zeta/16\), and the finite walk-position allowance is below \(\zeta/16\); the complete interface conservatively puts all its finite numerical errors within \(\zeta\). These charges are causal: each next sampler uses its stipulated law conditional on the past. There is no conditioning on all future comparisons succeeding and no product of selected posterior success probabilities. Physical kernels need only remain close to their continuous proxies; they need not have an exactly Haar endpoint.

The fixed loop counts cover both orientations, every answer sequence, and targets outside the correctness promise. Consequently the decoder is a total bounded program, not merely an expected-time program or a program bounded on likely targets. It invokes at most \(Q_*\) actual \(A_J\)/recovery calls and generates at most \(kQ_*\) physical sample components.

## 5. Coefficient geometry, exact dual, and rational target promise

For nonzero \(x\in J^{-1}\), the integral ideal \(xJ\) has positive integer norm. Thus \(|N_{K/\mathbb Q}(x)|D\ge1\), so at least one embedding has absolute value at least \(D^{-1/n}\). It follows that
\[
 \|x\|_{\rm canonical,2}\ge D^{-1/n},
 \qquad \|x\|_2\ge1/(\sqrt nD^{1/n}).
\]
This deliberately weaker bound suffices:
\[
 \lambda_1(L)\ge q/(\sqrt nD^{1/n})>4d_0/\sqrt n=4d.
\]
A rational target with coefficient distance at most \(d=d_0/\sqrt n\) has canonical Euclidean error at most \(d_0\), and hence canonical infinity error at most \(d_0\). It is therefore in the C8 promise, with a unique nearest lattice vector. The finite query \(Bv/H\) is exactly rational; only the radius is an algebraic scalar, and its square is the supplied rational \(d_0^2/n\).

For this power-of-two cyclotomic ring the trace dual of \(R\) is \(R/n\): the codifferent generator \(1/(nX^{n-1})\) differs from \(1/n\) by a unit of \(R\). Also
\[
 \langle x,y\rangle_{\rm coefficient}
 =\operatorname{Tr}(x\overline y)/n.
\]
The trace dual of an invertible fractional ideal \(I\) is \(I^{-1}/n\). Taking conjugation into account gives its ordinary coefficient dual \(I^*=\overline{I}^{-1}\). Therefore
\[
 (qJ^{-1})^*=\overline J/q=\Gamma.
\]
This computes the exact lattice identity; the full canonical-dual version is \(\overline J/(nq)\), with the different factor explained by the canonical similarity.

## 6. Finite quantum interface and complete error accounting

Section 5 verifies every geometric hypothesis of interface IV. Section 4 verifies pointwise failure \(p\in[0,1]\) and all-input termination. Ordinary exact membership and basis conversion totalize the decoder output. The theorem's power-of-two and precision choices are made before compilation, using rational square comparisons for all square-root ceilings. The actual circuit is compiled only at this finite target width.

The call-slot dispatcher exposes at most one pending recovery call per slot and invokes exactly one recovery block there. Inactive slots use valid dummy inputs and ignore answers. Padded simulation preserves the active program's law with fresh bits. Retaining all dispatch and work registers makes its forward/inverse coherent execution valid. The actual circuit thus has \(Q_*\) executable recovery blocks per forward pass; one inverse pass doubles this count. A naive branchwise classical call count would not establish the same property for an arbitrary circuit.

Applying interface IV gives a sample on \(\Gamma\) at width
\[
 s_\Gamma=\frac{\sqrt n}{\sqrt2d}=\frac{n}{\sqrt2d_0}.
\]
For clarity the complete finite proof's error ledger, in its normalized-reference convention, is:

| Stage | Charge |
|---|---:|
| Successful scalar preparation approximation | \(3n2^{-W}\) |
| Exhausted scalar caps | \(n2^{-8W}\) |
| Uniform conditional coset comparison | \(2^{-W}\) |
| Input reference truncation | \(2\sqrt{\tau_n}\) |
| Coherent decoder replacement | \(2\sqrt p\) |
| Input periodization comparison | \(\sqrt{2(\tau_n+c_n)}\) |
| Complete finite phase resources, including caps | at most \(2^{-W}\) |
| Output periodization comparison | \(\sqrt{2(\tau_n+c_n)}\) |
| Output Gaussian tail | \(\tau_n\) |

The finite terms \(3n2^{-W}+n2^{-8W}+2\cdot2^{-W}\) fit within \(\varepsilon\) by the chosen \(W\); the other terms give \(2\sqrt p+E_n\). The input off-promise tail occurs in the input-reference charge, not again in the decoder term.

Measured coset labels are retained as records. A common purification, when needed, is \(\sum_y\sqrt{P_y}|y\rangle_Y|y\rangle_E|\psi_y\rangle\); tracing its environment yields the measured classical-quantum law. It is not an assertion that a measured mixture is a pure state. Conditional normalization and periodization cross terms are provided by interface IV on that full law. Likewise phase resources are prepared before adaptive use, and their complete failure mixtures are charged before any entangled correction channel. The proof does not select a universally good random tape, discard decoder garbage before reversal, or condition preparations on future teleportation outcomes.

Multiplication by \(q\) and conjugation are a bijection \(\Gamma\to J\) and an isometry followed by scale \(q\). They send the normalized law \(D_{\Gamma,s_\Gamma}\) exactly to \(D_{J,qs_\Gamma}\): both exponents and normalizers match term by term. TV cannot increase under this deterministic map. Thus \(s_J=nq/(\sqrt2d_0)\), and canonical width is \(\sqrt n\,s_J\). All finite failures already output zero, giving support in \(J\) on every branch.

## 7. Finite bit complexity and actual execution resources

The scalar target errors and bridge use bounded scalar trial counts, bounded elementary rejection caps, ordinary rational arithmetic, and the supplied recovery bound. They require no ideal-Gaussian oracle. Let \(H_{\rm in}\) count all ordinary basis and metadata encodings, rational scalar numerators/denominators, algebraic evaluation descriptions, ring parameters, and the current target. Let \(E_C\) be the actual worst-transcript certified-evaluation cost in C8. The explicit programs give constructible bounds of the form
\[
 T_{AB}\le T_{\rm Rec}+\operatorname{poly}(H_{\rm in},n,k,\ell,\log q,\log P),
\]
\[
 T_{\rm BDD}\le Q_*T_{AB}+E_C+
 \operatorname{poly}(H_{\rm in},n,k,\kappa,1/\delta,\log(1/\zeta)).
\]
These refer to the exact finite interface code, not an unspecified exact-real oracle. Binary-searched scalar support cardinalities do not become unary loops. Every scalar's numerator and denominator length and every routine's actual precision cost is charged. The padded call-slot machine has a constructible polynomial overhead in these bounds and \(Q_*\); use its bound \(T_{\rm dec}\), not \(T_{\rm BDD}\) alone, in the circuit estimate.

Interface IV supplies the explicit nondecoder bound \(G_0\). Its excessively large fixed-degree expression includes all finite Machin/Taylor arithmetic, scalar support and phase resource loops, Fourier operations, measurements, and output arithmetic. The typed encoding in the theorem provides actual delimiters, so \(B_{\rm len}\) is an honest input-length bound. The Boolean circuit term \(4S_{\rm dec}+m+2r_{\rm dec}\) counts one reversible forward computation, XOR, one reverse computation and coin preparation/unpreparation, with work retained.

The resulting numerical bound concerns execution of the actual emitted circuit. Classical ideal/decoder setup, uniform finite host compilation and gate-list writing have their own polynomial costs, denoted by their actual count \(T_{\rm setup}\); they are not bounded merely because the emitted circuit has \(S_{\rm dec}\) gates. The theorem states that distinction explicitly and includes \(T_{\rm setup}\) if an end-to-end count is desired. F's own register/preparation preprocessing is already included in \(G_0\), so it is not charged twice. The alternative fourth-power circuit bound is applied to the fixed finite-alphabet padded dispatcher, and assumes bit steps, not exact-real or unlimited-word instructions.

For independent repetitions, product coupling gives joint TV at most the sum of the individual bounds. Fresh preparation and decoder coins give the claimed product target and at most \(2uQ_*\) coherent recovery executions. Reversing a recovery block is uncomputation of its retained coins/work, not a new independent draw of physical samples.

## 8. Scope of the conclusion

All transformations preserve the supplied eligible ideal as the final output lattice. The hypothesis \(N(J)\le2^{\rho n}\) was used in the A geometry and entropy loss. It is not removed by duality, conjugation, scaling or finite Fourier sampling. The theorem makes no reduction from arbitrary ideal-lattice instances to this restricted family, and no standard worst-case hardness statement follows from this composition alone.

For fixed \(\rho<1\), polynomial \(k\), inverse-polynomial known recovery success, polynomial-value supplied split \(q\ge n\sigma\) satisfying the coprimality condition, polynomial input encodings and bounded polynomial-time recovery/evaluation routines, the displayed classical losses vanish faster than inverse polynomials. Eventually \(\delta=\epsilon_{\rm rec}/2\) is valid. Choices such as \(\zeta=2^{-4n-10}\), \(\varepsilon=2^{-n-4}\), and \(\chi=a\) give negligible TV, polynomial bit complexity and polynomial absolute output width, with enormous fixed polynomial degrees allowed. The recovery promise must hold for each supplied \((q,J)\) in this family; a premise at one fixed \(q\) cannot be reused after selecting another \(q\) from \(J\). This conditional parameter observation supplies neither those recovery algorithms nor an arbitrary-ideal family connection. Polynomial bit length of a supplied \(q\) alone would give bit complexity, but not polynomial absolute width: the factor \(q\) in \(s_J\) remains explicit.
