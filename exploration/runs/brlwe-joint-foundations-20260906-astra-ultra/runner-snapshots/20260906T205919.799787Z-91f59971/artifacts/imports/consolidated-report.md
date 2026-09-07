# Consolidated mathematical state: joint noisy ideals

This consolidation incorporates the completed critic reports and separately checked corrections from the interrupted [joint-ideal investigation](../../runs/brlwe-joint-ideal-20260906-astra-ultra/). It supersedes that run's partial final report and precritic claim ledger **for purposes of reading the mathematical state**; the original artifacts remain unchanged. The source run's completed reviews support a conditional one-sample bridge and a matching asymptotic analytic construction. They do not establish the computational hardness of its exact source. A deterministic subexponential attack and a scoped failure of the alternative shear construction also survive review.

The ledger uses `PROVISIONAL` for reviewed mathematics that has not passed every global certification gate, `OPEN` for unsupported hypotheses, and `BLOCKED` for hardness conclusions lacking those hypotheses. The separately repaired NC1 and ATT statements have received fresh nonauthor rechecks; they are not awaiting their first recheck. Reviewers' local `ACCEPT` verdicts are preserved as review dispositions, not promoted to a global proof certificate. This consolidation did not launch research, reprove imported theorems, execute the proposed samplers or run new experiments.

## 1. Frozen target and the conditional bridge

The target is rank-one RLWE over \(R=\mathbb F_q[X]/(X^n+1)\), with growing power-of-two \(n\), a fully splitting polynomially bounded prime \(q\), coefficient-binary \(S\), and independent coefficient discrete Gaussian errors, wrapped modulo \(q\). Write \(D_t(z)\propto e^{-\pi z^2/t^2}\). A one-sample instance is \((a,aS+E)\), with uniform \(a\), target width \(\sigma\), and \(q/\sigma\ge n^c\), for fixed \(c>0\). Multiple samples require separate statements below.

The exact source draws \(\Gamma=(J,U,F,H)\), independently of fresh \(S,G\), where \(I=\operatorname{Ann}(J)\), \(Q=R/J\), and multiplication by \(U\) is a bijection from \(Q\) to \(I\). Given \(J\), draw \(V\) uniformly in \(I\), independently of the other source variables. Publish

\[
\mathsf{Src}=(U+F,V+H).
\]

This source has no binary-secret input. Its complete joint law, including active-coordinate conditioning and the dependence of \(H\) on \(F\), is part of any computational assumption. Let \(Y=S+G\), for a fixed public auxiliary law. The sufficient statistical premises are

\[
\begin{aligned}
\operatorname{TV}((J,U,F,FG+H),(J,U,F,E))&\le\eta_N,\\
\operatorname{TV}((J,U,F,H,Y,\pi_J(S)),(J,U,F,H,Y,Z))&\le\eta_X,
\end{aligned}
\]

where \(E\) is independent target noise and \(Z\) is conditionally independent uniform in \(Q\). The noise comparison integrates out \(H\); extraction retains it. These are sufficient latent-variable conditions, stronger than public-transcript correctness.

The source tests are public: \(B_1(a,c)=D(a,as+e)\), using fresh \(s,e\), and \(B_2(a,c)=D(a,ay+c)\), using fresh \(y=S_0+G_0\). Neither needs hidden source data. Noise substitution and extraction produce \(UZ+FY+H\). Setting \(K=Z-\pi_J(Y)\) makes \(UK\) an independent uniform ideal element, so this is \(AY+C\). For every fixed \(y\), the map \((a,c)\mapsto(a,ay+c)\) preserves uniform pairs. Thus

\[
\operatorname{Adv}_{\rm target}(D)
\le\operatorname{Adv}_{\rm src}(B_1)+\operatorname{Adv}_{\rm src}(B_2)+\eta_N+\eta_X.
\]

The two source advantages need not coincide. Implemented source, first-test sampler, auxiliary sampler and public target errors add \(2\xi_{\rm src}+2\xi_1+\xi_Y+\xi_{\rm target}\). Uniform \(U\in I\) cannot replace active-unit sampling for free: its exact averaged image defect is \(1-(1-1/q+1/q^2)^d\). See [B0](../../runs/brlwe-joint-ideal-20260906-astra-ultra/bridge.md) and [C01's review](../../runs/brlwe-joint-ideal-20260906-astra-ultra/criticism/C01/review.md).

## 2. A2: one common analytic regime

Put \(\ell=\lceil\log_2n\rceil\) and choose

\[
d=\lfloor\sqrt n/\ell^4\rfloor,\qquad b=\ell^2,\qquad
\tau=\ell,\qquad \sigma=2n\ell^3,
\qquad\sigma n^c\le q\le n^K.
\]

Choose a uniform \(d\)-subset \(T\) of all CRT roots; \(I\) is supported on \(T\). Choose nonzero uniform active coordinates for \(U\), independent uniform \(V\in I\), and iid integer \(F_j\sim D_\ell\) conditioned on \([-b,b]\). Form its integer negacyclic multiplication matrix \(M_F\) and
\(B_F=\sigma^2I-\tau^2M_FM_F^\top\).

The **exact** source law uses the canonical coefficient-order sequential Gaussian kernel \(H_{\rm seq}\) defined by the rational LDL decomposition of \(B_F\). Its adaptive centers depend on previous source draws and \(F\), never on the bridge's \(G\) or \(S\). It generally differs from the lattice Gaussian with exponent matrix \(B_F\). Finite polynomial-time table samplers approximate this one mathematical law with separately accounted whole-source error; no actual implementation was executed. The [A2 dossier](../../runs/brlwe-joint-ideal-20260906-astra-ultra/candidates/A.md) fixes the distribution, and [R03](../../runs/brlwe-joint-ideal-20260906-astra-ultra/refinement/R03-interface-audit.md) supplies the implementation argument.

The extraction theorem now covers **every** \(d\)-support, not merely the original binomial family. For fixed \(K\), sufficiently large \(n\), and
\(\lceil(\ln n)^2\rceil\le d\le\lfloor\sqrt n/(\ln n)^4\rfloor\), it gives

\[
\eta_X\le\tfrac12\exp\!\left(-c_K n/[d(\ln n)^6]\right).
\]

The proof uses same-observation posterior replicas and an exact ternary difference law, then the joint affine-walk theorem of Breuillard–Varju and Voutier's Mahler-measure bound. C01 checked the imported statements, all-root admissibility, normalization and asymptotic gates. There is no RH assumption, scalar-to-joint multiplication, or exceptional-support rejection. Appending the complete independent source kernel preserves the bound. The formerly proposed \(d\asymp n/\ell^3\) is **not covered** by that proof; its failure is a sufficient-bound failure, not a refutation of extraction there.

At A2, \(\|M_F\|\le nb\) gives \(B_F\succeq3\sigma^2I/4\), while the input smoothing matrix is at least \(3\ell^2I/4\). Discrete convolution and sequential-normalizer errors are negligible. A qualifying prime regime exists eventually: the least prime \(1\bmod 2n^h\), for fixed integer \(h>1+c\), and Xylouris's exponent 5.18 give sufficiently large fixed \(K\); \(c=1,h=3,K=16\) is one example. These are asymptotic existence and polynomial-in-\(n\) complexity results, without practical thresholds or security estimates.

## 3. Corrected completion and dependency closure

NC1 v1's literal ledger statement was false outside its denominator's domain. For integer \(M\in\mathbb Z^{p\times n}\), define

\[
B=\sigma^2I_p-\tau^2MM^\top\succ0,\quad
\Theta=\tau^2I_n-\tau^4M^\top M/\sigma^2\succ0,\quad
\delta=\sum_{k\ne0}e^{-\pi k^\top\Theta k}.
\]

NC1 v2 uses \(e_{\rm conv}=\min(1,\delta/(1-\delta))\) when \(\delta<1\), and 1 otherwise. With \(\beta=\lambda_{\min}(B)\), \(\kappa=2\sum_{j\ge1}e^{-\pi\beta j^2}\), its sequential comparison similarly uses
\(e_{\rm seq}=\min(1,[((1+\kappa)/(1-\kappa))^p-1]/2)\) only when \(\kappa<1\), and 1 otherwise. Independent \(G\sim D_\tau^n\) and canonical \(H_{\rm seq}\) then give full-output distance at most \(\min(1,e_{\rm conv}+e_{\rm seq})\) from \(D_\sigma^p\). Wrapping contracts this distance.

The counterexample \(M=0,n=p=1,\sigma=1,\tau=1/3\) has actual distance zero but \(\delta>1\), making the old bound negative. C03 freshly checked the piecewise repair and its boundary controls. A2 and its stacked extension satisfy both guards eventually, so their numerical regimes are unchanged. The updated dependency versions are NC1/AN/MN/CHAR v2 and A0/M0/S0 v3. S0 v3 explicitly includes AN v2; the old ledger omitted the analytic premise needed for its instantiated negligible-error consequence. [Corrections](../../runs/brlwe-joint-ideal-20260906-astra-ultra/corrections/NC1-v2-and-dependencies.md) and [C03's recheck](../../runs/brlwe-joint-ideal-20260906-astra-ultra/criticism/C03/objections.md) are authoritative.

## 4. What remains computationally unsupported, and the attack that survives

P0-A2 assumes that the exact pair \((U+F,V+H_{\rm seq})\) is computationally pseudorandom. The checked HLBDD/Order-LWE results use different ideal-point/noise laws and parameter interfaces; DSPR and matrix-entropic-LWE results do not supply this correlated source either. Analytic compatibility, information-theoretic uniqueness and negligible fixed-character bias cannot establish P0. In fact A2's first marginal has statistically tiny support, despite the character bounds.

ATT v3 replaces an unspecified probabilistic solver by deterministic exact SVP in a fixed-subfield lattice. For a power-of-two \(r\mid n\), \(2d\le r\le n\), and strict \(q^{1-d/r}>2nb\), it distinguishes the first component in time \(\exp(O(r))\operatorname{poly}(n,\log q,\log b)\), accepting every planted input and accepting uniform input with probability at most

\[
\min\{1,\;2^r(2b+1)^n/q^{n(1-d/r)}\}.
\]

The generic theorem includes public CRT roots or a primitive \(2n\)-th root as input. At A2, polynomially bounded \(q\) permits deterministic root enumeration within the polynomial factor. Taking \(r=\Theta_c(d)\) yields deterministic \(\exp(O_c(d))\operatorname{poly}(n,\log q)\) cost and advantage \(1-\exp(-\Omega_c(n\log n))\). C01 freshly checked the C02-authored repair, including exact rounding, norms and rectangular-lattice complexity. Exponential memory is allowed. This is subexponential but superpolynomial at A2, not a refutation of its polynomial-time assumption or a concrete security estimate. [ATT v3](../../runs/brlwe-joint-ideal-20260906-astra-ultra/corrections/ATT-v3.md) supersedes the old unqualified attack prose.

## 5. The retired shear route and multiple samples

B's public shear \((a,c)\mapsto(a,c+La+W)\) remains a valid exact source transformation. Its tested independent iid-shear completion has retained-variable noise error at least
\((1-\pi/16)e^{-2\pi}/[96n^2\ell^4(1+\ell)]\).
The proof handles wrapped residue fibers and complex characters. This retires that route for an all-negligible-error reduction, including independent broadening. It is not an attack on its public source or an impossibility for all public-only, nonlinear or correlated simulators. A2 escapes those hypotheses through its \(F\)-dependent completion, so B's source inheritance and A2's completion cannot be combined without a new argument.

For prescribed \(m\), the surviving conditional extension uses a **new** source
\(((U_i+F_i,U_iK+H_i))_{i\le m}\), with one uniform quotient element \(K\), independent of the full source kernel. The full stacked complement has cross blocks \(-\tau^2M_{F_i}M_{F_j}^\top\). The sufficient width is \(\sigma_m=2n\ell^3\sqrt m\), with \(\sigma_mn^c\le q\). Smoothing remains \(n\)-dimensional; the sampler has dimension \(mn\). Its Pm hypothesis is unsupported and does not follow by tensorizing P0. Conditional ideal tuples have only \(q^d\) values, rather than \(q^{dm}\). This latent distinction alone is not a public distinguisher.

Exposing separate \(Y_i=S+G_i\) causes a different problem: at A2, \(m=C\tau^2\ln n\), \(C>2/\pi\), drives the required conditional-extraction distance to \(1-o(1)\). This concerns exposed auxiliary observations, not hidden transcript information. Exact recovery with success \(\varepsilon\) from \(m\) samples implies decisional advantage at least \(\varepsilon-m\delta_T-2^nv_T^m\) by same-input residual verification. Baseline tails and volume make those losses negligible, but the corresponding \(m\)-sample decisional premise is still required.

## 6. The next bounded questions

1. Can an independently motivated source reduction produce A2's precise active-unit and \(F\)-dependent completion law without decoding hidden \(F\); alternatively, is that law polynomially distinguishable?
2. Can grouped-orbit or other algebraic decoding exploit more structure than the current \(\exp(O(d))\) attack, with explicit success, root-input and bit-complexity accounting?
3. Can a justified common-\(K\) source support a stated sample budget and target width, rather than repeating a one-pair premise?

The canonical [claim ledger](claims.json), [objection reconciliation](reconciliation.md), and [input hash manifest](input-hashes.json) distinguish reviewed implications, repaired statements, open assumptions and uncompleted certification gates. The next investigation should begin from those distinctions.

As a bounded preparation check, the coordinator reproduced E01's postprocessing from a copied script and the saved exhaustive counts: all 24 rows matched, including eight independent binary-image checks. The [verification record](../../verification/20260906-preparation/math-diagnostics.json) explicitly excludes rerunning the original ternary enumeration. These results check the finite diagnostic calculations, not the asymptotic extractor, any computational assumption, or the discrete Gaussian implementation. The present consolidation additionally checks that every current dependency references the recorded current version, that linked inputs exist, and that archived source hashes remain unchanged. Those delivery checks provide file and bookkeeping evidence; they do not close the remaining mathematical certification gates.
