# scilla-skills

Product management knowledge and skills from [scilla.studio](https://scilla.studio), packaged as Claude Code plugins. One skill per method. The list grows one skill at a time.

## Install

In Claude Code:

```
/plugin marketplace add scilla-studio-stockholm/scilla-skills
/plugin install product-knowledge@scilla-skills
```

Then switch on auto-update so new skills reach you without a manual step: `/plugin`, then **Marketplaces**, then `scilla-skills`, then **Enable auto-update**. Without it, run `/plugin marketplace update scilla-skills` whenever you want the latest.

Plugins load in Claude Code only (the terminal, the Code tab in the Claude desktop app, and Claude Code on the web). The ordinary Claude chat window does not read marketplaces.

## What is in it

| Plugin | Skills |
|---|---|
| `product-knowledge` | `product-foundations`: the four statements that describe one product, and how to run the two-hour exercise with a team |

Each skill folder holds a `SKILL.md` that tells Claude when and how to use it, and a `reference/` folder with the method itself.

## Releasing a change

Installed plugins refresh only when the plugin's version string changes. Commits alone do nothing.

1. Edit the skill.
2. Bump `version` in both `<plugin>/.claude-plugin/plugin.json` and the plugin's entry in `.claude-plugin/marketplace.json`, in the same commit.
3. Run `python3 scripts/check-release-consistency.py`. CI runs the same check.
4. Push to `main`.

## Licence

Copyright scilla.studio. Read and use freely; ask before republishing the material elsewhere.
