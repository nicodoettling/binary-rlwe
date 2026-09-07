# Finite investigation report — final structural reconciliation pending

**P0-A2 remains unsupported.** This investigation did not prove binary-secret RLWE hardness from an independently supported computational premise and did not obtain a polynomial-time distinguisher for the exact A2 challenge. It produced a checked conditional observable reduction, restricted source-conversion obstructions, and bounded structural results. These are useful finite outcomes; they do not complete the hardness theorem.

W1 and W3 were the two developed directions selected after all three triage reports. W2 received structural review without further development. All claims and their exact versions are in [claims.json](claims.json); the append-only record is [claim-history.jsonl](claim-history.jsonl).

## Exact common regime and unsupported premise

Let $n$ be a sufficiently large power of two and fix constants $c,K$ before the adversary. Set

\[
\ell=\lceil\log_2 n\rceil,\quad
d=\lfloor\sqrt n/\ell^4\rfloor,\quad b=\ell^2,\quad
\tau=\ell,\quad \sigma=2n\ell^3,
\qquad \sigma n^c\le q\le n^K,
\]

where $q$ is prime and $q\equiv1\pmod{2n}$. The common example is **$c=1,K=16$** along the inherited qualifying prime sequence; that prime-existence import remains PROVISIONAL. No practical threshold for “sufficiently large” was established. Work throughout is **one pair, $m=1$**.

In $R_q=\mathbb F_q[X]/(X^n+1)$, choose a uniform $d$-subset $T$ of the CRT roots. Let $I_T$ contain elements supported on $T$, and $J_T=\operatorname{Ann}(I_T)$. Conditional on $T$, $U$ has independent uniform **nonzero** coordinates on $T$, and $V$ is independently uniform in $I_T$, including zeros. Independently, $F$ has iid coefficient $D_\ell$ entries conditioned on $[-b,b]$, with $D_s(z)\propto e^{-\pi z^2/s^2}$.

The exact completion kernel is the coefficient-order sequential discrete Gaussian obtained from the canonical unit-lower LDL factorization of

\[
B_F=\sigma^2 I-\tau^2M_FM_F^T.
\]

Its adaptive centers and conditional normalizers are retained; $H_{\rm seq}(F)$ is **not** identified with the globally normalized lattice Gaussian $D_{B_F}$. Its fresh coins are independent of $T,U,V$ conditional on $F$. P0-A2 asserts computational indistinguishability of

\[
(U+F,\;V+H_{\rm seq}(F))\bmod q
\quad\text{and}\quad \operatorname{Unif}(R_q^2).
\]

Only the pair and public parameters are available. The exact kernel construction, algorithmic inputs and target binary-secret distribution are frozen in [target.md](target.md) and [SOURCE_CONTRACT.md](inputs/SOURCE_CONTRACT.md). The analytic bridge already assumes P0-A2; its completion and extraction calculations do not prove that premise.

## What the source reductions establish

The [frozen W1 proof](inputs/frozen/W1-final-v1-note.md) contains six claims, all freshly checked by [N01](criticism/N01/review-v1.md). Their global status remains PROVISIONAL, with favorable dispositions confined to their exact hypotheses.

The primary HLBDD comparison uses one common hidden ideal, two independent uniform ideal points, and independent small Gaussian errors. We wrote its two-element experiment explicitly because the printed definition is terse. Section 7 assumes this source hardness separately; its entropic bridge also uses swallowing and a superpolynomial-modulus unit step. It supplies neither active-point conditioning nor the A2 completion kernel. [Order-LWE, Section 7](https://eprint.iacr.org/2018/494.pdf#page=38).

For that explicit small-noise pair, the public map

\[
(a,c_0)\longmapsto(a,c_0+W),\qquad
W\sim D_{\sqrt{\sigma^2-\ell^2}}^n
\]

broadens the second noise to $D_\sigma^n$ with negligible guarded convolution error. The uniform comparator remains exactly uniform, including with an approximate independent $W$ sampler. Conditioning the first noise into its box adds the explicit truncation error. The map preserves the actual law of $U$; conditioning all its $d$ coordinates to be nonzero would introduce

\[
\delta_{\rm act}=1-(1-1/q)^d,
\]

which is nonnegligible for fixed polynomial $q$. This gives a valid finite advantage bound, not negligible-loss inheritance of active-point source hardness.

Two obstructions explain why a completion identity alone is insufficient:

* **Broad-source conversion.** Start instead from the active-point independent-noise pair $P_{\sigma}^{\rm act}=(U+F,V+E_\sigma)$. Under the strict uniqueness and box-injection gates in [parameter-table.md](parameter-table.md), every stochastic pair map $\mathcal K$ satisfying exact $\mathcal K\operatorname{Unif}=\operatorname{Unif}$ has
  \[
  \varepsilon=\operatorname{TV}(\mathcal K P_\sigma^{\rm act},P_{A2})
  \ \ge\ \frac{g^2}{(2n\ln q+2)^2},
  \qquad g=\Omega(\ell^{-2})>0.
  \]
  The proof defines $g$ by exact adaptive discrete entropy and exceptional-tail bounds. These gates hold eventually for $c>1/2$, including the common example. The map may change both coordinates and have unlimited computational resources. This theorem excludes negligible approximation in its declared class. It does not cover the original small-noise input or merely approximate preservation of the uniform comparator. A sparse-support collapse is a saved counterexample to that last extension. A separate exact A-keeping impossibility uses the positive-mass $F=1$ fiber, without claiming a quantitative lower bound from that rare fiber alone.

* **Repeated hidden-kernel sampling.** If a worst-case polynomial-time public algorithm could sample the latent completion kernel from $A$ alone, with uniform negligible error and fresh independent coins on repeated calls, then bounded second-moment estimates would recover $FF^\dagger$. The public test checks whether $AA^\dagger-FF^\dagger$ has CRT support at most $2d$. The reviewed proof gives polynomial sample cost and negligible uniform acceptance for every fixed $c>0$, while explicitly charging sequential-normalizer, wrapping, sampling and rounding errors. This hypothetical sampler would attack the first marginal, including the primary source after a positive-event argument. **The source challenge does not provide that sampler.** No such sampler was constructed or executed, and an arbitrary map using $C$ is outside this result.

Posterior simulation has two separate requirements: an effective posterior sampler and the correct output on a uniform input. The frozen Bayes calculation and finite counterexamples show that the first does not imply the second. Likewise, positive Fourier ratios alone do not guarantee a nonnegative convolution kernel. The DSPR and matrix entropic-LWE comparisons provide different source interfaces; no checked map from them to exact A2 was found. See [source-comparison.md](source-comparison.md) and the primary-source records in the review packets.

## The one observable alternative and its remaining loss

The [edited W3 proof](candidates/observable/statement-and-proof-v2.md), coordinator W3-OBS v3 / author v2, keeps $H_{\rm seq}$ only as a mathematical coupling. Its public tests on the independent-noise source are

\[
B_1(a,c)=D(a,aS+E),\qquad B_2(a,c)=D(a,aS_0+c),
\]

using fresh independent public-law draws. Under the explicitly frozen full product-kernel joint law and the retained noise/extraction premises, it proves

\[
\operatorname{Adv}_{\rm target}(D)
\le \operatorname{Adv}_{\rm src}(B_1)+\operatorname{Adv}_{\rm src}(B_2)
   +2\eta_N+\eta_X+\eta_{\rm iso},
\qquad
\eta_{\rm iso}=\mathbb E\!left[1-\frac{|UR_q|}{|I_T|}\right].
\]

Each test consumes one challenge pair; the two advantage terms do not assert two independent challenges from a common secret. All finite sampler losses and operation costs are given in the proof. Composing directly with the explicit uniform-point small-noise source costs an additional $2\delta_F+\eta_{\rm br}$, plus the separately listed implementation errors, where $\delta_F\le n e^{-\pi\ell^2}/(\pi\ell)$. It needs no public $H_{\rm seq}$ sampler.

For active $U$, $\eta_{\rm iso}=0$, but hardness of that independently noised active-point source remains unsupported. For uniform-in-ideal $U$,

\[
\eta_{\rm iso}=1-(1-1/q+1/q^2)^d,
\]

which differs from $\delta_{\rm act}$ and is nonnegligible at fixed $K$. This statistical loss cannot simply be removed from the stated endpoint comparison. With independent target errors, a deterministic **exponential** public witness proves

\[
\operatorname{TV}\big((U+F,US+FS+E),\ (U+F,V+FS_0+E_0)\big)
\ge \max\{0,\eta_{\rm iso}-2\delta_E\},
\quad \delta_E\le2n e^{-\pi\ell^2},
\]

under the explicit strict norm gates, eventually for $c>1/2$. It enumerates the unique bounded $F$, recovers the actual support of $U$, and tests a public ideal-plus-box condition. It establishes a public statistical lower bound, not a PPT attack on P0-A2. The matching upper bound still depends on the retained analytic premises.

The general review packet initially omitted full joint independence of $S,E$ with the source tuple. The [blind reviewer](criticism/B01/blind-report-v1.md) refuted its literal A1/A2 statements over $\mathbb F_3$: $E=-S$ gives all stated error terms zero, a uniform source, and target advantage $2/9$. That version remains REJECTED. The repaired full proof specifies the complete product-kernel law. Fresh nonauthor [N02](criticism/N02/review-v1.md) checked those exact edited bytes against the old witness, a new pairwise-independence counterexample, and a dual-number control with exact TV $=\eta_{\rm iso}=9/32$. The repair is closed within its finite conditional scope; inherited NC1/X1/AN/PR1 remain PROVISIONAL.

## Structural outcome and historical objections

W2's [frozen structural note](inputs/frozen/W2-final-v1-note.md) gives exact empty-orbit occupancy bounds for an $\exp(O(d))\operatorname{poly}(n,\log q)$ variant, a union bound over every small-index subgroup that limits this particular method at degree $o(d)$, and an exact scalar-cancellation bound under the actual $V,H_{\rm seq}$ law. A separately specified known-support PV search problem reduces to first-component recovery with success factor $(1-1/q)^d$; this is a positive-event search statement, not general pair decision hardness. No polynomial or $\exp(o(d))$ attack was obtained.

The orbit example $a=3$ at $c=1$ improves the archived sufficient constant $C_0=8$ only. Optimized deterministic ATT already permits any fixed $a>2$ eventually. The example therefore establishes neither a better optimized runtime nor a bit-security improvement. N03 has confirmed this qualification and the finite subgroup boundary; its final report is pending in this synthesis version.

All R01–R18 and later exact hand controls are retained, with nineteen complete historical evidence packets and their hashes. The principal dispositions are:

| Prior objection | Current handling |
|---|---|
| NC1 negative denominator; adaptive Gaussian normalizers | Both finite guards retained; exact conditional normalizers used, with explicit comparison costs where needed. |
| S0 dependency omission; strict ATT/uniqueness gates | AN v2 retained; deterministic solver policy, strict inequalities and public-root input preserved. Polynomial-$q$ root enumeration is separately charged. |
| Latent information mistaken for a public attack | New lower bounds supply an actual public test; the stronger repeated-kernel capability is stated as a hypothesis. F5 erasure remains a counterexample to the shortcut. |
| Gaussian marginals, pairwise independence, selected-stage probability products | Full joint kernels, conditional laws and exact chain rules used. CP-1 remains a rejection with $21/2000>1/100$. The blind independence defect was versioned and freshly rechecked. |
| Signed decision transfer; verified alternative preimages | Search transfers use positive success events and strict uniqueness where needed; no general decision-to-search implication is claimed. |
| Small finite subgroup coverage and conservative orbit constants | Explicit finite/asymptotic hypotheses and method scope retained; no general algorithmic lower bound. |
| One-pair tensorization, common $K$, separate-$Y$ leakage | Multiple-sample gate **NOT OPENED**. $m=1$ throughout; inherited Pm and joint-noise obligations remain open or deferred. |

The full claim-addressed reconciliation and review hashes are in [reconciliation.md](reconciliation.md). Same-model review is complementary mathematical scrutiny, not statistical independence. A favorable critic report and a successful artifact check do not certify an incomplete dependency graph.

## Evidence and bounded completion

The saved experiments include exact probability and ring computations, with code, parameters, seed policy and timeout records in [experiments/registry.json](experiments/registry.json). Examples include 46,798 blind independent-law checks, all 512 deterministic tests on a finite public alphabet, 3,360 rational bistochastic controls, 6,651 ternary autocorrelation vectors, and structural occupancy/rounding/conditioning controls. Gaussian diagnostics use labeled 80- or 90-digit arithmetic and explicit truncation bounds; they are not interval-certified proofs. Small toy dimensions are not claimed as instances of the asymptotic A2 parameter choice. No full source sampler, practical parameter benchmark or actual conditional-kernel attack was run.

Launch-specific authorization, the output path, finite UTC deadlines and supervisor evidence were checked before research. All new research is in this run directory; old runs, consolidation, plans, literature and runner code remain read-only. Worker assignments use Astra ultra and the full academic scope. The coordinator's five-file checkpoints acknowledge written evidence only. Operational deviations, including one late N01 worker checkpoint and corrected archive metadata, are recorded in progress and review files rather than omitted.

One numerical evidence limitation is explicit: the first Gaussian diagnostic full JSON was overwritten when a missing likelihood-ratio factor in a tail-bound annotation was corrected. Its stdout and a labeled reconstruction of the pre-edit source are retained; the final corrected code/data are complete. No original full JSON or contemporaneous hash is fabricated. See [experiment-provenance.md](criticism/N01/experiment-provenance.md).

This version remains partial until the final structural review is reconciled. Mathematical shutdown and the independent launcher's actual exit are separate records; no launcher exit is observed here.

**One discriminating next question:** Can the explicitly defined active-point, same-ideal HLBDD source at this fixed parameter regime inherit the ordinary uniform-point source assumption with negligible total distinguishing loss? A positive answer would supply the missing computational premise for the independent-noise observable route, subject to the retained analytic dependencies. It would still not itself prove P0-A2.
