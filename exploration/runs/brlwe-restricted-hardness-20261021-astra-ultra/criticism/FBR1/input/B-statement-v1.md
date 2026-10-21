# B-CUBE-THETA-v1: full binary guessing from the exact cube image

This is an information theorem; it makes no computational hardness claim.

Let n be a positive integer and J be any full-rank subgroup of Z^n. Write rho_t(x)=exp(-pi ||x||_2^2/t^2), rho_t(J)=sum_{g in J} rho_t(g), and D_{J,t}(g)=rho_t(g)/rho_t(J), for t>0. Let S be uniform on {0,1}^n, independent of G sampled from D_{J,t}. Observe the entire unwrapped integer vector Y=S+G. Let C_J be the number of nonempty fibers of the map {0,1}^n -> Z^n/J. Define optimal guessing by maximizing over all randomized decision rules from the observation to a binary vector, with success being equality to the actual S.

For every real r>0,

    C_J/2^n <= p_guess(S | Y)
      <= min(1, (C_J/2^n) exp(pi n/(4r)) (1+r/t^2)^(n/2)).    (T1)

In particular,

    p_guess(S | Y) <= min(1, (C_J/2^n)
                                exp((pi/4+1/2)n/t)).           (T2)

The lower bound is exactly the optimal guessing probability from Y mod J. No equidistribution of Gaussian cosets, smoothing condition, accessible sampler, or short supplied basis is assumed. The bound holds pointwise for each fixed J. Revealing additional data is permitted only when, conditional on that data and J, the stated independent law of S,G still holds.

For the power-of-two cyclotomic coefficient lattice R=Z[X]/(X^n+1), if C_J<2^n for a nonzero integral ideal J, there exists a nonzero ternary f in J with ||f||_2<=sqrt(n). Consequently

    N(J)<=|N(f)|<=n^(n/2),

and J has an ordinary coefficient basis with operator norm at most n^2. This is an existence claim, not an algorithm finding f or the basis. The geometry statement alone does not extend any previously accepted reduction.

The parameter substitution t=2n^2 ell, ell>=1, gives multiplicative guessing overhead at most exp((pi/8+1/4)/(n ell)). It does not authorize changing the accepted theorem's eligible family or asserting a hardness transfer.
