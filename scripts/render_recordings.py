"""Render genuine timestamped terminal recordings. No invented terminal events."""
from PIL import Image,ImageDraw,ImageFont
import json,pathlib,subprocess,textwrap,math
root=pathlib.Path('research/recordings');dest=pathlib.Path('public/artifacts')
fontpath='/System/Library/Fonts/Menlo.ttc';mono=ImageFont.truetype(fontpath,17);small=ImageFont.truetype(fontpath,14);titlefont=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',27)
def render(name,stages):
 fps=12;w,h=1280,720
 p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-vcodec','rawvideo','-s',f'{w}x{h}','-pix_fmt','rgb24','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p',str(dest/(name+'.mp4'))],stdin=subprocess.PIPE)
 for stem,duration,label in stages:
  rec=json.loads((root/(stem+'.json')).read_text());elapsed=rec['elapsed_seconds'];n=int(duration*fps)
  for f in range(n):
   # Last 2 seconds hold final output; map earlier frames to actual timestamps.
   pos=min(1,f/max(1,n-2*fps));actual=elapsed*pos;txt=''.join(e['text'] for e in rec['events'] if e['t']<=actual)
   lines=[]
   for ln in txt.splitlines():lines.extend(textwrap.wrap(ln,width=113,replace_whitespace=False,drop_whitespace=False)or[''])
   im=Image.new('RGB',(w,h),'#211c2d');d=ImageDraw.Draw(im)
   d.text((40,28),label,font=titlefont,fill='#f6f1fc');d.text((40,73),f'ACTUAL RECORDED COMMAND OUTPUT  |  Execution: {elapsed:.3f}s  |  Replay: {duration}s',font=small,fill='#bfacd8')
   for i,ln in enumerate(lines[-24:]):d.text((40,120+i*21),ln,font=mono,fill='#99d4c3' if ln.startswith('PASS') else '#e0d7ea')
   d.text((40,659),'Prepared execution replay. Timing adjusted for legibility; authoring time is not included.',font=small,fill='#bfacd8');d.line((40,698,40+int(1200*pos),698),fill='#b394e4',width=3)
   p.stdin.write(im.tobytes())
 p.stdin.close();assert p.wait()==0;print(f'Rendered {name}.mp4 from original timestamped recordings.')
render('sources',[('00-source-retrieval',14,'Literature workflow / public-source retrieval')])
render('revision',[('03-bridging-revision',12,'Researcher steering / add a bridging mechanism'),('04-revised-analysis',9,'Re-execute / 80 matched populations'),('05-model-tests',8,'Check / boundary cases and accounting'),('06-revised-memo',12,'Produce / compile the revised LaTeX memo')])
