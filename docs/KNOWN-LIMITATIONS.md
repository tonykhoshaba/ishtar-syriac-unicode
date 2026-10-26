# Known limitations — font and keyboard debugging

Licensing is closed as a release blocker; see [LICENSING.md](LICENSING.md). Current limitations are technical:

- Working family/version remains Alpha/0.001; final release metadata is pending.
- Thirty-eight keyboard mappings include characters not drawn by Ishtar; fallback fonts may supply them. See `keyboard/compatibility.json`.
- Combined vowel/Seyame, Talqana and below-mark placements are candidates pending visual approval. Five review sheets include connected Gamal/Kaph cases. Twenty-five Seyame entry-order checks pass; 264 single-mark render comparisons were unchanged.
- Kokhva has a complete 12-page Ishtar comparison with unchanged reviewed text; Tony is reviewing the PDFs for font defects.
- All 122 keyboard outputs pass compiled-rule checks. Actual installation/app tests on iPhone, Windows and Linux are pending; phone/tablet layouts and desktop Keyman packages exist.
- Mobile applications select their own display font. Inspect Ishtar inside Keyman first; other apps may display another Syriac font.
- OpenType stylistic sets and word-level overrides depend on application support. Plain text cannot preserve font-feature choices.
- Not every Taw–Alaph override/mark combination has received visual review.
- Existing reviewed key encodings are preserved, including generic versus Syriac-specific combining marks; text is not silently rewritten.

Report issues using exact Unicode text, font build, app/device/version and a screenshot. Debug the actual Ishtar build; the optional Noto tester kit checks input only.
