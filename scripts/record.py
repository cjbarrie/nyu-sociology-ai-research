"""Record actual subprocess output as asciicast v2 plus timestamped JSON."""
import subprocess, time, json, sys, pathlib, datetime
name=sys.argv[1]; command=sys.argv[2:]; out=pathlib.Path('research/recordings');out.mkdir(parents=True,exist_ok=True)
t0=time.monotonic(); events=[]
header={'version':2,'width':110,'height':28,'timestamp':int(time.time()),'title':name,'env':{'TERM':'xterm-256color'}}
with (out/(name+'.cast')).open('w') as f:
 f.write(json.dumps(header)+'\n')
 def emit(s):
  t=round(time.monotonic()-t0,4); events.append({'t':t,'text':s});f.write(json.dumps([t,'o',s.replace('\n','\r\n')])+'\n');f.flush();print(s,end='',flush=True)
 emit('$ '+' '.join(command)+'\n')
 p=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
 for line in p.stdout: emit(line)
 code=p.wait();emit(f'Exit status: {code}\n')
 elapsed=round(time.monotonic()-t0,3)
 (out/(name+'.json')).write_text(json.dumps({'title':name,'recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':elapsed,'command':command,'exit_code':code,'events':events},indent=2))
 print(f'Recorded actual execution: {elapsed:.3f}s')
 sys.exit(code)
