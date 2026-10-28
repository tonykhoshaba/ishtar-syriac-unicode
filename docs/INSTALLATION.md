# Installation

## Windows

Open `IshtarSyriacUnicode-Regular.ttf` and choose Install. Restart the application if needed, then select **Ishtar Syriac Unicode**. For typing, install Keyman from its official website and open `ishtar_syrc.kmp`. Use the English US physical-key positions with Shift and right Alt/AltGr.

## macOS

Open the TTF in Font Book and install it. Select **Ishtar Syriac Unicode** in the target application. For typing, install Keyman for macOS and the KMP package; Option/Alt behavior depends on the keyboard hardware and application.

## Linux

Install the TTF using your desktop font installer, or place it in `~/.local/share/fonts/` and run `fc-cache -f`. Select the font in LibreOffice or another compatible application. Keyman for Linux uses IBus integration; follow the current official Keyman installation guide for your distribution.

## iPhone/iPad and Android

Install Keyman and open/share `ishtar_syrc.kmp` to Keyman. Enable its keyboard using the device's keyboard settings. Phone and tablet layouts are included. Touch: Shift gives alternate letters/digits; Alt gives extra marks; 123 opens punctuation; hold a key for alternatives.

The bundled font is intended for Keyman's editor and environments that support it. Installing a keyboard does not install Ishtar into every mobile app. Messages, Notes, WhatsApp and other apps may use a different Syriac font. Native mobile installation and app behavior need more testing. The browser tester is the easiest way to inspect Ishtar on a phone without installation.

Official downloads and help: [Keyman downloads](https://keyman.com/downloads/), [Keyman help](https://help.keyman.com/).

## Web

Use the WOFF2 with CSS `@font-face` and `direction: rtl` for Syriac text. The included `keyboard/` demo loads it directly. No operating-system font installation is needed. Keep Unicode text unchanged; avoid converting it to the old Ishtar ASCII encoding.

## Upgrading from the review build

Select **Ishtar Syriac Unicode** in your documents. Refresh web pages after a font update; a hard refresh may be needed if a browser retains an older copy. The keyboard ID stays `ishtar_syrc`, with its version advanced to 1.0.0.

## Taw–Alap alternatives

Type Taw then Alap. The font selects the word-final design from the joining context. Applications that expose OpenType stylistic sets can use `ss01` for the attached design, `ss02` for the detached design and `ss08` for separate letters. The browser demo offers word-specific preview controls. Plain-text files do not preserve font-feature choices.

## Sharing documents

Other readers need Ishtar selected in their application to see its exact shapes. Use a PDF with the font embedded when appearance must be preserved. A plain-text export carries Unicode characters, not the font or its layout settings.
