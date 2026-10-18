# F-QFINITE-FV1 exact finite falsification controls

Root reservation: one foreground job, <=120 seconds, <=256 MiB address space, n<=3, auxiliary phase registers<=6 bits, <=200,000 cases. The reservation was granted before execution. No other experiment was run under it, and root subsequently released the slot.

The exact files `F-QFINITE-FV1-input.json`, `F-QFINITE-FV1.py`, `F-QFINITE-FV1-command.sh`, `F-QFINITE-FV1.stdout`, `F-QFINITE-FV1.stderr` and `F-QFINITE-FV1.resources` preserve the input, source, command, exact output and resource report. The command runs in this owned directory with CPU/address-space limits and `/usr/bin/time -v`. Source code also sets the address-space limit. There is no random seed: every calculation uses exact integers or fractions.

Result: PASS, exit code 0, 9,288 exact checks, wall time 0.18 seconds, user CPU 0.18 seconds, maximum RSS 12,288 KiB. Stderr is empty.

| Control | Exact checks |
|---|---:|
| Real phase-average filter amplitude | 67 |
| Real filter normalized successful law | 1,488 |
| Complete capped retry law | 7,440 |
| Four-phase counts nonnegative | 40 |
| Complex phase-average error | 40 |
| Uniform phase-preparation lower bound, at 6 bits | 8 |
| Normalized phase-resource fidelity bound, at 6 bits | 8 |
| Teleportation corrected success branch | 30 |
| Final exact Clifford correction | 10 |
| Controlled-phase decomposition | 40 |
| Conditional finite coset normalization | 53 |
| Complete joint coset-state reconstruction | 53 |
| Coset marginal normalization | 6 |
| Rare-branch conditional counterexample retained | 4 |
| Deleted-normalizer counterexample retained | 1 |

The finite support is [-3,3]^n, n=1,2,3, modulo scalar lattices 2Z^n and 3Z^n, with rational amplitudes 1/(1+||x||^2). These fixtures test exact normalization identities independently of transcendental Gaussian evaluation. Phase averages use all listed auxiliary widths 2 through 6 and eight rational unit-circle points. Teleportation corrections use exact symbolic phase exponents for dyadic denominators. Retry caps are 1,2,4,8,16. The retained rare-branch examples have eta=1/4,1/16,1/64,1/256, conditional bad-branch trace distance 1 and joint purification error squared 2eta.

Scope: these checks falsify several concrete bad normalization/conditioning approaches and check the finite algebra used by the proposed construction. They do not execute the full quantum algorithm, evaluate its enormous gate bound, establish the Gaussian transcendental estimates, cover arbitrary lattices, or constitute independent theorem acceptance. The pre-run failures are in `finite-quantum-failures-before-v2.md`; none was removed after obtaining PASS.
