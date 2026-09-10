---
title: Product Outcomes vs Business Outcomes
author: Joni Lindgren, scilla.studio
---

# Product Outcomes vs Business Outcomes

## Why does it matter?

When a team is given "increase revenue" as their goal, they have no clear direction. Revenue is affected by pricing, marketing, sales, churn, upsells, and a hundred other things. Product teams cannot directly control business results - but they can influence user behavior that drives those results.

The distinction between business outcomes and product outcomes is what gives a product team real agency.

## Business Outcome

A business outcome is a lagging metric that reflects how the business is performing. It answers: *"Is the company winning?"*

Examples:

- Revenue growth
- Customer churn rate
- Annual Revenue Per Account  (ARPA)
- Number of paying customers

Business outcomes are important for company strategy, but they are **too broad** for a product team to own. Too many variables are outside the team's control.

## Product Outcome

A product outcome is a **measurable change in user behavior** that the product team can directly influence, and that has a credible connection to a business outcome.

It answers: *"What are users doing differently because of what we built?"*

Examples:

- Percentage of new users who complete their first key action within 7 days
- Percentage of users who return at least 3 times per week
- Percentage of customers who invite a team member within 30 days
- Reduction in support tickets related to onboarding

## The relationship

```
Company Mission / Vision
        |
  Business Outcome        (lagging, broad, company-level)
        |
  Product Outcome          (leading, specific, team-level)
        |
  Opportunity Space        (customer needs, pains, desires)
        |
  Solutions & Experiments  (what we build and test)
```

A product outcome is the bridge between business strategy and daily product work. It gives the team a target they can actually move, while leadership retains confidence that moving it will matter for the business.

## Concrete examples

| Business Outcome              | Product Outcome                                         | Why the connection works                            |
| ----------------------------- | ------------------------------------------------------- | --------------------------------------------------- |
| Increase revenue              | More users complete their first purchase within 14 days | Users who buy early have 3x higher LTV              |
| Reduce churn                  | More users engage with core feature weekly              | Weekly active users churn at 1/5 the rate           |
| Grow market share             | More trial users reach "aha moment" before trial ends   | Users who experience value convert at higher rates  |
| Increase expansion revenue    | More users invite team members                          | Teams that collaborate upgrade to paid plans        |
| Improve customer satisfaction | Fewer users get stuck in onboarding                     | Onboarding friction is the #1 driver of early churn |

## From vague goal to product outcome - a worked example

**Starting point:** *"We want a positive experience for our customers - it should be easy to get started and to understand our licensing model."*

This is an **opportunity area**, not an outcome. To make it actionable:

### Step 1: Split it up

"Easy to get started" and "understand our licensing model" are two different things. Treat them separately.

### Step 2: Find the behavior

Ask: *What does a user who has successfully gotten started actually do? What does a user who understands the licensing model do differently from one who doesn't?*

| Vague goal                 | Possible product outcomes                                                                             |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| Easy to get started        | Percentage of new customers who complete [key action] within X days of purchase                       |
| Easy to get started        | Percentage of new customers who complete setup without contacting support                             |
| Understand licensing model | Percentage of customers who select the right license level from the start (no change within 3 months) |
| Understand licensing model | Reduction in support tickets related to licensing questions                                           |

### Step 3: Connect to business outcome

```
Business outcome:   Increased customer retention
        |
Product outcome:    More customers complete [key action]
                    within 14 days of purchase
        |
Opportunity:        "It's hard to get started"
        |
Discovery:          Why is it hard? Where do people get stuck?
```

### Step 4: Measure the baseline

Before setting a target, measure where you are today. Without a baseline, you cannot know if you are making progress.

## The test: Is it a good product outcome?

A well-formed product outcome passes all four checks:

| Check         | Question                                                                    |
| ------------- | --------------------------------------------------------------------------- |
| Measurable    | Can we track it with data we have (or can get)?                             |
| Behavioral    | Does it describe something users *do*, not something the business *earns*?  |
| Influenceable | Can this product team move this metric through product changes?             |
| Connected     | Is there a credible argument that improving this drives a business outcome? |

If it fails any of these, it needs reworking.

## Common mistakes

| Mistake                            | Example                       | Problem                                                            |
| ---------------------------------- | ----------------------------- | ------------------------------------------------------------------ |
| Disguised output                   | "Launch new onboarding flow"  | That's a solution, not an outcome                                  |
| Too broad                          | "Improve user experience"     | Not measurable, not specific                                       |
| Business metric as product outcome | "Increase revenue by 10%"     | Team can't directly control this                                   |
| Vanity metric                      | "Increase page views"         | Doesn't connect to real user value                                 |
| Missing the behavior               | "Users should feel it's easy" | Feelings aren't measurable - what do they *do* when it feels easy? |

## Sources

- Teresa Torres, *Continuous Discovery Habits* (2021)
- Teresa Torres, [Outcome-Based Roadmaps](https://www.producttalk.org/2014/04/drop-feature-based-product-roadmaps/)
- Josh Seiden, *Outcomes Over Output* (2019)
