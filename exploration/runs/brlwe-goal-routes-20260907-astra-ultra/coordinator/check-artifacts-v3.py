"""Saved-artifact consistency only; never certifies mathematical truth."""
from pathlib import Path
import json, hashlib, re, datetime, subprocess, sys

r=Path(__file__).resolve().parents[1]
checks=[]
def check(name,ok,detail=None):
    checks.append({'name':name,'passed':bool(ok),'detail':detail})
required=['final.md','resume.md','progress.md','claims.json','claim-history.jsonl','reconciliation.md','agents.json','regressions.json','parameter-table.md','source-comparison.md','experiments/registry.json','goal-created.json','coordinator-checkpoint.json','selection.md']
check('required nonempty outputs',all((r/f).is_file() and (r/f).stat().st_size for f in required),required)
json_errors=[]
for f in r.rglob('*.json'):
    if 'coordinator-checkpoints' in f.parts: continue
    try: json.loads(f.read_text())
    except Exception as e: json_errors.append({'path':str(f.relative_to(r)),'error':str(e)})
check('JSON parses',not json_errors,json_errors)
history_errors=[]
for i,line in enumerate((r/'claim-history.jsonl').read_text().splitlines(),1):
    try: json.loads(line)
    except Exception as e: history_errors.append([i,str(e)])
check('append-only claim history parses',not history_errors,history_errors)
cl=json.loads((r/'claims.json').read_text()); claims=cl.get('claims',[])
ids={c['id']:c for c in claims}
check('unique current claim IDs',len(ids)==len(claims))
dep_errors=[]
for c in claims:
    for d in c.get('dependencies',[]):
        if not isinstance(d,dict) or d.get('id') not in ids or ids[d['id']]['version']!=d.get('version'):
            dep_errors.append([c['id'],d])
        elif c['status']=='ACCEPTED' and ids[d['id']]['status']!='ACCEPTED':
            dep_errors.append([c['id'],'accepted depends on nonaccepted',d])
check('current dependency versions and accepted closure',not dep_errors,dep_errors)
visiting=set();visited=set();cycles=[]
def visit(id_):
    if id_ in visiting: cycles.append(id_); return
    if id_ in visited: return
    visiting.add(id_)
    for d in ids[id_].get('dependencies',[]):
        if isinstance(d,dict) and d.get('id') in ids: visit(d['id'])
    visiting.remove(id_);visited.add(id_)
for id_ in ids:visit(id_)
check('acyclic current graph',not cycles,cycles)
missing_proofs=[c['proof'] for c in claims if c.get('proof') and not (r/c['proof']).is_file()]
check('current claim proof paths',not missing_proofs,missing_proofs)
review_errors=[]
for c in claims:
    if c.get('proof_sha256') and hashlib.sha256((r/c['proof']).read_bytes()).hexdigest()!=c['proof_sha256']:review_errors.append([c['id'],'proof hash'])
    for rev in c.get('reviews',[]):
        if isinstance(rev,dict) and 'path' in rev and 'sha256' in rev:
            p=r/rev['path']
            if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=rev['sha256']:review_errors.append([c['id'],rev['path']])
check('claim proof and review hash pointers',not review_errors,review_errors)
manifest=r/'coordinator/frozen-evidence.json'
hash_errors=[]
if manifest.exists():
    evidence=json.loads(manifest.read_text())
    for x in evidence['files']:
        f=r/x['path']
        if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=x['sha256']:hash_errors.append(x['path'])
    check('frozen proof/review/input hashes',not hash_errors,{'files':len(evidence['files']),'failures':hash_errors})
else:check('frozen proof/review manifest exists',False,'May be absent during interim review; mandatory at final delivery')
historical=json.loads((r/'imports/historical-file-index.json').read_text())['files'];changed=[]
for x in historical:
    p=Path(x['path'])
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:changed.append(x['path'])
check('all imported historical originals unchanged',not changed,{'files':len(historical),'changes':changed})
bad_links=[]
for name in ['final.md','resume.md','progress.md','reconciliation.md','parameter-table.md','source-comparison.md']:
    p=r/name
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        target=target.strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):continue
        clean=target.split('#',1)[0]
        if clean and not (p.parent/clean).exists():bad_links.append([name,target])
check('core report local Markdown links',not bad_links,bad_links)
intake=json.loads((r/'intake-verification.json').read_text())
root=r.parents[2]
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
diff=subprocess.check_output(['git','diff','--','HANDOFF.md'],cwd=root,text=True)
check('original Git HEAD unchanged',head==intake['git_before']['head'],head)
observation=json.loads((r/'coordinator/metadata-change-observation-v1.json').read_text())
check('externally updated HANDOFF matches preserved observation',diff==observation['current_handoff_git_diff'] and hashlib.sha256((root/'HANDOFF.md').read_bytes()).hexdigest()==observation['current_handoff_sha256'])
check('externally updated config matches preserved observation',hashlib.sha256((root/'exploration/goal-routes-20260907/run-config.json').read_bytes()).hexdigest()==observation['current_config_sha256'])
check('external metadata preserves exact authorization and cap identity',all(observation['checks'].values()),observation['checks'])
receipt=json.loads((r/'goal-created.json').read_text())['goal'];config=json.loads((root/'exploration/goal-routes-20260907/run-config.json').read_text())
check('goal exact objective/session',receipt['objective']==config['goal_objective'] and receipt['threadId']==intake['worker']['codex_session_id'])
check('launch-specific approval',config['launch_authorized'] and config['launch_confirmation_received'] and bool(config['launch_authorization']['user_message']))
agent=json.loads((r/'agents.json').read_text());active=[x['id'] for x in agent['workers'] if x['status']=='running']
check('recorded active worker ceiling',len(active)<=3,active)
if (r/'shutdown.json').exists():
    shut=json.loads((r/'shutdown.json').read_text())
    check('shutdown goal state explicitly recorded','goal_state' in shut)
    check('shutdown has no known active workers',not active,active)
expected_accepted={'SOURCE-2','PRIME-POLY','NC-RECT','A-GUESS','MASK-TAIL','SAMP-E','A-FINITE','A-PPT'}
check('final selected accepted graph',cl.get('global_new_claim_acceptance') is True and all(ids[k]['status']=='ACCEPTED' for k in expected_accepted),{k:ids[k]['status'] for k in expected_accepted})
repair=json.loads((r/'coordinator/A-PPT-ledger-v2.json').read_text())
fields=['statement','version','proof','dependencies','explicit_computational_hypothesis','scope_repair_only']
check('accepted A-PPT exact repaired load-bearing fields',all(ids['A-PPT'].get(k)==repair.get(k) for k in fields),fields)
check('source hardness remains explicitly assumed',ids['SOURCE-2'].get('computational_hardness_status')=='ASSUMED_NOT_PROVED')
check('unreviewed B/C remain provisional',all(ids[k]['status']=='PROVISIONAL' for k in ['B-SPLIT','C-LARGE-Q','C-SPAN']))
reg=json.loads((r/'regressions.json').read_text());hist=json.loads((r/'imports/latest-regressions.json').read_text())
check('complete historical regression applicability graph',{x['id'] for x in hist['controls']}=={x['id'] for x in reg['historical_application']} and all(x['current_application_rows'] for x in reg['historical_application']),len(reg['historical_application']))
experiments=json.loads((r/'experiments/registry.json').read_text())
check('no known unfinished experiments',all(x.get('status')=='completed' and x.get('slot_released') is True for x in experiments['experiments']))
check('experiment evidence paths',all((r/p).is_file() for p in experiments['evidence_paths']))
check('fresh repair and delivery reports in accepted claim',{'RP1','RD1'}.issubset({v.get('reviewer') for v in ids['A-PPT'].get('reviews',[])}))
if (r/'goal-final.json').exists():
    last=json.loads((r/'goal-final.json').read_text())['goal']
    check('final native goal receipt matches identity and completion',last['threadId']==receipt['threadId'] and last['objective']==receipt['objective'] and last['status']=='complete')
    if (r/'shutdown.json').exists():
        shut=json.loads((r/'shutdown.json').read_text());check('shutdown mirrors exact final goal state',shut['goal_state']==last)
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Saved-artifact consistency and preservation only. Mathematical certification comes from claim-specific proof/review reconciliation; process exit remains cap-helper evidence.','all_passed':all(x['passed'] for x in checks),'checks':checks}
dest=r/'coordinator'/(sys.argv[1] if len(sys.argv)>1 else 'artifact-check-interim.json')
if dest.exists():raise RuntimeError('Use a new output name to preserve earlier audit')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'output':str(dest),'all_passed':out['all_passed'],'checks':len(checks),'failed':[x['name'] for x in checks if not x['passed']]},indent=2))
