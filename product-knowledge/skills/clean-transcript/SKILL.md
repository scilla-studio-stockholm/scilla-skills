---
name: clean-transcript
description: Use when someone has a raw interview or meeting transcript from Otter, Fireflies, Zoom, Rev, Grain, Supernormal, Teams or any recording tool and wants it cleaned before analysis. Triggers include "clean this transcript", "tidy up this interview", "remove the fillers and timestamps", "fix the speaker labels", "rensa den här transkriptionen", "städa upp intervjun", "fixa talarna". Also use to review speaker attribution in a transcript that is already clean. Claude does the cleaning in the reply; no script.
---

# Clean a transcript

Turn a raw transcript into a clean, speaker-labelled document that a team can read, quote from and analyse. The reply carries the cleaned transcript. Read `reference/format-patterns.md` for how each recording tool formats its output, `reference/output-template.md` for the shape of the result, and `reference/speaker-attribution-review.md` for the second pass.

## What the asker gives you

The raw transcript, pasted or as a file path, sometimes several at once. Optionally: who the speakers are and their roles, whether to keep timestamps, and which tool produced it. Ask for the speakers' roles if they are not given and the labels in the transcript do not say (Speaker 1, SPEAKER_2). One question, then proceed with what you have.

## What you do

1. Detect the source format from its markers (confidence percentages, VTT headers, inline timestamps, crosstalk markers). The reference lists them per tool.
2. Remove noise: filler words (um, uh, like, you know, sort of, alltså, liksom, typ), false starts and repeated words, timestamps unless asked to keep them, platform artefacts (confidence markers, VTT headers, auto-generated summary sections), and inaudible or crosstalk markers, replaced with [unclear] where a word is missing.
3. Normalise speakers. Consolidate inconsistent labels for the same person. Map labels to roles when the asker has given them (Interviewer, Participant, Observer). Otherwise keep the most consistent label in the transcript.
4. Structure the output: utterances grouped into paragraphs by speaker, speaker name in bold, the conversation in its original order, following the template. Section headings only where the conversation visibly changes topic, and never invented.
5. Keep the words. Cleaning removes noise and keeps meaning, phrasing and the speaker's own expressions, including grammatical slips that carry their voice. Never paraphrase, summarise, translate or complete a sentence. A quote taken from the cleaned transcript must still be something the speaker said.
6. Return the cleaned transcript in the reply, with a short metadata block (date, duration if known, source tool, participants). Several transcripts give several documents. Write to a file only when the asker names a path.

## Speaker attribution review

Automated transcription puts words in the wrong mouth: an "okay, thanks" that belongs to the next speaker stuck on the end of a turn, an interviewer's follow-up inside the participant's turn, a turn that starts mid-sentence. After cleaning, offer to review attribution. When asked, follow the reference: quote each suspect passage, say what is wrong, and give the corrected turns. Review long transcripts in sections.

## Options the asker can ask for

- Keep timestamps.
- Keep the fillers.
- Map named speakers to roles.
- Only the cleaned text, no metadata block.
- Plain text instead of markdown.

## How to answer

- Lead with the cleaned transcript, or with the one question you need answered first.
- No sentence that announces what follows. Not "Here is the cleaned transcript". Start with the document.
- Complete sentences in anything you write yourself. No dashes as separators; use a comma, a full stop or parentheses. The transcript's own words are exempt from every rule: they stay as spoken.
- No praise of the material, no closing recap.

## Language

The transcript stays in its own language. Reply in the language the asker writes in. Metadata labels and role names follow the asker's language.
