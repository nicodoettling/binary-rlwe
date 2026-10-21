# Integral linear transfer decomposition — proof and endpoints v1

PROVISIONAL author proof of exactly `linear-transfer-theorem-v1.md`. No earlier theorem is strengthened by this draft.

## Algebraic decomposition

Write G={u modulo 2n:u odd}; |G|=n. For each u the formula for B_u is an integral Z-linear map because multiplication by every w-power and sigma_u are signed permutations of the ordinary coefficient basis. Each summand sends J into I: J is stable under w, T(J) subset I, and I is stable under units sigma_u(w)^(-j). Thus B_u(J) subset I and U_u(J) subset sigma_u^-1(I).

The identity w^n=sigma_u(w)^n=-1 gives

    B_u(wx)=sigma_u(w) B_u(x).

Indeed, reindex j+1 from 1 to n. The term at n becomes the term at 0 since sigma_u(w)^(-n) T(w^n x)=(-1)(-T(x))=T(x). Therefore U_u(wx)=w U_u(x), making U_u R-linear.

The elementary root sum

    sum_{u odd modulo 2n} w^(-uj) = n if j=0, and 0 if 1<=j<n

holds because w^(-2j) is a nontrivial n-th root of unity when 1<=j<n. Summing B_u over u therefore gives nT. Since T is nonzero, at least one B_u, and hence U_u, is nonzero.

## The explicit multiplier and its ideal

The relative power basis 1,z,...,z^(t-1) has dual basis 1,z^-1,...,z^(-(t-1)) under Pi. This follows directly from coefficient selection: Pi(z^(r-s)) is one when r=s and zero for the other differences with |r-s|<t. Consequently

    a_u=sum_(r=0)^(t-1) z^-r U_u(z^r)

is the unique multiplier satisfying U_u(x)=Pi(a_u x) for every x in S. It is integral because all summands are integral. Nonzero U_u implies nonzero a_u. The exact module identity gives

    a_u in sigma_u^-1(I)S J^-1.

Set I_u=sigma_u^-1(I). If I_u=I, this is the required C. Otherwise I_u and I are distinct prime ideals of R. Their extension ideals are coprime, and J above I does not divide I_uS. Unique ideal valuations then give

    S intersect (I_uS J^-1)=I_uS:

the potentially negative valuation -1 at J disappears on intersection with S, and every other valuation is unchanged. Hence a_u belongs to I_uS. Write its unique coefficient expansion a_u=sum_(r=0)^(t-1) b_r z^r with b_r in R. Since S is free over R in this relative basis, membership in I_uS is equivalent to each b_r in I_u. At least one b_r is nonzero, and y=sigma_u(b_r) is a nonzero member of I. This gives the second output by exact arithmetic without a sample from J.

## Norm and bit accounting

All w-powers, sigma_u and their inverses preserve coefficient Euclidean norms. Triangle inequality therefore gives

    ||U_u||_op=||B_u||_op <= n||T||_op,
    ||U_u||_F=||B_u||_F <= n||T||_F.

Because U_u is R-linear, its columns indexed by z^r w^j are the n signed rotations w^j U_u(z^r). The t terms defining a_u occupy disjoint residue classes of exponents modulo t. Thus exactly

    ||U_u||_F^2 = n sum_r ||U_u(z^r)||^2 = n||a_u||^2.

Since U_u has n output rows, ||U_u||_F<=sqrt(n)||U_u||_op. Combining these identities yields

    ||a_u|| <= n||T||_op,
    ||a_u|| <= sqrt(n)||T||_F.

Every R-coefficient block b_r has norm at most ||a_u||, and sigma_u preserves that norm. The same bounds therefore hold for the extracted y.

Each entry of B_u is the sum of exactly n signed entries of T. Applying sigma_u^-1 is another signed permutation, and forming a_u rearranges t blocks without overlapping their coefficient support. Hence all a_u coefficient magnitudes are <=n2^b. There are n choices of u, n summands, and nm matrix entries, so the explicit computation uses O(n^3m) signed additions on O(b+log n)-bit integers. Checking equality of represented ideals and extracting a nonzero block uses polynomial-time exact integer linear algebra. No basis reduction, sampling, or real-number oracle is used.

## Full laws if the map is proposed as a sampler transfer

For a fixed public integral T satisfying the theorem, let L_T=T(J). The exact full planted pushforward of X~D_(J,W) is

    Pr[T(X)=y] = sum_{x in J:T(x)=y} exp(-pi||x||^2/W^2) / rho_W(J)

on y in L_T, retaining y=0. It is not asserted Gaussian on I. Any deterministic failure/tag/norm selection maps this full law to its full output including FAIL, without deleting a normalizer. Full input TV eta contracts to at most eta for this complete pushed law. There is no claim that marginal TV suffices when T is selected after observing X.

The exact distinct uniform input Xbar in J/qJ maps to uniform L_T/qL_T. Its further image in I/qI is uniform on (L_T+qI)/qI, which need not be all of I/qI. This is the actual uniform comparator, with identical I,J,T,q metadata. Selection or checks applied to it retain their actual failure mass. These algebraic endpoint statements do not manufacture a decisional reduction from the ideal-vector extraction interface.

If a proposed algorithm provides such a T before sampling, with operator-norm certificate L, this proof gives either a complementary multiplier or a target vector of norm at most nL using that same public map. It introduces no positive success assumption: the extraction is deterministic on every valid nonzero T. This is the precise circularity test for new integral linear-map constructions. It does not show that computing such a T is impossible, nor cover the explicit exclusions of the frozen theorem.
