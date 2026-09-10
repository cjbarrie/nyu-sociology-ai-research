import json,sys,pathlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
v=sys.argv[1];d=pathlib.Path('research')/v;j=json.loads((d/'results.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#aaa3b5','text.color':'#24232b','axes.labelcolor':'#24232b','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(7.5,3.25));colors=['#817a8d','#6841bb','#2f817c']
for i,s in enumerate(j['scenarios']):
 m=s['metrics']['humanRequests'];ax.errorbar(m['mean'],i,xerr=[[m['mean']-m['low']],[m['high']-m['mean']]],fmt='o',color=colors[i],capsize=4,markersize=9,lw=2);ax.text(m['high']+1.6,i,f"{m['mean']:.1f}",va='center',fontweight='bold')
ax.set_yticks(range(len(j['scenarios'])),[s['name'].replace(' + ',' +\n') for s in j['scenarios']]);ax.invert_yaxis();ax.set_xlim(0,85);ax.set_xlabel('Human requests per 100 support needs');ax.grid(axis='x',alpha=.15);ax.set_title('A mechanism illustration, not an empirical estimate',loc='left',fontsize=12,pad=20);fig.text(.03,.01,'80 matched seeds · bars: central 95% of simulated runs · 100 people × 100 periods',fontsize=8,color='#706d78');fig.tight_layout(rect=[0,.06,1,1]);fig.savefig(d/'requests.pdf');fig.savefig(d/'requests.png',dpi=180);plt.close(fig)
if v=='v2':
 z=np.array([g['mean'] for g in j['grid']]).reshape(6,6).T;fig,ax=plt.subplots(figsize=(6.4,4.0));im=ax.imshow(z,origin='lower',extent=[-.1,1.1,-.1,1.1],vmin=-50,vmax=50,cmap='BrBG',aspect='auto');ax.set_xticks(np.arange(0,1.01,.2));ax.set_yticks(np.arange(0,1.01,.2));ax.set_xlabel('Substitution probability');ax.set_ylabel('Bridging probability');fig.colorbar(im,ax=ax,label='Change in human requests / 100 needs');ax.set_title('The sign depends on the behavioral assumptions',loc='left',fontsize=11);fig.tight_layout();fig.savefig(d/'sensitivity.pdf');fig.savefig(d/'sensitivity.png',dpi=180);plt.close(fig)
print(f'Rendered {v} figure(s) from saved analysis results.')
