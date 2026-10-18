# Source-faithful product video production

## Photo mode

Use real source pixels as the product depiction. Uniform crop/scale/translation, conventional crossfades and separate text/vector overlays can add clarity without regenerating product details. Do not distort the image independently in X/Y, interpolate new viewpoints, or call an optical crop a true 3D camera orbit.

A useful 14-second hardware example (adapt the timing rather than treating it as a rule):

| Time | Customer value |
| --- | --- |
| 0–1 s | Full product orientation |
| 1–3.5 s | Actual left/right handle close-ups; show meaningful asymmetry |
| 3.5–5 s | Body, casting and union detail |
| 5–8 s | Height from mounting surface, animated extension line/arrow |
| 8–10.5 s | Mounting-centre close-up and spread |
| 10.5–13 s | Spout/outlet close-up and confirmed reach |
| 13–14 s | Full product with the dimension summary |

For another product, replace these features with its actual decision-relevant details. Shorten the shot list if text cannot be read comfortably. A tighter source crop improves inspection but does not create missing resolution; avoid extreme magnification or AI detail enhancement that invents machining marks or finish texture.

Keep dimension lines out of critical product details where possible. Show what the endpoints mean. Perspective can make same-height mounting points appear diagonally separated; annotate the confirmed centres rather than drawing the outside-width measurement. Use specification cards/schematics when direction is not supported by the photo. Arrows must not imply a certified scaled technical drawing.

Use large phone-readable numbers, sparse labels, neutral off-white/grey type and restrained brass-toned guides where suitable. Preserve the original photo's colour, including backgrounds and real reflections. Verify that the final codec/colour matrix does not introduce an orange/gold shift. Do not add generic sales claims or certifications.

## Model mode

Render the actual accepted GLB/editable source. Deterministically sample camera positions and overlay geometry at fixed timestamps; this keeps arrows and frame timing repeatable. Use the model's units, node transforms and mounting plane, not screen-space guesswork. Show the mounting plane clearly when height excludes lower threads.

Keep an orbit slow enough to inspect. A partial orbit with front/side holds can explain dimensions better than a rapid full turn. Use a reference-consistent studio environment and reveal material limitations honestly. Do not digitally move or operate individual components without supported kinematics and a request.

Generate hero, front, side and detail review frames from the actual render before encoding. Ensure labels do not clip as the camera moves and that the full product fits safe margins. For an installed/complete-product toggle, decide which configuration belongs in the video; don't hide requested hardware behind a floor by accident.

## Encoding and verification

Use a local FFmpeg installation or an explicitly located runtime binary. Avoid hard-coded developer-machine paths, bundled executables or downloaded tool chains in the skill. The included helper accepts `--ffmpeg` and standard numbered PNG frames; it does not install dependencies.

Preferred broadly compatible output: MP4/H.264, yuv420p, fast-start metadata, 1080-pixel-or-greater dimensions when the source supports it, 24/30 fps, and no audio for silent listing clips. Apply an explicit RGB-to-video colour matrix and verify decoded colours. White backgrounds compress efficiently; file size alone does not establish quality.

Check official destination requirements at execution time, not stale remembered limits:
- Etsy: https://help.etsy.com/hc/en-us/articles/360053206073-How-to-Add-Listing-Videos

Decode every frame for corruption and count/duration checks. Inspect actual decoded representative frames and transitions, including the first and last frame. Check measured duration, dimensions, codec, pixel format and file size; provide an actual output file. Save a small source/timing/measurement record for revision when useful. Keep test frames, runtime packages and encoder logs outside the skill repository.
