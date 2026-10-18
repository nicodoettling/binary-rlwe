# C-v6 CP1 wording disposition, before repair

2026-10-17T21:43Z; D; PROVISIONAL. This addendum narrows the disposition in c-v6-full-review-v1.md (SHA086e4ae54c19312eac31c0bf8cb6254aadde2aa09dba4ff7f8df8f26fee2589d). Frozen author proof SHA9c57cf10adf32b88a931ebf0cccec0a7705502f78640b71d1743e05954e29b76 is unchanged.

The exact author wording at line124 is:

> On the high-probability correctness event, PRS's page15 induction keeps the true radii in the comparison promise and each successful progress step decreases log radius by at least1/(4K d_H^(3/2)), with conditional progress probability at least1/(10K d_H). Its martingale estimate gives at least T_walk/(10K d_H)-10sqrt(KT) such steps except with probability exp(-K)/2.

This does NOT explicitly define conditional probability given the future intersection of all comparison successes. It therefore does not justify accusing the author of a literal stated false conditional inequality. However, the sentence scopes the probability statement under a global correctness event and leaves the filtration/reference process unstated. The claim cannot be certified from that prose alone: future conditioning would be invalid, and merely citing the primary progress calculation does not identify a valid per-history stochastic process for the modified finite algorithm. A past-history/stopped-process interpretation may be intended, but it is an interpretation requiring a written proof step.

Exact-version disposition: MATHEMATICAL THEOREM NOT REFUTED; FROZEN PROOF FINITE/CP1 GATE OPEN PENDING EXPLICIT CAUSAL SUPPLEMENT. Do not accept C6 as a complete finite proof merely on the phrase 'clarification.' The existing review's section4 supplies a substantive, independently checked completion with unchanged algorithm/constants. It must be frozen as an explicitly adopted proof supplement (or coherent new proof version) and exact-byte rechecked before acceptance. The old bytes and this wording defect remain preserved. No source-paper counterexample is asserted.

The required completion is the causal corrected-decision reference walk, per-history progress/Azuma on that walk, and sequential coupling until the first comparison or near-center bad event. It never conditions fresh steps on a future success event. A new accepted argument must include this or an equally explicit stopped-process proof. The report's all51 regression checks remain conditional on that completion for CP-1, R18 and C03-HC6; they are not unconditional certification of the frozen prose.
