from pathlib import Path
import zipfile,shutil,sys,json,io
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject
root=Path.cwd();out=root/'public/artifacts';out.mkdir(exist_ok=True)
# Stable research bundle: omit raw third-party papers and transient LaTeX/cache files.
with zipfile.ZipFile(out/'recordings.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted((root/'research/recordings').glob('*')):z.write(p,str(p.relative_to(root/'research')))
with zipfile.ZipFile(out/'research-package.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.write(root/'README.md','README.md')
 for base in ['research','scripts']:
  for p in sorted((root/base).rglob('*')):
   if not p.is_file() or 'sources' in p.parts or '__pycache__' in p.parts:continue
   if p.suffix not in ['.md','.json','.csv','.bib','.mjs','.py','.tex','.pdf','.png','.cast','.diff']:continue
   z.write(p,str(p.relative_to(root)))
 for p in sorted((root/'public/lab').glob('*')):
  if p.is_file():z.write(p,'lab/'+p.name)
 for p in sorted((out/'study-screenshots').glob('*.png')):
  z.write(p,'figures/study-screenshots/'+p.name)
 z.writestr('requirements.txt','matplotlib>=3.8\nnumpy>=1.25\nreportlab>=4\npillow>=10\n')
print('Packaged research sources and original recordings.')
if '--local' in sys.argv:
 site=root/'dist/client';assert (site/'index.html').is_file(),'Build the static presentation first.'
 # Refresh ordinary static downloads before creating the standalone distribution.
 for p in out.iterdir():
  if p.is_file() and p.name!='local-presentation.zip':shutil.copy2(p,site/'artifacts'/p.name)
 with zipfile.ZipFile(out/'local-presentation.zip','w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(site.rglob('*')):
   if p.is_file() and p.name!='local-presentation.zip':
    arc='site/'+str(p.relative_to(site))
    if p==site/'artifacts/presentation.pdf':
     writer=PdfWriter(clone_from=str(p))
     for page in writer.pages:
      for ref in page.get('/Annots',[]):
       action=ref.get_object().get('/A')
       if action and '/URI' in action:
        uri=str(action['/URI'])
        if uri.startswith('https://nyu-sociology-ai-research.chrisjbarrie.chatgpt.site'):
         action[NameObject('/URI')]=TextStringObject(uri.replace('https://nyu-sociology-ai-research.chrisjbarrie.chatgpt.site','http://127.0.0.1:8765',1))
     buff=io.BytesIO();writer.write(buff);z.writestr(arc,buff.getvalue())
    else:z.write(p,arc)
  z.writestr('serve.py','''from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
root=Path(__file__).resolve().parent/'site'
server=ThreadingHTTPServer(('127.0.0.1',8765),partial(SimpleHTTPRequestHandler,directory=str(root)))
print('Open http://127.0.0.1:8765 in your browser. Ctrl+C stops the server.',flush=True)
try: server.serve_forever()
except KeyboardInterrupt: server.server_close()
''')
  z.writestr('README.txt','NYU Sociology — AI for research\n\nRun: python3 serve.py\nOpen: http://127.0.0.1:8765\n\nNo Internet or AI API is required. Do not open index.html with file://.\nOpen the PDF slides from the index. Each research output opens directly.\nThe complete PDF backup and research archive are in site/artifacts/.\nRecordings replay actual command output; timing is adjusted for readability.\nThe current study protocol is a proposal, not an empirical estimate. The original model remains archived.\n')
 shutil.copy2(out/'local-presentation.zip',site/'artifacts/local-presentation.zip')
 print('Packaged local browser presentation, assets, videos, and server.')
for name in ['recordings.zip','research-package.zip']+(['local-presentation.zip'] if '--local' in sys.argv else []):
 with zipfile.ZipFile(out/name) as z:assert z.testzip() is None
 print(name,round((out/name).stat().st_size/1024),'KB')
