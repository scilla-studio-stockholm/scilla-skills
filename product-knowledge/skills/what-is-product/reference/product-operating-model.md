---
title: The product operating model, a summary
author: Joni Lindgren, scilla.studio
---

# The product operating model

How a company funds, staffs, organizes itself, and decides what to build so that technology-powered products are the engine of the business rather than an IT-service function to it.

A set of first principles describing how the best technology-powered companies create products. The model shifts organizations from output-driven (features shipped on dates) to outcome-driven (customer and business problems solved). It contrasts with the IT model, project model, feature-team model, and sales-driven model that most companies default to.

This summary draws on the writing of Marty Cagan and the Silicon Valley Product Group (SVPG), on the other sources listed at the end, and on scilla.studio's own work with teams moving to the model.

## The Five Core Concepts

| Concept               | Focus                | Key question                                         |
| --------------------- | -------------------- | ---------------------------------------------------- |
| **Product Culture**   | Mindset & values     | What do we believe about how products are created?   |
| **Product Strategy**  | Direction & focus    | Which problems matter most right now?                |
| **Product Teams**     | People & structure   | Who solves the problems, and how are they organized? |
| **Product Discovery** | Validating solutions | How do we figure out what to build?                  |
| **Product Delivery**  | Building & releasing | How do we ship reliably and learn from what we ship? |

## Three Dimensions of Change

A company moving to the product model makes three shifts:

1. **How you decide which problems to solve** — Product leaders create a customer-centric vision and insight-driven strategy to identify critical problems aligned with business objectives
2. **How you solve those problems** — Teams receive problems, not feature lists; engineers, designers, and PMs collaboratively discover solutions that are valuable, usable, feasible, and viable
3. **How you build and deploy** — Small, frequent, uncoupled releases with instrumentation and monitoring to validate outcomes

## The 20 Product Model Principles

### Product Team Principles

| #   | Principle                            | Description                                                                                                                                   |
| --- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Empowered with Problems to Solve** | Teams receive problems and desired outcomes, not predetermined solutions. They have accountability for results and decision-making authority. |
| 2   | **Outcomes over Output**             | Focus on meaningful customer and business results rather than features shipped. Measured via OKRs tied to outcomes.                           |
| 3   | **Sense of Ownership**               | Teams own both discovery (identifying solutions) and delivery (building and releasing). Clear purpose and autonomy.                           |
| 4   | **Collaboration**                    | Cross-functional teamwork with psychological safety, respectful disagreement, diverse perspectives, and unified commitment after decisions.   |

### Product Strategy Principles

| #   | Principle               | Description                                                                                                                   |
| --- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 5   | **Focus**               | Strategic choices involve saying "no" to viable ideas. Deliberate trade-offs concentrate effort and amplify value.            |
| 6   | **Powered by Insights** | Strategy derives from data, customer conversations, enabling technology, and industry trends — discovered, not predetermined. |
| 7   | **Transparency**        | Share data, reasoning, and strategic rationale openly. Builds stakeholder trust and enables better autonomous team decisions. |
| 8   | **Placing Bets**        | Strategy involves risk. Assign problems to multiple teams to increase odds of meaningful progress. Accept uncertainty.        |

### Product Discovery Principles

| #   | Principle                         | Description                                                                                                                                         |
| --- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| 9   | **Minimize Waste**                | At least half of ideas won't work. Validate the fastest, cheapest way possible. Failure in discovery is valuable.                                   |
| 10  | **Assess Product Risks**          | Evaluate five risk categories early: value (customer benefit), usability, viability (business sustainability), feasibility (technical), and ethics. |
| 11  | **Embrace Rapid Experimentation** | Remove bureaucratic barriers. Test hypotheses quickly through prototypes and experiments. Fail fast.                                                |
| 12  | **Test Ideas Responsibly**        | Protect the company and customers — security, privacy, ethics, and compliance must be respected even in experiments.                                |

### Product Delivery Principles

| #   | Principle                               | Description                                                                                                       |
| --- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 13  | **Small, Frequent, Uncoupled Releases** | Release at minimum every two weeks, ideally continuously via CI/CD. Small batches improve both speed and quality. |
| 14  | **Instrumentation**                     | Build telemetry to observe how features are actually used and whether intended outcomes are achieved.             |
| 15  | **Monitoring**                          | Real-time observability across multiple levels. Detect problems before customers do.                              |
| 16  | **Deployment Infrastructure**           | Automate delivery pipelines. Support A/B testing, feature flags, and rapid rollback.                              |

### Product Culture Principles

| #   | Principle                          | Description                                                                                     |
| --- | ---------------------------------- | ----------------------------------------------------------------------------------------------- |
| 17  | **Principles over Process**        | Flexible principles over rigid processes when solutions are uncertain or evolving.              |
| 18  | **Trust over Control**             | Psychological safety. Teams speak openly without fear. Leaders coach rather than command.       |
| 19  | **Innovation over Predictability** | True innovation requires abandoning absolute predictability. Discovery is inherently uncertain. |
| 20  | **Learning over Failure**          | The only real failure is neglecting to extract lessons. Every experiment produces learning.     |

## Key Roles in the Product Model

| Role                     | Primary responsibility                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------ |
| **Product Manager**      | Value and viability — ensures the product solves a real problem and works for the business |
| **Product Designer**     | Usability — ensures users can figure out how to use the product                            |
| **Tech Lead / Engineer** | Feasibility — ensures the solution can be built and scaled                                 |
| **Product Leader**       | Coaching, staffing, and providing strategic context — not dictating solutions              |

The "product trio" (PM, designer, tech lead) works together daily on both discovery and delivery. This is the fundamental unit of the product model.

## Product Model vs. Feature Team Model

| Dimension                      | Feature Team                            | Empowered Product Team           |
| ------------------------------ | --------------------------------------- | -------------------------------- |
| Input                          | Features to build (roadmap)             | Problems to solve (outcomes)     |
| PM role                        | Facilitator / project manager           | Value and viability owner        |
| Value/viability responsibility | Stakeholder who requested the feature   | Product manager                  |
| Success metric                 | On-time delivery                        | Customer and business outcomes   |
| Discovery                      | Minimal or none                         | Continuous                       |
| Autonomy                       | Low — executes someone else's decisions | High — figures out best solution |

## The Transformation Approach

The path *Transformed* recommends:

1. **Leadership buy-in** — CEO must believe current ways of working won't drive future success
2. **Organizational assessment** — Understand current state honestly
3. **Start with pilot teams** — Select 1-2 teams, give them real problems, coach them through the product model
4. **Demonstrate results** — Pilot teams prove the model works in your context
5. **Expand gradually** — Scale to more teams as competencies and culture develop
6. **Expect years, not months** — Transformation changes funding models, decision-making, team structures, and culture

### Prerequisites for Pilot Teams

- A real, meaningful problem to solve (not a throwaway project)
- Cross-functional composition: PM, designer, engineers
- A product leader willing to coach rather than direct
- Air cover from leadership to work differently

## Common Anti-Patterns

| Anti-pattern                       | Why it fails                                                                  |
| ---------------------------------- | ----------------------------------------------------------------------------- |
| Feature-team theater               | Calling teams "empowered" while still handing them roadmaps                   |
| Discovery theater                  | Running discovery rituals without actually changing what gets built           |
| Agile without empowerment          | Sprints and standups but no authority to decide what to build                 |
| Transformation by process change   | Adopting frameworks (SAFe, Scrum) without changing culture or decision-making |
| "Let's do this everywhere at once" | Transformation needs demonstrated success before scaling                      |

## Connection to Other Frameworks

- **OST (Teresa Torres)**: The product model provides the organizational context; OST provides the tactical discovery technique. Cagan's "Product Discovery" concept maps directly to Torres' opportunity-solution tree work. Both emphasize continuous customer contact and experimentation.
- **OKRs**: The model uses OKRs as the mechanism for communicating outcomes to empowered teams. Product strategy translates into team-level OKRs.
- **Continuous Delivery (Forsgren/Humble)**: The four delivery principles directly align with the DORA metrics and Accelerate research on high-performing engineering teams.
- **Agile**: The product model builds on agile's values but argues most "agile" implementations miss the point — they optimize delivery mechanics without addressing discovery or empowerment.

## The three SVPG books

| Book          | Year                | Focus                                                 |
| ------------- | ------------------- | ----------------------------------------------------- |
| *Inspired*    | 2008 (2nd ed. 2017) | How product teams do discovery — the "what"           |
| *Empowered*   | 2020                | How product leaders create the conditions — the "who" |
| *Transformed* | 2024                | How organizations change to this model — the "how"    |

## Sources

- [The Product Operating Model — SVPG](https://www.svpg.com/the-product-operating-model/)
- [The Product Operating Model: An Introduction — SVPG](https://www.svpg.com/the-product-operating-model-an-introduction/)
- [Product Model Concepts — SVPG](https://www.svpg.com/product-model-concepts/)
- [Product vs. Feature Teams — SVPG](https://www.svpg.com/product-vs-feature-teams/)
- [Principles — SVPG](https://www.svpg.com/principles/)
- [Product Operating Model Principles — Life in Tech](https://www.lifeintech.com/2024/08/22/product-operating-model-principles/)
- [Product Model First Principles In Depth — Product Compass](https://www.productcompass.pm/p/product-model-first-principles-transformed-cagan)
- [The Product Operating Model Explained — Product Talk](https://www.producttalk.org/the-product-operating-model/)
- [Marty Cagan on the Product Operating Model — Age of Product](https://age-of-product.com/marty-cagan-product-operating-model/)
- [Transformed — Amazon](https://www.amazon.com/Transformed-Becoming-Product-Driven-Company-Silicon/dp/1119697336)
