"""Assemble actual final receipts after the 295-minute checkpoint.

This script does not change native goal/process/service state or run experiments.
It may run once, before the original graceful deadline, using actual saved tools.
"""
from pathlib import Path
import datetime, hashlib, json, time, re

O = Path(__file__).resolve().parents[1]
def read(rel): return json.loads((O/rel).read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def atom(rel, obj):
    p = O/rel; t = p.with_suffix(p.suffix+'.tmp')
    t.write_text(json.dumps(obj, indent=2)+'\n'); t.replace(p)
def text(rel, value):
    p = O/rel; t = p.with_suffix(p.suffix+'.tmp')
    t.write_text(value); t.replace(p)
def dt(s): return datetime.datetime.fromisoformat(s.replace('Z','+00:00'))

cap = read('run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json')
now = datetime.datetime.now(datetime.timezone.utc)
elapsed = time.monotonic()-cap['started_monotonic']
assert 295*60 <= elapsed < 17935, 'Only original final closeout window'
assert now < dt(cap['graceful_shutdown_at'])
assert not (O/'coordinator/termination-certificate.json').exists(), 'Final delivery already recorded'
checkpoint = read('coordinator/checkpoints/030-closeout-295-minute.json')
worker_stop = read('coordinator/worker-experiment-stop-receipt.json')
agents = read('coordinator/final-agent-observation.json')
proc = read('coordinator/final-process-observation.json')
latest = read('coordinator/goal-final-receipt.json')
goal_observation = read('coordinator/goal-final-observation.json')
baseline = read('coordinator/goal-creation-receipt.json')
g, b = latest['goal'], baseline['goal']
assert g['threadId']==b['threadId'] and g['objective']==b['objective'] and g['status']=='active'
assert b['tokensUsed']==b['timeUsedSeconds']==0
assert worker_stop['known_active_experiments']==0 and worker_stop['active_child_count']==0
assert agents['active_child_count']==0

# Preserve the independently audited mathematical section byte for byte.
draft = (O/'coordinator/final-draft-v4.md').read_text()
report = (O/'final.md').read_text()
math = draft[draft.index('## What changed beyond'):draft.index('## Runtime and shutdown accounting')]
assert math in report
assert sha(O/'coordinator/final-draft-v4.md')=='e0bebf18e96b8dd1415838822ba2d9c2012115d13face97c2dc9c0d8f47ae870'

# Check the final original-evidence snapshot after all review seals.
index = read('experiments/evidence-index-v2.json')
for entry in index['artifacts']:
    p=O/entry['path']; assert sha(p)==entry['sha256'], entry['path']
    assert p.stat().st_size==entry['bytes'], entry['path']

usage = {'at':now.isoformat(), 'measurement_observation':goal_observation,
         'baseline_receipt':'coordinator/goal-creation-receipt.json',
         'baseline_tokens':b['tokensUsed'], 'baseline_time_seconds':b['timeUsedSeconds'],
         'latest_goal':latest, 'tokens_delta':g['tokensUsed']-b['tokensUsed'],
         'time_delta_seconds':g['timeUsedSeconds']-b['timeUsedSeconds'],
         'interpretation':'Actual native counters at the saved pre-delivery observation, not weekly quota or backend billing. Final receipt writing and response occur after this observation and are not retroactively included. Native goal clock starts after service activation.'}
atom('coordinator/native-usage-delta.json', usage)
atom('coordinator/native-usage-final.json', usage)

cadence=[]
origin=dt(cap['started_at'])
for p in sorted((O/'coordinator/checkpoints').glob('*.json')):
    c=json.loads(p.read_text()); number=int(p.name.split('-')[0])
    if number==0: continue
    minutes=295 if number==30 else number*10
    scheduled=origin+datetime.timedelta(minutes=minutes)
    cadence.append({'path':str(p.relative_to(O)), 'at':c['at'], 'scheduled_at':scheduled.isoformat(),
                    'lateness_seconds':(dt(c['at'])-scheduled).total_seconds()})
cadence.sort(key=lambda x:x['at'])
gaps=[{'from':a['path'],'to':z['path'],'seconds':(dt(z['at'])-dt(a['at'])).total_seconds()} for a,z in zip(cadence,cadence[1:])]
cadence_report={'at':now.isoformat(),'checkpoints':cadence,'maximum_lateness':max(cadence,key=lambda x:x['lateness_seconds']),
                'maximum_interval':max(gaps,key=lambda x:x['seconds']),
                'early_records':[x for x in cadence if x['lateness_seconds']<0],
                'qualification':'Actual timestamps preserved. Ten-minute target was not met exactly at all intervals; final checkpoint is scheduled at295 minutes, five minutes after290.'}
atom('coordinator/checkpoint-cadence-final.json',cadence_report)
dev=read('coordinator/operational-deviations-v2.json');dev['at']=now.isoformat()
dev['final_cadence']='coordinator/checkpoint-cadence-final.json';dev['checkpoint_cadence']['final_cadence_pending']=False
dev['live_cap_observation_limit']=proc['limits'];dev['final_process_observation']='coordinator/final-process-observation.json'
atom('coordinator/operational-deviations-v3.json',dev)

shutdown={'at':now.isoformat(),'service_elapsed_seconds':elapsed,
          'category':'OBSERVED_LOCAL_CLOSEOUT_BEFORE_EXTERNAL_GRACEFUL_DEADLINE',
          'worker_stop':'coordinator/worker-experiment-stop-receipt.json',
          'latest_agents':'coordinator/final-agent-observation.json',
          'visible_process_observation':'coordinator/final-process-observation.json',
          'known_active_child_agents':0,'known_active_experiments':0,
          'known_tool_exec_sessions_pending':0,
          'scope':'All coordinator-owned experiment calls returned and remaining workers reported completed. The final observer sees only its sandbox namespace; enclosing service and full host descendants are not visible. No host-wide cleanup certificate is claimed.',
          'systemd_live_query':proc['systemd_live_query'],
          'cap_cached_state':cap['state'],'cap_updated_at':cap['updated_at'],
          'scheduled_graceful_at':cap['graceful_shutdown_at'],'scheduled_kill_at':cap['scheduled_kill_at'],'hard_deadline_at':cap['hard_deadline_at'],
          'actual_external_graceful_observed':False,'actual_external_hard_kill_observed':False,
          'no_restart_extension_or_successor':True,'goal_state':'active unresolved; not mutated for delivery or cap'}
atom('coordinator/shutdown-receipt.json',shutdown)

decision=f'''\n\n{now.isoformat()} — Capped-run delivery closeout. The 295-minute checkpoint and actual worker/experiment-stop observation are saved. M-REVIEW-v1's bounded integration/delivery deliverable is achieved; this planning status does not certify FF or the native mathematical goal. All 28 accepted auxiliary/source gates are reconciled. FF remains OPEN, source classification is substantive at the inherited radius, and hardness is NOT ESTABLISHED. The fresh challenge leaves material routes open, so exhaustion is rejected. All future priorities remain HOLD, no new entry artifact or successor is authorized. Native goal remains ACTIVE; native token delta {usage['tokens_delta']} at the saved final observation. Local cleanup evidence is scoped to visible processes/completed tools and worker reports; future external shutdown is unobserved.\n'''
with (O/'programme-decisions.md').open('a') as f:f.write(decision)
prior=(O/'coordinator/programme-v4.md').read_text()
future=prior[prior.index('## Conditional future priority1'):prior.index('\n\n\nReview-status update')]
programme=f'''# Evidence-linked programme reconciliation v5

Final bounded-run reconciliation at {now.isoformat()}. Versions 1–4 are preserved. This programme remains within OUTPUT and does not authorize another run. Exact claims and acceptance records, not planning labels, determine mathematical status.

## M-REVIEW-v1 outcome

Planning deliverable achieved: the bounded integration, independent delivery/operations audits, exact acceptance/dependency/regression reconciliation and final evidence/usage/observed-closeout records are delivered. See ../programme-decisions.md, ../final.md, final-audit-integrity-v1.json, regression-integrity-v2.json, acceptance-integrity-v3.json and shutdown-receipt.json. No theorem statement, objective or success criterion was weakened to achieve this documentation milestone.

The mathematical result is partial. The inherited sigma0 >= 8 k0 n(n/2+2)/epsilon_* restriction remains unresolved for the fixed target quantifier order. Twenty-eight auxiliary/source claims are accepted at exact scopes. Substantive ordinary-basis algorithms classify regimes at the inherited radius; no new FF-delivered radius or established source-hardness connection exists. The native goal remains active and unresolved. Scientific exhaustion is rejected by the fresh challenge and evidence-backed replies.

All remaining routes below are HOLD and unlaunched. They require new authorization and their named entry artifacts; no capped-run continuation, successor or automatic escalation follows this delivery.

'''+future
text('coordinator/programme-v5.md',programme)

report=report.replace('Mathematical content follows the delivery-audited draft v4. Exact statements and acceptance records control scope. Final operational closeout is pending the scheduled checkpoints; this is not a declaration of scientific achievement or exhaustion.',
    f'Final bounded-run delivery at {now.isoformat()}. Mathematical content follows the delivery-audited draft v4 without changes. Exact statements and acceptance records control scope. This is a capped package delivery, not scientific achievement or exhaustion.')
report=report.replace('| Bounded package | Final operational closeout pending within the original cap. |','| Bounded package | **DELIVERED within the original cap**, with recorded operational exceptions and observed-cleanup limits. |')
report=report.replace('(coordinator/operational-deviations-v2.json)','(coordinator/operational-deviations-v3.json)')
report=report.replace('Final worker-stop, goal/usage, checkpoint and observed cleanup receipts will be bound here at the scheduled closeout. The unresolved mathematical goal must remain active. After terminal delivery or cap, stop scientific work; no automatic successor.',
    f'''Final native usage is **{usage['tokens_delta']:,} tokens** and **{usage['time_delta_seconds']:,} native goal seconds** above the zero baseline, at the saved pre-delivery observation in [native-usage-final.json](coordinator/native-usage-final.json). This is an actual native counter delta, not billing telemetry or a weekly quota percentage. The last receipt-writing work and final response occur after that observation.

The [worker/experiment-stop receipt](coordinator/worker-experiment-stop-receipt.json), [295-minute checkpoint](coordinator/checkpoints/030-closeout-295-minute.json), [shutdown receipt](coordinator/shutdown-receipt.json) and [complete checkpoint cadence](coordinator/checkpoint-cadence-final.json) preserve actual observations. No active child or experiment is known at delivery; the enclosing service's later termination is unobserved. The [bounded termination record](coordinator/termination-certificate.json) explicitly rejects positive achievement and scientific exhaustion. [Programme v5](coordinator/programme-v5.md) closes only the integration/delivery milestone; future research priorities remain HOLD. The [delivery manifest](coordinator/delivery-manifest.json) binds the delivered files.

The mathematical goal remains ACTIVE and unresolved. After this terminal delivery or the cap, stop scientific work; no automatic successor.''')
assert math in report
text('final.md',report)
atom('coordinator/final-mathematical-content-binding-v2.json',{
    'at':now.isoformat(),'audited_draft':'coordinator/final-draft-v4.md','audited_draft_sha256':sha(O/'coordinator/final-draft-v4.md'),
    'math_section_sha256':hashlib.sha256(math.encode()).hexdigest(),'math_section_byte_identical':True,
    'final_report_sha256':sha(O/'final.md'),'changes':'Header/status and operational footer only; no new mathematical assertion or acceptance.'})

compliance=read('coordinator/protected-period-compliance.json')
compliance['status']='PROTECTED_INTERVAL_COMPLETED_CAPPED_PACKAGE_DELIVERED'
compliance['terminal_delivery_at']=now.isoformat();compliance['operational_deviations']='coordinator/operational-deviations-v3.json'
compliance['final_cadence']='coordinator/checkpoint-cadence-final.json';compliance['post210_category']='Review/targeted repair, then scheduled consolidation and delivery; no new discovery assignment'
compliance['scientific_achievement']=False;compliance['scientific_exhaustion']=False
atom('coordinator/protected-period-compliance.json',compliance)
runtime=read('coordinator/runtime-verification.json');runtime['updated_at']=now.isoformat()
runtime['final_local_closeout']='coordinator/shutdown-receipt.json';runtime['actual_external_service_termination_observed']=False
atom('coordinator/runtime-verification.json',runtime)
with (O/'progress.md').open('a') as f:f.write(decision)
text('resume.md',f'''# Terminal capped-run handoff — STOP

Delivered at {now.isoformat()} before the original graceful deadline. Do not continue scientific work in this run, launch a successor, extend/reset the cap, or mutate the unresolved native goal to make process status look complete.

FF remains open; substantive source classifications apply to the inherited radius; established hardness is absent. The 210-minute protected investigation and fresh challenge were completed. Scientific exhaustion is rejected because material routes remain. All 28 accepted auxiliary/source gates are reconciled. Read final.md, claims.json, claim-dependencies.json, coordinator/programme-v5.md and coordinator/termination-certificate.json for the exact frontier. Future work requires separate authorization and named entry artifacts. Current native goal remains ACTIVE and unresolved.

Observed local closeout is recorded in coordinator/shutdown-receipt.json. It does not certify the enclosing service's future graceful/hard shutdown. No experiments or child agents remain known active. Original hard cap: {cap['hard_deadline_at']}.
''')

certificate={'at':now.isoformat(),'service_elapsed_seconds':elapsed,
    'category':'ORIGINAL_CAPPED_RUN_FINAL_CONSOLIDATION_AND_DELIVERY',
    'positive_scientific_achievement':False,'scientific_exhaustion':False,
    'operational_failure':False,'user_stop':False,'bounded_package_delivered':True,
    'reason':'Original fixed-duration run has entered its mandated final winddown; preserve reviewed partial results and unresolved obligations. No early-exhaustion or achievement certificate is asserted.',
    'FF':'OPEN','SV':'SUBSTANTIVE_REVIEWED_CLASSIFICATION_AT_INHERITED_RADIUS_NO_NEW_FF_RADIUS',
    'hardness':'NOT_ESTABLISHED','native_goal_state':g['status'],
    'protected_period':'coordinator/protected-period-compliance.json','challenge':'reviews/FRONTIER-CHALLENGE1/frontier-challenge-report-v1.md',
    'every_escape_reply':'coordinator/frontier-challenge-replies-v4.md',
    'remaining_routes':'coordinator/programme-v5.md','pending_mathematical_review_or_repair':[],
    'open_scientific_work':'Polynomial scalable nonlinear channel or explicit computational source comparison; compatible source-hardness map remains open. Not launched after discovery cutoff.',
    'shutdown':'coordinator/shutdown-receipt.json','usage':'coordinator/native-usage-final.json',
    'delivery_manifest':'coordinator/delivery-manifest.json','goal_mutations_for_closeout':0,
    'no_further_scientific_work_in_run':True,'no_restart_extension_or_successor':True,
    'external_service_termination_observed':False}
atom('coordinator/termination-certificate.json',certificate)

required=['final.md','claims.json','claim-dependencies.json','reconciliation.md','regressions.json','reduction-attempts.md','parameter-table.md','source-comparison.md','progress.md','resume.md','programme-decisions.md','coordinator/programme-v5.md','coordinator/native-usage-final.json','coordinator/shutdown-receipt.json','coordinator/termination-certificate.json']
assert all((O/x).is_file() for x in required)
for link in re.findall(r'\]\(([^)]+)\)',report):
    if not link.startswith(('http:', 'https:', '#')): assert (O/link).is_file(), link
assert datetime.datetime.now(datetime.timezone.utc) < dt(cap['graceful_shutdown_at'])
exclude={'run.log','worker-status.json','run.log.brlwe-fixed-family-20261021-astra-ultra.cap-status.json','coordinator/delivery-manifest.json'}
files=[]
for p in sorted(O.rglob('*')):
    if not p.is_file():continue
    rel=str(p.relative_to(O))
    if rel in exclude or p.suffix=='.tmp' or '__pycache__' in p.parts:continue
    files.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
manifest={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Final delivered static files, including frozen allowed packets and original failures. Artifact count is not experiment count.',
          'artifacts':files,'artifact_count':len(files),'excluded_live_or_self_files':sorted(exclude),
          'final_report':'final.md','native_goal_state':'active unresolved',
          'actual_native_usage_observation':goal_observation,'tokens_delta':usage['tokens_delta'],
          'goal_state_mutated':False,'future_external_shutdown_certified':False,
          'after_delivery':'No scientific continuation, restart, extension or successor.'}
atom('coordinator/delivery-manifest.json',manifest)
print(json.dumps({'at':manifest['at'],'artifacts':len(files),'report_sha256':sha(O/'final.md'),
                  'manifest_sha256':sha(O/'coordinator/delivery-manifest.json'),'native_tokens_delta':usage['tokens_delta'],
                  'native_goal':'active unresolved','category':certificate['category'],'external_shutdown_observed':False}))
