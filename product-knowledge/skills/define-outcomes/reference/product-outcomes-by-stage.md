---
title: Product outcomes by stage
author: Joni Lindgren, scilla.studio
---

# Product outcomes by stage

A product outcome is a measurable behaviour change in users that the team can influence and that has a credible link to a business result. See the product outcomes versus business outcomes reference for the full walkthrough of the difference between business outcomes and product outcomes.

This guide helps teams formulate product outcomes whatever their state of knowledge, from a completely new problem area to a well-established product.

## Template: specific product outcome

> Achieve/Increase/Reduce [specific behaviour change] from [baseline] to [target] within [time frame] (in order to achieve [business value].)

### Four parameters make up a product outcome

**1. Behaviour change rather than capability**

Describe what should change in the user's behaviour rather than what the product should be able to do.

- Good: "Reduce manual handling of customer cases by 50 % by October 2026"
- Bad: "Introduce automation to handle customer cases"

**2. Measurable with baseline and target**

State concrete values. If you do not know the baseline: write that. Then finding it out is part of your discovery.

Avoid fluffy words like "easy", "efficient", "secure", "enable". They are proxies for things that can actually be measured.

- Good: "Increase monthly active users (aged 18 to 35) from 12,000 to 15,000 by Q4 2026"
- Bad: "Enable the customer to find information"

**3. Time frame**

Use a concrete time frame. Without one there is no urgency, and it is hard to judge the ambition of the effort. Is it optimisation or innovation that is required, and is the time span reasonable in relation to that?

- Good: "Reach 60 % 7-day retention in the SMB segment by Q3 2025"
- Bad: "Improve activation during the year"

**4. Bonus: link to the overarching business goal**

It is perfectly fine to spell out which business goal or goals a product outcome is able to influence. It is usually implicit, but clarity rarely hurts.

## Common pitfalls

| Wording                                                        | Problem                                                                                    |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| "Launch a new onboarding flow so that more people get started" | Solution phrased as a goal                                                                 |
| "Improve the user experience"                                  | Not measurable                                                                             |
| "Increase revenue by 10 %"                                     | Too broad. Affected by factors outside the team's control                                  |
| "Increase page views"                                          | Output disguised as behaviour. Page views in themselves probably have no value             |
| "Users should feel that it is easy"                            | Not measurable. What does the user do that tells us it is easy?                            |
| "Enable the customer to find information"                      | The team has distanced itself from the result. Rephrase so that the team owns what happens |
| Several goals in the same wording                              | Impossible to focus on or follow up. Pick one                                              |
| Missing baseline or time frame                                 | No way to know whether you are making progress                                             |

## Self-test: can the team formulate a specific product outcome?

Not all teams are in the same place in their development phases. Specific outcomes help teams where a lot is known. Specific product outcomes fit if the team can answer yes to these statements:

| Statement                                                                                                | Answer |
| -------------------------------------------------------------------------------------------------------- | ------ |
| The team agrees on and understands the market's problem                                                  |        |
| The team knows who has the problem                                                                       |        |
| The team understands the segment's current behaviour well enough to identify where the change can happen |        |
| The team has a product that can at least partly address the problem                                      |        |
| The team has, or can establish, a measurable baseline for the behaviour                                  |        |

**Yes to all:** formulate a specific product outcome with the template above.

**No to one or more:** the first discovery needs to answer what is unknown. Use directional outcomes and hypothesis formulation instead.

## Why the self-test exists: the outcome is downstream of the hypothesis

A product outcome is a compression of a hypothesis. If the hypothesis was never written there is nothing to
compress, and the outcome work becomes construction instead of observation. A team in that position often
describes the problem as being bad at formulating outcomes, when what is missing sits one step up.

### The hypothesis takes its shape from what is being validated

There is no single template for the hypothesis. The scope of the hypothesis follows the scope of what is to
be validated, and the two common modes look different.

**The whole product against a market.** When the question is whether the product has a market at all, the
hypothesis needs four parts:

- the product and the features in it
- who is going to use it
- which pain point it solves for them
- whether they are willing to pay on a recurring basis

That is a starting point for validating product-market fit for a specific product against a specific market.
If any of the parts is missing, a specific outcome cannot be written.

**One step in a user journey.** When the product already exists and the question concerns a bounded part of
the journey, the hypothesis is instead the specific idea about how that particular step is solved. The four
parts are not needed, because product, users and willingness to pay are already known. What is to be
validated is the idea.

### The rule that ties them together

**An outcome can only be as specific as the hypothesis above it.** A vague "we think there is something
here" carries a directional outcome. A written hypothesis with product, users, pain point and willingness to
pay carries a specific outcome with baseline and target. An outcome that is more specific than its
hypothesis becomes a number with nothing behind it.

### The control question: what job is the outcome doing for the team?

When the outcome work drags on, the question to ask is: does this goal help the team do the discovery that
needs doing, or does it take time without steering anything? An outcome that eats time without steering
discovery has stopped doing a job for the team. Then the hypothesis is what should be written first.

## Directional outcomes: when specific outcomes are not applicable yet

For teams working on a completely new problem area, an unknown user journey or a new bet, specific product outcomes are hard to use. The team does not know enough yet for such a goal to be useful. Outcomes that point out a direction work better then, together with a hypothesis about the opportunity area.

### Examples of outcome wordings that fit different stages

| Type                                      | Description                                                                                                                                                  | Example                                                                                                                                                                                                          | Move on when...                                          |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Observation window without an outcome** | A hypothesis, the behaviour you believe exists, a time limit and a predetermined decision if the behaviour does not appear. No baseline, no target, no share. | "We believe engineering leads who have got value from Tempo's logs will ask to turn them into a client-billable timesheet. If we do not see that at any customer before Q4, we rethink the approach."             | The behaviour has been observed in someone               |
| **Directional outcome**                   | Shows direction without baseline or target. Specific enough to bound which opportunities the team explores                                                  | "Engineering teams that need to bill clients for their hours produce the timesheet from Tempo instead of through their current ways of working"                                                                  | The team has enough conviction to formulate a hypothesis |
| **Hypothesis with signals**               | Makes clear what the team believes and which evidence confirms or refutes it                                                                                 | "We believe engineering leads who bill clients spend significant time compiling hours by hand. We believe that if Tempo solves that, they start using the product for a new purpose and are willing to pay more" | The team can measure the behaviour                       |
| **Specific product outcome**              | Measurable behaviour with baseline, target and time frame                                                                                                    | "Increase the share of customers who produce their client timesheets from Tempo from 0 to 15 % by Q4 2026"                                                                                                       | Ongoing refinement                                       |

### Observation window without an outcome

At the bottom is the mode where not even a directional outcome can be set, because the behaviour that would
be measured does not exist in anyone yet. What remains is to describe the behaviour you believe in, set a
time limit and decide in advance what happens if you do not see it.

The predetermined decision point is what separates this mode from an evasion. Without it, "we wait and
see" becomes a position that can be held for any length of time.

### Directional outcome

A directional outcome answers: "Which area of customer behaviour do we believe matters?" It does not need a baseline or target yet. It needs to be specific enough to rule things out. Its purpose is for the team to do discovery and learn enough to decide on the next step, when too many parameters are unknown to begin with.

- Good: "Engineering teams use Tempo to produce client-billable timesheets instead of filling in hours by hand"
- Too vague: "Make the product more valuable"

### Moving on to a specific product outcome

When the team has validated that the problem exists and has a reasonable theory about which behaviour matters, they can set a specific outcome with baseline, target and time frame, following the template at the start of this document.

## Negotiating outcomes with leadership

Torres: setting a team's outcome should be the result of a two-way negotiation between the product leader and the product trio. The leader has an overview of the whole business. The trio has customer and technical knowledge.

In practice:

- Leadership sets the business outcome and strategic direction ("We want to raise ARPA for Tempo")
- Leadership can suggest an opportunity area ("We believe client-billable timesheets can drive this")
- The trio owns the product outcome wording and the discovery work
- The trio reports back what they learn, which can change the direction

## Sources

- Joni Lindgren, scilla.studio: template, pitfalls, self-test, practical examples, plus the
  hypothesis taking its shape from the scope of validation and the observation window as the lowest mode
- Teresa Torres, "How Continuous Discovery Works (and Doesn't) in Early-Stage Startups" (2022)
- Teresa Torres, "Empower Product Teams with Product Outcomes, Not Business Outcomes" (2020)
- Teresa Torres, "Defining Product Outcomes: The 8 Most Common Mistakes" (2022)
- Josh Seiden, Outcomes Over Output (2019)
- Josh Seiden, "Getting Started With Outcomes"
- Jeff Gothelf and Josh Seiden, Lean UX (3rd edition)
- Marty Cagan, "Outcomes Are Hard" (SVPG)
- Melissa Perri, Escaping the Build Trap (2018)
