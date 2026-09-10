# Our Skills — Guide and Usage

Last updated: 2026-09-10

This guide covers the two personal skills currently installed: Product Finish and Hatch Pet. Bundled system skills and third-party plugins are dependencies, not copies maintained by this library.

## Install in Codex

Install the complete skill folders so Codex receives the instructions, scripts, and visual references together.

### Option 1: clone with Git

On macOS or Linux, run:

```bash
git clone https://github.com/mkachtouli/mk-ai-skills.git
mkdir -p "$HOME/.agents/skills"
cp -R mk-ai-skills/skills/product-finish "$HOME/.agents/skills/"
cp -R mk-ai-skills/skills/hatch-pet "$HOME/.agents/skills/"
```

On Windows PowerShell, run:

```powershell
git clone https://github.com/mkachtouli/mk-ai-skills.git
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse mk-ai-skills/skills/product-finish "$HOME/.agents/skills/"
Copy-Item -Recurse mk-ai-skills/skills/hatch-pet "$HOME/.agents/skills/"
```

### Option 2: install without Git

1. Open the [repository](https://github.com/mkachtouli/mk-ai-skills).
2. Select **Code → Download ZIP** and extract it.
3. Create `.agents/skills` inside your user folder if it does not exist.
4. Copy the complete `product-finish` and `hatch-pet` folders from the repository's `skills` folder into `.agents/skills`.
5. Start a new Codex session. If the skills do not appear, restart Codex.

The installed layout should look like this:

```text
~/.agents/skills/
  product-finish/
    SKILL.md
    agents/
    references/
  hatch-pet/
    SKILL.md
    agents/
    references/
    scripts/
    tests/
```

Do not copy only `SKILL.md`. Product Finish needs its approved reference images, and Hatch Pet needs its supporting files.

### Confirm the installation

Start a new Codex chat and ask:

```text
What personal skills are available?
```

You should see `product-finish` and `hatch-pet`. You can also mention them explicitly as `$product-finish` or `$hatch-pet`. If a `$` mention is not offered by your Codex interface, use the skill name in ordinary text; Codex can match the request to its description.

Image generation must be available in the user's Codex environment. Product-page jobs also require permission to access the Etsy or Shopify page.

### Update an existing installation

Pull the latest repository version, then copy the folders again:

```bash
cd mk-ai-skills
git pull
cp -R skills/product-finish "$HOME/.agents/skills/"
cp -R skills/hatch-pet "$HOME/.agents/skills/"
```

Start a new Codex session after updating. If you made private changes inside an installed skill, save them before replacing its folder.

## Product Finish

Change the finish in product photographs while preserving the product design, camera angle, background, framing, and non-metal components. Uses the available image-generation editing tool.

| Shortcut | Result |
| --- | --- |
| `/PN-FINISH` | Polished Nickel |
| `/AC-FINISH` | Antique Copper |
| `/ORB-FINISH` | Oil-Rubbed Bronze, matched to our approved references |
| `/ALL-FINISH` | Three separate versions: PN, AC, and ORB |

These are instruction aliases, not registered application slash commands. Use `FINISH`; the older `FINCH` spelling has been retired.

### How to use it

Attach a product photograph and type `/PN-FINISH`, or another shortcut from the table.

Copy-ready examples:

```text
$product-finish /PN-FINISH
```

```text
$product-finish /ALL-FINISH
```

Attach the product photo to the same message. For an Etsy or Shopify listing:

```text
$product-finish https://example.com/product-page /AC-FINISH
Process all editable product photos from the listing gallery.
```

For a batch, attach several product photographs or identify a folder and say: “Use product-finish to convert all these photos with /ALL-FINISH.” Three finishes across five source photos means fifteen output images. Every finish starts from the original photograph.

For a product page, provide its Etsy or Shopify URL followed by the shortcut. Ask to collect the product gallery, identify the editable product photographs, and process those images. Gallery access depends on the available browsing tools and the website. If images cannot be retrieved, upload the originals. Keep dimension diagrams and instructions separate; do not treat unrelated recommendations as gallery images. This request creates edited files; it does not replace images on the live store.

### Finish standards

- **PN:** approved polished-nickel showerhead reference; reflective silver with subtle warmth and smooth polished surfaces.
- **AC:** approved antique-copper showerhead reference; muted reddish-brown copper, restrained satin sheen, darker recesses, and softly worn highlights.
- **ORB:** current four-photo reference set; medium-light muted golden bronze with olive-brown undertones, fine brushed grain, soft satin highlights, and dark patina concentrated in actual seams and recesses. The rounded-joint and overall-tube photos are the primary pair for every edit. Valve and cylinder details are supporting references.

Always supply the actual approved reference images to the image editor. A written color description alone is insufficient for our workflow. New explicitly approved references supersede older ones. Keep the same reference set across a batch. The older bronze showerhead reference is historical.

Transfer the material appearance only. Preserve the target's geometry, markings, holes, fittings, component count, and background. Review generated results for shape drift and finish consistency. Reference-guided edits are visual approximations, not guaranteed exact color matches.

### Results

Results normally go into `outputs/product-finish/<run-id>/`. Filenames use `_PN`, `_AC`, or `_ORB` with the actual image format extension. Preserve originals and version replacements. Batches include a manifest recording sources, references, prompts, output paths, status, and unresolved issues. Resume only unfinished jobs after an interruption.

## Hatch Pet

Create or repair an animated Codex pet using a description, character artwork, or brand references. This skill uses image generation and supporting preparation, assembly, validation, and preview tools.

### How to use it

- “Use hatch-pet to create a small friendly copper robot named Pip.”
- Attach artwork and say: “Use hatch-pet to turn this character into an animated Codex pet. Preserve its colors and face.”
- Provide an existing pet and say: “Use hatch-pet to inspect and repair this pet while preserving its identity.”

You can also invoke it explicitly:

```text
$hatch-pet Create a small friendly copper robot named Pip.
```

You can specify the pet's name, personality, style, colors, and references. Missing optional details can be inferred from the concept. Brand-based work can require research to establish visual cues.

### Results and requirements

Produces a v2 pet package with an 8 × 11 sprite atlas, nine standard animation rows, sixteen look directions, and review previews. Its workflow requires the image-generation skill and the bundled workspace runtime with Pillow. It is intended for Codex pet production; ordinary browser image generation alone does not replace its assembly and validation tools.

## Where these skills work

The current copies are local Codex skills. A Markdown guide documents usage; it does not install the skills or carry their image assets and scripts by itself.

For another Codex installation, follow **Install in Codex** above. Transfer the complete skill folders, including references and supporting tools, and confirm they appear before running them.

For ChatGPT in a browser, Product Finish can be adapted into project instructions with the approved images, or packaged as a compatible plugin. Local paths and local installations do not automatically transfer. Browser image editing, gallery collection, and bulk delivery must be checked in that environment. Hatch Pet additionally requires its execution and packaging dependencies.

## Git repository and update workflow

Recommended repository layout:

```text
README.md
CHANGELOG.md
skills/
  product-finish/
    SKILL.md
    references/
    agents/
  hatch-pet/
    SKILL.md
    scripts/
    ...other required supporting files
```

Track complete skill source folders and approved references. Keep generated product batches, temporary files, credentials, and unrelated personal files outside the repository. Prefer a private repository for this personal library.

When updating a skill:

1. Apply the requested change to the maintained source and update this guide if usage changes.
2. Add a dated entry to `CHANGELOG.md`, including any reference replacement.
3. Check the skill metadata, referenced files, and relevant behavior. Inspect image references when finish standards change.
4. Review the diff, commit the intended changes, and push to the agreed repository and branch.
5. Update the installed local copy from the reviewed source so the repository and installed skill agree.

Future pushes require a configured repository and working authentication. This guide does not start a background watcher or automatic synchronization. Ask “Update the skill and push the changes” during future work, or configure a separate automation if automatic updates are desired.

## Repository

Maintain this library at [mkachtouli/mk-ai-skills](https://github.com/mkachtouli/mk-ai-skills). Use the repository source for future reviewed updates. Automatic background synchronization is not enabled.
