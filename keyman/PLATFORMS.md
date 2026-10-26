# Ishtar Syriac keyboard — private test 0.1.0

One package, `build/ishtar_syrc.kmp`, contains desktop KMX, mobile JavaScript, phone/tablet touch layouts, the Ishtar font, and help. It preserves all 119 existing Ramsina mappings plus the three reviewed additions. Keyman 14 or later is required; current Keyman is recommended.

| Platform | Installation | Status |
| --- | --- | --- |
| Windows | Install Keyman, open the KMP, then select Ishtar in Keyman. Use English US physical keys, Shift and right Alt/AltGr. | Compiled; device test pending |
| macOS | Install Keyman for macOS, open the KMP, select Ishtar from the input menu. Check right Option/Alt behavior on your hardware. | Compiled; device test pending |
| Linux | Install Keyman for Linux and its IBus integration, open the KMP and select the Ishtar input method. | Compiled; desktop integration test pending |
| Android phone/tablet | Install Keyman, transfer/open the KMP using the device's Open with/Share → Keyman action, enable Keyman in system keyboard settings and select it. | Phone and tablet layouts included; device test pending |
| iPhone/iPad | Install Keyman, transfer the KMP through Files or a private download and open/share it to Keyman. Enable Keyman under Settings → General → Keyboard → Keyboards → Add New Keyboard. | Phone and tablet layouts included; device test pending |

Keyman downloads: https://keyman.com/downloads/
Package format and mobile font limits: https://help.keyman.com/developer/19.0/reference/file-types/kps
Custom keyboard installation: https://help.keyman.com/products/iphone-and-ipad/current-version/basic/keyboard-install

Touch: top row contains vowels/marks, Shift gives digits. Shift and Alt select alternate layers; 123 opens punctuation. Hold a key for its alternatives. Menu switches keyboards. Ordinary typing produces Unicode, so text remains usable with other Syriac fonts.

The bundled font works in Keyman's app and keyboard on mobile. It does not replace fonts in Messages, WhatsApp, Notes or other apps; those apps may display another Syriac font. Font styling and Taw–Alaph stylistic alternates require application support. Do not insert private characters to force glyph forms.

Suggested device test: type `ܫܠܵܡܵܐ ܒܬܐ ܕܬܐ ܪ̈ ܡ̣ܢ ܒ݇̈`; try Shift, Alt, punctuation, digits, long press, backspace, copy/paste, portrait and landscape. Test a native text app as well as Keyman's editor. Record device/OS/app and what fails.

The compiler succeeds and all 122 compiled outputs match the source mapping. This is not a claim of completed testing on five operating systems. Some less-used Ramsina key outputs are not drawn in Ishtar yet and use fallback fonts; see `../keyboard/compatibility.json`.

Private evaluation only. The original font outline license remains unresolved. This package is not a public release.

Build (Node 20+): install the pinned compiler with `npm ci --prefix compiler`; run `python ../tools/build_keyman.py`, then `compiler/node_modules/.bin/kmc --no-error-reporting build source/ishtar_syrc.kmn -o build/ishtar_syrc.kmx` and the same command for `source/ishtar_syrc.kps -o build/ishtar_syrc.kmp`.
