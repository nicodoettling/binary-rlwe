# GP v2 exact natural-log ceiling: complexity addendum

Status: PROVISIONAL source/complexity recheck. This preserves gaussian-periodic-theorem-v2.md and proof-v2.md WITHOUT changing their finite kernel. It reconstructs BT4/report-v1.md Section9, as directed by root after BT5's implementation qualification.

The only transcendental ceiling is L=ceil(40K ln(16/nu)). Approximate it to fixed absolute accuracy, leaving a constant number of candidate integer boundaries m=O(K²). To resolve one boundary compare exp(x) with T=16/nu, where x=m/(40K)=A/B>0 is in lowest terms and A,B are polynomial in K. Write T=U/V with V<=2^H; H is bounded by the complete encoding length of nu plus a constant.

Choose integer N>=32(A²+H+A+1), define f(t)=t^N(x-t)^N/N!, and F(t)=sum_(j=0)^(2N)(-1)^j f^(j)(t). Since F+F'=f,

  I=B^N integral_0^x exp(t)f(t)dt=C exp(x)-E,
  C=B^N F(x), E=B^N F(0).

The endpoint derivatives make C,E integers: every nonzero derivative has order N+j and equals, up to sign, [(N+j)!/N!] binom(N,j) x^(N-j). Multiplication by B^N clears its denominator.

The estimates

  0<I<=3^A A(3A²/N)^N<2^(-H-2)<=1/(4V),
  |C|<=(A+B)^N (2N)!/N! = C0,
  I>=(x/3)(2A²/(9B))^N/N! = I0>0

follow respectively from bounding exp(t), the factorial inequality N!>=(N/3)^N, summing endpoint derivatives, and restricting the positive integral to [x/3,2x/3]. The chosen N makes the first upper bound strict: 3A²/N<=3/32, and its exponential decay dominates 3^A A and2^H. Since0<I<1 and E is integer, C cannot be zero.

If CT-E!=0, its magnitude is at least1/V, giving |exp(x)-T|>=3/(4VC0). If CT-E=0, then |exp(x)-T|=I/|C|>=I0/C0. Both explicit positive rational lower bounds have polynomial bit length in H and K. Evaluating exp(x) to that precision therefore determines the sign. There is no equality boundary. Thus every candidate ceiling boundary, and hence L, is computable in polynomial bit complexity under v2's complete rational encoding convention.

This closes the literalization qualification; it does not alter the endpoint proof or samplers. A previously written theorem/proof v3 using Lplus=40K ceil(log2(16/nu)) is preserved as an OPTIONAL, UNUSED finite-kernel variant, not as a necessary repair of v2. The file gaussian-periodic-bt5-literalization-v1.md records the earlier decision to use that variant before this exact argument was inspected; it is not evidence that v2 is false or inefficient. The bounded wrapper below uses v2 and may use Lplus merely as an integer upper bound on its trial count.
