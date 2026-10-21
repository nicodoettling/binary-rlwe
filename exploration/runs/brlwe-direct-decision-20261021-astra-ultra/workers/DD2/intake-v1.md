# DD2 intake and frozen first construction, v1

Recorded 2026-10-21 12:26 UTC. Status: exploratory, no accepted claim.

The native run began 12:19:00.281989 UTC. Gate 13:04:00.281989; discovery cutoff 15:04:00.281989; delivery 15:54:00.281989; workers and experiments stop 16:04:00.281989; final checkpoint 16:14:00.281989; graceful shutdown 16:17:55.281989; hard cap 16:19:00.281989. The cap sidecar was read at intake and 12:25:54, reports running, and retains its original timestamps. No restart, external session, goal creation, or descendant agent was performed.

Startup evidence: root's `coordinator/runtime-verification.json` records DD2 spawn as `gpt-6-astra`, reasoning `ultra`, with `fork_turns=none`; the launcher command explicitly sets `service_tier="default"`. The available spawn API has no tier parameter. This is configuration evidence, not billing telemetry. The launcher's `features.fast_mode=true` capability flag does not supersede its explicit default tier; DD2 changed neither setting.

Read: Package PLAN in full; mathematical-proof-audit SKILL and both audit-protocol/probability-regressions references; RECENT final/programme decisions; PRS17 local text Sections 2.4, 6 and 6.1; OLD finite multiplier theorem-v8, proof-v9 and algorithm-v2; OLD binary-fixed-secret-root-test-v1. The inherited finite hidden-center machinery is used by reference and will not be rebuilt. RECENT's 164-entry regression registry remains an intake dependency; a compact current applicability registry will retain every ID and provenance. No acceptance claimed before complete applicability review.

## Original interface

PRS17 Lemma 6.8, printed p.20: given factorized q, I∨, target coset e+I∨ with canonical infinity bound d, r≥sqrt(2)qη(I), and elliptical samples x~D_(I,rvec), produce continuous-torus RLWE with uniform secret in R∨/qR∨ and errors of embedding widths

    r_i'^2 = (r_i |e_i|/q)^2 + (rd/q)^2.

Definition 2.15 chooses one uniformly random secret and one elliptical error law for the entire sample oracle. In Lemma 6.6, e is itself sampled from a spherical continuous Gaussian and induces the Υα mixture of error laws. Secret randomization is explicitly cited as the reason the secret can be uniform. Neither coefficient-binary secrets nor coefficient discrete-Gaussian errors follow from this statement.

## DD2-CANCEL-v1: exact binary masking after integral cancellation

Freeze R=Z[X]/(X^n+1), n a power of two, integral ideal I, modulus q≥2. Let the rational target be T=λ+e with λ∈L=qI^-1. The unknowns are λ and e. The reduction knows T, I, q and receives independent samples x_i from specified Gaussian laws on I; they are not silently available from an ordinary basis. Let g be a known guess and h=e−g.

For one k-sample call, choose S uniformly from {0,1}^n once; choose A_i independently uniform in R/qR; choose x_i independently from the supplied sampler; choose all base-noise/rounding coins independently. Since x_i λ∈qR,

    x_i(T−g) mod qR = x_i h mod qR.

This cancellation is exact before any Gaussian approximation. Responses are

    B_i = A_i S + K(x_i(T−g)+G_beta) mod qR,

where G_beta is continuous Gaussian in coefficient space, and K is scalar Gaussian randomized rounding to Z^n at width τ. The kernel is integer-translation equivariant, so the unknown x_i λ cancels even through K. Choose beta²+τ²=σ². At h=0 the rounded law is exponentially close to the exact coefficient discrete Gaussian D_(Z^n,σ) when τ and σ meet scalar smoothing bounds, with every rounding normalizer retained. Conditional on S, errors are independent of A and across samples. S is fresh for each oracle invocation, and shared across its k samples. It is not the unknown translate S+s(T).

The continuous proxy has covariance beta² Id + M_h V M_h^T in coefficient coordinates, followed by a fixed K. V is the canonical elliptical covariance of x. Under an explicit posterior-smoothing hypothesis for I, it depends on a selected complex residual only through exp(t)|h_j|. The other residual embeddings remain nuisance parameters fixed across that query family. This profile claim still needs its exact smoothing and finite implementation charges.

This avoids the binary-secret defect but removes the 1/q in PRS17's product term. The decoding radius scales as σ/r on the qI^-1 target, versus the elementary sample-based radius q/r up to logarithms. It therefore does not currently supply a useful hardness bridge.

## DD2-ONE-SAMPLE-v1: deterministic elementary comparison

Given any nonzero x∈I, if ||x e||_(coefficient,infinity)<q/2, then

    z=round(xT/q) ∈ R, lambda_hat=qz/x

recovers λ exactly. Indeed xλ/q∈R and coefficient rounding removes xe/q. Ring division is rational field arithmetic; final membership in qI^-1 is exact. A sufficient condition is ||e||_(canonical,infinity)<q/(2||x||_(canonical,infinity)), because inverse canonical evaluation has coefficient infinity norm at most canonical infinity norm. Only one nonzero sample is needed, not a full-rank list. This is a deterministic observation, not a claim about sampling nonzero x under an unspecified Gaussian law.

For broad supplied Gaussian samples, typical ||x||_(canonical,infinity) is O(r sqrt(log n)); hence the binary profile radius σ/(r poly(n,k,1/delta)) is within this elementary range when σ/q is sufficiently small. A direct conditional sampler theorem would not improve ordinary decoding in that regime.

## Next alternatives

1. Recover the lost modulus through a binary-compatible unknown-secret map rather than integral cancellation.
2. Test whether uniform-secret masking can be transferred to binary via shifts, Fourier averaging, or a ring-compatible dimension expansion; retain the exact shared-secret/public-law constraints.
3. Isolate small-modulus/CRT and tower embeddings with all rank, degree and noise costs. A failed translate-of-cube mask does not retire these different mechanisms.

All current statements remain PROVISIONAL or OPEN. No experiments have run.
