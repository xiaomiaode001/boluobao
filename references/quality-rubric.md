# Quality Rubric

Use this base rubric for every Boluobao result. Score each dimension `0`, `1`, or `2`. A usable result scores at least **17/20**, with no zero in subject fidelity, physical-media feel, controlled error, or exclusions.

After this file, read exactly one matching gate file:

- [Content and text gates](quality-gates-content.md): editorial illustration, article social series, platform covers, data charts, compact tables, manuscript story pages, and handwritten letters.
- [Visual subject gates](quality-gates-visual.md): single food, scenes, landscapes, landmarks, character portraits, and close-up characters.
- Modes without a dedicated gate use this base rubric and the closest recipe-specific constraints.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Subject fidelity | Identity/count/order changed | Mostly preserved | Immediately recognizable; all content locks preserved |
| Silhouette simplification | Muddy or generic | Recognizable but busy | Strong shape plus 2–5 diagnostic details |
| Line character | Clean vector, noisy scratch, or unreadable broken edge | Some variation, but contours are stitched/dashed, equally weighted, or over-described | Mostly continuous confident silhouette; clear outer/interior weight hierarchy; only localized breaks or short echoes; sparse diagnostic interior marks |
| Controlled error | Only clean rendering or global noise | One repeated defect | At least three unevenly distributed construction-error families |
| Shape/perspective naivety | Perfect render or broken identity | Mild simplification | Readable subject with selective lopsidedness, scale slip, or compressed space |
| Physical-media feel | Smooth digital fill | Texture partly visible | Colored-pencil grain and paper tooth remain visible |
| Color discipline | Neon or uncontrolled | Mostly muted | Cohesive earthy 4–7-color palette |
| Composition | Cluttered or rigid grid | Serviceable | Asymmetric, readable, and intentionally paced |
| Annotation integration | Random/copy text | Relevant but detached | Notes, arrows, and bubbles support the subject naturally |
| Exclusions | Major anti-style or semantic artifacts | One mild artifact | No photorealism, glossy 3D, vector polish, anime, watermark, copied reference text, pseudo-writing, or unexplained marks on the hero |

## Common failures and targeted fixes

- **Digital cartoon:** reveal more paper, lower fill opacity, add directional pencil grain, and vary contour pressure.
- **Commercial stickers:** leave two partial fills, distort one secondary plane, vary shadow placement, and create one awkward spacing relationship.
- **Procedural wobble:** remove global jitter; concentrate errors at stroke restarts, overlaps, corners, and hand-position changes.
- **Stitched contour:** reconnect most of the edge into one confident stroke; retain only a few localized restarts and remove periodic gaps or full-perimeter echoes.
- **Overloaded interior ink:** retain only diagnostic folds, ingredients, rings, or facial relationships; let colored-pencil blocks carry texture and volume.
- **Errors everywhere:** restore clean anchors around the silhouette and protected features; keep mistakes local and asymmetric.
- **Too tidy or too chaotic:** offset one cluster or baseline when tidy; remove one motif and reopen quiet paper when chaotic.
- **Texture filter only:** rebuild simplified shapes and perspective instead of overlaying paper grain.
- **Subject identity drift:** restore diagnostic features before adding more style.
- **Wrong or pseudo text:** correct exact wording once; if still unreliable, remove all generated text and deliver a clean title-safe zone.
- **Handwriting font effect:** vary selected baselines, widths, optical centers, pressure, gaps, slant, or x-height without damaging glyph identity.
- **Vintage/grunge excess:** retain subtle tooth without stains, torn edges, sepia overlay, or ruled paper.
- **Unexplained hero mark:** remove any block, emblem, floating seam, pseudo-character, or ornament without a real structural source.
- **Generic infographic:** return to one concrete causal or emotional relationship; remove icon rows, dashboards, and redundant labels.

When iterating, correct the lowest-scoring dimension only, then rescore. Make at most one corrective generation pass unless the user asks for more exploration.

## Line pass gate

A result cannot score `19/20` unless **Line character** scores `2`. Reject the line pass when any major hero contour is built from periodic dashes or beads, a second outline follows most of the perimeter, interior marks compete with the silhouette, or every repeated detail is individually outlined.

## Delivery pass

Before handoff, verify:

1. pixel dimensions and effective ratio;
2. requested subject, count, chronology, and platform;
3. every exact glyph and punctuation mark, or the explicit `blank-fallback` status;
4. final rubric score and matching mode gate;
5. versioned filename and absolute path outside the installed Skills folder;
6. project output contains only the accepted final deliverable set—no rejected candidate, superseded correction, contact sheet, or unrequested before/after composite.
