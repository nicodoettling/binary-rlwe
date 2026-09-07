# N01-PROVENANCE-v1 — Gaussian diagnostic correction accounting

Administrative completion of the N01 experiment record. No calculation or experiment was rerun for this assignment. The frozen mathematical review and W1 proof remain unchanged. The follow-up assignment is preserved in `provenance-assignment.md`.

The first Gaussian diagnostic **did not fail**: its process returned exit code 0 and its stdout reported `all_assertions_passed: true`. The later correction fixed a missing likelihood-ratio factor in one conservative **truncation-bound annotation**. It did not change the Gaussian probabilities, raw moments, entropy calculations, likelihood-ratio checks, wrapping checks, or assertion results.

## Exact correction

In `gaussian_controls.py`, the local variables are `sigma2 = sigma^2`, `R = Rseq`, and `pbox` is the upper bound on the mass outside the joint enumeration box. The first invocation used:

```python
moment_tail_bound=2*mp.sqrt(R)*sigma2/mp.pi*mp.sqrt(pbox)+pbox*sigma2/(2*mp.pi)/(1-pbox)
```

The corrected source, now line 108, uses:

```python
moment_tail_bound=2*mp.sqrt(R)*sigma2/mp.pi*mp.sqrt(pbox)+pbox*R*sigma2/(2*mp.pi)/(1-pbox)
```

The exact formula increase is

    pbox * (Rseq - 1) * sigma^2 / [2 pi (1-pbox)].

The second term accounts for renormalizing the truncated H_seq law. The available bound on the full H_seq absolute product moment includes domination by Rseq, namely `E_Hseq |H_i H_j| <= Rseq sigma^2/(2pi)`. The first annotation had used the corresponding D_B bound without that domination factor. The omitted-tail Cauchy–Schwarz term already had its square-root Rseq factor and was unchanged.

The variable `moment_tail_bound` is written to the JSON field `joint_moment_truncation_bound` and printed in the stdout summary. It does not feed any assertion or the computed Gaussian moments. Therefore the initial all-assertions-passed result was not reversed by this correction. Both invocations' retained stdout summaries display the same 65-significant-digit truncation-bound strings; this statement is a comparison of the recorded transcripts, not a new numerical calculation. It does not assert that the two unrounded symbolic bounds are equal.

The actual correction command in the original turn was:

```bash
python3 - <<'PY'
from pathlib import Path
p=Path('exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N01/gaussian_controls.py')
s=p.read_text().replace('pbox*sigma2/(2*mp.pi)/(1-pbox)','pbox*R*sigma2/(2*mp.pi)/(1-pbox)')
p.write_text(s)
PY
```

That tool call then wrote and ran the separate injection-control script. A subsequent call reran the Gaussian suite using the corrected source. Both Gaussian invocations used this same command:

```bash
timeout 120s python3 exploration/runs/brlwe-joint-foundations-20260906-astra-ultra/criticism/N01/gaussian_controls.py
```

These commands describe the completed original audit. They were **not executed again** during this administrative follow-up.

## What remains available

The original on-disk `gaussian_controls.py` was edited in place, and the original full `gaussian_controls.json` was overwritten by the corrected invocation. No immutable pre-edit copy of either file was retained in N01, and no first-invocation source/output hash was recorded at execution time. Runner-owned snapshots were not accessed.

The original source-creation tool call and first process stdout remain visible in this conversation's tool transcript. This permits the following limited preservation:

- `provenance/first-invocation-stdout-transcript.txt` is a copy of the first invocation's stdout from the tool-return transcript. It preserves the reported matrix summaries and successful completion. It is **not** the full first-invocation `gaussian_controls.json`, and its hash authenticates this recovered transcript copy rather than a separately retained process-log artifact.
- `provenance/reconstructed-first-invocation-gaussian_controls.py` is explicitly a **reconstruction**, made by reversing the one exact recorded replacement in the current source. The administrative byte operation verified that the corrected string occurred exactly once. The reconstructed line agrees with the first source-creation call visible in the transcript. Its hash is a hash of the reconstruction; it is **not** a contemporaneous first-run source hash or proof that an original file was preserved independently.
- The original full first-invocation JSON bytes, including its exact start/finish timestamps and all unprinted fields, are **unavailable in the permitted surviving artifacts**. They were not fabricated, reconstructed from the later JSON, or assigned an invented hash. No first-run timestamp is inferred as exact from the second run.

The byte lengths and SHA-256 hashes observed in this administrative completion are:

| Artifact | Provenance/status | Bytes | SHA-256 |
|---|---|---:|---|
| `gaussian_controls.py` | Surviving corrected source | 8913 | `1ae11c58a5659e4cb2114eaa693122252bfb0af303f1080e0e724a071ea05f60` |
| `gaussian_controls.json` | Surviving corrected-invocation full data | 27314 | `c38b8d3beb47457a08628ddd3de4a7a2ca8c9571f3727393161505857fe034f1` |
| `provenance/reconstructed-first-invocation-gaussian_controls.py` | Reconstruction from the recorded one-line edit | 8911 | `113d19610b02b0874f0cf8a50c28b92d054b34404d92afec1321b90fbe92386f` |
| `provenance/first-invocation-stdout-transcript.txt` | Recovered stdout transcript copy, not full data | 1775 | `d1f01a0b420c5b87536a20e66c05c532ddc8b7823957e2c09cc7594a14eb1cc5` |
| `review-v1.md` | Frozen and unchanged | 40600 | `b2567a04649aca0f668f8fd5278412e1f00f280f755a9b0a7801ec93da365c43` |

## Available command and time evidence

The first Gaussian invocation appears in tool-result chunk `977dbd`. The tool reported exit code 0 and `wall_time_seconds=0.889323062`. Its stdout has `all_assertions_passed=true`, 25 scalar cases, and both matrix summaries. Its exact absolute UTC start/finish values were only in the now-overwritten full JSON, not the retained stdout. Transcript order places this invocation after the recorded 20:43:54 UTC clock check and before the correction/injection call below. These are bounds, not a newly invented timestamp.

The correction/injection call appears in chunk `ff3d54`. The corrected source's observed modification time is `2026-09-06T20:47:45.391114+00:00`. This metadata corroborates the edit sequence but is not an immutable original-run log. The injection JSON independently records start `2026-09-06T20:47:45.417781+00:00` and finish `2026-09-06T20:47:45.420478+00:00`; it was generated later in that same command after the correction.

The corrected Gaussian invocation appears in chunk `e637dd`. Its tool result reported exit code 0 and `wall_time_seconds=0.906198753`. Its surviving full JSON records start `2026-09-06T20:48:00.572270+00:00` and finish `2026-09-06T20:48:01.519961+00:00`. These tool-duration and application-timestamp fields are reproduced as observed; no new timing benchmark was run. The corrected JSON's observed modification time is `2026-09-06T20:48:01.520225+00:00`.

The administrative follow-up began with the 21:01:05 UTC read-only clock/directory check. The recovered/reconstructed artifact hashes above were produced at `2026-09-06T21:02:11.474922+00:00`. File reading, copying transcript text, reversing the recorded text edit, and hashing are the only local operations used here. No numerical Gaussian evaluation, experiment, external retrieval, or runner-snapshot access occurred.

## Effect on the frozen review

This record makes the pre-edit evidence boundary explicit. The initial diagnostic's computations and assertions succeeded, while its tail-bound annotation lacked one factor. The original audit corrected that annotation, reran the suite under its allocated timeout, and based its final report on the corrected artifacts. This follow-up supplies provenance only; it neither reopens the mathematics nor changes the six frozen claim dispositions.

Reviewer `/root/n01_source_audit`, assigned gpt-6-astra / ultra. Previously observed metadata remains `CODEX_THREAD_ID=01a0786f-bf9b-7d23-bf99-ff481afc4581` and `CODEX_SESSION_ID=01a07849-2b26-7ac1-96c2-c15903ac2341`. No content-policy interruption occurred in this follow-up.

Administrative completion: 2026-09-06T21:04:02.505950+00:00, before 2026-09-06T21:09:15Z.
