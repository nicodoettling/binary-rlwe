# Additional historical parameter definitions for SV-RS-ACTUAL-v1

These are definitions/assumptions only. The current review must independently evaluate the claimed parameter corollary.

The inherited fixed-target interface uses epsilon0=epsilon_*/2, epsilon=epsilon_*/4, delta=epsilon_*/16 and r=epsilon_*ell^2/(1024 n K chi Qmax). The master auxiliary list and K,ell precede source ideal execution. Its valid polynomial-value parameter families are permitted as assumptions, not as a claim of a fixed family for all adversaries.

For w=sqrt(n)ell^2, h0=delta*w/(32nK), define a0,max=D^(1/n)*w^(1-2/n)*h0^(2/n)/(n Qmax) and Smax=max(0,(n/2)log(1/a0,max)). The common integer kappa must satisfy
kappa>=max(4Smax+4n+4log(K+1)+20,2K,2/delta,20log3,log(8n/zeta)) and 3w exp(-kappa)<Qmin/(8D).
The finite C8 loop bounds Q_*=n Q_H are polynomial in the supplied polynomial-value parameters, with their precise inherited formula unchanged. epsilon_C=min(1/16,zeta/(64KQ_*)); a=Up(sqrt(log(8n/epsilon_C)/pi))+1. Up evaluates to certified error1/8 then takes a rational ceiling.
The inherited interface sets chi=a but expressly permits a larger integer chi with explicitly charged value. It also requires d0=delta*ell^2/(64nKchi)<Qmin/(4D^(1/n)).

Primary provenance for these definitions is DD/coordinator/am-main-theorem-v3.md sections2 and4, DD/coordinator/fixed-main-statement-v2.md and the C8 loop excerpt supplied in this packet. These references identify provenance only; the allowed mathematical reads remain the packet and listed primary sources.
