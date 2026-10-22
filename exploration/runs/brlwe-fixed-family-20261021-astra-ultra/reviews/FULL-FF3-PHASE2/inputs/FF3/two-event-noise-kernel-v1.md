# FF3-TWOEVENT-v1: an explicitly normalized correlated ring-noise kernel

PROVISIONAL constructive lemma and Gaussian instantiation note. This constructs H in the two-secret theorem; it does not extend that theorem to the full binary cube.

Let U and V be uniform laws on finite sets X,Y; let P on X and positive N on Y be noise laws. Choose an efficiently testable event C subset X and write p=P(C), u=U(C), with0<=u<p<=1. Put L(y)=N(y)/V(y). Assume

    (1-p)/(1-u) <= min_y L(y),
    max_y L(y) <= p/u,

where the latter inequality is vacuous when u=0. Define distributions

    g1(y)=[(1-u)N(y)-(1-p)V(y)]/(p-u),
    g0(y)=[p V(y)-u N(y)]/(p-u).

The inequalities give nonnegative entries; summing gives unit mass. The kernel H(x,·)=g1 if x in C and g0 otherwise satisfies UH=V and PH=N exactly, by direct substitution. It is secret-independent, fully normalized, and generally correlates target coefficients.

If p>=3/4 and u<=1/4, sample g1 by proposing from N and accepting with probability1-[(1-p)/(1-u)]/L(y); sample g0 by proposing from V and accepting with probability1-(u/p)L(y). The average acceptances are(p-u)/(1-u)>=2/3 and(p-u)/p>=2/3. Thus ideal evaluation/sampling gives expected at most3/2 trials. All-input capped implementations must pay their numerical/sampler errors and at most3^-L for L rejected proposals. Exact transcendental probabilities are not claimed to have finite exact binary implementations.

For the original Gaussian noise problem, let X=R/QR,Y=R/q0R, P and N be the exact coefficient product wrapped discrete-Gaussian laws. Take C to be the centered coefficient box[-T,T]^n, with2T+1<Q. Then

    u=((2T+1)/Q)^n,
    p=(Pr[E modQ has centered representative in[-T,T]])^n,

where E~D_(Z,sigmaQ). These scalar probabilities and N(y) factor into one-dimensional theta sums; no sum over binary secrets is needed. For q0>=n*sigma0, sigma0>=1, rho_sigma0(Z)<=1+sigma0<=2sigma0 gives the explicit lower bound

    min_y L(y) >= exp(-pi*n*q0^2/(4*sigma0^2));

the crude upper bound max_y L(y)<=q0^n always holds. With T=ceil(sigmaQ*n*q0/sigma0) and Q>=4*q0*(2T+1), the upper condition holds eventually with p>=3/4, while the Gaussian tail from FF3-ENUM gives

    1-p <= n(2+sigmaQ^2/(pi*T))*exp(-pi*T^2/sigmaQ^2).

For every polynomial-value sigmaQ and fixed polynomial-value q0,sigma0 satisfying q0>=n*sigma0, twice this tail is eventually below the displayed target minimum likelihood. Thus this H exists with polynomial-value auxiliary parameters and a strong normalized input-noise reserve. Finite instances require checking the two displayed inequalities using certified bounds. This is an exact mathematical Gaussian noise kernel; a fully frozen finite sampler implementation remains to be supplied before any new algorithmic theorem uses it.

This construction isolates a computational edge cleanly: converting a KNOWN residual's noise law is easy to describe with two scalar normalizers. Selecting suitable residuals without knowing the binary secret is the remaining full-cube problem. Using C to find the true residual by testing all candidate secrets reproduces FF3-ENUM's exponential search cost.

The n1 finite H used in FV4 is exactly this formula with C={0}, p=7/8,u=1/3 and N=(3/4,1/4), yielding H(0,0)=21/26,H(1,0)=H(2,0)=9/26. Therefore the positive n1 controls already verify a concrete instance; they do not certify the infinite Gaussian instantiation.
