from pathlib import Path
from PIL import Image,ImageFont,ImageDraw
import json,uharfbuzz as hb
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1];O=R/'output';P=O/'IshtarSyriacUnicode-Regular.ttf';f=TTFont(P);face=hb.Face(P.read_bytes());hf=hb.Font(face)
letters=list(zip('ܐܒܓܕܗܘܙܚܫܝܟܠܡܢܤܥܦܨܩܪܛܬ',['Alaph','Beth','Gamal','Dalath','He','Waw','Zain','Heth','Shin','Yudh','Kaph','Lamadh','Mim','Nun','Semkath','Ain','Pe','Sadhe','Qoph','Resh','Teth','Taw']))
ft=ImageFont.truetype(str(P),54);lab=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',19);sm=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15)
groups=[('talqana-seyame','TALQANA WITH SEYAME',[('Above silencer + Seyame','݇̈'),('Below silencer + Seyame','݈̈')]),('below-vowels-seyame','BELOW VOWELS WITH SEYAME',[('Horizontal zlama + Seyame','ܸ̈'),('Angular zlama + Seyame','ܹ̈')]),('rukakha-vowels','RUKAKHA WITH VOWELS',[('Rukakha + Ptakha','݂ܲ'),('Rukakha + Zlama','݂ܸ')]),('majliyana-vowels','BELOW MAJLIYANA WITH VOWELS',[('Majliyana + Ptakha','̰ܲ'),('Majliyana + Zqapa + Seyame','̰ܵ̈')])]
checks=[]
for slug,title,marks in groups:
 im=Image.new('RGB',(1600,2350),'#faf8f3');d=ImageDraw.Draw(im);d.text((30,20),'ISHTAR — '+title,font=lab,fill='black');d.text((30,55),'Placement tests, not vocabulary. Some combinations are rare or unused. Nothing on this sheet is approved yet.',font=sm,fill='black')
 for i,(c,name) in enumerate(letters):
  x=20+(i%4)*395;y=95+(i//4)*370;d.rounded_rectangle((x,y,x+375,y+350),radius=10,fill='white',outline='#bbb');d.text((x+15,y+10),f'{i+1}. {name}',font=lab,fill='black')
  for j,(label,mark) in enumerate(marks):
   text=c+mark+('ܒ' if c in 'ܡܢ' else '')
   if slug=='majliyana-vowels' and c not in 'ܓܟ':
    d.text((x+185,y+120+j*155),'Not a proposed use',font=sm,fill='#888',anchor='ms');continue
   if slug=='rukakha-vowels' and c not in 'ܒܓܕܟܡܬ':
    d.text((x+185,y+120+j*155),'Not a proposed use',font=sm,fill='#888',anchor='ms');continue
   d.text((x+185,y+125+j*155),text,font=ft,fill='black',anchor='ms',direction='rtl');d.text((x+185,y+175+j*155),label,font=sm,fill='black',anchor='ma')
   b=hb.Buffer();b.add_str(text);b.guess_segment_properties();hb.shape(hf,b);names=[f.getGlyphName(a.codepoint) for a in b.glyph_infos];assert '.notdef' not in names;checks.append({'text':text,'glyphs':names})
 im.save(O/(slug+'-review.png'))
# Test multiple entry orders: the same marks must produce identical outlines.
for c in 'ܒܓܟܪܫ':
 for a,b in [('ܲ','̈'),('ܵ','̈'),('ܸ','̈'),('݇','̈'),('݈','̈')]:
  shaped=[]
  for text in [c+a+b,c+b+a]:
   buf=hb.Buffer();buf.add_str(text);buf.guess_segment_properties();hb.shape(hf,buf);shaped.append([(g.codepoint,p.x_advance,p.x_offset,p.y_offset) for g,p in zip(buf.glyph_infos,buf.glyph_positions)])
  assert shaped[0]==shaped[1],(c,a,b,shaped)
(O/'mixed-marks-checks.json').write_text(json.dumps({'samples':checks,'entry_order_checks':25,'status':'visual review pending'},ensure_ascii=False,indent=2));print('Rendered four review sheets; passed',len(checks),'shaping and 25 entry-order checks')
# Connected Gamal and Kaph must also be checked, not just isolated letters.
cases=[('Gamal standalone','ܓ',''),('Gamal initial','ܓ','ܒ'),('Gamal medial','ܒܓ','ܒ'),('Gamal attached final','ܒܓ',''),('Kaph initial','ܟ','ܒ'),('Kaph medial','ܒܟ','ܒ'),('Kaph attached final','ܒܟ',''),('Kaph detached final','ܕܟ','')]
im=Image.new('RGB',(1800,2550),'#faf8f3');d=ImageDraw.Draw(im);d.text((30,20),'ISHTAR — CONNECTED GAMAL AND KAPH: MIXED MARKS',font=lab,fill='black')
for i,(title,before,after) in enumerate(cases):
 y=65+i*305;d.text((30,y),f'{i+1}. {title}',font=lab,fill='black')
 for j,(label,mark) in enumerate([('Unmarked',''),('Rukakha + Ptakha','݂ܲ'),('Rukakha + Zlama','݂ܸ'),('Talqana + Seyame','݇̈')]):
  x=25+j*445;d.rounded_rectangle((x,y+35,x+425,y+285),radius=10,fill='white',outline='#bbb');text=before+mark+after;d.text((x+210,y+170),text,font=ft,fill='black',anchor='ms',direction='rtl');d.text((x+210,y+240),label,font=sm,fill='black',anchor='ma')
im.save(O/'connected-mixed-marks-review.png')
