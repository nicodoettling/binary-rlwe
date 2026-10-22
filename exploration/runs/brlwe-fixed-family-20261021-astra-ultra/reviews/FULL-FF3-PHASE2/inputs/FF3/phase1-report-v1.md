# FF3 constructive phase report

Author freeze, PROVISIONAL pending nonauthor full/blind review. Main FF remains OPEN. This worker does not determine SV or establish a hardness foundation, and this freeze does not terminate the protected programme.

## Positive constructions

1. **FF3-TWOSECRET-v1** gives an exact normalized unknown-label kernel for two candidate ring secrets separated by a unit, assuming a noise kernel H preserving uniform. Both full planted conditional laws and comparator are proved, and arbitrary shared-label batches follow from fresh conditional kernels. The whole n1 binary experiment is included; the n>=2 full cube is not.

2. **FF3-ENUM-v1** gives an explicit nonlinear positive kernel for ALL coefficient-binary secrets with negligible retained-secret batch error at polynomial-value auxiliary parameters and exact target coefficient Gaussian law. Enumerate2^n candidates, accept a unique small residual, then generate fresh target samples. The determinant/rank inequality includes nonunits. Its exponential runtime is explicit; this proves statistical existence in the stated regime and does not solve FF.

3. **Finite unrestricted kernels** at n2Q3→q2 with nonzero rational source noise reserve have exact rational certificates. They preserve every fixed-secret law and uniform comparator. These finite surrogates are not Gaussian theorems.

4. **Finite correlated ring-H escape, FV9.** A ring-level H depending on the source and target residual zero-count classes has four exact3-by3 weight-channel vertices. Combining two such H channels along cube edges, with observation-dependent edge/vertex selection, gives an EXACT n2 full-cube kernel. Its121nonzero selector weights were solved over Q and checked against every source row, all four planted endpoints, and comparator. This strictly escapes the coefficientwise H exclusions below. The radial H itself has a simple polynomial-state representation; the selector table has no proved scalable factorization yet. It remains a promising constructive route, not an exhaustion item.

5. **FF3-TWOEVENT-v1** gives an explicit two-event normalized noise kernel with both endpoint normalizers. Its Gaussian instantiation note shows how strong source-noise reserve can satisfy the likelihood inequalities; finite capped implementation remains unsealed. It does not solve the unknown full-cube residual-selection problem.

## Exact finite exclusions and scope

- Independent application of H to four cube residuals violates their affine consistency relation unless every H row is deterministic. The n2 named bad event has positive exact probability. This restriction excludes independent residual sampling, not coupled kernels.
- Conditioning the product onto compatible target pairs and normalizing each row does not repair endpoints: FV5 has planted TV≈0.1180482685 and comparator TV≈0.0200531575, with exact rational witnesses and every row normalizer retained.
- Every fixed positive mixture of the FV6 cube-edge channels fails. At n4 the retained-secret event D=C*S has target probability81/256, while every edge channel has probability at most1004756811/9885304832. The exact gap is2123015421/9885304832. This is a convex separation certificate, independent of LP status.
- For the fixed symmetric scalar H, even arbitrary observation-dependent edge selection fails at n2: its zero-residual probability is at most9011/16224<9/16. Exact Farkas certificates also cover public-only selection.
- FV8 permits ALL coefficientwise scalar-H vertices, independent choices for both residual branches and every coefficient, and arbitrary observation-dependent mixtures. An exact rational Farkas certificate rejects this entire finite class. The smaller branch-isotropic LP returned UNKNOWN; no solver status is upgraded, but its model is a subset of the certified larger class.
- FV9 is a positive counterexample to extending the preceding exclusion to correlated ring-level H. No general modulus-transfer impossibility is asserted.

## Evidence and resources

Every mathematical experiment was registered before a fresh root slot was granted. FV1 aborted before a mathematical result due to a solver thread resource error; it is preserved. FV2 through FV9 completed under120s and512MiB address-space limits, each in at most1.51s and at most122MiB peak RSS. Actual commands, stdout, stderr/resources and exact certificates are in experiments/. No background process remained after each completed job. Scalar solver discovery used one thread; exact Fraction postchecks carry the conclusions.

All203 inherited regression IDs/provenance are retained in inherited-regression-references.json. New controls were appended before attempted repairs. CP-1 remains rejected:21/2000>(1/10)^2. Shared-secret and fresh-secret two-sample targets differ by15/256 in the exact finite control; the former is preserved. No new claim has received the required independent-role exact-version full and blind reviews yet; all analytic candidates and finite certificate summaries remain author-provisional.

## Immediate constructive frontier

Compress the FV9 selector by exact likelihood-profile symmetries, then test whether it depends on a polynomially computable collection of residual statistics rather than all2^n candidate residuals. A general ring-level H based on squared coefficient norm can have polynomially many numeric energy states when moduli have polynomial value, but wrapped-Gaussian classes and conditional sampling need exact normalization/tail accounting. Selecting the unknown-secret residual remains the load-bearing gap. An unrestricted n4 LP would add little to statistical existence alone, so it was not run.

The existing positive finite selector is allowed to depend on the observed pair(A,B), never on the true secret. Extending it by giving an autocorrelation invariant or a candidate list to the reduction would require charging that advice in the fractional-source posterior; common latent-G completion cannot be reused after unproved conditioning.
