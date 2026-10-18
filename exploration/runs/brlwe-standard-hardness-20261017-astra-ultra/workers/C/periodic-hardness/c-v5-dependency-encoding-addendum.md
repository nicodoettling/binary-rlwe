# C-OHCP-v5 dependency encoding clarification

Metadata-only dependency clarification; immutable C-v5 theorem/proof bytes are unchanged. C-v5 already explicitly charges all scalar encodings/evaluation costs, bounded scalar-rejection fallback, actual t-dependent precision, and global adaptive error budgets.

The authoritative compatible B dependencies are now:

- gaussian-periodic-theorem-v2.md SHA be7f05d67fc8f2b24fc6b93321c95005f4d7f6e24bab513b2cbaf35c82aeaad7;
- gaussian-periodic-proof-v2.md SHA 207a9af38eb570e2a140d88008c0f4bc363f7d3c8a72049c53bbab85798910b4;
- elliptical-multiplier-sampler-v2.md SHA 9077cb68d8a6f4fd29fa276d1819518980e81b492852a86e35e5410ef9c9cf2b.

The B-v2 repairs concern complete scalar-encoding runtime statements, with the same analytic laws. C-v5 proof Section7.3 instantiates the scalar algorithm at the integer width a and includes the extra bounded integer-rejection cap; its Section7.4 and final paragraph charge all encoding/evaluation costs. No source law, comparator, parameter, normalizer, or new approval is changed by this dependency update. Blind/nonblind reviews remain separately scoped.
