# D-THETA-1 prelaunch estimate and command

Coordinator granted the second LIGHT reservation: <=30 seconds, <=256 MiB address space, <100000 primitive states, one Python process. No other mathematical processes are launched by this command. The script sets RLIMIT_AS and SIGALRM before computation.

Estimated <50000 elementary iterations: four ideal supports, two finite latent-noise branches, 25 frequencies each, 25 exact phase products per frequency, at most 625 pair outputs per branch, plus 49 principal-ideal vectors. Tables are at most 625 entries. Expected <2 seconds and <32 MiB; enforced caps remain 30 seconds/256 MiB.

The experiment does not approximate a Gaussian. It checks the coefficient-dual annihilator against conjugate Q, entire finite Fourier Parseval sums using exact arithmetic in the fifth-root cyclotomic field, retained-latent product bounds, and a principal-ideal scaling equality. Shared latent mixing remains separate from independent product marginals. All arithmetic is integer or Fraction; timings alone are floating point. No seed is used.

Exact command, cwd repository root:

    python3 exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/D/experiments/theta-control-v1.py > exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/D/experiments/theta-control-v1.stdout.json 2> exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/D/experiments/theta-control-v1.stderr.txt

Preserve a failing output before any repair. No third experiment is authorized.
