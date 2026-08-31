# Editorial Illustration and Cover Recipes

Read this reference when the output will accompany an article, open a chapter, or act as a social or publication cover.

## Text intake and automatic image planning

When the user supplies prose and asks for illustrations without naming paragraphs or a count, make those decisions from the content. Do not generate one image per paragraph. Select only moments where a picture can carry a relationship, mechanism, contrast, emotional turn, chronology change, or consequence that prose alone would otherwise need to explain.

Build a compact internal content map before prompting:

- **Thesis:** the central claim or emotional landing in one sentence.
- **Paragraph roles:** assign each meaningful section a role such as entry tension, context, mechanism, example, turn, consequence, or conclusion; merge repeated roles.
- **Factual locks:** named entities, quantities, comparisons, causal direction, chronology, and claims that must not drift.
- **Candidate visual moments:** rank the roles by visual value. Prefer a decisive contrast, mechanism, turn, or consequence over introductory throat-clearing, repeated examples, citations, or transitions.
- **Series anchor:** choose one object, person, route, color, or material relationship that can visibly change state across the selected frames.
- **Exact text:** select no more than one title-level phrase or one to two short source-aligned labels per frame. Long prose stays outside the image.

Choose the smallest count that covers the article's distinct narrative work:

- **1 image:** one short passage, one thesis, or one self-contained visual proposition.
- **2 images:** a clear contrast/turn or mechanism/consequence pair; also the default for a short article with two strong visual roles.
- **3 images:** an entry–mechanism–consequence progression or a medium article with three genuinely distinct visual roles.
- **4–5 images:** only when a longer article contains additional indispensable roles that cannot be merged without losing meaning. Do not exceed five unless the user asks.

If the user gives a range, choose the lowest count that still covers the distinct roles. If the user gives an exact count, obey it and merge lower-priority roles. If the source is too thin to support the requested count without repetition or invented claims, explain the limit and generate fewer only when the request permits a range.

Before generation, present or record a concise plan with one row per image: `source span or paragraph role`, `visual proposition`, `recurring-anchor state`, `exact image text`, and `ratio`. Then generate the planned images as a coherent series and validate each frame against both its source role and the cross-frame progression.

Default article-companion images to landscape `16:9` when no destination is named. A cover is a separate deliverable: it represents the whole thesis and exact title, not one body paragraph. For a generic social cover without a named platform, use a portrait `4:5` composition with a flexible central crop; when a platform or ratio is supplied, recompose natively for it.

## Editorial illustration

Translate the content into one visual proposition rather than illustrating every sentence. Lock the author's thesis, named entities, factual relationships, emotional tone, and any required symbol. Then select one dominant visual metaphor that can be understood without the body text.

- Use one hero subject or interaction, plus no more than three supporting cues.
- Preserve 15–30% quiet paper so the image can sit beside typography or survive a crop.
- Prefer concrete objects, gestures, paths, containers, tools, or scale contrasts over generic decorative icons.
- Keep annotations to a title fragment or 1–3 short labels. Do not put the article's full argument inside the generated image.
- Do not invent quotes, statistics, logos, people, or events that the source does not establish.
- If the topic is abstract, make the metaphor clear through composition before adding arrows or notes.

```text
Editorial mode: distill [ARTICLE OR IDEA] into one immediately readable visual proposition. Preserve [THESIS, FACTUAL LOCKS, TONE]. Use one dominant hand-drawn metaphor with 1–3 supporting cues, uneven dark ink, translucent colored pencil, warm paper, and loose local construction errors. Keep 15–30% quiet space and avoid a literal illustration of every sentence. Text: [OPTIONAL EXACT SHORT TITLE OR LABELS]; render no other words.
```

## Article-to-social series

Use a series when several paragraph roles need distinct images rather than one cover. Map the article before prompting:

- **Thesis lock:** state the article's central claim in one sentence.
- **Narrative roles:** identify the entry tension, the mechanism or turn, and the consequence or landing. These are a useful three-image default, not a mandatory story shape; merge or expand them when the source structure requires it.
- **Factual locks:** list named entities, causal relationships, comparisons, chronology, quantities, and claims that must not drift.
- **Frame proposition:** give each image one sentence that can be understood without the body text. Do not make three cosmetic variants of the same metaphor.
- **Series anchor:** repeat one subject, object, path, color, or material relationship whose state visibly changes across the set. Repeat the anchor, not the entire composition.
- **Text policy:** a series frame may use one title-level source phrase or one to two short source-aligned labels when they materially improve its relationship to the surrounding prose. Lock every character verbatim, keep the wording subordinate to the metaphor, and keep long copy outside the generated image as source copy.

If the user gives no platform or aspect ratio, use a landscape `16:9` social image with a flexible central crop. Keep identity-critical content and short annotations inside crop-safe margins, preserve roughly 20–30% functional quiet paper, and let each frame have one hero interaction plus no more than three supporting cue families. A repeated group that performs one operation may count as one cue family; unrelated props count separately.

Across a series, preserve medium, paper, palette, line hierarchy, and the diagnostic form of the recurring anchor. Vary scale, crop, route, and negative-space placement so the sequence progresses instead of becoming a template grid. The final image may broaden the metaphor, but it must not make a stronger factual claim than the article.

```text
Article social-series mode: create frame [N] of [TOTAL] from [ARTICLE]. Thesis lock: [CENTRAL CLAIM]. This frame's narrative role: [ENTRY / MECHANISM / CONSEQUENCE / OTHER]. Visual proposition: [ONE-SENTENCE METAPHOR]. Preserve [FACTUAL LOCKS]. Recurring series anchor: [ANCHOR] changing from [PRIOR STATE] to [CURRENT STATE]. Use one hero interaction, at most three supporting cue families, warm paper, uneven dark ink, translucent colored pencil, and local construction errors. Unless another destination is specified, compose a landscape 16:9 image with a flexible central crop and 20–30% functional quiet paper. Text: [NONE / ONE EXACT SOURCE PHRASE / 1–2 EXACT SHORT LABELS]; verify every glyph and render no other words. Do not invent facts, statistics, brands, people, events, interface details, or explanatory labels.
```

Treat annotation as a bridge to the prose, not as a substitute for it. A title-level phrase should name the frame's paragraph role while the image itself still carries the causal or emotional relationship. Keep text in a quiet paper zone, use at most one small arrow or underline by default, and never place construction errors through a glyph. If any character is wrong or any pseudo-writing appears, the frame fails even when the illustration is otherwise strong.

When one frame becomes dense, correct hierarchy before changing the metaphor: remove unrelated props, merge repeated operations into one station or cluster, reopen paper between steps, and retain only the cues needed to distinguish that frame's narrative role.

## Cover illustration

A cover must remain legible at thumbnail size and leave deliberate room for external typography when title text will be added later.

- Choose one dominant motif occupying roughly 45–60% of the canvas.
- Use two or three asymmetric color blocks or secondary sketches, not a uniform collage grid.
- Establish a title-safe zone at the top, center, or lower third according to the intended crop.
- Keep important faces, landmarks, and diagnostic shapes away from trim edges.
- Use the requested aspect ratio. If none is supplied, infer it from the named destination; otherwise make a portrait cover with a flexible central crop.
- For exact titles, generate once, verify every glyph, and allow at most one surgical correction. If the correction still fails, deliver a clean no-text version with an irregular open title zone rather than pseudo-text.

When the source is an article, derive the cover from the article-level thesis and title rather than selecting a paragraph illustration and enlarging it. The cover's hero relationship may reuse the series anchor, but its scale, crop, title zone, and supporting cues must be recomposed for thumbnail reading.

```text
Cover mode: create a thumbnail-readable Boluobao-style cover for [TOPIC]. Hero motif: [SUBJECT], occupying 45–60% of the canvas. Supporting elements: [0–3 CUES]. Reserve a clean irregular [TOP / CENTER / LOWER] title-safe zone for later typography. Use asymmetrical colored-pencil blocks, warm paper, uneven ink contours, and restrained journal marks. Preserve the central crop and keep identity-critical features away from edges. Do not generate random text, logos, a perfect card grid, or dense body copy.
```

## Platform-native social cover set

Use this mode when one article or campaign needs covers for several destinations. Build one content map first, then recompose every canvas independently. Shared identity comes from the title, hero motif, palette, paper, and line system—not from reusing the same coordinates.

### Content and title lock

- Lock the exact topic, Chinese title, approved English title, punctuation, hero relationship, emotional direction, and any required platform order before generation.
- When the title is bilingual, render the Chinese once as the primary headline and the English once as the smaller translation. Do not add a kicker, category label, logo, handle, date, or explanatory copy unless requested.
- Chinese should normally carry about 1.7–2.2 times the visual weight of English through size, line count, darkness, or placement. English must remain readable at normal feed size, not reduced to decorative microtype.
- Keep the two languages in compatible one-person handwriting, but allow Chinese width and optical-center changes and English local slant and x-height changes. Never distort a protected glyph to manufacture style.
- Verify every glyph, letter, capitalization choice, and punctuation mark. If any generated title is wrong, keep the illustration and attempt one surgical title correction. If it remains wrong, return the no-text title-safe fallback instead of accepting an approximation.

### Destination recomposition

- An explicit user ratio or pixel size overrides every default and becomes a hard content lock.
- For a WeChat Official Account lead-cover test with no supplied size, use approximately `900 x 383` (`2.35:1`): place a compact two-line Chinese headline and subordinate English in one broad quiet zone, and counterweight it with a thumbnail-readable hero interaction. Avoid critical detail at the extreme left and right.
- For a Xiaohongshu cover test with no supplied size, use portrait `3:4`: title first in the upper reading field, English immediately subordinate, then let the hero interaction and supporting cues descend as one irregular vertical route. Preserve generous side margins for mobile viewing.
- For X, obey the supplied ratio rather than assuming one permanent platform default. On an extra-wide `5:2` request, use a left/right or staggered three-part route; keep title and hero large enough to survive feed reduction, and prevent support motifs from becoming a tiny icon strip.
- Do not crop, letterbox, stretch, or pad a master image into the other ratios. Change title line breaks, hero scale, crop, negative-space placement, and the path between supporting cues while preserving the same topic and motif family.
- Keep one hero interaction occupying roughly 40–55% of the useful canvas and use at most three supporting cue families. At thumbnail size, the viewer should read the title first and the hero relationship second.

```text
Platform cover-set mode: create the [PLATFORM] version at exact [RATIO OR PIXELS] for [TOPIC]. Shared identity lock: [HERO MOTIF], [PALETTE], warm paper, uneven dark ink, translucent colored pencil, and the same bilingual title. Recompose for this destination rather than cropping another version. Chinese title, exact: [CHINESE]. English translation, exact: [ENGLISH]. Render each once, Chinese primary and English subordinate, with no other words. Layout route: [PLATFORM-SPECIFIC TITLE/HERO/QUIET-ZONE PLAN]. Use one hero interaction and at most three supporting cue families. Preserve readable face, hands, diagnostic objects, title safe margins, raw paper, localized construction errors, and thumbnail clarity. No pseudo-writing, logo, interface chrome, decorative icon row, or dense body copy.
```

## Validation

An editorial image fails if its metaphor changes the source claim or requires many labels to explain. An article series also fails when the images have no recurring anchor, repeat the same narrative job, depend on the captions to become distinct, or accumulate more supporting props than the paragraph role needs. A cover fails if the hero motif disappears at thumbnail size, the title-safe zone is unusable, or essential content is lost in the expected crop. A platform cover set also fails when one canvas has merely been cropped or padded, when either language is inaccurate or decorative, or when a platform's title and hero hierarchy collapses at feed size. In all modes, fix hierarchy and content fidelity before adding more texture or decoration.
