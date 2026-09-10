from pathlib import Path
import difflib
p=Path('research/model.mjs');old=p.read_text();target='const bridge=false; // v1: substitution only; no bridge from chatbot to a person.'
assert target in old
new=old.replace(target,'const bridge=usesAI && u.bridge<bridging; // v2: AI may prompt human outreach.')
p.write_text(new)
diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='v1/model.mjs',tofile='v2/model.mjs'))
Path('research/revision.diff').write_text(diff)
print('Researcher instruction from the agreed plan: Add the possibility that chatbot use encourages human contact.')
print('Applied actual change to the model:')
print(diff)
