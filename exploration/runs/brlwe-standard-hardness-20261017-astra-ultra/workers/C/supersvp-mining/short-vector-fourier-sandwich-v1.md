# Known short ideal vector gives an explicit finite periodic-Gaussian test

PROVISIONAL new local lemma. This complements the conditional C-OHCP decoding route; it does not extract Fourier mass from an arbitrary decision algorithm and does not undo the earlier sparse-indicator counterexample.

Let J be an integral ideal, D=N(J), q>=2, h=1/(DP), and L=qJ^-1. Let x be a KNOWN nonzero vector in J. In coefficient coordinates write bar(x) for field conjugation, which is an orthogonal signed permutation for this ring. Define the character

    chi_x(y)=exp(2pi i <coeff(bar(x))/q, coeff(y)>).

For z in J^-1, the coefficient inner product <bar(x),z> is the constant coefficient of xz and is integral. Thus chi_x is well-defined on H/L. On F=hZ^n/L it is nontrivial exactly when bar(x)/q is not in DP Z^n, equivalently x not in qDP R. A uniform F sample then has E[chi_x]=0 EXACTLY.

For coefficient spherical Gaussian width w_B, before rounding,

    E chi_x(G_(w_B))=exp(-pi w_B² ||x||coef²/q²).

Nearest-grid rounding changes each coefficient by at mosth/2, hence

    |E chi_x(Q_h(G))-E chi_x(G)|
      <= pi h sqrt(n) ||x||coef/q.

Therefore the efficient Bernoulli test accepting with probability (1+Re chi_x(y))/2 has advantage at least

    (1/2) exp(-pi w_B² ||x||coef²/q²)
       - pi sqrt(n)||x||coef/(2DPq)

over the exact uniform finite comparator. Cosine is evaluated to any prescribed additional error in polynomial bit complexity; charge that numerical error explicitly. The same ideal metadata is retained in both worlds, and additional iid samples can be ignored.

For example, assume w_B>=1, 0<||x||coef<=q/(2w_B), and P>=8pi sqrt(n)/(D w_B). Then x not in qDP R and the displayed advantage is greater than1/8, before a chosen small numerical evaluation loss. This is a direct known-frequency test; it requires no unproved global monotonicity or spectral concentration of an arbitrary oracle.

Together with the separately reviewed C-OHCP and primary quantum BDD-to-DGS import, this gives a quantitative restricted-family comparison:

* A short-vector algorithm at radius q/(2w_B) supplies a constant-advantage finite periodic-Gaussian distinguisher.
* A pointwise advantage-delta distinguisher supplies, quantumly, a vector in the SAME J of radius R_out=(64/sqrt(2))n^(5/2)ka q/(delta w_B), under the exact C parameters.

The two scales differ by an explicit polynomial factor. Both statements concern integral ideals with their actual coefficient geometry. For J=K_T(q0), choose q coprimeq0 and q0>R_out to remain below the public exponent-vector radius. This helps identify the concrete lattice task represented by the new periodic source; it does not establish a reduction from arbitrary standard ideal lattices into this low-index family.
