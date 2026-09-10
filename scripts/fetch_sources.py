import urllib.request,json,pathlib,hashlib,time
rows=json.loads(pathlib.Path('research/evidence.json').read_text());manifest=[]
for r in rows:
 t=time.monotonic(); entry={'key':r['key'],'url':r['url']}
 try:
  req=urllib.request.Request(r['url'],headers={'User-Agent':'NYU-Sociology-Research-Demo/1.0 (source verification)'})
  with urllib.request.urlopen(req,timeout=20) as response:
   body=response.read();kind=response.headers.get_content_type();
   if not body: raise ValueError('Empty response body; not a retrieved source')
   entry.update(status=response.status,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),content_type=kind)
  suffix='.pdf' if kind=='application/pdf' else '.html';pathlib.Path('research/sources',r['key']+suffix).write_bytes(body)
  print(f"{r['key']}: retrieved {len(body):,} bytes ({kind}); SHA256 {entry['sha256'][:12]}",flush=True)
 except Exception as e:entry['error']=str(e);print(f"{r['key']}: unavailable via direct fetch: {e}; see evidence table for web-tool access",flush=True)
 entry['seconds']=round(time.monotonic()-t,3);manifest.append(entry)
pathlib.Path('research/retrieval-manifest.json').write_text(json.dumps(manifest,indent=2));print('Saved retrieval manifest. Retrieval alone does not verify a claim.',flush=True)
