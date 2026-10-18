# Executable binary-pivot convolution test

2026-10-17. PROVISIONAL new map and analysis, not an accepted reduction. This uses the exact allowed discrete coefficient source and keeps fresh errors unchanged. No experiment.

## Full map and both endpoints

Input M+1 ordinary RLWE pairs in R_q=F_q[X]/(X^n+1), q odd split prime, shared uniform s, iid full-uniform multipliers, iid coefficient D_tau errors. Comparator: iid uniform pairs. Choose private R uniform coefficient-binary, independently. If designated a_0 is not a unit, abort identically in both worlds. Otherwise set

    a'_i=-a_i/a_0,
    b'_i=b_i+a'_i(b_0+R),  1<=i<=M.

The exact planted law is

    b'_i=a'_i S+e_i,  S=e_0+R modq.

The exact comparator is iid uniform full pairs, even conditional on the pivot, R and all multipliers. The a'_i are iid full uniform and independent of S and the fresh e_i. Conditional on the event S in{0,1}^n, S is EXACTLY uniform binary, and fresh errors remain iid D_tau independent of S and all multipliers. Thus this is an actual executable mixture containing the original binary query law with sigma=tau. No simulation of an unknown error is needed to run the map; the promising branch cannot be observed by the reduction.

Let h_j=Pr[D_tau modq=j], so h_1=h_(-1). For every coordinate,

    Pr[S_j=0]=Pr[S_j=1]=(h_0+h_1)/2.

Hence the branch probability is p^n, p=h_0+h_1. A recovery oracle for the exact binary target with success epsilon consequently recovers S on this branch with probability p^n epsilon. Then e_0=S-R modq and s=a_0^(-1)(b_0-e_0) recover the original secret. Unit conditioning costs u_q=(1-1/q)^n. Recovery of S by an oracle restricted to binary outputs can only occur on the modular binary branch, so p^n is also an upper bound on the direct success. Other oracle outputs or subsequent adaptive processing are not analyzed by this upper bound.

The private R is correlated with S after conditioning on the binary branch, but R is not in the oracle query; the conditional marginal query law is exactly the required one. If a proof exposes R as additional advice to the binary oracle, it must recheck that richer promise rather than assume independence.

The exact source-error characteristic function is not changed in fresh samples. If the target requires another sigma, an additional valid noise conversion must be supplied. Merely naming a larger width does not make a sum of discrete Gaussians exact.

## Direct branch probability at the standard test width

By the exact wrapped-atom bound from distribution-change-v1.md,

    p<=2(1/tau+1/q).

For tau=n^2 and q>=n^2, p^n<=(4/n^2)^n. More fresh samples do not change the pivot branch probability. Independent pivot trials at most multiply this bound by their number; trials selected using responses require separate posterior analysis.

## Polynomial branch implies an easy source in this map

Assume q>=n^2 and p^n>=n^(-C) for a fixed C and sufficiently large n. First p>=1/2 eventually. The upper bound p<=2/tau+2/q then implies tau<=8 eventually. At this bounded width, all wraparound contributions to h_0+h_1 are exp(-Omega(q^2)), uniformly: every noncentral term has |z|>=q-1, and the remaining Gaussian series is bounded by a geometric tail. Thus

    p_raw=(1+a)/rho_tau(Z),  a=exp(-pi/tau^2),
    p_raw^n >= n^(-(C+1))

for sufficiently large n. Since rho_tau(Z)>=1+2a,

    p_raw <= (1+a)/(1+2a)=1-a/(1+2a).

Taking logs yields n a/(1+2a)<=(C+1)log n and therefore na<=3(C+1)log n. Let z=Pr[D_tau=0]=1/rho_tau(Z). Since z=p_raw/(1+a),

    z^n = p_raw^n/(1+a)^n >= n^(-4(C+1)).

So an ENTIRE source error polynomial is zero with inverse-polynomial probability. Also

    Pr[|D_tau|>=2] <= 2a^4/(1-a^5),

because z^2>=4+5(z-2) for integers z>=2. Therefore a fresh error polynomial has every coefficient in{-1,0,1} with probability1-O(n a^4)=1-o(1).

Here is an explicit decision attack on that source. Use one designated unit pivot, guess s*=b_0/a_0, and obtain one independent fresh pair(a_1,b_1). Accept if every centered coefficient of b_1-a_1s* lies in{-1,0,1}. In the planted world, if e_0=0, the guess is correct and the test passes with probability1-o(1), so acceptance is at least

    u_q n^(-4(C+1))(1-o(1)).

In the comparator, conditional on every prior value and a_1, the response b_1 is uniform. Hence the acceptance probability is EXACTLY

    u_q (3/q)^n.

The difference is inverse polynomial. Acceptances from incorrect planted guesses only increase the lower bound. Thus the binary-pivot convolution map has no parameter regime with both polynomial branch probability and hardness of the ordinary decision source at q>=n^2. This statement concerns this concrete map and direct branch use only; it does not rule out an adaptive oracle reduction outside this architecture.

## Cost and precision

The map consumes one pivot plus M fresh samples and performs exact modular arithmetic and iid fair-bit sampling. It introduces no Gaussian sampler beyond the given source samples. The source-easiness test uses two source samples. Its residue-box test is exact. All theta/tail formulas refer to the specified ideal D_tau law; approximate source sampling must add its actual joint TV error to the displayed bounds.
