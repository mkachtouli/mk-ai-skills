# MK AI Skills

A growing library of reusable skills for Codex. Each skill lives in its own folder and contains the instructions, references, scripts, and assets needed for that workflow.

This repository currently includes Product Finish and Hatch Pet. Future skills can cover workflows such as Etsy-to-Shopify listing migration, listing SEO checks, product content, and store operations.

## Skill catalog

| Skill | Purpose | Main invocation |
| --- | --- | --- |
| [product-finish](skills/product-finish/) | Convert brass product photos to approved Polished Nickel, Antique Copper, or Oil-Rubbed Bronze finishes | `$product-finish` |
| [hatch-pet](skills/hatch-pet/) | Create, repair, validate, and package animated Codex pets | `$hatch-pet` |

The catalog will grow as new skills are added. A planned workflow should become a real folder only when its `SKILL.md` and required resources are ready.

## Repository structure

```text
mk-ai-skills/
├── README.md                 Library catalog, installation, and usage
├── CONTRIBUTING.md           Rules for adding and updating skills
├── CHANGELOG.md              Repository-wide changes
└── skills/
    ├── product-finish/
    │   ├── SKILL.md          Required skill instructions
    │   ├── agents/           Optional Codex interface metadata
    │   └── references/       Approved finish references
    ├── hatch-pet/
    │   ├── SKILL.md
    │   ├── agents/
    │   ├── references/
    │   ├── scripts/
    │   └── tests/
    └── future-skill-name/
        ├── SKILL.md
        └── optional resources only when needed
```

Every folder directly inside `skills/` is an independent installable skill. Use lowercase, action-oriented names with hyphens, such as `etsy-to-shopify` or `etsy-seo-audit`.

## Install in Codex

### Clone the library

```bash
git clone https://github.com/mkachtouli/mk-ai-skills.git
cd mk-ai-skills
```

### Install one skill on macOS or Linux

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/product-finish "$HOME/.agents/skills/"
```

Replace `product-finish` with the folder name shown in the catalog.

### Install all skills on macOS or Linux

```bash
mkdir -p "$HOME/.agents/skills"
cp -R skills/* "$HOME/.agents/skills/"
```

### Install one skill on Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse skills/product-finish "$HOME/.agents/skills/"
```

### Install all skills on Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse skills/* "$HOME/.agents/skills/"
```

### Install without Git

1. Select **Code → Download ZIP** on this repository.
2. Extract the archive.
3. Create `.agents/skills` inside your user folder.
4. Copy the complete folders you want from `skills/` into `.agents/skills/`.
5. Start a new Codex session. Restart Codex if the skills do not appear.

Copy the complete skill folder, not only `SKILL.md`. Some skills depend on bundled references, scripts, tests, or assets.

### Confirm installation

Start a new Codex chat and ask:

```text
What personal skills are available?
```

Installed skills should appear by name. Invoke one explicitly with `$skill-name`, or describe a matching task and let Codex select it automatically.

Availability of image generation, internet access, connected apps, and other tools depends on the user's Codex environment and permissions.

## Update installed skills

Pull the latest repository changes:

```bash
cd mk-ai-skills
git pull
```

Then copy the updated skill folder to `.agents/skills/` again and start a new Codex session. Save any private edits made inside an installed copy before replacing it.

## Product Finish

Attach a brass product photograph and use one of these instructions:

| Shortcut | Result |
| --- | --- |
| `/PN-FINISH` | Polished Nickel |
| `/AC-FINISH` | Antique Copper |
| `/ORB-FINISH` | Oil-Rubbed Bronze using the approved reference set |
| `/ALL-FINISH` | Separate PN, AC, and ORB versions |

Example:

```text
$product-finish /PN-FINISH
```

For several attached photos:

```text
$product-finish /ALL-FINISH
Process every attached product photo. Start each finish from the original.
```

For an Etsy or Shopify product page:

```text
$product-finish https://example.com/product-page /AC-FINISH
Process all editable product photos from the listing gallery.
```

The finish shortcuts are aliases defined by the skill, not application slash commands. Use `FINISH`; the retired `FINCH` spelling is not the current standard.

The skill includes the approved material references and preserves product geometry, background, crop, lighting direction, and non-brass components. Generated images should have consistent material direction, but they will not be pixel-identical between runs. Product-page access requires internet permission. The skill produces edited files and does not update a live Etsy or Shopify listing.

## Hatch Pet

Examples:

```text
$hatch-pet Create a small friendly copper robot named Pip.
```

```text
$hatch-pet Turn the attached character art into an animated Codex pet. Preserve its face and colors.
```

The skill creates a Codex-compatible v2 pet package with an 8 × 11 sprite atlas, standard animation rows, look directions, and review previews. It requires image generation and the bundled runtime used by its scripts.

## Add another skill

Follow [CONTRIBUTING.md](CONTRIBUTING.md). In brief:

1. Create `skills/<skill-name>/`.
2. Add a complete `SKILL.md` with `name` and `description` frontmatter.
3. Add only the references, scripts, assets, tests, or agent metadata the workflow actually needs.
4. Validate the skill and test meaningful behavior.
5. Add the skill to the catalog above and record the change in `CHANGELOG.md`.

Keep Etsy-to-Shopify migration and SEO auditing as separate skills because they have different triggers, inputs, tools, and outputs. They can cooperate when a user asks for both workflows.

## Compatibility

These folders are standalone skills for Codex desktop, CLI, and IDE environments that support personal skills. ChatGPT browser distribution requires packaging skills in a compatible plugin; cloning this repository alone does not install them in ChatGPT web.

## Repository

Maintained at [mkachtouli/mk-ai-skills](https://github.com/mkachtouli/mk-ai-skills). Automatic background synchronization is not enabled.
