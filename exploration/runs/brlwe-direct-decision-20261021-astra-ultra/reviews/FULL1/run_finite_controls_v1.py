#!/usr/bin/env python3
import datetime, hashlib, json, os, pathlib, resource, signal, subprocess, sys, time
base=pathlib.Path(__file__).resolve().parent
script=base/'finite_controls_v1.py'
def limits():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(115,115))
start=time.monotonic()
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (base/'finite_controls_v1.stdout.json').open('wb') as out, (base/'finite_controls_v1.stderr.txt').open('wb') as err:
    proc=subprocess.Popen([sys.executable,str(script)],stdout=out,stderr=err,start_new_session=True,preexec_fn=limits)
    timed_out=False
    try:
        code=proc.wait(timeout=120)
    except subprocess.TimeoutExpired:
        timed_out=True
        os.killpg(proc.pid,signal.SIGTERM)
        try: code=proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid,signal.SIGKILL); code=proc.wait()
receipt={'start_utc':stamp,'elapsed_seconds':time.monotonic()-start,'exit_code':code,
    'timed_out':timed_out,'rlimit_as_bytes':536870912,'rlimit_cpu_seconds':115,
    'peak_child_rss_kib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
    'code_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
    'wrapper_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    'preregistration_sha256':hashlib.sha256((base/'finite_controls_v1.preregistration.md').read_bytes()).hexdigest()}
(base/'finite_controls_v1.receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
raise SystemExit(code if code>=0 else 1)
