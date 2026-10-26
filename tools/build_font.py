"""Build a review-only Unicode alpha using only the user's original outlines."""
from pathlib import Path
from copy import deepcopy
import json
from fontTools.ttLib import TTFont,newTable
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
R=Path(__file__).resolve().parents[1];out=R/'output';out.mkdir(exist_ok=True)
f=TTFont(R/'originals/ISHAR_XP.ttf');old=f.getGlyphOrder();mapping={};forms={};cmap={}
def copy(name,source,width=None):
 f['glyf'][name]=deepcopy(f['glyf'][source]);f['hmtx'][name]=(f['hmtx'][source][0] if width is None else width,f['hmtx'][source][1]);old.append(name)
# id, initial/medial source, isolated/final source; mappings remain subject to expert review.
letters=[(0x710,'a','a'),(0x712,'b','B'),(0x713,'g','W'),(0x715,'d','d'),(0x717,'h','h'),(0x718,'w','w'),(0x719,'z','z'),(0x71a,'x','X'),(0x71b,'j','T'),(0x71d,'y','Y'),(0x71f,'k','K'),(0x720,'l','l'),(0x721,'m','M'),(0x722,'n','N'),(0x724,'s','Z'),(0x725,'v','AE'),(0x726,'p','I'),(0x728,'c','c'),(0x729,'q','Q'),(0x72a,'r','r'),(0x72b,'f','f'),(0x72c,'t','t')]
for cp,join,stand in letters:
 base=f'uni{cp:04X}';copy(base,stand);cmap[cp]=base;forms[base]={}
 for tag,src in [('init','G' if cp==0x713 else 'exclamdown' if cp==0x725 else 'T' if cp==0x72c else join),('medi','T' if cp==0x72c else join),('fina','T' if cp==0x71b else 'I' if cp==0x726 else 'O' if cp==0x722 else 'c129' if cp==0x713 else 'V' if cp==0x725 else 'L' if cp==0x71f else stand)]:
  name=base+'.'+tag;copy(name,src);forms[base][tag]=name
 mapping[hex(cp)]={'base':stand,'connected':join,'status':'provisional visual identification'}
for tag,src in [('fina','A'),('fin2','A'),('fin3','a'),('med2','a')]:
 n='uni0710.'+tag
 if n in old: f['glyf'][n]=deepcopy(f['glyf'][src]);f['hmtx'][n]=f['hmtx'][src]
 else:copy(n,src)
 forms['uni0710'][tag]=n
# Second standalone ain, confirmed legacy 0x201A; optional alternate.
copy('ain.isol.alt','quotesinglbase')
# User-confirmed divine-name yudh-he at legacy 0x55 (U).
copy('uni071E','U');cmap[0x71e]='uni071E'
copy('alaph.after.lamadh','C')
# Reuse original Latin punctuation only where it is actually punctuation.
for cp in list(range(0x20,0x40))+[0x5b,0x5d]:
 g=f.getBestCmap().get(cp)
 if g:cmap[cp]=g
# Default-ignorable controls: no outline, no advance.
pen=TTGlyphPen(None);blank=pen.glyph();f['glyf']['control']=blank;f['hmtx']['control']=(0,0);old.append('control')
for cp in [0x200c,0x200d,0x200e,0x200f,0x061c]:cmap[cp]='control'
# Tatweel is a new straight joining segment, not a borrowed outline.
pen=TTGlyphPen(None);pen.moveTo((0,0));pen.lineTo((400,0));pen.lineTo((400,80));pen.lineTo((0,80));pen.closePath();f['glyf']['uni0640']=pen.glyph();f['hmtx']['uni0640']=(400,0);old.append('uni0640');cmap[0x640]='uni0640'
# Create seyame from two of the font's round dots; the legacy S slot is not seyame.
from fontTools.pens.transformPen import TransformPen
pen=TTGlyphPen(f.getGlyphSet())
for dx in [-145,145]:
 f.getGlyphSet()['braceright'].draw(TransformPen(pen,(1,0,0,0.55,dx-398,-384)))
f['glyf']['seyame.source']=pen.glyph();f['hmtx']['seyame.source']=(0,0);old.append('seyame.source')
# Rish + seyame must suppress the rish's own dot.
copy('rish.dotless','r');g=f['glyf']['rish.dotless'];cut=g.endPtsOfContours[0]+1
g.coordinates=type(g.coordinates)(g.coordinates[cut:]);g.flags=g.flags[cut:];g.endPtsOfContours=[x-cut for x in g.endPtsOfContours[1:]];g.numberOfContours-=1;g.recalcBounds(f['glyf'])
# Restore the preceding square-dot candidate at the user's request.
copy('rish.dot.source','r');g=f['glyf']['rish.dot.source'];cut=g.endPtsOfContours[0]+1
g.coordinates=type(g.coordinates)(g.coordinates[:cut]);g.flags=g.flags[:cut];g.endPtsOfContours=[cut-1];g.numberOfContours=1;g.recalcBounds(f['glyf'])
cx=(g.xMin+g.xMax)/2;bottom=g.yMin
pen=TTGlyphPen(f.getGlyphSet());f.getGlyphSet()['rish.dotless'].draw(pen)
for target in [265,535]:
 f.getGlyphSet()['rish.dot.source'].draw(TransformPen(pen,(1,0,0,1,target-cx,705-bottom)))
f['glyf']['rish.seyame']=pen.glyph();f['hmtx']['rish.seyame']=f['hmtx']['r'];old.append('rish.seyame')
# Seyame uses the same full-size original square dots as the approved Resh form.
pen=TTGlyphPen(f.getGlyphSet())
for target in [-135,135]:
 f.getGlyphSet()['rish.dot.source'].draw(TransformPen(pen,(1,0,0,1,target-cx,-bottom)))
f['glyf']['seyame.source']=pen.glyph();f['glyf']['seyame.source'].recalcBounds(f['glyf'])
f['hmtx']['seyame.source']=(0,f['glyf']['seyame.source'].xMin)

# Correct original resh-seyame glyph is still being identified.
copy('sadhe.nun.liga','c128')
copy('pe.fe.legacy','quotedblbase')
copy('pe.fe.connected','P')
copy('taw.alaph.alt1','D');copy('taw.alaph.alt2','F')
copy('he.yudh.calligraphic','H')
marks=[(0x732,'u','split'),(0x735,'o','top'),(0x738,'i','bottom'),(0x739,'e','bottom'),(0x73c,'oacute','bottom'),(0x73f,'braceright','top'),(0x307,'braceright','top'),(0x323,'braceleft','bottom'),(0x741,'braceright','top'),(0x742,'oacute','bottom'),(0x308,'seyame.source','top'),(0x747,'grave','top'),(0x748,'grave','bottom'),(0x331,'underscore','bottom'),(0x32e,'asciitilde','bottom'),(0x330,'asciitilde','bottom'),(0x303,'ellipsis','top')]
markinfo=[]
for cp,src,kind in marks:
 n=f'uni{cp:04X}';copy(n,src,0);g=f['glyf'][n];g.recalcBounds(f['glyf']);cx=(g.xMin+g.xMax)//2
 # Normalize above/below marks; retain the original split pthaha's vertical relation to baseline.
 dy=-g.yMin if kind=='top' else -g.yMax if kind=='bottom' else 0
 for i,(x,y) in enumerate(g.coordinates):g.coordinates[i]=(x,y+dy)
 g.recalcBounds(f['glyf']);f['hmtx'][n]=(0,g.xMin);cmap[cp]=n;markinfo.append((n,kind,cx,g.yMax-g.yMin))
# Pthaha needs separate upper/lower placement for tall and descending bases.
pthaha_variants=[]
for base in list(dict.fromkeys(old)):
 if not (base.startswith(('uni0710','uni0713','uni0720','uni0721','uni0722','uni072A','uni071D','uni0715','uni0719','uni0728','uni072B','uni0725','uni071F','uni0726')) or base in ['rish.dotless','rish.seyame','alaph.after.lamadh']):continue
 glyph=f['glyf'][base];glyph.recalcBounds(f['glyf'])
 name='pthaha.'+base;pen=TTGlyphPen(f.getGlyphSet())
 # Small optical adjustments from the user's ptakha review.
 dx=-130 if base.startswith('uni0713') and '.medi' in base or base.startswith('uni0713') and '.fina' in base else 0
 if base.startswith('uni072A') or base in ['rish.dotless','rish.seyame']:
  resh=f['glyf']['r'];end=resh.endPtsOfContours[0]+1
  dot_x=[x for x,y in resh.coordinates[:end]]
  dx=(min(dot_x)+max(dot_x))/2-(glyph.xMin+glyph.xMax)//2-45
 if base=='uni0713.medi':dx-=155
 if base.startswith('uni0715'):dx-=85
 lower=-40 if base.startswith(('uni0710','uni0720')) or base=='alaph.after.lamadh' else 155 if base.startswith('uni0713') else -35 if base.startswith('uni072A') or base in ['rish.dotless','rish.seyame'] else 0
 lower-=55 if base.startswith('uni0722') else 40 if base.startswith('uni0721') else 0
 lower-=60 if base.startswith(('uni0715','uni0719','uni0728','uni072B')) else 0
 upper=45 if base.startswith('uni0726') else -250 if base.startswith('uni072B') else 70 if base.startswith('uni0725') else -50 if base.startswith('uni0728') else 55 if base.startswith('uni0722') else -25 if base.startswith('uni071D') else 0
 for src,dy in [('braceright',glyph.yMax+65-698+upper),('braceleft',min(0,glyph.yMin)-65+77+lower)]:
  f.getGlyphSet()[src].draw(TransformPen(pen,(1,0,0,1,dx-(f['glyf'][src].xMin+f['glyf'][src].xMax)/2,dy)))
 f['glyf'][name]=pen.glyph();f['glyf'][name].recalcBounds(f['glyf']);f['hmtx'][name]=(0,f['glyf'][name].xMin if base=='uni0713.medi' or base.startswith(('uni0715','uni072A')) or base in ['rish.dotless','rish.seyame'] else 0);old.append(name);markinfo.append((name,'split',0,0));pthaha_variants.append((base,name))
# Zqapha optical adjustment for sadhe and the confirmed teth outline family.
copy('zqapha.lowered','uni0735',0);zg=f['glyf']['zqapha.lowered']
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x,y-60)
zg.recalcBounds(f['glyf']);f['hmtx']['zqapha.lowered']=(0,zg.xMin)
markinfo.append(('zqapha.lowered','top',(zg.xMin+zg.xMax)//2,zg.yMax-zg.yMin))
# User-selected horizontal zlameh lowered 50 font units.
copy('zlameh.horizontal.lowered','uni0738',0);zg=f['glyf']['zlameh.horizontal.lowered']
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x,y-50)
zg.recalcBounds(f['glyf']);f['hmtx']['zlameh.horizontal.lowered']=(0,zg.xMin)
markinfo.append(('zlameh.horizontal.lowered','bottom',(zg.xMin+zg.xMax)//2,zg.yMax-zg.yMin))
# Gamal zlameh: slightly higher; connected medial/final forms also left.
for name,dx in [('zlameh.horizontal.gamal',0),('zlameh.horizontal.gamal.attached',-180)]:
 copy(name,'uni0738',0);zg=f['glyf'][name]
 anchor_x=(zg.xMin+zg.xMax)//2
 for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+dx,y+40)
 zg.recalcBounds(f['glyf']);f['hmtx'][name]=(0,zg.xMin)
 markinfo.append((name,'bottom',anchor_x,zg.yMax-zg.yMin))
# Teth horizontal zlameh optical adjustment: left and slightly higher.
copy('zlameh.horizontal.teth','uni0738',0);zg=f['glyf']['zlameh.horizontal.teth']
anchor_x=(zg.xMin+zg.xMax)//2
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x-100,y+40)
zg.recalcBounds(f['glyf']);f['hmtx']['zlameh.horizontal.teth']=(0,zg.xMin)
markinfo.append(('zlameh.horizontal.teth','bottom',anchor_x,zg.yMax-zg.yMin))
# Angular zlameh: user-selected pairs lowered slightly.
copy('zlameh.angular.lowered','uni0739',0);zg=f['glyf']['zlameh.angular.lowered']
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x,y-50)
zg.recalcBounds(f['glyf']);f['hmtx']['zlameh.angular.lowered']=(0,zg.xMin)
markinfo.append(('zlameh.angular.lowered','bottom',(zg.xMin+zg.xMax)//2,zg.yMax-zg.yMin))
# Angular zlameh on Gamal and Teth: up and left, per visual review.
for name,dx in [('zlameh.angular.gamal',-180),('zlameh.angular.teth',-100)]:
 copy(name,'uni0739',0);zg=f['glyf'][name]
 anchor_x=(zg.xMin+zg.xMax)//2
 for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+dx,y+40)
 zg.recalcBounds(f['glyf']);f['hmtx'][name]=(0,zg.xMin)
 markinfo.append((name,'bottom',anchor_x,zg.yMax-zg.yMin))
# Fuller single-dot optical adjustments from the current review.
single_dot_rules=[('khwasa.final','uni073C',80,0,['uni071D','uni071D.fina']),('rwasa.lowered','uni073C',0,-60,['uni0718','uni0718.init','uni0718.medi','uni0718.fina']),('rukakha.beth','uni0742',0,-60,['uni0712','uni0712.init','uni0712.medi','uni0712.fina']),('rukakha.kaph.detached','uni0742',-220,530,['uni071F']),('rukakha.kaph.initial','uni0742',0,-40,['uni071F.init']),('rukakha.kaph.medial','uni0742',0,-40,['uni071F.medi']),('rukakha.kaph.final','uni0742',-180,220,['uni071F.fina']),('rukakha.gamal.isol','uni0742',0,180,['uni0713']),('rukakha.gamal.init','uni0742',0,260,['uni0713.init']),('rukakha.gamal.medi','uni0742',-180,180,['uni0713.medi']),('rukakha.gamal.fina','uni0742',0,180,['uni0713.fina']),('rukakha.taw','uni0742',0,-40,['uni072C','uni072C.init','uni072C.medi','uni072C.fina'])]
for name,src,dx,dy,targets in single_dot_rules:
 copy(name,src,0);zg=f['glyf'][name];anchor_x=(zg.xMin+zg.xMax)//2
 for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+dx,y+dy)
 zg.recalcBounds(f['glyf']);f['hmtx'][name]=(0,zg.xMin)
 markinfo.append((name,'bottom',anchor_x,zg.yMax-zg.yMin))
# Majliyana below Gamal: optical placement by positional form.
majliyana_rules=[('majliyana.gamal.isol',0,180,['uni0713']),('majliyana.gamal.connected',-180,180,['uni0713.init','uni0713.medi','uni0713.fina'])]
for name,dx,dy,targets in majliyana_rules:
 copy(name,'uni0330',0);zg=f['glyf'][name];anchor_x=(zg.xMin+zg.xMax)//2
 for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+dx,y+dy)
 zg.recalcBounds(f['glyf']);f['hmtx'][name]=(0,zg.xMin)
 markinfo.append((name,'bottom',anchor_x,zg.yMax-zg.yMin))
# Modern pronoun He: fuller round dot above, from original 0xF3.
copy('he.dot.above','oacute',0);zg=f['glyf']['he.dot.above'];zg.recalcBounds(f['glyf'])
dy=-zg.yMin
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x,y+dy)
zg.recalcBounds(f['glyf']);f['hmtx']['he.dot.above']=(0,zg.xMin)
markinfo.append(('he.dot.above','top',(zg.xMin+zg.xMax)//2,zg.yMax-zg.yMin))
# Taw–Alaph 0x46: center Rukakha toward the rounded Taw component.
copy('rukakha.taw.alaph.alt2','uni0742',0);zg=f['glyf']['rukakha.taw.alaph.alt2'];anchor_x=(zg.xMin+zg.xMax)//2
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+350,y+140)
zg.recalcBounds(f['glyf']);f['hmtx']['rukakha.taw.alaph.alt2']=(0,zg.xMin)
markinfo.append(('rukakha.taw.alaph.alt2','bottom',anchor_x,zg.yMax-zg.yMin))
# Taw–Alaph Seyame: optical shift right and down on both designs.
copy('seyame.taw.alaph','uni0308',0);zg=f['glyf']['seyame.taw.alaph'];anchor_x=(zg.xMin+zg.xMax)//2
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+260,y-160)
zg.recalcBounds(f['glyf']);f['hmtx']['seyame.taw.alaph']=(0,zg.xMin)
markinfo.append(('seyame.taw.alaph','top',anchor_x,zg.yMax-zg.yMin))
# Separate Seyame adjustment for the 0x46 Taw–Alaph design.
copy('seyame.taw.alaph.alt2','seyame.taw.alaph',0);zg=f['glyf']['seyame.taw.alaph.alt2']
anchor_x=next(m[2] for m in markinfo if m[0]=='seyame.taw.alaph')
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+100,y-80)
zg.recalcBounds(f['glyf']);f['hmtx']['seyame.taw.alaph.alt2']=(0,zg.xMin)
markinfo.append(('seyame.taw.alaph.alt2','top',anchor_x,zg.yMax-zg.yMin))
# Zqapha on both Taw–Alaph designs: right and down.
copy('zqapha.taw.alaph','uni0735',0);zg=f['glyf']['zqapha.taw.alaph'];anchor_x=(zg.xMin+zg.xMax)//2
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+180,y-160)
zg.recalcBounds(f['glyf']);f['hmtx']['zqapha.taw.alaph']=(0,zg.xMin)
markinfo.append(('zqapha.taw.alaph','top',anchor_x,zg.yMax-zg.yMin))
# Additional Zqapha optical shift for the 0x46 design.
copy('zqapha.taw.alaph.alt2','zqapha.taw.alaph',0);zg=f['glyf']['zqapha.taw.alaph.alt2']
anchor_x=next(m[2] for m in markinfo if m[0]=='zqapha.taw.alaph')
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+100,y-20)
zg.recalcBounds(f['glyf']);f['hmtx']['zqapha.taw.alaph.alt2']=(0,zg.xMin)
markinfo.append(('zqapha.taw.alaph.alt2','top',anchor_x,zg.yMax-zg.yMin))
# Pthaha on Taw–Alaph: shift the vertically aligned pair right.
copy('pthaha.taw.alaph','uni0732',0);zg=f['glyf']['pthaha.taw.alaph']
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+160,y)
zg.recalcBounds(f['glyf']);f['hmtx']['pthaha.taw.alaph']=(0,zg.xMin)
markinfo.append(('pthaha.taw.alaph','split',next(m[2] for m in markinfo if m[0]=='uni0732'),0))
# Additional rightward Pthaha shift for Taw–Alaph 0x46 only.
copy('pthaha.taw.alaph.alt2','pthaha.taw.alaph',0);zg=f['glyf']['pthaha.taw.alaph.alt2']
for i,(x,y) in enumerate(zg.coordinates):zg.coordinates[i]=(x+140,y)
zg.recalcBounds(f['glyf']);f['hmtx']['pthaha.taw.alaph.alt2']=(0,zg.xMin)
markinfo.append(('pthaha.taw.alaph.alt2','split',next(m[2] for m in markinfo if m[0]=='pthaha.taw.alaph'),0))
# Combined mark proof: preserve reviewed singles; explicit stacked outlines.
stack_rules=[];stack_bases=[]
for base in list(forms):
 for b in [base]+list(forms[base].values()):
  if b not in f['glyf']:continue
  bg=f['glyf'][b];bg.recalcBounds(f['glyf']);cx=(bg.xMin+bg.xMax)//2;top=max(650,bg.yMax)+75
  combos=[('uni0732','uni0308'),('uni0735','uni0308'),('uni0308','uni0303'),('uni0308','uni0303','uni0735')]
  for seq in combos:
   n='stack.'+b+'.'+'.'.join(seq);pen=TTGlyphPen(f.getGlyphSet());f.getGlyphSet()['rish.dotless' if base=='uni072A' else b].draw(pen)
   def drawmark(src,x,y):
    g=f['glyf'][src];g.recalcBounds(f['glyf']);f.getGlyphSet()[src].draw(TransformPen(pen,(1,0,0,1,x-(g.xMin+g.xMax)/2,y)))
   sy=705 if base=='uni072A' else top
   if base=='uni072B':sy-=100
   if base=='uni0728':sy-=100
   if 'uni0303' in seq:
    drawmark('uni0303',cx,top);sy=top+f['glyf']['uni0303'].yMax+90
   drawmark('uni0308',cx,sy)
   vowel_y=sy+f['glyf']['uni0308'].yMax+90
   if base in ['uni071A','uni071D','uni0728']:vowel_y-=40
   if 'uni0735' in seq:drawmark('uni0735',cx,vowel_y)
   if 'uni0732' in seq:
    src='pthaha.'+b if 'pthaha.'+b in f['glyf'] else 'uni0732'
    g=f['glyf'][src];cut=g.endPtsOfContours[0]+1
    # Split original/source dot outlines at their midpoint by vertical position.
    temp=deepcopy(g);ys=[y for x,y in temp.coordinates];mid=(min(ys)+max(ys))/2
    upperys=[y for x,y in temp.coordinates if y>mid];delta=vowel_y-min(upperys)
    for j,(x,y) in enumerate(temp.coordinates):
     temp.coordinates[j]=(x,y+delta if y>mid else y)
    tmp='temp.stack.pthaha';f['glyf'][tmp]=temp;f['hmtx'][tmp]=(0,temp.xMin)
    drawmark(tmp,cx,0)
   f['glyf'][n]=pen.glyph();f['glyf'][n].recalcBounds(f['glyf']);f['hmtx'][n]=(f['hmtx'][b][0],f['glyf'][n].xMin);old.append(n);stack_bases.append(n);stack_rules.append('sub '+b+' '+' '.join(seq)+' by '+n+';')
old=list(dict.fromkeys(old));f.setGlyphOrder(old);f['maxp'].numGlyphs=len(old)
# Expert-confirmed identities: legacy j/T is shin; legacy f is teth.
cmap[0x71b],cmap[0x72b]=cmap[0x72b],cmap[0x71b]
mapping['0x71b'],mapping['0x72b']=mapping['0x72b'],mapping['0x71b']
t=CmapSubtable.newSubtable(4);t.platformID=3;t.platEncID=1;t.language=0;t.cmap=cmap
u=CmapSubtable.newSubtable(4);u.platformID=0;u.platEncID=3;u.language=0;u.cmap=cmap;f['cmap'].tables=[u,t]
# Symbol-font flag removed; Unicode Syriac range declared.
f['OS/2'].ulCodePageRange1=0;f['OS/2'].ulCodePageRange2=0;f['OS/2'].ulUnicodeRange1=0;f['OS/2'].ulUnicodeRange2=1<<(71-32) if 71<64 else 0
f['OS/2'].ulUnicodeRange3=1<<(71-64);f['OS/2'].ulUnicodeRange4=0;f['OS/2'].usFirstCharIndex=min(cmap);f['OS/2'].usLastCharIndex=max(cmap)
f['OS/2'].sTypoAscender=1500;f['OS/2'].sTypoDescender=-1000;f['OS/2'].sTypoLineGap=100;f['OS/2'].usWinAscent=1600;f['OS/2'].usWinDescent=1100;f['hhea'].ascent=1500;f['hhea'].descent=-1000;f['hhea'].lineGap=100
# Preserve original copyright/provenance, but give the derivative a unique identity.
for id,value in {1:'Ishtar Syriac Unicode Alpha',2:'Regular',3:'IshtarSyriacUnicodeAlpha-0.001',4:'Ishtar Syriac Unicode Alpha',5:'Version 0.001; review prototype',6:'IshtarSyriacUnicodeAlpha-Regular',10:'Experimental Unicode conversion of Tony Khoshaba’s Ishtar XP. Original provenance preserved. Not a production release.'}.items():
 f['name'].removeNames(nameID=id)
 for platform,enc,lang in [(3,1,0x409),(1,0,0)]:f['name'].setName(value,id,platform,enc,lang)
fea=['languagesystem DFLT dflt;','languagesystem syrc dflt;','languagesystem syrc SYR;',"feature ccmp { sub uni072A uni0308 by rish.seyame; } ccmp;"]
for tag in ['init','medi','fina','fin2','fin3','med2']:
 rules=[f'sub {base} by {v[tag]};' for base,v in forms.items() if tag in v]
 if rules:fea.append(f'feature {tag} {{ '+ ' '.join(rules)+f' }} {tag};')
# Syriac Taw is right-joining: fina means attached to its predecessor.
# Final Alaph forms limit this rule to the word-final pair; marks are ignored.
fea.append('feature calt { lookupflag IgnoreMarks; sub uni072C.fina uni0710.fin2 by taw.alaph.alt1; sub uni072C.fina uni0710.fina by taw.alaph.alt1; sub uni072C uni0710.fin2 by taw.alaph.alt2; sub uni072C uni0710.fina by taw.alaph.alt2; } calt;')
fea.append('feature calt { '+' '.join(stack_rules)+' } calt;')
fea.append('feature dlig { sub uni0728 uni0722 by sadhe.nun.liga; sub uni0728.init uni0722.fina by sadhe.nun.liga; sub uni0728.medi uni0722.fina by sadhe.nun.liga; } dlig;')
fea.append('feature calt { sub uni0726.init uni032E by pe.fe.connected; sub uni0726.medi uni032E by pe.fe.connected; sub uni0726.fina uni032E by pe.fe.legacy; sub uni0726 uni032E by pe.fe.legacy; } calt;')
fea.append("feature ss01 { lookupflag IgnoreMarks; sub taw.alaph.alt2 by taw.alaph.alt1; sub uni072C uni0710 by taw.alaph.alt1; sub uni072C uni0710.fin2 by taw.alaph.alt1; sub uni072C uni0710.fina by taw.alaph.alt1; lookupflag 0; sub taw.alaph.alt1 [uni0308 seyame.taw.alaph seyame.taw.alaph.alt2]' by seyame.taw.alaph; sub taw.alaph.alt1 [uni0735 zqapha.taw.alaph zqapha.taw.alaph.alt2]' by zqapha.taw.alaph; sub taw.alaph.alt1 [uni0732 pthaha.taw.alaph pthaha.taw.alaph.alt2]' by pthaha.taw.alaph; } ss01;")
fea.append("feature ss02 { lookupflag IgnoreMarks; sub taw.alaph.alt1 by taw.alaph.alt2; sub uni072C uni0710 by taw.alaph.alt2; sub uni072C uni0710.fin2 by taw.alaph.alt2; sub uni072C uni0710.fina by taw.alaph.alt2; lookupflag 0; sub taw.alaph.alt2 [uni0742 rukakha.taw rukakha.taw.alaph.alt2]' by rukakha.taw.alaph.alt2; sub taw.alaph.alt2 [uni0308 seyame.taw.alaph seyame.taw.alaph.alt2]' by seyame.taw.alaph.alt2; sub taw.alaph.alt2 [uni0735 zqapha.taw.alaph zqapha.taw.alaph.alt2]' by zqapha.taw.alaph.alt2; sub taw.alaph.alt2 [uni0732 pthaha.taw.alaph pthaha.taw.alaph.alt2]' by pthaha.taw.alaph.alt2; } ss02;")
fea.append('feature ss08 { sub taw.alaph.alt1 by uni072C.fina uni0710.fin2; sub taw.alaph.alt2 by uni072C uni0710.fin2; } ss08;')
fea.append('feature ss06 { sub uni0725 by ain.isol.alt; } ss06;')
fea.append("feature calt { lookupflag IgnoreMarks; sub uni0720.init uni0710.fina' by alaph.after.lamadh; sub uni0720.medi uni0710.fina' by alaph.after.lamadh; sub uni0720 uni0710.fina' by alaph.after.lamadh; } calt;")
fea.append('feature ss07 { sub alaph.after.lamadh by uni0710.fina; } ss07;')
fea.append("feature ss03 { sub uni0717 uni071D by he.yudh.calligraphic; sub uni0717 uni071D.fina by he.yudh.calligraphic; sub uni0717.fina uni071D by he.yudh.calligraphic; } ss03;")
fea.append('feature calt { '+ ' '.join(f"sub {base} uni0732' by {mark};" for base,mark in pthaha_variants)+' } calt;')
fea.append("feature calt { sub [uni0728 uni0728.init uni0728.medi uni0728.fina uni072B uni072B.init uni072B.medi uni072B.fina] uni0735' by zqapha.lowered; } calt;")
zlameh_families=['uni0710','uni0712','uni0715','uni0718','uni0719','uni071A','uni071B','uni071D','uni071F','uni0720','uni0721','uni0722','uni0724','uni0725','uni0726','uni0728','uni0729','uni072A','uni072C']
zlameh_bases=[g for g in old if any(g==b or g.startswith(b+'.') for b in zlameh_families)]+['alaph.after.lamadh','rish.dotless','rish.seyame']
fea.append("feature calt { sub ["+' '.join(zlameh_bases)+"] uni0738' by zlameh.horizontal.lowered; } calt;")
fea.append("feature calt { sub [uni0713 uni0713.init] uni0738' by zlameh.horizontal.gamal; sub [uni0713.medi uni0713.fina] uni0738' by zlameh.horizontal.gamal.attached; } calt;")
fea.append("feature calt { sub [uni072B uni072B.init uni072B.medi uni072B.fina] uni0738' by zlameh.horizontal.teth; } calt;")

angular_families=['uni0710','uni0712','uni0718','uni071A','uni071B','uni071D','uni071F','uni0720','uni0721','uni0722','uni0724','uni0725','uni0726','uni0728','uni0729','uni072A','uni072C']
angular_bases=[g for g in old if any(g==b or g.startswith(b+'.') for b in angular_families)]+['alaph.after.lamadh','rish.dotless','rish.seyame']
fea.append("feature calt { sub ["+' '.join(angular_bases)+"] uni0739' by zlameh.angular.lowered; } calt;")

fea.append("feature calt { sub [uni0713 uni0713.init uni0713.medi uni0713.fina] uni0739' by zlameh.angular.gamal; sub [uni072B uni072B.init uni072B.medi uni072B.fina] uni0739' by zlameh.angular.teth; } calt;")

for name,src,dx,dy,targets in single_dot_rules:
 fea.append("feature calt { sub ["+' '.join(targets)+"] "+src+"' by "+name+"; } calt;")

for name,dx,dy,targets in majliyana_rules:
 fea.append("feature calt { sub ["+' '.join(targets)+"] uni0330' by "+name+"; } calt;")

fea.append("feature calt { sub [uni0717 uni0717.init uni0717.medi uni0717.fina] [uni0307 uni0741]' by he.dot.above; } calt;")

# Meem's combining dot below uses the approved fuller Rukakha outline.
fea.append("feature calt { sub [uni0721 uni0721.init uni0721.medi uni0721.fina] uni0323' by rukakha.beth; } calt;")

# Approved ligature mark placement applies in automatic mode as well.
fea.append("feature calt { sub taw.alaph.alt1 [uni0742 rukakha.taw rukakha.taw.alaph.alt2]' by rukakha.taw; sub taw.alaph.alt2 [uni0742 rukakha.taw rukakha.taw.alaph.alt2]' by rukakha.taw.alaph.alt2; sub taw.alaph.alt1 [uni0308 seyame.taw.alaph seyame.taw.alaph.alt2]' by seyame.taw.alaph; sub taw.alaph.alt2 [uni0308 seyame.taw.alaph seyame.taw.alaph.alt2]' by seyame.taw.alaph.alt2; sub taw.alaph.alt1 [uni0735 zqapha.taw.alaph zqapha.taw.alaph.alt2]' by zqapha.taw.alaph; sub taw.alaph.alt2 [uni0735 zqapha.taw.alaph zqapha.taw.alaph.alt2]' by zqapha.taw.alaph.alt2; sub taw.alaph.alt1 [uni0732 pthaha.taw.alaph pthaha.taw.alaph.alt2]' by pthaha.taw.alaph; sub taw.alaph.alt2 [uni0732 pthaha.taw.alaph pthaha.taw.alaph.alt2]' by pthaha.taw.alaph.alt2; } calt;")

bases=[g for g in old if g.startswith('uni07') and g not in [m[0] for m in markinfo]]+['uni0640','rish.dotless','rish.seyame','sadhe.nun.liga','pe.fe.legacy','pe.fe.connected','taw.alaph.alt1','taw.alaph.alt2','alaph.after.lamadh','he.yudh.calligraphic']
bases+=stack_bases
fea.append('@Bases = ['+' '.join(bases)+'];');fea.append('@Marks = ['+' '.join(m[0] for m in markinfo)+'];')
fea.append('table GDEF { GlyphClassDef @Bases, [], @Marks, []; } GDEF;')
for n,kind,cx,height in markinfo:fea.append(f'markClass {n} <anchor {cx} 0> @MC_{kind};')
fea.append('feature mark {')
for g in bases:
 glyph=f['glyf'][g];glyph.recalcBounds(f['glyf']);cx=(glyph.xMin+glyph.xMax)//2
 fea.append(f'pos base {g} <anchor {cx} {max(650,glyph.yMax)+75}> mark @MC_top <anchor {cx} {min(0,glyph.yMin)-65}> mark @MC_bottom <anchor {cx} 0> mark @MC_split;')
fea.append('} mark;');fea.append('feature mkmk {')
for n,kind,cx,height in markinfo:
 if kind!='split':fea.append(f'pos mark {n} <anchor {cx} {height+70 if kind=="top" else -height-70}> mark @MC_{kind};')
fea.append('} mkmk;')
(out/'IshtarSyriacUnicodeAlpha.fea').write_text('\n'.join(fea));addOpenTypeFeaturesFromString(f,'\n'.join(fea));f['head'].fontRevision=0.001
f.save(out/'IshtarSyriacUnicodeAlpha-Regular.ttf');(out/'mapping-provisional.json').write_text(json.dumps(mapping,indent=2));print('Built',len(cmap),'Unicode mappings;',len(old),'glyphs')
