# Pointwise binary recovery to ordinary sampling on the same ideal

## Conventions and finite inputs

Let \(n\ge2\) be a power of two, \(R=\mathbb Z[X]/(X^n+1)\), and identify its fraction field with coefficient vectors. Conjugation sends \(X\mapsto X^{-1}\). Write \(\|\cdot\|_2\) for coefficient Euclidean norm. The full canonical Euclidean norm is \(\sqrt n\|\cdot\|_2\); canonical infinity norm is the maximum absolute value of a complex embedding. For a lattice \(K\),

\[
 \rho_s(x)=\exp(-\pi\|x\|_2^2/s^2),\qquad
 D_{K,s}(x)=\rho_s(x)/\sum_{z\in K}\rho_s(z).
\]

The continuous coefficient Gaussian \(G_s\) has density \(s^{-n}\rho_s\). Every Gaussian mentioned below has this convention, with canonical width explicitly marked. TV is half the classical L1 distance. State comparisons used by the interfaces use Euclidean norm and trace distance half the trace norm.

The supplied inputs are:

1. An integer \(k\ge1\), a rational \(0\le\rho<1\), an odd prime \(q\equiv1\pmod {2n}\), and an ordinary integer basis of one nonzero integral ideal \(J\subset R\), with \(D=[R:J]\le2^{\rho n}\) and \(\gcd(D,q)=1\). Set \(\Lambda=J^{-1}\) and \(L=q\Lambda\). No short basis, trapdoor, ideal Gaussian sampler, or distribution over ideals is supplied.
2. Finite classical randomized code \(\mathrm{Rec}\), its finite-alphabet bit-machine description, and an explicit worst-case step bound on **every valid input and every random tape** at the ring-sample input length. Fresh fair-bit consumption is bounded by that step bound. Malformed outputs are failures. A known rational \(0<\epsilon_{\rm rec}\le1\) is a lower bound for its probability of returning the actual secret in the following exact experiment for this fixed \(J\): independently sample \(a_i\leftarrow R/qR\) uniformly, \(S\leftarrow\{0,1\}^n\) uniformly, and all \(kn\) integer coefficients of \(E_i\leftarrow D_{\mathbb Z,\sigma}\); give \(\mathrm{Rec}\) the \(k\) pairs \((a_i,a_iS+E_i\bmod q)\).
3. Fix once whether \(\mathrm{Rec}\) additionally receives the ordinary basis of \(J\). If it does, the success premise is pointwise for that same basis/metadata. If it does not, the exact target distribution and its success probability are independent of \(J\). The construction itself receives \(J\) as a sampler input in either case. All comparisons retain the same metadata, and no proof auxiliary variable is appended to \(\mathrm{Rec}\)'s input.
4. Every rational is encoded by its signed numerator and positive denominator. Derived algebraic scalars and logarithms have fixed certified polynomial-time evaluation routines, whose code and actual evaluation cost are charged. No unlimited-word or exact-real unit-cost machine is used.

For families of ideals this is a pointwise premise, or a uniform pointwise premise if one wants a sampler for every member. An average success bound over a distribution of public ideals alone does not satisfy item 2 for every ideal. Hiding \(J\) from \(\mathrm{Rec}\) does not hide it from the reduction.

## Recovery and finite bridge parameters

Set
\[
\begin{split}
 \ell&=\lceil\log_2(2nk)\rceil,&\tau_2&=2n^2,&t_A&=2n^2\ell,\\
 w_B&=r_B=\ell^2,&s&=\sqrt2\ell^2,&
 \sigma&=8n^2\lceil\sqrt{kn}\rceil\ell^4,\\
 \epsilon_B&=\nu=\eta_{\rm cap}=2^{-\ell^2},&P&=2^{2\ell^2}.
\end{split}
\]
Assume additionally \(q\ge n\sigma\). Define
\[
\begin{split}
 \delta_{\rm tail}&=\min(1,4kn e^{-\pi\ell^2}),\\
 \beta&=\min(1,\exp(-(1-\rho)n\log2+1/(2n\ell))),\\
 \theta_A&=2\sum_{j\ge1}e^{-\pi(3\ell^2/4)j^2},\quad
 \Delta_A=(1+\theta_A)^n-1,\\
 \eta_A&=\begin{cases}\min(1,\Delta_A/(1-\Delta_A)),&\Delta_A<1,\\1,&\Delta_A\ge1,\end{cases}\\
 \Delta_B&=\frac{2k\epsilon_B}{1-\epsilon_B}+\frac{2\pi kn}{Pr_B}+kn\nu.
\end{split}
\]
Supply a rational \(0<\delta\le1\) for which
\[
 \delta\le\epsilon_{\rm rec}-\delta_{\rm tail}-\beta-\eta_A
 -\frac{2k\epsilon_B}{1-\epsilon_B}-\frac{2\pi kn}{Pr_B}
 -3kn\nu-2\eta_{\rm cap}. \tag{G}
\]
This is a numerical hypothesis on explicit real quantities, not an instruction to decide equality at a transcendental boundary.

Use the finite group
\[
 F=(DP)^{-1}\mathbb Z^n/L,\qquad |F|=q^nD^{n-1}P^n,
\]
with fixed ordinary HNF/SNF representatives and fixed nearest-grid tie convention \(Q_h\), \(h=1/(DP)\). The two input laws are iid \(Q_h(G_{w_B})\bmod L\) and iid uniform \(F\), respectively, with the same \(J\). Their mathematical laws are exact; subsequent finite physical sampling errors are accounted for in the BDD interface.

Define the single bounded Boolean test \(A_J\) by the specification accompanying this theorem: apply the B-v2 bridge to each input, choose one **fresh independent** uniform binary \(S\), choose independent approximate coefficient \(D_{\mathbb Z,\sigma}\) errors of per-coordinate TV at most \(\nu\), call \(\mathrm{Rec}\) once, and accept precisely when its answer equals that actual \(S\). The complete wrapper uses
\[
 K_B=\ell^2+6,\quad L_+=40(\ell^2+6)(\ell^2+4),\quad
 U_{\rm all}=kn(1+2L_+),\quad
 B_{\rm cap}=\ell^2+\lceil\log_2U_{\rm all}\rceil.
\]
All elementary uniform-integer rejection loops have at most \(B_{\rm cap}\) attempts with a fixed valid fallback. The B-v2 scalar trial count remains \(\lceil40K_B\ln(16/\nu)\rceil\), computed by its exact-ceiling procedure; \(L_+\) is only an upper bound.

The interface statements supplied with this theorem give the following full laws, including the generated \(S,E\), retained metadata, and the acceptance test:

| Implemented endpoint | Exact reference | TV bound |
|---|---|---:|
| Capped planted completion | iid \(D_{\Lambda,s}\bmod q\Lambda\), fresh exact binary \(S\), exact coefficient integer errors | \(\Delta_B+kn\nu+\eta_{\rm cap}\) |
| Capped uniform completion | the exact recovery target of item 2 | \(kn\nu+\eta_{\rm cap}\) |

In particular \(A_J\) has absolute distinguishing advantage at least \(\delta\) between the two exact finite \(F\) laws. This is a property of the fixed implemented test \(A_J\).

## Pointwise bounded decoder

Put \(w=\sqrt n\ell^2\), the **canonical** Gaussian width of the finite GP law. Choose rational \(0<\zeta\le1/8\) first, and put
\[
 h_0=\frac{\delta w}{32nk},\quad
 a_0=\frac{D^{1/n}w^{1-2/n}h_0^{2/n}}{nq},\quad
 S_0=\max(0,(n/2)\log(1/a_0)).
\]
Supply an integer \(\kappa\) satisfying
\[
 \kappa\ge\max(4S_0+4n+4\log(k+1)+20,2k,2/\delta,20\log3,\log(8n/\zeta)),
 \qquad 3w e^{-\kappa}<q/(8D).
\]
Such a choice can be made using certified upper evaluations with slack. Define, in this order,
\[
\begin{split}
 K&=\kappa+200,\quad d_H=2,\quad T_w=10^6K^3d_H^4,\\
 \Lambda_w&=10Kd_H^2\lceil\log_2(2T_w)\rceil,\quad C=K+\Lambda_w,\\
 \Lambda_c&=10000C^4,\quad M=100C\lceil\log_2(C\Lambda_c)\rceil,\\
 \Delta_c&=(100C\Lambda_c M)^{-1},\quad G=100C\Lambda_c M^2,\\
 N_c&=10000\Lambda_c^2M^2[C+\lceil\log_2(8(G+1))\rceil],\\
 Q_H&=2(T_w+1)(G+1)N_c,\quad Q_*=nQ_H,\\
 \epsilon_0&=\min(1/16,\zeta/(64kQ_*)),\quad
 a=\operatorname{Up}(\sqrt{\log(8n/\epsilon_0)/\pi})+1.
\end{split}
\]
For any certified rational \(c_x\) with \(|c_x-x|\le1/8\), \(\operatorname{Up}(x)=\lceil c_x+1/8\rceil\); fix the certified evaluation routine, so this is a deterministic integer with \(\lceil x\rceil\le\operatorname{Up}(x)\le\lceil x\rceil+1\). Choose an integer \(\chi\ge a\), and set
\[
 v_0=2\sqrt n\chi,\qquad
 d_0=\frac{\delta w}{32nkv_0}=\frac{\delta\ell^2}{64nk\chi},\qquad
 d^2=d_0^2/n.
\]
The assumptions above ensure \(d_0<q/(4D^{1/n})\). All choices precede execution and the scalar \(d_0\) is rational.

Use the C8 finite algorithm bound in the interface statements, with precisely these inputs and \(A=A_J\). It is an all-input bounded classical bit program. On **every rational** target \(T=\lambda+e\), \(\lambda\in L\), with canonical infinity norm \(\|e\|_\infty\le d_0\), it returns \(\lambda\) with probability at least \(1-p\), where
\[
 p=(n/2)e^{-\kappa}+\zeta\le17\zeta/16<1.
\]
It has at most \(Q_*\) calls to \(A_J\), hence to \(\mathrm{Rec}\), and at most \(kQ_*\) physical finite sample components, on every input, every random tape, and both orientations. The finite conditional query-simulation error is already included in \(\zeta\); the source gap \(G\) is not charged per call.

## Finite quantum registers and circuit model

Compute any ordinary rational coefficient basis \(B\) of \(L\). Put \(\Gamma=L^*\), where duality is coefficient Euclidean duality. Let rational \(0<\varepsilon\le1/16\) be supplied. Define the following parameters before compiling the decoder:
\[
\begin{split}
 b&=\prod\text{positive denominators of entries of }B,\quad A=bB,\\
 U&=1+\sum_{ij}|A_{ij}|,\quad V=1+\sum_{ij}|\operatorname{adj}(A)_{ij}|,\\
 W&=\max(4,\lceil\log_2(2^{20}n/\varepsilon)\rceil).
\end{split}
\]
Let \(H\ge2\) be the least power of two such that \((bH)^2d^2\ge2^{2W+40}n^2U^2\); set \(h_Q=\log_2H\), \(c=bH\), \(r^2=c^2d^2/(2n)\). Let \(N_g\) be the least power of two with \(N_g^2\ge r^2W^2\), and define
\[
\begin{split}
 C_u&=2nV(N_g+U+\lceil cd\rceil+1),\quad b_u=\lceil\log_2(2C_u+1)\rceil+2,\quad m=nb_u,\\
 p_g&=W+\lceil\log_2(2^{20}W)\rceil+10,\quad R_g=4096W^2,\\
 M_{\rm ph}&=4n(h_Q+2)^3,\quad
 p_{\rm ph}=W+\lceil\log_2(2^{20}M_{\rm ph})\rceil+10,\quad R_{\rm ph}=64p_{\rm ph}.
\end{split}
\]
Square-root ceilings are computed by exact rational square comparisons.

At these input widths compile the actual bounded decoder, including its dispatcher, into an AND/XOR/NOT circuit \(C_{\rm dec}\). On residue labels \(v\in\{0,\ldots,H-1\}^n\), it runs C8 on the exact rational target \(Bv/H\), checks exact lattice membership of its answer \(\lambda\), and outputs \(v-HB^{-1}\lambda\) modulo \(2^{b_u}\), with a fixed output for failure/nonmember/malformed answers. Let \(S_{\rm dec}\) be its actual gate count, \(r_{\rm dec}\) its number of fresh fair bits, and \(m\) its output length. Include all dispatch work and retained intermediate bits. The call-slot construction in the specification has exactly \(Q_*\) executable recovery blocks per forward evaluation, using valid dummy inputs on inactive branches. A classical pathwise call bound alone is not a bound for arbitrary circuit compilation.

For explicit encoding lengths use typed self-delimiting objects: an integer has a two-bit tag, sign bit, unary magnitude length \(L\ge1\) followed by a zero, and its \(L\) magnitude bits, length \(2L+4\); a rational has a distinct two-bit tag followed by its encoded numerator and denominator; a list has a distinct two-bit tag, encoded entry count, and its encoded entries. Matrices are lists of row lists. Zero uses \(L=1\) and positive sign. Count the encoding of each item in
\[
 n,B,b,A,d^2,\varepsilon,U,V,W,H,N_g,C_u,b_u,p_g,p_{\rm ph},R_g,R_{\rm ph},M_{\rm ph}
\]
and add \(n^2(h_Q+b_u+p_g+p_{\rm ph}+1)+100\) to obtain \(B_{\rm len}\). Put
\[
 A_{\rm eval}=B_{\rm len}+p_g+p_{\rm ph}+W^2+10,\quad
 E_{\rm eval}=2^{300}A_{\rm eval}^{64},\quad
 G_0=2^{12}(n+M_{\rm ph}+1)(R_g+R_{\rm ph}+1)E_{\rm eval}.
\]

## Conclusion

There is a finite quantum sampler, specified by the accompanying construction and the four mathematical interfaces, that outputs a classical point of the **same supplied** integral ideal \(J\). Its output law \(\mathcal Q_J\) satisfies
\[
 \operatorname{TV}(\mathcal Q_J,D_{J,s_J})
 \le\min\{1,\varepsilon+2\sqrt p+E_n\},\qquad
 s_J=\frac{nq}{\sqrt2d_0},
\]
where
\[
 \tau_n=2^{n/2}e^{-\pi n},\quad c_n=2^{-16n},\quad
 E_n=2\sqrt{\tau_n}+2\sqrt{2(\tau_n+c_n)}+\tau_n.
\]
Here \(s_J\) is the coefficient width; the canonical width is \(\sqrt n s_J\). All fallbacks output zero, so the sampler always outputs a point of \(J\).

The sampler uses only \(X,H,S=\operatorname{diag}(1,i),\mathrm{CNOT},\mathrm{Toffoli}\), computational-basis measurements, reset, and bounded classical feedforward. The **execution** of its actual compiled circuit, together with elementary nondecoder classical bit operations, costs at most
\[
 G_0+4S_{\rm dec}+m+2r_{\rm dec}.
\]
Working qubits plus classical working bits are at most this quantity plus \(B_{\rm len}\), and measurements at most the displayed execution bound. It uses one forward and one inverse decoder execution, hence at most \(2Q_*\) coherent executions of the supplied \(\mathrm{Rec}\) code. Full executable code is required; classical oracle service access is insufficient.

Classical setup of the ideal/decoder parameters and uniform host compilation are separately charged finite polynomial-time operations in their complete inputs and unrolling bounds. Let \(T_{\rm setup}\) denote their actual elementary bit-operation count, including any serialization; an end-to-end mixed count is \(T_{\rm setup}+G_0+4S_{\rm dec}+m+2r_{\rm dec}\). The displayed quantum execution bound is not a numerical claim about arbitrary compiler/serialization costs. F's own finite-register and transcendental preprocessing is already included in \(G_0\), so it is not charged again in \(T_{\rm setup}\). For a fixed finite-alphabet bit machine realizing the bounded **call-slot dispatcher**, of description length \(P_{\rm dec}\) and all-input step bound \(T_{\rm dec}\), one available circuit bound is
\[
 S_{\rm dec}\le2^{20}(P_{\rm dec}+T_{\rm dec}+nh_Q+m+1)^4,
 \qquad r_{\rm dec}\le T_{\rm dec}.
\]
Here \(T_{\rm dec}\) bounds the padded dispatcher, including dummy executions and all numerical evaluation, not merely the unpadded active path. Alternatively use the actual emitted circuit's counts. No uniform complexity bound for an arbitrary recovery program is asserted.

Independent repetition \(u\ge1\) times with fresh quantum preparation and decoder coins yields joint TV at most \(\min(1,u(\varepsilon+2\sqrt p+E_n))\) from \(D_{J,s_J}^{\otimes u}\), using at most \(2uQ_*\) coherent recovery executions. The conclusion concerns ordinary classical discrete Gaussian samples, not preparation of a pure coherent Gaussian state.

The eligible family is \(J\subset R\) integral, \(N(J)\le2^{\rho n}\), and \(\gcd(N(J),q)=1\), with the supplied input and recovery promises. The statement supplies no transformation from arbitrary ideal-lattice instances into this family. Coefficient/canonical normalization, inversion, conjugation, and scaling below do not assert such a transformation or a standard worst-case hardness implication.
