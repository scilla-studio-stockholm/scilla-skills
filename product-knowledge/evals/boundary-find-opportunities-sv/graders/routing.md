---
with-only: true
tool_used: Skill
---

# Routing

The session invoked the skill `product-knowledge:find-opportunities`.

Interviews are done and cleaned transcripts are in hand. The work is downstream of interviewing, so the interview skill must NOT fire.

This grader is the plugin-fired indicator, not a judgement on the answer. It fails
if no skill fired, and it fails if a different skill fired, even when the reply is
good. A good reply with no skill behind it is the base model answering, which is
what the ablation arm measures separately.
