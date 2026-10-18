# RF2 addendum: exact natural-log ceiling in B Gaussian-periodic v2

PROVISIONAL independent nonblind recheck, 2026-10-17T21:28Z. Root requested the precise BT4 Section 9 argument before B-v2 acceptance. No contact with BT5; no experiment. Inputs: BT4 report-v1.md SHA256 e2ef724b22e7db12b94f500d42d522b3fd2ecbfd4c8d0905f5dfbc0716f1c610, Section 9 (lines 342–394); B theorem-v2 SHA256 be7f05d67fc8f2b24fc6b93321c95005f4d7f6e24bab513b2cbaf35c82aeaad7 and proof-v2 SHA256 207a9af38eb570e2a140d88008c0f4bc363f7d3c8a72049c53bbab85798910b4.

Verdict: BT4's elementary Hermite-integral separation argument is valid. It supplies a polynomial-bit implementation of the exact integer L=ceil(40K log(16/nu)) for the rational input model of B v2. This removes the stated logarithmic-ceiling qualification without changing B's scalar law or constants. It does not turn expected running time into bounded running time, certify C's primary OHCP complexity contract, or supply a source hardness edge.

## Independent check of all estimates

Let T=16/nu=U/V>1 in lowest terms and x=m/(40K)=A/B>0 in lowest terms. The candidate boundary integers m have size O(K^2), so A=O(K^2), B=O(K). Let V<=2^H with H bounded by the full encoding length. Choose integer N>=32(A^2+H+A+1), and put f(t)=t^N(x-t)^N/N!, F=sum_{j=0}^{2N}(-1)^j f^(j). Differentiation gives (e^t F)'=e^t f. Consequently

    I'=B^N integral_0^x e^t f(t) dt=C e^x-E,
    C=B^N F(x), E=B^N F(0).

For an explicit integrality check, set d_j=binom(N,j)(N+j)!/N!. The endpoint formulas are

    C=sum_{j=0}^N (-1)^j d_j A^(N-j) B^j,
    E=(-1)^N sum_{j=0}^N d_j A^(N-j) B^j.

Both are integers. Also |C|<=C0=(A+B)^N(2N)!/N!, by the binomial theorem and (N+j)!<=(2N)!.

On (0,x), f is positive. Using e^x<=3^A, x<=A and N!>=(N/3)^N yields

    0<I'<=3^A A (3A^2/N)^N < 2^(-H-2) <= 1/(4V).

Indeed 3A^2/N<=3/32<1/8 and log2(3^A A)<=3A for integer A>=1, while N>=32(H+A+1). These are stronger than needed for the last inequality. If C=0, then I'=-E would be an integer strictly between 0 and 1, a contradiction. Thus division by C is legitimate.

On t in [x/3,2x/3], t(x-t)>=2x^2/9 and e^t>=1. Hence

    I'>=I0=(x/3)(2A^2/(9B))^N/N! >0.

If CT-E is nonzero, its absolute value is at least 1/V and therefore |C| |e^x-T|>=1/V-I'>=3/(4V). If CT-E=0, then |C| |e^x-T|=I'>=I0. In either case

    |e^x-T| >= min(3/(4VC0), I0/C0)>0.

This is an explicit rational lower bound. Its numerator and denominator have bit lengths polynomial in H and K: N is polynomial, factorials require O(N log N) bits, and all powers have polynomial exponents and polynomial-bit bases. Thus certified evaluation of e^x to fewer than one quarter of this bound determines the sign against the exact rational T in polynomial bit complexity. A Taylor-series exponential evaluation suffices because x=O(K), with output precision polynomial in H,K. No transcendence oracle or zero-test for a general computable real is used.

## Ceiling algorithm and scope

Approximate 40K log(T) to a fixed absolute accuracy, leaving only constantly many candidate integers m. Each required comparison is equivalent to the sign of e^(m/(40K))-T, resolved above. Equality never occurs. Standard logarithm approximation here costs polynomial time in the rational input length and log K; it is needed only to constant absolute accuracy of the final quantity. K and p are binary-log ceilings of positive rationals, computable by integer comparisons, and N in B's sampler is a rational-product ceiling. The reuse of the symbol N for the integral degree in this review is unrelated to B's proposal radius.

Therefore the literal B-v2 implementation is covered by its full numerator/denominator encoding-length bound. B v1's omission of those lengths remains a preserved defect. The exact comparator still relies on expected-time exact finite uniform sampling. A bounded outer wrapper must add its separately proved abort/approximation charge; the ceiling argument itself adds zero statistical error.

Claim-specific disposition: RF2/B-GP2 runtime-log-boundary control RESOLVED; RF2/B-GP2 statistical endpoint clauses unchanged; imported regression dispositions unchanged; C-OHCP finite-primary contract remains separately OPEN pending its actual primary-algorithm audit. This addendum is review evidence, not an acceptance decision.
