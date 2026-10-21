# M1 exact scoped acceptance

Accepted 2026-10-21T06:43:58.728596+00:00: theorem-only-v2.md (SHA2564deb0d8091f33578a1c08614ae1a2330af998d1bdbe290722434ca990622152b) with proof-v3.md (SHA256ec71050187e534f853548a510252c2af7faa9318fe1b554c114173a6724a4bc7).

RFR2 independently rechecked the complete exact proof, numerical constants, finite scalar implementation and source/bit complexity. FBR2 was fresh fork-none and received only the neutral theorem, definitions and administrative assignment; its complete report and exposure log were sealed before findings. Root verified seals before reading and read both full reports. All151 inherited plus13 new controls have explicit current scope dispositions, with exact CP1 and targeted normalizer/fallback/prerequisite experiments preserved. Structural checks are separately recorded and are not proof certification.

The former scalar/global-fallback ambiguity and omitted explicit primeq prerequisite are preserved. The repair matches the inherited prime/congruence setting and does not add a hardness premise. FBR2 notes that W>4n sqrt(n) alone is too weak to deduce W>12n at n4; the exact stronger lower bound already present in proof-v3 establishes the family requirement, as RFR2 and FBR2 both reconstruct. No further theorem/proof change is needed.

The optional remaining-family-v2.md changes only its dependency label from its preserved v1; the arithmetic received a separate favorable RFR2 audit. It is not a new main hardness theorem. A/B remain accepted in their independent scopes with the current regression addendum; none relies on rejected M1-v1. The norm289 example and entropy-extended composition remain separate provisional companions.

Acceptance is only the algorithmic scope stated in m1-acceptance-v2.json. It supplies no standard hard family, no inverse reduction to binary recovery, and no coherent sampler replacement. Original native goal remains unfinished. Same-model scrutiny is correlated, not formal verification.
