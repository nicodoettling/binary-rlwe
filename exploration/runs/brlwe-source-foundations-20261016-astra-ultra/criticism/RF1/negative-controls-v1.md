# RF1 targeted negative controls

These refute nearby shortcuts, not the frozen theorem or author proof. They were checked before any report integration; no author repair is proposed.

## RF1-N1: three positive marginal complements can hide a negative full complement

Take n=4,m=3, ell^2=4, and all three blocks equal I_4. At sigma^2=8, each marginal complement is (8-4)I_4=4I_4>0. The full 12-by-12 complement is 8I_12-4 M M^T for M=[I_4;I_4;I_4]. For x=[e_1;e_1;e_1], x^T B x=8*3-4*9=-12. Thus blockwise positivity is insufficient. The frozen proof uses the full operator norm and a much larger sigma, and passes. The exact script also tests the valid three-distinct-block case and rejects a block-diagonal substitution there.

## RF1-N2: expansion coins cannot be appended to EX-REG

Fix any valid n,q,m. If the comparison also reveals all expansion coins R,W, then C is deterministic given (A,R,W). The event C=Expand(A;R,W) has probability one in the real joint law and q^(-mn) under independent uniform Z appended to the same (A,R,W). Consequently joint TV is 1-q^(-mn). The frozen EX-REG retains A but does NOT retain R,W, and the target interface explicitly withholds those coins. Its proof-only planted reveal is a different information upper bound.

## RF1-N3: appending an internal completion variable can destroy a noise comparison

Finite diagnostic: take H uniform F_3, G=0, M=0, and E=MG+H=H. Its marginal is exactly uniform. Comparing (H,E) to (H,U) with independent uniform U has TV 2/3, although comparing E to U has TV zero. Thus marginal noise comparison cannot simply append H. The author proof explicitly integrates H out of the comparison and reveals it only in the completed-world guessing upper bound; it does not make this invalid extension. This toy is not asserted to satisfy the Gaussian reference parameter assumptions.
