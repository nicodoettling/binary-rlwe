# SV-FV4 preregistration (separate repair after SV-FV3 timeout)

SV-FV3 is preserved unchanged with exit124,120.03s,maxRSS473088KiB and empty mathematical output. No assertion passed or failed was observed. Its redundant n by n² ideal-product generation caused a suspected HNF resource blowup during case construction; this cause is an inference, not profiled fact.

New experiment keeps the same hypotheses and exact methods but uses compact ideal generators: P²=(p²,p g,g²), PQ=(pq,p h,q g,g h), and the principal matrix for(1-X)^a. It omits the degree32 prime-power case, so max dimension16 and max generator matrix16 by64. Ten deterministic cases, maximum contraction index28033, all exact. It prints every case name before processing, preserving progress if interrupted.

Root slot reuse requested after FV3 completed; launch only on allocation. Expected runtime<60s, memory<256MiB, enforced120s and512MiB address space. Code hash saved before launch. Command:

```
/usr/bin/time -v -o SV-FV4.resources.txt timeout --kill-after=5s 120s bash -c 'ulimit -v 524288; exec python3 SV-FV4.py' > SV-FV4.stdout.txt 2> SV-FV4.stderr.txt
```

All output/exit/resource evidence retained. This version changes finite test construction and coverage, not frozen theorem or proof bytes. No Gaussian tails or probability lemma is involved.
