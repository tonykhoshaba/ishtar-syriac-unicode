# Building the font and keyboard

These commands require the source archive or GitHub checkout; the smaller user download contains the ready-to-install files.

Use Python 3 with the pinned `requirements.txt` in a virtual environment. The build reads `originals/ISHAR_XP.ttf` and writes `output/IshtarSyriacUnicode-Regular.ttf` plus an OpenType feature file and mapping report.

```
python tools/build_font.py
python tools/build_keyboard.py
python tools/build_keyman.py
python tools/verify_font.py
python tools/verify_taw_alaph.py
```

The proof renderers use DejaVu Sans for English labels. These label outlines are not copied into Ishtar.

Use Node 20 or later and the pinned Keyman compiler lockfile:

```
npm ci --prefix keyman/compiler
keyman/compiler/node_modules/.bin/kmc --no-error-reporting build keyman/source/ishtar_syrc.kmn -o keyman/build/ishtar_syrc.kmx
keyman/compiler/node_modules/.bin/kmc --no-error-reporting build keyman/source/ishtar_syrc.kps -o keyman/build/ishtar_syrc.kmp
node tools/verify_keyman.cjs
```

To generate WOFF2 after a font rebuild:

```
python -c "from fontTools.ttLib import TTFont; f=TTFont('output/IshtarSyriacUnicode-Regular.ttf'); f.flavor='woff2'; f.save('output/IshtarSyriacUnicode-Regular.woff2')"
```

Font timestamps can vary between builds. Match glyph outlines, Unicode mapping, shaping tables, metrics and release metadata when auditing reproducibility. The published archive's SHA256SUMS.txt identifies the exact distributed files.
