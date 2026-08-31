# Text Manuscript to Journal Page

Use this workflow when the main input is prose, notes, a diary entry, itinerary, transcript excerpt, or article draft rather than an image.

## Build a content map first

Do not prompt the image model with an undifferentiated paragraph. Extract:

1. **Premise:** one sentence describing what happened.
2. **Narrator and place:** only what the draft explicitly establishes.
3. **Content locks:** names, destinations, chronology, objects, emotional turn, and any phrases that must remain verbatim.
4. **Story spine:** 3–5 beats, each phrased as one concrete visual action.
5. **Emotional turn:** the beat where expectation, mood, or understanding changes.
6. **Image text:** one short title plus up to five short labels or quoted fragments.
7. **Silent beat:** one image that carries meaning without a caption.

Ask for clarification only when chronology or a required identity cannot be inferred. Otherwise preserve ambiguity rather than inventing facts.

## Text fidelity modes

- **Editorial compression (default):** preserve meaning and order; shorten body text into handwritten labels. Tell the user what was condensed.
- **Selected verbatim:** preserve only user-marked phrases exactly; paraphrase the rest into visual beats.
- **Full verbatim:** keep the entire draft outside the generated illustration and return it as verified source copy beside a blank irregular writing zone. Do not introduce a bundled font or layout dependency.

Never claim that long generated image text is verbatim without checking every character.

A blank callout is a fallback only for a specific phrase that failed to render. If every requested phrase is already present and correct, remove all unused bubbles, caption boxes, and empty text zones.

## Story-page composition

- Use 3–5 beats, not one panel per sentence.
- Give the emotional turn the largest or most isolated drawing.
- Repeat one visual anchor across beats: narrator, suitcase, umbrella, cup, vehicle, building, or color.
- Vary beat size and spacing. One beat may be tiny; one gap may be awkwardly large.
- Use arrows or a dashed route only if chronology is otherwise unclear.
- Keep at least one silent beat and one marginal reaction doodle.
- Treat only the emotional-turn beat as a developed illustration. Render other beats as abbreviated line-and-color vignettes with 2–4 diagnostic details; four equally polished mini-scenes fail this mode.

### Beat finish ladder

- **Emotional turn:** the only developed drawing. It may receive a complete silhouette, the strongest color mass, one local shadow, and 4–6 diagnostic marks.
- **Opening beat:** use one action silhouette, the recurring anchor, and only 2–4 diagnostic marks. Background becomes one incomplete pencil patch or disappears entirely.
- **Waiting or transition beat:** reduce it to a figure/prop relationship with partial contours and one color cue; do not render a complete room, street, counter, or vehicle.
- **Resolution or silent beat:** use 2–3 objects or marks with the most open paper. Let absence, spacing, an empty vessel, weather change, or an arriving shape carry the meaning.

At least two secondary beats must visibly contain less than half the line and color information of the emotional turn. Delete complete scenery, anatomy, vehicle parts, furniture, reflections, and repeated material detail before adding more stylistic wobble.

### Manuscript irregularity budget

- Change scale for a narrative reason: the emotional turn grows; one transition becomes tiny; the recurring character may drift slightly in proportion while retaining the same hair, clothing color, and prop cue.
- Keep chronology readable through placement first. Use no more than two route arrows or dashed paths; let one bend awkwardly or nearly touch a vignette, but never point to the wrong beat.
- Use no clean panel grid. One vignette edge may stop early, one gap may be unusually large, and one drawing may crop at the page edge.
- Keep repeated characters diagrammatic: one head/hair shape, one torso block, simple limb strokes, and 2–4 facial marks. Omit fingers, garment-fold rendering, facial shading, and realistic pose modeling.
- Vary the recurring prop by shorthand, not identity: a suitcase may lose a seam or change handle angle, but its color, basic shape, and ownership stay recognizable.
- Preserve at least four different error families across the page: scale drift, partial vignette edge, prop shorthand, color miss, baseline drift, arrow near-touch, local contour restart, or one awkward gap. Never use event order or exact wording as error material.

## Controlled errors for prose conversion

Errors belong to visual narration, not factual content:

- character scale may drift slightly between beats;
- one panel boundary may be missing or stop early;
- a recurring prop may be simplified differently each time;
- arrows may bend unevenly or nearly touch a drawing;
- color emphasis may land slightly outside a figure;
- handwriting baselines may climb or change size.

Never reorder events, change quoted words, merge different people, or invent a destination as a style error.

If the page looks like a polished storyboard, keep the content map unchanged but remove half the environmental detail, convert most backgrounds to two or three pencil patches, break one vignette edge, and expose more paper. Do not solve over-polish by adding uniform scribble.

## Prompt scaffold

```text
Manuscript premise: [ONE SENTENCE]
Content locks: [NAMES, PLACE, ORDER, OBJECTS, EMOTIONAL TURN]
Story beats: 1) [VISUAL ACTION] 2) [VISUAL ACTION] 3) [VISUAL ACTION] [4–5 OPTIONAL]
Silent beat: [IMAGE-ONLY MOMENT]
Text (verbatim): title "[TITLE]"; labels "[SHORT PHRASE]", "[SHORT PHRASE]" ... Render no other text.
Composition: irregular portrait travel-journal story page; unequal beat sizes; one repeated visual anchor; emotional turn receives extra scale or whitespace; no clean comic grid.
Finish ladder: only the emotional turn is developed. At least two secondary beats contain less than half its line and color information; backgrounds collapse to one patch or disappear. Figures remain diagrammatic rather than anatomically modeled.
Spontaneity: preserve at least four unevenly distributed construction-error families in vignette edges, repeated prop shorthand, figure scale, arrows, color registration, contour restarts, spacing, and text baselines; factual order and exact phrases remain locked.
Avoid: illustrating every sentence, four equally complete mini-scenes, realistic character or vehicle modeling, invented details, reordered events, dense generated paragraphs, pseudo-characters, perfect comic panels, polished children's-book layout, watermark.
```

## Validation

Compare the result to the content map, not just the prompt. A text-driven page fails if it looks stylish but loses chronology, the emotional turn, the recurring anchor, or exact selected phrases.

It also fails if it contains an unused empty bubble, gives every beat equal visual weight, or renders each beat as a fully developed scene.
