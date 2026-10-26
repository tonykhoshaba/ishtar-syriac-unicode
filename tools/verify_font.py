from pathlib import Path
from fontTools.ttLib import TTFont
from PIL import Image,ImageFont,ImageDraw
import uharfbuzz as hb,json
R=Path(__file__).resolve().parents[1];p=R/'output/IshtarSyriacUnicodeAlpha-Regular.ttf';f=TTFont(p);face=hb.Face(p.read_bytes());font=hb.Font(face)
samples=['ܐ ܒ ܓ ܕ ܗ ܘ ܙ ܚ ܛ ܝ ܟ ܠ ܡ ܢ ܤ ܥ ܦ ܨ ܩ ܪ ܫ ܬ','ܒܒܒ ܓܓܓ ܟܟܟ ܡܡܡ ܢܢܢ ܦܦܦ ܬܬܬ','ܐܵܢܵܐ ܒܲܝܬܵܐ ܫܠܵܡܵܐ ܟܬܵܒ݂ܵܐ','ܟܬܵܒ݂ܝܼ ܟܬܵܒ݂ܘܼܟ݂ ܟܬܵܒ݂ܵܟ݂ܝ ܟܬܵܒ݂ܹܗ','ܒܵܒܵܐ ܢܲܗܪܵܐ ܐܝܼܕܵܐ ܬܐ','ܡ̇ܢ ܡ̣ܢ ܪ̈ ܐܵܬܘܿܪ̈ܵܝܹܐ']
results=[]
for s in samples:
 b=hb.Buffer();b.add_str(s);b.guess_segment_properties();hb.shape(font,b);g=[f.getGlyphName(i.codepoint) for i in b.glyph_infos];assert '.notdef' not in g;results.append({'text':s,'glyphs':g})
# Meaningful joining assertion: same Unicode beth selects initial, medial and final.
b=hb.Buffer();b.add_str('ܒܒܒ');b.guess_segment_properties();hb.shape(font,b);assert [f.getGlyphName(i.codepoint) for i in b.glyph_infos]==['uni0712.fina','uni0712.medi','uni0712.init']
for m in [0x732,0x735,0x738,0x739,0x73c,0x73f,0x308]:assert f['hmtx'][f.getBestCmap()[m]][0]==0
ft=ImageFont.truetype(str(p),64);label=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
im=Image.new('RGB',(1600,1700),'white');d=ImageDraw.Draw(im);d.text((40,20),'ISHTAR SYRIAC UNICODE — ALPHA / REVISED PROOF',font=label,fill='black')
letters=samples[0].split()
names=['Alaph','Beth','Gamal','Dalath','He','Waw','Zain','Heth','Teth','Yudh','Kaph','Lamadh','Mim','Nun','Semkath','Ayn','Pe','Sadhe','Qoph','Resh','Shin','Taw']
for i,(char,name) in enumerate(zip(letters,names)):
 x=1450-(i%11)*140;y=80+(i//11)*210
 d.text((x,y),char,font=ft,fill='black',anchor='ma',direction='rtl');d.text((x,y+130),str(i+1)+' '+name,font=label,fill='black',anchor='ma')
for i,s in enumerate(samples[1:]):
 d.text((1500,560+i*175),s,font=ft,fill='black',anchor='ra',direction='rtl')
d.text((40,1470),'Restored square-dot resh-seyame candidate; original glyph still to be located',font=label,fill='black')
d.text((1500,1520),'ܪ     ܪ̈     ܦ     ܦ̮',font=ft,fill='black',anchor='ra',direction='rtl')
im.save(R/'output/unicode-proof.png');(R/'output/shaping-tests.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print('Passed shaping checks; rendered all 22 letters in labeled cells.')
