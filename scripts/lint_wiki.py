from pathlib import Path
import re, yaml, sys
BASE=Path(__file__).resolve().parents[1]
W=BASE/'wiki'
errors=[]; warning=[]; ids={}; found_claims=set()
for p in W.rglob('*.md'):
 s=p.read_text(encoding='utf-8')
 if p.name not in ['index.md','log.md']:
  if not s.startswith('---\n'):
   errors.append(f'{p.relative_to(BASE)}: missing YAML frontmatter')
  else:
   try: m=yaml.safe_load(s.split('---',2)[1])
   except Exception as e: errors.append(f'{p}: invalid YAML {e}'); continue
   if not isinstance(m,dict) or not m.get('id'): errors.append(f'{p}: missing id')
   elif m['id'] in ids: errors.append(f'duplicate id {m["id"]}: {ids[m["id"]]} and {p}')
   else: ids[m['id']]=p
   if p.parent.name=='sources':
    for field in ('title','type','publisher','url','published_at','accessed_at','source_authenticity','raw_path','claim_ids'):
     if field not in m: errors.append(f'{p}: missing {field}')
    if m.get('url')=='unknown':warning.append(f'{p.relative_to(BASE)}: original URL missing')
    for cid in m.get('claim_ids',[]):
     if cid in found_claims: errors.append(f'duplicate claim {cid}')
     found_claims.add(cid)
 for link in re.findall(r'(?<!!)\[[^]]*\]\(([^)]+)\)',s):
  if link.startswith(('http://','https://','#','mailto:')): continue
  target=(p.parent/link.split('#')[0]).resolve()
  if not target.is_file(): errors.append(f'{p.relative_to(BASE)}: broken link {link}')
for p in (W/'sources').glob('*.md'):
 s = p.read_text(encoding="utf-8")
 m = yaml.safe_load(s.split("---", 2)[1])
 for cid in m.get('claim_ids',[]):
  if not re.search(r'\| '+re.escape(cid)+r' \|',s):errors.append(f'{p.name}: claim {cid} not in table')
print('Source notes:',len(list((W/'sources').glob('*.md'))))
print('Unique claim IDs:',len(found_claims))
print('Errors:',len(errors),'Warnings:',len(warning))
for x in errors: print('ERROR',x)
for x in warning:print('WARNING',x)
sys.exit(1 if errors else 0)
