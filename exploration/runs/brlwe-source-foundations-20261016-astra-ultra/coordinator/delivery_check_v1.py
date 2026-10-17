import sys,json,hashlib,re,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
p=Path(__file__).resolve().parents[1]
errors=[]; checks=[]
def check(ok,label):
    checks.append({"check":label,"pass":bool(ok)})
    if not ok: errors.append(label)
def digest(f): return hashlib.sha256(f.read_bytes()).hexdigest()
def exists(s):
    return (p/s).is_file()
claims=json.loads((p/"claims.json").read_text())
reg=json.loads((p/"regressions.json").read_text())
agents=json.loads((p/"agents.json").read_text())
exp=json.loads((p/"experiments/registry.json").read_text())
reviews=json.loads((p/"coordinator/review-index-v1.json").read_text())
check(digest(p/claims["current_candidate"])==claims["statement_sha256"],"exact theorem hash")
check(digest(p/claims["proof"])==claims["proof_sha256"],"exact canonical proof hash")
by={x["id"]:x for x in claims["claims"]}
check(len(by)==len(claims["claims"]),"unique claim IDs")
vis=set();done=set()
def dfs(k):
    if k in vis: raise AssertionError("claim cycle "+k)
    if k in done:return
    vis.add(k)
    for z in by[k].get("dependencies",[]):
        check(z in by,"dependency exists "+k+" -> "+z)
        if z in by:dfs(z)
    vis.remove(k);done.add(k)
for k in by:dfs(k)
for c in by.values():
    for f in c.get("evidence",[]):check(exists(f),"claim evidence "+f)
    if "--require-accepted" in sys.argv and c["id"].startswith("EX-"):
        check(c["status"]=="ACCEPTED","accepted current "+c["id"])
        for d in c["dependencies"]:check(by[d]["status"]=="ACCEPTED","closed dependency "+d)
check(len(reg["entries"])==43 and len({x["id"] for x in reg["entries"]})==43,"all 43 historical controls preserved")
for e in reg["entries"]:
    check(bool(e.get("scope_reason")) and "PENDING" not in e["current_status"],"regression disposition "+e["id"])
    for f in e["new_evidence"]:check(exists(f),"regression evidence "+f)
for e in reg.get("new_entries",[]):
    for f in e["evidence"]:check(exists(f),"new control evidence "+f)
for r in reviews["reviews"]:
    check(digest(p/r["report"])==r["sha256"],"frozen report "+r["role"])
check(reviews["strict_blind"]["role"]=="RB2","fresh blind role")
receipt=json.loads((p/reviews["strict_blind"]["receipt"]).read_text())
check(receipt["blindness_preserved"] is True,"blind isolation declared and frozen")
check(receipt["report_sha256"]==next(r["sha256"] for r in reviews["reviews"] if r["role"]=="RB2"),"blind freeze receipt hash")
for e in exp["experiments"]:
    check(e["status"]=="completed","experiment stopped "+e["id"])
    for k in ["code","results","command_file","preflight","receipt"]:
        if k in e:check(exists(e[k]),"experiment artifact "+e[k])
check(all(r["status"]=="released" for r in exp["reservations"]),"all experiment reservations released")
for f in ["final.md","resume.md","reconciliation.md","parameter-table.md","source-comparison.md",claims["current_candidate"],claims["proof"]]:
    text=(p/f).read_text()
    check(bool(text.strip()),"nonempty "+f)
    for link in re.findall(r"\]\(([^)]+)\)",text):
        link=link.strip("<>").split("#",1)[0]
        if not link or re.match(r"[a-zA-Z]+://",link):continue
        target=Path(link) if link.startswith("/") else (p/f).parent/link
        check(target.exists(),"local markdown link "+f+" -> "+link)
for f in (p/"coordinator-checkpoints").glob("*/manifest.json"):
    x=json.loads(f.read_text())
    for a in x["artifacts"]:check(digest(f.parent/"artifacts"/a["path"])==a["sha256"],"immutable snapshot "+f.parent.name+"/"+a["path"])
for line in (p/"claim-history.jsonl").read_text().splitlines():json.loads(line)
created=json.loads((p/"goal-created.json").read_text())
cfg=json.loads((p.parents[1]/"source-foundations-20261016/run-config.json").read_text())
check(created["goal"]["objective"]==cfg["goal_objective"],"exact native goal objective")
check(created["remainingTokens"] is None and "tokenBudget" not in created["goal"],"no invented token budget")
check(agents["configured"]["total_ceiling"]==4,"configured total team ceiling four")
check(agents["observed"]["observed_total_active"]<=4,"observed current team ceiling")
cap=json.loads((p/"run.log.brlwe-source-foundations-20261016-astra-ultra.cap-status.json").read_text())
now=datetime.datetime.now(datetime.timezone.utc)
check(now<datetime.datetime.fromisoformat(cap["wrapup_at"]),"delivery within unchanged discovery envelope")
history=json.loads((p/"imports/historical-index-recheck-v1.json").read_text())
check(history["files"]==1902 and history["matches"]==1902,"historical provenance recheck recorded")
out={"checked_at":now.isoformat(),"structural_check_only_not_mathematical_certification":True,"mode":"accepted" if "--require-accepted" in sys.argv else "preacceptance","checks":checks,"errors":errors,"passed":not errors}
name="delivery-check-accepted-v1.json" if "--require-accepted" in sys.argv else "delivery-check-preacceptance-v1.json"
(p/"coordinator"/name).write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"receipt":"coordinator/"+name,"checks":len(checks),"errors":errors,"passed":not errors}))
if errors:sys.exit(1)
