# Exact ideal-subspace conditioning test for a general-matrix import

PROVISIONAL coordinator lemma, 2026-10-17. This is a narrow distributional calculation motivated by the supplied SuperSVP paper. It is not a general impossibility theorem or a cryptographic hardness result.

Let N be a power of two, q an odd prime with q=1 mod2N, and 0<m<N. Identify F_q^N with F_q[X]/(X^N+1). Let H be its invertible negacyclic shift. Draw a full-row-rank m-by-N matrix A uniformly. Its kernel is an ideal if and only if its row space is invariant under the transpose shift (equivalently under the inverse transpose). More explicitly, kernel invariance is equivalent to existence of an invertible m-by-m U with A H=U A. This follows by factoring the linear map AH through the surjection A when ker A is H-invariant; H is invertible so the induced quotient map U is invertible. The reverse implication is immediate.

The split polynomial has N distinct roots. In its eigenbasis, invariant subspaces of a diagonal operator with distinct eigenvalues are exactly sums of eigenspaces: polynomial interpolation gives every coordinate projection as a polynomial in H. Hence there are exactly binom(N,m) invariant m-dimensional row spaces. Every m-dimensional subspace occurs equally often as the row space of a uniformly chosen full-rank A. Consequently

    Pr[ker A is an ideal] = binom(N,m) / GaussianBinomial(N,m;q)
                         <= binom(N,m) q^(-m(N-m)).

Here GaussianBinomial(N,m;q)=product_(i=0)^(m-1) (q^(N-i)-1)/(q^(m-i)-1). Each factor after removing q^(N-m) is at least one, proving the displayed upper bound. The total variation between the uniform full-rank matrix law and that law conditioned on ideal kernel is exactly one minus this probability.

The index of the integer kernel lattice {x in Z^N:A x=0 modq} is q^m. Its small index can match the entropy budget m log2q<=rho N, but this fact alone does not make its general-matrix distribution an ideal lattice distribution. Rejection conditioning to ideal kernels costs the displayed inverse probability. Generic invertible coordinate transformations can change the kernel but usually destroy compatibility with the fixed negacyclic ring action; their algebraic invertibility does not prove the required distributional or response/noise statement.

Scope: this refutes a direct identification or cost-free conditioning of uniform matrix kernels with split-ring ideals. It does not rule out a structured sampler, a reduction with a different ambient ring, a module interface, a computational transformation, or a nonuniform/hinted premise. Both q and the quotient index must remain distinct from the modulus of any downstream SIS/LWE experiment.

Finite falsification attempt: ROOT-IDEAL-SUBSPACE-1 exhaustively checks all6 lines in F5² and all89030 planes in F17⁴, with exact modular arithmetic; code and original output are preserved under experiments. Finite agreement is not a proof of asymptotic hardness.
