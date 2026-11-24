# Role-labelled prompt scaffold

Adapt this to inspected inputs. Do not send unfilled placeholders or unsupported specifications to the image tool. Keep the prompt focused on the actual product and reference environment.

```text
Use case: compositing.
Deliverable: one photorealistic lifestyle product image.

Input roles:
- Image [index/name]: PRODUCT IDENTITY AND FINISH reference. This exact object is the product being placed.
- Image [index/name]: ENVIRONMENT [BASE / INSPIRATION] reference. This determines the location and visual setting.
- [Optional image index/name]: additional geometry evidence of the SAME product.

Request:
Integrate this exact photographed [product] into the supplied [environment], at [observed installation site], mounted on [surface]. [Replace only the existing identified fixture and repair its immediate mounting area / insert into the specified clear site].

Product lock:
Preserve [observed silhouette, component count, handle shape/asymmetry, arm or spout configuration, curvature, thickness, joints, outlet, mounting plates, holes, hardware and engraving]. Keep the exact relative proportions. Do not simplify, beautify, symmetrize, unfold/reconfigure, add accessories or substitute a similar design. Do not infer the product from a text description or copy the environment fixture.

Finish lock:
Retain [observed source hue/undertone, patina, texture and gloss] and the original non-metal parts. Match local light and reflections while preserving material identity. No warmer yellow/orange gold grade, copper shift, fake polishing or finish conversion.

Environment direction:
Preserve [specific layout, architecture, cabinet style, materials/patterns, colour palette, viewpoint and light direction visible in the environment reference]. [Default: keep the supplied room and all unrelated objects/framing intact; edit only the installation region and necessary local integration effects. / Explicit adaptation: describe the requested changes and which concrete reference features remain authoritative.]
Do not invent a generic kitchen/bathroom or transfer the product photograph's studio background into this setting.

Placement and photographic integration:
Use [confirmed size evidence or explicitly approximate relative scale]. Preserve proportions; do not stretch parts to fit. Match the camera perspective, physically plausible mounting/contact, localized shadows, natural occlusion and environment reflections. Keep important product details visible and believable. [Resolve any actual fit/angle limitation before requesting unsupported geometry.]

Output:
[Requested crop/ratio, otherwise the environment's framing/aspect ratio]. Premium but natural photographic presentation. No added people, styling props, text, watermark, logos or measurement graphics unless specifically requested. Preserve genuine physical product engraving.
```

## Focused correction example

State the observed failure rather than restarting with a broad “make it better” instruction:

> Use the original product image and original environment image again. The previous output changed [specific handle/joint/finish/environment detail]. Restore [observable source feature]. Keep the requested placement, room anchors and all other product details intact; do not fix the defect by hiding it behind an object or changing the camera to an unsupported angle.

The prompt's input labels are explanatory text, not dedicated tool arguments. Include the actual image references through the current tool schema. Do not fabricate a mask file, generation quality argument, output dimension or destination parameter.
