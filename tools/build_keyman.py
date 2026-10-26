"""Build Keyman sources from the same mapping used by the review keyboard."""
from pathlib import Path
import json,shutil,unicodedata,html
R=Path(__file__).resolve().parents[1];D=R/'keyman';S=D/'source';B=D/'build';S.mkdir(exist_ok=True);B.mkdir(exist_ok=True)
m=json.loads((R/'keyboard/ishtar-qwerty.json').read_text());family='Ishtar Syriac Unicode Alpha'
codes={'Space':'K_SPACE','Backquote':'K_BKQUOTE','Minus':'K_HYPHEN','Equal':'K_EQUAL','BracketLeft':'K_LBRKT','BracketRight':'K_RBRKT','Backslash':'K_BKSLASH','Semicolon':'K_COLON','Quote':'K_QUOTE','Comma':'K_COMMA','Period':'K_PERIOD','Slash':'K_SLASH'}
def code(k):return codes.get(k,'K_'+k.removeprefix('Key').removeprefix('Digit'))
lines=["store(&VERSION) '14.0'","store(&NAME) 'Ishtar Syriac — Ramsina layout'","store(&KEYBOARDVERSION) '0.1.0'","store(&TARGETS) 'any'","store(&LAYOUTFILE) 'ishtar_syrc.keyman-touch-layout'","store(&CAPSALWAYSOFF) '1'","store(&KMW_RTL) '1'",'begin Unicode > use(main)','group(main) using keys']
for k,v in m.items():
 mods,key=k.split(':');prefix=('RALT ' if 'A' in mods else '')+('SHIFT ' if 'S' in mods else '')
 lines.append('+ ['+prefix+code(key)+'] > '+(' '.join('U+%04X'%ord(c) for c in v) if v else 'nul'))
(S/'ishtar_syrc.kmn').write_text('\n'.join(lines)+'\n')
modlayers={'default':'','shift':'S','rightalt':'A','rightalt-shift':'AS'}
def label(t):
 if not t:return '∅'
 if t=='\u200c':return 'ZWNJ'
 if t=='\u200d':return 'ZWJ'
 if t=='\u200f':return 'RLM'
 return ('◌'+t) if unicodedata.combining(t[0]) else t
used=set()
def key(k,mod='',layer=None):
 sig=mod+':'+k;t=m.get(sig,'');out={'id':code(k),'text':label(t)}
 if layer:out['layer']=layer
 if sig not in m:out['text']='';out['sp']='9'
 if sig in m:used.add(sig)
 subs=[]
 for ml,mm in modlayers.items():
  alt=mm+':'+k
  if mm!=mod and alt in m and m[alt]:subs.append({'id':code(k),'text':label(m[alt]),'layer':ml});used.add(alt)
 if subs:out['sk']=subs
 return out
def special(id,text,nextlayer=None,width='100'):
 d={'id':id,'text':text,'sp':'1','width':width}
 if nextlayer:d['nextlayer']=nextlayer
 if id=='K_SPACE':d['layer']='default'
 return d
layers=[]
for lid,mod in modlayers.items():
 shift='default' if lid=='shift' else 'rightalt' if lid=='rightalt-shift' else 'rightalt-shift' if lid=='rightalt' else 'shift'
 alt='default' if lid=='rightalt' else 'shift' if lid=='rightalt-shift' else 'rightalt-shift' if lid=='shift' else 'rightalt'
 rows=[[key('Digit'+d,mod) for d in '1234567890'],[key('Key'+c,mod) for c in 'QWERTYUIOP'],[key('Key'+c,mod) for c in 'ASDFGHJKL'],[special('K_SHIFT','*Shift*',shift)]+[key('Key'+c,mod) for c in 'ZXCVBNM']+[special('K_BKSP','*BkSp*')],[special('K_SYMBOLS','123', 'symbols'),special('K_RALT','Alt',alt),special('K_SPACE','*Space*',width='350'),key('Period','', 'default'),special('K_ENTER','*Enter*'),special('K_LOPT','*Menu*')]]
 layers.append({'id':lid,'row':[{'id':i+1,'key':r} for i,r in enumerate(rows)]})
punc=['Backquote','Minus','Equal','BracketLeft','BracketRight','Backslash','Semicolon','Quote','Comma','Period','Slash']
rows=[[key('Digit'+d,'S','shift') for d in '1234567890'],[key(k,'','default') for k in punc[:6]],[key(k,'','default') for k in punc[6:]],[special('K_ALPHA','ܐܒܓ','default'),special('K_LOPT','*Menu*'),special('K_SPACE','*Space*',width='350'),special('K_BKSP','*BkSp*'),special('K_ENTER','*Enter*')]]
layers.append({'id':'symbols','row':[{'id':i+1,'key':r} for i,r in enumerate(rows)]})
layout={p:{'font':family,'fontsize':'1em','layer':layers} for p in ['phone','tablet']};(S/'ishtar_syrc.keyman-touch-layout').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
# Space is handled as the standard space key, identically on desktop and touch.
used.add(':Space');assert set(m)<=used,sorted(set(m)-used)
shutil.copy2(R/'output/IshtarSyriacUnicodeAlpha-Regular.ttf',S)
help='''<!doctype html><meta charset="utf-8"><title>Ishtar Syriac keyboard</title><h1>Ishtar Syriac — Ramsina layout</h1><p>Private test package 0.1.0. Unicode text, with the familiar physical Ramsina QWERTY mapping. On desktop use Shift and right Alt (AltGr). On phones and tablets use Shift, Alt and 123; hold a key for alternatives. The top row contains vowels and marks; Shift gives digits.</p><p>Talqana: desktop backslash; mobile 123 then backslash-position silencer key. Seyame: 0 on the main layer. Dot below: 8. Rukakha: Alt+R or the consonant shortcuts. Above Majliyana: Alt+F. He dot above: Alt+H.</p><p>Taw–Alaph joins automatically in Ishtar. OpenType alternates require an application that supports stylistic sets; a system keyboard cannot force a font feature in every app. Text always remains ordinary Syriac Unicode.</p><p>Mobile: install Keyman, then open this KMP package in Keyman and enable its keyboard in system settings. iPhone/iPad: Settings → General → Keyboard → Keyboards → Add New Keyboard → Keyman. Android: enable Keyman in system keyboard settings and choose it as the input method. Desktop: install Keyman for Windows, macOS or Linux, then open the KMP package.</p><p>The included font is available inside Keyman on mobile; other apps choose their own display font. Installing a keyboard does not replace the system font. Device installation and typing still need testing. Private evaluation only: the original outline license is unresolved. No public redistribution license is granted.</p>'''
for n in ['welcome.htm','readme.htm']:(S/n).write_text(help)
files=['../build/ishtar_syrc.kmx','../build/ishtar_syrc.js','IshtarSyriacUnicodeAlpha-Regular.ttf','welcome.htm','readme.htm']
kps='''<?xml version="1.0" encoding="utf-8"?><Package><System><KeymanDeveloperVersion>18.0</KeymanDeveloperVersion><FileVersion>7.0</FileVersion></System><Options><ReadMeFile>readme.htm</ReadMeFile><WelcomeFile>welcome.htm</WelcomeFile><FollowKeyboardVersion/></Options><Info><Name>Ishtar Syriac — Ramsina layout (private test)</Name><Author>Tony Khoshaba</Author><Description>Unicode Eastern Syriac keyboard with phone and tablet layouts</Description></Info><Files>'''+''.join('<File><Name>'+f+'</Name></File>' for f in files)+'''</Files><Keyboards><Keyboard><ID>ishtar_syrc</ID><Languages><Language ID="aii">Assyrian Neo-Aramaic</Language></Languages></Keyboard></Keyboards></Package>'''
(S/'ishtar_syrc.kps').write_text(kps)
(D/'touch-coverage.json').write_text(json.dumps({'mapping_entries':len(m),'reachable_on_touch':len(set(m)&used),'unreachable':sorted(set(m)-used),'device_tested':False},indent=2)+'\n')
print('Generated desktop rules and phone/tablet layouts:',len(m),'mapping entries reachable')
