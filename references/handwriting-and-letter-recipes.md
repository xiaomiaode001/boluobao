# Handwriting and Letter Recipes

Read this reference when text itself is the visual subject: journal stationery, a short letter, diary card, handwritten quote, Chinese, English, or Japanese handwriting calibration, or a bilingual or multilingual note. Use `text-manuscript-recipes.md` instead when prose must become illustrated story beats.

## Content and layout lock

- Exact wording, capitalization, numbers, punctuation, language, and any user-required line breaks are protected content. Verify every glyph before accepting style improvements.
- Default to one title, an optional date, one short body block, and at most one margin note. Follow a user-requested structure when it differs.
- Use warm unruled ivory paper with generous quiet space. Do not add notebook binding, school-copybook grids, a photographed desk, stamps with invented writing, signatures, or decorative pseudo-text unless requested.
- Keep decoration subordinate: one underline and one or two small colored-pencil doodles are enough. Decorations contain no text by default.
- For long passages or production-critical copy, keep the passage outside the generated image and return it as verified source copy. Generate only a clean irregular writing zone unless the user explicitly accepts a shorter locked excerpt; never call unverified generated paragraphs verbatim or introduce a bundled font dependency.

## One-person handwriting system

The page should feel written by one person, not assembled from a handwriting font and not distorted glyph by glyph.

- Keep a compatible pen angle, stroke ending, pressure range, and overall tempo across title, body, date, and note.
- Create variation unevenly: select a few glyphs, words, or lines for width, center, baseline, slant, pressure, or spacing changes. Most writing remains confident and readable.
- Let one body line climb or dip gently and give another line a quieter counter-direction. Avoid perfectly parallel baselines, but also avoid a different random angle on every word.
- Use a few compact gaps and one or two wider gaps. Do not alternate spacing mechanically.
- Permit at most one short retrace on an existing stroke and one mild terminal overshoot by default. Do not add crossed-out wording, correction words, duplicated letters, or invented marks to create imperfection.
- Headings may be larger and heavier; body writing stays lighter and conversational; margin notes may be smaller. Avoid turning all three into separate unrelated typefaces.

## Chinese handwriting boundary

- Vary the width and height of selected characters by roughly 12–20%: mix a few narrow/tall characters with a few broad/squat characters without making an alternating pattern.
- Shift the optical center of a few characters slightly left or right inside their imagined square. Keep radicals joined and proportioned well enough that the character remains immediately identifiable.
- Let only 3–5 selected characters in a short block lean by small, different angles. Most characters remain upright anchors.
- Allow local pressure changes and one short retrace only on real strokes. A stylistic stroke must never change a radical, merge neighboring characters, resemble another character, or become pseudo-Chinese.
- Avoid uniform square-grid spacing, typeset regularity, formal brush calligraphy, fake ancient calligraphy, childish scrawl, outline lettering, and page-wide wobble.

## English handwriting boundary

- Vary lowercase x-height by roughly 12–22% across selected letters and words. Some `a/e/n/o/s` forms may sit smaller while selected ascenders rise higher and descenders drop unevenly.
- Give selected letters gentle local slants of roughly 2–7 degrees left or right. Cluster the changes naturally instead of alternating direction letter by letter.
- Keep uppercase clearly distinct from lowercase while varying capital width and stance. Preserve the identity of easily confused forms such as `I/l`, `o/a`, `r/v`, and `c/e`.
- Default to upright printed handwriting with only a few natural joins. Use full cursive, copperplate, or another explicit script only when requested.
- Avoid uniform x-height, identical slant, font-like kerning, bubble lettering, malformed letters, pseudo-writing, global wobble, and decorative distress.

## Japanese handwriting boundary

- Preserve kanji identity, kana identity, okurigana, punctuation, and line order exactly. Keep small kana such as `ゃ`, `ゅ`, `ょ`, and `っ`, the long-vowel mark `ー`, and dakuten or handakuten attached to the intended character.
- Let a few kana sit slightly smaller or lower and let selected kanji vary modestly in width or optical center, while most characters remain stable reading anchors.
- Protect mixed-script tokens independently. For example, `AI` must not become `A1`, `Al`, or decorative pseudo-Latin; Latin case remains locked inside Japanese text.
- Default to contemporary printed handwriting with restrained local joins. Avoid formal brush calligraphy, faux historical script, manga sound-effect lettering, or stereotyped cultural decoration unless requested.

## Multilingual calibration

For style calibration, generate different scripts as separate sheets with the same paper, hierarchy, spacing roles, accent palette, and doodle budget. This isolates script behavior and makes exact-text comparison easier.

If the user requests several languages on one page:

- lock and proofread each language block separately before judging the composition;
- separate the blocks clearly while matching pen pressure, stroke endings, and page rhythm;
- when no primary language is named, give all blocks comparable size, contrast, and spatial importance rather than silently promoting English or Chinese;
- when a primary language is named, let it lead and keep translations readable but subordinate;
- use one neutral shared motif to connect the blocks when useful, but do not use flags, flag colors, national costumes, or culturally stereotyped symbols unless requested;
- preserve each script's own proportions instead of forcing Chinese square structure, Japanese kana rhythm, and Latin x-height into one common glyph system.

## Mixed-script copy and contact details

For a creator introduction or other text-led visual, a Chinese sentence may contain Latin names, acronyms, and contact details without becoming a separate typography system.

- Lock each Latin token independently, including case and spacing: `AI`, `GEO`, and a product or community name are not decorative glyphs. Keep them legible within the same pen-pressure family as the Chinese line.
- Treat an email address as one atomic text field. Verify every character, digit, `@`, dot, domain, and local-part order; do not wrap it in the middle, add spaces or hyphens, or over-distort its x-height and slant. A source `\@` used as a Markdown escape represents a literal `@`, not a backslash in the address.
- Give practical contact copy quieter handwriting and more stable baselines than an expressive title. Keep it on the same paper surface with enough contrast and edge space for mobile reading.
- For user-requested longer in-image copy, compose a small number of readable blocks and proofread each one. If one surgical correction still leaves protected copy wrong, deliver the verified wording separately with a clean open text zone; never call approximate image text exact.

## Prompt scaffold

```text
Handwritten journal-letter mode: make the exact text the visual subject on warm unruled ivory paper. Layout: [TITLE POSITION], [OPTIONAL DATE], [SHORT BODY BLOCK], and [OPTIONAL MARGIN NOTE], with generous quiet paper and no invented writing. Preserve every glyph, capitalization, number, punctuation mark, and required line break verbatim.

Shared hand: one near-black soft pen, compatible pressure and stroke endings, a slightly heavier title, lighter conversational body, one gently drifting line, a few uneven gaps, one local pressure change, at most one short retrace on an existing stroke, and no global wobble.

Chinese when present: selected character widths and heights vary by 12–20%; a few optical centers shift left or right; only 3–5 characters lean slightly; radicals and character identity remain protected.

English when present: selected lowercase x-heights vary by 12–22%; a few letters use 2–7-degree local slants; ascenders, descenders, capital stance, and word gaps vary modestly; uppercase/lowercase and letter identity remain protected.

Japanese when present: preserve kanji, kana, okurigana, small kana, long-vowel marks, dakuten, handakuten, and punctuation exactly; vary only a few kana sizes or baselines and selected kanji widths or centers; protect embedded Latin tokens separately.

Multilingual hierarchy: [PRIMARY LANGUAGE AND DOMINANCE, OR EQUAL-WEIGHT BLOCKS WHEN NONE IS SPECIFIED]. Keep script blocks distinct but visibly written by the same hand. Use no flag or cultural-stereotype coding unless requested.

Decoration: [ONE UNDERLINE OR COLOR PATCH] plus at most [ONE OR TWO SMALL DOODLES], containing no text.

Avoid: handwriting-font regularity, perfect baselines, uniform glyph distortion, formal calligraphy unless requested, crossed-out or duplicate wording, pseudo-characters, extra text, ruled paper, binding, collage stickers, heavy vintage grime, and watermark.
```

## Correction order

1. If any text is wrong, restore exact wording before adjusting style.
2. If text is correct but font-like, change only the script-specific variable: Chinese width and optical center, English slant and x-height, or Japanese kana baseline and selected kanji width.
3. If variation becomes noisy, restore most glyphs as upright readable anchors and retain only the strongest local differences.
4. For multilingual work, recheck each script block and every mixed-script token independently after the edit.
5. Recheck every glyph after each edit; a handwriting improvement never compensates for a text error.
