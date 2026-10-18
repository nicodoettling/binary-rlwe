# BT7 hand counterexample: physical endpoint is not exact Haar

Recorded before proposing a repair. This refutes a physical-law reading of the sentence that the selected width tends to FULL Haar. It does not refute the continuous Gaussian proxy endpoint or the BDD existence claim.

Take n=2, R=Z[i], J=R, D=1, q=2, P=1, k=1, w=1, delta=1/4, zeta=1/8, kappa=64. The scalar lower bounds for kappa hold: h0=1/256, a0=1/1024, S=log(1024), and 4S+8+4log(2)+20<64; also 3exp(-64)<1/4. After calculating epsilon0 and a as prescribed, choose an integer m congruent to 1 modulo 4 sufficiently large that v0=m/256>=2sqrt(2)a. Then d0=1/m and the BDD radius bound holds. Take T=lambda=e=0 and query z=0. The multiplier error is h=2/m.

The distinguisher A accepts precisely when the first rounded coefficient is even. Its uniform acceptance is 1/2. A coefficient of G_w has density sqrt(2) exp(-2pi x^2), and its probability of leaving (-1/2,1/2) is at most (sqrt(2)/pi)exp(-pi/2)<1/4. Thus its GP acceptance exceeds 3/4 and its advantage exceeds delta.

For the unrounded physical query, choose the nonzero dual character chi=m/4 in L*=R/4. For every integral multiplier r, the character of (2/m)r is one, because the canonical real pairing is Tr(chi conjugate((2/m)r))=Re(r), an integer. Consequently the query Fourier coefficient at chi equals exp(-pi m^2/8)>0 for every t. Haar has zero coefficient, so the physical law does not converge to Haar.

The exact finite rounded endpoint also fails to be uniform. As t tends to infinity, the first coefficient r modulo m tends to uniform. The period-two function f(x)=(-1)^round(x) has Fourier coefficients 4(-1)^s/[pi(2s+1)] at positive odd cosine frequencies. Averaging over the m shifts 2r/m leaves frequencies m(2s+1). Since m=1 mod 4, the limiting parity expectation is

  (4/(pi m)) sum_{s>=0} (-1)^s exp(-pi m^2(2s+1)^2/8)/(2s+1),

which is strictly positive by the alternating-series test. Hence the limiting finite law has a nonuniform first-coordinate marginal. This is an exact hand calculation; no experiment was run.

The bias is extremely small and can be below the fixed approximation budget. A valid theorem can use an analytically defined continuous-Gaussian proxy whose endpoint is Haar, together with uniform physical-to-proxy coupling. That interpretation must be explicit; the discrete physical endpoint cannot itself be asserted to converge exactly to Haar.
