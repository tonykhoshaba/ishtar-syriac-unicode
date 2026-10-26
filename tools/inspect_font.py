from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
from PIL import Image,ImageDraw,ImageFont
import json,hashlib
R=Path(__file__).resolve().parents[1];p=R/'originals/ISHAR_XP.ttf';f=TTFont(p);order=f.getGlyphOrder()
report={'glyph_count':len(order),'tables':list(f.keys()),'names':{str(n.nameID):n.toUnicode() for n in f['name'].names if n.platformID==3},'cmaps':[{'platform':t.platformID,'encoding':t.platEncID,'format':t.format,'count':len(t.cmap)} for t in f['cmap'].tables],'glyphs':[]}
for i,g in enumerate(order):
 glyph=f['glyf'][g];report['glyphs'].append({'gid':i,'name':g,'advance':f['hmtx'][g][0],'bounds':[getattr(glyph,k,0) for k in ['xMin','yMin','xMax','yMax']],'legacy_codes':[hex(c) for c,n in f.getBestCmap().items() if n==g]})
t=CmapSubtable.newSubtable(4);t.platformID=3;t.platEncID=1;t.language=0;t.cmap={0xE000+i:g for i,g in enumerate(order)};f['cmap'].tables=[t];f.save(R/'output/glyph-inspection-only.ttf')
ft=ImageFont.truetype(str(R/'output/glyph-inspection-only.ttf'),60);label=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
for page in range(3):
 im=Image.new('RGB',(1200,1200),'white');d=ImageDraw.Draw(im)
 for j,i in enumerate(range(page*80,min((page+1)*80,len(order)))):
  x=(j%8)*150;y=(j//8)*120;g=report['glyphs'][i]
  d.rectangle((x,y,x+149,y+119),outline='#ccc');d.text((x+4,y+3),f'{i}: {g["name"]}',font=label,fill='black');d.text((x+55,y+35),chr(0xE000+i),font=ft,fill='black');d.text((x+4,y+100),' '.join(g['legacy_codes']),font=label,fill='black')
 im.save(R/f'output/glyph-chart-{page+1}.png')
report['original_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'originals').iterdir()};(R/'output/inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
