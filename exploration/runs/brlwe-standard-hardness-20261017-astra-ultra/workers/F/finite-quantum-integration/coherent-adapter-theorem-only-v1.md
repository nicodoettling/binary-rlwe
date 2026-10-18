# F-QCOH v1: bounded randomized programs as approximate clean quantum oracles

Status: **PROVISIONAL, NEW THEOREM, UNACCEPTED.** This is F's proposed finite adapter, not a verdict on F's own theorem. It requires nonauthor full-proof, source/parameter, regression and fresh-blind gates. It does not assume or prove the correctness of C8 or a quantum Gaussian state preparation routine. The separate complete proof is `coherent-adapter-proof-v1.md`.

Fix a finite set X of b-bit valid inputs, a subset P of promised inputs, and a function f:P->{0,1}^m. Let A be one explicitly given classical randomized program. A terminates on every b-bit input after at most T steps, uses at most r fair random bits, and returns an m-bit answer after a fixed padding/totalization convention. Fix its code and its deterministic implementation of every numerical operation. On every x in P assume

    Pr_c[A(x;c)=f(x)] >= 1-p,

where c is uniform in {0,1}^r. There is no success condition off P. The given bounds T,r,m,b and the code must suffice to construct a finite Boolean circuit for A; an unspecified classical answer service is not such a code description.

There is a finite quantum circuit V acting on an input register x, an arbitrary m-bit target register z, and fresh ancillary registers initially zero, with the following property. For every normalized input state, including a reference system, supported on promised x,

    || V(|psi> |0_anc>) - (U_f |psi>) |0_anc> ||_2 <= 2 sqrt(p),

where U_f maps |x,z> to |x,z XOR f(x)>. No single random tape correct simultaneously on every x is assumed. The input register is retained throughout.

If the squared norm on x outside P is at most tau, extend f arbitrarily there. Then the same bound is at most 2 sqrt(p+tau). This is a vector-norm bound for arbitrary input/reference entanglement with fresh ancillas, not a classical total-variation bound. After any common quantum postprocessing and measurement, the output statistical distance is at most the displayed bound. For a sequence of s replacements, fresh ancillas at each replacement and a bound tau_j on each ideal query state give the sum 2 sum_j sqrt(p_j+tau_j), by a hybrid argument; no future-success conditioning is permitted.

More explicitly, let S be the number of gates in an explicitly constructed acyclic Boolean circuit evaluating A(x;c), using fan-in-two AND/XOR and fan-in-one NOT, with one new output wire per gate and its m designated output wires included. Its all-input time cap and padding are included. A reversible compute/copy/uncompute construction uses at most 4S+m+2r elementary NOT/CNOT/Toffoli/Hadamard gates and at most b+r+m+S qubits, excluding any untouched external reference. For a standard bounded multitape machine a conservative unrolling gives S=O((T+b+r+m+|code|)^2); the exact chosen unrolling determines S. The circuit evaluates A once forward and once backward. If A contains at most Q calls to another bounded program Rec, this requires at most Q forward and Q inverse coherent executions of Rec's circuit. These are calls to an available circuit, not classical sampling-oracle queries.

For C8 instantiated with a fixed finite GP distinguisher and a fixed bound on the BDD target encoding, put

    p=(n/2) exp(-kappa)+zeta,  Q=Q_*.

The C8 conclusion, if accepted, supplies the pointwise premise on its rational promised targets. Mapping a failure symbol to a fixed padded bit string makes the program total. All classical branches, finite random choices, approximate scalar computations and verifier operations are compiled reversibly. This adapter costs at most 2 Q_* coherent Rec evaluations, because the fixed GP wrapper contains one Rec execution. It does not by itself prepare the finite quantum query state or establish an ordinary-DGS output law.

In particular a negligible p yields negligible coherent error; a merely constant or inverse-polynomial p cannot be relabeled negligible. A proposed final DGS error budget must separately pay for the primary quantum state preparation, truncation/aliasing, gate approximation and any off-promise query mass.
