# Installation and platform status

## Font versus keyboard

Installing the font changes the available typeface. Installing a keyboard changes how keystrokes produce Unicode text. One does not install the other.

The same TTF file is intended for desktop applications on Windows, macOS and Linux. Platform/app interoperability still needs testing; only local browser and shaping-engine checks have been completed.

- Windows: install the TTF through Windows Fonts, then select Ishtar in the application.
- macOS: install using Font Book, then select Ishtar in the application.
- Linux: use the desktop font installer or the user’s font directory and refresh the font cache as appropriate.
- iPhone/iPad: font availability depends on font installation support and the target app. An installed keyboard cannot force the target application to use Ishtar.
- Android: applications can bundle this font or expose compatible custom-font support. System-wide font replacement is not part of this package.
- Web: serve the keyboard/static site with its adjacent `output/` font resources. Visitors do not need a desktop font installation.

No native desktop keyboard installers or mobile touch keyboard packages are included yet. The included QWERTY keyboard runs inside the browser demo. Any already installed Syriac Unicode keyboard can also be used with the font, subject to its character coverage.

## Taw–Alap

Type Taw then Alap. The font chooses the attached or detached design at word end from the joining context. In applications exposing the relevant OpenType features: ss01 forces the attached design, ss02 the detached design, and ss08 separate letters. The browser prototype exposes these as word-specific preview controls. Plain text cannot retain OpenType styling choices.

## Sharing

Recipients of Unicode text may see another Syriac font if their app does not use Ishtar. Use a properly generated PDF with embedded fonts when preserving appearance matters and the final font license permits embedding. The keyboard demo’s text export is plain text; its saved local preview formatting is not embedded in that export.
