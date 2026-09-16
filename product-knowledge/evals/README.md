# Evals

Ten cases that measure whether the right skill fires, and whether the answer is the
method rather than an approximation of it. Those are two different qualities and only
the second is visible by reading a reply.

A reply can be good because Claude already knows a fair amount about product discovery,
with no skill involved at all. That is the failure these cases exist to make visible.

## The cases

| Case | Expects | Tests |
|---|---|---|
| `teach-method-sv` | `customer-interviews` | The teach path. Nothing in hand. |
| `plan-round-sv` | `customer-interviews` | The plan path. An outcome in hand. |
| `review-questions-sv` | `customer-interviews` | The review path. Four questions, each broken differently. |
| `ambiguous-intervjufragor-sv` | `customer-interviews` | The prompt that reached two different skills before 0.5.0. |
| `vague-start-sv` | `customer-interviews` | No artifact, no vocabulary. Who owns the vague entry. |
| `boundary-find-opportunities-sv` | `find-opportunities` | Interviews are done. The interview skill must stay out. |
| `boundary-define-outcomes-sv` | `define-outcomes` | The word *outcome* appears in both descriptions. |
| `boundary-clean-transcript-sv` | `clean-transcript` | A raw transcript, upstream of extraction. |
| `english-fallback` | `customer-interviews` | The English arm, for installers who found the repo on GitHub. |
| `no-skill-expected` | nothing | A plugin that grabs unrelated questions costs every installer. |

Prompts are in customer Swedish with no method jargon, because that is how the people
these skills are for actually write. The English arm is thinner on purpose.

Each case has `prompt.md`, `graders/routing.md` (which skill fired) and
`graders/quality.md` (whether the answer is the method).

## Running them

### The real harness, when early access lands

```
claude plugin eval product-knowledge@scilla-skills --runs 5 --ablation with-without
```

`--ablation with-without` adds a no-plugin baseline arm and reports the score delta.
That delta is the number worth having: it separates "the skill is good" from "the model
already knew this". Without it a suite can score well on knowledge the plugin did not
contribute.

`claude plugin eval` is in early access. If it is not enabled on your account it exits
with `plugin eval is currently in early access`, and the probe below covers the routing
half in the meantime.

### The routing probe, today

```
CLAUDE_CONFIG_DIR=/tmp/scilla-eval claude          # once: /login, then exit
CLAUDE_CONFIG_DIR=/tmp/scilla-eval python3 scripts/routing-probe.py --setup
CLAUDE_CONFIG_DIR=/tmp/scilla-eval python3 scripts/routing-probe.py --runs 5
```

It reports, per case, which skill fired and how often. It does not grade answers.

**`CLAUDE_CONFIG_DIR` is not optional.** A throwaway config holding only this
marketplace is the whole point. Run it against a personal setup and you measure that
setup. On the machine where this suite was written, `ambiguous-intervjufragor-sv`
scored 0/2 under the author's own harness: a private plugin with an overlapping skill
won every time and `customer-interviews` never fired. Credentials are per config dir,
which is why the login step is separate.

Runs happen in an empty temporary directory, so no `CLAUDE.md` is in scope. Bash, Edit,
Write, WebFetch and WebSearch are denied and `--strict-mcp-config` keeps MCP servers
out. Skill and Read stay, because a skill has to be able to fire and read its own
reference files.

## Reading the result

**Stability is the metric, not any single run.** A prompt that reaches
`customer-interviews` three runs in five and `find-opportunities` twice has a boundary
that is not real, and it will find a customer eventually. Five runs is the floor; the
probe prints the spread whenever a case routes more than one way.

A case that fails every run is usually a description problem, not a method problem. Two
skills describing the same situation, or one description written so broadly that it
swallows a neighbour. `CLAUDE.md` has the rules for fixing that.

## Format

Cases use the `prompt.md` + `graders/*.md` layout that `claude plugin eval` documents.
The frontmatter keys in the routing graders (`with-only`, `tool_used`, `expect`) follow
what the CLI help describes but have not been run against the tool itself, since early
access is not enabled here. Expect to adjust them on first real run. The prompts and the
grading criteria are the expensive part and do not depend on that.
