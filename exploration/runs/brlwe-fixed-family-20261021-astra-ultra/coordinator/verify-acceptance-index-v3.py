from pathlib import Path
import json,hashlib,datetime
O=Path(__file__).resolve().parents[1];C=json.loads((O/'claims.json').read_text());by={c['id']:c for c in C['claims']};checks=[];claims=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for ver in range(1,8):
 p=O/f'coordinator/acceptance-v{ver}.json';x=json.loads(p.read_text());items=x.get('accepted_claims',[])
 for c in items:
  if not isinstance(c,dict):continue
  ident=c.get('id');ev=c.get('evidence_sha256',{})
  for rel,h in ev.items():
   q=O/rel;ok=q.exists() and sha(q)==h;checks.append({'acceptance_version':ver,'claim':ident,'path':rel,'sha256':h,'match':ok});assert ok,(ver,ident,rel)
  if ident:claims.append({'id':ident,'acceptance_version':ver,'current_status':by[ident]['status']})
 for rel,h in x.get('review_seals',{}).items():
  if not isinstance(h,str):continue
  candidates=[O/rel,O/'reviews'/rel]
  if '/' not in rel:candidates+=list((O/'reviews'/rel).glob('*.json'))
  matches=[q for q in candidates if q.is_file() and sha(q)==h];assert matches,(ver,rel,h)
  q=matches[0];checks.append({'acceptance_version':ver,'original_key':rel,'resolved_review_seal':str(q.relative_to(O)),'sha256':h,'match':True})
res={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'claim_rows':claims,'distinct_claims':len({r['id'] for r in claims}),'qualification':'Cross-version exact bytes/status reconciliation, not rerunning mathematics. Original v1 document checker failed because review-seal keys v1-v3 are labels, v4 is reviews-relative, v5+ output-relative; v2 resolves each by exact hash and retains original labels. No mathematical hash mismatch was observed.'};(O/'coordinator/acceptance-integrity-v3.json').write_text(json.dumps(res,indent=2)+'\n');print({'checks':len(checks),'distinct_accepted_claims':res['distinct_claims']})
