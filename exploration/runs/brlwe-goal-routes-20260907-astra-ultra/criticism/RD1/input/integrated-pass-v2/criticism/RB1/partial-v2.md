# Blind partial report RB1 — 2026-09-07 22:08 UTC

The independent argument now closes the finite inequality (F), the implementation inequality (I), and the stated asymptotic implication, conditional on the explicitly supplied least-prime statement and computational source assumption. No candidate proof or historical objection has been read. The full report is being written before freezing and hashing.

Exact finite controls in `finite-controls-v1.py` passed for all 712 ideal-element tuples across n=2, q=5, m=1,2, d=0,1,2, using a finite symmetric unimodal noise law to isolate the guessing/leakage lemma. All-zero tuples attain the exact baseline 9/16; no inversion premise is used. Numerical Gaussian constants and residual-theta envelopes passed separate checks. Full unedited output is `finite-controls-v1.results.json`; runtime was 0.017 seconds under a 120-second timeout.

The completed normalization is p(e)=r(e)h(e)/E_r[h], with h(e) in [1-Delta_N,1+Delta_N]. This gives TV <= Delta_N/(1-Delta_N), capped at one. The approximation is for the entire mn-dimensional error vector conditional on all F values, so it preserves the target's iid error requirement up to the claimed joint TV term.

For implementation, the exact uniform-branch success is epsilon_m. Replacing the local independent sampler changes each branch by at most xi_alg, and replacing the planted source changes only that branch by xi_source. This gives xi_source+2xi_alg. Full witness/transcript target TV gives the additional xi_target. A fixed bounded-support dyadic Gaussian sampler with cutoff O(n^2 ell^3) and O(n^2) bits achieves negligible TV in deterministic polynomial worst-case time.

For asymptotics, q^d <= 2^(n/4) eventually, D_ell(0)<=1/ell, and the entropy term is bounded by ((3/4)2^(1/4))^n for ell>=2. Both eta_N and delta_F,m are exp(-Omega((log n)^2)) up to polynomial factors. The fixed prime bound gives q<=n^16 and q/sigma_m>=n eventually. No parameter or sampling accuracy needs to depend on Q or its success exponent.
