# SV-SPARSE-ACQ-v1: ordinary-basis sparse-member classification

Fix an integer h>=1. Let R=Z[X]/(X^n+1), n>=2 a power of two, and supply an ordinary integer basis A of a nonzero integral ideal J. Let B>=1 be an integer. There is a deterministic algorithm, costing at most(1+2nB)^h times a polynomial in n and all input bit lengths, which finds a nonzero f in J having at most h nonzero coefficients and coefficient magnitudes at most B whenever one exists. It requires no supplied short member or factorization. For fixed h and polynomial NUMERIC B this is polynomial time.

For a rational target T=lambda+w, lambda in J^-1 and canonical infinity error at most rational r, if such an f exists and

                         4r^2 h B^2<1,

the algorithm followed by coefficient rounding of fT and division by f returns lambda exactly. All rational output costs are charged. One can instead test the sharper exact guard4r^2||f||_coef,2^2<1 for each found candidate. This is a sufficient classification of every ideal with such a member, not only of principal ideals, and not a claim that all eligible ideals contain a polynomially enumerable sparse member.

For an explicit regime beyond polynomial quotient exponent, take f=X^2-X-1 and J_n=fR for powers-of-two n>=4, supplied by ANY ordinary ideal basis. Let L_j be the integer Lucas sequence L_0=2,L_1=1,L_(j+2)=L_(j+1)+L_j. Then

    R/J_n as an additive group is (Z/L_(n/2)Z)^2,
    e(J_n)=L_(n/2),   N(J_n)=L_(n/2)^2.

These exponent and norm values are exponential in n. For every fixed rho with log2((1+sqrt(5))/2)<rho<1, the norm is at most2^(rho n) for all sufficiently large powers-of-two n. The h=3,B=1 search finds a qualifying member from the ordinary basis. At the actual inherited radius r=epsilon_*ell^2/(1024nKchi Qmax), with its guards giving r<1/(4sqrt(n)), the sparse decoder succeeds. In every inherited family with inverse-polynomial r, the scalar sufficient guard2e(J_n)r<1 eventually fails, while the sparse-member decoder succeeds. This compares two sufficient algorithms; it establishes no hardness of the remaining source ideals and no new FF radius.
