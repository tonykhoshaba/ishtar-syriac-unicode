# Ishtar QWERTY keyboard review

Browser keyboard prototype based on the exact mapping in the existing Ramsina review editors. All original mappings are preserved, including AltGr, Shift and empty Shift+Y. It inserts Unicode text, not legacy Ishtar character positions. This is not yet an operating-system keyboard installer.

New unoccupied keys: Right Alt+H = He + U+0307; Right Alt+R = U+0742 Rukakha; Right Alt+F = U+0303 tilde above. Existing Shift+K/T/B encodings remain as in the Ramsina editor, even where similar-looking marks have different code points. These remain explicit review items; do not silently normalize them.

The Taw–Alap selector controls font features ss01 / ss02 for the entire typing field. These choices are presentation settings, not separate Unicode characters, and are not preserved in plain-text export.

Coverage report: compatibility.json. Amber keys in the page indicate font coverage gaps. Retaining a key assignment does not claim a matching glyph exists in this alpha font. Original mapping provenance and SHA-256 are recorded in the report. Source editor mapping author/license still needs review before public keyboard distribution.

Run `../.venv/bin/python ../tools/build_keyboard.py` from this folder to regenerate mapping artifacts after changing font coverage. Text is saved locally in the browser and can be downloaded. No text is transmitted elsewhere.

## Automatic Taw–Alap and word overrides

The default font now follows Yoab page 4: word-final Taw–Alap after an attached Taw uses 0x44, and after an unattached Taw uses 0x46. Non-final sequences remain letters. IgnoreMarks allows vowels between Taw and Alap.

OpenType overrides: ss01 forces attached design; ss02 forces detached design; ss08 shows separate letters. The keyboard selector applies to the word containing the typing cursor, in the formatted preview. The typing box always shows automatic behavior. A whole word is styled to preserve its joining context. Plain-text export retains Unicode letters only; preview overrides are saved in local browser storage. The optional attached-design override is also exposed for review.

Run tools/verify_taw_alaph.py for joining, word-final, mark-tolerant and explicit override shaping checks. Approval of single-mark proofs does not cover every new override/mark combination.
