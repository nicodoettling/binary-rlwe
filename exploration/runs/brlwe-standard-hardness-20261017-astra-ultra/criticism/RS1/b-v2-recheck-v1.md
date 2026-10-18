# B-GP v2 source/parameter/complexity recheck

Coordinator nonauthor review, 2026-10-17. Exact theorem SHA256 be7f05d67fc8f2b24fc6b93321c95005f4d7f6e24bab513b2cbaf35c82aeaad7; proof 207a9af38eb570e2a140d88008c0f4bc363f7d3c8a72049c53bbab85798910b4.

The B-v1 complexity PASS in report-v1.md is withdrawn for its literal statement. BT4's bounded-magnitude rational family has arbitrarily large numerator/denominator encodings and proves that magnitude logarithms alone do not bound the computation. The full original report and defect remain preserved. This correction does not invalidate the separately scoped A F1/F2 source review.

V2 charges the full encodings of all rational parameters, ideal bases, input representatives, metadata read/copied, and numerical tolerances. Exact uniform finite-integer rejection has expected polynomial time, which is precisely the claim; this report does not promote it to a bounded-time implementation. Optional challenge sampling is conditional on a supplied ideal and metadata. Joint generation additionally requires an efficient Gen and charges its runtime. Arbitrary common Gen remains legitimate only for the mathematical mixture statement.

The full theorem was read again and the preserved v1/v2 diff was inspected. Statistical endpoint clauses and constants are unchanged: exact finite comparator by translation equivariance; planted loss 2k epsilon/(1-epsilon)+2pi kn/(Pr)+kn nu. The two theta normalizers, coprimality requirement, ordinary HNF/SNF representation, coefficient/canonical scale conversion, and absence of a short-basis oracle remain as in the original review. RF2's independent exact-byte recheck confirms the same scope. The complete BT4 mathematical reconstruction also found no endpoint defect, but it is not a blind review of v2.

Verdict: PASS for the repaired source, representation, parameter and expected bit-complexity scope, pending the fresh BT5 blind gate and separate artifact check. No source hardness, ideal generator efficiency, or standard worst-case connection is accepted here.
