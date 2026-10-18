# RT2-WEIGHTED-FV1 execution receipt

Root reservation was granted before execution and explicitly released after the run. The live launcher manifest and cap were read administratively immediately before execution. The state was running with discovery stop 2026-10-18T01:36:14.695009Z and hard deadline 2026-10-18T02:06:14.695009Z. This foreground run finished before 01:20 UTC. No detached jobs, external services, installations, subagents, or goals were used.

Exactly one execution: `timeout 30s python3 -B finite-control-v1.py`, measured with `/usr/bin/time -v`. Python installed an address-space bound of 268,435,456 bytes. The code checked the actual support bound before enumerating its weighted pairs. Exit 0; 0.04 seconds elapsed; 13,312 KiB maximum RSS; stderr empty. All source, configuration, command, full stdout and resource files are retained beside this receipt. No rerun was performed.

The experiment checks 625 ambient multiplier vectors and 1,152 exact weighted pairs, from 64 valid nonzero complementary multipliers, nine sample points, and two rational weight schedules. It stores every fixed-multiplier output law and zero probability. Twenty-four multipliers per schedule have a nonzero-input/zero-output branch. It additionally preserves the sample-dependent multiplier, TV-moment, marginal-versus-joint, and CP-1 negative controls. Full results and exact probabilities are in `finite-stdout-v1.json`.

The control is intentionally finite. It does not certify the infinite Gaussian covariance or subspace theorem, an implemented source width, an efficient complementary multiplier algorithm, or computational hardness. Those remain analytic proofs or separate computational dependencies as identified in the reports.
