# R2 cyclotomic tower lift: exact first endpoint test v1

PROVISIONAL root calculation. This tests a new field-extension ingredient outside the accepted same-field class-count theorem. It is not a general barrier, standard hardness proof, or accepted theorem. Full independent review remains absent.

Let K=Q(zeta_(2n)) and L=Q(zeta_(2m)), n,m powers of two with m=tn, t>=2. Write R and S for their integer rings and z=zeta_(2m), so z^t=zeta_(2n). The relative power basis is 1,z,...,z^(t-1). Define the integral R-linear projection

    Pi(sum_(j=0)^(t-1) b_j z^j)=b_0=Tr_(L/K)(x)/t.

It has coefficient Euclidean operator norm one. The division by t is exact on S; no rounded trace is being used. For an odd prime ideal I of R, M=N(I), all primes are unramified in this tower. Let I S=product_(a=1)^r J_a with residue degree f, so t=rf. Each J_a has norm M^f. The extension ideal I S has norm M^t, preserving normalized determinant M^(1/n). Choosing a single prime factor instead gives normalized determinant M^(1/(nr)), a possible reduction by splitting. This is the proposed benefit, not yet a valid reduction.

The full output map fails the needed ideal containment when r>=2. Modulo I, the CRT algebra S/IS is a product of r finite fields of degree f over R/I. Pi modulo I is (1/t) times the sum of their field traces. Each finite-field trace is onto, and t is invertible modulo the odd residue characteristic. The ideal J_1 imposes zero only in its first component; a second free component already makes Pi(J_1) modulo I onto. Moreover I is contained in Pi(J_1), since constants from I are in J_1. Thus

    r>=2: Pi(J_1)=R;     r=1: J_1=IS and Pi(J_1)=I.

Consequently the direct projection obtains determinant improvement precisely on the branch where it loses the target ideal. The original Gaussian output law on J_1 is not transported to a Gaussian on I. For exact X~D_(J_1,W), its full pushforward is

    Pr[Pi(X)=y] = sum_(x in J_1, Pi(x)=y) exp(-pi||x||^2/W^2) / rho_W(J_1).

For r>=2 this is positive for every y in R, including points outside I. It cannot be labelled D_(I,s) at any s without a new approximation or rejection analysis. A claim of approximate usefulness would need an actual outside-I mass bound, not merely this support observation. Rejection onto I uses its actual normalizer and pays every attempt; it changes the source law.

For an integer q>=2, uniform X in J_1/qJ_1 maps uniformly onto R/qR when r>=2. This follows from Pi(J_1)=R and the quotient homomorphism. Metadata I,J_1 and the tower remain public and identical. For r=1 the same argument gives uniform I/qI. Thus both endpoints, including their different target modules, are explicit. A source distinguisher or a recovery algorithm in dimension m does not automatically supply one in dimension n; the binary target in dimension m still has m independent coefficient bits and m-dimensional coefficient Gaussian errors per ring sample. No secret-law transport is asserted.

Concrete easy control: n=2,m=8,t=4,p=17. Take J=(17,z-3) in S=Z[z]/(z^8+1), since 3^8=-1 mod17. Its contraction is I=(17,i-13), since i=z^4 and 3^4=13 mod17. Here M=17, r=4,f=1. J is eligible already at rho=3/4, since17<2^6; IS has norm17^4>2^8. The element z-3 belongs to J but Pi(z-3)=-3 does not belong to I. In fact the exact CRT argument above gives Pi(J)=R. Both number fields in this finite example are easy controls, not a hard family.

Tower size is a separate restriction. For any fixed odd rational prime p and conductor2^a, the residue degree is ord_(2^a)(p). Put c=max(v_2(p-1),v_2(p+1)). Once a is large enough, the ratio of residue degree to field degree2^(a-1) is 2^(1-c), by repeated squaring of odd units. Thus the minimum eventual normalized prime norm is p^(2^(1-c)), not a quantity tending to one with dimension. For p=5, every power-two degree n>=2 has residue degree n/2 and normalized prime norm sqrt(5)>2. No amount of this tower lifting makes those prime ideals meet N(J)<=2^(rho n),rho<1. This p=5 family is itself an easy control and does not exclude algorithms that treat it separately. The finite test below checks orders directly; a general source-family theorem is not imported from the computation.

Possible next ingredient: a weighted trace Tr(aX)/t, a nonlinear combination, or an input-dependent class-changing construction. For weighted traces one must first compute the exact trace-dual module of a satisfying Tr(aJ)/t subset I, then account for a's norm, computability and full pushed Gaussian law. Assuming a short such a is available would introduce new advice. Products of samples or selective prime factors do not preserve the stated Gaussian law automatically. These possibilities remain open; this test only rejects the unweighted prime-factor projection as an exact family transfer.
