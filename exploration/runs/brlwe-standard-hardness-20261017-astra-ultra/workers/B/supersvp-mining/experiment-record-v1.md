# B-SUP-1 exact finite control

Coordinator authorized the sole active computation at <=30 seconds wall time and <=256MiB. The code sets RLIMIT_AS=268435456 bytes and RLIMIT_CPU=30 seconds; the command also uses timeout30s. It completed and the reservation was released to the coordinator at21:08:18 UTC. Exit0, empty stderr. Script-measured elapsed time0.07124558504438028 seconds; peak RSS11264KiB. The exec tool reported a distinct wall_time_seconds0.00000408 measurement; these boundaries are recorded without equating them.

Input: n=2,q=5, CRT roots2,3, h=1,2; independent uniform coefficient-ternary sources. Exhaustive exact Python integer/Fraction arithmetic, no RNG seed. Floats only record resource timing. There were50850 hash evaluations and5625 triangular comparator points, plus exact projection and trapdoor controls.

The exact averaged one-output chi-square values are280/81 for h=1 and3608/6561 for h=2, matching the frozen CRT identity. The source projection collision probabilities are17/81,17/81,1/9 for the two singleton supports and their union. Shared-key two-output chi-square differs from the false product-of-averages expression. The joint total-variation values satisfy the two-column hybrid bound. Conditioning the key to zero makes extraction fail, and retaining the source gives deterministic-graph advantage24/25 (624/625 for two outputs). A zero divisor has annihilation probability1/5, refuting the inappropriate general-matrix2-universality value1/25. Every retained triangular coefficient gives a bijection on comparator responses; the explicit L=2 transported ring trapdoor identity also passed.

These finite checks support only their exact identities. They do not establish asymptotic extraction without the proof, any sampler theorem, or any hardness claim.

Artifacts:

| File | SHA256 |
|---|---|
| control-v1.py | ce0f1625f640df360fc470782a22ff1570ec2dfed0a04ff6c70d53eeefa6fa5a |
| control-v1.command.txt | cb882ca53ec8f6125a713c3b1ea49addae310c1e5ed0eb6397d38f25588fbd66 |
| control-v1.stdout.json | fb3bb308f243c1d2264d513bf4baf309d5fce16313b5a7b234467e20b3063d27 |
| control-v1.stderr.txt | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

No experiment remains active or reserved.
