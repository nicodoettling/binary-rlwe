# Finite conditional parameter instance

This instantiates the supplied-parameter theorem. It is a compatibility certificate conditional on the stated recovery algorithm; it is not a claim of security or of a standard-family reduction.

The frozen source is coordinator/quantum-integration/effective-parameter-v3/certificate.md, SHA256 bdc9ea7aa9ba63f59a2ed52a16ee1cdbe31334cee469364c74a1cf39fd98611d, together with its adjacent control.py, input.json, stdout.json and freeze-receipt.json. Code SHA256 is 6f09e6c5218075cb41fef696906b0a30cd73d5fb913228588ba5bd39a648f947; stdout SHA256 is 464c6a248dcc27479d37a7c379e628ea727ff12a16a8bf1a7cf72506cdf9c487. No new experiment was run for this author packet.

Take \(n=k=16,\rho=1/2,q=2^{64}-2^{32}+1\), and \(J=(97,X-19)\). The exact residues \(19^2,19^4,19^8,19^{16}\bmod97\) are \(70,50,75,96\), so \(N(J)=97\le256\). The supplied modulus is prime, split, coprime to 97, and at least \(n\sigma\). Its elementary prime certificate is \(7^{q-1}\equiv1\pmod q\), \(7^{(q-1)/2}\equiv-1\pmod q\). For every prime \(p\mid q\), the order of 7 modulo \(p\) then has 2-adic valuation 32, so \(p\ge2^{32}+1>\sqrt q\). This rules out composite \(q\).

The recovery premise is bounded code with actual-secret success at least \(1/16\) for this fixed \((q,J)\) and exact target law. Set
\[
 \ell=9,\quad t_A=4608,\quad\tau_2=512,\quad
 w_B=r_B=81,\quad s=81\sqrt2,\quad\sigma=214990848,\quad
 P=2^{162},\quad\delta=1/32.
\]
Use \(\epsilon_B=\nu=\eta_{\rm cap}=2^{-81}\). Bounds \(\delta_{\rm tail}\le1024\cdot2^{-243}\), \(\beta\le2^{-8}(288/287)\), and \(\theta_A<2^{-180}\), with \(2\pi<8\), give the strict gap required by (G), including all three \(kn\nu\) and both cap terms.

Choose \(\zeta=2^{-74}\), \(\kappa=4096\). The C8 schedule gives \(w=324\), \(h_0=81/65536\), \(a_0>2^{-68}\), \(S_0<544\), and a 600-bit integer \(Q_*\). A certified inequality \(\ln(8n/\epsilon_0)<691\) gives \(a\le128\) for the specified Up rule. Choose \(\chi=128\), so \(v_0=1024\) and
\[
 d_0=81/2^{26},\qquad d^2=6561/2^{56}.
\]
This is the theorem's allowed choice \(\chi\ge a\), with no change to the original Up definition.

For \(\varepsilon=2^{-40}\), the ordinary basis in the frozen certificate and the theorem's typed encoding yield:

| Parameter | Value |
|---|---:|
| \(W\) | 64 |
| \(\log_2H\) | 179 |
| \(\log_2N_g\) | 267 |
| \(b_u,m\) | 2823, 45168 |
| \(p_g,p_{\rm ph}\) | 100, 123 |
| \(R_g,R_{\rm ph}\) | 16777216, 7872 |
| \(M_{\rm ph}\) | 379503424 |
| \(B_{\rm len},A_{\rm eval}\) | 859028, 863357 |
| Binary length of \(G_0\) | 1627 |

The coefficient output width remains exactly \(16q/(\sqrt2d_0)\); it is not a normalized smoothing ratio. The finite TV bound is below
\[
 3145745/549755813888<2^{-17}.
\]
The bound on full circuit execution is still \(G_0+4S_{\rm dec}+m+2r_{\rm dec}\), dependent on the actual supplied decoder/recovery code. No such large circuit, BDD walk, recovery algorithm, or lattice Gaussian sampler was executed by the parameter certificate. This isolated small-dimension witness does not establish an asymptotic family hardness statement.
