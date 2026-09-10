---
title: Product Foundations
source: scilla.studio method, in use since roughly 2022
author: Joni Lindgren, scilla.studio
---

# Product Foundations

Product Foundations describes one specific product in four statements: what the product is, what it does, who uses it, and who it is for.

It is level 1 of the scilla.studio product canvas. The four levels above it (customer journey, growth loops, monetization, product growth metrics) all get fuzzy while the room still disagrees about what the product is.

A separate note covers what the word "product" means inside a product operating model. This doc is about writing down one company's actual product.

## The same four statements do two jobs

### When the product is still an idea

The four statements are the product hypothesis, before anything has validated it. This is the product. These are its functions. These are the people who will use it. And these are the ones whose pain it solves well enough that they keep paying. Product/market fit work is observing whether that holds.

A team that has not written the four parts down has nothing to observe against. It then constructs a product outcome after the fact to satisfy a reporting need, instead of measuring against something it committed to in advance. The tell is that writing the outcome feels unreasonably hard. That difficulty is a signal about the missing hypothesis, not about the product leader's skill.

### When the product is already built

The four statements are the source of truth for what the product currently is. They change when discovery teaches the company something new, as a deliberate edit that someone can point at.

Two uses recur. A new joiner reads one page and understands the product without a tour. A team that has started pulling in several directions reads the same page and sees where it left off.

## The four statements

The examples follow one fictional product, Tempo, an auto-time-tracker for software teams. 

### 1.1 Product definition

Describe the product in 1 to 2 sentences so that more or less anyone could grasp what it is.

Strip it to its most basic version. Describe the product from first principles. No marketing or positioning language, no internal jargon, no future capability written as though it already exists.

- **Done when** someone outside the company understands the product from those two sentences alone, and the room agrees they are true today.
- **Fails when** the sentences describe an ambition, or when they are technically accurate and unreadable.

> Tempo is an auto-time-tracker for software teams. It logs work across GitHub, Linear and Slack in the background, so engineers do not have to remember to start and stop timers.

### 1.2 Core functionality

What are the core features or functionality that make the product what it is?

A bullet list of everything that makes the product definition true. Typically 5 to 10 items, no explanations. The skill is picking the level of abstraction: concrete enough to mean something, high level enough that the list stays readable and describes this product rather than the whole category.

- **Done when** the list, read on its own, makes 1.1 believable.
- **Fails when** it turns into a backlog, or into three items so abstract they would fit any competitor.

> 1) Connects tools (GitHub, Linear, Slack). 2) Reviews auto-logged time in a weekly report. 3) Tags time to projects and clients. 4) Exports a timesheet to QuickBooks. 5) Shares the week with the team lead.

### 1.3 User groups

What distinct types of users interact with the product in fundamentally different ways?

A user group has its own access, its own role and its own job, so in practice it experiences a different product. Segments of one user type do not count. Many products have exactly one group. A marketplace always has at least a buyer and a seller. A SaaS product often has end users and admins. Name each group and its job.

- **Done when** each group would describe the product differently if asked, and every group named is one the product serves today.
- **Fails when** demographic or commercial segments get listed instead, or when a group is named because it is wanted rather than because it exists.

> Engineers (passively capture their own time). Team leads (review and approve the team's week). Finance (export client-billable hours to invoicing).

### 1.4 Ideal customer profile

Who is the ideal customer?

The characteristics shared by the customers who would be glad they bought this. For B2B: firmographics, tooling, team shape, and the pain that makes them urgent. For B2C: demographics, context, behaviour, and the same urgency.

It is a list of characteristics, not a persona. It describes the organisations or people who benefit from what 1.1 to 1.3 just described. Who signs the contract is a separate question, answered further up the canvas.

When the list has to be derived rather than asserted, win/loss analysis across won, lost and churned accounts is the usual way in.

- **Done when** a salesperson could disqualify a prospect using the list.
- **Fails when** it is a buyer persona, or when it stays empty because nobody has decided.

> 10 to 80-person software agencies that bill hourly, use GitHub and Linear, and currently lose 10 to 15% of billable hours because engineers forget to log time in Toggl or Harvest.

## Jobs to be done sits upstream of 1.1

A job statement is solution-agnostic by definition, written as verb plus object plus context, and naming a solution disqualifies it. 1.1 opens by naming the solution, so the two cannot be the same sentence.

For Tempo the job reads something like "log billable time accurately without interrupting deep work". It stays true if Tempo shuts down tomorrow. 1.1 describes the thing built to win that job, and it dies with the product.

Run the job first. It gives 1.1 a check: when nobody can say what the product gets hired for, 1.1 tends to come out as a feature list or as an ambition, which are the two failure modes listed above. The job also reaches past this exercise. It starts the chain from job to business goal to product outcome, the same chain that stalls when the four statements are missing.

Two reasons the job sits in front of section 1 rather than inside it. Asked after 1.1, a room tends to retrofit a job that justifies what it already built. And 1.1 to 1.4 are all answerable from inside the building, so a team can complete section 1 without ever discovering that the product solves no problem for anyone. The job is the one question the room cannot settle by agreeing, because the answer lives with customers.

## Running it

Around two hours, facilitated, with the people in the room who can commit to the answers. That usually means the product team plus whoever holds the strategy. The facilitator writes what the room says and reads it back.

The rules that do most of the work:

- Plain language throughout. No marketing phrasing, and no internal shorthand a newcomer would not follow.
- Where a bullet list is asked for, write a bullet list.
- Write what is true today. Anything aspirational goes somewhere else.
- Read 1.1 out loud to someone who was not in the room before calling it finished.

The output is one page. Agreement in the room matters more than the wording, and the wording can be tidied afterwards without a meeting.

## What the exercise surfaces

Most of the value shows up while the statements are being written.

- Disagreement in the room is the finding. When a team cannot land 1.1, the wording is rarely the obstacle.
- Teams that keep dressing up 1.1 often do not trust what the product is today. In one founding team that had never been said out loud between them until the exercise forced the sentence.
- A weak job in 1.1 can explain a team pulling in several directions. Running in several directions feels like large work. Writing the small true version does not.
- Sales closing deals that need customisation is a signal that 1.1 was never really agreed, since each customisation tests a different product.
- An empty 1.4 blocks the outcome work downstream. The team knows who signs the contract and has never written down which organisations it means, so there is nothing to measure adoption against.

Three reactions from client sessions, rendered from the Swedish:

> "This is the best thing we have ever done. Why have we not had something like this before?"

> "I would have needed this when I started." (a marketer on the same team)

> "Now I understand what we are actually building." (a developer in a third team)

## Naming

Formalised around 2022 as the PLG canvas, then renamed. Product-led growth is one of the things a company can attempt once these four statements hold, and the statements are worth having whether or not PLG is ever on the table. The wider five-level artifact has been called the product canvas since. "Product Foundations" names level 1.
