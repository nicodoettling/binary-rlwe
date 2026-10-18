# B-SYN-1 resource and evidence record

Coordinator reservation: granted 2026-10-17 before execution, light slot, maximum 30 seconds and 256 MiB address space. Start/end notices sent in the collaboration channel. Current cap sidecar was read immediately before the job. No detached job, package, remote solver or other experiment was used.

Exact command from project root:

    timeout 30s python3 exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/B/syndrome_controls_v1.py > exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/B/syndrome_controls_v1.stdout.json 2> exploration/runs/brlwe-standard-hardness-20261017-astra-ultra/workers/B/syndrome_controls_v1.stderr.txt

The script sets RLIMIT_AS to 268435456 bytes before enumeration. It uses deterministic exhaustive integer/rational arithmetic; there is no random seed or floating Gaussian approximation. Floating values occur only in timing. It exited 0. Its recorded elapsed time was 0.14996027946472168 seconds and maximum RSS 11264 KiB; exec tool reported wall_time_seconds 0.063088219. Both observations are preserved without equating their measurement boundaries. Stderr is empty. Full stdout is the JSON file; it is short enough that no tail truncation is necessary.

Inputs: n=2,q=5,T={root 2}, quotient root 3; k=1,2,3; coefficient preimage alphabet {0,1}. For each quotient multiplier tuple all binary preimage tapes were enumerated. The exact success probabilities for two independent designated syndromes are 13/25, 529/625, 2993/3125. These exceed the square of average single success because both syndromes share the auxiliary matrix; the script uses the conditional image-size square before averaging. This is an explicit correlation control, not a sequential product of marginal probabilities.

For the selected full ring matrix recorded in stdout, the script checked all 625 fresh comparator pairs under 75 conditioned auxiliary-response/ideal-point tapes, and every map was a bijection. It enumerated the entire selected planted law with coefficient Bernoulli errors: 6400 equally weighted latent combinations; planted TV from uniform is 21/200. Shared auxiliary errors produce mask-pair TV 15/64 from the product of mask marginals. It also checked 12800 pointwise secret/error identities. The dense unit-pivot surrogate reproduces TV 576/625 against noiseless Base2.

This establishes only the stated finite controls and preserves the intended correlated-law bookkeeping. Exponential binary-tape enumeration is not a polynomial Syn sampler. Neither finite forward coverage nor these endpoint checks proves an asymptotic reduction or computational hardness.
