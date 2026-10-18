# RH1 independent narrow parameter-v3 recheck

Parent separately authorized these exact files after the original review began:

- parameters-v3.md: c7174507a45e93a6a42f392b3ee82f3ab10c3235295c62230b521d8a8ab388fa
- parameter-recheck-pointer-v3.md: ad1df2204d76ff94a48d0a0d5d0422f0cb1fb1ec884ac2e4e9b2a92080a78016
- freeze-receipt-v3.json: b61217a5e695d9a1db20c937182a4ab4705f9308d85605fe0fc331ff90944def

Read every line and independently rechecked the changed magnitude claims. Recommendation: **SUPPORTED repair**, with no acceptance action. The old v2 counterexample and rejection remain intact in parameter-scope-counterexample-v1.md and full-proof-report-v1.md.

V3 explicitly says that polynomial absolute width is an additional magnitude premise unless the actual \(v_0\) is bounded in value. It preserves the \(2^n v_0\) counterexample and distinguishes a sufficient choice from every allowed choice.

The sufficient schedule is valid. Polynomial-value \(q,k,\kappa\), inverse-polynomial \(\delta\), and \(\log(1/\zeta)\le\operatorname{poly}(n)\) imply polynomially bounded \(\log(1/\epsilon_0)\), since \(Q_*\) is polynomial in \(\kappa\). The specified Up-derived \(a\) is therefore polynomially bounded in value. Choosing polynomial-value integer \(\chi\ge a\) and \(v_0=2\sqrt n\,\chi\) gives polynomial absolute \(s_J\) in A's \(w_B=\ell^2\) regime by the exact equality in (W1).

There is no need for an unbounded uniqueness enlargement in that regime. At \(v_0=2\sqrt n\,a\),
\[
 \frac{d_0}{q}=\frac{\delta w_B}{64nkaq}.
\]
Condition (W2) gives \(d_0/q\le1/(512\sqrt2\,n)\). Since \(D_F^{1/n}<2\), this is strictly below \(1/(4D_F^{1/n})\). Larger \(\chi\) only improves uniqueness. Thus the proposed magnitude schedule is compatible with the existing C8 constraint.

The lower-width estimates (W1)–(W3), main H theorem/proof and short-relation-v2 bytes are unchanged. The repaired conclusion is conditional on the stated magnitude schedule or explicit polynomial-width premise. It establishes no new recovery algorithm, modulus generation procedure, ideal-family reduction or unconditional DGS availability. No experiment was needed or run for this algebraic recheck.
