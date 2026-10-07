# C1 primary-source and provenance checks

Sources directly read in this assignment:

1. Breuillard–Varju, arXiv:1810.13360v2, Section 5.1, Definition 22 and Proposition 23, printed pp. 23–24. Checked the exact M=1,D=d,Q=q substitution, generic tuple condition, admissibility degree 3 ln(q^d), support condition, duration bound, absolute probability error, and lack of a polynomial-q restriction. Only the proposition is imported; the paper's RH-based irreducibility theorems are not.
2. Voutier, arXiv:1211.3110, Corollary 2, printed p. 4. Checked log Mahler lower bound 2/(ln(3degree))^3 for nonzero non-roots-of-unity of degree >=2. Linear/content/cyclotomic cases are handled separately in the new proof.
3. Thorner–Zaman, arXiv:2108.10878v2, Section 1.2, printed p. 3. Checked the stated Siegel–Walfisz consequence uniform for progression modulus <=(ln x)^A, including the ineffectivity qualification. The new setup deduction uses progression modulus 2n and prime magnitude x=2^ceil(n^(1/8)); these two quantities are deliberately not both called q. The source theorem has been read, not independently reproved.
4. Agrawal–Kayal–Saxena, author-hosted `https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf`, Theorem 4.1 and the stated Section 5 complexity. This supplies the polynomial-bit primality test needed by the optional new setup. It is an optional setup dependency, not a new cryptographic assumption.

The complete targeted raw web-tool return is preserved in primary-web-record-v1.json. Its SHA256 identifies the returned representation, not PDF bytes. Earlier calls read the same BV and Voutier pages; the final recorded call was made to retain a durable raw packet. Screenshot requests for BV p. 24 and Voutier p. 4 returned ordinary tool errors saying the PDF could not be resolved for screenshots; the searchable PDF text and the pre-existing C01 primary-checked report were available. No content-policy interruption occurred.

A search also opened Carella's arXiv:2004.02010 note. It is NOT used as a dependency. The established Thorner–Zaman source was selected for the prime-density statement. No paper from the search-results snippets alone is imported.

The primary HLBDD source comparison is assigned separately to the coordinator. This worker freezes its exact same-ideal source law and does not claim to have reverified its worst-case or cryptographic motivation from the public paper. Input file hashes are in input-hashes-v1.sha256. The old ledger governs claim/version status over frozen proof headers.

Timestamp clarification: partial.md's manually entered 21:47 UTC label was an approximate progress label written shortly before the 21:46:09 UTC clock read, not an exact tool clock timestamp. This does not alter any mathematical version. This final source record uses the actual surrounding tool clock observations.
