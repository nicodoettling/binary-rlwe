# C1 useful partial — source transfer

Status: PROVISIONAL author analysis, 2026-09-07 21:47 UTC. No experiment has run; coordinator slot requested and awaiting release. Exact cap read from launcher-run.json's cap.status_file; assignment ends 22:15 UTC.

## Frozen source

R=F_q[X]/(X^n+1), q odd split prime; T uniform d-subset of CRT roots, I_T supported on T. Draw U,V independently uniform in I_T and F,H independently with iid coefficient D_ell. Planted challenge is (U+F,V+H); comparator is the independent uniform R pair. Only these two public components are supplied. Target is one pair (a,aS+E) for a uniform in R, S independent coefficient-binary, E independent iid coefficient D_sigma.

## First exact mixture falsification

Let delta in (0,1/2), Q=Bernoulli(1/2), P_bad=point mass at 0, and P_good=Bernoulli(1/[2(1-delta)]). Then P=(1-delta)P_good+delta P_bad=Q exactly, but D(x)=x has positive P_good-versus-Q advantage delta/[2(1-delta)]. Thus no inference of arbitrary inverse-polynomial active-source advantage from mixture-source advantage is valid from the mixture decomposition alone. Every adaptive repeated public computation on a single challenge is one Markov kernel K and KP=KQ; independent internal tapes do not alter the challenge law. This does not refute an implication using additional specific algebra of actual HLBDD.

## Both-point span defect

Even granting hidden U,V as proof variables and granting arbitrary fresh uniform ring coefficients, all ideal-linear combinations remain in J0=RU+RV. A coordinate of T is absent from J0 precisely when U_i=V_i=0, independently with probability q^-2. Conditional on U,V, alpha U+beta V with independent uniform alpha,beta in R is exactly uniform in J0. Its average conditional distance from uniform I_T is

    E[1-|J0|/|I_T|] = 1-(1-q^-2+q^-3)^d.

At q=3,d=1 the value is 2/27. Two points improve the original 2/9 defect but fixed polynomial q keeps a nonnegligible inverse-polynomial lower bound. Fresh linear coefficients and arbitrary repeated combinations cannot fill the common-zero set. This is a retained-variable/support obstruction for ideal-linear transformations, not yet a public-pair TV lower bound and not an obstruction to arbitrary public maps, additive fresh masks, nonlinear maps, or changes in the source family. Multiplying observed noisy components by uniform ring coefficients can also destroy the required small-noise law, so even the optimal latent span sampler is not a claimed public target reduction.

## Larger-q candidate requiring analytic recheck

Take log q=Theta(n^(1/8)), d=floor(n^(1/4)), ell=ceil(log2 n), sigma=2n ell^3. Then Lambda=d log q=Theta(n^(3/8)), while the displayed X1 exponent E_X is Theta(n^(5/8)/polylog n); the displayed finite X1 gates appear eventually satisfied and eta_iso<=d/q is negligible. Polynomial representation follows from log q=poly(n). The old proof cannot simply be cited because its frozen theorem assumed polynomial q. Need inspect the actual extractor's q dependence, replace polynomial-in-q root enumeration by polynomial-bit randomized root finding, and justify an admissible prime family or explicitly use promise-input prime/root descriptions. Exact source parameters differ from the polynomial-q baseline and remain an independent computational assumption.

Next discriminating work: exact finite controls; actual X1 proof and primary theorem hypotheses; coherent larger-q resource/source statement.
