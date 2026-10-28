"""Review the corrected Gamal forms with vowels and Seyame."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from fontTools.ttLib import TTFont
import uharfbuzz as hb
import json
R=Path(__file__).resolve().parents[1];O=R/'output';P=O/'IshtarSyriacUnicode-Regular.ttf';f=TTFont(P);hf=hb.Font(hb.Face(P.read_bytes()))
label=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',24);small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18);sy=ImageFont.truetype(str(P),66)
forms=[('Standalone','ܓ','','uni0713'),('Initial','ܓ','ܒ','uni0713.init'),('Medial','ܒܓ','ܒ','uni0713.medi'),('Attached final','ܒܓ','','uni0713.fina'),('Detached final (after Dalath)','ܕܓ','','uni0713')]
groups=[('gamal-vowels-review','GAMAL — VOWELS',[('Unmarked',''),('Ptakha','ܲ'),('Zqapa','ܵ'),('Zlama horizontal','ܸ'),('Zlama angular','ܹ')]),('gamal-seyame-review','GAMAL — SEYAME WITH VOWELS',[('Seyame','̈'),('Ptakha + Seyame','ܲ̈'),('Zqapa + Seyame','ܵ̈'),('Zlama horiz. + Seyame','ܸ̈'),('Zlama ang. + Seyame','ܹ̈')])]
groups.append(('gamal-consonant-marks-review','GAMAL — DOT / MAJLIYANA WITH VOWELS',[('Rukakha','݂'),('Rukakha + Ptakha','݂ܲ'),('Rukakha + Zlama','݂ܸ'),('Majliyana + Ptakha','̰ܲ'),('Majliyana + Zlama','̰ܸ')]))
checks=[]
for slug,title,marks in groups:
 im=Image.new('RGB',(1800,1830),'#f6f3ed');d=ImageDraw.Draw(im)
 d.text((25,20),'ISHTAR / '+title,font=label,fill='#263b39');d.text((25,57),'Original forms: standalone 0x57; initial 0x47; medial 0x67; attached final 0x81. Placement tests, not vocabulary.',font=small,fill='#53675e')
 for row,(name,before,after,expected) in enumerate(forms):
  y=100+row*340;d.text((25,y),f'Row {row+1}: {name}',font=label,fill='#263b39')
  for col,(heading,mark) in enumerate(marks):
   num=row*5+col+1;x=15+col*357
   d.rounded_rectangle((x,y+40,x+344,y+321),radius=10,fill='white',outline='#b7c4b8')
   d.text((x+13,y+53),f'{num}. {heading}',font=small,fill='#263b39')
   text=before+mark+after
   d.text((x+172,y+174),text,font=sy,fill='black',anchor='mm',direction='rtl')
   d.text((x+13,y+293),'Marks belong to Gamal',font=small,fill='#65776d')
   buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(hf,buf)
   names=[f.getGlyphName(g.codepoint) for g in buf.glyph_infos]
   assert expected in names or any(n.startswith('stack.'+expected+'.') for n in names),(text,names,expected)
   assert '.notdef' not in names,(text,names)
   checks.append({'sheet':slug,'box':num,'form':name,'text':text,'glyphs':names})
 im.save(O/(slug+'.png'))
(O/'gamal-marks-review.json').write_text(json.dumps({'status':'Awaiting Tony visual review','samples':checks},ensure_ascii=False,indent=2)+'\n')
html='<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Gamal vowels and Seyame review</title><style>body{font:18px/1.6 system-ui;background:#f6f3ed;color:#263b39;margin:24px}img{display:block;width:100%;max-width:1800px;margin:20px 0}a{color:#245f53}</style><h1>Gamal: vowels and combining marks</h1><p>Review vowel and mark placement across all Gamal joining forms. The Syriac examples demonstrate shapes, not vocabulary. Click a sheet to enlarge it. Please report the sheet and box number.</p>'
for slug,title,marks in groups:html+=f'<h2 id="{"talqana" if "talqana" in slug else slug}">{title}</h2><a href="../output/{slug}.png" target="_blank"><img src="../output/{slug}.png" alt="{title}"></a>'
(R/'keyboard/gamal-review.html').write_text(html)
print('Rendered three sheets;',len(checks),'shaping checks passed; visual approval pending.')
