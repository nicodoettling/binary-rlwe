# Preserved normalizer objection to LSW Theorem 1

Status: **PROVISIONAL exact counterexample**, needs independent source/math recheck. Frozen before any proposed repair. Primary: Lai–Swarnakar–Woo, [publisher PDF](https://cic.iacr.org/p/2/3/21/pdf), Theorem1 and proof on printed pp.10–11. The text explicitly asserts equality of the two discrete joint laws, with no smoothing hypothesis in Theorem1. D's primary-browser extraction returned the whole statement/proof. This objection does not by itself refute a repaired approximate Theorem3 under its stronger smoothing conditions.

Take scalar lattices Λ0=Λ1=Z, Σ0=Σ1=1, L=1. These satisfy every stated Theorem1 hypothesis, including L^TΛ0⊂Λ1. Then

    Θ0=1/2, Θ1=2, c(y)=y/2.

The first experiment draws independent X,E~D_1 and returns (X,Y=X+E). Its Y marginal is

    Pr[Y=y] ∝ exp(-πy²/2) ρ_(1/sqrt2)(Z-y/2).

This follows by the exact identity x²+(y-x)²=y²/2+2(x-y/2)². The second experiment draws Y~D_sqrt2 and then X~D_(1/sqrt2),center=y/2. Its Y marginal is exactly proportional to exp(-πy²/2), with no shifted-theta factor.

The shifted normalizers differ strictly:

    ρ_s(Z)-ρ_s(Z-1/2)
      =2s sum_(j odd) exp(-πs²j²)>0,  s=1/sqrt2.

The identity follows directly from the absolutely convergent Poisson theta formula. Hence

    Pr_first[Y=1]/Pr_first[Y=0]
      =exp(-π/2) ρ_s(Z-1/2)/ρ_s(Z)
      <exp(-π/2)
      =Pr_second[Y=1]/Pr_second[Y=0].

The two joint laws cannot be identical. The proof's last proportionality before D2 silently makes a normalization constant depending on y1 disappear: normalizing the conditional Gaussian D_(Λ0,sqrtΘ0,c(y1)) introduces ρ_(sqrtΘ0)(Λ0-c(y1)). This is the same structural hazard as the project's shifted-normalizer regressions.

Immediate downstream consequence: B's semiadaptive-hints-map-v1.md currently imports an unqualified Theorem2/3 simulation distance based on this exact Theorem1 identity. That distance requires rechecking. The explicit simulator's uniform comparator remains exact by its fresh designated-response blocks; the planted simulation loss must include a valid bound for the missing marginal normalizer before its claim is accepted.

No numerical experiment was run. This exact scalar witness is preserved first. Stronger smoothing in Theorem2/Condition2 may permit a negligible-loss repair; such a repair must be separately versioned and reviewed rather than treating the claimed exact identity as correct. No claim is made that all semiadaptive leakage results or all public reductions fail.
