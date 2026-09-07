"""Exact postprocessing and separate small Boolean-fiber check for E01."""
import collections
import itertools
import json
import math
import pathlib
import time
from fractions import Fraction

HERE = pathlib.Path(__file__).resolve().parent
started = time.monotonic()
raw = json.loads((HERE / 'E01-root-collisions.json').read_text())
rows = []
for case in raw['cases']:
    n, q = case['n'], case['q']
    assert case['enumerated'] == 3**n
    for name, den in [('beta1', 4**n), ('beta_half', 8**n)]:
        hist = case['hist_' + name]
        assert sum(hist) == den
        for d in range(1, min(4, n) + 1):
            coll = Fraction(sum(hist[z] * math.comb(z, d)
                                for z in range(d, n + 1)),
                            den * math.comb(n, d))
            normalized = q**d * coll
            assert normalized >= 1
            row = dict(n=n, q=q, beta='1' if name == 'beta1' else '1/2', d=d,
                       normalized_collision=str(normalized),
                       collision_deficit=float(normalized - 1),
                       tv_upper=min(1, math.sqrt(float(normalized - 1)) / 2))
            if d in (2, 4):
                ix = 0 if d == 2 else 1
                row['binomial_normalized_collision'] = str(
                    Fraction(q**d * case['binomial_' + name][ix], den))
            if name == 'beta1' and n <= 8:
                # Independent calculation from binary secret images, not differences.
                powers = [[pow(r, j, q) for j in range(n)] for r in case['roots']]
                evals = [tuple(sum(p[j] for j in range(n) if s >> j & 1) % q
                               for p in powers) for s in range(2**n)]
                colls, tvs = [], []
                for support in itertools.combinations(range(n), d):
                    counts = collections.Counter(tuple(v[i] for i in support) for v in evals)
                    colls.append(Fraction(sum(x*x for x in counts.values()), 4**n))
                    tvs.append(Fraction(sum(abs(q**d * x - 2**n) for x in counts.values())
                                        + (q**d - len(counts)) * 2**n,
                                        2 * 2**n * q**d))
                direct_coll = sum(colls) / len(colls)
                assert direct_coll == coll
                row['independent_binary_check'] = 'passed'
                row['actual_average_tv'] = str(sum(tvs) / len(tvs))
                row['actual_average_tv_decimal'] = float(sum(tvs) / len(tvs))
            rows.append(row)
out = dict(seed=None, precision='exact integer/rational counts; display bounds use float',
           tail_bound='none: exhaustive finite spaces', rows=rows,
           runtime_seconds=time.monotonic()-started,
           departures=['beta=1 and beta=1/2 are exact effective-posterior diagnostic parameters, not claimed Gaussian widths',
                       'fixed tiny rings establish no asymptotic extraction or hardness'])
(HERE / 'E01-analysis.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
