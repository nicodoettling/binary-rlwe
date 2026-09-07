# S05 independent development

Started 2026-09-06 09:15 UTC; only `context/formal-only.md` read. No baseline/barrier/scout material read. No CPU experiment run.

## Arithmetic family

Let f=X^n+1, q odd prime, and let I be an ideal of F_q[X]/f of F_q-dimension rho. Because f is squarefree, I corresponds to a subset of irreducible CRT factors. Let U be uniform in I, and let F have independent integer coefficients uniform on [-H,H], reduced mod q. Sample A=U+F. This explicitly changes the reference public multiplier distribution; secret and transcript error can remain the reference distributions. H=0 is the exceptional resultant locus. Large H may conceal membership in I. No pseudorandomness is asserted.

For fixed A, the algebraic fiber of S -> AS has q^{deg gcd(A,f)} points. Its intersection with {0,1}^n need not have this size or dimension. Indeed the Boolean scheme has dimension zero over every odd field before imposing AS=B.

### Half-dimensional kernel with no Boolean collision (fully written small calculation)

Take q=1 mod 4 and u^2=-1 in F_q. Put k=n/2 and A=(X^k-u)T, with T a unit. Write S=P+X^k Q, deg P,Q<k. Before multiplication by T, A S has lower block -Q-uP and upper block P-uQ. Its kernel consists of (P,Q)=(uQ,Q), dimension k. But for a binary difference P,Q each coefficient lies in {-1,0,1}. Since u is not 0,+1,-1 over an odd field, P=uQ forces P=Q=0 coefficientwise. Thus every nonempty Boolean fiber has exactly one point, despite q^{n/2} points in its ambient field fiber. The four scalar images of (p,q) in {0,1}^2 under p-uq are distinct. This construction works without assuming either degree-k factor is irreducible.

### Rich fibers from very small CRT rank (fully written small calculation)

If q=1 mod 2n, fix a primitive 2n-th root zeta and let I be the one-dimensional ideal supported at zeta. For nonzero A in I, AS determines only S(zeta), so all 2^n binary points are distributed over at most q field fibers. Mean Boolean fiber size is 2^n/q. Uniform secret has noiseless conditional entropy H(S|AS)>=n-log_2(q), so recovery is information-theoretically impossible with all multipliers in this same I. Membership of A in I and rank one are public polynomial-time tests; this does not resemble reference multipliers. Other samples must share I for this entropy statement.

## Norm and covering tension (own deductions)

Let nonzero binary difference delta have coefficient weight w (entries in {-1,0,1}). If U delta=0 for every U in I, then delta vanishes on rho CRT dimensions. Hence q^rho divides the nonzero integer resultant Res(f,delta). Nonzero follows from irreducibility of f over Q and deg delta<n. By Parseval at the n complex roots of f, mean |delta(zeta_j)|^2=w. AM-GM therefore gives |Res(f,delta)|<=w^{n/2}, hence q^{rho/n}<=sqrt(w).

The family A=U+F has support size at most q^rho(2H+1)^n. Statistical distance <=epsilon from uniform R_q therefore requires (2H+1)^n >= (1-epsilon)q^{n-rho}, or 2H+1 >= (1-epsilon)^{1/n} q^{1-rho/n} >= (1-epsilon)^{1/n}q/sqrt(w).

For fixed delta independent of F, each coefficient of F delta is a signed sum of w independent box variables, with variance w H(H+1)/3. Thus statistical hiding of the exceptional ideal entails an unwrapped collision displacement of RMS order q, rather than the desired sigma << q. This is an RMS obstruction for this specific independent, isotropic perturbation construction, not a blanket impossibility theorem: adaptive delta, structured/anisotropic F, and wrapped distributions require separate arguments.

Distribution ledger: reference n, rank one ring, binary secret, coefficient basis and Gaussian E are unchanged; q specialized to odd primes (q=1 mod4 or q=1 mod2n in examples); A changes from uniform R_q to U_I+F_H; repeated samples share the same chosen ideal I but draw independent U,F,E. The box perturbation is part of A sampling, not a replacement for E. Exact H=0 examples do not claim hardness.

## Refinements before release

The precise collision-family geometry is the union, indexed by nonzero ternary delta, of linear spaces Ann(delta) in public-A space. The Boolean scheme itself is a disjoint union of 2^n copies of Spec(Z), so geometric dimension alone cannot estimate Boolean fibers. Over Q every nonzero delta is invertible in Q[X]/f; consequently distinct Boolean graph sheets meet only at A=0. Reduction modulo primes dividing the integer norm creates larger intersections.

The RMS lower bound from the support calculation is valid uniformly, without assuming q>sqrt(n). If epsilon<1/2 and I is proper, H=0 cannot give epsilon-closeness to uniform, so H>=1. Then H(H+1)/(2H+1)^2>=2/9, and Var((F delta)_j)>= (2/27)(1-epsilon)^{2/n}q^2.

Stronger but narrower observation: if A itself is epsilon-close to uniform, any fixed nonzero delta has each coordinate of A delta epsilon-close to uniform F_q, because every row of multiplication by delta is nonzero. Thus for 0<=T<(q-1)/2, P[|(A delta)_j|_q<=T] <=(2T+1)/q+epsilon. No norm argument is needed for this fixed-delta statement. It does not handle a collision selected adaptively after seeing A.

Hand calculation n=4,q=3: f=(X^2+X-1)(X^2-X-1). For A=X^2+X-1, multiplication has rank 2, so each nonempty field fiber has 9 points. Modulo X^2-X-1, S=a+bX+cX^2+dX^3 maps to (a+c+d,b+c-d) in F_3^2. Enumerating the four (c,d) offsets gives binary fiber counts 2 at eight image points and 0 at (0,2). Thus 16 Boolean points occupy only eight of the nine target points; field dimension alone gives neither count. This is a finite toy specialization, not the growing small-noise target.

A possible exact norm saturator noticed from that example is delta=1+X^2+X^3: delta*delta^*=3 in Z[X]/(X^4+1), where * sends X to X^{-1}. Hence Norm(delta)=9 and the weight bound is sharp. Negacyclic conference matrices generalize this phenomenon, but the known Paley orders q+1 being powers of two restrict prime q to Mersenne primes; an unbounded family cannot be presumed. This is background for the same ideal-perturbation idea, not an additional hardness candidate.

Primary source accessed 2026-09-06 09:21 UTC: Stacks Project, Lemma 31.18.6, https://stacks.math.columbia.edu/tag/0BD2, directly verifies that the finite locally free norm is the determinant of multiplication and commutes with base change. Section 9.20, https://stacks.math.columbia.edu/tag/0BIE, gives the corresponding field norm and multiplicativity. These support only the norm mechanism; all Boolean counts and bounds above are own deductions. No access failures for these pages.
