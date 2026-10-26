from pathlib import Path
import json,csv,hashlib
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1];K=R/'keyboard';K.mkdir(exist_ok=True)
src=R.parent/'yoab-lectures/review/keyboard-map.js'
if src.exists():
 m=json.loads(src.read_text().split('=',1)[1].strip().rstrip(';'))
else:
 src=K/'ramsina-baseline.json';m=json.loads(src.read_text())
baseline=dict(m)
additions={'A:KeyH':'ܗ̇','A:KeyR':'݂','A:KeyF':'̃'}
assert all(k not in m for k in additions);m.update(additions)
cmap=TTFont(R/'output/IshtarSyriacUnicodeAlpha-Regular.ttf').getBestCmap()
rows=[]
for k,v in m.items():
 rows.append({'key':k,'text':v,'unicode':' '.join(f'U+{ord(c):04X}' for c in v),'origin':'added' if k in additions else 'Ramsina editor','missing':' '.join(f'U+{ord(c):04X}' for c in v if ord(c) not in cmap)})
(K/'ishtar-qwerty.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
(K/'mapping-data.js').write_text('const keyboardMap='+json.dumps(m,ensure_ascii=False)+';\nconst mappingRows='+json.dumps(rows,ensure_ascii=False)+';\n')
with (K/'mapping.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
(K/'compatibility.json').write_text(json.dumps({'baseline_source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'baseline_keys':len(baseline),'changed_existing_keys':[],'added':additions,'font_coverage_gaps':[r for r in rows if r['missing']]},ensure_ascii=False,indent=2)+'\n')
print(f'{len(baseline)} original mappings preserved; {len(additions)} additions; {sum(bool(r["missing"]) for r in rows)} mappings have font coverage gaps.')
