"""Prepare the static export for a GitHub Pages project URL, including PDF links."""
from pathlib import Path
import os,re,shutil
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,TextStringObject
root=Path('dist/client')
base=os.environ.get('PAGES_BASE_PATH','').rstrip('/')
origin=os.environ.get('PAGES_ORIGIN','https://cjbarrie.github.io').rstrip('/')
assert base=='' or re.fullmatch(r'/[A-Za-z0-9_.-]+',base)
old='https://nyu-sociology-ai-research.chrisjbarrie.chatgpt.site'
for p in root.rglob('*'):
 if p.is_file() and p.suffix in {'.html','.js','.css','.json','.rsc','.md','.txt'}:
  s=p.read_text()
  # Rewrite authored root-relative resources and Vite's static asset references.
  s=re.sub(r'''(["'`(=])/((?:artifacts|workshop|lab|_next)/)''',lambda m:m[1]+base+'/'+m[2],s)
  s=re.sub(r'''(href=["'])/([#"'])''',lambda m:m[1]+base+'/'+m[2],s)
  s=s.replace(old,origin+base)
  p.write_text(s)
for p in root.rglob('*.pdf'):
 w=PdfWriter(clone_from=str(p));changed=False
 for page in w.pages:
  for ref in page.get('/Annots',[]):
   action=ref.get_object().get('/A')
   if action and '/URI' in action:
    uri=str(action['/URI'])
    if uri.startswith(old):action[NameObject('/URI')]=TextStringObject(uri.replace(old,origin+base,1));changed=True
 if changed:
  temp=p.with_suffix('.tmp');w.write(temp);temp.replace(p)
(root/'.nojekyll').touch()
print('Prepared GitHub Pages at '+origin+base+'/')
