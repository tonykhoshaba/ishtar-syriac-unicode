# Known limitations of the working preview

- This is a preview build, not a certified complete Syriac Unicode font.
- The keyboard currently reports 39 mappings containing one or more characters absent from the font. These include everyday punctuation and less common symbols/extended letters. See `keyboard/compatibility.json`; the browser may show fallback-font glyphs for those keys.
- Existing Ramsina keyboard assignments are retained exactly. Some use generic combining-dot characters where another key uses a Syriac-specific mark. These distinctions need documenting/testing; text is not silently rewritten.
- Single-mark and selected ligature proofs were reviewed by Tony. Some combined vowel/Seyame placements remain provisional, and input mark-order coverage needs further testing.
- Word-final Taw–Alap automation and explicit overrides have shaping checks. Every override/mark combination has not yet received visual review.
- Manual font features are application-dependent. The demo’s word-specific overrides are saved locally in the browser; plain-text export loses styling.
- The keyboard is a browser implementation, not a native system keyboard or mobile touch layout.
- Only the current local browser and Python/HarfBuzz shaping checks are verified. Windows/macOS/Linux desktop applications and mobile applications still require interoperability testing.
- Working font internal names/version still say Alpha/0.001. Final preview release metadata must be set consistently before shipping.
- Original-outline and keyboard provenance/licenses remain unresolved. Public distribution is blocked until resolved.

Version 1 will focus on practical coverage and reliable typing. Real text from a Kokhva issue will guide later refinement rather than hypothetical per-letter mark combinations.

## 2026-10-26 update

The package now includes Keyman desktop/mobile files and phone/tablet layouts. Real-device testing is still pending. Font coverage gaps now affect 38 mappings; U+2010 and U+0723 have been added from existing Ishtar outlines. Five new mixed-mark review sheets are prepared, including connected Gamal/Kaph forms; their visual approval is pending. Twenty-five Seyame entry-order tests pass, and all 264 approved single-mark render comparisons remain unchanged. A complete 12-page Kokhva Ishtar comparison was rendered locally with unchanged transcription.
