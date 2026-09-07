"""E03 deterministic scalar diagnostic; not a hardness experiment.

Gaussian width sigma means exp(-pi*z*z/sigma**2). We wrap its
integer masses modulo each odd q. The cutoff K=ceil(12*sigma)+2
has omitted unnormalized mass <= sigma**2/(pi*K)*exp(-pi*K*K/sigma**2).
Finite precision calculations are diagnostic; the symbolic identities in
the C03 dossier establish the asymptotic claim.
"""
import json
import math
import time
from pathlib import Path
import numpy as np

started = time.monotonic()
rows = []
for sigma in [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]:
    q = 2 * math.ceil(6 * sigma) + 1
    cutoff = math.ceil(12 * sigma) + 2
    z = np.arange(-cutoff, cutoff + 1, dtype=np.int64)
    masses = np.exp(-math.pi * z.astype(float)**2 / sigma**2)
    p = np.bincount(z % q, weights=masses, minlength=q)
    p /= p.sum()
    uncentered = (p + np.roll(p, 1)) / 2
    centered = (np.roll(p, 1) + np.roll(p, -1)) / 2
    assert abs(p.sum() - 1) < 1e-14
    assert np.max(np.abs(p[1:] - p[:0:-1])) < 1e-14
    t = math.pi / sigma**2
    reverse_uncentered = float(np.sum(p*p / uncentered))
    reverse_centered = float(np.sum(p*p / centered))
    forward_centered = float(np.sum(centered*centered / p))
    reverse_bound = 1 + math.exp(t) * (math.cosh(2*t) - 1)
    forward_identity = math.cosh(2*t)
    # Wrapping contracts divergence, and for these q the discrepancy is tiny.
    assert reverse_centered <= reverse_bound * (1 + 1e-12)
    assert forward_centered <= forward_identity * (1 + 1e-12)
    rows.append(dict(sigma=sigma, q=q, cutoff=cutoff,
        omitted_mass_upper_bound=sigma**2/(math.pi*cutoff)*math.exp(-math.pi*cutoff**2/sigma**2),
        wrapped_M2_P_over_uncentered=reverse_uncentered,
        wrapped_M2_P_over_centered=reverse_centered,
        wrapped_M2_centered_over_P=forward_centered,
        unwrapped_forward_exact=forward_identity,
        reverse_centered_upper_bound=reverse_bound,
        sigma4_times_centered_chi2=(reverse_centered-1)*sigma**4,
        sigma2_times_uncentered_chi2=(reverse_uncentered-1)*sigma**2,
        total_variation_uncentered=float(np.abs(p-uncentered).sum()/2),
        total_variation_centered=float(np.abs(p-centered).sum()/2)))
result = dict(id='E03_centered_noise_renyi', seed=None,
    evidence='floating-point diagnostic with explicit Gaussian truncation; no asymptotic or hardness inference from numerics',
    rank_degree_sample_ledger='scalar noise diagnostic only; C03 algebra separately preserves degree n and rank one with one sample',
    runtime_seconds=time.monotonic()-started, rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
