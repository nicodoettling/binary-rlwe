# Complete proposed proof of F-QCOH v1

Status: **PROVISIONAL author proof, UNACCEPTED.** The frozen statement is `coherent-adapter-theorem-only-v1.md`. F is the author of this adapter and cannot supply its nonauthor or blind gates. This proof uses finite linear algebra and explicit reversible computation; it does not import an unexplained randomized quantum oracle.

## 1. Fix and reversibly evaluate the actual finite program

Pad all random tapes to r bits and all executions to T steps. An unused coin remains unused; a halt is followed by identity transitions. Invalid inputs or malformed outputs receive the fixed totalization convention. Therefore the entire program is a deterministic function of (x,c), with fixed finite input and output registers on every branch. Variable-length rational arithmetic, memory access, sample loops and Rec invocations are part of this bounded program, not external unitaries assumed for free.

Construct a Boolean circuit for this function by the specified bounded unrolling. A direct machine simulation keeps O(T+b+r+m+|code|) cells and unrolls every step using a linear scan; the conservative quadratic size bound in the statement suffices. Each Boolean gate can be made reversible using a constant number of NOT/CNOT/Toffoli gates and an initially zero output wire, retaining its inputs. Recording all intermediate wires gives a reversible evaluator U with

    U |x,c,0_work> = |x,c,g(x,c),A(x;c)>,

where g denotes its other work bits. Its inverse is the same gates in reverse order. Hence U and U^{-1} exist constructively with linear overhead in this chosen Boolean circuit size. The code, time bound and arithmetic routines are needed; a classical input/output service alone does not provide U^{-1}.

## 2. Clean compute, copy, and uncompute

Prepare r fresh coin qubits in |+>^r with Hadamards. Apply U, XOR its answer into the target register z, apply U^{-1} to the work/answer registers, and apply Hadamards to the coin register. The target register is not touched by U or U^{-1}. For a fixed computational coin tape c, all work bits are therefore exactly uncomputed, regardless of whether the answer was correct. The induced operation before the final Hadamards is

    2^(-r/2) sum_c |c> (U_{A_c} |psi>),

with work registers zero, where U_{A_c} is XOR by the deterministic function A(.;c). The ideal operation at that stage is

    2^(-r/2) sum_c |c> (U_f |psi>).

Their difference is zero in each promised (x,c) block where A(x;c)=f(x). In each other block its norm is at most twice the input-block norm, since it is the difference of two unitaries. The x and c labels remain orthogonal even if the input, target and reference systems are entangled. Consequently, writing mu(x) for the squared input norm at x, the squared distance is at most

    4 sum_x mu(x) Pr_c[A(x;c) != f(x)].

For support on P this is at most 4p. If off-promise mass is tau, it is at most 4[(1-tau)p+tau] <= 4(p+tau). The final Hadamards and every common postprocessing preserve or contract the relevant distance. This proves the vector bounds without selecting a good tape or exposing a measurement of the coins. Coins can remain entangled on the error component; the statement only says the entire result is close to the ideal state with all ancillas zero.

For normalized pure states the trace distance is at most their vector distance. The same conclusion for mixed inputs follows by purification, and quantum channels and measurement do not increase trace distance. Thus the stated measurement-distribution bound follows. Applying the one-replacement estimate along ideal-prefix hybrids and the triangle inequality proves the sum for several calls. At each replacement the new coin/work registers are fresh and uncorrelated with the existing state. The off-promise mass is that of the corresponding ideal-prefix query, not a distribution conditioned on all future calls succeeding.

## 3. Resource accounting

For the stipulated Boolean basis, an AND gate needs one Toffoli into its new zero wire; XOR needs two CNOTs; NOT needs a NOT on the new zero wire followed by a CNOT. Thus the evaluator and its inverse each cost at most 2S reversible gates, the answer copy costs m CNOTs, and preparing/restoring coins costs 2r Hadamards. The total is at most 4S+m+2r gates on b+r+m+S qubits, with the S work wires retaining every Boolean gate output. The designated m answer wires are among those S wires; the m extra wires are the external target register. If the bounded evaluator makes Q calls to Rec, its reversal traverses those Q executions in reverse order and reverses each of their circuits. The count is Q forward plus Q inverse Rec executions, not Q classical oracle answers. The upper bound remains valid for all answer strings and all off-promise inputs.

C8 fixes Q_* before epsilon0 and v0 and bounds every loop on all valid finite inputs. Its target encoding may be restricted to a publicly specified b-bit domain; choose its worst-case polynomial time bound at that b and pad as above. Its implemented scalar routines, global sample counter, fixed Bbits and final rational threshold are ordinary finite programs. No exact-real branch is introduced by reversible compilation. A scalar approximation need not agree bit-for-bit with an exact transcendental value; it must agree with the already frozen implemented program whose classical error was analyzed.

## 4. Hand-checkable finite regressions and rejected shortcuts

These are analytic finite models, not executed experiments. No experiment reservation was used or needed. They are proposed regression fixtures and do not constitute independent certification.

**FQ-R1, no uniformly good seed.** Let X={0,...,M-1}, choose c uniformly in X, let f(x)=0 and let A(x;c)=1 exactly if x=c. Each point has error 1/M. Every tape is wrong somewhere. Thus pointwise success does not imply the existence of a tape correct on all finite inputs, still less all rational inputs. The proof above never makes this implication.

**FQ-R2, square-root error is real.** Let one promised x have f(x)=0. Use r fair coin bits and let A(x;c)=1 only when c is all zero, so p=2^{-r}. Put the target in |->. The incorrect controlled XOR changes its phase by -1. Relative to the ideal state the coin-branch difference has norm exactly 2 sqrt(p), even after the final Hadamards. Thus the uniform coherent estimate cannot in general be replaced by an O(p) vector-norm estimate. A classical variation-distance ledger does not directly certify this step.

**FQ-R3, discard of garbage fails even at p=0.** A correct deterministic program can also copy its input to a work bit. On input |+>, discarding that copied bit produces the mixed state (|0><0|+|1><1|)/2 instead of |+><+|. The compute/copy/uncompute procedure retains and reverses all such work; it never discards it before uncomputation.

**FQ-R4, off-promise support.** If a query lies entirely outside P, the classical premise gives no restriction on the answer. The bound must allow tau=1 and be vacuous. The state-support proof uses a separate tau and does not treat the classical BDD uniqueness radius as a guarantee for every grid point.

**CP-1 scope.** The cached-prefix control has selected-hit mass 21/2000=0.0105>0.01, with the second residual incidence 21/221<0.1. It rejects multiplication of marginal stage probabilities. The present proof instead sums orthogonal finite blocks under an explicitly fresh uniform coin register and uses a norm triangle inequality for multiple replacements. It does not condition the input on future correctness, infer independence of a reused tape, or multiply selected-hit marginals. Its multi-call claim explicitly forbids silently reusing entangled coins.

## 5. What this proof does not close

It does not prove a finite primary Gaussian-state preparation algorithm, supply its exact gate-synthesis tolerances, justify querying an approximate real target, or prove a DGS sample law. Those require a separately specified quantum construction. It also does not upgrade the scope of C8, A or B. The integral ideal supplied at the start remains the same ideal throughout the proposed application.
