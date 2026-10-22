# SV-GAP-DECODE-v1 author proof

Since p is the exponent, pR is contained in J. The completely split semisimple algebra R/pR is F_p^n; its ideals are specified by subsets of zero coordinates, so J is the product of the distinct prime ideals indexed by T_alpha. Hence pJ^-1 is the integral product of the complementary prime ideals. The vector a=p*lambda modp has Fourier support contained in T_alpha, exactly as in SV-RS-DECODE-v1.

Cut the cyclic index set at a largest gap g=g_max. The remaining support lies in an interval of n-g+1 consecutive indices, including its endpoints. If its first index is j0 and theta=alpha^2, inverse Fourier transformation writes

    a_i = alpha^(-(2j0+1)*i) * f(theta^(-i)) modp,

where deg(f)<n-g+1; missing support indices give zero coefficients. The n evaluation points are distinct and the coefficient scaling is nonzero. Thus the residues lie in a generalized Reed–Solomon SUPERcode of dimension w=n-g+1 and Hamming distance g. No assumption that every interval frequency is actually present is needed.

Coefficientwise nearest-integer rounding of pT changes at most h=floor(4p^2r^2) positions, by Parseval and the1/2 threshold argument. The strict condition8p^2r^2<g implies2h<g and n>=w+2h. The explicit monic-error-locator linear system from SV-RS-DECODE-v1 therefore recovers f, and hence a modp. Since r<1/2, lifting each recovered residue to the closest coefficient of T recovers lambda. This is a direct pointwise decoder and does not reveal or assume lambda during recognition.

The positive cyclic gaps between t support indices sum to n, so their maximum is at least ceil(n/t). If t*log2(p)<=rho*n, then n/t>=log2(p)/rho, giving the stated simpler guard. Strict versus weak inequalities are preserved: the guard is strict even when the gap lower bound is an equality.

Ordinary-input acquisition uses the exponent computation, deterministic numeric-p primality/root search, and basis-column evaluations from SV-RS-DECODE-v1. Enumerate all n primitive2n-th roots, form their support index sets, sort cyclically, and choose a maximum gap with deterministic ties. All scans and finite-field operations have polynomial size. The error-locator degree is less than n under the guard. Exact input and output rational bit lengths are charged. This is an algorithmic consequence of the displayed structure, not a computational assumption on unclassified ideals.
