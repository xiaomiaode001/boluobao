# Food and Scene Recipes

Read this reference only for meals, restaurants, streets, interiors, landscapes, or event scenes.

## Food study

Preserve the dish's recognizable vessel, dominant ingredients, sauce color, garnish, and serving arrangement. Simplify ingredient count and render appetite through color contrast rather than realistic shine.

### Single-food hero quality boundary

A single-food request contains exactly one named food presentation. Its required vessel or wrapper belongs to the same presentation; everything else must be requested explicitly.

- **Subject count:** show no unrelated side dish, drink, utensil, tabletop prop, decorative ingredient pile, mascot, or second serving. Preserve any requested count of buns, slices, skewers, dumplings, or other repeated units.
- **Scale and space:** place the hero slightly off-center at 55–70% of the canvas and preserve roughly 25–40% visible paper around it. Do not crop identity-critical edges.
- **Annotation budget:** default to one food name and at most one short observation, with no more than one arrow. Exact wording remains a content lock.
- **Shadow and accident budget:** use one muted cast-shadow stain and at most one small physical accident such as a crumb, spill, steam group, or faint smudge. Both must have an obvious source and must not resemble an added object part.
- **Detail budget:** keep the silhouette, vessel structure, requested count, and 2–5 diagnostic features. Abbreviate repeated pleats, noodle strands, pastry layers, seeds, garnish, bamboo strips, and surface hatching after recognition is secure.
- **Error placement:** keep at least three valid construction-error families, concentrated on contour restarts, fill registration, low-information ellipse slips, shadow edges, steam, crumbs, or background paper. Protected food and vessel surfaces remain semantically clean.
- **Finish boundary:** the result should feel observed and handmade but intentional. It fails if it becomes a polished menu illustration, a rough low-quality scribble, or a clean sticker on textured paper.

`assets/tests/single-food-xiaolongbao-v2.png` is an `18/20` baseline for subject count, vessel coherence, semantic cleanliness, material finish, and annotation restraint. It is not a line-quality gold standard: its repeated broken contours create a stitched rhythm that new outputs must correct. `assets/tests/single-food-xiaolongbao-v3.png` is the current `19/20` single-food line-quality boundary: preserve its continuous silhouette, weight hierarchy, localized restarts, and clean vessel structure while reducing interior pencil texture further when the subject allows.

```text
Single-food hero: draw exactly one [FOOD PRESENTATION] with [VESSEL OR WRAPPER] and preserve [COUNT / DIAGNOSTIC FEATURES]. Occupy 55–70% of the canvas with 25–40% raw paper. Use one food name, at most one short observation, one arrow, one muted shadow, and at most one sourced crumb/spill/steam/smudge. Abbreviate repeated internal detail after identity is clear. Keep at least three valid error families away from protected food and vessel surfaces. Add no unrelated food, drink, utensil, prop, pseudo-writing, emblem, floating seam, or unexplained mark.
```

Use a slight top-down view with deliberately imperfect construction:

- bowl or plate ellipses are lopsided and not perfectly concentric;
- garnish clusters overlap or float slightly instead of obeying precise perspective;
- sauce or broth color misses the rim in a few places;
- one ingredient is oversized because it matters to the note;
- cast shadow is a dusty patch offset by eye;
- steam, oil dots, crumbs, or chopstick marks use quick irregular strokes.

### Food line budget

- Draw the hero silhouette and vessel-defining edges with mostly continuous, assertive ink. Keep interior folds, ingredient separations, and texture visibly lighter.
- For repeated foods, show only a representative subset of pleats, kernels, noodle strands, seeds, layers, bamboo strips, or garnish marks. Once identity and count are clear, let colored-pencil shape and open paper replace extra ink.
- Give secondary foods only a few diagnostic interior marks. Do not outline every small ingredient or repeat the same texture mark across every unit.
- For vessels, keep only the rings needed to explain rim, opening, wall, and base. Avoid redundant concentric ellipses, full parallel echoes, and decorative bands that do not describe real structure.
- Across the page, use only a few localized line restarts and short correction echoes. Reject evenly dashed, beaded, perforated, hash-broken, or stitched outlines.

### Vessel structure lock

Before introducing looseness, identify the vessel's readable parts: rim, inner opening, side wall, base, handle, seams, and any real material pattern. Every structural stroke must belong to one of those parts.

- Ellipses may disagree slightly, but the rim, wall, and base must still describe one coherent container.
- Simplify or omit repeated bamboo strips, ceramic motifs, plate rings, or glass facets; do not replace them with floating seams, solid blocks, pseudo-writing, or invented ornaments.
- Keep the front face of a bowl, plate, cup, or steamer free of unexplained high-contrast marks. Decoration appears only when the user or source subject requires it.
- Food spills may cross the rim only when their source and direction are visually clear. Shadows stay outside the vessel and must not look attached as a new object part.
- Put most construction errors on the rim, fill edge, shadow boundary, steam, crumbs, or background paper rather than on the vessel's clean front face.

```text
Food mode: one hero dish plus 1–3 small supporting items, seen from a loose slight top-down angle. Draw directly in ink without an underdrawing. Keep most silhouette strokes continuous and heavier than interior marks; allow only a few localized restarts or short correction echoes. Keep the vessel readable but make its ellipses mildly lopsided; draw only structural vessel rings; abbreviate repeated ingredients; let selected colored-pencil fills stop early or cross the contour. Keep the vessel front free of unexplained symbols, pseudo-writing, floating seams, and invented decoration. Add one tasting reaction, one arrow, and one local stain or shadow patch. Do not render glossy food photography or stitched outlines.
```

## Multi-food sheet

For 5–8 different foods on one page, do not render every item as a finished hero illustration. Choose one hero food; reduce every other item to a strong silhouette plus 2–5 diagnostic marks.

- vary item scale and spacing enough that the page cannot be mistaken for six equal menu cards;
- omit at least half of repeated ingredients, pastry layers, garnish marks, seeds, reflections, and tableware decoration;
- spend only 2–3 cast-shadow stains across the whole page, leaving the other foods directly on raw paper;
- make at least one secondary item a very abbreviated ink-and-pencil note rather than a complete product rendering;
- use 4–7 colors for the entire page, not a fresh palette for each food;
- keep labels short and exact; a food identity must remain readable even if its label is removed.

If the page looks like a polished illustrated menu, remove interior rendering and repeated shadows before adding more wobble. More contour jitter does not solve over-completion.

```text
Multi-food sheet: show [5–8 FOODS] in an irregular notebook rhythm. Choose [HERO FOOD] as the only developed drawing. Render the remaining foods as abbreviated studies with 2–5 diagnostic marks each. Omit half of repeated ingredient detail, use only 2–3 dusty shadow stains across the entire page, leave broad raw-paper gaps, and distribute contour restarts and color misses locally. Do not create equal menu cards or give every item the same degree of finish.
```

## Scene vignette

Preserve the place identity through 3–5 anchors: facade or skyline shape, main path, dominant color block, weather/light cue, and one distinctive prop. Omit the rest.

### Scene anchor hierarchy

Before drawing, assign every requested element one role:

1. **Hero anchor:** one structure, spatial event, or foreground relationship carries the scene and receives the strongest continuous contour and the most color.
2. **Middle anchors:** keep only two or three supporting objects, people, vehicles, furniture groups, or architectural cues. Each receives a readable silhouette plus 2–4 diagnostic marks.
3. **Atmosphere layer:** indicate sky, wall, rain, foliage, pavement, water, or distant buildings with one or two incomplete colored-pencil masses and very little ink.

Do not give every object the same finish. A scene fails when every window, shelf, chair, brick, roof tile, bicycle spoke, tree, wave, or paving joint is individually described.

### Scene line and surface budget

- Use the heaviest, most continuous ink for the hero silhouette, main opening, roofline, horizon, or path edge. Secondary structures use lighter partial edges; atmosphere may have no outline at all.
- Keep most long scene-defining contours continuous. Allow only 2–5 localized restart events across the page and at most two short correction echoes; never use periodic gaps, stitched architecture, or a full parallel perimeter.
- Choose one dominant spatial direction for the ground, floor, wall, street, shore, or horizon. Let only one or two secondary planes disagree; if every vertical leans and every plane slips, the scene becomes unstable rather than naive.
- Collapse repeated architecture and texture into representative marks: a few window divisions, shelf bands, roof tiles, spokes, leaves, puddle edges, or waves must stand in for the whole run.
- Let raw paper complete light, air, walls, sky, and ground. For street and interior vignettes, keep roughly 25–40% of the page unfilled; for natural views, keep roughly 20–35% unfilled unless weather requires a broader mass.
- Use no more than three people or vehicles unless crowding is the subject. Keep them embedded through overlap, ground contact, or shared color patches so they do not read as separate stickers.
- Use one short title and at most one short observation by default. Never invent shop signs, labels, logos, license plates, posters, or pseudo-writing to make the setting feel busy.

### Scene finish ceiling

- Complete the hero anchor's silhouette, then deliberately leave at least one supporting object partially described and at least one major plane open. A wall, floor, street, sky, sea, shelf interior, or storefront recess should stop before edge-to-edge completion.
- Use no more than two strongly filled color masses. Inside a large pencil mass, preserve irregular paper gaps rather than hatching the entire region to one even density.
- Delete roughly 30–50% of nonessential interior lines after the scene is recognizable. Remove complete rows before adding hand wobble: book spines, produce units, shelf contents, roof stripes, spokes, waves, grass, paving, bricks, and distant stalls are common deletion targets.
- Keep people diagrammatic rather than anatomically illustrated: one head/hair shape, one torso block, simple limb strokes, and 2–4 facial marks. Omit fingers, garment-fold rendering, facial shading, and realistic pose modeling unless identity requires them.
- A valid scene should still feel like a notebook observation when the annotations are hidden. If it reads as a polished editorial or children's-book illustration, flatten the depth, simplify the figure, open a major plane, and remove interior rendering before introducing any new error.

Compress space rather than constructing a realistic environment:

- verticals may lean independently;
- the foreground grows too quickly and distant objects stay slightly too large;
- repeated windows, chairs, trees, or signs reduce to a few marks;
- one person or vehicle may be disproportionate but readable;
- edges may crop a doodle or building unexpectedly;
- colored areas behave as patches, not realistic lighting volumes.

```text
Scene mode: compress [PLACE OR MOMENT] into a notebook vignette with one hero anchor, two or three middle anchors, and one incomplete atmosphere mass. Give the hero the strongest mostly continuous contour; use lighter partial edges for supporting structure and almost no ink for distant atmosphere. Perspective is judged by eye around one dominant ground or horizon direction: only selected verticals or secondary planes disagree. Collapse repeated windows, shelves, bricks, tiles, spokes, trees, waves, and paving into representative marks, then omit 30–50% of nonessential interior lines. Keep at least one supporting object partially described and one major plane open. Use no more than two strong color masses and preserve irregular paper gaps inside them. Keep figures diagrammatic with a head/hair shape, torso block, simple limbs, and 2–4 facial marks. Keep 25–40% raw paper for streets/interiors or 20–35% for natural views. Use one short title and at most one short observation. Include localized restarts, local color-registration misses, and one awkward crop or near-touch. Add no invented signage, pseudo-writing, or decorative clutter. Do not turn the scene into a polished children's-book environment or an equally finished architectural rendering.
```

## Scene density rule

Render only three layers:

1. one dominant foreground or facade shape;
2. two or three middle-ground anchors;
3. a sparse atmosphere/background patch.

Do not fill every architectural surface. If the scene becomes polished, delete half the repeated details before adding more wobble.
