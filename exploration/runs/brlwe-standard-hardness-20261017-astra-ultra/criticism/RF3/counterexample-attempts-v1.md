# RF3 counterexample attempts before any repair

Frozen target: binary-class-count theorem SHA256 f090c6c128eb2d0fd52a9cadb2a2b67b8bdd731d84ef932aabbbdc3c74eb180a; proof SHA256 012d77de4765194b8b22943d81773c42c59739f00e91012df8afd676ef210bfc. No change to either input has been proposed or made. These are exact hand calculations, not a new computational experiment.

1. **Omitting the ramified-prime factor fails.** In degree 2, R=Z[i] and z=1+i have N(z)=2. The principal ideal (z) has exactly two integral divisors, R and (1+i). Here u_2=0, so 2^u_2=1 would be too small. The frozen M_2=(v_2+1)2^u_2=2 is correct. There is one prime of norm 2, not two independent primes attached to the two embeddings.

2. **High-index integral representatives do not escape.** If J is integral and z is a nonzero ternary element of J, then (z) is contained in J, which is contained in R. Thus N(J) divides N((z)) and N(J)<=N((z))<=n^(n/2). An attempted collision in an integral J of larger index contradicts this chain. The theorem imposes no prior norm constraint, but a collision itself imposes this derived norm constraint. Multiplying an ideal by a large integer can remove a collision; it cannot preserve that collision at arbitrarily large index.

3. **Fractional representatives do escape, in every class.** Choose any nonzero integral representative I of any ordinary ideal class and any nonzero a in I. The same-class fractional ideal L=a^(-1)I contains 1, and hence contains R. In L the binary vectors 0 and 1 collide. Therefore every ordinary ideal class has a fractional representative with a binary collision. This refutes an extension of the finite count to fractional ideals; it does not refute the actual theorem, which explicitly excludes them. For a nonprincipal class, such an L cannot be integral: an integral ideal containing 1 would equal R.

   This also gives an exact posterior countercontrol to the corresponding fractional extension. Let S and G be independent and uniform on the coefficient cube {0,1}^n, with G supported on R contained in L. There are 3^n possible sums y in {0,1,2}^n; for each y, the maximum over s of Pr[S=s,Y=y] is 4^(-n). Hence optimal guessing probability is 3^n/4^n, strictly less than one. This is an exact finite sum, with no sequential-conditioning product assumption.

4. **A pointwise embedding bound would be false.** In degree 4, let zeta=exp(pi i/4) and z=1+zeta+zeta^2=zeta(1+sqrt(2)). One embedding has |z|=1+sqrt(2)>sqrt(4). The absolute field norm is nevertheless 1. The proof uses the sum of all squared embedding moduli and AM-GM, not the false pointwise inequality; it survives this control.

5. **The odd-prime bound allows equality.** In degree 4, z=1+zeta-zeta^2 has relative norm -3i to Q(i), so its absolute norm is 9. The norm lower bound for odd prime ideals is 2n+1=9. Since 3 has residue degree 2, (z) is one prime ideal of norm 9 and has exactly two integral divisors. Replacing >= by > would be wrong; the frozen proof uses >= and succeeds.

6. **Small dimensions do not give an effective asymptotic cutoff.** In degree 2 the class group has size 1 and its principal class belongs to C_2 via J=R. Thus the fraction is 1, whereas the finite count bound is 16. The asymptotic claim must not be interpreted as a strict fraction bound valid in every dimension. No starting dimension is claimed.

7. **Nonuniform masks do not defeat disjoint-coset decoding.** In Z[i], take J=2R, S uniform on {0,1,i,1+i}, and G=0 with probability 1/3 or G=2 with probability 2/3. The eight sums split into disjoint sets according to S; each has posterior guessing probability one. More generally, two representations y=g+s=g'+s' would force s-s' in J. No choice of mask probabilities can overcome injectivity. The principal class lies in C_2 because of another representative R; this illustrates that class exclusion is a sufficient condition for every representative, not a necessary condition for an individual representative.

No counterexample to the frozen theorem was found. The failed stronger statements above are retained as regressions, especially the all-classes fractional escape. No repair was needed or endorsed.
