# SuperSVP mining: B first-pass decision

Status: PROVISIONAL, frozen before21:45UTC2026-10-17. No computational foundation for the original binary-RLWE source is established. Keep the constructive ring transport tools; do not promote a uniform-secret or restricted-ideal statement into the missing binary/fractional-source premise.

## Concrete positive edges

1. Standard RLWE to wide decomposed ring challenges: full concatenated R rank and uniform affine-fiber sampling preserve the entire shared-key planted/comparator law. This uses polynomially many ordinary input samples and preserves secret/error laws. Full-rank failure is explicitly paid. D's initial exact check found no defect.

2. Triangular transport to canonical ring hints: the short-inverse ring map preserves responses algebraically, has a proved ring-specific extraction bound, and pays noise completion and canonical hint resampling. The standard composition has a nonempty polynomial source/noise/sample/hint window. Its operative version is standard-canonical-composition-v2.md, SHA2569a168be29fd5fbf020b253980ace92aac178105d8f7f8bc4b98883713a4ed860. D found the standalone v1 unreachable-key omission; v1 and exact defect are preserved. v2 defines a common T=FAIL kernel retaining A,W,b, without conditioning the uniform keys. No numerical bound changed. The actual repair freeze was21:42:19UTC; the defect record's 'around21:43' is only a draft rounded timestamp.

3. Wide-mask ring decision to search: ring-decision-search theorem/proof v1, hashes0b261e05f1f76026e19bccb48a90e1ec9e4170ddd38327a2f45ac84384342b1c /64a4d46993ae3fa5668ff35979ac61f0a0ac586ae7ce0e61993bdd2e856b3eff. Correct guesses and wrong guesses have explicit full CRT-hybrid laws. Calibration and disjoint diagonal blocks avoid unjustified independence after reusing a key. It replaces the paper's extra ordinary-LWE wrong-guess premise by a statistical rank condition at wider h. It still requires uniform secret shifts and q polynomial in VALUE.

4. Canonical hints to decomposed search/decision: ring-preimage-transport theorem/proof v1, hashes5b0ead1be61417159c0b1733e3accc95e629467d0f19e202249c367b9c208604 /9e8417c4b88ac8a21a283b69f0992302bd13090173223761065d590d00219779. This ring version of the Lemma8.8 mechanism proves its one-row and augmented two-row coset flatness rather than substituting a general matrix theorem. It retains the actual shared-R normalizer, handles rectangular Gaussian completion, and preserves either supplied secret law. It is new and not yet independently reviewed.

5. Previously frozen restricted ideal-to-ring-SIS and uniform-secret quantum search-to-SIS packets have D reports finding no substantive defect within their declared scope/implementation premises. That is not acceptance and not a standard hardness import for low-index ideals.

## Binary and fractional-source discriminating result

The binary Fourier law does not concentrate on the exact SIS kernel; repeated filtering leaves exponential postselection cost. Canonical correction currently yields an augmented kernel relation with W residuals, and the useful joint quotient/modq preimage mechanism is assigned to D.

A genuinely binary-preserving fixed-secret calibration variant is frozen at binary-fixed-secret-root-test-v1.md, SHA256e57a08d1ebb6f8cb2b4b85c58c93952e59c91697267a1391b27869348e202cce. From a binary-secret distinguisher of gap epsilon it can recover an input-dependent single CRT coordinate for an epsilon/2 fraction of secrets, up to explicit amplification losses. It does not prove all-coordinate coverage. Galois/affine restoration preserves the average binary law but changes each fixed-secret acceptance profile. No full binary search-to-decision conclusion follows.

The current ideal-generated SIS public-law packet is degree1. A potential full chain through decision/search inflation requires an arbitrary-degree ideal-generated canonical hint construction and its padded W width. A plausible quotient-block extension exists at the algebraic level but is not frozen or proved here. Even that would leave restricted ideal-family hardness and final binary conversion open. No complete SuperSVP chain is asserted.

## Experiment and operational record

B-SUP-4 full-fiber test: exact15625 W states and15625 planted response checks; uniform comparator preserved. Separate block ranks and one-root rank checks fail as intended. Exit0,0.084211s,10MiB RSS; reservation released.

B-SUP-5 two-row hash/normalizer test: exact5625 key/source checks, Echi²=2000/27 matching the identity, bound80. A729-state shared-R countercontrol gives actual normalizer15/1024 and TV17/40 if it is omitted. Exit0,0.005064s,11MiB RSS; reservation released. All original code, commands, outputs, stderr, hashes and resource records are preserved. No B computation is active.

Next priority is a concrete mechanism reaching binary law or the low-index fractional source, especially the joint quotient correction under D's ownership, rather than extending uniform-secret statements without a source connection. All original cap deadlines remain in force.
