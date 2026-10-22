# FF3-COMPACT-SELECTOR-v3

The finite n2 instance is exactly checked by FV11; no asymptotic family theorem or Gaussian scope is asserted.

Let R_m=Z_m[X]/(X^n+1), and let the candidate secrets be all coefficient-binary vectors. Let E be the set of n*2^(n-1) positively oriented cube edges e=(u,v=u+X^i), where u_i=0. Each edge difference X^i is a unit in both R_Q and R_q. Let {H_j}_{j=1}^V be ring-noise Markov kernels, each mapping uniform R_Q to uniform R_q and an exact noise law nu_Q to an exact noise law nu_q. Their coefficients need not be independent.

For an observed x=(a,b), define residuals r_u=b-au,r_v=b-av. Let c_e(x) be a polynomially computable local class. Give nonnegative rational selector weights g(c,j,k), with G(c)=sum_(j,k)g(c,j,k), satisfying the exact normalization

    sum_(e in E) G(c_e(x)) = |E|                 for every input x.       (N)

Let M be a supplied positive rational, encoded by binary integers, with M>=max_c G(c). Its encoding length is charged in all bit costs; an integer upper bound may be used. For each input: draw a uniform cube edge; accept it with probability G(c_e(x))/M; repeat until accepted. Then sample(j,k) with probabilities g(c_e(x),j,k)/G(c_e(x)); draw two independent ring residual outputs according to H_j(r_u) and H_k(r_v). Invert the two residual coordinates using the unit difference X^i to obtain(c,d).

The resulting row-normalized kernel is

 K(x,y) = |E|^-1 sum_e sum_(j,k) g(c_e(x),j,k)
          H_j(r_u,d-cu) H_k(r_v,d-cv).                           (K)

It uses expected exactly M trials, since the per-trial acceptance probability is1/M for every observed x. The expected cost is polynomial in n, all input and M encoding bit lengths, and the numeric value M if classes, tables, H sampling and rational coins are efficient. Capping at L trials and outputting a fixed fallback gives per-input TV error at most exp(-L/M). This is a pointwise bound; it needs no inference from marginal success rates after conditioning.

If, in addition to(N), the exact linear endpoint equations P_s K=T_s for every binary s and U K=V hold, independent executions preserve the full shared-secret batch law. The end-to-end approximate error from a capped implementation is at most k*exp(-L/M) for k samples, plus the explicitly charged H/coin approximation errors. The existence of each H alone DOES NOT imply these endpoint equations for an input-dependent selector.

Finite certified instance: n2,Q3,q2; source coefficient law(7/8,1/16,1/16), target coefficient law(3/4,1/4). H_j are the four frozen FV9 radial ring kernels, with vertices in experiments/radial-ring-H-vertices.json. Class c=(zero_count(a),zero_count(r_u),zero_count(r_v)). FV11 supplies33nonzero rational weights. Exact verification gives(N),all four P_s K=T_s,and U K=V. The maximum local weight is

 31747846170836756094431065767102005668874369915000841877198843
 /11688058834193179864192788149647847121368047468795377899320297 <3.

This instance may take M=3. The exact selector certificate is experiments/public-geometry-public_norm_local_edge_weights-witness.json, SHA256140a8b92c3a772c217801f66f9d7618843330f0ca8264718858c3cfcf679cba8. The checker and all model coefficients are specified by experiments/ff3-public-geometry-fv11.py. This statement imports only its finite exact Fraction checks, not a floating solver status.

For arbitrary n, this class has(n+1)^3 states and a uniform cube edge can be sampled using expected O(n) independent fair bits without listing the edges. When n is a power of two, a worst-case O(n) fair-bit bound is also available. A scalable result would require an effective polynomial-size family of H_j and g tables, exact or negligible endpoint error, and polynomial M with polynomial bit complexity. None follows from the n2 certificate. In particular, a feasible g could have exponentially large M, and target/source finite rational laws are not silently replaced by discrete Gaussians.
