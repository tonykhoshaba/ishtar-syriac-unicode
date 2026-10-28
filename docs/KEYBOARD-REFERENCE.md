# Keyboard reference

Use English US physical positions. Unshifted number keys supply vowels and marks; Shift supplies digits. Right Alt/AltGr supplies additional forms. The complete mapping is in `keyboard/mapping.csv` and the browser demo's expandable reference.

| Keys | Output/use |
| --- | --- |
| P / Shift+P | Pe / Fe |
| G / Shift+G / J | Gamal / Gamal with dot below / Gamal with Majliyana |
| F / Shift+F | Sheen / Sheen with Majliyana above |
| Z / Shift+Z | Zen / Zen with Majliyana above |
| R / Shift+R | Resh / Resh with Seyame |
| 1 / 2 / 3 / 4 | Ptakha / Zqapa / horizontal Zlama / angular Zlama |
| 0 | Seyame |
| Backslash | Talqana above |
| Right Alt+H | Dotted He |
| Right Alt+R | Rukakha mark |
| Right Alt+F | Majliyana above |
| T then A | Taw–Alap; font selects its contextual form |

On phones/tablets, use Shift, Alt, 123 and held-key alternatives. The top row contains marks. Inside the browser tester choose System keyboard when using an installed Syriac input method, to avoid translating input twice.

Final and initial letter shapes are selected by the font, not by separate letter keys. Some uncommon mapped characters use fallback fonts; see KNOWN-LIMITATIONS.md.

## Choosing Taw–Alap forms

Automatic contextual ligatures are the default. To prefer separate Taw and Alap, enable OpenType stylistic set **ss08** for the text or document in an application that supports it. This preserves the two Unicode letters and their normal contextual shapes.

In the web keyboard, place the cursor in a word, choose **Separate letters** under **Taw–Alap for selected word**, then click **Apply to selected word**. The result appears in the formatted preview. Choose **Automatic — Yoab’s rule** to restore the default. The same selector offers the attached and detached ligature designs.

For websites, apply `font-feature-settings: "ss08" 1;` to the relevant Ishtar text. Other applications need their own OpenType feature controls; the keyboard cannot force this preference in every app. The web tester saves its formatting choices in the same browser, but plain-text export and copy/paste do not carry those choices.
