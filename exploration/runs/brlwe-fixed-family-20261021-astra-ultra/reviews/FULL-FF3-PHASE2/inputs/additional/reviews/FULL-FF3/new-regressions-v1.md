# Newly identified exact proof issue

**FULL-FF3-ENUM-SIGN-1.** The frozen exhaustive-kernel-proof-v1.md says that, for d=s-t and a competing residual in the centered box, A(s-t) belongs to E-[-T,T]^n. The correct set is [-T,T]^n-E because B-At=E+A(s-t).

Exact counterexample: n=2, Q=17, T=1, s=(1,0), t=(0,0), A=(-2,0) modulo17 and E=(1,0). Then B=A*s+E=(-1,0), so both actual s and competing t pass the T-box test. But A(s-t)=(-2,0) does not belong to E-[-1,1]^2, whose first coordinates are 0,1,2. All stated finite premises hold, and E has positive probability under every positive-width discrete Gaussian.

The final theorem bound is not falsified: the correct translated box has the same size, and both signs are contained in [-2T,2T]^n, which is the looser box actually used for etaQ. The disposition is **REJECTED-INTERMEDIATE-SET-INCLUSION-v1; mathematical theorem survives via the stated larger box**. A proof correction must be separately versioned; no frozen author bytes are edited here. This counterexample is recorded before proposing that correction.
