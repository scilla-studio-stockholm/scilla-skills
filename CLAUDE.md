# scilla-skills

Public Claude Code plugin marketplace for scilla.studio. Anyone on the internet can read this
repo, clone it, and install what it ships.

**This file is the only rules file that applies here.** It does not defer to global rules, to
another repo's CLAUDE.md, or to anything in the private `scilla-studio` marketplace. If a rule
matters for this repo, it is written out below. If you arrived from another scilla repo, leave
its conventions there.

## The isolation rule

This repo is self-contained, in both directions.

**Nothing private comes in.** No client names, no engagement material, no ticket numbers in
shipped files, no paths into other scilla repos, no dependency on a private plugin, skill, hook,
agent, output style or rules file. A skill here must work for someone who has installed nothing
else. When a method comes from `scilla-studio/core/knowledge/`, the copy in `reference/` is
cleaned for a public reader and then stands on its own.

**Nothing local goes out.** This repo carries **no `.claude/` directory** — no settings, no
hooks, no agents, no commands. That is deliberate and not an oversight to fix. `.claude/settings.json`
hooks run shell commands on anyone who opens the repo in Claude Code, and this repo takes pull
requests from strangers. `.claude/` is in `.gitignore` so a local experiment cannot be committed
by accident.

Personal session config for working in this repo goes in `.claude/settings.local.json`, which is
ignored and never leaves the machine. Prefer not needing it.

**The plugin ships only what is under `product-knowledge/`.** A skill may read files inside its
own plugin, including a sibling skill's `reference/`. It may not read anything above the plugin
directory.

## Layout

- `.claude-plugin/marketplace.json` lists the plugins.
- `<plugin>/.claude-plugin/plugin.json` is the plugin manifest. Its `version` decides whether
  installed copies refresh.
- `<plugin>/skills/<skill>/SKILL.md` tells Claude when and how to use the skill.
- `<plugin>/skills/<skill>/reference/` holds the method itself, cleaned for a public reader.

## Writing a SKILL.md

The `description` is the whole routing decision. Claude sees the name and description of every
skill and nothing else until one fires, so any disambiguation has to live in the description.

- Route on **what the asker has in hand** — nothing yet, an outcome, a raw transcript, a cleaned
  transcript, a draft list — not on where they are in the method. Customers do not announce the
  stage.
- Put the discriminator early, not in a closing sentence.
- Name the situations and phrases that should trigger it, in Swedish and English. Customers are
  Swedish, so Swedish is the primary path; English is there for the rest of the internet.
- Carry the discriminating verb in both languages. Swedish compounds collapse distinctions
  (*intervjufrågor* covers writing them and reviewing them), so *ta fram* / *skriv* / *planera*
  against *granska* / *kolla* / *är … bra* is what separates two skills.
- No trigger phrase may appear in two skills' descriptions without a distinguishing verb in both.
- Keep the description at 1024 characters or fewer. Claude Code rejects longer ones.
- When two skills keep colliding, merge them. Removing the routing decision beats improving it
  (SCI-1016).

## Adding a knowledge skill

1. Copy the source doc from `scilla-studio/core/knowledge/` into `reference/`, then strip
   wiki-links, ticket numbers, client names, repo paths and internal history.
2. Write `SKILL.md` per the rules above.
3. Bump the plugin version in both manifests and update the README table.
4. `python3 scripts/check-release-consistency.py`.

## Workflow

Ticket-first: work is tracked in Linear, team Scilla (`SCI`). Branch `hello/sci-<n>-<desc>`, base
`main`. Every change reaches `main` through a pull request with the release-consistency check
green; a ruleset on the repo refuses direct pushes, force-pushes and deletions, with no bypass
for anyone. Ticket numbers stay in Linear and in commit messages, never in shipped files.

People install this marketplace with auto-update on, so a broken manifest on `main` reaches their
machines within a session. Removing or renaming a skill is a breaking change for anyone already
installed; say so in the release note.

Licence is CC BY 4.0 (`LICENSE`).
