#!/usr/bin/env python3
"""Check that the marketplace manifest agrees with every plugin manifest.

This repo IS the marketplace, so a mismatch here ships silently: `plugin.json`
wins when both are set — it's what actually resolves and ships to a user.
`.claude-plugin/marketplace.json` is only what the catalog advertises in
`/plugin` listings. Bumping only `plugin.json` still propagates the update,
but the marketplace catalog then misreports what's shipping.

In the private scilla marketplace this drift shipped four times despite a
README checklist describing the trap. A checklist is not a guard; this is.

Usage:
    python3 scripts/check-release-consistency.py

Exits 0 when clean, 1 when it finds a problem. No dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

# Skill directories whose frontmatter `name` is deliberately not the directory
# name. None yet in this repo.
NAME_MISMATCH_OK = re.compile(r"$^")


def load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as exc:
        print(f"  INVALID JSON  {path.relative_to(REPO)}: {exc}")
        return None


def main() -> int:
    problems: list[str] = []

    marketplace = load_json(MARKETPLACE)
    if marketplace is None:
        print(f"FAIL: cannot read {MARKETPLACE.relative_to(REPO)}")
        return 1

    entries = marketplace.get("plugins", [])
    if not entries:
        problems.append("marketplace.json lists no plugins")

    seen_sources = set()

    for entry in entries:
        name = entry.get("name", "<unnamed>")
        source = entry.get("source", "")
        if not source:
            problems.append(f"{name}: marketplace entry has no source")
            continue

        plugin_dir = (REPO / source.lstrip("./")).resolve()
        seen_sources.add(plugin_dir)

        if not plugin_dir.is_dir():
            problems.append(f"{name}: source {source} does not exist")
            continue

        manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
        manifest = load_json(manifest_path)
        if manifest is None:
            problems.append(f"{name}: missing or unreadable {manifest_path.relative_to(REPO)}")
            continue

        # The one that actually breaks installs.
        mk_version = entry.get("version")
        pj_version = manifest.get("version")
        if mk_version != pj_version:
            problems.append(
                f"{name}: VERSION DRIFT — marketplace.json says {mk_version!r}, "
                f"plugin.json says {pj_version!r}. plugin.json resolves and is what "
                f"ships; the marketplace catalog is now misreporting what's running."
            )

        if manifest.get("name") != name:
            problems.append(
                f"{name}: plugin.json name is {manifest.get('name')!r}, "
                f"marketplace entry is {name!r}"
            )

        if entry.get("description") != manifest.get("description"):
            problems.append(
                f"{name}: description differs between marketplace.json and plugin.json"
            )

        mk_author = (entry.get("author") or {}).get("name")
        pj_author = (manifest.get("author") or {}).get("name")
        if mk_author != pj_author:
            problems.append(
                f"{name}: author differs — marketplace {mk_author!r}, plugin {pj_author!r}"
            )

        skills_dir = plugin_dir / "skills"
        if skills_dir.is_dir():
            for skill in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
                problems.extend(check_skill(skill, plugin_dir))

    # A plugin directory that exists but nothing publishes is invisible to the team.
    for candidate in sorted(REPO.iterdir()):
        if not candidate.is_dir() or candidate.name.startswith("."):
            continue
        if (candidate / ".claude-plugin" / "plugin.json").is_file():
            if candidate.resolve() not in seen_sources:
                problems.append(
                    f"{candidate.name}: has a plugin.json but no marketplace.json entry "
                    f"— it will not be installable"
                )

    if problems:
        print(f"FAIL: {len(problems)} release-consistency problem(s)\n")
        for p in problems:
            print(f"  - {p}")
        print("\nSee README.md → 'Releasing a plugin update'.")
        return 1

    print(f"OK: {len(entries)} plugins, marketplace and plugin manifests agree.")
    return 0


def check_skill(skill: Path, plugin_dir: Path) -> list[str]:
    """Validate one skill directory. Returns a list of problems."""
    rel = skill.relative_to(REPO)
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        return [f"{rel}: no SKILL.md"]

    text = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return [f"{rel}: SKILL.md has no YAML frontmatter"]

    frontmatter = match.group(1)
    problems = []

    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
    if not name_match:
        problems.append(f"{rel}: SKILL.md frontmatter has no name")
    elif name_match.group(1).strip() != skill.name and not NAME_MISMATCH_OK.match(skill.name):
        problems.append(
            f"{rel}: frontmatter name {name_match.group(1).strip()!r} "
            f"does not match directory name"
        )

    if not re.search(r"^description:\s*\S", frontmatter, re.M):
        problems.append(f"{rel}: SKILL.md frontmatter has no description")

    return problems


if __name__ == "__main__":
    sys.exit(main())
