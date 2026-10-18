# Preserved transcription defect in rounded-source-check-v1

2026-10-17 22:07 UTC. PROVISIONAL; original bytes retained.

Affected file SHA256 d1ca275ec12d9d70de418a59ca3683b22865c7254ac8af96f515db4e0b007eb2. The first paragraph transcribed flattened `nl` and `n2l` from CZZ2018 Corollary1 as powers n^l and n^(2l). The factors are n*l and n^2*l. The later phrase “grows by n^l” has the same defect. Primary indexed PDF text was rechecked at https://eprint.iacr.org/2018/536.pdf, Theorem2, Corollary1 and Lemma6, browser result turn426search0. Lemma6 gives per-coordinate Renyi factor 1+alpha/(c beta); the nl-fold product gives beta=Omega(n*l*alpha). Corollary1 additionally has q/p=Omega(n^2*l*alpha). This repairs a notation transcription, not the endpoint map. The bounded-secret parameter still grows with n for fixed positive l, and the scoped binary-support mismatch conclusion survives. No proof or hardness claim relies on the incorrect exponent.

Version2 changes exactly these three mathematical transcriptions and adds a provenance sentence. No other constants or endpoint laws change.
