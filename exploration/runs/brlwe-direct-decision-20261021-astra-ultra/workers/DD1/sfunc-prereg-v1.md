# DD1-SFUNC-FV1 preregistration

Before execution. Independent finite-support/normalizer falsification of coordinator DD3-SFUNC-v1. n=2, alpha=15/16, exact Gaussian weights alpha^(||g||²), so t²=pi/log(16/15). Truncate g to[-24,24]², retaining exact integer masses with common denominator16^1152. Full-rank subgroups tested: Z², {(x,y):x+y even}, {(x,y):x even}, and2Z². Function families: identity on the whole binary vector; coordinate0 alone; coordinates0/1 adaptively selected; constant function. Enumerate all4 binary secrets and every possible y=g+s; compute exact maximum-of-sums joint numerator and residue-only K. Check lowerboundK, and a conservative rigorous infinite-Gaussian upperbound K*43/28 by charging omitted Gaussian mass. Since log(16/15)<1/15 and pi>3, t>6; pi<22/7 gives T2 overhead<=exp(3/7)<=43/28. The two-dimensional omitted unnormalized mass is at most4*31*alpha^625/(1-alpha^51), because the one-dimensional total theta is <=31. Z_J>=1, so this also bounds full-law TV from truncation.

Expected max-order negative control: for J=Z² and the adaptive coordinate family, selected guessing is STRICTLY larger than either single-coordinate guessing, rejecting interchange of max with the y sum. Constant-function and singleton-residue cases must give1. Tail and every exact ratio retained. These finite controls do not prove the general theta-envelope theorem.

Code sfunc_finite_v1.py, deterministic no seeds. Dimension2, at most2401 lattice points and about2500 observations per case; integer encodings below5000bits;16 cases. Expected<20sec/<128MiB. Limits120sec wall,512MiB RLIMIT_AS, no descendants, full stdout/stderr/time/exit receipt. Parent slot coordination required.

Command:

    timeout --signal=TERM --kill-after=5s 120s /usr/bin/time -v python3 exploration/runs/brlwe-direct-decision-20261021-astra-ultra/workers/DD1/sfunc_finite_v1.py
