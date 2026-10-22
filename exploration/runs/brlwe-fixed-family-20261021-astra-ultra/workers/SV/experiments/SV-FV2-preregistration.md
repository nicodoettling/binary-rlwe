# SV-FV2 preregistration

Registered before execution. Root allocated one light slot; root may use the second slot for a separate CRT control. Hypothesis: signed Frobenius cycles give exact fixed rank n/ord_(2n)(p), negative-sign cycles vanish, all fixed vectors have prime-subfield residues, and O(p) binary sums yield a nonzero ternary ideal member supporting exact direct decoding.

Deterministic nine input pairs are listed in SV-FV2.py, n<=32,p<=97. Prime ideals are formed from one exact irreducible factor of X^n+1 modulo p, then represented by ordinary HNF and an obscuring unimodular basis change. All arithmetic is exact integer/rational or finite-field polynomial arithmetic. No random seed, floating precision or tail approximation. Maximum matrix32 by64, at most98 binary sums per case. Expected runtime<60s and memory<256MiB; enforced120s wall and512MiB address space. The script imports installed SymPy only.

Command:

```
/usr/bin/time -v -o SV-FV2.resources.txt timeout --kill-after=5s 120s bash -c 'ulimit -v 524288; exec python3 SV-FV2.py' > SV-FV2.stdout.json 2> SV-FV2.stderr.txt
```

Code hash recorded before launch; stdout/stderr/exit/resource records retained regardless of outcome. This finite test is not a proof of the asymptotic family theorem.
