# Ishtar Syriac Unicode

Ishtar Syriac Unicode is an Eastern Syriac typeface for reading, writing and preserving Assyrian text. Version 1 brings the historical Ishtar designs into Unicode, with contextual letter forms, vowels and combining marks, and a companion keyboard based as closely as practical on the familiar Ramsina QWERTY layout.

Tony Khoshaba worked on the original Ishtar letterforms and vowel placement in 1998–1999 under the guidance of **the late Rabi Yoab Benjamin**. This edition builds on that work through Unicode mapping, OpenType shaping and careful visual review. “Rabi” is an Assyrian title of respect for a teacher, learned person or expert.

The project also acknowledges the historical type design of Esho Marcus, the OpenType work and source clarification of Sargon Hasso, and Sparksoft Systems' publication of the upstream font families. Full credits and the adopted source history appear in [NOTICE.md](NOTICE.md) and [PROVENANCE.md](docs/PROVENANCE.md).

## Sample text

ܝܠܘܿܦ ܘܡܲܠܹܦ ܠܸܫܵܢܵܐ ܕܝܸܡܘܼܟܼ  
ܐܸܢ ܠܹܐ ܒܵܥܹܝܬ ܕܬܵܠܹܩ ܫܸܡܘܼܟܼ

## Download and use

The Version 1 release package contains:

- **IshtarSyriacUnicode-Regular.ttf** — desktop font for compatible Windows, macOS and Linux applications.
- **IshtarSyriacUnicode-Regular.woff2** — font for websites.
- **ishtar_syrc.kmp** — Keyman keyboard package with desktop, phone and tablet layouts and the matching Ishtar font.
- Installation instructions, keyboard reference, release notes, font license and credits.

Install the font, then select **Ishtar Syriac Unicode** in your application. The keyboard produces ordinary Unicode text; it does not force applications to display the Ishtar font. Mobile apps control which fonts they use. See [installation and platform notes](docs/INSTALLATION.md).

Try the [public web keyboard](https://assyrian-text-test.netlify.app/keyboard/) or [phone/tablet keyboard](https://assyrian-text-test.netlify.app/keyboard/keyman-preview). The live site can receive improvements after this tagged release; the downloadable Version 1 files are the fixed reference build.

## Kokhva issue sample

A complete 12-page Kokhva issue is included as a [PDF typeset in Ishtar Syriac Unicode 1.0.0](samples/Kokhva-1911-Ishtar-v1.0.0.pdf). It demonstrates the font in extended newspaper text. The Kokhva transcription belongs to a separate corpus project that remains a work in progress; the full corpus will be released later.

## Included features

- The 22 core Syriac letters and reviewed joining forms, including distinct final Lamad and attached-final Gamal.
- Eastern vowels, Seyame, Rukakha, Majliyana, dotted He and Talqana.
- Automatic word-final Taw–Alap selection following the joining rule described in Yoab's lectures.
- Optional OpenType stylistic sets for supported ligature and calligraphic alternatives.
- A Ramsina-compatible keyboard preserving 119 existing assignments, with three additions in unused positions.

Version 1 is a usable first release. Some uncommon combinations and application-specific behavior remain candidates for later refinement. See [known limitations](docs/KNOWN-LIMITATIONS.md) and [release notes](docs/RELEASE-NOTES.md).

## Build from source

Install Python requirements in a virtual environment, then run:

```sh
python tools/build_font.py
python tools/build_keyboard.py
python tools/build_keyman.py
python tools/verify_font.py
python tools/verify_taw_alaph.py
```

For Keyman compilation and verification, follow [BUILDING.md](docs/BUILDING.md). `originals/ISHAR_XP.ttf` is the historical outline input; it retains its original metadata. The project source/license basis is documented in [LICENSING.md](docs/LICENSING.md).

For a local browser demo, run `python3 -m http.server 8877 --bind 127.0.0.1` from the repository and open `http://127.0.0.1:8877/keyboard/`.

## License and feedback

Font software is distributed under the **SIL Open Font License 1.1**. Keep [OFL.txt](OFL.txt) and the required notices with redistributed copies. Upstream reserved font names are Marcus and Nohadra; this derivative is named Ishtar. Third-party tools retain their own licenses.

Please report bugs through GitHub Issues with the exact Unicode text, app/browser and operating-system versions, the Ishtar version, a screenshot and the expected appearance. Improvements will be released in later versions. The Google Fonts/Google Docs request is a future action, not a feature of this release.
