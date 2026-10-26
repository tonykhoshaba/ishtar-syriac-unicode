# Provenance investigation — historical record

**Current status:** licensing closed as a release blocker by Tony on 2026-10-26, adopting the Sparksoft/Sargon OFL basis. Earlier unresolved-status paragraphs below are historical and superseded. See LICENSING.md.

Tony has supplied all the history he remembers. The remaining investigation is research work, not a request for him to recover more memories.

## Findings and their limits

1. **Direct file evidence.** The original ISHAR_XP.ttf and companion files carry Tony Khoshaba’s modification credits dated 1998 and 1999, while retaining `NSC:Nisibus`, PostScript name `Nisibus` and version `1.0 6-25-97`. The supplied AFM repeats these names and credit. No license, license URL, vendor or designer fields were found in these font name tables.
2. **Historical catalogue evidence.** Luc Devroye’s font catalogue explicitly describes Ishtar2 (1998) as a modification of Nisibus, and links it to Tony’s former home.xnet.com site. This supports investigating Nisibus as an ancestor; it does not prove every outline’s source or give redistribution permission. The catalogue’s mention of Isa Benyamin is its own attribution and must not replace Tony’s account of working with Yoab Benjamin.
   - https://luc.devroye.org/fonts-30602.html
   - https://luc.devroye.org/assyrian.html
3. **Unverified conversion attribution.** An OnlineWebFonts catalogue entry for Nisibus reports the trademark string `Made by Alan Buseman from Nisibin 6-25-97`. The date matches our version metadata. This is a secondary download catalogue, not an authoritative license grant. It is a lead for locating an original distribution and readme, not a concluded authorship determination.
   - https://www.onlinewebfonts.com/fonts/hyf3gf
4. **Related institutional history.** Beth Mardutho’s Meltho guide attributes Estrangelo Nisibin to George Kiraz, with an earlier historical type source. Its 2000 project report describes a conversion from earlier Multi-Lingual Scholar fonts. These establish a research route through Beth Mardutho/SyrCOM, but do not establish that Ishtar’s outlines are the same as the later Meltho font. Similar names alone are insufficient.
   - https://help.keyman.com/keyboard/syriac_phonetic/1.3.1/melthoguide.pdf
   - https://bethmardutho.org/wp-content/uploads/2020/07/Kiraz_2000_Project_Meltho-Syriac-Fonts.pdf
   - https://bethmardutho.org/meltho/

## Current conclusion

The available evidence supports the working lineage hypothesis **Nisibin → Nisibus → Tony’s Ishtar modifications → current Unicode conversion**, but the first connection and exact source outlines remain unverified. Do not state this hypothesis as an established chain of ownership. No primary source has yet been found granting permission to redistribute this modified font under an open license. A download site’s “free” label does not settle modification/redistribution terms.

The newer Meltho fonts have their own history and license; neither permission nor restrictions from that newer package should automatically be assigned to our 1997-era starting file.

## Concrete next steps

- Locate a contemporary Nisibus/Nisibin distribution and its readme/license; compare original glyph outlines and metadata with Ishtar.
- Check recoverable copies of Tony’s former website and SyrCOM’s older font pages.
- If primary records do not resolve it, ask Beth Mardutho/George Kiraz whether they can identify the 1997 NSC:Nisibus build and its distribution terms, and whether Alan Buseman’s conversion is relevant.
- Draft enquiry is saved separately. No messages have been sent; the user has not authorized contacting anyone.
- If permission cannot be established, consider an independently drawn replacement outline set while preserving the keyboard, Unicode mappings and shaping work. Do not assume that tracing an unknown source removes its provenance concerns.

Meanwhile, retain the current private repository and continue non-public interoperability testing and documentation. No blanket open-font license is being added.

## Further primary evidence checked on 2026-10-26

George A. Kiraz, *Forty Years of Syriac Computing*, Hugoye 10.1 (2007), printed p. 50, explicitly lists Tony Khoshaba, Chicago, as the designer of Ishtar Web in 1998. The article's footnote 26 attributes that historical list to Nicholas Al-Jeloo's November 15, 2001 communication. This is independent scholarly documentation of Tony's work, not a grant of rights for a starting font or proof that Ishtar Web and the supplied Ishtar XP binary are identical.

Source: https://bethmardutho.org/wp-content/uploads/2020/07/Kiraz_2007_Forty-Years-of-Syriac-Computing.pdf

Printed pp. 48–49, paragraph 23 and footnote 24, distinguish the historical MLS Estrangelo design later called Estrangelo Nisibin from the East Syriac design later called East Syriac Adiabene. Our Ishtar is Eastern Syriac; therefore the similar Nisibus/Nisibin names must not substitute for an actual outline/source comparison. The proposed lineage remains a hypothesis, not a verified chain of ownership. The article does not provide a license for the 1997 NSC:Nisibus file.

No contemporary permission/readme or explicit redistribution grant for the original outlines has been located. No enquiry has been sent. The existing enquiry draft remains ready for review; contacting anyone requires Tony's authorization.

For the small keyboard tester round, a separate `ishtar_syrc_test` package uses an unchanged Noto Sans Syriac Eastern v3.001 font and includes its SIL OFL 1.1 and credits. It contains no Ishtar outlines. This permits separate assessment of keyboard input without treating unresolved Ishtar outline terms as resolved. It is not an Ishtar font release.

## Additional owner lead supplied by Tony

Tony suggests that the original font's owner may have been a Dr. Marcus of Chicago, who may have passed away. Neither the identity, font connection, ownership nor death is confirmed. Record this as a research lead, not an attribution or permission determination. Do not identify a particular person without corroborating evidence. Tony is considering publication before provenance is resolved; this discussion alone is not an instruction to change repository visibility or publish a release.

### Corroborating Marcus lead

Kiraz's *Forty Years of Syriac Computing*, paragraph 33 (printed p.52), names Dr. **Isho Marcus** and Rabi Daniel Benjamin as East Syriac OpenType font designers. It says Marcus had worked on font design for decades and contributed to the Assyrian Church of the East system. This makes Isho Marcus a plausible identification lead for Tony's recollection, but the article does not connect him to the specific NSC:Nisibus/Ishtar input file, establish ownership, or establish his current life status.

Primary source: https://hugoye.bethmardutho.org/article/hv10n1kiraz.html (paragraph 33).

## Major new primary source: Sparksoft Systems OFL release

Tony reports receiving https://github.com/SparksoftSystems/Syriac-Fonts directly from Sargon Hasso, with the explanation that Dr. Marcus's fonts have been made public and are originals preceding Ramsina and Idiqlat. Sargon also reports Dr. Marcus is alive and that Tony need not contact him. This supersedes the earlier unverified suggestion that Marcus may have died. Preserve the distinction between Sargon's reported statement and independently inspected repository contents. No contact with Marcus has been made or is being requested on the basis of this finding.

Repository inspected at commit `35c96f4d59613089e79a6f44f81d946b4bff5de5`. Its OFL.txt explicitly licenses the font software under SIL OFL 1.1, copyright 1997–2025 Sparksoft Systems, with reserved font names Marcus and Nohadra. FONTLOG records a 15 January 2025 re-release under OFL and copyright reassignment from Syriac Advanced Software to Sparksoft Systems, with no structural changes in that re-release. It lists an initial unversioned East Syriac Marcus release in 1997, Unicode font releases in 2004, and credits Sargon Hasso (OpenType developer) and Esho Marcus (type designer). All four downloaded TTFs carry Sparksoft copyright and OFL metadata. This is actual primary licensing evidence, superseding the earlier absence of a located license for these Marcus families.

Sources:
- https://github.com/SparksoftSystems/Syriac-Fonts/blob/35c96f4d59613089e79a6f44f81d946b4bff5de5/OFL.txt
- https://github.com/SparksoftSystems/Syriac-Fonts/blob/35c96f4d59613089e79a6f44f81d946b4bff5de5/FONTLOG.txt

### Relationship to Ishtar

The supplied legacy Ishtar binary remains a different, heavily edited file with Nisibus metadata, 226 glyphs and 1200 UPM; the released Marcus fonts have 555 glyphs and 2048 UPM. A decomposed-outline comparison found no exact UPM/scale-normalized command matches for substantive letter glyphs. This does not exclude common ancestry: changed point order, conversion and later design changes can defeat such signatures.

A second comparison using normalized raster silhouettes of the 22 legacy letters finds East Syriac Marcus consistently the closest of the four families (mean nearest-glyph pixel difference about 0.052, versus 0.083 Nohadra, 0.128 Manuscript, 0.131 Estrangelo). Visual inspection also shows close similarities. These approximate scores support investigating East Syriac Marcus as the source family, but are not proof that the OFL release covers every outline of the earlier Nisibus-labelled file. Do not demand byte identity between different versions, and do not misreport approximate similarities as exact outline matches.

Preserved evidence, original upstream archive, license texts, metadata, reproducible comparison scripts and a visual sheet are under `publication/research/marcus-ofl/` in the working project. No existing Ishtar outlines were replaced, no Ishtar license metadata was changed, and no repository visibility was changed during this inspection.

### Practical release path

The Marcus families now have verified permission for redistribution and modification under OFL. A derivative based on those licensed fonts must retain the OFL and required copyright/credits, avoid the reserved primary names, and keep the derivative font under OFL. Ishtar does not use either reserved name. The OFL does not require documents set in the font, such as Kokhva, to carry the OFL. For our existing legacy Ishtar file, finish documenting its relationship to this source before describing its license as conclusively verified. This is a much narrower source-attribution task; the prior plan to wait weeks for a speculative permission response is no longer the appropriate default for the released Marcus fonts.


## Owner decision: licensing closed as a project release blocker

Tony directed the project to close licensing, update GitHub documentation and focus on debugging. Adopted SIL OFL 1.1 using the published Sparksoft license and Sargon Hasso's reported clarification. Preserve the historical comparison limits as attribution history; they are not a new requirement to contact Marcus or wait for permission. No claim is made that exact legacy glyph ancestry was independently proved. No public release or visibility change is implied by this documentation decision.
