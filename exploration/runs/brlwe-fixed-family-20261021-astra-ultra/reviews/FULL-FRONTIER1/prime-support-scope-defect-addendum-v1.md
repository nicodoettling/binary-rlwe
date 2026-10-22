# Immutable scope correction to the sealed FRONTIER1 review

This addendum leaves every artifact covered by review-seal-v1.json unchanged. It corrects the scope disposition of one sentence of SV-PRIME-SUPPORT-v1, whose frozen statement hash is b7d9c43af7dedfcaeec509b9693dd374b7f05f197ea9a3bd0fbc09e9c0967df9 and proof hash is 12967509eed52f8fe2896e7d341a792beacbd06cd4a50a43a07bc04c1ea4014d.

The statement assumes fixed rho<1 (inheriting the eligible range including rho=0) and then says that the family contains eligible exponential-index ideals with unbounded support and trivial stabilizer. Taken literally at rho=0, this existence sentence is false: N(J)<=2^(0*n)=1 forces J=R, so no exponential-index family is eligible. The proof's construction instead explicitly chooses 0<rho<1.

**Exact scoped verdict: REJECTED-LITERAL-EXISTENCE-SENTENCE-v1 at rho=0.** The contraction bound, factorization-free algorithm, sufficient support criterion and decoding-radius conclusion are unaffected and retain their prior full-review pass. The sealed report identified the positive-rho interpretation but should have recorded the literal existence-sentence defect instead of an unqualified whole-candidate pass. This addendum makes that distinction explicit; no blanket acceptance of v1 is recommended.

The coordinator has announced a v2 repair that states 0<rho<1 for the existence clause. This referee has not reviewed or accepted v2. Fresh blind and fresh full exact-v2 gates remain pending; no acceptance is inherited from the old review. The rejected v1 bytes and the original seal remain preserved.

Counterexample ID: FRONTIER1-PRIME-RHO-ZERO. Parameters: any power-of-two n>=2, rho=0, J=R. Expected outcome: core theorem valid, exponential-index existence clause rejected. No numerical experiment is needed for the integer norm argument.
