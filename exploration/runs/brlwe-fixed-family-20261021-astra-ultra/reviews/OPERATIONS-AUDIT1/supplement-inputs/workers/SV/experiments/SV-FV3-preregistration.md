# SV-FV3 preregistration

Registered before execution under root's fresh light-slot allocation. Hypotheses: e's2-part<=2 in the eligible family; J+mR removes exactly that part; aJ_o⊂J; full stabilizer tests and signed-orbit basis are exact; the SNF-computed image index satisfies d_H^|H|=N(J_o); binary collisions yield actual members and exact decoding. Negative control: skipping ramified-part removal at J=P_2 in degree4 gives actual contraction index2, whose fourth power16 differs from norm2.

Code SV-FV3.py lists eleven deterministic ordinary-basis cases, n<=32, including2-primary powers, mixed2/odd ideals, odd prime powers and products of distinct characteristics. Maximum product-generator matrix32 by1024. Nominal contraction index at most28033 in the composite test; Gray-code keys use exact bounded integer arithmetic, not symbolic matrix multiplication per candidate. SymPy is already installed. No random seed, floating arithmetic, probability or Gaussian truncation.

Expected runtime<90s, peak RAM<256MiB; enforced timeout120s and512MiB address-space cap. Exact command:

```
/usr/bin/time -v -o SV-FV3.resources.txt timeout --kill-after=5s 120s bash -c 'ulimit -v 524288; exec python3 SV-FV3.py' > SV-FV3.stdout.json 2> SV-FV3.stderr.txt
```

Code hash saved before launch. Full stdout/stderr/resource/exit evidence preserved on every outcome. This is finite falsification control, not proof or review certification.
