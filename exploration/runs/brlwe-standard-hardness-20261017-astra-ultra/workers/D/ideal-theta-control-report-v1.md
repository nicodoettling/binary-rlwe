# D-THETA-1 exact finite control report

Status: **PASS for the encoded finite controls only**. The analytic theorem remains PROVISIONAL. One authorized LIGHT experiment ran, with no repairs or retries.

At n=2,q=5, every one of the four CRT supports was enumerated. For each ideal I_T, coefficient character annihilation agrees exactly with conjugate Q_T modulo q. This verifies the conjugation that would be missed by identifying the coefficient dot product with an unconjugated trace pairing.

Two finite coefficient-noise laws, mixed through one common latent fair bit, were tested. Within each latent branch the two outputs use independent noises. Exact fifth-root polynomial arithmetic verifies that the **entire** finite Fourier squared sum equals the directly computed chi-square divergence. All nonannihilating characters vanish exactly, and TV²<=chi-square/4. The conditional two-output product bound and retained-latent average bound pass. With either rank-one ideal the retained-latent pair TV is 295/2592, while the actual pair differs from the product of its unconditional marginals by 25/2592. Thus the test retains the shared-latent dependence and would reject an unconditional independence shortcut. No finite noise is asserted to model the BBPS Gaussian quantitatively.

For P=(2+i), Q=(2-i), u=(2+i)/5 in Z[i], all 49 vectors (a,b) in [-3,3]² satisfy

    z=(2+i)(a+bi),  conjugate(u)z=a+bi,
    |u|² ||σ(z)||²=2(a²+b²).

This is an exact principal-ideal equality control for the Fourier scaling. For z=(2,1) or (-1,2), the canonical squared norm is 10 and the weighted norm is 2; for z=(1,3), these are 20 and 4.

Resource record: 9609 primitive enumerated states, recorded wall time 0.04697969602420926 seconds, peak RSS11264 KiB, one process, SIGALRM30 seconds and RLIMIT_AS268435456 bytes. Tool exit0; stderr has zero bytes. No random seed, float mathematical probability, Gaussian truncation, solver, installation or detached child occurred. The only floating values are diagnostic resource times.

Code/input/prelaunch estimate and exact command/original output are experiments/theta-control-v1.*. Code SHA256 a3fe34718f373c9ea70ea8361f5439fc5478f9498f9871329db0ef53b97b923e; stdout SHA25619b3a68b8b7e80c2018b741740d46d01041b8b06463f5c32faa6934a0ec452d6. Infinite-series convergence, canonical Gaussian transform, retained-latent theorem and asymptotic claims require analytic nonauthor review; this finite pass does not certify them.
