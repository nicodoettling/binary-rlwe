"""E04: exact observation model, numerically truncated wrapped Gaussians.

S_j are fair bits. E_j has mass proportional to exp(-pi*z^2/sigma^2).
Precursor K_j=(q+1)*S_j+E_j mod 2q; public Y_j=K_j mod q.
Thus Y=S+E mod q with A=1 FIXED. This is an observation comparison,
not a uniform-A instance or a cryptographic claim. Coordinates are
independent in this explicitly diagonal example; no ring rotations are used.
"""
import json
import math
import time
from pathlib import Path
import numpy as np

started = time.monotonic()
rows=[]
for n, q, sigma in [(4,17,4.), (8,97,8.), (16,257,16.), (64,4097,64.)]:
    cutoff = math.ceil(12*sigma)+2
    z=np.arange(-cutoff,cutoff+1,dtype=np.int64)
    masses=np.exp(-math.pi*z.astype(float)**2/sigma**2)
    masses/=masses.sum()
    w2=np.bincount(z%(2*q),weights=masses,minlength=2*q)
    w=w2[:q]+w2[q:]
    wdirect=np.bincount(z%q,weights=masses,minlength=q)
    assert np.max(np.abs(w-wdirect))<1e-14
    # Guessing under equal priors is .5 sum max(p0,p1), independently per bit.
    pg_y=.5*float(np.maximum(w,np.roll(w,1)).sum())
    pg_k=.5*float(np.maximum(w2,np.roll(w2,q+1)).sum())
    assert pg_y <= pg_k+1e-14
    rows.append(dict(n=n,q=q,sigma=sigma,rank=1,independent_ring_samples=1,
        public_multiplier='A=1 fixed, not uniform',precursor_modulus=2*q,
        coefficient_guess_public=pg_y,coefficient_guess_precursor=pg_k,
        total_guess_public=pg_y**n,total_guess_precursor=pg_k**n,
        residual_min_entropy_public=-n*math.log2(pg_y),
        residual_min_entropy_precursor=max(0.,-n*math.log2(pg_k)),
        cutoff=cutoff,
        omitted_mass_upper_bound=sigma**2/(math.pi*cutoff)*math.exp(-math.pi*cutoff**2/sigma**2)))
result=dict(id='E04_wrapped_precursor',seed=None,
    evidence='fully specified finite observation experiment, floating-point diagnostic; exact likelihood formula given in code',
    numerical_limitation='Values printed as precursor guessing 1 or entropy 0 are truncation/rounding. The exact wrapped Gaussian has full support and strictly positive residual entropy.',
    runtime_seconds=time.monotonic()-started,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
