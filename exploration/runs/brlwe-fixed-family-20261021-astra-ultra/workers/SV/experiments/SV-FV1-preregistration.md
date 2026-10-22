# SV-FV1 preregistration

Registered before execution. Root allocated one light slot in a message received during this turn; no other SV job exists. Hypotheses: exact HNF maximum equals quotient exponent for ideals; scalar and nonzero-member rounding return prescribed inverse-ideal points under strict sufficient radii; numeric-index collision search returns a nonzero ternary ideal member; closed endpoint is not sufficient for these rounding algorithms.

Code: SV-FV1.py, deterministic inputs listed in `cases`; n in {2,4,8}, p<=17, basis obfuscation coefficients<=14. Exact SymPy integers/rationals, no random seeds, floating arithmetic, Gaussian tail truncation or posterior assertion. Largest exhaustive error bank is 2^8 and ideal matrices at most 8 by 16. Expected runtime under 60 seconds, peak RAM below 256 MiB. Absolute job limit 120 seconds, address space 512 MiB. No installation if SymPy is unavailable; that failure is retained.

Command (run in this experiments directory):

```
/usr/bin/time -v -o SV-FV1.resources.txt timeout --kill-after=5s 120s bash -c 'ulimit -v 524288; exec python3 SV-FV1.py' > SV-FV1.stdout.json 2> SV-FV1.stderr.txt
```

Exit status will be retained separately, and stdout/stderr/resource files preserved whether success or failure. This is finite structural regression evidence, not asymptotic proof. The code hash is recorded before launch in SV-FV1.code.sha256.
