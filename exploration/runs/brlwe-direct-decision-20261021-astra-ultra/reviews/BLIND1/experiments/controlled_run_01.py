from pathlib import Path
import subprocess,resource,time,os,signal,json,hashlib,datetime
base=Path(__file__).resolve().parent
code=base/'exact_checks_01.py'
def limits():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(110,110))
start=time.monotonic()
with (base/'exact_checks_01.stdout').open('wb') as out,(base/'exact_checks_01.stderr').open('wb') as err:
    p=subprocess.Popen(['python3',str(code)],stdout=out,stderr=err,preexec_fn=limits,start_new_session=True)
    timeout=False
    try:ret=p.wait(timeout=120)
    except subprocess.TimeoutExpired:
        timeout=True;os.killpg(p.pid,signal.SIGKILL);ret=p.wait()
r=resource.getrusage(resource.RUSAGE_CHILDREN)
status={'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'returncode':ret,'timed_out':timeout,'wall_seconds':time.monotonic()-start,'user_cpu_seconds':r.ru_utime,'system_cpu_seconds':r.ru_stime,'maxrss_kib':r.ru_maxrss,'address_space_cap_bytes':536870912,'cpu_cap_seconds':110,'wall_cap_seconds':120,'code_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),'outputs':{name:hashlib.sha256((base/name).read_bytes()).hexdigest() for name in ['exact_checks_01.stdout','exact_checks_01.stderr']}}
(base/'exact_checks_01.status.json').write_text(json.dumps(status,indent=2)+'\n')
print(json.dumps(status,indent=2))
