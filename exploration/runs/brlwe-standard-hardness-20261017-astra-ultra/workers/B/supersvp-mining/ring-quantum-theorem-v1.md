# B-SUP-RQ-T v1 — uniform-secret ring search to ring SIS

Status: PROVISIONAL new ring extension. This is a quantum SEARCH reduction for the explicitly stated uniform-secret hinted law. It supplies neither a decision-to-search reduction nor binary-secret hardness. Proof: ring-quantum-proof-v1.md.

Let Rq=Fq[X]/(X^n+1), n a power of two and q an odd split prime. Let a be uniform in Rq^m conditioned on generating Rq. Let Z be ANY public auxiliary tuple sampled by an explicitly fixed conditional law given a, independently of the fresh secret and errors. It may include W and the canonical ring hints from ideal-ring-sis-theorem-v1.md; the reduction receives the entire (a,Z) and preserves it.

The two response laws are

  planted: (a,Z,b=s a+e), s uniform in Rq,
      e with nm independent coefficient D_chi entries modulo q;
  comparator: (a,Z,u), u uniform in Rq^m independent conditional on (a,Z).

The solver hypothesis is recovery of s on the PLANTED law with probability delta. No success hypothesis on the comparator and no decision hypothesis is assumed. A nonuniform secret substitution is excluded.

Put M=nm, let lambda>=4, H=lambda+ceil(log_2(M+1)), and assume

  4sqrt(H)<=chi<=q/(8sqrt(H)).

Let alpha0=1-nq^-m>0, mu=3chi/q, and

  K1=(1+(q-1)mu^m)^n,
  K2=(1+(q^2-1)mu^m)^n,
  theta=2^(1-M)+16M exp(-2pi lambda),
  z0=q^n mu^M,
  epsilon_E=2M exp(-pi q^2/(8chi^2)),
  Bbad=z0+sqrt(K2 theta)/alpha0.

The Gaussian Fourier-state tail estimate used here is precisely the one-dimensional/product estimate proved in primary 2026/2443 Lemma7.2; its proof does not require a random general matrix. It is separate from the matrix-ensemble moment estimate, which is replaced by the new ring proof below.

Given coherent reversible access to a polynomial-size recovery circuit and its inverse, there is a quantum polynomial-time algorithm that invokes each once and outputs a nonzero y in R^m satisfying

  sum_i a_i y_i=0 mod q,    ||y||coef<=q sqrt(M)/(2chi)

with probability at least

  [max(0, delta-epsilon_E-sqrt(Bbad))]^2 /(K1/alpha0) - delta_Q.

Here delta_Q is the explicitly budgeted total trace/implementation error for state preparation, Fourier transformation and reversible arithmetic; all full rational parameter encodings and log(1/delta_Q) are charged. The ideal algebraic algorithm and exact finite register states are specified in the proof. This uses the supplied public tuple, so no sampler for the arbitrary conditional metadata law is required.

For example, if m>=ceil(log_2 q), M>=4lambda+4, and n(q^2-1)mu^m<=2^-lambda, then K1,K2=1+O(2^-lambda), z0 is negligible, and the result has success delta^2-negl(lambda), with polynomial dimensions and appropriately small delta_Q. The Fourier error estimate remains exponentially small at these widths. The condition involves the number m of RING samples, not the coefficient dimension M.

This repairs the general-matrix step Pr[Ax=0]<=q^-n, which is false for ring zero divisors, by an exact shared-key moment calculation. It leaves untouched the separate low-index ideal worst-case premise, the hinted ring decision-to-search step, auxiliary-width/decomposition-degree effects, and binary-secret conversion. No claim of standard binary-RLWE hardness follows.
