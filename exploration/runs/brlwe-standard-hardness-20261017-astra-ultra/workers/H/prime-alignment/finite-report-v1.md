# H finite controls: original artifacts and exact scope

Both reserved jobs completed successfully. Their code, inputs, exact commands, original stdout/stderr and OS resource reports remain separate immutable files. No job remains active and no further reservation is held.

| Reservation | Script | Exit | OS wall time | OS peak RSS | Exhaustive scope |
|---|---|---:|---:|---:|---|
| H-ALIGN-FV1 | finite-controls-v1.py | 0 | 0.48s | 12,288KiB | 8 laws;143,144 ordered point pairs;296 exact packing counts |
| H-REL-FV2 | relation-controls-v1.py | 0 | 3.94s | 15,360KiB | Same8 laws and143,144 ordered pairs; exact2D relation and complete output laws |

Both stderr files are empty. Each job was foreground-only with timeout120s and an internal256MiB address-space cap. Every probability/inequality assertion uses exact integers or Python Fractions. Wall/RSS metadata use ordinary OS measurements; the in-script RSS for the second job was13,312KiB while /usr/bin/time reported15,360KiB after the complete JSON serialization. The more conservative final OS peak is reported above. No random seed was used.

The finite laws use coefficient points in[-6,6]^2 belonging to F=Z[i] or(1+i), prime ideals(2+i) or(3+2i), and weights t^(a^2+b^2) for t=1/2 or1/4. These are separately normalized restrictions of Gaussian weights, with corresponding s^2=pi/log(1/t). They are NOT full infinite Gaussian laws, and their widths are NOT the delivered wide s_J. No truncation-tail inference is used or claimed.

The alignment job preserved the literal finite denominator, the zero-excluded numerator, the zero-conditioned denominator and the complete residue probability vector. It checked all two-draw selected-success and collision masses. Later selection can increase one-output success above the original one-draw mass; conditioning on selecting an alignment makes its conditional success exactly one. The full original attempt union bound remains valid. Deterministic history-by-history maximization of the second width checks every two-kernel adaptive policy without enumerating all policy encodings.

The packing controls count ALL ideal points in each ball of squared radius0,...,36, because those balls lie inside the declared box. They compare the exact n=2 disjoint-ball inequality by rational squaring, using lambda^2=N(FI). They check only those finite radii and ideals. They do not prove general lattice packing or any infinite theta bound.

CP-1 reproduces vk normalizer10/11, posterior masses21/2000,1/20,879/1000, selected probability21/2000>1/100 and later incidence21/221<1/10. The inflated first incidence221/2000 exceeds121/2000. The old selected-stage product is explicitly rejected, with support restriction and renormalization retained.

The relation job computes exact Gauss reduction in the two-dimensional integer congruence kernel. It checks the coefficient norm bound using ||c||^4<=2h^2, the full kernel determinant h, membership of each returned ring output, Cauchy-Schwarz transfer, and nonzero output after rank screening. It also preserves the positive zero-image mass when screening is omitted. Its actual source index law is h=1 with probability pi(0)^2 and h=M otherwise; the uniform-residue comparator has h=1 with probability1/M^2. Thus the code does not pretend the index is always M.

Every comparator residue has positive finite conditional-lift support in these eight cases, as explicitly checked. Empty support would have stopped the run as a failed control rather than silently dividing by zero, conditioning, or resampling. The complete retained-vector source/comparator TV equals the TV of their residue marginals, and the complete output distributions including FAIL obey TV contraction. Both output probability tables are preserved in relation-stdout-v1.json, not merely their TV summaries.

These controls support the normalizer, selection and implementation bookkeeping in the author packet. They do not certify the full Gaussian rank bound, ideal algebra, asymptotic parameter intersection, primary LLL import or any standard-hardness edge. Exact independent proof/source/fresh-blind gates remain separate.
