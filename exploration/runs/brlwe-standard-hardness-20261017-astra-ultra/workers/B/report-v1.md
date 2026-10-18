# Role B checkpoint report

2026-10-17 20:35 UTC. All new claims PROVISIONAL. Source hardness remains OPEN. No positive reduction to the required small-mask source or useful binary-RLWE target was obtained. This report closes the initial standard-RLWE public-map and auxiliary-hint investigation; it does not terminate the coordinated run.

## Discriminating results

1. **Dense elimination is an explicit failed public map.** With n+2 standard samples, the selected-unit pivot channel has an exact independent-uniform comparator and planted masks e_j−r_j e_p. At verified ordinary coefficient width n² and polynomial split q, its output is O(1/n) from uniform and far from SC-v1. See first-test-v1.md, hash d36ad12ebd95b20ef640482324aae9bce23911e9821a8546c076af7778d2eb0f. This is not a general sample-count barrier.

2. **The short-syndrome interface is sound conditional on a useful algorithm.** A multiplier-only routine producing short r_ji with a'_j−Σr_ji a_i∈I_T preserves exact comparator uniformity using designated fresh response coefficients one. Fresh ideal pads provide the declared full planted ideal law while retaining correlated errors. See short-syndrome-interface-v1.md, hash 13264630fa3ae32c4651bf44832c0e8e68137e9b630e8f3c6b4a57ff0ef435bb. A and D hand-checked the endpoints, without certifying a theorem. A now independently investigates an actual scalar LLL/Babai algorithm and reports its useful parameter range also enables full-syndrome RLWE distinguishing.

3. **A newer adaptive-hint theorem supplies a real public simulator, but its noise is too large.** LSW2025 allows the leakage map after the multipliers are known. Reverse Gaussian sampling publicly generates enlarged responses and a noisy full elimination-error hint. Subtracting that hint gives independent Gaussian masks on common ideal points, with exact actual uniform comparator and explicit statistical/sample/runtime losses. The theorem requires ζ>τ*||H||; dense H has norm at least q/4 except with exponentially small probability. Thus the masks exceed q in the verified τ*=n² regime. See semiadaptive-hints-map-v1.md, hash f9c6bc8d89ab7914fbbcee69c2e87248200fe95940d99bcad23a36b99dcec8e2. This is stronger than merely pointing out an unavailable adaptive oracle. A provisional Gaussian-rounding bridge to the established continuous standard input is included and needs independent review.

4. **Large q does not erase the approximation-factor cost.** PRS Cor7.3 permits arbitrary integer moduli but the primal spherical parameter conversion retains approximation scale Õ(n(q/τ)(nN/log(nN))^(1/4)). See large-modulus-primary-v1.md, hash acc19d8459ae2a40dc29fa1e306dc0f0a21811c6b93d5663a6389320da600f1e. Sent to A for its large-q algorithm analysis.

## Other scoped failures

programming-failures-v1.md records the missing external-response programming in forward samplers, new-matrix trapdoors and gadget columns. rejection-syndrome-v1.md bounds nonadaptive trial-list coverage by M/q^(n−d), with a separate adaptive-ideal union bound; it does not bound algebraic adaptive Syn routines. extended-hints-check-v1.md records BKMS2022's fixed-prior/noisy interface. exact-linear-hints-scope-v1.md records that WLL2024's located exact leakage is one scalar value, not a batch of full ring error hints. None is a general impossibility theorem.

## Experiment and resources

The one reserved experiment B-SYN-1 completed under 30 seconds/256MiB, used 11MiB measured maxRSS and deterministic exact rational/integer enumeration, then released its reservation. Code, command, stdout, empty stderr and measurements are preserved in experiment-record-v1.md and syndrome_controls_v1.*. It verifies finite conditional preimage coverage, exact comparator bijections, shared-mask dependence and the dense control. Finite enumeration supplies no efficient asymptotic preimage algorithm or hardness evidence. No other computation is active or reserved.

## What would change the conclusion

An actual short partial-syndrome routine with a useful parameter window not already solving the ordinary input; a different public response-programming mechanism with complete standard-hardness simulation and small residual masks; or an independently verified direct standard foundation outside these maps. Merely improving dense-matrix constants, choosing exponentially large q, replacing joint laws by marginal covariances, or granting exact challenge-dependent error hints does not close the missing edge.

All immutable notes, claims.json, references-v1.md, progress.md and resume.md are in the owned B directory. No writes outside that directory, no new agents, goals or external sessions, and no policy interruption occurred.
