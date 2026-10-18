# B Gaussian-periodic v2 exact-byte repair review

2026-10-17. PROVISIONAL nonblind review; no acceptance authority. No contact with isolated blind reviewers and no experiment.

Fresh file hashes match the frozen statement be7f05d67fc8f2b24fc6b93321c95005f4d7f6e24bab513b2cbaf35c82aeaad7 and proof207a9af38eb570e2a140d88008c0f4bc363f7d3c8a72049c53bbab85798910b4. The full v1 proof was previously read and analyzed in full-report-v1.md. Every v1-to-v2 byte change has now been inspected. The only substantive changes are the total-encoding runtime model and qualification of joint challenge generation; constants, scalar kernel, exact equivariance and both endpoint arguments are unchanged.

The repair addresses the literal defect. For r=2±1/(2^H+1), fixed nu=1/4 and K=8, computing N distinguishes17 from18 although log r stays bounded. V2 explicitly charges both numerator and denominator lengths of every rational, not only its numerical magnitude. It also charges metadata that is read/copied, sample representatives, ideal basis, every auxiliary precision input and the downstream distinguisher. Expected polynomial time is the claim, so exact uniform-integer binary rejection is consistent here; it must not be silently relabeled bounded-time.

The optional finite challenge sampler is now explicitly conditional on a supplied J and metadata. An arbitrary Gen is still legitimate for the pointwise statistical statement and common-mixture conclusion, but efficient JOINT sampling requires an efficient Gen and includes its runtime. This separates a mathematical joint law from its computational availability.

The exact comparator still follows from the integer-translation-equivariant finite scalar kernel and uniform coset selection. The planted comparison still charges both the shifted-coset and convolution-center theta normalizers, finite input rounding, and kn scalar approximation errors. Common J metadata stays retained, and the per-sample product law is only asserted conditional on J and supplied metadata. No new endpoint or conditional-independence issue was found.

Disposition: recommend the repaired conditional finite bridge for coordinator/fresh-blind consideration. This is not acceptance of a source hardness premise or A's instantiated F3. B v1's literal runtime defect remains preserved and no certification is transferred from it.

Regression scope: the51 exact imported dispositions in regression-review-v1.json continue to apply to the UNCHANGED endpoint/proof clauses, with a new explicit implementation check for A-PPT-LEDGER-SCOPE and a new control RF2-B-GP-V1-SCALAR-ENCODING. The latter is rejected for v1 and repaired in v2 by full encoding charges. RF2-B-GP-ARBITRARY-GEN is repaired by the supplied-J conditional statement. No ideal-generator efficiency, source hardness, or global acceptance follows from these local repairs. CP1 remains handled by same-J conditional product kernels and full joint laws; no sequential product is restored.
