"""Read-only documentary checks; writes confined to this audit directory."""
import collections, datetime as dt, hashlib, json, pathlib, re

ROOT=pathlib.Path('/home/nico/projects/research_projects/binaryRLWE')
OUT=ROOT/'exploration/runs/brlwe-fixed-family-20261021-astra-ultra'
HERE=OUT/'reviews/OPERATIONS-AUDIT1'
THREAD='01a15f93-e6bd-7fd2-953c-80af410308a1'
NOW=dt.datetime.now(dt.timezone.utc).isoformat()
def digest(b): return hashlib.sha256(b).hexdigest()
def put(name,x):
 p=HERE/name; p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(x,indent=2)+'\n')
def iso(s): return dt.datetime.fromisoformat(s.replace('Z','+00:00'))

inputs=[]
def snapshot(p,tag=None):
 b=p.read_bytes(); rel=tag or str(p.relative_to(ROOT))
 dest=HERE/'inputs'/rel; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(b)
 inputs.append({'source':str(p),'snapshot':str(dest.relative_to(HERE)), 'bytes':len(b),'sha256':digest(b),'read_at':NOW})
 return json.loads(b) if p.suffix=='.json' else b.decode()

base=['launcher-run.json','run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json',
 'coordinator/deadlines.json','coordinator/runtime-verification.json','coordinator/spawn-receipts-all-v5.json',
 'coordinator/protected-period-compliance.json','coordinator/gate-045-nonterminal.json',
 'coordinator/allocation-090-nonterminal.json','coordinator/allocation-150-nonterminal.json',
 'coordinator/goal-creation-receipt.json','coordinator/goal-initial-receipt.json',
 'coordinator/native-usage-delta.json','experiments/registry.json','experiments/evidence-index-v1.json',
 'programme-decisions.md','progress.md','coordinator/programme-v3.md','coordinator/frontier-challenge-replies-v3.md',
 'coordinator/final-draft-v1.md']
data={p:snapshot(OUT/p) for p in base if (OUT/p).exists()}
snapshot(ROOT/'exploration/fixed-family-20261021/PLAN.md')
cap=data['run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json']
start=iso(cap['started_at'])
checkpoints=[]; goals=[]
for p in sorted((OUT/'coordinator/checkpoints').glob('*.json')):
 x=snapshot(p); n=int(p.name.split('-')[0]); stamp=x.get('at',x.get('recorded_at'))
 elapsed=(iso(stamp)-start).total_seconds()
 checkpoints.append({'path':str(p.relative_to(OUT)),'number':n,'at':stamp,'utc_elapsed_seconds':elapsed,
  'recorded_elapsed_seconds':x.get('service_elapsed_seconds'),'scheduled_offset_seconds':n*600,
  'lateness_seconds':elapsed-n*600,'goal_status':x.get('goal_status'),'phase':x.get('phase')})
for p in sorted((OUT/'coordinator').glob('goal-checkpoint-*.json')):
 x=snapshot(p); g=x.get('goal') or {}
 goals.append({'path':str(p.relative_to(OUT)), **{k:g.get(k) for k in ['threadId','status','tokensUsed','timeUsedSeconds','createdAt','updatedAt']},
  'token_budget_keys':[k for k in g if 'budget' in k.lower()]})
gates=[]
for rel,offset in [('coordinator/gate-045-nonterminal.json',2700),('coordinator/allocation-090-nonterminal.json',5400),('coordinator/allocation-150-nonterminal.json',9000)]:
 x=data[rel]; stamp=x.get('at',x.get('recorded_at')); elapsed=(iso(stamp)-start).total_seconds()
 gates.append({'path':rel,'at':stamp,'scheduled_offset_seconds':offset,'lateness_seconds':elapsed-offset,'scientific_termination':x['scientific_termination']})
put('clock-and-goal-checks.json',{'at':NOW,'service_activation':cap['started_at'],'activation_monotonic':cap['started_monotonic'],
 'cap_snapshot_last_updated_at':cap['updated_at'],'checkpoints':checkpoints,'gates':gates,'goals':goals,
 'max_clock_difference_seconds':max(abs(x['utc_elapsed_seconds']-x['recorded_elapsed_seconds']) for x in checkpoints),
 'adjacent_checkpoint_intervals_seconds':[round(checkpoints[i]['utc_elapsed_seconds']-checkpoints[i-1]['utc_elapsed_seconds'],6) for i in range(1,len(checkpoints))]})

index=data['experiments/evidence-index-v1.json']; mismatches=[]; missing=[]
for a in index['artifacts']:
 p=OUT/a['path']
 if not p.exists(): missing.append(a['path']); continue
 b=p.read_bytes()
 if digest(b)!=a['sha256'] or len(b)!=a['bytes']: mismatches.append({'path':a['path'],'recorded_sha256':a['sha256'],'current_sha256':digest(b),'recorded_bytes':a['bytes'],'current_bytes':len(b)})
regs=[]; resource_files=[]
for p in OUT.rglob('*'):
 if not p.is_file(): continue
 parts=p.relative_to(OUT).parts
 if {'inputs','preserved','OPERATIONS-AUDIT1'}.intersection(parts): continue
 if p.suffix=='.json' and ('registration' in p.name or 'preregistration' in p.name):
  x=snapshot(p); regs.append({'path':str(p.relative_to(OUT)),'data':x})
 elif (('resource' in p.name and p.suffix in ['.txt','.resources']) or p.suffix=='.resources' or 'cleanup' in p.name):
  if p.stat().st_size<100000:
   b=snapshot(p); resource_files.append({'path':str(p.relative_to(OUT)),'data':b})
put('experiment-documentary-checks.json',{'at':NOW,'index_at':index['at'],'indexed_artifacts':len(index['artifacts']),
 'missing_indexed_paths':missing,'changed_indexed_paths':mismatches,'registrations':regs,'resource_files':resource_files})

sessions=[]; tool_records=[]; root_calls={}; root_outputs={}; lifecycle=[]
for p in pathlib.Path('/home/nico/.codex/sessions/2026/10/21').glob('rollout-*.jsonl'):
 with p.open() as f:
  try: head=json.loads(next(f))
  except (ValueError,StopIteration): continue
 h=head.get('payload',{}); sid=h.get('id'); source=h.get('source',{})
 spawn=(source.get('subagent',{}).get('thread_spawn',{}) if isinstance(source,dict) else {})
 if sid!=THREAD and spawn.get('parent_thread_id')!=THREAD: continue
 # Read a fixed prefix and retain only approved metadata; never copy raw sessions.
 raw=p.read_bytes(); turns=[]; counts=collections.Counter(); evs=[]
 agent=spawn.get('agent_path','/root')
 for lineno,line in enumerate(raw.splitlines(),1):
  try: x=json.loads(line)
  except ValueError: continue
  y=x.get('payload',{}); typ=x.get('type'); kind=y.get('type'); name=y.get('name')
  if typ=='turn_context':
   turns.append({'timestamp':x['timestamp'],**{k:y.get(k) for k in ['model','effort','approval_policy','sandbox_policy']},'service_tier_present':'service_tier' in y})
  if typ=='event_msg' and kind in ['task_started','task_complete','task_completed','turn_aborted']:
   rec={'timestamp':x['timestamp'],'kind':kind,'turn_id':y.get('turn_id'),'agent':agent}
   evs.append(rec); lifecycle.append(rec)
  if typ=='response_item' and kind=='function_call':
   counts[name]+=1
   if agent=='/root' and name in ['spawn_agent','followup_task','interrupt_agent','list_agents']:
    args=json.loads(y['arguments']); selected={k:v for k,v in args.items() if k in ['task_name','model','reasoning_effort','fork_turns','target']}
    root_calls[y['call_id']]={'timestamp':x['timestamp'],'line':lineno,'tool':name,'selected_arguments':selected,'argument_field_names':list(args)}
  if typ=='response_item' and kind=='function_call_output' and agent=='/root':
   root_outputs[y['call_id']]=y.get('output')
  if typ=='response_item' and kind=='custom_tool_call':
   src=y.get('input',''); nested=re.findall(r'\btools\.([a-zA-Z0-9_]+)\s*\(',src)
   for n in nested: counts[n]+=1
   for n in ['create_goal','update_goal']:
    if n in nested:
     tool_records.append({'timestamp':x['timestamp'],'agent':agent,'line':lineno,'tool':n,'input_sha256':digest(src.encode()),
      'token_budget_field_in_call':'token_budget' in src,'status_arguments':re.findall(r'status\s*:\s*[\"\']([^\"\']+)',src)})
 sessions.append({'path':str(p),'agent':agent,'thread_id':sid,'parent_thread_id':spawn.get('parent_thread_id'),
  'read_at':NOW,'read_prefix_bytes':len(raw),'prefix_sha256':digest(raw),'turn_configurations':turns,'lifecycle':evs,'tool_name_counts':dict(counts)})
for cid,rec in root_calls.items():
 rec['call_id']=cid; rec['actual_return']=root_outputs.get(cid,'NOT_PRESENT_IN_SNAPSHOT')
put('selected-session-metadata.json',{'at':NOW,'qualification':'Selected metadata only; no raw payload, instructions, ciphertext, secret values, or backend billing telemetry retained.',
 'sessions':sessions,'goal_mutation_calls':tool_records,'actual_coordination_receipts':list(root_calls.values())})

events=sorted(lifecycle,key=lambda x:(x['timestamp'],0 if x['kind']!='task_started' else 1)); running=set(); max_active=0; intervals=[]; anomalies=[]
for e in events:
 if e['agent']=='/root': continue
 if e['kind']=='task_started':
  if e['agent'] in running: anomalies.append({'kind':'start_while_running','event':e})
  running.add(e['agent'])
 else: running.discard(e['agent'])
 max_active=max(max_active,len(running))
 intervals.append({**e,'active_child_count':len(running),'active_children':sorted(running)})
put('concurrency-checks.json',{'at':NOW,'method':'Union of child task_started/task_complete/turn_aborted lifecycle timestamps, current prefix snapshots. A documentary reconstruction, not backend scheduler or process observation.',
 'maximum_observed_active_children':max_active,'active_children_at_snapshot':sorted(running),'anomalies':anomalies,'events':intervals})
put('input-manifest.json',{'at':NOW,'scope':'Copied documentary inputs and selected-session prefix digests. Live files can advance after this snapshot.','inputs':inputs})
print(json.dumps({'at':NOW,'copied_inputs':len(inputs),'session_count':len(sessions),'root_coordination_receipts':len(root_calls),'goal_mutations':tool_records,
 'max_active_children':max_active,'active_at_snapshot':sorted(running),'lifecycle_anomalies':len(anomalies),
 'index_artifacts':len(index['artifacts']),'index_missing':len(missing),'index_changed':len(mismatches),'registrations':len(regs),'resource_receipts':len(resource_files)},indent=2))
