---
with-only: true
tool_used: Skill
---

# Routing

The session invoked the skill `product-knowledge:define-outcomes`.

The artifact is a written outcome, not an interview question. The word *outcome* appears in the interview skill's description too, which is what makes this a boundary worth testing.

This grader is the plugin-fired indicator, not a judgement on the answer. It fails
if no skill fired, and it fails if a different skill fired, even when the reply is
good. A good reply with no skill behind it is the base model answering, which is
what the ablation arm measures separately.
