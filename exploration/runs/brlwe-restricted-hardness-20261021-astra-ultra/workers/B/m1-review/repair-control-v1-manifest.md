# B-M1-FV1 provenance

Root reservation timestamp06:01:44 UTC; execution authorized again by message at approximately06:05 UTC. Completed and release requested at06:05:53 UTC, 2026-10-21. One deterministic local process, no random seed and no external dependencies.

Exact command from the workspace root:

    /usr/bin/time -v -o exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/m1-review/repair-control-v1-resources.txt timeout --kill-after=2s 20s prlimit --as=268435456 --cpu=18 -- python3 -I exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/m1-review/repair-control-v1.py > exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/m1-review/repair-control-v1-stdout.txt 2> exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/m1-review/repair-control-v1-stderr.txt

Limits20s wall,18s CPU,256MiB address space. Exit0. /usr/bin/time measured0.05s wall,21,504KiB peak RSS. The script's earlier pre-serialization resource snapshot was17,408KiB; final measured RSS takes precedence. Original stderr is empty. Original full output retains all2,048 tape records and exact law fractions. Every possible tape is enumerated; no selected-success sample is discarded. All integer arithmetic is exact, with the largest specified matrix input129 bits and squared entries257 bits. No Gaussian-tail approximation is used in this finite toy; it tests failure semantics and coupling only.

Code SHA25620fbad63fb6fb9859612481d71a3ebdca1e6b3f77ca0be15bad7f0d2744668ed.
Output SHA2562d2a0d1269126cf4a098babbb8becbe06e96f1f7030e21e38312058b2e85116f.

The cap sidecar was copied immediately before the command to repair-control-v1-cap-before.json. The full live schedule retained graceful08:33:39 UTC and hard08:34:44 UTC; this job finished well before all research gates.
