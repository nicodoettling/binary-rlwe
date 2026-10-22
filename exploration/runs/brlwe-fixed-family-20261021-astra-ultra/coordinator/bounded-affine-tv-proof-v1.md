# Proof and conditional-law audit of BOUNDED-AFFINE-TV-v1

Use RAW second moments C=E[Delta Delta^T], B=E[ZZ^T], L=E[Z Delta^T]. They exist and C is positive semidefinite with trace E||Delta||^2; no centering or Gaussian assumption is used. For every s,

    V_s=E[W_s W_s^T]=B-L M_s^T-M_s L^T+M_s C M_s^T.

Let T be multiplication by X. For any binary baseline U outside positions0,1,2,3, take the four secrets U+e0+e1,U+e0+e3,U+e2+e1,U+e2+e3. Their alternating raw-second-moment sum equals

    D=P C (TP)^T+(TP) C P^T, P=I-T^2.

All terms except the mixed quadratic one cancel. In a unitary Fourier eigenbasis of T, with theta_j=(2j+1)pi/n and nonnegative diagonal c_j of C, the diagonal of D is8 sin^2(theta_j)cos(theta_j)c_j. For n>=4 a power of two, each scalar has magnitude at least16/n^2. Indeed if |cos theta|>=1/2 use |sin theta|>=2/n; otherwise sin^2>3/4 and |cos theta|>=2/n. Consequently ||D||_F>=16 tr(C)/n^(5/2), and ||D||_op>=16 tr(C)/n^3.

Put V_*=E[YY^T] and d_s=||V_s-V_*||_op. Triangle inequality gives sum of d_s over each four-corner face at least16 tr(C)/n^3. The faces for distinct U are disjoint. There are2^(n-4) such faces in the full cube; dividing by2^n gives E_S d_S>=tr(C)/n^3. In a weight-w slice there are binom(n-4,w-2) faces, giving E_S d_S>=4 p_w tr(C)/n^3. No random sequential face selection is used.

For each fixed s choose a real unit eigenvector u_s attaining the norm of V_s-V_*. Under the bounded-support premise, f_s(x)=(u_s^T x)^2/R^2 lies in[0,1] on both supports. Its expectation difference has magnitude d_s/R^2, hence TV(Law(W_s),Law(Y))>=d_s/R^2. Because the same marginal S occurs in both endpoints, the retained-S total variation is EXACTLY the average of these conditional distances. Average the previous inequality. The test may depend on retained s; no claim is made for hidden-S TV.

For finite second moments without bounded support, replace f_s by min((u_s^T x)^2,R^2)/R^2. The expectation lost from each raw quadratic is at most its stated norm-tail second moment, so conditional TV is at least(d_s-eta_s-eta_Y)/R^2. Averaging gives the tail version. Finite variance alone is insufficient without these terms: a rare large perturbation can carry the variance.

For the modulo-q statement, condition Y_G on the single event ||Y_G||_2<=R, obtaining Y_R. It is one S-independent distribution and its TV distance from Y_G is tau. W_s and Y_R are supported in the coefficient ball of radius R<q/2, on which reduction modulo q is injective. Thus the bounded-support TV lower bound is unchanged for this pair after reduction. Data processing gives TV(Y_R modq,Y_G modq)<=tau, and triangle inequality proves the result. This neither asserts coordinatewise independence after conditioning nor multiplies posterior event probabilities. Each s has the same original joint pair (Delta,Z); dropping this independence invalidates the common C and the face identity. No inference about batch amplification or source hardness is made.
