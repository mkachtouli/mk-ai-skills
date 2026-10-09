# Studio standard — version 1

## Provenance

`studio-anchor.png` is the exact 1254 × 1254 PNG supplied on 2026-10-09 and selected by the user as the Studio Image photographic direction. It shows a golden bridge faucet against white with softbox highlights and a fading surface reflection. It is a **style anchor**, not a universal product or finish swatch. Retain the untouched reference for provenance; never reproduce its lower-left Brassty watermark in deliverables. Replace this standard only when the user requests an update.

## Theme

High-key photography with readable metal, not flat or overexposed. Broad pale highlights and narrower dark bands articulate the actual target's curvature. Neutral softboxes and reflection cards create the material reflections, without household scenery. Highlight shape must follow the target, not the anchor faucet.

Near-white seamless backdrop with restrained gray falloff, no strong horizon, room or decorative texture. Isolated, sharp product with comfortable margins. Balance framing according to the target shape rather than imposing the faucet's bounding box.

The surface reflection follows the camera and surface plane, begins at real contact points, and loses contrast quickly below. Keep it much lighter than the product. Avoid a second solid upside-down object, mirror lettering, heavy gray shadows or watery ripples. The mark in the lower-left corner is excluded from the style.

## Material behavior

| Target finish | Studio light response |
| --- | --- |
| Unlacquered Brass | Preserve actual brass tone, polish, variation and existing patina; no invented aging. |
| Lacquered Brass | Preserve clear-coated brass color and gloss; elongated highlights on polished surfaces. |
| Polished Nickel | Silver with the target's subtle warm undertone; bright and dark reflection bands, no yellow brass wash. |
| Antique Copper | Preserve red-brown copper, dark recesses and fine texture; broad subdued highlights appropriate to satin sheen. |
| Oil-Rubbed Bronze | Preserve dark brown/bronze and warm highlights with subdued reflectivity; no gray wash or polished-gold conversion. |
| Brushed or matte surface | Preserve directional texture and roughness; soften highlights instead of adding mirror gloss. |

These describe lighting behavior, not an automatic finish conversion. The target or an explicitly requested material reference takes precedence.

## Product adaptations

**Bridge and deck faucets, freestanding pieces:** keep orientation, spacing and all feet. Place the assembly on a white glossy plane with a faint reflection under actual contact points. Preserve outlets and handle details.

**Wall-mounted products:** keep flange arrangement, projection and mounting. Use a seamless white support/background and soft local mounting shadows. Add a restrained lower surface reflection only when the source-supported plane and viewpoint make it physically plausible. Otherwise retain the studio backdrop and metal highlights without inventing feet, a counter, a basin or a duplicate floating below.

**Shower systems and tall assemblies:** retain every source-supported head, arm, riser, mixer, bracket, handset and hose path. Fit the full height with appropriate canvas space or uniform scaling; never shorten pipes or simplify hoses. Preserve wall attachments and local shadows. Omit an impossible floor reflection when the system does not meet a visible floor plane.

**Small hardware and other products:** retain real configuration and source angle, with comfortable margins and physically supported placement. Keep openings, perforations, screws, threads, seams and engraving readable. Do not impose the anchor faucet's standing pose.

## Example decisions

- `$studio-image` + Antique Copper wall faucet: one studio edit, copper satin, original plates and perspective, no deck feet or watermark.
- `$studio-image` + Polished Nickel shower system: keep nickel and all visible components, fit full height, no gold faucet silhouette or impossible floor reflection.
- `Studio Image, process every photo in this folder`: one output per target, each existing finish retained, references excluded, separate files and resumable manifest.
- `$studio-image, make this brass faucet Polished Nickel`: explicit conversion with an appropriate material reference, original geometry evidence and saved studio theme.
- `$studio-image` with no target: request the product image; do not treat the bundled anchor as the target.
