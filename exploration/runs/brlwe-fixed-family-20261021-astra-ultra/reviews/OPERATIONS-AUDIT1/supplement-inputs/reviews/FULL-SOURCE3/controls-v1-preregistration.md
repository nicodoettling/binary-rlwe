Hypothesis: the stated coefficient-root recursion enumerates exactly every polynomial root of degree below t without superpolynomial branching, including repeated/inseparable roots. Independently computed direct polynomial substitution supplies the exhaustive oracle. Supporting controls verify Fourier support orientation, cyclic shifts, dense odd-support stabilizers and contraction counts, arbitrary-support gap containment, explicit list-regime integer guards, and the retained CP-1 negative inequality.

Code: controls-v1.py, frozen before execution. Inputs are exhaustive tuples (p,degX,degY)=(2,2,2),(2,1,3),(3,1,2), every nonzero bivariate coefficient vector, and t=1,2,3; inseparable Y^p-X^p for p=2,3,5,7; Fourier/contraction dimensions n=2,4,8,16 at p=5,17,17,97; all nonempty proper supports at n<=8; exact list-guard integer controls for powers n=128 through32768. All field and rational arithmetic exact, no float thresholds, no tails, no random seeds.

Expected outcome: PASS with direct root-set equality; at each depth number of nodes and evaluation-degree budget bounded by initial evaluation degree. Any failure remains preserved and must be diagnosed before rerun.

Resource request: one LIGHT slot, <=120 seconds wall, 512 MiB address space, expected <30 seconds and <64 MiB. Requires explicit root slot grant before execution. Command:

    /usr/bin/time -v timeout --signal=TERM --kill-after=5s 120s prlimit --as=536870912 -- python3 controls-v1.py

Execution uses the review directory as cwd, stdout to controls-v1.stdout.json, stderr to controls-v1.stderr.txt (including /usr/bin/time resource report), and a separate receipt records command, code hash, start/end, exit status and cleanup. No child process is intentionally retained. These finite controls do not prove infinite theorem statements or hardness.
