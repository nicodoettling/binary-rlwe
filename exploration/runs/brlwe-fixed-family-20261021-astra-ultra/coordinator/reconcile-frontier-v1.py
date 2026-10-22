import pathlib,json,hashlib,datetime,difflib
O=pathlib.Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atom(name,obj):
 p=O/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(obj,indent=2)+'\n');t.replace(p)
seals=['FULL-FRONTIER1/review-seal-v1.json','BLIND-FRONTIER1/seal-v1.json','FULL-SOURCE3/phase1-final-seal-v1.json'];checks=[];sealhash={}
for name in seals:
 p=O/'reviews'/name;sealhash[name]=sha(p);x=json.loads(p.read_text())
 for key in ['artifacts','files','inputs']:
  for e in x.get(key,[]):
   if not isinstance(e,dict) or not {'path','sha256'}<=e.keys():continue
   z=p.parent/e['path'];match=z.exists() and sha(z)==e['sha256'];checks.append({'path':str(z.relative_to(O)),'sha256':e['sha256'],'match':match});assert match,z
ids=['GAUSS-AVG-v1','FRAC-INFO-v1','WEIGHT-COV-v1','WEIGHT-GAUSS-v1','SV-PRIME-SUPPORT-v2','SV-ALL-SUBFIELDS-v1'];claims=json.loads((O/'claims.json').read_text());accepted=[];diffs=[]
for c in claims['claims']:
 if c['id'] not in ids:continue
 st=O/c['statement'];pr=O/c['proof'];blind=O/'reviews/BLIND-FRONTIER1/allowed-input'/st.name
 diff='\n'.join(difflib.unified_diff(st.read_text().splitlines(),blind.read_text().splitlines(),fromfile=str(st.relative_to(O)),tofile=str(blind.relative_to(O))))
 diffs.append(diff)
 c['status']='ACCEPTED-EXACT-DIAGNOSTIC-SCOPE';c['evidence_sha256']={c['statement']:sha(st),c['proof']:sha(pr)};c['review']='coordinator/acceptance-v4.json';c['check_depth']='Nonauthor full proof/source/complexity plus fresh statement-only reconstruction and bounded controls; same-model correlated scrutiny, not formal verification.'
 if c['id']=='SV-PRIME-SUPPORT-v2':c['full_review']='FULL-SOURCE3 exact v2; earlier FULL-FRONTIER1 v1 is NOT a repair gate'
 else:c['full_review']='FULL-FRONTIER1'
 c['blind_review']='BLIND-FRONTIER1 strict no-status six-claim subset'
 accepted.append(dict(c))
assert len(accepted)==6
(O/'coordinator/acceptance-v4-blind-text-diffs.txt').write_text('\n\n'.join(diffs)+'\n')
record={'at':now,'type':'NONTERMINAL exact auxiliary/source diagnostic acceptance','accepted_claims':accepted,'review_seals':sealhash,'review_integrity_checks':checks,'blind_text_reconciliation':'coordinator/acceptance-v4-blind-text-diffs.txt: only author status, proof/status references and prior regression pointers omitted; mathematical hypotheses/conclusions preserved. Strict subset comprises original six claims only.','qualifications':['GAUSS/WEIGHT Gaussian TV claims retain S and their common affine Gaussian law. They imply neither hidden-secret marginal TV nor general nonlinear transfer impossibility.','FRAC-INFO has statistical ML over a finite alphabet with no efficient/transcendental-comparison algorithm claim; conditioned on one S, the physical samples are iid. Its fixed q,sigma permit a sufficiently high polynomial K that defeats universal statistical hiding.','WEIGHT-COV uses finite second moments but concludes exact equality obstruction, not approximate TV without tails.','PRIME-SUPPORT-v2 explicitly restricts the exponential-index existence example to rho>0; rho=0 has only J=R. Algorithm is ordinary-basis, polynomial in numeric feasible contraction, with no supplied factorization.','ALL-SUBFIELDS minima are used only when feasible sets exist; eligible norm<2^n supplies this. The criterion comparison excludes no other decoder.','FULL-SOURCE3 additive correction cde9466547daf28c5e7ea1d0205b6099f1d7cae601a3e2c252459874d31fd245 withdraws RS-v1 and affects its descendants, not PRIME-SUPPORT-v2.','External normal-form theorem used at exact standard scope; publisher abstract directly checked, full Kannan-Bachem proof not audited. Milne relevant full text and Xylouris theorem statement checked.','All203 inherited regression references retained at their scoped applicability. No historical theorem promoted by cataloguing.'],'FF_status':'OPEN','SV_status':'REVIEWED-SUBSTANTIVE-DIAGNOSTIC-AT-INHERITED-RADIUS','hardness_status':'NOT_ESTABLISHED','native_goal':'active','scientific_termination':False,'protected_period':'IN_PROGRESS'}
atom('coordinator/acceptance-v4.json',record);claims['updated_at']=now;atom('claims.json',claims)
with (O/'reconciliation.md').open('a') as f:f.write('\n\n## Exact frontier acceptance v4 — '+now+'\n\nSix auxiliary/source statements are accepted at their exact scopes after the full and strict blind subset reviews: '+', '.join(ids)+'. All157 sealed artifact/input hashes match. The sanitized blind text differences preserve the mathematical claims and are recorded separately. PRIME-SUPPORT-v2 uses a fresh full repair review; its rejected v1 is not promoted. The RS-v1 withdrawal remains in force and does not affect this independent dependency. ALL-SUBFIELDS applies its minima only to nonempty feasible sets, as guaranteed for eligible source norms. Fixed-family reduction remains open, source diagnostic is substantive at the inherited radius, and hardness is not established. This acceptance is nonterminal during the protected investigation.\n')
print({'accepted':ids,'integrity_checks':len(checks),'at':now})
