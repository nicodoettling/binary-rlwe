# Periodic-hardness primary endpoints, v1

Status: PROVISIONAL. Source hardness remains OPEN. First partial for the 20:50 UTC assignment, saved 2026-10-17. No experiment was run.

## Primary theorem that actually solves decision to BDD

Bruna–Regev–Song–Tang, *Continuous LWE*, [primary PDF](https://arxiv.org/pdf/2005.09595), Definitions 2.18–2.21, Theorem 3.1, Lemmas 3.3/3.5/3.8, Corollary 4.2. All Gaussians below have density proportional to exp(-pi ||x||²/s²).

The exact CLWE planted sample is (Y, (gamma <Y,W>+E) mod 1), with Y~D_(R^n,1), E~D_(R,beta), one hidden W uniform on the unit sphere shared across samples. Comparator is D_(R^n,1) times Haar(T), independently across samples. For 0<beta<1, gamma>=2 sqrt(n), gamma/beta=poly(n), the paper gives a quantum reduction from DGS at width 2 sqrt(n) eta_epsilon(L)/beta to this decision problem. Its BDD lemma needs D_(L,r_i) samples at polynomially many r_i>=r>=2(gamma/beta)eta_epsilon(L), and decodes L* within gamma/(sqrt(2)r). These are sampled inputs to a quantum iterative reduction, not arbitrary per-ideal advice.

For a BDD target T=u+w, u in L*, and a candidate z, write d=w-z. Given X~D_(L,r), V~D_(R^n,s1), E~D_(R,s2), the actual query sample is

    ((X+V)/h, (<X,T-z>+E) mod 1),   h=sqrt(r²+s1²).

Because <X,u> is integral, the second coordinate is exactly (<X,d>+E) mod1. Under the Lemma 3.5 smoothing condition

    r s1 / sqrt(||d||² (r s1/s2)² + h²) >= eta_epsilon(L),

this is within 8epsilon of CLWE with

    gamma_d=||d|| r²/h,
    beta_d²=||d||² (r s1/h)²+s2²,
    hidden direction d/||d||.

A common random Haar rotation of the first components supplies the uniform-direction law. Taking d=0 gives Gaussian first component and wrapped scalar Gaussian of width s2, not the independent uniform comparator. The actual comparator is reached at large logscale when beta_d grows past smoothing of Z. This distinction is essential: the oracle is used as a radial hidden-center oracle, not as a direct near/far classifier.

Homogeneous CLWE has density proportional to

    exp(-pi ||y||²) sum_(k in Z) exp(-pi (k-gamma<y,W>)²/beta²),

and comparator D_(R^n,1). Rejection on the scalar CLWE coordinate with Gaussian window delta changes beta to sqrt(beta²+delta²), with polynomial overhead when delta>=1/poly(n). It preserves the Gaussian envelope; it is not Haar on a known full-rank ideal quotient. Arbitrary rotations used to randomize W do not preserve the fixed ring multiplication. No reduction from these endpoints to the run's admissible ideal source has been supplied.

## Old wavy theorem: promise mismatch

Regev, *New Lattice Based Cryptographic Constructions*, [primary PDF](https://arxiv.org/pdf/cs/0309051), Section4, especially Lemmas4.6–4.8, treats Gaussian modulo L* versus uniform and then replaces the Gaussian by a single-frequency wavy distribution under a unique-short-vector promise. Ordinary g-unique lattices require every nonparallel vector to exceed the shortest by factor g>1.

For a power-two cyclotomic ideal J, any nonzero shortest x has n linearly independent rotations x,Xx,...,X^(n-1)x of identical coefficient and canonical Euclidean norms. Independence follows from irreducibility and x!=0 in the field. Hence lambda_1(J)=lambda_n(J), so the ordinary unique-lattice promise is empty in dimensions n>1. Restricting the cited theorem to full ideal lattices therefore does not establish this run's source hardness. An embedding into a nonideal lattice would need a further endpoint map back to our source.

## OHCP obligation and a live alternative

The hidden-center lemma requires: acceptance depending only on logscale+log distance to the hidden center; a nonnegligible excursion from a limiting acceptance probability; quantitative decay to that limit; and polynomial Lipschitz dependence on logscale. BRST establishes these from the entire CLWE query distribution, not from a distinguisher's success at one centered Gaussian law.

B is separately testing a genuinely different query: for Lambda=J^-1, T=q lambda+e and r in R,

    r(T-z)+G_w mod qLambda = r(e-z)+G_w mod qLambda.

C suggested elliptical integer-Gaussian r with only one embedding's width varying; the other widths remain fixed. This could make the selected complex coordinate a two-dimensional hidden center while keeping other unknown errors as fixed nuisance parameters. Required unproved steps are uniform posterior smoothing, a preserved central advantage, quantitative one-embedding convergence to Haar, and efficient sampling across all scales. This live candidate must not inherit the CLWE theorem merely by analogy.

The earlier coherent-phase counterexample remains at ../direct-coset-test-v1.md: an indicator of a set of Haar mass mu can have 1-mu decision advantage but only 4mu(1-mu) nonconstant Fourier sampling mass. No Fourier inversion step may discard this density loss.

## Access record

Arxiv primary PDFs were readable through web tools. The original PRS17 author PDF https://web.eecs.umich.edu/~cpeikert/pubs/rlwe-anyring.pdf is indexed with complete theorem excerpts, but direct web retrieval returned502 and local curl returned DNS error6. Alternate guessed author filenames also failed. These are ordinary access failures; no content-policy interruption occurred.
