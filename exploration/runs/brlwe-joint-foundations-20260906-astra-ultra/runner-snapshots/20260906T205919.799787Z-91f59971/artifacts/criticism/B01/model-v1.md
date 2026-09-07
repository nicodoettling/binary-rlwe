# Frozen mathematical packet B01-M1

This packet specifies mathematical objects and two statements to assess. It contains no proposed proof. All logarithms used for entropy are natural unless a base is displayed. Distinguishing advantage is an absolute acceptance-probability difference. The academic research context is supplied in the complete assignment scope.

## Finite statement A

R is a finite effectively represented commutative ring. Draw (J,U,F) from a fixed law mu, where J is an ideal, I=Ann(J), Q_J=R/J and U belongs to I. Let V be conditionally uniform in I and independent of (U,F) given J. Let E have a fixed public law P_E, independent of these variables. Let S and G have fixed public laws P_S,P_G and be mutually independent and independent of (J,U,F). Write Y=S+G. Given (J,U,F), draw H from a fixed mathematical kernel, with coins independent of S,G.

Assume precisely
TV((J,U,F,FG+H),(J,U,F,E)) <= eta_N,
TV((J,U,F,H,Y,pi_J(S)),(J,U,F,H,Y,Z)) <= eta_X,
where Z is uniform in Q_J and conditionally independent of (U,F,H,Y) given J. H is integrated out in the first comparison and retained in the second. The first comparison's E is independent of (J,U,F).

Let S0,E0 be independent copies from P_S,P_E, independent of source variables. Let
P=(U+F,(U+F)S+E),
Q=(U+F,V+FS0+E0),
eta_iso=E_mu[1-|UR|/|I|].
Statement A1 is TV(P,Q)<=min(1,2eta_N+eta_X+eta_iso).

Define an independently noised computational challenge:
world 0: (A,C)=(U+F,V+E0);
world 1: (a,c) independent uniform R elements.
Only the pair is public; J,U,F,V,E0 and H are not provided. Neither challenge takes S as input, and H is absent from the challenge sampler. The target is (a,aS+E), with uniform a independent of S,E. Statement A2 is that for each randomized public bit test D there are two public tests B1,B2, each invoking D once and otherwise using only public secret/noise samplers and ring operations, such that
Adv_target(D)<=Adv_source(B1)+Adv_source(B2)+2eta_N+eta_X+eta_iso.
Determine explicit tests and resource costs if the statement holds. Describe finite implementation errors if the mathematical public samplers are approximated. Do not presume that H needs to be efficiently sampled by those tests.

Boundary models to classify include U=0; U inducing a bijection Q_J->I; and over F3, S uniform {0,1}, G uniform F3 with Y=S+G. Distinguish retaining the original S as an additional observation from discarding it. All variables and independence premises must be checked jointly.

## Ring specialization and finite statement B

Let n be a power of two, q an odd prime with q=1 modulo 2n, and R_q=F_q[X]/(X^n+1) in coefficient basis. The public ring description includes all CRT roots or a primitive 2n-th root. Let 1<=d<n and b>=1 be integers. Choose T uniformly among d-element subsets of the roots. Let I_T be the elements supported on T and J the ideal vanishing on T. Conditional on T, U and V are independent uniform elements of I_T, including zero coordinates. F is independent of T,U,V and is an integer coefficient vector supported in [-b,b]^n; its specified distribution may be arbitrary. S,S0 are independent coefficientwise fair binary vectors. E,E0 are independent iid coefficient D_sigma integer vectors, independent of all other variables, wrapped modulo q at public output; D_t(k) is proportional to exp(-pi k^2/t^2).

Define the two public laws P,Q exactly as in A1 with these variables. Fix a nonnegative integer R0 and let
B0=nb+R0,
delta_E=Pr[an iid D_sigma vector lies outside [-R0,R0]^n],
eta_iso=1-(1-1/q+1/q^2)^d.
Assume
2b<q,
q^(1-2d/n)>2b sqrt(n),
q^(1-d/n)>2B0 sqrt(n).
Statement B1 is TV(P,Q)>=max(0,eta_iso-2delta_E).
Assess whether there is a finite deterministic public test witnessing the stated bound and provide its true runtime class. Hidden T,U,F,V,S are not algorithm inputs. Statistical distinguishability and polynomial-time distinguishability are different conclusions.

Boundary examples include n=4,q=97,d=1,b=1, F=0 and errors identically zero (a deliberately modified finite noise model), with R0=0; and equality instead of strict inequality in either displayed norm gate.

## Exact shared asymptotic model

For sufficiently large powers of two n, ell=ceil(log2 n), d=floor(sqrt(n)/ell^4), b=ell^2, tau=ell, sigma=2n ell^3. Fix constants c>0 and K before choosing a test; q is a split prime with sigma*n^c<=q<=n^K. One explicit regime to assess is c=1,K=16 along qualifying primes. F coefficients are independent D_ell conditioned on [-b,b]. Both U conventions (uniform I_T or independent nonzero coordinates on T) must be distinguished explicitly. V is uniform I_T independently conditional T. All work concerns m=1.

For possible instantiation of the mathematical H kernel, let M_F be integer negacyclic multiplication and B_F=sigma^2 Id-tau^2 M_F M_F^t. In coefficient order take the unique rational decomposition B_F=L diag(v_i)L^t, L unit lower triangular and pivots positive. Draw h_i sequentially with mass proportional to exp(-pi(h_i-c_i)^2/v_i), c_i=sum_(j<i)L_ij y_j and y_i=h_i-c_i, with fresh coins. This defines H_seq exactly. It is not defined as multivariate D_B. It is independent of S,G conditional F. Its statistical comparisons may be assumed in statement A; this review need not prove a general extraction theorem from scratch.

For statement B in this asymptotic model take R0=ceil(sigma ell), delta_E<=2n exp(-pi ell^2). Determine the c range in which the finite gates follow from the stated lower bound on q. Determine whether the resulting error budget is negligible; fixed K cannot depend on an adversary's advantage exponent.

Permitted primary sources: public mathematical literature, especially https://eprint.iacr.org/2018/494, https://eprint.iacr.org/2020/1185, https://eprint.iacr.org/2022/709, and https://dlmf.nist.gov/20.5.E3. No external source result is assumed merely from its name. Do not read coordinator ledgers, plans with scientific assessments, worker notes, proposed proofs, prior verdicts or other criticism until this blind report has been frozen and hashed.
