---
with-only: true
tool_used: Skill
---

# Routing

The session invoked the skill `product-knowledge:customer-interviews`.

This is the prompt that was ambiguous before the two interview skills merged: it carries neither *ta fram* nor *granska*. One skill now owns it, so it must route here every run.

This grader is the plugin-fired indicator, not a judgement on the answer. It fails
if no skill fired, and it fails if a different skill fired, even when the reply is
good. A good reply with no skill behind it is the base model answering, which is
what the ablation arm measures separately.
