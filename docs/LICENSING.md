# Licensing — closed as a release blocker

**Project decision, 2026-10-26:** Tony Khoshaba approved closing the licensing investigation as a release blocker and continuing font/keyboard debugging. The project adopts **SIL Open Font License 1.1** for Ishtar font software, supplied with `OFL.txt` and the required copyright/credit notices.

## Basis

Tony reports that Sargon Hasso directly supplied the Sparksoft Systems Syriac-Fonts repository and explained that Dr. Marcus's original fonts had been made public to address the licensing concern. The published repository explicitly licenses its font families under OFL 1.1. Its FONTLOG records the January 2025 reassignment from Syriac Advanced Software to Sparksoft Systems and OFL re-release. It credits Sargon Hasso and Esho Marcus and dates the initial East Syriac Marcus release to 1997.

- [Upstream repository](https://github.com/SparksoftSystems/Syriac-Fonts)
- [Pinned license](https://github.com/SparksoftSystems/Syriac-Fonts/blob/35c96f4d59613089e79a6f44f81d946b4bff5de5/OFL.txt)
- [Pinned font history](https://github.com/SparksoftSystems/Syriac-Fonts/blob/35c96f4d59613089e79a6f44f81d946b4bff5de5/FONTLOG.txt)

This records the project's accepted source/license basis, relying on the published grant and the clarification from an identified upstream contributor. The complete point-by-point ancestry of the 1990s Nisibus-labelled file has not been reconstructed. That remains historical documentation, not an active release blocker or a claim of a completed forensic ownership audit. No additional inquiry to Dr. Marcus is required by the project decision.

## Distribution requirements

Keep `OFL.txt` and the copyright/credit notices with the font, including in keyboard packages. Modified font software remains under OFL. Do not use the reserved primary font names Marcus or Nohadra for a derivative without permission. Do not sell the font by itself. The license permits sharing, modification, embedding and redistribution subject to its terms. Documents made with the font, including Kokhva PDFs, are not required to adopt OFL.

The license covers this project's font software and accompanying project build/keyboard material distributed as part of that font software. Third-party compiler/runtime dependencies retain their own licenses and are not relicensed by this file. See `NOTICE.md` for credits.

## Release status

Licensing is closed as a project blocker. This does not certify font quality: mixed-mark review, Kokhva appearance feedback, device installation, keyboard interoperability, coverage and final version metadata remain technical release tasks. Updating these documents does not change repository visibility, enable Pages or publish a tagged release.
