# Frozen channel-scope controls D-CS v1

Status: PROVISIONAL. Let R be a split finite F_q-algebra isomorphic to F_q^n, q>=2. For integers k,m>=1, P_k is the law of iid uniform a_1,...,a_k in R, uniform shared s in R, and b_i=a_i s+e_i, where the full error tuple is independent of all a_i,s. Q_k is uniform on R^(2k). Let K be any randomized channel R^(2k)->R^m with input-independent coins; no runtime restriction is imposed unless stated. Write M=q^(mn), U uniform on R^m, and all logs natural.

1. If KQ_k(y)<=exp(alpha)/M for every y, alpha>=0, then

       H(KP_k)>=(m-k+1-q^-k)n log q-alpha.

   For every target distribution B, epsilon=TV(KP_k,B) obeys

       h2(epsilon)+epsilon log M
       >= (m-k+1-q^-k)n log q-H(B)-alpha.

   If only TV(KQ_k,U)<=delta is known, alpha=log(1+M delta) is valid. This bound need not be useful for negligible delta.

2. Now set every source error to zero. Let C={(a,b):there exists s with b_i=a_i s for all i}, and gamma=[q^(1-k)(1-q^-k)+q^(-2k)]^n. For any distribution B on R^m, the channel that samples fresh B on C and fresh U off C has planted law exactly B and comparator gamma B+(1-gamma)U, hence comparator TV exactly gamma TV(B,U). For k>=2, gamma<q^(-(k-1)n). C is efficiently decidable from a split-ring representation or by linear algebra, without hidden information. If B is efficiently approximately samplable, this channel is also efficiently approximately implementable with the corresponding full-law errors.

3. In the same noiseless model, if k>=m+1, then gamma<1/M. Therefore H=(U-gamma B)/(1-gamma) is a distribution for every B. The channel sampling B on C and H off C maps P_k exactly to B and Q_k exactly to U. This is an information-theoretic existence statement; efficient H sampling for general B is not asserted.

The claims are scope controls for an entropy argument. They do not establish hardness of any source or exclude reductions from noisy standard RLWE. Noiseless RLWE is deliberately an easy control. The exponentials above are probability bounds, not assumed computational indistinguishability. Acceptance requires nonauthor review of the exact version and applicable finite controls.
