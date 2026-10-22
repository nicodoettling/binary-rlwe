# WEIGHT-GAUSS-v1 author proof and conditional-law audit

For each binary baseline U of weight w-2 outside coordinates0,1,2,3, form the four secrets from WEIGHT-COV-v1. Their covariance alternating sum is the same matrix

    D=P C (TP)^T+(TP) C P^T,  P=I-T^2.

In a unitary eigenbasis of T, its j-th diagonal is a_j*c_j, where c_j>=0 sum to tr(C), theta_j=(2j+1)pi/n, and a_j=8 sin^2(theta_j)cos(theta_j). Both |sin theta_j| and |cos theta_j| are at least sin(pi/n)>=2/n. A sharper combined bound is |a_j|>=16/n^2: if |cos theta_j|>=1/2 use sin^2>=4/n^2; otherwise sin^2>3/4 and |cos theta_j|>=2/n, giving |a_j|>12/n>=16/n^2 for n>=4.

Thus

    ||D||F >= (16/n^2)*sqrt(sum_j c_j^2)
            >=16 tr(C)/n^(5/2),
    ||D||op >= ||D||F/sqrt(n) >=16 tr(C)/n^3.

Write d_s=||Cov(W_s)-V_*||op. The triangle inequality gives sum_(four corners)d_s>=||D||op. The faces are disjoint: the outside baseline U uniquely determines a face, and the four allowed patterns each have exactly one1 in{0,2} and one1 in{1,3}. There are binom(n-4,w-2) faces. Consequently the average over all binom(n,w) secrets satisfies

    E[d_S] >= [binom(n-4,w-2)/binom(n,w)]*16 tr(C)/n^3
            =4*p_w*tr(C)/n^3.

For every fixed s, choose a unit eigenvector of the real symmetric covariance difference attaining d_s. Project the two Gaussian laws onto it. At frequency1/sqrt(L), their characteristic-function magnitudes are exp(-v/(2L)) and exp(-v_*/(2L)), with0<=v,v_*<=L. Their magnitude difference is at least exp(-1/2)|v-v_*|/(2L); arbitrary means cannot reduce the absolute characteristic-function difference below the difference of magnitudes. A unit-modulus test has expectation difference at most2TV. Thus conditional TV is at least exp(-1/2)d_s/(4L). Average and use the preceding bound.

The sufficient L follows from Var(u^T(Z-M_s Delta))<=2tr(B)+2||M_s||op^2 tr(C) and ||M_s||op<=n. For the uniform full cube, weight is a deterministic function of S. The exact retained-secret TV decomposition first sums conditional distances over each s, then groups by weight. The same weight probabilities occur in both endpoints. No fresh secret is drawn between stages, and no event-probability product or independence between successive data-dependent conditionings is inferred. Within each fixed slice the perturbation's stated independence is essential; allowing it to depend on the full s invalidates the common C/B/face argument. The proof assumes genuine continuous joint Gaussian laws and makes no discrete-Gaussian replacement.
