# scilla-skills

Public Claude Code plugin marketplace for scilla.studio. Everything here is visible to anyone on the internet, so nothing client-specific goes in: no client names, no engagement material, no ticket numbers, no paths into other scilla repos.

The private marketplace lives in `scilla-studio-stockholm/claude-plugins` and stays private.

## Layout

- `.claude-plugin/marketplace.json` lists the plugins.
- `<plugin>/.claude-plugin/plugin.json` is the plugin manifest. Its `version` decides whether installed copies refresh.
- `<plugin>/skills/<skill>/SKILL.md` tells Claude when and how to use the skill.
- `<plugin>/skills/<skill>/reference/` holds the method itself, cleaned for a public reader.

## Adding a knowledge skill

1. Copy the source doc from `scilla-studio/core/knowledge/` into `reference/`, then strip wiki-links, ticket numbers, client names, repo paths and internal history.
2. Write `SKILL.md` with a `description` that names the situations and phrases that should trigger it, in English and Swedish.
3. Bump the plugin version in both manifests and update the README table.
4. `python3 scripts/check-release-consistency.py`.

## Workflow

Ticket-first, per the global rules. Branch `hello/sci-<n>-<desc>`, base `main`. Every change reaches `main` through a pull request with the release-consistency check green; a ruleset on the repo refuses direct pushes, force-pushes and deletions, with no bypass for anyone. People install this marketplace with auto-update on, so a broken manifest on `main` reaches their machines within a session. Licence is CC BY 4.0 (`LICENSE`).
