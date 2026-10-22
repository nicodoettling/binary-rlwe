# FF3 exact review packet index

Author-provisional packet. Read statements without proofs for a fresh blind review; do not treat this author's conclusions as accepted.

Analytic theorem-only inputs: two-secret-channel-statement-v1.md; exhaustive-kernel-statement-v1.md. Corresponding full proofs: two-secret-channel-proof-v1.md; exhaustive-kernel-proof-v1.md. The two-event-noise-kernel-v1.md is a separate constructive lemma/instantiation note and has no theorem-only blind split yet.

Finite model: finite-kernel-statement-v1.md. Unrestricted exact positives: experiments/ff3-lp-fv2.py and ff3-exact-fv3.py, their registrations/outputs, and reserve_n2_a-exact-witness.json, reserve_n2_b-exact-witness.json. Identity, uniform-source negative and wide-noise negative controls are retained in the same experiment directory.

Full conditional controls: experiments/ff3-constructive-fv4.py and output; normalized correlated-product counterexample: ff3-normalized-fv5.py and normalized_n2-witness.json. Fixed edge-mixture convex certificate: ff3-pair-mixture-fv6.py, summary and pair-mixture-n4-witness.json. Adaptive symmetric-H exclusions: ff3-adaptive-edge-fv7.py and both adaptive-edge witnesses. Complete coefficientwise-H exclusion: ff3-asymmetric-fv8.py and asymmetric-coefficientwise_vertices-witness.json.

Positive correlated ring-level construction: experiments/ff3-radial-fv9.py, radial-ring-H-vertices.json, radial-radial_ring_vertices-witness.json, output and registration. Every selector row, conditional endpoint and comparator is exactly checked by the frozen code. Its fixed finite parameter set is n2,Q3,q2, source noise(7/8,1/16,1/16), target noise(3/4,1/4); do not replace either by a Gaussian.

Mandatory review challenges: target quantifier order; source normalized reserve; exact retained-secret batch coupling; nonunit difference ranks; enumeration cost; scalar/ring coefficient correlation; row and endpoint normalization; lack of an efficient general selector; finite surrogate versus Gaussian scope; and no unsupported sequential products. All203 old regression references and new controls are in inherited-regression-references.json and regressions.json. Files will be bound by author-phase1-seal-v1.json; later constructive files must not silently replace this packet.
