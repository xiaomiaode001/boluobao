# Data Chart and Table Recipes

Read this reference when the user asks Boluobao to visualize supplied values as a compact chart or table. These modes are data graphics, not decorative illustrations: data fidelity is protected before style.

## Build a data lock first

Record the title, labels, values, units, category order, row/column membership, sorting, comparison direction, and any stated source. Never infer missing values, normalize units silently, reorder categories for aesthetics, or turn an approximate relationship into an exact claim.

Use a compact display only:

- Bar charts work best with `3–8` bars and one comparison variable.
- Generated tables work best with at most `5` columns and `8` body rows.
- If the source exceeds those limits, ask the user to select or authorize a summary. Never silently omit rows or columns.
- Default article data graphics to `16:9`; use a requested destination ratio when supplied.

## Hand-drawn bar chart

- Preserve one common baseline unless the user explicitly supplies a truncated scale.
- Bar height, order, category, value, unit, and label-to-bar mapping are clean anchors.
- Put the exact value close to its bar when labels are required; avoid a separate legend when direct labeling is clearer.
- Use one chart only. Remove dashboard cards, icon rows, decorative scenes, 3D bars, gradients, and invented trend lines.
- Keep 20–30% warm paper and use 3–5 muted pencil colors. Repeated bars may share a color unless the comparison requires distinction.

```text
Boluobao data-chart mode: render [TITLE] as one hand-drawn [BAR TYPE] chart in [RATIO]. Data lock: [CATEGORY = VALUE + UNIT, IN EXACT ORDER]. Preserve the common baseline, monotonic relationships, labels, values, units, and mapping exactly. Use warm ivory paper, uneven near-black ink, broad matte colored-pencil bars, and quiet space. Put controlled errors only on harmless border endpoints, corner shape, local fill coverage, and one short contour restart. Render no unrequested words, ticks, legend, icon, or claim.
```

## Compact hand-drawn table

- Preserve the exact number of columns and rows, header/body distinction, cell membership, punctuation, capitalization, and units.
- Keep text left aligned or optically centered consistently by column purpose; numeric cells may align by their right edge or decimal when useful.
- Use a mostly continuous ink grid with adequate cell padding. Slight row-height variation is allowed; missing separators and ambiguous cell boundaries are not.
- Use pale pencil swipes for the header or selected rows. Color may stop early or cross a harmless border slightly, but must not change grouping.
- Do not imitate spreadsheet chrome, toolbars, filters, formulas, or interface controls unless requested.

```text
Boluobao data-table mode: render [TITLE] as one compact [ROWS] by [COLUMNS] hand-drawn table in [RATIO]. Data lock: [HEADERS AND EVERY ROW, IN EXACT ORDER]. Preserve every glyph, value, unit, separator, and cell membership. Use warm ivory paper, confident uneven ink grid lines, restrained colored-pencil row accents, generous padding, and no extra panels. Controlled errors may affect only row height, one grid overshoot, local fill coverage, and one short correction echo; never alter data or cell boundaries.
```

## Safe irregularity and failure policy

Allowed error zones: harmless grid endpoints, bar corner shape, line pressure, light fill registration, background paper, title underline, and non-data shadow patches.

Protected zones: every data glyph, sign, decimal, percent mark, unit, row/column association, bar order, bar height relationship, baseline, separator needed to identify a cell, and any sourced claim.

Verify the visual against the data lock cell by cell or bar by bar. One surgical correction is allowed. If any protected data remains wrong, do not deliver a blank or approximate data graphic; mark it failed and return the verified data mapping so it can be regenerated. A blank-title fallback is allowed only when the title is the sole error and every data mark is correct.

## Mode pass

A chart or table passes only when:

1. every label, value, unit, order, and mapping matches the data lock;
2. chart geometry tells the same relationship as the numbers, or every table value occupies the correct cell;
3. title and data remain readable at the intended feed size;
4. line and colored-pencil treatment feel physical without making the structure ambiguous;
5. at least three safe error families are visible outside protected data;
6. no extra statistic, row, column, legend, icon, claim, pseudo-writing, or watermark appears.
