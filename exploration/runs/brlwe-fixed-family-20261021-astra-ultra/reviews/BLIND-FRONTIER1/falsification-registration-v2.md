# BLIND-FRONTIER1 finite falsification registration v2

Registered before execution; fresh authorization is required.

One lightweight exact Python 3 process, 120-second wall and 512 MiB memory cap,
no network, solver, package installation, or parallel child jobs. Preserve full
output, exit, elapsed time, peak RSS, precision/tail policy and cleanup note.

Target the newly supplied SV-LIST-DECODE-v1 claim:

* Implement the normalized coefficient recursion for polynomial roots of Q(X,Y)
  of degree < t. Compare its complete output with exhaustive polynomial-root
  enumeration over F_2,F_3,F_5 for bounded t and bidegrees. Include repeated and
  inseparable roots, vanishing leading X coefficients, no polynomial roots, and
  many prefixes that fail at the final identity test.
* Record tree width and prove/check the multiplicity accounting invariant:
  the sum of the degrees of normalized Q_node(0,Y) across a depth never exceeds
  the original Y degree. Exhaustive polynomial coefficients will be limited to
  at most 729 Q polynomials per field/degree configuration.
* Check exact arithmetic in the convenient regime for powers-of-two n from128
  through4096 and all 2<=t<=n/64: N>n(2B+1), h<n/2 using the stated rational
  squared bound on pr, and 2B+1<=2n+1.

The finite test cannot certify unrestricted bivariate root finding or an infinite
lattice. It targets the explicitly derived recursion and conservative constants.
