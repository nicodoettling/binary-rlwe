# Status-only exposure exception for the eleventh claim

At approximately 20:26 UTC on 2026-10-21, the explicitly supplied and hashed
`allowed-input/rs-actual-radius-witness-statement-v1.md` was opened in full. Its
second paragraph unexpectedly included:

> Provisional parameter corollary of SV-RS-DECODE-v1 and SV-DENSE-SPLIT-v1; exact-version review required. It is not a new FF theorem.

This is author-status exposure for SV-RS-ACTUAL-v1. It is not an author proof,
counterexample, or experimental result. The parent was immediately notified and
agreed that this eleventh claim must be labeled independent statement
reconstruction with a status-only exception, not a strict blind gate. Removing
that line after exposure would not restore blindness, so the frozen input and
its hash are preserved unchanged.

The original six-claim packet had no author-status label exposed. The four later
claims had the limited sanitizer-metadata exposure recorded separately in
`exposure-qualification-v1.md`; their actual author-status paragraphs were not
read. All ten proofs had already been drafted before this additional claim
arrived. No historical author proof or theorem file was
opened under the v4 manifest's optional additional-read permission. Further
parameter information has been requested as sanitized definitions only.
