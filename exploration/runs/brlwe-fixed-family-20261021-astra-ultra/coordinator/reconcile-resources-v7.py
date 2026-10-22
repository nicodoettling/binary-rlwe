from pathlib import Path
import json,hashlib,datetime,difflib
O=Path(__file__).resolve().parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atom(rel,x):
 p=O/rel;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(x,indent=2)+'\n');t.replace(p)
seals=['reviews/FRONTIER-CHALLENGE1/seal-v1.json','reviews/FRONTIER-CHALLENGE1/compact-v3-addendum/seal-v1.json','reviews/DELIVERY-AUDIT1/compact-v3-full/seal-v1.json','reviews/BLIND-RESOURCE3/final-seal-v1.json','reviews/BLIND-RESOURCE4/seal-v1.json'];checks=[];hs={}
for rel in seals:
 p=O/rel;x=json.loads(p.read_text());hs[rel]=sha(p)
 for key in ['files','artifacts','entries']:
  for e in x.get(key,[]):
   if not isinstance(e,dict) or not e.get('sha256'):continue
   path=e.get('path',e.get('file'));assert path is not None
   qs=[p.parent/path,O/path,Path(path)] if not Path(path).is_absolute() else [Path(path)]
   matches=[q for q in qs if q.is_file() and sha(q)==e['sha256']];assert matches,(rel,path)
   q=matches[0];checks.append({'seal':rel,'file':str(q.relative_to(O)),'sha256':e['sha256'],'match':True})
x=json.loads((O/'claims.json').read_text());by={c['id']:c for c in x['claims']};accepted=[];diffs=[]
for ident in ['FF3-COMPACT-SELECTOR-v3','FF3-ENERGY-RANK-v2']:
 c=by[ident];st=O/c['statement'];pr=O/c['proof'];b=O/'reviews/BLIND-RESOURCE4/allowed-input'/st.name
 assert sha(b) in {a['sha256'] for a in checks}
 if ident=='FF3-COMPACT-SELECTOR-v3':
  full=json.loads((O/'reviews/DELIVERY-AUDIT1/compact-v3-full/seal-v1.json').read_text());assert full['statement_sha256']==sha(st) and full['proof_sha256']==sha(pr);fullref='reviews/DELIVERY-AUDIT1/compact-v3-full/full-report-v1.md'
 else:
  assert sha(st) in {a['sha256'] for a in checks} and sha(pr) in {a['sha256'] for a in checks};fullref='reviews/FRONTIER-CHALLENGE1/kernel-repair-full-review-v1.md'
 diffs.append(ident+'\n'+'\n'.join(difflib.unified_diff(st.read_text().splitlines(),b.read_text().splitlines(),fromfile=c['statement'],tofile=str(b.relative_to(O)))))
 c.update(status='ACCEPTED-EXACT-CONDITIONAL-KERNEL-SCOPE',review='coordinator/acceptance-v7.json',full_review=fullref,blind_review='reviews/BLIND-RESOURCE4/referee-report-v1.md',evidence_sha256={c['statement']:sha(st),c['proof']:sha(pr)},check_depth='Different fresh full edited-proof reviewer and clean fresh theorem-only reconstruction, exact coefficient binding and finite controls; correlated same-model scrutiny, not formal verification.')
 if ident=='FF3-COMPACT-SELECTOR-v3':c['path_binding']='coordinator/kernel-resource-v3-path-resolution-v1.json';c['scope']='Encoded rational M; expected cost polynomial in numeric M and encodings, all endpoint equations separate; finite n2 exact instance only; outer L cap does not cap all inner bit/H runtimes.'
 else:c['dependency_binding']='coordinator/energy-twoevent-dependency-binding-v1.json';c['scope']='Given-h shell-constant rank theorem; pair requires JOINT shell-uniform law; numeric alphabets, expected rational sampling, exact finite Gaussian/truncation law. TWOEVENT conditional construction imports every premise.'
 accepted.append(dict(c))
qual=['COMPACT original fair-bit and v2 real-M defects remain rejected. FRONTIER-CHALLENGE1 same-reviewer compact-v3 recheck is supporting evidence only; DIFFERENT fresh DELIVERY-AUDIT1 edited-statement-and-proof gate is controlling full repair review.',
'BLIND-RESOURCE3 later status/provenance exposure is preserved and is NOT the pristine compact-v3 gate. BLIND-RESOURCE4 had only clean theorem statements, coefficient tables and specifically requested definitions; its exact report/seal controls.',
'All mathematical coefficient fields in sanitized/author tables are canonically identical, recorded in blind-table-linkage-v1.json and independently in DELIVERY-AUDIT1 coefficient-binding. Author experiment shorthand resolves explicitly to workers/FF3/experiments; retained proof-v1 headings are historical text, exact v2/v3 file hashes govern.',
'Every retry uses fresh randomness conditional on x and prior failures. Outputs are sample pairs, not arbitrary leaked internal traces. Shared S is fixed before independent row processing. Complete endpoints P_sK=T_s and UK=V are independent requirements.',
'Expected polynomial numeric-M cost is not polynomial-in-logM cost or all-tape bounded time. Outer caps give output TV only; inner coin/edge/H samplers need separate caps/errors in a future bounded reduction.',
'ENERGY given-h theorem uses shell-constant full laws. Pair marginals alone do not imply joint-shell uniformity. Count-bit bound doubles for pair products; polynomial numerical alphabets and magnitudes are required for DP.',
'Optional TWOEVENT construction imports ALL named premises: finite uniform U,V,strictly positive N,0<u<p<=1,both likelihood inequalities,and union-of-source-shell C. The blind p=u/zero-target extension remains separately recorded and is not promoted by indexing. No optional asymptotic Gaussian instantiation is imported through v7.',
'Finite n2 rational endpoints and known-residual rank transport do not give a scalable efficient Gaussian full-binary-cube reduction. No FF/hardness or scientific-exhaustion conclusion.',
'All203 inherited regression IDs/provenance and scoped dispositions remain; new endpoint/joint-rank/trace/runtime boundaries preserved. Bounded controls do not prove infinite distributions.']
atom('coordinator/acceptance-v7.json',{'at':now,'type':'NONTERMINAL exact resource repair/conditional-kernel acceptance','accepted_claims':accepted,'review_seals':hs,'review_integrity_checks':checks,'qualifications':qual,'path_binding':'coordinator/kernel-resource-v3-path-resolution-v1.json','table_binding':'coordinator/blind-table-linkage-v1.json','dependency_binding':'coordinator/energy-twoevent-dependency-binding-v1.json','blind_text_diffs':'coordinator/acceptance-v7-blind-text-diffs.txt','FF_status':'OPEN','SV_status':'REVIEWED-SUBSTANTIVE-DIAGNOSTIC-AT-INHERITED-RADIUS','hardness_status':'NOT_ESTABLISHED','native_goal':'active','scientific_termination':False,'protected_period':'COMPLETED; review/targeted repair phase'})
(O/'coordinator/acceptance-v7-blind-text-diffs.txt').write_text('\n\n'.join(diffs)+'\n');x['updated_at']=now;atom('claims.json',x)
r=json.loads((O/'regressions.json').read_text())
for e in r['new_entries']:
 if e['id']=='FF3-COMPACT-M-ENCODING-1':e['status']='V2_REJECTED_V3_ACCEPTED_EXACT_REPAIR';e['review']='coordinator/acceptance-v7.json'
if not any(e['id']=='FF3-COMPACT-PERSISTENT-EDGE-1' for e in r['new_entries']):r['new_entries'].append({'id':'FF3-COMPACT-PERSISTENT-EDGE-1','status':'PRESERVED_EXACT_NEGATIVE_CONTROL','evidence':'reviews/DELIVERY-AUDIT1/compact-v3-full/full-report-v1.md','scope':'G=(1/2,3/2,1/2,3/2),M=3/2: retaining first edge across retries gives two-failure2/9, not1/9, and mean2,not3/2. Fresh proposals mandatory; not a counterexample to accepted v3.'})
r['updated_at']=now;atom('regressions.json',r)
with (O/'reconciliation.md').open('a') as f:f.write('\n\n## Exact resource acceptance v7 — '+now+'\n\nCOMPACT-v3 and ENERGY-v2 accepted only at exact conditional/expected-cost scopes. A DIFFERENT fresh DELIVERY-AUDIT1 proof referee closes the compact repair, and clean BLIND-RESOURCE4 reconstructs both statements. Earlier compact-v2 full PASS is withdrawn; contaminated later BLIND-RESOURCE3 exposure is not used as pristine repair gate. Exact paths, table coefficients, all TWOEVENT premises, shared-secret law and inner-runtime limits are bound explicitly in acceptance-v7. No scalable full-cube family, FF reduction or hardness is obtained.\n')
print({'at':now,'accepted':['FF3-COMPACT-SELECTOR-v3','FF3-ENERGY-RANK-v2'],'sealed_checks':len(checks),'local_regressions':len(r['new_entries'])})
