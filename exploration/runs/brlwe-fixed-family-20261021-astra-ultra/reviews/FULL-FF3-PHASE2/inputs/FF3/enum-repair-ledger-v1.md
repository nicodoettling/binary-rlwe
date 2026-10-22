# FF3-ENUM-v1 proof repair ledger

Recorded before writing the repair. The frozen exhaustive-kernel-proof-v1.md and phase1 seal remain unchanged.

FULL-FF3-ENUM-SIGN-1 (provenance: ../../reviews/FULL-FF3/new-regressions-v1.md) rejects the exact intermediate inclusion A(s-t) in E-[-T,T]^n. With d=s-t, the competitor residual is B-At=E+A(s-t), so the correct inclusion is A(s-t) in [-T,T]^n-E.

Exact counterexample: n2,Q17,T1,s=(1,0),t=(0,0),A=(-2,0),E=(1,0),B=(-1,0). Both residuals pass. A(s-t)=(-2,0) is outside E-[-1,1]^2, but inside [-1,1]^2-E and [-2,2]^2.

Status of the v1 intermediate inclusion: REJECTED. The FF3-ENUM-v1 theorem itself is reopened pending corrected-proof review, not declared refuted: the two translated sets have the same cardinality and both are contained in the symmetric larger box already used in etaQ. The corrected exhaustive-kernel-proof-v2.md changes only this sign and adds a correction banner; all quantitative statements and theorem-only bytes remain the same. Its status is REPAIRED-PENDING-RECHECK. The original full reviewer is not counted as the fresh repair reviewer.

Dependency chain: residual translated-box inclusion -> wrong-candidate probability etaQ -> retained-S one-sample bound -> arbitrary polynomial batch bound -> statistical-existence corollary. Every downstream assertion is pending exact proof-v2 recheck. The exponential cost and the main FF OPEN status are unchanged.
