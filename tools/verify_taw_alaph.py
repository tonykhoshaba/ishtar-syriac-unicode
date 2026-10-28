from pathlib import Path
import uharfbuzz as hb
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1];p=R/'output/IshtarSyriacUnicode-Regular.ttf';font=TTFont(p);h=hb.Font(hb.Face(p.read_bytes()))
def shape(t,features=None):
 b=hb.Buffer();b.add_str(t);b.guess_segment_properties();hb.shape(h,b,features or {});return [font.getGlyphName(g.codepoint) for g in b.glyph_infos]
for text,expected in [('ܬܐ','alt2'),('ܒܬܐ','alt1'),('ܕܬܐ','alt2'),('ܪܬܐ','alt2'),('ܒܬܵܐ','alt1'),('ܒܬܐ،','alt1')]:
 assert 'taw.alaph.'+expected in shape(text),(text,shape(text))
for text in ['ܬܐܒ','ܒܬܐܒ','ܬܐܕ','ܬܐܬ','ܒܬܐܝ']:
 assert not any(g.startswith('taw.alaph.') for g in shape(text)),(text,shape(text))
for text in ['ܬܐ','ܒܬܐ','ܕܬܐ']:
 assert not any(g.startswith('taw.alaph.') for g in shape(text,{'ss08':1}))
 assert 'taw.alaph.alt2' in shape(text,{'ss02':1})
 assert 'taw.alaph.alt1' in shape(text,{'ss01':1})
print('Passed automatic joining/word-final/mark checks and explicit form overrides.')
