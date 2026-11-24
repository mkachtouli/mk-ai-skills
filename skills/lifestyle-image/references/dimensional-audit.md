# Mandatory dimensional audit after generation

Run this on EVERY returned candidate and every correction before presenting it as acceptable. The dimensions in a prompt and a plausible overall impression are not verification.

## Freeze the evidence before measuring

Retain the original product dimensions and their definitions, the source technical drawing, the selected real product view, site dimensional anchors and the camera/placement plan. Identify anchors in the actual supplied photograph; a specification for a similar vanity is not proof of the pictured model. Do not change the plan or widen an uncertainty range just to pass an output.

## Measure two independent kinds of consistency

1. **Physical size in the scene:** locate the mounting contact, highest point, riser axis and outlet axis in the returned image. Account for actual output size/crop changes. Use camera-aware projection from suitable known site dimensions to assess original height, reach and clearance. Do not turn horizontal countertop pixels/mm into vertical height pixels/mm: these axes can have different projection and depth. A wall-tile reference also needs a justified depth/camera relationship to the fixture. Do not measure a foreshortened reach as if it were a side elevation. If camera/scale calibration is insufficient, record what can be bounded and mark absolute size unresolved; do not claim exact millimetres from an uncalibrated image.
2. **Internal geometry and proportions:** compare original and output using a source-supported matching viewpoint. Record mounting base, union/collar, straight-to-curve transition, arch apex, outlet and handle centres/ends. Check straight-riser length, arch rise/radius, outlet drop, body height/width, tube diameter and handle span relative to one another and overall height. Height-to-reach is authoritative in world space, not necessarily raw image space. Prefer components sharing direction/depth for ratio comparisons; do not compare different perspectives without accounting for them. An overall-size pass cannot compensate for a squat body/arch with a shortened riser or vice versa.

For repeated product instances, compare the same original object in world space and allow only camera-induced differences in pixel size. Check each instance and its reflections; do not independently resize components or equalize foreground/background pixel heights.

Use native-resolution crops for detail review, preserving the untouched full frame. If the product is too small or occluded to distinguish relevant parts, mark that check unresolved rather than asserting microdetail fidelity. Review overlays/crops are evidence, never substitutes for the original product or edited deliverable.

## Record and decide

For each candidate record: authoritative dimensions/definitions; source and output landmark coordinates; any crop/resize mapping; dimensional anchors and provenance; projection assumptions; observed component ratios; uncertainty due to pixel selection, depth and camera; and separate physical-size, proportions, detail and installation decisions (`pass`, `fail`, `unresolved`). Do not invent a universal tolerance or declare exact accuracy unsupported by the evidence. Derive any useful bound from the evidence and keep it distinct from the user's target dimensions.

A known shortened/tallened riser, changed reach, altered body/tube proportions or world-scale mismatch fails. Insufficient evidence is unresolved, not a pass. User-rejected candidates lose their prior accepted status; keep previous files and rejection reasons in the audit trail. Do not include a failed or unresolved candidate in an “approved/final” package without clearly identifying its status.

## Correct without changing the product

Use the original product photos and environment again, with the rejected image only as the edit target/diagnostic reference if the live tool can include them all. Name the actual failed landmark/ratio. Restore original geometry AND the fixed physical-size/camera plan; do not solve the issue by stretching just the shaft, shrinking the whole fixture, changing reach or enlarging the basin. Re-run both size and proportions checks on the new image, plus detail/finish checks. At most two focused correction attempts per candidate per revision request; if still unsupported or defective, retain unresolved/rejected status and explain the concrete limitation. Never promise certified millimetre accuracy or unchanged microgeometry from generative editing alone.
