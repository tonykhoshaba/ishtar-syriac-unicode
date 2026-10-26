# Provenance investigation — 2026-10-26

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
