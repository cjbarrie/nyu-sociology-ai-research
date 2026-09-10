"""Render title-page excerpts from primary PDFs, without recreating their typography."""
from pathlib import Path
from pypdf import PdfReader,PdfWriter
import subprocess,json,hashlib
src=Path('research/sources/opening-screenshots');out=Path('public/artifacts/study-screenshots');out.mkdir(exist_ok=True)
items={
 'risko':('https://samgilbert.net/pubs/Risko2016TiCS.pdf',(.075,.035,.94,.23)),
 'lee':('https://www.microsoft.com/en-us/research/uploads/prod/2025/01/lee_2025_ai_critical_thinking_survey.pdf',(.08,.065,.935,.402)),
 'bastani':('https://doi.org/10.1073/pnas.2422633122',(.05,.014,.95,.207)),
 'coscientist':('https://www.nature.com/articles/s41586-026-10644-y.pdf',(.05,.028,.95,.323)),
 'crux':('https://arxiv.org/pdf/2607.27191',(.115,.083,.888,.350))}
manifest=[]
for key,(url,(l,t,r,b)) in items.items():
 path=src/(key+'.pdf');page=PdfReader(path).pages[0];w,h=float(page.mediabox.width),float(page.mediabox.height)
 page.cropbox.lower_left=(l*w,(1-b)*h);page.cropbox.upper_right=(r*w,(1-t)*h)
 writer=PdfWriter();writer.add_page(page);tmp=Path('/private/tmp')/('study-crop-'+key+'.pdf');writer.write(tmp)
 subprocess.run(['pdftoppm','-cropbox','-f','1','-l','1','-singlefile','-scale-to-x','2200','-scale-to-y','-1','-png',str(tmp),str(out/key)],check=True)
 manifest.append({'id':key,'source':url,'captured':'2026-09-09','page':1,'crop_fraction_from_top':[l,t,r,b],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'note':'Actual PDF title-page excerpt, rendered with Poppler; no recreated text. CRUX downloaded version is v2.' if key=='crux' else 'Actual PDF title-page excerpt, rendered with Poppler; no recreated text.'})
Path('research/opening/screenshot-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
