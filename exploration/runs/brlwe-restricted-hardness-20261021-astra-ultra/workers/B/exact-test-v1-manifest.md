# B-FV1 provenance

Reservation requested and granted by root at approximately05:47 UTC, 2026-10-21; completion and immediate release request reported before05:49 UTC. No random sampling, seed or outside dependency. Source and all fixed inputs are in exact-test-v1.py.

Exact command (workspace root working directory):

    /usr/bin/time -v -o exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/exact-test-v1-resources.txt timeout --kill-after=2s 120s prlimit --as=536870912 --cpu=110 -- python3 -I exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/exact-test-v1.py > exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/exact-test-v1-stdout.txt 2> exploration/runs/brlwe-restricted-hardness-20261021-astra-ultra/workers/B/exact-test-v1-stderr.txt

Hard limits:120s wall,110s CPU,512MiB address space. Exit0, measured wall0.49s, maximum RSS19,456KiB. No stderr. exact-test-v1-exit.txt records the process status, exact-test-v1-cap-before.json preserves the cap sidecar, and the full /usr/bin/time record is retained. The wrapper's stdout was read in full. Exact rational output, including Gaussian success numerators/denominators and tail numerator/denominator, is retained in exact-test-v1-output.json.

Source SHA256 b9cb08b74125185a35ffe52eaed44a8ca215867e40378c803449b87e40c6754f.
Output SHA256 99e62ccd8e06d0b365dc2bfd37cac64be5427a3b5773f5a222af1b753764c017.

Work:40 rank-two HNF lattices;304 exact ternary signed-rotation classes in degree8;152 high-index cases with all256 cube vectors enumerated; old norm2176/image248 replay; CP1 exact fractions. The Gaussian computation uses t^2=pi/log(16/15), r=t^2/2, but every enumerated weight is rational. Truncation to [-32,32]^2 is charged by the rigorous bound124(15/16)^1089/[1-(15/16)^67] <3.767e-29. Common integer weight representation uses approximately8192 bits before summation (under8300 bits including the sums), with no floating arithmetic in the assertions. Floats in the output are display-only. All attempted candidates, determinant counts and successful high-index fiber records are kept in the output; there is no selected-success inference.

This bounded finite check supports regression handling; it does not prove the infinite theta theorem or any hardness claim.
