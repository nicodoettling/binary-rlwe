# C-OHCP-2 exact control report

Completed2026-10-17T21:36:06.164766Z, exit0. One reserved local job, hard wall30s and address-space256MiB; also CPU25s. External /usr/bin/time wall0.17s and peakRSS12288KiB. Empty stderr. Exhaustive deterministic inputs, no seed. Code, plan, exact shell command, original stdout/stderr, tail, exit status, and resource record are preserved in this directory.

PASS: 60 exact rational shifted-profile cases, C=200,201,256, four signed multi-peak patterns and five shifts each. Continuous weighted absolute maxima and discrete-grid maxima were calculated from all piecewise-quadratic endpoints/stationary candidates, including adjacent grid indices; no enormous grid was enumerated. Each exact grid error satisfies the displayed1/Lambda_cmp allowance, each YES pair has the v6 gap and clears the rational threshold, and reversing it gives NO. The profiles retain a positive peak after the first shift even when other peaks are negative. This checks deterministic interpolation/ordering examples; it does not sample the enormous empirical Bernoulli batches or certify their concentration theorem.

PASS:343 exhaustive two-step adaptive binary transition systems with every conditional probability pair within1/8. Exact transcript TV is at most11/64, below the valid2*(1/8) sum. The second transition uses the previous observed bit; no marginal-product independence assumption is made. This is a finite targeted regression, not a proof for arbitrary adaptive algorithms.

The code also checks exact rational grid integrality. The guided-walk numerical inequalities, Gaussian moment calculation, asymptotic runtime, and all-source-law claims are analytic obligations in v6, not independently established by this small control. No standard-hardness evidence is inferred. C-OHCP-v6 remains PROVISIONAL pending full and fresh blind review.

Artifacts SHA256:
control.py b24fab1c09e3b1da256be73404c73ba64fc69e35230d6b5e6c0c95ad80a5d8e7
plan.json 41405be86d1cd68e57cb9d43200f3224eb62e59d214f2b0edfc4edae6053ccbd
command.sh 315c9ab9caf26110100825b89bd4856ec36b58af8873a5ec6f7f6702d03b5a55
stdout.json 930779eea0bde98d8dd20e6786028a6747e05b2c210d807ec252490601dd0204
stderr.txt e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
resources.txt e934b93a61a1ba6348ca5548f1577ee84ee4878738926a904606a4c1a1dd7ddd
exit-status.json 687c241378e20faf8b6955b07cb31d057f011a92dc46ce042c56ce0b2663111e
stdout.tail.txt 31837ad8303a157fe4b4717ea5e032deb8fbe1cbb0666e8e0fee3950d0ae866d
