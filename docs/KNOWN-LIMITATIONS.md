# Known limitations in Version 1

- **Character coverage:** 38 keyboard assignments include characters outside Ishtar's drawn coverage. Those characters remain Unicode text and may use a fallback font. This font is primarily Syriac; Latin text generally uses a companion font. See `keyboard/compatibility.json` for the exact assignments.
- **Combined marks:** Lamad and Gamal corrections received focused visual approval, along with earlier vowel and mark reviews. Not every possible combination on every letter has been approved. Rare combinations may need more optical adjustment.
- **Classical Syriac:** below-letter Talqana is encoded and supported, but its usage and placement are deferred for later review. Version 1's review emphasis is Modern Assyrian/Eastern Syriac text.
- **Mobile and desktop interoperability:** browser testing and compiled keyboard checks are completed; Tony has also begun Ubuntu/LibreOffice testing. This is not certification of every application or operating system. iPhone setup did not work smoothly in initial testing; native mobile installation and cross-app display need further feedback.
- **Fonts and keyboards are separate:** a keyboard enters characters; the receiving app chooses the display font. A successful keyboard installation does not make Ishtar available in every mobile app or in Google Docs.
- **Optional ligatures:** stylistic-set controls depend on application support. Plain text cannot preserve an explicitly selected alternate. He–Yod is retained as an optional calligraphic form rather than imposed automatically without a confirmed rule.
- **Existing encodings:** the familiar Ramsina-compatible assignments retain their reviewed generic or Syriac-specific combining characters. The keyboard does not silently normalize or reinterpret existing text.

Future versions will address reproducible defects and extend testing. Google Fonts/Docs inclusion is a recorded future action, not an approved or scheduled integration.

## Character coverage planned for future versions

The additional characters below are deferred from Version 1 and recorded for future coverage work. Priorities will follow Modern Assyrian usage and user feedback. Adding them will require suitable designs, combining-mark placement where applicable, and review. No release date is assigned. Until supported, applications may display these characters using another font.

The 38 affected keyboard assignments represent 34 distinct characters; all 22 core Syriac letters are already covered.

| Unicode | Character name |
| --- | --- |
| U+007B | Left Curly Bracket |
| U+007D | Right Curly Bracket |
| U+0304 | Combining Macron |
| U+0324 | Combining Diaeresis Below |
| U+032D | Combining Circumflex Accent Below |
| U+060C | Arabic Comma |
| U+061B | Arabic Semicolon |
| U+061F | Arabic Question Mark |
| U+0651 | Arabic Shadda |
| U+0700 | Syriac End Of Paragraph |
| U+0701 | Syriac Supralinear Full Stop |
| U+0702 | Syriac Sublinear Full Stop |
| U+0703 | Syriac Supralinear Colon |
| U+0704 | Syriac Sublinear Colon |
| U+0705 | Syriac Horizontal Colon |
| U+0708 | Syriac Supralinear Colon Skewed Left |
| U+0709 | Syriac Sublinear Colon Skewed Right |
| U+070A | Syriac Contraction |
| U+070B | Syriac Harklean Obelus |
| U+070C | Syriac Harklean Metobelus |
| U+070D | Syriac Harklean Asteriscus |
| U+070F | Syriac Abbreviation Mark |
| U+0711 | Syriac Letter Superscript Alaph |
| U+0714 | Syriac Letter Gamal Garshuni |
| U+071C | Syriac Letter Teth Garshuni |
| U+0743 | Syriac Two Vertical Dots Above |
| U+0744 | Syriac Two Vertical Dots Below |
| U+0745 | Syriac Three Dots Above |
| U+0746 | Syriac Three Dots Below |
| U+250C | Box Drawings Light Down And Right |
| U+2510 | Box Drawings Light Down And Left |
| U+25CC | Dotted Circle |
| U+2670 | West Syriac Cross |
| U+2671 | East Syriac Cross |
