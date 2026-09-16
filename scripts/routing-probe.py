#!/usr/bin/env python3
"""Measure which skill fires for each eval prompt, over N runs.

`claude plugin eval` is the real harness: it grades answers, runs a no-plugin
baseline arm, and reports a score delta. This script is not that. It answers the
one question the graders cannot answer by reading a reply — which skill actually
fired — and it answers it repeatedly, because the signal is stability rather than
any single run.

A prompt that reaches `customer-interviews` three runs in five and
`find-opportunities` twice has a description boundary that is not real. That shows
up here and nowhere else.

Isolation is the point. Runs go through a throwaway CLAUDE_CONFIG_DIR holding only
this marketplace, so the personal harness (other plugins, an output style injected
every turn, MCP servers) cannot flatter the result. That config dir needs its own
login once, because credentials are per config dir:

    CLAUDE_CONFIG_DIR=/tmp/scilla-eval claude          # then /login, then exit

Then:

    CLAUDE_CONFIG_DIR=/tmp/scilla-eval \
      python3 scripts/routing-probe.py --setup
    CLAUDE_CONFIG_DIR=/tmp/scilla-eval \
      python3 scripts/routing-probe.py --runs 5

Each run denies the tools that would let a session go exploring (Bash, Edit, Write,
WebFetch, WebSearch) and passes --strict-mcp-config so no MCP server loads. Skill and
Read stay available, because a skill has to be able to fire and read its own reference
files. --allowed-tools alone does not restrict anything: it widens what runs without a
prompt, it does not narrow what the model may reach for.

Turns are capped at 4. One is not enough: a session can spend its first turn orienting
itself and never answer, which reads as "no skill fired" when the truth is "no reply
happened".

Every run happens in an empty temporary directory. Running from inside this repo would
load this repo's CLAUDE.md, which is maintainer instruction and nothing a customer has.
The working directory is part of the environment being controlled.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EVALS = REPO / "product-knowledge" / "evals"
MARKETPLACE = "scilla-studio-stockholm/scilla-skills"
PLUGIN = "product-knowledge@scilla-skills"

EXPECT = re.compile(r"^The session invoked the skill `([^`]+)`", re.M)
EXPECT_NONE = re.compile(r"^expect:\s*none\s*$", re.M)


def expected_skill(case: Path) -> str | None:
    """Read the routing grader. Returns a skill name, or None when none should fire."""
    grader = (case / "graders" / "routing.md").read_text()
    if EXPECT_NONE.search(grader):
        return None
    match = EXPECT.search(grader)
    if not match:
        sys.exit(f"{case.name}: routing.md names no skill and does not expect none")
    return match.group(1)


def skills_fired(stream: str) -> list[str]:
    """Pull Skill invocations out of a stream-json transcript."""
    fired = []
    for line in stream.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") != "assistant":
            continue
        for block in event.get("message", {}).get("content", []):
            if isinstance(block, dict) and block.get("type") == "tool_use":
                if block.get("name") == "Skill":
                    name = (block.get("input") or {}).get("skill")
                    if name:
                        fired.append(name)
    return fired


def run_once(prompt: str, model: str | None, max_turns: int) -> tuple[list[str], str]:
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "stream-json", "--verbose",
        "--max-turns", str(max_turns),
        # Keep the session on the question. Skill and Read stay, because a skill must
        # be able to fire and read its own reference files.
        "--disallowed-tools", "Bash", "Edit", "Write", "WebFetch", "WebSearch",
        "--strict-mcp-config",
    ]
    if model:
        cmd += ["--model", model]
    # An empty cwd: no CLAUDE.md, no project memory, nothing to orient against.
    with tempfile.TemporaryDirectory(prefix="routing-probe-") as clean:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              stdin=subprocess.DEVNULL, cwd=clean)
    if "Not logged in" in proc.stdout:
        sys.exit("Not logged in in this CLAUDE_CONFIG_DIR. See the docstring.")
    return skills_fired(proc.stdout), proc.stdout


def setup() -> int:
    if not os.environ.get("CLAUDE_CONFIG_DIR"):
        sys.exit("Refusing to run without CLAUDE_CONFIG_DIR: setup would install into "
                 "your real config and stop the run being isolated.")
    for cmd in (["claude", "plugin", "marketplace", "add", MARKETPLACE],
                ["claude", "plugin", "install", PLUGIN]):
        print("  " + " ".join(cmd))
        subprocess.run(cmd, check=False)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--max-turns", type=int, default=4)
    parser.add_argument("--case", help="only cases whose name contains this")
    parser.add_argument("--model", help="pass through to claude --model")
    parser.add_argument("--setup", action="store_true",
                        help="add the marketplace and install the plugin, then exit")
    args = parser.parse_args()

    if args.setup:
        return setup()

    if not os.environ.get("CLAUDE_CONFIG_DIR"):
        print("WARNING: CLAUDE_CONFIG_DIR is unset, so this runs under your personal\n"
              "         harness. Every other plugin, output style and MCP server you\n"
              "         have installed is in play, and a customer has none of them.\n",
              file=sys.stderr)

    cases = sorted(p for p in EVALS.iterdir() if (p / "prompt.md").is_file())
    if args.case:
        cases = [c for c in cases if args.case in c.name]
    if not cases:
        sys.exit("no cases matched")

    unstable = failed = 0
    for case in cases:
        prompt = (case / "prompt.md").read_text().strip()
        want = expected_skill(case)
        tally: Counter[str] = Counter()
        for _ in range(args.runs):
            fired, _ = run_once(prompt, args.model, args.max_turns)
            tally[fired[0] if fired else "(none)"] += 1

        want_key = want or "(none)"
        hits = tally[want_key]
        stable = len(tally) == 1
        ok = hits == args.runs
        mark = "ok  " if ok else ("MIX " if hits else "FAIL")
        if not ok:
            failed += 1
        if not stable:
            unstable += 1
        spread = "  ".join(f"{k} x{v}" for k, v in tally.most_common())
        print(f"{mark} {case.name:34} want {want_key:44} {hits}/{args.runs}")
        if not stable:
            print(f"     routed to: {spread}")

    print(f"\n{len(cases)} cases, {args.runs} runs each. "
          f"{failed} did not always reach the expected skill, "
          f"{unstable} routed inconsistently.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
