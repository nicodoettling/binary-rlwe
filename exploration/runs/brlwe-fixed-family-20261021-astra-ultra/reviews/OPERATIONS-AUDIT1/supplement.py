"""Preserve additional operational records, without changing the first snapshot."""
import datetime as dt, hashlib, json, pathlib, re
ROOT=pathlib.Path('/home/nico/projects/research_projects/binaryRLWE')
OUT=ROOT/'exploration/runs/brlwe-fixed-family-20261021-astra-ultra'
HERE=OUT/'reviews/OPERATIONS-AUDIT1'
now=dt.datetime.now(dt.timezone.utc).isoformat()
def h(b): return hashlib.sha256(b).hexdigest()
def put(n,x): (HERE/n).write_text(json.dumps(x,indent=2)+'\n')
original=json.loads((HERE/'input-manifest.json').read_text())
already={x['source'] for x in original['inputs']}; added=[]; resources=[]
extra={'worker-status.json','coordinator/final-draft-v2.md','experiments/symmetrized-rank-fv2-summary.json',
 'reviews/BLIND-SV1/experiment-01.py','reviews/BLIND-FF2/finite-models-v1.py',
 'reviews/BLIND-RESOURCE4/exact-audit-v1.py','reviews/BLIND-SV1/experiment-01-result.json'}
for p in OUT.rglob('*'):
 if not p.is_file(): continue
 rel=p.relative_to(OUT)
 if {'inputs','preserved','OPERATIONS-AUDIT1','allowed-input'}.intersection(rel.parts): continue
 selected=(str(rel) in extra or
   (p.suffix=='.md' and any(x in p.name for x in ['registration','preregistration'])) or
   (p.suffix=='.json' and any(x in p.name for x in ['-receipt','execution','-exit','-end.json'])) or
   (p.suffix in ['.time','.txt'] and ('time' in p.name or 'stderr' in p.name)))
 if not selected or p.stat().st_size>150000: continue
 b=p.read_bytes()
 if str(p) not in already:
  dest=HERE/'supplement-inputs'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
  added.append({'source':str(p),'snapshot':str(dest.relative_to(HERE)),'bytes':len(b),'sha256':h(b),'read_at':now})
 s=b.decode(errors='replace')
 if 'Maximum resident set size (kbytes)' in s:
  record={'path':str(rel)}
  for k,pat in [('elapsed',r'Elapsed \(wall clock\) time \(h:mm:ss or m:ss\):\s*(\S+)'),('peak_RSS_KiB',r'Maximum resident set size \(kbytes\):\s*(\d+)'),('exit',r'Exit status:\s*(\d+)'),('signal',r'Command terminated by signal (\d+)')]:
   m=re.search(pat,s)
   if m:record[k]=m.group(1)
  resources.append(record)

settings=[]; prefixes=[]; post=[]
sessions=json.loads((HERE/'selected-session-metadata.json').read_text())['sessions']
for session in sessions:
 p=pathlib.Path(session['path']);raw=p.read_bytes()
 prefixes.append({'path':str(p),'read_at':now,'prefix_bytes':len(raw),'prefix_sha256':h(raw)})
 for lineno,line in enumerate(raw.splitlines(),1):
  try:x=json.loads(line)
  except ValueError:continue
  y=x.get('payload',{})
  if x.get('type')=='event_msg' and y.get('type')=='thread_settings_applied':
   z=y.get('thread_settings',{})
   settings.append({'path':str(p),'line':lineno,'agent':session['agent'],'timestamp':x['timestamp'],
    'selected_fields':{k:z.get(k) for k in ['model','service_tier','approval_policy','reasoning_effort']}})
  if session['agent']=='/root' and x.get('type')=='response_item' and y.get('type')=='function_call' and y.get('name') in ['spawn_agent','followup_task'] and x['timestamp']>'2026-10-21T21:18:10.636448Z':
   a=json.loads(y['arguments']);msg=a.get('message','')
   post.append({'timestamp':x['timestamp'],'tool':y['name'],'task':a.get('task_name',a.get('target')),
    'stored_assignment_sha256':h(msg.encode()),'assignment_payload':'OMITTED; stored tool message may be encrypted; use preserved plaintext assignment files for scope',
    'field_names':list(a)})
put('supplement-manifest.json',{'at':now,'inputs':added,'selected_session_prefixes':prefixes})
put('selected-thread-settings.json',{'at':now,'scope':'Actual local configuration settings only; no billing observation. Only sessions with these events supply explicit tier fields.','records':settings})
put('post-cutoff-assignment-metadata.json',{'at':now,'scope':'Selected task names, stored argument hashes and tool fields only. No message content or ciphertext retained.','records':post})
put('additional-resource-metadata.json',{'at':now,'scope':'Additional GNU time records in stderr/time files, supplementary to first snapshot. Exit status 0 does not override a recorded terminating signal.','records':resources})
contract=['final.md','claims.json','reconciliation.md','regressions.json','reduction-attempts.md','parameter-table.md','source-comparison.md','progress.md','resume.md','programme-decisions.md']
put('delivery-presence-at-audit.json',{'at':now,'final_receipts_not_due':True,'paths':[{ 'path':x,'exists':(OUT/x).exists()} for x in contract],
 'qualification':'Presence is not content acceptance; the final package is still in preparation. Shutdown and final counters have future deadlines.'})
print(json.dumps({'at':now,'additional_inputs':len(added),'settings_events':len(settings),'settings_agents':sorted({x['agent'] for x in settings}),
 'post_cutoff_assignments':post,'additional_resource_receipts':len(resources)},indent=2))
