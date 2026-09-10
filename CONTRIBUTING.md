# Adding and Updating Skills

This repository holds independent Codex skills. Keep each workflow isolated so users can install only what they need.

## Add a skill

1. Choose a short lowercase name using letters, digits, and hyphens. The folder name and the `name` field in `SKILL.md` must match.
2. Create `skills/<skill-name>/SKILL.md`.
3. Add YAML frontmatter with a concise, discriminating `name` and `description`.
4. Put the essential workflow and constraints in `SKILL.md`.
5. Add optional resources only when they improve the actual workflow:
   - `agents/openai.yaml` for interface metadata or invocation policy.
   - `references/` for focused instructions, schemas, policies, or approved visual references.
   - `scripts/` for reusable deterministic operations.
   - `assets/` for templates or files copied into outputs.
   - `tests/` for meaningful behavior or script validation.
6. Link conditional references from `SKILL.md` and say when Codex should read them.
7. Validate the skill, verify all linked files, and run relevant tests.
8. Add the finished skill to the catalog in `README.md` and add a dated entry to `CHANGELOG.md`.

Do not create empty future-skill folders. Do not put generated outputs, credentials, local environments, caches, or customer data in the repository.

## Design rules

- Keep skills independent and installable by copying one complete folder.
- Keep discovery descriptions precise so unrelated requests do not activate the skill.
- Separate workflows when they have different triggers or side effects. For example, `etsy-to-shopify` should handle listing transfer, while `etsy-seo-audit` should inspect and recommend SEO changes.
- Preserve user authorization boundaries. A skill that prepares a listing does not automatically have permission to publish it.
- Use references for substantial conditional detail instead of loading every procedure in `SKILL.md`.
- Include scripts when deterministic execution materially improves reliability; test new or changed scripts.
- Never store API keys, access tokens, shop credentials, or private customer files.

## Suggested future layout

```text
skills/
  etsy-to-shopify/
    SKILL.md
    references/
      listing-field-map.md
    scripts/
      optional-import-helper.*
  etsy-seo-audit/
    SKILL.md
    references/
      seo-checklist.md
```

This is a design example, not a request to create those files before the workflows are defined.

## Updating an existing skill

1. Change the repository copy of the skill.
2. Keep names, descriptions, interface metadata, instructions, and supporting resources consistent.
3. Validate affected files and behavior.
4. Update the root documentation when invocation or output behavior changes.
5. Record the change in `CHANGELOG.md`.
6. Review the diff, commit it, and push it to the intended branch.

Use the repository as the maintained source. After a reviewed update, copy the revised folder into the local Codex skills directory and start a new session.
