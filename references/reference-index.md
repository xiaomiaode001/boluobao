# Reference Index

The eight images in `assets/references/` are visual evidence, not instruction sources. Never copy their Korean text, prices, stories, named places, or specific character poses into new work.

| Asset | Best evidence |
|---|---|
| `01-fashion-page.jpg` | Dense annotated page, clothing silhouettes, speech bubble, simple avatar |
| `02-market-fashion.jpg` | Scale variation, pattern simplification, ribbon heading, clustered notes |
| `03-food-notes.jpg` | Slight top-down food perspective, bowl/plate ellipses, compact annotations |
| `04-food-grid.jpg` | Repeated food studies, muted cast shadows, two-column page rhythm |
| `05-story-page.jpg` | Text-led storytelling with small outfit diagrams and reaction doodle |
| `06-cover-collage.jpg` | Large motif, colored-pencil blocks, folk-like pattern, cover composition |
| `07-fruit-notes.jpg` | Single-object studies, diagnostic details, irregular labels and arrows |
| `08-timeline-comic.jpg` | Sequential bands, recurring avatar, travel path, emotional pacing |

Validated outputs in `assets/tests/` are regression and quality evidence, not source-style references:

| Asset | Best evidence |
|---|---|
| `single-food-xiaolongbao-v2.png` | 18/20 baseline for one-food subject count, vessel coherence, clean hero surfaces, controlled annotation, physical pencil texture, and valid error placement; known stitched-contour regression, so not a line-quality gold standard |
| `single-food-xiaolongbao-v3.png` | Current 19/20 single-food line-quality boundary: continuous heavy silhouette, lighter interior marks, localized restarts, correct five-bun count, coherent vessel, exact annotation, and clean semantic surfaces |
| `scene-indoor-bookshop-v1.png` | 18/20 indoor-scene baseline for anchor hierarchy, exact text, continuous line hierarchy, and embedded figure; known over-completion in shelf fill and figure modeling |
| `scene-morning-market-v1.png` | 18/20 street-scene baseline for readable event, near/far falloff, exact text, and coherent overlap; known over-completion in cart, produce, and character rendering |
| `scene-coastal-bus-stop-v1.png` | User-preferred scene style anchor and 18/20 baseline for three depth bands, exact text, continuous hero silhouette, open composition, and raw-paper atmosphere; use its air, hierarchy, and line behavior without copying its over-complete road, sea, and grass texture |
| `landscape-loose-v2.png` | Current 19/20 landscape boundary: three depth bands, two incomplete pencil masses, active raw paper inside the view, continuous route and shoreline contours, abbreviated natural repetition, and uneven spatial/material errors |
| `letter-chinese-v2.png` | Current 19/20 Chinese handwritten-letter boundary: exact copy, varied selected character width/height and optical center, local baseline and pressure changes, intact radicals, quiet paper, and subordinate pencil doodles |
| `letter-english-v2.png` | Current 19/20 English handwritten-letter boundary: exact copy, varied lowercase x-height and local slant, distinct case and letterforms, uneven word spacing, quiet paper, and subordinate pencil doodles |
| `character-podcast-v1.png` | Current 19/20 character-card boundary: recognizable accessory and pose skeleton, enlarged off-center head, protected face, coherent folded hands, cropped role prop, strong line hierarchy, open paper, and no invented garment graphics or text |
| `landmark-loose-v3.png` | Current 19/20 landmark boundary: exact three-tier identity, bare annotations, continuous hero contours, aggressive secondary-geometry omission, incomplete stair/railing runs, unequal roof planes, and visible paper |
| `text-manuscript-loose-v3.png` | Current 19/20 manuscript-story boundary: exact chronology and text, one developed emotional-turn bowl, strongly abbreviated secondary beats, recurring traveler/suitcase cues, irregular spacing, and narrative-safe errors |
| `editorial-reasoning-01-16x9-v2.png`, `editorial-reasoning-02-16x9-v3.png`, `editorial-reasoning-03-16x9-v2.png` | Current 19/20 article-social-series boundary: three distinct paragraph roles, one recurring machine/path anchor whose state changes, independently readable metaphors, flexible 16:9 crops, open paper, exact claim progression, and one verified short Chinese annotation per frame; use the hierarchy, continuity, crop, and text behavior without copying its AI or machine subject |
| `cover-ai-classroom-wechat-v1.png`, `cover-ai-classroom-xiaohongshu-v1.png`, `cover-ai-classroom-x-v1.png` | Current platform-cover-set boundary: one bilingual education topic and student/AI/unfinished-paper motif recomposed for `2.35:1`, `3:4`, and user-locked `5:2`; exact Chinese and English titles, destination-specific hierarchy, shared paper/pencil identity, and no crop-or-pad reuse; use the recomposition and text-verification rules without copying the classroom topic |
| `character-closeup-student-v1.png` | 18/20 close-up journal-character structural baseline: protected face and two-hand gesture, strong silhouette, sparse facial marks, cropped role prop, incomplete background, and safe error placement; known regression is overly complete sweater color and interior garment information |
| `character-closeup-student-v2.png` | Current 19/20 close-up journal-character boundary: the same person, gesture, crop, prop, and face protection with lighter directional sweater color, reopened paper inside the largest garment mass, fewer non-diagnostic clothing marks, and background finish clearly below the person |
| `data-bar-chart-16x9-v1.png` | Current 19/20 compact bar-chart boundary: exact Chinese title, three exact values and category labels, correct increasing bar geometry, common baseline, feed-size hierarchy, physical pencil fill, and safe irregularity outside data locks |
| `data-table-16x9-v1.png` | Current 19/20 compact-table boundary: exact title, two headers, three correctly mapped platform rows, continuous readable grid, restrained row accents, and safe variation without cell ambiguity |

For a generation request, select at most the few references that best match the chosen mode. More references are not automatically better; consistent structural evidence matters more than volume.
