# DD2-FV1 preregistration

Frozen before execution, 2026-10-21 12:34 UTC. Code `dd2-fv1.py`; hash and root slot coordination recorded separately before execution. Deterministic exhaustive arithmetic, no random seed or remote solver. No installation or descendant jobs.

Hypotheses and expected outcomes:

1. At n=2, q=3,5, exact affine cube automorphisms are signed permutations (8 maps); the ring-multiplier subset has 4 maps. At q=5 translation by (2,0) has TV exactly1 from the binary cube.
2. All625 two-query all-negative translation paths at n=2,q=5 hit at most8 of25 hidden offsets. This checks the exact union argument; it does not assert an ideal-decoding lower bound.
3. For n=2,q=5, X²+1=(X−2)(X+2), coefficient Gaussian weight 2^(-z²), independently recombined CRT errors differ from the original law by TV>1/10. Enumerate coefficients |z|≤5 with exact fractions; retain the explicit geometric-series upper bound on omitted infinite mass and charge six scalar tails.
4. One nonzero supplied ideal element in (2+i) decodes two valid rational small-error targets by multiplication, rounding and division. A strict endpoint countercontrol must fail; x=0 is excluded.
5. CP-1 still has21/2000>1/100 and conditional residual21/221<1/10. No multiplication of marginal event probabilities is accepted.

Inputs: ring degree2 only, q3 and5, 625 all-negative paths, at most625 matrices times25 offsets, cutoff5. Largest exact integers arise from rational probabilities with denominator powers up to2^25 before normalization; no unbounded search. Expected runtime well below5 seconds. Hard wall120 seconds, RLIMIT_AS512MiB inside script, full stdout/stderr/exit and `/usr/bin/time -v` receipt retained. At most one DD2 job; global slot must be coordinated with root. Command:

```sh
timeout --signal=TERM --kill-after=5s 120s /usr/bin/time -v -o exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-fv1.resources.txt python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-fv1.py > exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-fv1.stdout.json 2> exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-fv1.stderr.txt
```

The wrapper timeout terminates its process group on expiration; the script launches no children. This is per-job address-space control, not aggregate memory containment. Finite controls support only their stated finite/model scope.
