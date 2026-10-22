# Exact regression registration (before execution)

Hypotheses: inverse finite Fourier orientation gives exactly the pJ^-1 annihilator; a largest cyclic gap gives the claimed containing GRS dimension; normalized polynomial-root recursion preserves a multiplicity budget even with inseparable roots, common coefficient prefixes and X-content; CP-1 rejects the unsupported sequential product estimate.

Exact inputs: n,p=(2,5),(4,17),(8,17); every nonempty proper support subset; minimum positive alpha satisfying alpha^n=-1; every spectral unit vector for each support; explicit triangular ideal basis from the support polynomial. Root recursion: F_5, degree bound 3, six explicitly coded polynomials, exhaustive comparison with all 125 degree<3 polynomials for each case. CP-1 uses the exact rational distribution in the required methodology.

Arithmetic: integers and fractions only, no sampling, no seeds, no floating-point precision or tail truncation. Expected resources: under 10 seconds, under 50 MiB. Hard limits: timeout 120 seconds, CPU 115 seconds, address space 512 MiB. No detached process, no installation, no unrelated files. Coordinator granted the LIGHT slot before execution. This bounded check is not an infinite proof.

Command (from this directory):

    timeout 120s prlimit --as=536870912 --cpu=115 /usr/bin/time -v python3 exact-regression.py > exact-regression.stdout 2> exact-regression.stderr

The exact script is preserved in exact-regression.py; its pre-execution SHA256 is recorded in exact-regression-prehash.txt. Exit and resource results are preserved separately. No cleanup deletes evidence; no long-lived process is created.
