# Prompt Recipes

Use these as scaffolds. Replace bracketed fields with the user's content; omit unused lines.

## Universal style-transfer block

Use this block when the user supplies an image and asks to “用 boluobao 进行设计”, “转成 boluobao 风格”, or otherwise redesign it in this visual language. Inspect the source first and list the semantic locks that must survive. The supplied image is the edit target unless the user explicitly calls it only a reference.

```text
Use case: style-transfer
Primary request: Rebuild [SUBJECT OR SCENE] as a warm hand-drawn travel-journal illustration while preserving [CONTENT LOCKS].
Style/medium: uneven dark brush-pen contours; translucent colored-pencil and dry-marker fills on warm ivory uncoated paper; visible paper grain; simplified observational drawing; charming controlled imperfections.
Shape language: strong recognizable silhouette, sparse interior details, slightly flattened perspective, one muted offset shadow patch.
Line hierarchy: draw most hero silhouette edges as confident continuous strokes, 1.5–2.5 times heavier than interior marks. Allow only a few localized gaps or short correction echoes; keep repeated internal detail abbreviated and lighter.
Spontaneity: [restrained / loose / wild]. Use unevenly distributed construction mistakes, not a global noise effect: selected contour restarts and double strokes, partial color misses and spills, one or two lopsided shapes, omitted secondary details, drifting handwritten baselines, and an awkward gap or near-collision.
Composition: [MODE-SPECIFIC LAYOUT]. Keep readable hierarchy and some untouched paper.
Annotations: [USER-PROVIDED LANGUAGE AND EXACT SHORT TEXT]. Use casual handwritten placement, arrows or one speech bubble only where useful.
Palette: earthy tomato red, burnt orange, mustard, olive, dusty teal, slate blue, plum; 4–7 colors total.
Constraints: preserve subject count, identity, pose/order, and diagnostic features; reconstruct the image rather than applying a texture overlay; every mark on the hero must correspond to a real contour, seam, fold, ingredient, or requested decoration; do not copy text or stories from style references.
Avoid: photorealism, smooth gradients, glossy 3D shading, vector-perfect lines, anime polish, watercolor wash, clip-art stickers, perfect grids, uniformly thick contours, perfectly closed shapes, evenly distributed wobble, fake global noise, stitched or beaded outlines, evenly dashed contours, full-perimeter echo lines, dense decorative clutter, unexplained dark blocks, pseudo-writing, invented emblems, watermark.
```

For image-led redesign, preserve the source's subject relationships before choosing stylistic omissions. Do not introduce an article metaphor, notebook story, extra label, or cover layout unless the user asks for that deliverable. When source text is visible, preserve it only if requested or identity-critical; otherwise remove it cleanly rather than replacing it with pseudo-writing.

## Single subject

```text
Subject boundary: exactly one hero presentation. A required bowl, plate, cup, wrapper, or steamer belongs to that presentation; do not add unrelated food, drink, utensils, table props, or decorative companions.
Composition: one slightly off-center subject occupying 55–70% of the canvas, one title or food name plus at most one short observation, one small colored-pencil shadow, and generous raw-paper margin.
Detail boundary: preserve the silhouette, requested count, vessel structure, and 2–5 diagnostic features. Abbreviate repeated ingredients, folds, pleats, seeds, crumbs, and surface texture after identity is secure.
Line budget: keep the outer silhouette continuous and heavier; use lighter interior ink only for diagnostic structure. Do not outline every repeated unit, trace redundant vessel rings, or convert paper grain into broken ink marks.
Spontaneity boundary: keep at least three valid error families visible, but place them on contour restarts, fill edges, low-information geometry, shadow boundaries, steam, crumbs, or background paper.
Hero-surface lock: keep the main food and vessel free of unexplained symbols, floating strokes, pseudo-writing, attached shadow shapes, and decorative marks that were not requested.
```

Use for dishes, products, outfits, pets, buildings, or portraits. Keep annotation subordinate to the main silhouette. For a single food, use `assets/tests/single-food-xiaolongbao-v3.png` as the current 19/20 line-quality boundary. Use v2 only as an 18/20 semantic-cleanliness and vessel-structure baseline; its stitched contour rhythm is a known regression and must not be copied.

## Annotated sheet

```text
Composition: portrait notebook page with 4–8 isolated sketches in a loose two-column rhythm; vary scale; interlock short notes and arrows with the objects; one rough ribbon heading; preserve 8–15% quiet paper.
```

Use for menus, packing lists, wardrobe studies, travel souvenirs, or collections. Do not repeat equal-sized cards.

## Story strip

```text
Composition: 3–6 chronological beats divided by hand-drawn horizontal bands or open whitespace; one simple avatar recurs across frames; a dashed path, arrows, or time words clarify order; final beat receives extra breathing room.
```

Use for journeys, routines, recipes, mishaps, and before/after narratives. Lock event order before styling.

## Cover collage

```text
Composition: one dominant central motif occupying about half the page, supported by two or three asymmetric color blocks, a small banner title, one tiny traveler/avatar, and restrained folk-like marks; no dense body text.
```

Use for chapter openers, trip covers, recipe-section covers, or social covers.

## Photo-content preservation block

Append when recognizable source content matters:

```text
Content locks: keep the same [person/object], [pose/viewpoint], [number of items], [key clothing or color], and [distinctive shape/details]. Simplify secondary texture, but do not alter identity, anatomy, logo-free silhouette, or event meaning.
```

## Exact-text fallback

If the generator is unreliable with text:

```text
Leave clean, irregular blank paper zones for later handwritten labels. Do not generate random pseudo-letters or substitute words.
```

Do not add a font or editor dependency. Report the intended wording separately and deliver the clean title-safe or label-safe blank version with exact-text status `blank-fallback`.
