# Binary-error normal form with exponentially accurate Gaussian fresh errors

2026-10-17. PROVISIONAL, not accepted. This is a conditional distributional/oracle reduction. It does not establish binary-error RLWE hardness from standard RLWE or a worst-case ideal problem. Proof: switch-gaussianize-proof-v1.md. No experiment was used to derive this statement.

## 1. Parameters and full source laws

Let n be a power of two, R=Z[X]/(X^n+1), q an odd prime fully split in R, and t,M,k positive integers. All coefficient vectors use the power basis. Write B_n for the uniform law on {0,1}^n, reduced modulo q. Fix rational sigma>=2 and numerical budget eta in (0,1/4). Let N=t+M+k.

Planted source BE(N): sample one s uniformly in R_q, mutually independent a_1,...,a_N uniformly in R_q and e_1,...,e_N from B_n, then b_i=a_i s+e_i. Comparator U(N): all a_i,b_i mutually independent uniform in R_q. Public input is only these pairs and the parameters. No error hints, secret advice, trapdoor, or conditioned secret is supplied.

A weaker heterogeneous source would suffice: the reserved t pivot errors are independent B_n, while the M output errors are already independent coefficient D_{Z,sigma}^n. Its comparator is still U(N); it is a separate source problem and is not supplied by a standard Gaussian-RLWE theorem merely because most errors are Gaussian.

## 2. Public simulator and exact intermediate laws

Reserve the first t pairs exclusively for pivot selection. Choose the first p in this pool for which a_p is a unit. Discard every other pivot-pool pair. If none exists, output FAIL, with no recovery-oracle call. The pool is never reused for output samples. Let

    u=(1-1/q)^n,       u_t=1-(1-u)^t.

For each of the next M untouched pairs define

    A_i=-a_i a_p^{-1},       C_i=b_i+A_i b_p.

On success, under BE(N), the exact whole output law is

    S=e_p ~ B_n,
    A_1,...,A_M iid uniform R_q,
    C_i=A_i S+e_i,

where S, all A_i, and all fresh e_i are mutually independent. The original s has cancelled. The one shared S is reused across all outputs; it is not resampled. S=0 is included with its original probability 2^{-n}; S need not be a unit. On the comparator, all (A_i,C_i) are exactly iid uniform. The abort probability 1-u_t is identical in both worlds. The reduction retains its selected input pair privately for recovery; the recovery oracle receives no pivot-pool responses or auxiliary metadata.

## 3. Positive Bernoulli deconvolution

For p_j=D_{Z,sigma}(j), let

    delta_sigma = sum_{j in Z} (-1)^j p_j.

For j>=0 define

    f_sigma(j)=2 sum_{h>=0} (-1)^h p_{j+1+h},
    f_sigma(-1-j)=f_sigma(j),
    F_sigma(j)=f_sigma(j)/(1-delta_sigma).

These absolutely convergent formulas define a nonnegative probability distribution F_sigma on Z. If E is a uniform bit independent of F~F_sigma, then

    Law(E+F) = Q_sigma
              = (D_{Z,sigma}-delta_sigma * pointmass_0)/(1-delta_sigma).

In particular, with TV in the 1/2 L1 convention,

    TV(Q_sigma,D_{Z,sigma})
      = delta_sigma(1-p_0)/(1-delta_sigma)
      <= delta_sigma/(1-delta_sigma),
    0<delta_sigma <= 2 exp(-pi sigma^2/4)/(1-exp(-2 pi sigma^2))
                  <= 3 exp(-pi sigma^2/4).

For sigma>=2, delta_sigma<1/2. The sampler in the proof returns an integer law Ftilde within eta/(Mn) of F_sigma, in strictly bounded time polynomial in n,M, sigma (its value), the bit lengths of sigma and eta, and log(1/eta). Thus this is polynomial time when sigma is polynomially bounded in the security parameter. No claim of runtime polynomial only in log sigma is made.

Independently add one Ftilde sample to every coefficient of every C_i. Call the resulting response B_i. Conditional on pivot success, the full planted tuple (S,(A_i,B_i)_{i=1}^M) is within

    Delta = Mn * delta_sigma/(1-delta_sigma) + eta

of the original target with S~B_n, A_i iid uniform, and independent coefficient D_{Z,sigma}^n errors. Under U(N), the complete output (A_i,B_i) remains EXACTLY iid uniform, for any finite numerical additive sampler. The added variables are private coins; releasing them would change the Gaussian-error target law.

Choosing sigma>=2 with 3 exp(-pi sigma^2/4)<=epsilon/(4Mn), and eta<=epsilon/2, gives Delta<=epsilon. Therefore sigma=O(sqrt(log(Mn/epsilon))) suffices; q may remain polynomial and q/sigma polynomially large. This parameter window is for this conditional switching edge only, not an imported hardness intersection.

## 4. Recovery, decision, samples and runtime

Suppose a binary-secret recovery oracle succeeds with probability a on the original target with M samples and width sigma. Run it on the transformed tuple. If it returns Shat, set

    shat=a_p^{-1}(b_p-Shat) mod q.

On BE(N), this recovers the original secret with probability at least u_t max(0,a-Delta). Modular recovery of e_p determines the actual bit vector because q is odd. No inversion of e_p is performed.

For a decision reduction, reserve the last k source pairs exclusively for validation, unused in selection, transformation, and recovery. Accept precisely when a valid candidate shat is produced and every coefficient of every b_v-a_v shat belongs to {0,1} modulo q. Planted acceptance is at least u_t(a-Delta); comparator acceptance is at most u_t(2/q)^{nk}. Thus signed planted-minus-uniform advantage is at least

    u_t [a-Delta-(2/q)^{nk}].

There is one oracle call, exactly t+M+k input ring samples, and M target samples. Inversion and ring arithmetic are polynomial in n and log q; the explicit scalar sampler is polynomial in sigma's value and all input encoding lengths. The helper generates independent additive coefficients and never requires the binary errors or original secret.

For a decision oracle of absolute target advantage a, the direct simulation instead gives absolute source advantage at least u_t(a-Delta). There is no need for the validation samples in this variant.

## 5. Scope and outstanding primary edge

The constructed direction is

    binary-error uniform-secret RLWE -> binary-secret Gaussian-error RLWE.

It is not standard Gaussian RLWE -> binary-error RLWE. Normal form alone leaves fresh errors unchanged, so identifying the two endpoints without this conversion would be incorrect. The selected-pivot convention deliberately avoids the known bias caused by reusing rows examined during pivot selection. All source errors are genuine iid coefficient bits, not merely bounded, centered-binomial, rounded-canonical, or ternary errors.

No verified standard rank-one ring source theorem is asserted here. A theorem about dense ordinary LWE matrices, higher module rank, a different modulus/degree, or an extra average-case Ring-BinLWE assumption cannot fill that missing edge by renaming it.
