"""Attach the owner-adopted OFL/credits without changing font design tables."""
from pathlib import Path
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1]
def apply_ofl_metadata(font):
 original=font['name'].getDebugName(0) or ''
 upstream='Copyright (c) 1997-2025, Sparksoft Systems. Reserved Font Names: Marcus, Nohadra.'
 if upstream not in original:original += '\n'+upstream+'\nCopyright (c) 1998-2026, Tony Khoshaba (Ishtar modifications and Unicode conversion).'
 values={0:original,13:(R/'OFL.txt').read_text(),14:'https://openfontlicense.org/'}
 for id,value in values.items():
  font['name'].removeNames(nameID=id)
  for platform,encoding,language in [(3,1,0x409),(1,0,0)]:font['name'].setName(value,id,platform,encoding,language)
if __name__=='__main__':
 import hashlib,json
 p=R/'output/IshtarSyriacUnicode-Regular.ttf';f=TTFont(p)
 before={k:hashlib.sha256(f.getTableData(k)).hexdigest() for k in f.keys() if k not in ['GlyphOrder','name','head']}
 apply_ofl_metadata(f);f.save(p);g=TTFont(p)
 after={k:hashlib.sha256(g.getTableData(k)).hexdigest() for k in g.keys() if k not in ['GlyphOrder','name','head']}
 assert before==after,'Unexpected design/shaping table change'
 (R/'output/license-metadata-check.json').write_text(json.dumps({'license':'SIL OFL 1.1','design_and_shaping_tables_unchanged':True,'verified_tables':sorted(before),'font_sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2)+'\n')
 print('OFL metadata added; all design, metrics, mapping and shaping tables unchanged')
