"""Read-only documentary integrity recheck. No mathematical experiments."""
from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

ROOT = Path('/home/nico/projects/research_projects/binaryRLWE')
OUT = ROOT / 'exploration/runs/brlwe-fixed-family-20261021-astra-ultra'
HERE = OUT / 'reviews/DELIVERY-AUDIT1'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def obj(p): return json.loads(p.read_text())
def entry_hash(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
def pointer(x, p):
    for k in p.split('/')[1:]:
        k = k.replace('~1','/').replace('~0','~')
        x = x[int(k)] if isinstance(x,list) else x[k]
    return x

old = obj(HERE/'documentary-integrity-v1.json')
checks=[]
def check(path, expected, source, base=OUT):
    p = base/path
    actual = digest(p) if p.is_file() else None
    checks.append(dict(path=str(p.relative_to(ROOT)), expected=expected,
                       actual=actual, match=actual==expected, source=source))
for c in old['acceptance_checks']['details']:
    check(c['path'],c['expected'],'v1 evidence unchanged check')
a7=obj(OUT/'coordinator/acceptance-v7.json')
for c in a7['review_integrity_checks']:
    check(c['file'],c['sha256'],'acceptance-v7 exact sealed evidence')
for p,h in a7['review_seals'].items(): check(p,h,'acceptance-v7 review seal')
for c in a7['accepted_claims']:
    for p,h in c['evidence_sha256'].items(): check(p,h,'acceptance-v7 statement/proof')

claims=obj(OUT/'claims.json')['claims']; by_id={c['id']:c for c in claims}
graph=obj(OUT/'claim-dependencies.json'); nodes={n['id']:n for n in graph['nodes']}
graph_errors=[]
for n in graph['nodes']:
    c=by_id.get(n['id'])
    if not c or c['status'] != n['status']: graph_errors.append(['status',n['id']])
    for kind in ['statement','proof']:
        if n.get(kind) and n.get(kind+'_sha256'):
            check(n[kind],n[kind+'_sha256'],'current graph '+n['id'])
            if c and (c.get(kind)!=n[kind] or c.get('evidence_sha256',{}).get(n[kind])!=n[kind+'_sha256']):
                graph_errors.append(['claim/graph byte binding',n['id'],kind])
adj={k:[] for k in nodes}
for e in graph['edges']:
    a,b=e['from'],e['requires']
    if a not in nodes or b not in nodes: graph_errors.append(['missing node',a,b]); continue
    adj[a].append(b)
    if nodes[a]['status'].startswith('ACCEPTED') and not nodes[b]['status'].startswith('ACCEPTED'):
        graph_errors.append(['accepted dependency gap',a,b])
    if e['status']!=nodes[b]['status']: graph_errors.append(['edge status',a,b])
visiting=set(); visited=set()
def walk(k):
    if k in visiting: graph_errors.append(['cycle',k]);return
    if k in visited:return
    visiting.add(k)
    for j in adj[k]:walk(j)
    visiting.remove(k);visited.add(k)
for k in nodes:walk(k)

reg=obj(OUT/'regressions.json'); entries=reg['inherited_entries']; rchecks=[]; dchecks=[]
for e in entries:
    p=ROOT/e['source_registry']; x=pointer(obj(p),e['json_pointer'])
    rchecks.append(dict(id=e['id'],source_registry_match=digest(p)==e['source_registry_sha256'],
                        entry_hash_match=entry_hash(x)==e['entry_sha256'],id_match=x['id']==e['id']))
    for d in e['exact_current_dispositions']:
        p=OUT/d['registry']; x=pointer(obj(p),d['json_pointer'])
        dchecks.append(dict(id=e['id'],registry=d['registry'],registry_hash_match=digest(p)==d['registry_sha256'],
                            entry_hash_match=entry_hash(x)==d['entry_sha256'],id_match=x['id']==e['id']))
def bad(x): return any(v is False for v in x.values())
result=dict(at=datetime.now(timezone.utc).isoformat(),scope='Read-only documentary recheck, not theorem recertification or a finite mathematical experiment',
            prior_report_sha256=digest(HERE/'documentary-integrity-v1.json'),
            current_inputs={f:digest(OUT/f) for f in ['claims.json','claim-dependencies.json','regressions.json','coordinator/acceptance-v7.json']},
            hash_checks=dict(count=len(checks),unique_paths=len({c['path'] for c in checks}),failures=[c for c in checks if not c['match']],details=checks),
            claim_graph=dict(claim_count=len(claims),node_count=len(nodes),edge_count=len(graph['edges']),accepted_count=sum(c['status'].startswith('ACCEPTED') for c in claims),errors=graph_errors,recorded_gaps=graph['accepted_dependency_gaps']),
            regressions=dict(count=len(entries),unique_ids=len({e['id'] for e in entries}),local_control_count=len(reg['new_entries']),reference_failures=[c for c in rchecks if bad(c)],disposition_count=len(dchecks),disposition_failures=[c for c in dchecks if bad(c)],details=rchecks,dispositions=dchecks))
(HERE/'documentary-integrity-v2.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:({a:b for a,b in v.items() if a not in ('details','dispositions')} if isinstance(v,dict) else v) for k,v in result.items()},indent=2))
