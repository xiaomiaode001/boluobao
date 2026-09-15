# Animal and Pet Portrait Recipes

Read this reference for pets, companion animals, identity-preserving animal-photo reconstructions, and close animal portraits where the face carries the subject's identity. This is a specialization of the single-subject and image-reconstruction routes, not a license to invent a mascot, breed, costume, or human expression.

## Identity skeleton

Lock the smallest feature set that makes this animal recognizable before styling:

- species or breed-type silhouette, head angle, body pose, expression, and subject count;
- ear number, placement, fold or tuft shape, skull-to-muzzle proportion, nose placement, and mouth line;
- eye count, scale, spacing, gaze direction, iris hue, pupil shape, and any source-visible catchlight relationship;
- 3–7 diagnostic coat zones such as a forehead mark, eye surround, muzzle patch, cheek group, blaze, mask, ear edge, chest transition, or limb marking;
- visible paw ownership, overlap order, whisker origin, tail or limb relationship, and one or two characteristic proportions.

Do not let a generic species template overwrite the individual. A caption must not be required to recognize the same pet.

## Eyes: matte identity, not glass

Eyes are protected identity geometry. Simplify optical detail without changing the gaze.

- Preserve count, scale, spacing, alignment, gaze, iris color family, pupil shape, and source expression.
- Build each iris from one matte translucent pencil field plus roughly 3–5 irregular radial or tonal marks. Use at most one small paper-colored catchlight per eye unless the source requires a different diagnostic relationship.
- Keep the upper eyelid as one confident pressure-varying dark contour. The lower lid may be lighter or partly open away from the inner corner.
- Allow only subtle safe variation: one lid a fraction higher or lower, a slightly off-center catchlight, or unequal pencil coverage. Do not change pupil direction, eye size, health cues, or emotional meaning.
- Remove photographic reflections, smooth spherical gradients, lens-like depth, realistic iris filaments, wet highlights, and hard digital shine. Large glossy or enlarged eyes fail even when the animal remains cute.

For dark eyes, keep the pupil/iris distinction only where the source supports it; use paper exposure, a muted edge, or one tiny catchlight rather than inventing a bright ring.

## Face and coat compression

Treat coat pattern as a map of large relationships, not a collection of hairs.

- First place 3–7 diagnostic color or value zones. For a patterned face, these may include a forehead mark, brows, eye surrounds, cheek groups, muzzle, blaze, mask, or chest transition.
- Preserve marking direction and ownership while abbreviating repetition. One cheek group may end earlier or one patch may be marginally fuller, but the breed type, individual identity, and expression must remain stable.
- Render long fur with broad translucent pencil masses plus a few representative directional tufts. Render short fur with incomplete directional coverage, not dense hatch carpet.
- Keep nose, mouth, eye corners, teeth, tongue, and whisker roots sparse and protected. Do not place correction marks, fill accidents, isolated blocks, pseudo-writing, or decorative symbols on them.
- A muzzle may be slightly lopsided by hand, but it must remain attached to the same nose, jaw, and head angle. Never turn natural facial structure into a smile, pout, human eyebrow performance, or mascot expression unless requested.

## Whiskers, ears, and paws

- Use a representative subset of whiskers with varied length and spacing. They may contain one gentle bend or local restart, but must originate plausibly, avoid the pupils, and never become a bright digital wire net.
- Preserve ear count, ownership, inner/outer relationship, and characteristic fold or tuft. A small angle difference is safe only when it does not alter species or alertness.
- Preserve visible limb and paw count, overlap, contact, and ownership. Use one coherent paw silhouette plus a few light separation marks; do not add toes, claws, floating pads, or shadow limbs.

## Composition and finish

- Use one animal hero occupying roughly 58–72% of the canvas. Preserve the source crop when identity depends on it; otherwise crop one low-information body or background edge asymmetrically.
- Retain at most two incomplete environment fragments. Keep the background below half the subject's information density and leave warm paper active around and, where physically plausible, inside weak coat or light zones.
- Keep outer head, ear, body, chest, and paw contours mostly continuous and 1.5–2.5 times heavier than face and coat interiors.
- At the loose default, distribute 3–5 error families across safe outer fur, low-information body contours, fill edges, shadow, and background. The eyes, nose, mouth, teeth, tongue, paw anatomy, and identity-critical markings remain protected.

## Distinctiveness without caricature

Choose one or two authored relationships rather than exaggerating the whole animal:

- a slightly unequal upper-eyelid height while gaze remains coherent;
- one cheek mass or coat group that resolves earlier than the other;
- one mildly different ear angle that preserves alertness and identity;
- one broad color-registration miss on an outer coat edge;
- one short correction echo on a low-information outer fur contour;
- an off-center crop or muted shadow patch that gives the page a personal rhythm.

Do not combine all asymmetries. The goal is an observed individual drawn by hand, not a generic cartoon pet.

## Prompt scaffold

```text
Pet portrait mode: rebuild [ANIMAL] as one Boluobao single-subject portrait. Identity skeleton: preserve [SPECIES/BREED-TYPE SILHOUETTE], [HEAD ANGLE/POSE], [EYE COUNT/SCALE/SPACING/GAZE/IRIS/PUPIL], [MUZZLE/NOSE/EAR RELATIONSHIPS], [3–7 DIAGNOSTIC COAT ZONES], [VISIBLE PAW/WHISKER RELATIONSHIPS], and [SOURCE EXPRESSION]. Use one animal only.

Eyes: use one matte translucent iris field, 3–5 irregular marks, one small paper catchlight, a confident upper lid, and a lighter partly open lower contour. Permit only a subtle eyelid or catchlight asymmetry while gaze and pupil direction remain locked. No glassy reflections, spherical gradients, anime enlargement, or realistic iris filaments.

Face and coat: build the face from diagnostic value/color zones before adding representative tufts. Reduce repeated fur detail aggressively; use broad directional pencil masses and active paper. Keep nose, mouth, eye corners, whisker roots, teeth, tongue, and paw anatomy protected.

Line and composition: the animal occupies 58–72% of warm paper; outer head/ear/body/chest/paw contours remain mostly continuous and heavier than interior marks; retain at most two incomplete background fragments. Put 3–5 local error families on safe outer fur, low-information body edges, fills, shadow, and background.

Text: [EXACT REQUESTED TEXT OR NONE]. Do not invent a pet name, breed label, speech bubble, logo, or pseudo-writing.

Avoid: changed identity, added anatomy, human expression, mascot treatment, glossy eyes, anime/chibi proportions, hair-by-hair fur, dense scratch texture, bright wire whiskers, stitched contours, full-perimeter echoes, complete room detail, text, logo, watermark.
```

## Correction order

1. Restore subject count, pose, eye relationship, muzzle, ear set, paw ownership, and diagnostic coat zones.
2. Remove extra anatomy, pseudo-marks, glossy eyes, humanized expression, and whisker artifacts.
3. Reduce fur and facial interior information until the silhouette and 3–7 coat zones lead.
4. Strengthen outer/interior line hierarchy before adding one missing safe asymmetry or error family.
5. Make at most one targeted correction per active request, then rescore with the base rubric and pet-portrait gate.
