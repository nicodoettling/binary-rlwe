# DD2-AM-FV1 preregistration

Frozen before execution 2026-10-21 12:45 UTC. Code `dd2-am-fv1.py`; deterministic exhaustive rational/integer arithmetic, no seeds. Bind code hash and root global-slot coordination before execution.

Hypotheses/expected outcomes:

1. Exhaust all nonzero ternary f in degrees2,4,8 (8+80+6560=6648), compute integer multiplication determinants, verify1≤|Normf|≤n^(n/2), and for each of16 explicit split primes verify q^(number of zero roots) dividesNormf. Verify product divisibility over distinct primes. For every nonzero root count, independently compute modular matrix rank and check nullity. Expect degree8 multiplicity≥2 witness; retain exact f,q,norm.
2. For binary fibers of J=R, J=2R and the norm3^(n/2) ideals J=(3,X^(n/2)+X^(n/4)−1), compute every K_q exactly and verify the max/pair/diagonal inequalities and average bound with the exact empirical pair-collision maximum. Radical comparisons use rational squaring with sign checks; no floating-point certification.
3. Negative controls: repeating a prime must break the claimed norm-product divisor in the saved multiplicity witness. At ramified q2, X+1 in degree8 has norm2 and nullity1; treating the repeated polynomial root as multiplicity8 would incorrectly demand2^8|2.
4. Exercise explicit auxiliary-congruence prime-list algorithm for (n,M,Qmin,D)=(2,2,11,1),(4,3,25,9),(8,3,101,81). Verify roots/primality/congruence/distinctness/lower bound/gcd after filtering. These finite cases do not prove Linnik's theorem or calibrate its universal constant.

Inputs: exact prime lists are frozen in code; largest supplied q769, n8, ternary vector length8, determinant magnitude≤4096. Prime-list construction has explicit finite small inputs and relies only on deterministic trial division. Expected wall time<20 seconds. Hard timeout120 seconds, RLIMIT_AS512MiB, no child jobs. Full output, stderr, exit and time/RSS retained. Command:

```sh
timeout --signal=TERM --kill-after=5s 120s /usr/bin/time -v -o exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-am-fv1.resources.txt python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-am-fv1.py > exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-am-fv1.stdout.json 2> exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD2/dd2-am-fv1.stderr.txt
```

No execution before root slot coordination. Timeout owns the foreground process group; script spawns no descendants. Limits are per-job, not aggregate memory containment.
