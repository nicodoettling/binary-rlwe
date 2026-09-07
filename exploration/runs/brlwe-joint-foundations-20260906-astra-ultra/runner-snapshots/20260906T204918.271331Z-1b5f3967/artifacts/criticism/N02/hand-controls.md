# N02 exact finite hand controls

These are exact hand calculations, not a CPU search. No experiment slot was allocated or used. All rings and probability spaces below are local mathematical synthetic models. None is a deployed cryptographic target. The finite controls do not prove the unrestricted theorem.

## HC-N02-1: reproduce SE-CORRELATION-F3

Work in R=F3 with J=0, I=Q_J=R and U=1. Draw F,V,S,G,H independently uniformly in R; set E=-S. Let S0 and E0 be fresh independent uniform R variables. The primitive five-variable law gives each (F,V,S,G,H) mass 3^-5, with E then determined; adding S0,E0 gives each primitive seven-tuple mass 3^-7. All probabilities normalize to one.

The retained Nhat comparison has exact error zero: conditional on F=f, fG+H is uniform R because H is fresh uniform, while E=-S is uniform R and independent of F. For extraction, for every (f,h,y,s),

    Pr[F=f,H=h,Y=y,S=s] = 1/81,

since the unique G=y-s has probability 1/3. This is exactly the law with S replaced by independent uniform Z. Thus eta_X=0. Since U=1, UR=I and eta_iso=0. The independent source (1+F,V+E0) is uniform on R^2, every pair having probability 1/9.

The target draws a fresh uniform a independently of the correlated pair (S,E=-S) and outputs (a,(a-1)S). Its 3-by-3 probability table (rows a=0,1,2; columns beta=0,1,2) is

    [1/9, 1/9, 1/9]
    [1/3,   0,   0]
    [1/9, 1/9, 1/9].

The total mass is 6/9+1/3=1. Against the uniform table, TV is (1/2)(2/9+1/9+1/9)=2/9. The event {a=1,beta=0} has probabilities 1/3 and 1/9 and witnesses this difference. P in OBS.1 has the same table; Q is uniform. Therefore both literal old A1 and old A2 fail with zero stated errors and zero source advantages.

The edited product law excludes this exact control: it requires Pr[E=e|F=f,S=s]=P_E(e)=1/3 on every positive-mass (f,s), whereas this model gives the point mass at -s. It is not enough that E be independent of the latent source alone. No earlier verdict on the omitted premise is carried over to the repair.

## HC-N02-2: NEW pairwise independence still fails the finite hybrid

Again take R=F3,J=0,U=1. Draw F,V,S,G,H independently uniformly and set E=-F-S; S0,E0 are fresh independent uniform draws. The primitive seven-tuple has mass 3^-7. For every (f,s,e),

    Pr[F=f,S=s,E=e] = 1/9 if e=-f-s, and 0 otherwise.

Every two-coordinate marginal of (F,S,E) is uniform on R^2, with masses 1/9: for prescribed (f,e) there is exactly one s=-f-e, and similarly for the other pairs. Thus S and E really are independent as a pair, and each is individually independent of F. E is also independent of every separately sampled V,G,H,S0,E0. The full triple is not the product law: it has nine supported points of mass 1/9 instead of 27 points of mass 1/27. The triple TV from the product law is 2/3.

Nhat and Xhat remain exact with eta_N=eta_X=eta_iso=0. The first follows from fresh uniform H and the uniform E marginal conditional F; the second from fresh uniform G as in HC-N02-1. Yet

    (1+F)S+E = F(S-1).

For F=0 (a=1) the response is identically zero, and for F=1,2 it is uniform. P therefore has exactly the preceding 3-by-3 table, while Q is uniform and TV(P,Q)=2/9. This rejects OBS.1 under a weakened assumption demanding only pairwise independence. Here the independently generated target a together with the marginal product pair (S,E) is uniform, so this control is specifically a failure of the finite comparison and first noise-append step; it is not a new counterexample to OBS.2.

The exact point of failure is appending S to Nhat. Conditional on (F=f,S=s), target E is the point mass at -f-s, whereas fG+H remains uniform R; the retained (F,S,N) TV is 2/3 although the retained (F,N) TV was zero. The edited statement excludes the model by explicitly imposing mu x P_S x P_E jointly. This check is new relative to the received SE-CORRELATION-F3 witness and to the old binary-XOR control.

## HC-N02-3: NEW full-product law across zero and nonzero U fibers

Take R=F3,J=0,I=Q_J=R. Let U,V,S,G,S0 be independent uniform R variables, and F=H=E=E0=0 deterministically. Each primitive (u,v,s,g,s0) has mass 3^-5. The complete edited product-kernel premise holds. For the extracted side, append uniform independent Z; for H3r use an independent uniform G0. Each augmented primitive tuple has the appropriate mass 3^-6 or 3^-7 and normalizes to one.

Because F=H=E=0, Nhat is exact. Because G is uniform, (Y=S+G,S) is uniform on R^2, with each atom mass 1/9, so Xhat is exact. U is zero with probability 1/3. Conditional on U=0, UZ is the point mass at 0; conditional on either U=1 or U=2, UZ is uniform R, each output having mass 1/3. The conditional image distance is 2/3 on the zero branch and 0 on each nonzero branch. Thus

    eta_iso = (1/3)(2/3) + (2/3)0 = 2/9.

The P=(U,US) table (rows u=0,1,2) is

    [1/3,   0,   0]
    [1/9, 1/9, 1/9]
    [1/9, 1/9, 1/9],

while Q=(U,V) is uniform, each atom mass 1/9. Both have total mass one, and TV(P,Q)=2/9. H1,H2,H3,H3r,H4 all have the P table: the Nhat changes do nothing, and replacing S by Z preserves the conditional US law. H5,H6,H7 have the uniform table. The public event {a=0,beta=0} has probabilities 1/3 and 1/9 and realizes the entire gap. Since the source itself is uniform R^2, both source advantages vanish; the target has TV 2/9. Hence OBS.1 and OBS.2 are attained with their exact eta_iso term.

The source-endpoint translation can be checked pointwise. For every prescribed (u,s0,v'), there is a unique v=v'+u s0, so

    Pr[U=u,S0=s0,V'=v'] = 1/27,
    V'=V-U S0.

Thus V' is uniform and independent of U,S0 even on the U=0 fiber. This is an exact normalized kernel calculation, not a marginal-independence assertion.

Finally, conditioning U to be nonzero changes its law by delta_act=1/3. In that active model P=Q exactly and eta_iso=0. The numbers delta_act=1/3 and eta_iso=2/9 are distinct, as the proof requires.

## HC-N02-4: old-secret retention versus valid discarding

Take S uniform {0,1} in F3 and G uniform F3, independent. Every (s,y) with s=0,1 has probability 1/6. Thus Y is uniform and independent of S. Against independent uniform Z in F3, (Y,Z) has nine atoms of mass 1/9, giving TV((Y,S),(Y,Z))=1/3.

If the original S is retained, the triple (S,Y,S) has six supported atoms of mass 1/6. The comparison (S,Y,Z) has 18 supported atoms of mass 1/18, giving TV=1-1/3=2/3. This reproduces the dossier's old-secret control. H3r may only replace the discarded old construction of Y after the extracted retained tuple factors as mu K P_Y Unif_Q; it may not preserve an unmentioned old-S coordinate.

## HC-N02-5: rank-test finite control independently recomputed

In the received n=4,q=97,d=1,b=1 control, F=E=0 and R0=0, so B0=4. All roots 33,47,64,50 satisfy r^4=-1 mod 97; they are distinct. The middle gate is sqrt(97)>4. The final gate is 97^(3/4)>16; raising both sides to the fourth power compares 97^3=912673 with 16^4=65536. Also 2<97.

For each of the four singleton T, every (U,V) pair has conditional mass 97^-2. With uniform T the primitive (T,U,V) atoms have mass 1/(4*97^2); adding binary S,S0 gives mass 1/(4*97^2*16^2). The only deficient branch is U=0, with total mass 1/97. Under P the response is zero there. Under Q the response is V; the strict norm gate forces every ideal vector in Box(4) to be zero. The test therefore accepts with probabilities 1/97 and 1/97^2, giving 96/9409=eta_iso. This test is finite and potentially exponential, not PPT.

## HC-N02-6: NEW hidden varying quotient and zero fibers in a nonsemisimple ring

This further hand check was added after reading B01's updated partial report, which independently records a related pairwise F3 example. It tests a different finite ring and a hidden mixture of quotient sizes; it is not claimed as statistically independent reviewer evidence.

Let R=F2[t]/(t^2), ordered as (0,t,1,1+t), and choose J uniformly from {0,(t)}. For J=0, I=Ann(J)=R; for J=(t), I=Ann(J)=(t)={0,t}. Conditional on J draw U,V independently uniformly in I. Put F=H=E=E0=0. Draw S,G,S0 independently uniformly in R and independently of the whole source kernel. Thus, on J=0, each primitive (U,V,S,G,S0) atom has mass 1/(2*4^5)=1/2048; there are 4^5 such atoms, totaling 1/2. On J=(t), each atom has mass 1/(2*2^2*4^3)=1/512; there are 2^2*4^3 such atoms, again totaling 1/2. The whole law is exactly the edited product-kernel law and normalizes to one.

Nhat is exact. Since G is uniform R, Y=S+G is independent uniform R, so pi_J(S) is uniform in the varying Q_J and independent of Y conditional J. Xhat is exact, with its required uniform kernel depending only on J.

For J=0, the conditional image defects for U=0,t,1,1+t are 3/4,1/2,0,0. For J=(t), the defects for U=0,t are 1/2,0. In particular t is not a unit of R but does identify R/(t) with (t). Averaging gives

    eta_iso = (1/2)[(3/4+1/2)/4] + (1/2)[(1/2)/2]
            = 5/32+4/32 = 9/32.

For P=(U,US), the exact public probability matrix, with both rows and columns in order (0,t,1,1+t), is

    (1/32) * [[12,0,0,0],
              [ 6,6,0,0],
              [ 1,1,1,1],
              [ 1,1,1,1]].

For Q=(U,V) it is

    (1/32) * [[5,5,1,1],
              [5,5,1,1],
              [1,1,1,1],
              [1,1,1,1]].

Both matrices have numerator sum 32. Their L1 discrepancy is 18/32, so TV(P,Q)=9/32=eta_iso. A public event attaining the distance is {a=0,beta=0} union {a=t,beta in (t)}: its probabilities are 24/32 and 15/32. This checks full-joint averaging over varying J and quotient sizes, the distinction between a nonzero ring element and a quotient-to-ideal isomorphism, all zero-rank branches, and projection to the actual public pair. It is a finite positive control, not a proof for all finite rings.

## Historical normalization checks retained

Same-Y posterior replicas: take independent S uniform {0,1} and integer G with masses 1/4,1/2,1/4 at -1,0,1. Y=S+G has masses (1/8,3/8,3/8,1/8) at (-1,0,1,2), and the posterior probabilities p_y=Pr[S=1|Y=y] are (0,1/3,2/3,1). These normalize on every positive-mass fiber. Draw S,S' independently from the same posterior after Y is drawn. Then Pr[S-S'=+1]=Pr[S-S'=-1]=(3/8)(2/9)+(3/8)(2/9)=1/6, and Pr[S-S'=0]=2/3. Independent unconditional prior replicas would give collision 1/2 instead. This reproduces the current coordinator evidence from its specified finite law. H3r's fresh unconditional representation of the extracted-side P_Y does not replace the same-Y posterior replica law used inside inherited X1.

CP-1: preconditioning mass of vk=1 is 2*(21/2200)+2*(1/11)*(1/2)+879/1100=10/11. Dividing gives A_b=21/2000,C_b=1/20,D=879/1000, total 1. Raw incidences are 1/10,121/2000,21/2000. At strict threshold 1/10 none is heavy. The selected two-hit probability is 2*(21/2000)*(1/2)=21/2000>1/100. Later incidence 21/221<1/10 does not repair the false product; support restriction and normalization caused the inflation. The edited hybrid uses contraction of complete joint measures; the rank proof conditions on full T,U,F before using fresh V. Neither proof asserts the false product.

F5 erasure: F uniform {0,1}, U=1,V uniform F5. Comparing H=0 with H=F gives latent TV 1/2, but both public (1+F,V+H) laws have ten atoms of mass 1/10. Thus public TV is zero. This remains a live rejection of latent-to-public lower-bound projection. W3-RANK supplies its own public F-recovery and membership test under strict extra hypotheses.

Common K: in F3 with U1=U2=1, a common uniform K yields three diagonal atoms of mass 1/3; independent ideal points yield nine atoms of mass 1/9. TV is 2/3. The edited theorem is m=1 and does not replace that common-K law by a product source.

NC1 guard: for M=0,n=p=1,sigma=1,tau=1/3, true TV is zero and delta>=2 exp(-pi/9)>1, so delta/(1-delta) is negative. The explicit v2 guard returns 1. H_seq's parity-dependent normalizer in the received [[2,-1],[-1,2]] matrix example is likewise retained; it is never silently identified with D_B.

Correlated Gaussian marginals: independent S,T fair and Z~D_sigma, with E1=Z,E2=(-1)^(S xor T)Z, preserve each conditional Gaussian marginal but give guessing 1-W_sigma,q(0)/2 when T is revealed versus 1/2 without T. Full joint noise laws, not marginal widths, are required. The repaired product-kernel model and the retained Nhat/Xhat premises preserve this distinction.
