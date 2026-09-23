# Changelog

Installed copies refresh on the plugin's version string. Anything that changes what a skill does
gets a version here.

## product-knowledge 0.5.1 (2026-09-23)

**`define-outcomes` checks an outcome in a new order and answers in plain words.** When you hand
it an outcome to review, it now asks first whose behaviour changes. If the people in the outcome
are your own staff, it asks which customer behaviour that serves. It then says whether the wording
describes one particular solution, and it asks what you know today before it asks for a baseline
or a time frame. The answer no longer names the four checks. It describes the biggest problem in
everyday words and ends with one question.

## product-knowledge 0.5.0 — 2026-09-16

**Breaking: `plan-interview` and `story-based-interviews` are gone.** They are replaced by one
skill, `customer-interviews`, which does everything both of them did. If you called either by
name, call `/product-knowledge:customer-interviews` instead. Nothing else about them survives,
and there is no compatibility shim.

Nothing is lost in the merge. The new skill teaches what story-based interviews are and why
discovery runs on them, plans a round from an outcome or an opportunity (research questions, the
opening story question, a follow-up cheat sheet, a coverage checklist), and reviews interview
questions one by one with rewrites. Each of those paths kept the procedure it had.

**Why they merged.** Claude picks a skill from names and descriptions alone, so two skills that
describe the same situation compete. These two split on *writing* interview questions against
*reviewing* them, which in Swedish came down to one verb: *ta fram intervjufrågor* against
*granska mina intervjufrågor*. Anyone asking for help with *intervjufrågorna* matched both and
got whichever won that turn. Merging removes the choice rather than trying to sharpen it.

If you ask for either half the way you always did, in Swedish or English, you land in the same
place. The difference is that you now land there reliably.

## product-knowledge 0.4.0

`clean-transcript` and `find-opportunities`.

## product-knowledge 0.3.0 and earlier

`what-is-product`, `define-outcomes`, `story-based-interviews`, `plan-interview`.
