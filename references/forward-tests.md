# Forward Tests

Use these boundaries only after changing shared style, routing, text, or validation rules, or when diagnosing a repeated failure. Observable behavior matters more than exact pixels. Current retained assets are indexed in [reference-index.md](reference-index.md) and machine-checked by `assets/tests/test-manifest.json`.

## Current boundaries

| Mode | Retained evidence | Boundary | Known risk |
|---|---|---:|---|
| Single food | `single-food-xiaolongbao-v2.png`, `single-food-xiaolongbao-v3.png` | 18 / 19 | stitched contours, dense pleats, vessel-front artifacts |
| Scene | `scene-indoor-bookshop-v1.png`, `scene-morning-market-v1.png`, `scene-coastal-bus-stop-v1.png` | 18 | equally completed anchors, resolved perspective, texture carpet |
| Landscape | `landscape-loose-v2.png` | 19 | filled natural surfaces, dashed routes, complete tree repetition |
| Chinese letter | `letter-chinese-v2.png` | 19 | font-like rhythm or damaged radicals |
| English letter | `letter-english-v2.png` | 19 | uniform x-height/slant or ambiguous letterforms |
| Character card | `character-podcast-v1.png` | 19 | filtered-photo anatomy, dark garment carpet, hand errors |
| Landmark | `landmark-loose-v3.png` | 19 | centered postcard symmetry or complete secondary geometry |
| Manuscript story | `text-manuscript-loose-v3.png` | 19 | equal beat completion, wrong chronology, invented events |
| Article social series | `editorial-reasoning-01-16x9-v2.png`, `editorial-reasoning-02-16x9-v3.png`, `editorial-reasoning-03-16x9-v2.png` | 19 | cosmetic variants, generic infographic, excessive cue families |
| Platform covers | `cover-ai-classroom-wechat-v1.png`, `cover-ai-classroom-xiaohongshu-v1.png`, `cover-ai-classroom-x-v1.png` | 19 | wrong text, crop reuse, collapsed feed hierarchy |
| Close-up character | `character-closeup-student-v1.png`, `character-closeup-student-v2.png` | 18 / 19 | dense garment fill or background matching hero finish |
| Data bar chart | `data-bar-chart-16x9-v1.png` | 19 | wrong value-to-bar mapping, decorative ticks, geometry contradicting values |
| Compact data table | `data-table-16x9-v1.png` | 19 | wrong cell membership, missing separator, invented row or pseudo-writing |

The 18-point assets are structural or semantic baselines, not line-and-finish gold standards.

## Regression lessons

### Line and semantic safety

- Hero silhouettes stay mostly continuous and heavier than interior marks.
- Restarts remain local; periodic broken edges, beaded lines, and full-perimeter echoes fail.
- Every high-contrast hero mark needs a real source. Move accidents to low-information edges, fills, shadows, or background paper.
- Repeated detail is represented, not counted: omit most pleats, ingredients, windows, rails, trees, waves, folds, and surface lines.

### Finish hierarchy

- Scenes keep one hero, two or three middle anchors, one partial support object, and one major open plane.
- Landscapes use three depth bands, at most two strong pencil masses, and representative natural groups.
- Manuscript pages develop only the emotional-turn beat; at least two secondary beats stay below half its information.
- Close-up people protect faces and hands while moving irregularity to hair, clothing, furniture, props, and incomplete background fragments.

### Text and content

- Exact text is verified glyph by glyph. One surgical correction is allowed; a second failure produces a no-text title-safe fallback for covers or article illustrations.
- A failed letter glyph means the letter itself does not pass; return verified wording separately with a blank writing-zone fallback rather than approximate text.
- Article frames preserve source roles and one changing anchor. They do not invent facts, statistics, people, products, interfaces, or conclusions.
- Covers are independently recomposed for each ratio and never created by crop, pad, stretch, or letterbox reuse.
- Charts and tables protect every value, unit, order, encoding, and cell relationship. Their irregularity belongs only on harmless lines, fills, spacing, and paper.

## Retest protocol

After a shared-rule change:

1. run `scripts/validate_package.py`;
2. choose one retained gold sample from each affected mode and compare only the changed behavior;
3. run the matching case from `assets/tests/invocation-cases.json`;
4. score with the base rubric and exactly one mode-gate file;
5. correct the lowest-scoring dimension at most once;
6. record a new boundary only when the result is repeatable and replaces, rather than accumulates beside, an older sample.

## Stable v1.1 rule

Do not add a new universal rule for a one-off generation accident. Update Boluobao v1.1 only when a failure is reproducible, affects a public invocation route, or invalidates a current retained boundary.
