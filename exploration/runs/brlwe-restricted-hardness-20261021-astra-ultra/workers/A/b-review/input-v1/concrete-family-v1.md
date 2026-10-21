# B-17-BLOCK-v1: concrete full-observation enlargement and its easy-source boundary

Status PROVISIONAL, information-only. This family is a new finite control in this package, not a claimed new hardness family or literature-priority result. It improves the historical degree-eight norm2176/image248 control's information bound, but has the same easy-source limitation and a small additive exponent.

## Exact ideal family

For n>=8 power-two, put m=n/8 and Y=X^m. In R8=Z[Y]/(Y^8+1), define

    g(Y)=1+Y+Y^2-Y^3+Y^7,
    J0=g R8=(17,Y^2-5Y+1).

Set F(X)=g(X^m) and J=F R_n. Permuting coordinates into m blocks (X^j,X^(j+m),...,X^(j+7m)) makes J the orthogonal direct sum of m copies of J0. Thus

    N(J)=289^m>256^m=2^n,   exponent(R_n/J)=17.

Here is an algebraic norm check independent of the determinant code. Since Yg=-(Y^4-Y^3-Y^2-Y+1), put z=Y+Y^-1. The reciprocal polynomial divided by Y^2 equals z^2-z-3. The real-subfield polynomial is P(z)=z^4-4z^2+2. Modulo Q(z)=z^2-z-3, P(z)=3z+2. Hence Res(P,Q)=Res(Q,3z+2)=9Q(-2/3)=-17. Squaring to the full degree-eight field yields N(g)=289. Modulo17, the reciprocal polynomial factors as (Y^2-5Y+1)(Y^2+4Y+1). The first quadratic has roots10 and12, each with eighth power-1. Thus (g) is contained in (17,Y^2-5Y+1), whose index is17^2; equal indices prove equality. The quotient is F17 x F17, so its additive exponent is17.

## Exact cube image and full Gaussian observation

B-FV1 enumerated every one of the256 binary vectors using exact rational inverse-lattice residues. For g (the code uses its negative, defining the same ideal), the image has176 elements and fiber histogram

    112 singleton fibers, 48 double fibers, 16 triple fibers;
    112+2*48+3*16=256,   112+48+16=176.

The same count can be reproduced by reducing binary polynomials modulo (17,Y^2-5Y+1), with recurrence Y^2=5Y-1. This finite count is not inferred from field rank. Independent-block decomposition gives C_J=176^m exactly.

For S uniform binary, independent G~D_(J,t), and full unwrapped Yobs=S+G, B-CUBE-THETA-v1 gives

    (11/16)^(n/8) <= p_guess(S|Yobs)
       <= min(1,(11/16)^(n/8) exp((pi/4+1/2)n/t)).             (F1)

At the frozen t=2n^2 ell, the upper/lower ratio is at most exp((pi/8+1/4)/(n ell)). Alternatively the exact full guessing probability factors as p0(t)^m: both the lattice Gaussian and uniform secret are independent across the orthogonal blocks. This is true independence of the specified joint law, not a multiplication of conditional marginal success claims.

The old index bound is vacuous for every t because N(J)/2^n=(289/256)^m>1. Thus this is a strict information-theoretic enlargement. It does not establish a useful computational enlargement.

## Public fractional-source endpoints

Fix q coprime to17, and preserve the supplied J metadata in both worlds. A planted multiplier is a~D_(J^-1,s), reduced modulo qJ^-1 and identified with A in R_q. Its comparator is uniform A in R_q. The public F belongs to J, so Fa is integral and the computable product F A moduloq equals Fa moduloq. Because N(F)=17^(2m) is coprime toq, multiplication by F is bijective on R_q. Therefore the comparator F A is exactly uniform in R_q, including zero and all nonunit outcomes.

Every coefficient of Fa is an inner product of a with a signed rotation of F of Euclidean norm sqrt(5). The actual lattice-Gaussian MGF bound from A-FRAC gives

    Pr[max_j |(Fa)_j| > s sqrt(5) U] <= 2n exp(-pi U^2).

Let K=s sqrt(5) U. Accept if every centered coefficient of F A belongs to [-K,K]. Planted acceptance is at least1-2n exp(-pi U^2). Comparator acceptance is exactly

    [min(q,2 floor(K)+1)/q]^n.

The test uses one sample and a public ring multiplication. It has no retries, selection, nonzero conditioning, hidden advice, or proof-variable input. For s=sqrt(2)ell^2 and U=ell, K=sqrt(10)ell^3, while q>=n sigma=8n^3 ceil(sqrt(kn))ell^4. This is an efficient high-advantage public-source distinguisher throughout the frozen regime.

## Noise and delivered Gaussian geometry

The ordinary multiplication basis of J is public and has each column norm sqrt(5), operator norm<=||F||_1=5. In particular the frozen proof-only basis bound tau2=2n^2 is more than sufficient. The fixed t=2n^2 ell and sigma=8n^2 ceil(sqrt(kn))ell^4 satisfy sigma>=2ts sqrt(kn)ell. The original rectangular Gaussian completion and its normalizers therefore remain compatible; none of G,H or their conditioning law is changed.

The delivered width remains W=nq/(sqrt(2)d0). The coordinator's provisional M1 sampler applies both through the public multiplication basis, whose Gram–Schmidt lengths are at most sqrt(5), and through exponent17/HNF diagonals<=17. At eta=2^(-4n), its u=4n condition is met by the inherited width. This conclusion uses ordinary classical Gaussian sampling, without coherence or a replacement width oracle. Even without accepting M1 yet, the explicit short public basis identifies the computational obligation as the standard basis-Gaussian simulation rather than a hidden ideal-lattice problem.

## Disposition

Keep this as a sharpened entropy/normalizer regression and a demonstration that norm>2^n alone is not meaningful computationally. Stop this explicit-generator block route as a hardness direction. A discriminating next mechanism would need a noncircular way to certify small exact cube image for an ordinary-basis ideal while neither exposing an efficiently usable short basis nor falling under the annihilator/HNF criterion, and then a reduction relating that exact public family to a standard hard distribution. No such mechanism is supplied here.
