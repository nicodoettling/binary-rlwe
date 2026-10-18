# BT5 scalar control-parameter literalization, before v3

Status: implementation qualification preserved before repair; not a statistical counterexample or a claimed intractability result.

BT5 reconstructed the v2 endpoint laws and expected-time implementation, and identified the natural-log ceiling L=ceil(40K ln(16/nu)) as needing either an exact finite-bit justification or a conservative computable integer replacement. This record chooses the latter. Let Lplus=40K ceil(log_2(16/nu)). Exact rational comparison against powers of two computes the inner ceiling. Since ln(x)<=log_2(x) for x>=1, Lplus>=L, so the same rejection-failure bound and integer-translation equivariance hold. The literal finite scalar kernel changes because its maximum number of trials changes, even though all stated Gaussian approximation constants and endpoint bounds remain the same.

The other control parameters K,p involve ceilings of base-two logarithms of rationals and can be computed by exact integer comparisons; N=ceil(rK)+1 is a rational ceiling. Full numerator/denominator bit lengths remain charged. No claim about efficiently evaluating an arbitrary exact transcendental ceiling is needed in v3.

Version2 remains immutable. The coherent theorem/proof v3 will use Lplus explicitly and remain REPAIRED-PENDING-RECHECK. A separate bounded-time wrapper caps exact uniform-integer rejection; that wrapper incurs eta on each endpoint and therefore2eta in advantage, unlike the expected-time kernel's exact comparator.
