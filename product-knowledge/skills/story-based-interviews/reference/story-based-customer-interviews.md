---
title: Story-Based Customer Interviews
author: Joni Lindgren, scilla.studio
---

# Story-Based Customer Interviews

A story-based customer interview is a research technique where you ask customers to share specific stories about past behavior rather than opinions, preferences or predictions about the future. The story (a concrete, situated account of something that actually happened) is the unit of data.

The technique appears under different names across practitioners but the core principle is the same: people are unreliable narrators of their own behavior when asked directly, but become much more accurate when asked to reconstruct a specific past event.

## Why stories instead of direct questions

Humans are poor at accurately summarizing their own behavior. When asked general questions ("What do you look for in a product?"), people present idealized versions of themselves. When asked about the future ("Would you use this?"), they answer based on what they think they should do rather than what they actually do.

> "We don't want to build our products based on what people aspire to do. We want to build our products based on what people actually do."
> Teresa Torres, [Ask Teresa: What Are the Best Customer Interview Questions?](https://www.producttalk.org/2022/04/best-customer-interview-questions/)

Rob Fitzpatrick makes the same point: asking someone "Would you buy a product that does X?" produces worthless data because people lie, not maliciously, but because they want to be supportive and don't understand their own behavior well enough to predict it.

> "It's possible to ask the questions in the wrong way and then the data you get back is corrupted - it's worse than worthless."
> Rob Fitzpatrick, *The Mom Test* (2013)

Story-based questions force what psychologists call System 2 thinking (slow, deliberate recall of concrete events) instead of System 1 fast gut responses. You can't fabricate a detailed past story as easily as you can say "yeah, I'd totally use that."

## How it differs from other interview approaches

| Dimension | Opinion-based interview | Story-based interview |
|---|---|---|
| Core question | "What do you think about...?" | "Tell me about the last time you..." |
| Time orientation | Present opinions or future predictions | Past behavior, what actually happened |
| What you learn | What people say they want | What people actually do and why they struggle |
| Risk | Aspirational answers, social desirability bias | Grounded in real events |
| Data quality | Stated preference (unreliable) | Revealed preference (reliable) |

Story-based interviewing also differs from usability testing and solution validation. It is a problem space technique: the goal is to understand opportunities, needs and context, not to evaluate a specific solution. Torres is explicit on this point: interviews are for understanding the problem space; use assumption tests for evaluating solutions.

## The opening question

The master prompt across all practitioners is some variation of:

**"Tell me about the last time you [did the thing relevant to your research question]."**

Examples:
- "Tell me about the last time you had to compile a consultation list for a permit process."
- "Tell me about the last time you needed property data for a client delivery."
- "Tell me about the last time you switched from one tool to another for this task."

Scope the opening to your product outcome or research question. If your outcome is about a specific use case, ask about that use case rather than broadly.

Torres recommends one opening question per interview rather than a long discussion guide. The story itself generates the follow-ups.

> Source: Teresa Torres, [Story-Based Customer Interviews Uncover Much-Needed Context](https://www.producttalk.org/2024/04/story-based-customer-interviews/)

## Follow-up questions

Once the story starts, your job is to fill in the gaps. Good follow-ups stay inside the story:

**Temporal:**
- "What happened first?"
- "Then what happened?"
- "How long had you been dealing with that before you decided to act?"

**Contextual:**
- "Where were you when that happened?"
- "Who else was involved?"
- "Show me the tool / email / document you used."

**Emotional:**
- "What was frustrating about that?"
- "Was there a moment where you almost gave up? Tell me about that."

**Motivational (from Fitzpatrick):**
- "What else have you tried?"
- "How are you dealing with it now?"
- "Why do you bother?" (to understand their goals)
- "What are the implications of that?" (to separate real problems from annoyances)

Bob Moesta adds a specific technique: when someone skips ahead or gives a vague summary, slow them down. "Wait, slow down. What happened between X and Y?" or "Nobody just decides. Take me back to when you first thought about it."

> Source: Bob Moesta, *Demand-Side Sales 101* (2020)

Torres also recommends reflection over rapid questioning: paraphrasing what you heard to encourage elaboration rather than firing the next question.

> Source: Teresa Torres, [Customer Interviews: How to Recruit, What to Ask, and How to Synthesize](https://www.producttalk.org/2022/12/customer-interviews/)

## Bad question types

### 1. Opinion and preference questions

- "What features do you look for in a tool like this?"
- "Do you think it's a good idea?"
- "What do you like about your current solution?"

These invite the participant's "best self" rather than their real behavior. Someone asked what they watch on TV will mention documentaries and leave out reality TV (Torres).

### 2. Hypothetical and future questions

- "Would you use a product that does X?"
- "How much would you pay for X?"
- "Would this be valuable to you?"

People cannot predict their own future behavior. Fitzpatrick: "Future me doesn't even want to see the friends on Saturday that I agreed to see on Friday."

### 3. Self-summary questions

- "How often do you do X?"
- "How many times a week do you typically...?"
- "What's your usual workflow?"

The word "typically" is a red flag (Torres). It asks people to summarize behavior they don't actually track. Instead, ask about the last specific time.

### 4. Leading and closed questions

- "Don't you find it frustrating when...?"
- "Do you use X?" (yields yes/no)
- "Is the current process slow?"

These either telegraph the answer you want or generate limited responses that kill elaboration.

### 5. "Why" questions (use with caution)

- "Why did you choose that tool?"
- "Why do you do it that way?"

Moesta avoids "why" questions entirely because they trigger post-hoc rationalization rather than concrete recall. Instead he asks "when", "where", "who was there", "what happened next." Fitzpatrick uses "why" selectively ("Why do you bother?") but anchors it to specific past events.

### 6. Solution pitching disguised as questions

- "What would you think if we built [specific solution]?"
- "Here's our prototype, what do you think?"

Once you start talking about your idea, they stop talking about their problems (Fitzpatrick). Solution validation belongs in separate assumption tests, not in story-based interviews (Torres).

## Three types of bad data to watch for

Fitzpatrick identifies three categories of unreliable data that show up when questions aren't story-based:

1. **Compliments**: "That sounds really useful!" Deflect and return to specifics.
2. **Fluff**: Generic claims ("I usually..."), future promises ("I would definitely..."), hypothetical maybes ("I might..."). Future promises are the deadliest form.
3. **Ideas**: Feature requests and suggestions. Not bad in themselves, but dig into the underlying problem rather than accepting the proposed solution.

> Source: Rob Fitzpatrick, *The Mom Test* (2013)

## Listening framework: Four forces of progress

Bob Moesta's JTBD framework provides a useful listening model for story-based interviews. When someone tells you about switching from one solution to another, four forces were at play:

1. **Push**: Frustration with the current situation ("I was tired of manually compiling lists")
2. **Pull**: Attraction to something better ("I heard that tool could automate it")
3. **Anxiety**: Fear of the new ("What if I lose data in the migration?")
4. **Habit**: Comfort with the status quo ("I'd been doing it this way for years")

A switch happens when push + pull overcome anxiety + habit. Most companies only work on pull (better features). They neglect reducing anxiety and breaking habits, which are often the real blockers.

> Source: Bob Moesta, *Demand-Side Sales 101* (2020); also covered in Clayton Christensen et al., *Competing Against Luck* (2016)

## Sources

### Books

- Teresa Torres, *Continuous Discovery Habits* (2021). Chapter on customer interviewing covers story-based approach
- Rob Fitzpatrick, *The Mom Test* (2013). Three rules for customer conversations
- Bob Moesta, *Demand-Side Sales 101* (2020). Timeline interview technique and four forces
- Clayton Christensen, Taddy Hall, Karen Dillon, David Duncan, *Competing Against Luck* (2016). JTBD theory
- Alan Klement, *When Coffee and Kale Compete* (2018, free online). Demand-side thinking and forces model

### Articles and blog posts

- Teresa Torres, [Ask Teresa: What Are the Best Customer Interview Questions?](https://www.producttalk.org/2022/04/best-customer-interview-questions/)
- Teresa Torres, [Story-Based Customer Interviews Uncover Much-Needed Context](https://www.producttalk.org/2024/04/story-based-customer-interviews/)
- Teresa Torres, [Customer Interviews: How to Recruit, What to Ask, and How to Synthesize](https://www.producttalk.org/2022/12/customer-interviews/)
- Teresa Torres on Lenny's Podcast, [How to Interview Customers](https://www.lennysnewsletter.com/p/teresa-torres-on-how-to-interview)
