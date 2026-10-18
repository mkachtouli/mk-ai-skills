---
name: 3d-object
description: Create or revise real product 3D models from photographs, product pages and dimensions, with source-faithful geometry and finish, editable source, GLB export and an interactive review. Use for actual 3D assets or product-model corrections, rather than a raster image that merely looks three-dimensional.
---

# 3D Object

Build a reviewable, physically scaled model of the user's actual product. For Vintaless, Brassty, Atlassy/Atlasty and related hardware, product identity and natural finish colour take priority over an impressive render. Apply the same source fidelity to other products without assuming they are brass.

## Establish the evidence

- Inspect supplied photographs before modelling. For a supplied product URL, retrieve the gallery and relevant specification documents when accessible. Distinguish the target product, finish references, and construction-only examples; an example of legs does not authorize copying its spout, handles, body or finish.
- Record dimensions as **confirmed**, **photo-estimated**, or **unknown**, including endpoints and units. Ask about an ambiguous measurement when it materially controls geometry; continue independent work. Do not stretch the entire product to force a disputed dimension. Explain conflicts between dimensions and photographic proportions, and record which later correction supersedes an earlier interpretation.
- Match handle style, finish and configuration to the intended variant. Do not combine features from multiple variants.
- Use original photographs as the geometric and colour evidence. An earlier synthetic model or generated studio image may be a working draft, but cannot validate its own accuracy. Identify a supplied processed image as such when that is known.

Read [references/reconstruction.md](references/reconstruction.md) for modelling, material and export decisions. For the Atlas bridge faucet only, read [references/atlas-case.md](references/atlas-case.md); its measurements are not defaults for other products.

## Reconstruct and revise

1. Establish mounting plane, axes, real-world units and major silhouette before detailed hardware. Use metres in GLB; define whether overall height includes concealed mounting shanks.
2. Compare the actual contours of handles, bridge/cast transitions, valve housings, legs, collars, unions, outlet and mounting plates. Handle symmetry must follow the photograph: do not substitute generic centred T bars for offset levers. Assess cross-section thickness as well as overall bounding size.
3. Keep components and important dimensions editable. Use Blender/CAD or a suitable reconstruction tool that is actually available. Fit the geometry to evidence; a stock faucet assembled from primitives is a starting point, not a finished likeness.
4. Preserve accepted parts when correcting one region. Save a new revision and document moved, reshaped and unchanged components. Preserve source material colour unless a finish change was requested. Modify lighting separately from albedo.
5. Treat unseen faces and hardware dimensions as estimates. Model threads or bores only when supported/requested; do not call an estimated helix a manufacturing-standard connection. Do not invent internals.
6. Render from the actual exported geometry. Never pass off an AI-enhanced image as proof of what the GLB will look like.

A single photograph does not establish an exact complete object or measured optical material. Produce an explicit review prototype when reconstruction is underdetermined; do not promise perfect hidden geometry or colour calibration. Additional front, side, rear and detail references improve confidence.

## Review and deliver

- Check silhouette and proportions against the original at comparable camera angles. Review handle asymmetry, body thickness, junction shape and material midtones, not just file validity.
- Export a GLB with embedded material/texture resources and no display floor, camera, lights, annotations or accidentally selected reference geometry. Keep editable source separately.
- Run the Khronos glTF validator when available. Use `scripts/inspect_glb.py model.glb --output inspection.json` to inspect bounds from actual vertex data; compare named component endpoints to confirmed measurements. This inspector is a geometry sanity check, not a replacement for the validator or visual review.
- Test the exported GLB in a real viewer: orbit, zoom, inspect materials and download. A studio HDR/viewer is a presentation setup; its reflections are not baked into an ordinary GLB. Disclose material differences between viewers when relevant.
- Show under-deck hardware in a complete-product view when it is part of the request. An installed view can conceal it; do not make the studio floor hide the feature being reviewed.
- Deliver the GLB, editable source, useful actual-model previews/viewer, and a short dimension/assumption record. Use portable resource references; do not embed developer-machine paths or private credentials in deliverables. Preserve previous versions.

## Store attachment

Creating a model does not itself authorize attaching it to a live product. When the user asks to attach it, verify the exact shop/product and latest accepted revision, preserve existing media, use the store's supported 3D upload flow, and verify processing readiness and live playback. Read the relevant store/API instructions and current documentation. Do not upload the review HTML or a rendered image as a substitute for a 3D asset, or imply that a stored file is already visible on the storefront.
