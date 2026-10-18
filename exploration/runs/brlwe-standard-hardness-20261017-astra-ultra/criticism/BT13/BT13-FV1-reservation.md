# BT13-FV1 reservation and exact input

Coordinator authorized one foreground job, at most 120 seconds, 512 MiB address space, n <= 8 and at most 1,000,000 finite cases. No other experiment is authorized.

This deterministic Python-standard-library job checks exact rational guided-step inequalities, the final rational threshold at binary precision boundaries, conservative integer parameter inequalities and the fixed normalization budget. It also numerically inspects small scalar Gaussian normalizers. Dimensions: n in {2,4,8}; geometric dimension 2. There is no random seed because no random numbers are generated. Rational input numerators/denominators have at most 220 bits; generated loop-bound integers are expected below 1,024 bits. Fewer than 200,000 cases and below 64 MiB RSS are expected. Arithmetic output is a falsification aid, not asymptotic or hardness certification. No files outside BT13 are read by the experiment apart from the Python interpreter/standard library and resource-monitor binaries.

Code: BT13-FV1.py. Command: bash BT13-FV1-command.sh. Original stdout: BT13-FV1.stdout. Original stderr: BT13-FV1.stderr. Resource output: BT13-FV1.resources. Time cap is enforced by timeout; address space by ulimit -v 524288. The full finite input is encoded as the explicit arrays/ranges in the code.
