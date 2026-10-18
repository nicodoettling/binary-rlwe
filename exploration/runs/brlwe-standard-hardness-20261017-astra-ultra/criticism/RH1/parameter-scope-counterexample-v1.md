# RH1 preserved parameter-scope objection, before repair

Frozen input: workers/H/prime-alignment/parameters-v2.md, SHA256 454991f1d39d8fe20937cd2da3d6fe26a4f1ec686c425044c91f7b7a10b48756.

The sentence under “Size and premise qualifications” says:

> The explicit polynomial-VALUE q choice, polynomial k, inverse-polynomial delta and polynomial-time finite scalar parameters give the intended polynomial absolute width.

Taken with the usual bit-complexity meaning of polynomial-time scalar parameters, this implication is not justified by the preceding formulas. C8 allows any \(v_0\ge2\sqrt n\,a\), and its width is proportional to \(v_0\). There is no numerical upper bound on \(v_0\) in this companion's assumptions.

Preserved counterexample family: begin with any compatible supplied polynomial-value \(q\), polynomial \(k\), inverse-polynomial \(\delta\), polynomially chosen \(\kappa\) and its resulting \(a\). Replace a valid \(v_0\) by
\[
 v'_0=2^n v_0,\qquad d'_0=2^{-n}d_0.
\]
All C8 lower constraints continue to hold. In particular \(h_0=v_0d_0\), hence \(\kappa,Q_*,\epsilon_0,a\), are unchanged; uniqueness improves. The new scalar has only \(O(n)\) extra integer bits and a polynomial-time certified algebraic evaluation routine. However
\[
 s'_J=\frac{nq}{\sqrt2d'_0}=2^n s_J,
\]
which is not polynomial in \(n\) when the original width is polynomial and bounded below as in (W3). Thus polynomial-value \(q\) and polynomial-time scalar evaluation alone do not force polynomial absolute width.

Scope of this objection: it does **not** affect H-ALIGN v1, the valid width lower bounds (W1)–(W3), or the conclusion \(s_J\ge512n^2\). The short-relation-v2 introduction and section 5 separately assume polynomial absolute \(s\), so their explicitly conditional formulas remain valid. What fails is using the cited sentence as a derivation of that upper-width premise.

No author file has been changed. A sufficient clarification would make the polynomial absolute-width premise explicit or specify a polynomial-value choice of \(v_0\) and the upstream confidence parameters. This proposed clarification is recorded only after preserving the counterexample above.
