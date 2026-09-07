# S10 calculations (all deductions, not cited hardness theorems)

## 1. Planted two-block knapsack: first sampler and quantitative oracle arrow

Evidence label: fully written small calculation.

Let R_q=Z_q[X]/(X^n+1), coefficient basis, n a power of two. For an explicit conditioning bound restrict q to an odd prime q>2n; this is a subclass of the reference odd polynomial moduli. Sample independent a_1,a_2 uniform R_q and x,y uniform {0,1}^n; publish t=a_1 x+a_2 y. Search returns the planted (x,y), or more weakly any binary preimage. This is a two-column ring-knapsack source with one ring equation, not an assumed rank-two LWE source.

Given (a_1,a_2,t), abort if a_2 is not a unit. Otherwise set A=a_2^{-1}a_1, C=a_2^{-1}t, draw G with iid D_sigma integer coefficients, and output (A,B=C+G mod q). Then B=A x+(y+G) mod q exactly. Conditional on a_2 being a unit, A is uniform and independent of x,y; the source y is iid binary and independent of x,A,G.

Let Z_sigma=sum_z exp(-pi z^2/sigma^2). For the symmetric unimodal D_sigma, TV(D_sigma,D_sigma+1)=D_sigma(0)=1/Z_sigma, by telescoping the mass difference on the two sides of the origin. Thus TV((G_j+Y_j),G_j)=1/(2 Z_sigma), because Y_j is an independent fair bit. Tensorization gives TV((G+Y),G)<=n/(2 Z_sigma). Reduction modulo q cannot increase TV, so the same bound applies to the actual wrapped law ((W_sigma,q(r)+W_sigma,q(r-1))/2)_r versus W_sigma,q(r), without any no-wrap assumption. One may retain exact delta=n/(2 Z_sigma); the simple bound Z_sigma>=sigma-1 follows by integrating the decreasing Gaussian on the positive half-line (sigma>1), so delta<=n/[2(sigma-1)].

Consequently, an algorithm recovering S on ONE ring sample of reference binary RLWE with probability epsilon yields a planted knapsack inverter with conditional probability at least epsilon-delta. Given output x_hat, compute y_hat=C-A x_hat mod q and verify both coefficient vectors are binary and satisfy the original equation. When x_hat=x, this recovers y exactly; any verified alternative also solves preimage search. The nonunit probability is at most n/q: X^n+1 is squarefree for odd q, CRT yields factors of degrees d_j, and the union bound gives sum_j q^{-d_j}<=n/q. Unconditional planted recovery is at least (1-n/q) max(0,epsilon-delta).

The preceding additive-TV bound does not preserve arbitrary nonnegligible success at fixed polynomial sigma. A stronger multiplicative transfer resolves that issue. Define M_2(P||Q)=sum_z P(z)^2/Q(z), the exponential of order-two Renyi divergence. For P=D_sigma^n and any integer shift y, completing the square gives M_2(P||P+y)=exp(2 pi ||y||_2^2/sigma^2): explicitly, -2||z||^2+||z-y||^2=-||z+y||^2+2||y||^2, and summing exp(-pi||z+y||^2/sigma^2) over integer z leaves the normalizer unchanged. For Q=E_Y[P+Y], convexity of u->1/u gives

M_2(P||Q) <= E_Y M_2(P||P+Y) = ((1+exp(2 pi/sigma^2))/2)^n <= exp(2 pi n/sigma^2).

Wrapping modulo q is deterministic data processing, so this also upper-bounds M_2 between the wrapped target and simulated errors. Joint A,x have the same independent law in both experiments, and adding the solver's randomness is another common channel. Cauchy–Schwarz on the event that the solver outputs x gives

Pr_source[recovery | a_2 unit] >= epsilon^2 / ((1+exp(2 pi/sigma^2))/2)^n.

Thus source success is nonnegligible for every nonnegligible epsilon when n/sigma^2=O(log n), and at least exp(-2 pi n/sigma^2) epsilon^2. In particular sigma^2=Omega(n) gives a constant-factor squared-success reduction. Multiply by at least (1-n/q) for the unconditional source. This is a valid first-sampler oracle reduction, but has no independent hardness consequence absent an independently supported K2 assumption.

This is NOT a source of m>1 independent ring samples. Repeated Gaussian additions share A and hidden y. Neither repetition nor rotations create uniform independent A_i. The modulus must simultaneously keep q/sigma>=n^c. The target secret, rank, basis and degree are preserved; source binary residual y is converted to approximate/likelihood-dominated wrapped Gaussian noise, with the explicit success comparison above, rather than an assertion of exact equality.

Uniform-source warning: for fixed a_1,a_2 the planted target support contains at most 4^n values. A uniform target lies in that support with probability at most (4/q)^n. Hence for q>4 the planted joint distribution and a uniform-target joint distribution have statistical distance at least 1-(4/q)^n. This is an information-theoretic support statement, not an efficient distinguisher.

## 2. Binary QCSD: first lift and explicit carry obstruction

Evidence label: fully written small calculation.

Source Q_2=F_2[X]/(X^n-1). Let h be uniform, x,y independently uniform weight-w binary polynomials, z=x+h y. The public (h,z) is the planted systematic index-two QC syndrome. Over F_2, choosing independent uniform binary T gives S=y+T (XOR), B=z+hT=hS+x. S is iid uniform binary and independent of h,x. Recovering S yields y=S+T and then x=z+h y. This is a valid average-case reduction from planted QCSD to the uniform-secret binary-field ring channel with fixed-weight noise, ONE ring sample; it does not reach odd-q Gaussian RLWE. Moreover this target is information-theoretically unrecoverable on unit h: B=hS+x is uniform when S is uniform, and conditional on (h,B), every weight-w x is equally likely and determines one S=h^{-1}(B-x). Thus planted recovery probability is at most 1/binom(n,w). In the uniform source-syndrome branch, B remains uniform after masking too. The masked experiment therefore erases the relevant decision information on units rather than explaining cryptographic hardness. Exposing T to the oracle instead changes the target to a leakage experiment.

Lift h,z,T to coefficient representatives in Z[X]/(X^n+1). If simply T=0, define K=(lift(h)lift(y)+lift(x)-lift(z))/2; the numerator is coefficientwise even because X^n+1 and X^n-1 coincide modulo 2. Then lift(z)=lift(h)lift(y)+lift(x)-2K. Thus an odd-q output (A=lift(h),B=lift(z)+G) has effective error lift(x)-2K+G, with unknown K depending on h,y,x. A has binary coefficients rather than being uniform R_q; neither error independence nor target Gaussian law is established.

If one tries A=lift(h)+2U, B=lift(z)+2V+G with independent uniform U,V in R_q, then A is uniform because 2 is invertible, but B is also uniform (V is a one-time pad), so the error is uniform and carries no recoverable planted secret. There is no nonzero additive homomorphism Q_2 -> R_q: every image satisfies 2z=0 and odd q forces z=0.

Even over odd q with a hypothetical sparse binary source, the usual F_2 uniformization is obstructed. In coefficients y XOR T=T+D_T y where D_T=diag(1-2T_j). Maintaining B=A' S+E from B=A y+E requires A'=A D_T, plus known offsets. For invertible negacyclic multiplication A, A D_T is a ring multiplication matrix iff D_T is one. A diagonal multiplication matrix must be scalar: its first column is d_0 e_0, hence its ring element is constant d_0 and all diagonal entries equal. Thus only all-equal T preserve the rank-one multiplication structure by this direct coordinate-mask construction. This does not rule out more elaborate randomized reductions.

Ledger departure: coding uses q=2, cyclic ring, degree generally independently chosen rather than forced power of two, coefficient basis, rank-one channel after rewriting, fixed-weight source secret/noise, and exactly one ring sample. At power-of-two n, X^n-1=(X+1)^n over F_2; no hardness from prime-length QC parameter sets is transferred automatically.

Cheap exact lift diagnostic: at n=2, h=1+X, x=1, y=1 or X, the F2 source syndrome is z=X in both cases. In Z[X]/(X^2+1), h*1+1=2+X while h*X+1=X. Consequently K=1 or 0. This confirms concretely that the same visible binary source can require different witness-dependent carries.
