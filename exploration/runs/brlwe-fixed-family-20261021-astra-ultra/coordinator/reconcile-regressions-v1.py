from pathlib import Path
import json,hashlib,datetime
O=Path(__file__).resolve().parents[1];ROOT=O.parents[2];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def enc(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
r=json.loads((O/'regressions.json').read_text());checks=[]
registries=['reviews/FULL-FRONTIER1/regression-dispositions-v1.json','reviews/FULL-SOURCE3/regression-dispositions-v1.json','reviews/FULL-FF3-PHASE2/regression-dispositions-v1.json']
rs={p:json.loads((O/p).read_text()) for p in registries}
for e in r['inherited_entries']:
 p=ROOT/e['source_registry'];x=json.loads(p.read_text());parts=e['json_pointer'].strip('/').split('/');v=x
 for k in parts:v=v[int(k)] if isinstance(v,list) else v[k]
 ok=digest(p)==e['source_registry_sha256'] and enc(v)==e['entry_sha256'] and v['id']==e['id'];assert ok,e['id'];checks.append({'id':e['id'],'source_pointer':e['json_pointer'],'source_and_entry_hash_match':ok})
 e['exact_current_dispositions']=[]
 for rel,x in rs.items():
  entries=x.get('entries',[]);matches=[(i,a) for i,a in enumerate(entries) if a.get('id')==e['id']];assert len(matches)==1,(rel,e['id']);i,a=matches[0]
  e['exact_current_dispositions'].append({'registry':rel,'registry_sha256':digest(O/rel),'json_pointer':'/entries/'+str(i),'entry_sha256':enc(a),'scope':'Read exact entry disposition/reason; no historical recertification or blanket pass.'})
 e['current_applicability']['frontier/source/FF3']='Acceptance-v4/v5/v6 plus exact per-ID disposition pointers below. Original negative scopes and CP-1 remain binding.'
assert len(checks)==203 and len({e['id'] for e in r['inherited_entries']})==203
seen={e['id'] for e in r['new_entries']};added=[]
rel='reviews/FULL-FF3-PHASE2/regression-dispositions-v1.json';x=rs[rel]
for group in ['phase1_local','phase2_local','new']:
 for i,e in enumerate(x[group]):
  if e['id'] in seen:continue
  rec={'id':e['id'],'status':'EXACT_SCOPED_REFERENCE_LOCAL_CONTROL','source_registry':rel,'source_registry_sha256':digest(O/rel),'json_pointer':f'/{group}/{i}','entry_sha256':enc(e),'scope':'Use exact recorded model, expected outcome and review disposition. Finite certificate or negative control is not a general impossibility theorem.'};r['new_entries'].append(rec);seen.add(e['id']);added.append(e['id'])
if 'FF3-COMPACT-M-ENCODING-1' not in seen:r['new_entries'].append({'id':'FF3-COMPACT-M-ENCODING-1','status':'V2_REJECTED_V3_FRESH_GATES_PENDING','evidence':'coordinator/compact-selector-v2-rejection-v1.md','scope':'M>=max G with rational G does not ensure an exact computable G/M coin for arbitrary real M. Supply encoded rational M and charge its bits/numeric value.'})
for e in r['new_entries']:
 if e['id']=='FF-SYNTHESIS-SCOPE-1':e['status']='CORRECTED_EXACT_SCOPE_FRESH_CHALLENGE_CONFIRMED';e['review']='reviews/FRONTIER-CHALLENGE1/frontier-challenge-report-v1.md'
r['updated_at']=now;t=O/'regressions.json.tmp';t.write_text(json.dumps(r,indent=2)+'\n');t.replace(O/'regressions.json')
a={'at':now,'inherited_exact_count':203,'checks':checks,'new_exact_local_references_added':added,'local_count':len(r['new_entries']),'qualification':'Registry identity, exact reference and disposition integration only; no historical theorem promoted or203 experiments rerun.'};(O/'coordinator/regression-integrity-v1.json').write_text(json.dumps(a,indent=2)+'\n');print({'at':now,'inherited':203,'new_refs_added':len(added),'local_count':len(r['new_entries'])})
