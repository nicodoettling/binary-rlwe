# GAUSS-AVG-v1 proof candidate

PROVISIONAL. Exact assumptions are in gaussian-average-obstruction-statement-v1.md.

Put H=Cov(Delta,Z). For each fixed secret,

    V(s)=Cov(W_s)=B+M_s C M_s^T-M_s H-H^T M_s^T.

Partition the uniform binary cube into disjoint faces by fixing coordinates2,...,n-1 and varying coordinates0,1. On EVERY face the matrix second difference is

    V(11)-V(10)-V(01)+V(00)=K,  K=TC+CT^T.

All background coefficients and all cross covariances cancel. For any constant target V_*, at least one corner of each face satisfies ||V(s)-V_*||F≥||K||F/4 by the triangle inequality. Hence at least one quarter of all secrets satisfy this bound, with no conditioning on a rare globally prescribed secret.

Diagonalize the unitary real shift T over C, with eigenvalues zeta_j=exp((2j+1)pi i/n). In that basis C' is PSD, has trace tr(C), and K' has diagonal2 Re(zeta_j) C'jj. Since n is divisible by4, every |Re(zeta_j)|≥sin(pi/n). Therefore

    ||K||F² ≥4 sin²(pi/n) sum_j(C'jj)²
            ≥4 sin²(pi/n) tr(C)²/n.

On the at-least-quarter set, symmetry of V(s)-V_* gives an eigenvector u_s of unit length with

    |u_s^T(V(s)-V_*)u_s|
      ≥||V(s)-V_*||F/sqrt(n)
      ≥sin(pi/n) tr(C)/(2n)
      ≥tr(C)/n²,

using sin(pi/n)≥2/n. Selecting u_s in a mathematical TV lower bound does not assert that an observer of samples alone knows s or the covariance matrices.

Let v=u_s^T V(s)u_s and v_*=u_s^T V_*u_s. Both lie in[0,L]. For the one-dimensional projections, at Fourier frequency t=1/sqrt(L), the characteristic-function magnitudes are exp(-v/(2L)) and exp(-v_*/(2L)), irrespective of the Gaussian means. The mean-value theorem gives magnitude difference at least exp(-1/2)|v-v_*|/(2L). The difference of magnitudes is no larger than the absolute difference of the characteristic functions, and a bounded unit-modulus test has expectation difference at most2TV. Projection cannot increase TV. Hence the conditional TV at this s is at least exp(-1/2) tr(C)/(4n²L). Averaging over the common uniform retained S, whose disjoint atoms give exact conditional-TV decomposition, yields the theorem's1/4 factor and final constant1/16.

For the sufficient L, every unit vector u satisfies Var(u^T(Z-M_s Delta))≤2Var(u^T Z)+2Var(u^T M_s Delta)≤2tr(B)+2||M_s||op² tr(C). The triangle inequality and ||T^i||op=1 give ||M_s||op≤n. This uses no independence between Delta and Z and no unproved conditional posterior law.

Conditional-law audit: S is independently sampled once, the joint Gaussian perturbation has the same law at every S, and conditioning on S=s leaves its means/covariances unchanged. The TV decomposition uses the SAME uniform secret law on both endpoints. Face counting is a deterministic partition, not a sequential product argument. No Gaussian is replaced by a discrete Gaussian, and no coordinate covariance equality is promoted to an independent error law. CP-1's old product bound remains rejected. A finite face/matrix falsification and Gaussian-characteristic diagnostic are required before review; neither proves the infinite Gaussian statement.
