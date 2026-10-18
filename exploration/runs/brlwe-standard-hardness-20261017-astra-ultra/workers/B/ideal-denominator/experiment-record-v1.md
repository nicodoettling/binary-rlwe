# B-IDEN-1 exact control record

Coordinator reservation granted for the proposed deterministic control, <=30s wall and <=256MiB address space. Start notified at 2026-10-17 20:49:11 UTC; completion/release notified at20:49:25 UTC. No process remains active.

Code: control-v1.py, SHA256 f266f3fb6802789c757124b8facc290a3aad75abdd68333a5203c65c2fac68eb. Exact command is preserved in control-v1.command.txt. No seed: all inputs and cases are deterministic. Mathematical arithmetic uses Python integers and Fraction; floating point appears only in timing measurement.

Inputs n=4,p=41,q=17, all four roots3,14,27,38 of X^4+1 mod41. Tested160 nonzero fractional cosets,12960 denominator-membership probes in {-1,0,1}^4, and334084 comparator inputs. All assertions passed, including row orientation, rational/modular lift identity, integrality, membership equivalence, binary-image size16, bijective public-basis maps, and exact box counts (2b+1)^4 for b=0,1,2,4,8. Zero coset is explicitly excluded from the claim Den(a)=J; its denominator is R.

Exit0. Script monotonic elapsed1.2531652550096624s; maxRSS25036KiB; RLIMIT_AS268435456 bytes and RLIMIT_CPU30s. Shell timeout30s supplied the wall guard. Initial tool returned a session after1.001019253s; later poll reported exit0. These tool elapsed values are distinct from the script's own duration.

stdout control-v1.stdout.json SHA25673cc338982382d7b2f3cda9f1fc9c244310983474ccc28c220583f465b2304c4. stderr empty, SHA256e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.

Finite control is a falsification check only. It does not prove an asymptotic bound, ideal family hardness, or a Gaussian-normalizer claim. No theorem is self-certified by this record.
