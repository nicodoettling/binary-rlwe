# DD1-EXTRACT-v1: ordinary binary-RLWE decision to one selected CRT value


Let n>=2 be a power of two, R_q=F_q[X]/(X^n+1), and q an odd prime congruent 1 modulo 2n. Fix an ordering r_1,...,r_n of its roots, and let e_j be the corresponding CRT idempotents. Fix k0>=1 and an all-input bounded randomized Boolean algorithm D_q acting on k0 ordered ring samples and fixed public metadata. All calls use fresh D_q coins. The error law can be any fixed distribution on R_q; the target case is an exact product coefficient discrete Gaussian reduced modulo q. Raw sample errors are independent across samples and independent of public multipliers and the secret.

For fixed s in R_q, define p_j(q,s), j=0,...,n, as D_q's expected acceptance on k0 independent uniform public multipliers A_i, responses A_i s+E_i, and independent uniform response masks on CRT coordinates 1,...,j in each sample. In particular p_n(q,s)=p_U(q), independent of s. Let S be uniform coefficient-binary, shared across the whole raw input batch. Write d(q,s)=p_0(q,s)-p_U(q).

Supply rational 0<epsilon<=1 and 0<eta<1. Put

    a=epsilon/(64n),
    Lcal=ceil(log2(4(n+1)/eta)),
    Ltest=ceil(log2(4q/eta)),
    Ncal=ceil((2048 n²/epsilon²) Lcal),
    Ntest=ceil((2048 n²/epsilon²) Ltest),
    K=k0(Ncal+Ntest).

All ceilings above use exact rational/integer arithmetic; log2 ceilings are computable by bit comparisons. The supplied batch contains exactly K samples, with independent uniform multipliers/errors conditional on S. Split it into a calibration bank of Ncal blocks and a fresh test bank of Ntest blocks, each block containing k0 raw samples. Reuse the calibration bank across all n+1 prefixes, and reuse the test bank across all q candidate values. These reuses do not create new raw source samples.

Algorithm:

1. For each j=0,...,n, apply fresh independent uniform CRT-prefix response masks to every calibration block, run D_q and form empirical mean p_hat_j. Choose j* maximizing |p_hat_(j-1)-p_hat_j|, with a fixed tie rule. If this maximum is less than epsilon/(4n), output FAIL.
2. For each t in F_q and each test block, independently choose p_i uniform F_q per sample and an independent uniform prefix mask W_i on roots 1,...,j*-1. Replace each raw pair by

       A'_i=A_i+p_i e_(j*),
       B'_i=B_i+t p_i e_(j*)+W_i.

   Run D_q and form empirical mean z_hat_t. Compare z_hat_t to the two calibrated endpoint means p_hat_(j*-1), p_hat_(j*). Mark t exactly when its distance to the first is strictly smaller than its distance to the second.
3. If exactly one t is marked, output (j*,t); otherwise output FAIL.

In the ideal uniform-field-coin model, for every fixed s,

    Pr[output is an incorrect pair | S=s]<=eta.                         (E1)

For every fixed s with |d(q,s)|>=epsilon/2,

    Pr[output=(j,s(r_j)) for some j | S=s]>=1-eta.                      (E2)

The test makes at most

    N_D=(n+1)Ncal+q Ntest

D_q calls and consumes exactly K raw samples. Polynomial runtime is in q in VALUE, n,k0,epsilon^-1,log eta^-1 and the actual all-input D_q bound. The raw sample requirement depends on log q. No oracle assertion is made on off-promise calls in other multiplier worlds.

For a fixed q with |E_S d(q,S)|>=epsilon, or more generally for a uniformly selected q from any supplied finite list with E_q |E_S d(q,S)|>=epsilon, the joint extraction success is at least epsilon/2-eta. The latter uses the same epsilon threshold for every q; parameters may use q itself or one Qmax upper bound in Ltest. Taking eta=epsilon/16 gives success at least 7epsilon/16.

Finite fair-bit implementation: the number of uniform F_q draws is at most

    Tfield=k0 Ncal n(n+1)/2+k0 n q Ntest.

Each draw uses ceil(log2 q) bits per rejection attempt, at most B attempts, and returns0 if all attempts fail. For any requested 0<nu<1, choose B>=ceil(log2(Tfield/nu)). The resulting all-input bounded extractor's complete output law is within TV nu of the ideal extractor, pointwise for every raw input. Thus E1 becomes <=eta+nu; E2 becomes >=1-eta-nu; and the average success bound loses nu. Its total runtime includes N_D actual bounded D_q executions, finite ring arithmetic, root/idempotent computation or supplied root data, and at most B Tfield ceil(log2 q) fresh bits. No exact bounded fair-bit sampler for odd q is assumed.

Root data can be supplied or computed by bounded enumeration of F_q, finding an element of order 2n and then all roots/idempotents; this cost is polynomial in q in value and n. Metadata is unchanged across all calls and target comparators. Every empirical block uses the same unknown S as the other raw blocks; a new binary secret per block would invalidate the theorem.

For downstream fractional completion the stacked matrix has K n rows, and the inherited condition is sigma>=2 t s sqrt(Kn)L. The target D_q is therefore promised at that selected sigma even though each call consumes only k0 samples. N_D is not substituted for K, and k0 is not substituted for K.
