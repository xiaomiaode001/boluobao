# Content and Text Quality Gates

Read this file with the base [quality rubric](quality-rubric.md) for article illustrations, social series, covers, data charts, compact tables, manuscript story pages, and handwritten letters.

## Editorial and article-social gate

An editorial image or series targets **19/20** only when:

1. a content map preserves the thesis, paragraph roles, factual relationships, emotional direction, chronology, named entities, quantities, and exact copy;
2. every frame has one distinct visual proposition matching its assigned source role and remains understandable without explanatory labels;
3. a series anchor changes state across frames while scale, crop, route, or negative-space placement varies enough to avoid cosmetic variants;
4. each frame contains one hero interaction and at most three supporting cue families, with no unrelated prop, icon row, interface panel, or competing metaphor;
5. the default `16:9` article composition keeps critical content inside crop-safe margins and uses roughly 20–30% raw paper as functional air;
6. line character and physical-media feel each score `2`, with at least three uneven construction-error families outside exact text and thesis-critical objects;
7. text is limited to one exact title-level phrase or one to two short source-aligned labels; long prose remains outside the image;
8. no quote, statistic, logo, named person, product, event, causal claim, interface detail, or conclusion is invented or strengthened.

## Platform-cover gate

A social cover or platform set targets **19/20** only when:

1. every requested pixel size or ratio is verified, and each platform version is independently recomposed rather than cropped, padded, stretched, or letterboxed;
2. the topic, hero relationship, palette, paper, and line system remain shared while title breaks, hero scale, crop, negative space, and route adapt to the destination;
3. every requested title and language appears exactly once with correct glyphs, spelling, capitalization, and punctuation; do not invent an unrequested translation;
4. the requested primary language is visually dominant and any translation remains readable but subordinate;
5. title is the first read and the hero relationship the second at feed size, both inside safe margins;
6. one hero interaction occupies roughly 40–55% of the useful canvas with at most three supporting cue families;
7. line character and physical-media feel each score `2`, with at least three error families outside faces, hands, exact text, and diagnostic objects;
8. no unrequested logo, handle, date, category tag, interface chrome, icon row, body copy, claim, watermark, or pseudo-writing appears.

For a generic social cover with no named platform, verify a true portrait `4:5` composition with a flexible central crop.

## Data-chart gate

A compact chart targets **19/20** only when:

1. title, category labels, values, signs, decimals, units, order, and label-to-mark mapping match the approved data lock;
2. bar height, baseline, scale, and comparison direction tell the same relationship as the numbers, with no decorative geometry that can be mistaken for data;
3. the chart contains one comparison and no invented tick, legend, trend line, icon row, statistic, source, or conclusion;
4. labels and values remain readable at destination size and stay visibly attached to the correct mark;
5. physical-media feel and line character each score `2`, while at least three error families remain outside data geometry and exact text;
6. any mismatch remaining after one surgical correction fails the chart rather than becoming a blank or approximate delivery.

## Data-table gate

A compact table targets **19/20** only when:

1. title, headers, row and column count, cell membership, values, units, punctuation, capitalization, and order match the approved data lock;
2. every required separator remains clear, cell padding supports feed-size reading, and styling never changes grouping;
3. the generated table contains at most five columns and eight body rows unless the user explicitly approves a denser display;
4. there is one table only, with no spreadsheet chrome, filters, formulas, extra panels, invented row, omitted cell, or pseudo-writing;
5. physical-media feel and line character each score `2`, with safe variation in row height, grid endpoints, fill coverage, pressure, and one local correction echo;
6. any protected-data mismatch remaining after one surgical correction fails the table rather than becoming a blank or approximate delivery.

## Manuscript-story gate

A manuscript story page targets **19/20** only when:

1. premise, chronology, emotional turn, recurring anchor, silent beat, and every selected phrase match the approved content map;
2. only the emotional-turn beat is developed, while at least two secondary beats contain visibly less than half its line and color information;
3. beat sizes and spacing are unequal, one transition is small or partial, and the page does not resolve into a clean comic grid;
4. recurring people remain diagrammatic and recurring props vary only by safe shorthand, never by identity or ownership;
5. at least four narrative-safe error families remain visible while arrows and event order stay correct;
6. there is no invented destination, extra event, unused bubble, pseudo-writing, realistic storyboard finish, or equally complete background in every beat.

## Handwritten-letter gate

A Chinese, English, or bilingual letter targets **19/20** only when:

1. every requested glyph, word, capitalization choice, number, punctuation mark, language, and line break is exact, with no extra writing;
2. title, optional date, body, and optional note read as one person's hand through compatible pen angle, pressure, endings, and tempo;
3. at least three local irregularity families are visible without global wobble: baseline drift, width or x-height change, optical-center or slant change, spacing imbalance, pressure jump, retrace, or terminal overshoot;
4. Chinese width, height, and optical-center variation preserves radicals and recognition; English x-height and slant variation preserves spelling, case, and confused-letter distinctions;
5. hierarchy is readable and decorations remain subordinate to the text;
6. warm paper, near-black soft pen, and limited matte pencil accents remain physical without ruled-paper, font-rendering, calligraphy, or vintage-filter polish;
7. there is no crossed-out replacement, duplicate letter, malformed glyph, invented signature, text-bearing stamp, logo, watermark, or unrelated decoration;
8. if one surgical correction still leaves any requested text wrong, the result is not a letter pass; return the verified wording separately and deliver a blank writing-zone fallback with status `blank-fallback` rather than approximate text.
