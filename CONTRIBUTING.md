# Contributing

Thanks for looking. This repo is public and the content is CC BY 4.0, so you are welcome to use,
adapt and share it. Contributions back are welcome too.

## What we take

**Fixes, without asking first.** Typos, broken links, wrong file paths, a Swedish or English
phrasing that reads badly, a reference that contradicts itself. Open a pull request.

**Method and behaviour changes, after an issue.** The skills carry scilla.studio's way of working
with product teams, so a change to what a method says or how a skill behaves is a change to our
practice. Open an issue and let's talk it through before you write it.

## How

Fork, branch off `main`, open a pull request. There is no ticket number to obtain and no branch
naming convention to follow — the `hello/sci-<n>` branches you see in the history are internal
and mean nothing here. Describe what you changed and why in the pull request body.

CI runs `python3 scripts/check-release-consistency.py` on every pull request. Run it locally
before pushing; it needs no dependencies.

## What to know before changing a skill

- `<plugin>/skills/<skill>/SKILL.md` tells Claude when and how to use a skill. Its `description`
  is the whole routing decision — Claude sees only names and descriptions until a skill fires.
  `CLAUDE.md` has the rules for writing one.
- `<plugin>/skills/<skill>/reference/` holds the method itself.
- A skill may read files inside its own plugin. It may not read anything above the plugin
  directory, and it may not depend on anything you have installed that an ordinary installer does
  not.
- If you change a skill's behaviour or content, bump `version` in **both**
  `<plugin>/.claude-plugin/plugin.json` and the plugin's entry in
  `.claude-plugin/marketplace.json`. Installed copies refresh on the version string, not on
  commits. The consistency check fails if the two disagree.
- Renaming or removing a skill breaks anyone already installed. Say so in the pull request.
- `product-knowledge/evals/` holds cases that check the right skill fires for a realistic
  prompt. If you change a description, add or adjust a case there; a description change is a
  routing change even when the wording looks cosmetic.

## What we cannot take

This repo carries no `.claude/` directory — no settings, no hooks, no agents, no commands — and
pull requests adding one will be declined. Hooks in `.claude/settings.json` run shell commands on
anyone who opens the repo in Claude Code, and this repo takes pull requests from strangers. The
same reasoning applies to anything else that would execute on a reader's machine.

## Licence

By contributing you agree your contribution is licensed under CC BY 4.0, the same as the rest of
the repo.
