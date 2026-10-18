# Mathematical interfaces for the same-ideal composition

This file contains statements and definitions of the mathematical interfaces used in the companion theorem. File paths below are relative to the run root exploration/runs/brlwe-standard-hardness-20261017-astra-ultra. SHA256 identifies an exact statement/specification. The four interface results are the dependencies of the composition theorem.

## I. Fractional-source actual-secret bound

Use the ring and coefficient Gaussian convention of the companion theorem. For a fixed integral ideal \(J\), \(D=N(J)\), assume \(\gcd(D,q)=1\), \(D\le D_{\max}\), and the existence of a row basis of \(J\) of operator norm at most \(\tau_2\). This is an existence assumption only. Let \(t,s,L_A,\sigma>0\) satisfy \(\sigma\ge2ts\sqrt{kn}L_A\).

For independent \(a_i\leftarrow D_{J^{-1},s}\), expose only their classes in \(J^{-1}/qJ^{-1}\), identified with \(R/qR\) by
\[
 v/D\longmapsto vD^{-1}\pmod q.
\]
Complete these multipliers with independent uniform coefficient-binary \(S\) and independent coefficient integer \(D_{\mathbb Z,\sigma}\) errors, call a recovery algorithm, and test equality to the actual \(S\). Its planted acceptance is at most
\[
 \delta_{\rm tail}+\beta_{\rm exact}+\eta,\quad
 \delta_{\rm tail}=\min(1,4kn e^{-\pi L_A^2}),\quad
 \beta_{\rm exact}=\min(1,D_{\max}[(1+D_{\mathbb Z,t}(0))/2]^n),
\]
where \(\theta=2\sum_{j\ge1}e^{-\pi(3t^2/(4\tau_2^2))j^2}\), \(\Delta=(1+\theta)^n-1\), and \(\eta=\min(1,\Delta/(1-\Delta))\) if \(\Delta<1\), otherwise \(1\). The uniform-multiplier completion is exactly the recovery target, including its secret in the acceptance experiment. Therefore recovery success \(\epsilon_{\rm rec}\) yields absolute advantage at least \(\epsilon_{\rm rec}-\delta_{\rm tail}-\beta_{\rm exact}-\eta\).

Every such integral ideal has some row basis with operator norm at most \(n^2D^{1/n}\). Neither this basis nor any completion proof variable is input to the executable wrapper.

Exact statement: workers/A/fractional-composition/theorem-only-v1.md, SHA256 5c471744bb04c8149b0d539eaa26e1544d0ba8097b0d68ea019cabb74461b485. Notation: coordinator/a-frac-definitions-v1.md, SHA256 29ed77d3b83a8495396b10b4bef7933e36039c397a5616aa46c77b363017515b. The planted acceptance formulation is the analytic actual-secret statement underlying that interface; only the displayed advantage inequality is required by the composition.

## II. Finite GP bridge and complete cap

For any supplied ordinary integral \(J\), \(\gcd(D,q)=1\), \(P\ge1\), let \(F=(DP)^{-1}\mathbb Z^n/qJ^{-1}\) with fixed HNF/SNF representatives. Given rational \(w_B,r_B>0\), \(0<\epsilon_B,\nu\le1/4\), and
\[
 r_B\ge\max(1,\sqrt{\log(8n/\epsilon_B)/\pi}),\qquad s^2=w_B^2+r_B^2,
\]
there is the following public map. Choose \(u\) uniformly in \(J^{-1}/\mathbb Z^n\), represented in \([-1/2,1/2)^n\). At input \(y\), independently generate an approximate \(D_{\mathbb Z,r_B,y_i-u_i}\) in every coordinate and output \(u+E\bmod qJ^{-1}\). Its fixed scalar kernel is integer-translation-equivariant.

For \(k\) independent inputs \(Q_h(G_{w_B})\bmod qJ^{-1}\), the full joint output differs in TV by at most
\[
 \Delta_B=2k\epsilon_B/(1-\epsilon_B)+2\pi kn/(Pr_B)+kn\nu
\]
from independent \(D_{J^{-1},s}\bmod qJ^{-1}\). For iid uniform \(F\) input, with exact uniform quotient sampling, its full output is exactly iid uniform \(R/qR\). These statements retain the same metadata.

The scalar kernel at rational center \(c=m+f\), \(m=\lfloor c\rfloor\), \(0\le f<1\), width \(r\), is:
\[
 K_B=\lceil\log_2(64/\nu)\rceil,\quad N_B=\lceil rK_B\rceil+1,\quad
 p_B=\lceil\log_2(1024(K_B+1)/\nu)\rceil,\quad L_B=\lceil40K_B\ln(16/\nu)\rceil.
\]
At most \(L_B\) times choose uniform \(j\in[-N_B,N_B]\), compute a fixed dyadic \(v_j\in[0,1]\) with denominator \(2^{p_B}\) and error at most \(2^{-p_B}\) from \(e^{-\pi(j-f)^2/r^2}\), and accept with exactly probability \(v_j\). Output \(m+j\) on acceptance and \(m\) after all failures. Its distance from \(D_{\mathbb Z,r,c}\) is at most \(\nu\). The exact natural-log ceiling is computable in polynomial bit complexity in the full rational encodings; it is not replaced by an unbounded equality test or a different kernel.

If at most \(U_{\rm all}\) elementary uniform-integer draws occur in a complete wrapper, capping each binary rejection loop at \(B_{\rm cap}\) trials with valid fallback changes its full output law, for every input, by at most \(U_{\rm all}2^{-B_{\rm cap}}\). This applies separately in both worlds. Using the same scalar kernel at width \(\sigma\), center zero, for the \(kn\) target error coefficients adds at most \(kn\nu\) to each endpoint. The parameters in the companion theorem give \(U_{\rm all}=kn(1+2L_+)\) and \(U_{\rm all}2^{-B_{\rm cap}}\le\eta_{\rm cap}\). Consequently the two endpoint bounds are exactly the table in that theorem.

These are finite all-input maps; the implemented test's source advantage is established once, not used as a per-call simulation error. Runtime is polynomial in dimension and complete finite encodings, including scalar evaluation and the recovery program's supplied bound.

Exact statements: workers/B/ideal-denominator/gaussian-periodic-theorem-v2.md, SHA256 be7f05d67fc8f2b24fc6b93321c95005f4d7f6e24bab513b2cbaf35c82aeaad7; gaussian-periodic-bounded-wrapper-v1.md in that directory, SHA256 335f4a176331df262eda5c775a7d565e3c47fee6413d714957741c81b6087521; gaussian-periodic-v2-ceiling-addendum-v1.md, SHA256 17044d83881bee69c3182ed0cdaaccf91687d4a1e173618e837350fe1ebb2e47.

## III. Finite canonical GP decision to pointwise ideal BDD

For \(L=qJ^{-1}\), \(F=(DP)^{-1}\mathbb Z^n/L\), let a bounded finite algorithm \(A_J\) have absolute advantage at least \(\delta>0\) between iid \(Q_h(G_{w/\sqrt n})\bmod L\) and iid uniform \(F\), with the same \(J\). Let all the parameters \(\zeta,\kappa,Q_*,\epsilon_0,a,v_0,d_0\) be as in the companion theorem, including all its displayed lower bounds and \(d_0<q/(4D^{1/n})\).

The finite algorithm specified below returns \(\lambda\) on every rational input \(T=\lambda+e\), \(\lambda\in L\), \(\|e\|_{\infty,\rm canonical}\le d_0\), with probability at least \(1-(n/2)e^{-\kappa}-\zeta\). It terminates within a constructible bound on every target and every tape, even off the promise, uses at most \(Q_*\) calls to the actual \(A_J\), and generates at most \(kQ_*\) physical sample components. Its time is polynomial in complete input encodings, \(n,k,\log P,1/\delta,\log(1/\zeta),\kappa\), the actual certified evaluation costs, and the runtime of \(A_J\).

For each conjugate pair \(j\), its analysis center is \(2+e_j/d_0\), scale 3. The physical query at \(z,t\) is
\[
 Q_h(r(T-g(z))+G_{w/\sqrt n})\bmod L,
\]
where \(r\in R\) is an exact integral multiplier, with elliptical canonical Gaussian widths \(v_0e^t\) in pair \(j\) and \(v_0\) elsewhere, and the canonical coordinates of \(g\) are \(g_j=d_0(z-2)\), \(g_i=0\) elsewhere. The implemented multiplier and physical-query sampler uses the finite precision and capped scalar routines of the bound specification. The algorithm runs all pairs under each global orientation \(A_J\) and \(1-A_J\), with the exact comparison/walk loop counts of the companion theorem, reconstructs at most two candidates, and uses exact membership and the specified rational distance threshold.

The finite physical algorithm's total additional error is at most \(\zeta\). It includes the fixed posterior/multiplier comparison allowance \(2kQ_*\epsilon_0/(1-\epsilon_0)<\zeta/16\), a single global sample counter \(c\ge1\) across both orientations with conditional budget \(\zeta/[16(c+1)^2]\), and finite walk-position error below \(\zeta/16\); all remaining finite numerical allowances are within the stated \(\zeta\). The counter budgets are conditioned only on the past. The physical multiplier kernel is compared to a continuous proxy; only that proxy's endpoint is Haar. There is no assumption of an exactly uniform physical endpoint.

Exact statement: coordinator/c8-repair/multiplier-ohcp-theorem-v8.md, SHA256 857a62e9f4a937a80e5cb3b115c8b132abf122c16665d29b39dcb62bde86fe0a. Its complete finite algorithm definition is coordinator/c8-repair/multiplier-ohcp-algorithm-v2.md, SHA256 4361c90a7fa7cfe25d0ab3e8cd5c5333fb474cf1fb764375e10c29fca5102735. The latter's precise finite sampler, comparison score, walk initialization/update, and rational final threshold are incorporated as definitions of this interface; changing them changes the interface.

## IV. Finite coefficient BDD to ordinary dual DGS

Let \(B\) be any nonsingular rational basis, \(L=B\mathbb Z^n\), \(\Gamma=L^*\), and \(d>0\) with supplied rational square, \(\lambda_1(L)>4d\). Let an all-input bounded classical randomized program recover the unique closest lattice vector on every rational target within coefficient Euclidean distance \(d\), with probability at least \(1-p\), \(0\le p\le1\). Its full finite code, randomness bound, and conversion to integer \(B\)-coordinates are supplied. Set all registers, caps, precisions, and encoding costs exactly as in the companion theorem. The actual compiled circuit includes any call-slot dispatcher.

There is a finite sampler on \(\Gamma\) at coefficient width \(\sqrt n/(\sqrt2d)\), with TV at most
\[
 \min(1,\varepsilon+2\sqrt p+
 2\sqrt{\tau_n}+2\sqrt{2(\tau_n+2^{-16n})}+\tau_n),\qquad
 \tau_n=2^{n/2}e^{-\pi n}.
\]
It uses one clean coherent decoder evaluation, one forward and one inverse execution of the actual Boolean circuit, costing at most \(4S_{\rm dec}+m+2r_{\rm dec}\) gates. Its nondecoder allowance is \(G_0\), with the gate set, measurement, memory and ordinary-bit-operation bounds in the companion theorem. The input off-promise tail is charged in the displayed \(\tau_n\) terms, not again inside \(p\). The guarantee holds for the complete measured law, including retry failures, measured coset labels, entangled adaptive phase corrections, and retained work. No common random tape that is good for all targets is assumed.

Exact statement: workers/F/finite-quantum-integration/finite-quantum-theorem-only-v2.md, SHA256 ce7f5992b071f7d82e5e034a7dc323f69a85d0f4969afa0530603527bc7338e2. Complete finite algorithm definition: workers/F/finite-quantum-integration/finite-quantum-algorithm-v2.md, SHA256 1ea3e1ab1c297773d591a3bd983ff278f31cdafcd459acd29076a3867ede2545. Its preparation and phase-resource routines are incorporated as definitions, with the explicit typed binary encoding in the companion theorem instantiating its required full encodings.
