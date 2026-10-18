# RF3 narrow fractional endpoint review v1

This added review addresses only fractional-escape-test-v1.md, SHA256 13975760fadda817b0a338f260cb72983562c0f14cf19f5f09fce26ef04ba0ca. It was requested after completion of the main theorem's full/source reports and does not change their verdict. Verdict: the exact endpoint algebra and Gaussian-zero estimate pass; the final scale diagnostic is **REJECTED as a standalone guarantee** because its parameter/radius hypotheses are missing. Exact objections were preserved first in fractional-endpoint-objections-v1.md. No new experiment or source was used.

For any integral I and nonzero a in I, a^(-1)I contains R and has the same ordinary ideal class as I. Its inverse aI^(-1) is integral because I I^(-1)=R. Thus the first fractional escape is real and the inverse-lattice integrality statement is exact.

For the padded candidate J=PH/p with N(P)=p and N(H)=D_H,

    H subset J,
    Lambda=J^(-1)=pP^(-1)H^(-1) subset H^(-1),
    [J]=[P][H],
    covol_coeff(Lambda)=N(Lambda)=p^(n-1)/D_H.

The containments follow from pR subset P and pP^(-1) subset R. For every prime dividing q, the ideals P and H are local units because gcd(q,pD_H)=1. Consequently Lambda localized at those primes agrees with R, and natural rational reduction gives the claimed isomorphism Lambda/qLambda -> R/qR. This validates the source endpoint as a distribution on R/qR, but does not equate it with the distribution obtained from H^(-1).

For nonzero x in Lambda, xJ is a nonzero integral ideal, so

    |N(x)| N(J)>=1,
    |N(x)|>=p^(n-1)/D_H.

The same full-embedding AM-GM calculation as in the main review gives |N(x)|<=||x||_coeff^n. Hence lambda_1(Lambda)>=R0=p^(1-1/n)/D_H^(1/n). The norm is explicitly the coefficient Euclidean norm; there is no lost sqrt(n) from switching canonical conventions.

Set A=pi R0^2/s^2. Disjoint balls of radius R0/2 around lattice vectors in the shell [jR0,(j+1)R0) fit inside a ball of radius (j+3/2)R0, so their number is at most (2j+3)^n. When A>=2n log 5,

    rho_s(Lambda minus {0})
      <= sum_(j>=1) exp(n log(2j+3)-A j^2)
      <= sum_(j>=1) exp(-A j^2/2).

The elementary inequality log(2j+3)<=j^2 log 5 holds at j=1 and thereafter; for example 2j+3<=5^j<=5^(j^2). As A/2>=n log 5>=log 2, using j^2>=j gives

    sum_(j>=1) exp(-A j^2/2)
      <= exp(-A/2)/(1-exp(-A/2))
      <=2exp(-A/2).

If this unnormalized nonzero mass is T, then the centered zero probability is 1/(1+T)>=1-T. Reduction modulo q may only increase the mass at zero. The uniform distribution on R/qR has zero probability q^(-n), so the stated one-sample distinguishing gap follows for the exact centered discrete Gaussian. This uses its actual normalizer and no conditioning approximation.

In the degree-2 hand control, Lambda=(2-i)R, R0^2=5, and s^2=pi/(2log 2) give A=10log 2. The required A>=4log 5 is equivalent to 2^10>=5^4 and holds. The displayed tail bound is 2exp(-5log 2)=1/16. A point (2-i)(a+bi) has Gaussian weight 1024^(-a^2-b^2), and the nine-point conditional normalizer and nonzero mass are exactly (1+2/1024)^2 and 1-(512/513)^2. This conditional finite calculation does not prove the full tail; the shell argument above does.

The hypothetical scale substitution itself is algebraically correct:

    W_J=(32/sqrt(2)) n^(3/2) k v0 q/(delta w_B)
        >=(32/sqrt(2)) n^(3/2) k v0 q/(delta s).

Likewise the direct map x -> p x sends J into PH subset P and multiplies the coefficient norm by exactly p. Therefore any explicitly supplied certificate B_J>=1 becomes a certificate pB_J>=p. The publicly known vector p in P already meets that search radius. This restricted implication is valid for a nonzero-vector search guarantee and does not show that the sampler cannot happen to output a better vector.

As a standalone frozen note, q/s>=1 does not ensure B_J>=1: the displayed parameter tuple in FEP-1 even makes W_J=1/8. A sufficient clarification would be k>=1, v0>=1, 0<delta<=1, n>=2, q/s>=1, together with a specified conventional certificate satisfying B_J>=W_J and the relevant nonzero-output convention. Then W_J>=64 and the direct certified radius is at least 64p. This is a suggested conditional formulation, not a silent repair of the reviewed note. Any edited note remains pending recheck.

The generator observation also needs a scale condition before becoming a theorem about a short-residue test. Exact multiplication by a supplied generator f gives f Lambda=pP^(-1) subset R and preserves a uniform comparator modulo q. Quantitative concentration would additionally use the multiplication bound stated in FEP-3. No conclusion about a different fractional extraction map, a different source family, or computational hardness is drawn.
