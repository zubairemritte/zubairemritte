[← Profile](../README.md) · [Version française](README.fr.md)

# Portfolio roadmap

Five independent data products, developed sequentially. This roadmap records **design intentions**, not completed capabilities. The public profile is the current deliverable; CareerGraph Europe's repository is initialized and its implementation comes next.

| Order | Product brief | Intended user | Decision supported | Current state |
| --- | --- | --- | --- | --- |
| 1 | [CareerGraph Europe](projects/careergraph-europe.md) | Candidate, recruiter, skills analyst | Which skills, roles and locations deserve attention? | Scoped; repository initialized |
| 2 | [LuxRisk Intelligence](projects/luxrisk-intelligence.md) | Economic or financial analyst | Which country indicators changed, and why? | Planned |
| 3 | [PricePulse AI](projects/pricepulse-ai.md) | Pricing or commercial analyst | Which price movements merit investigation or evaluation? | Planned |
| 4 | [AMLGraph](projects/amlgraph.md) | Financial crime analyst in a simulated setting | Which transaction patterns should be reviewed first? | Planned |
| 5 | [Data Platform Lab](projects/data-platform-lab.md) | Data engineer or platform owner | Can a pipeline be deployed, monitored and recovered reliably? | Planned |

## A common delivery standard

Each product should eventually be understandable at three levels: a short business explanation, a working demonstration and a technical review.

| Gate | Evidence required before describing it as complete |
| --- | --- |
| **Scope** | User, decision, data access, definitions and exclusions documented |
| **Data foundation** | Reproducible ingestion, provenance, schema and meaningful quality checks |
| **Analytical value** | A justified method, a baseline and an evaluation matched to the business question |
| **Demonstration** | A working user journey, with known limitations visible |
| **Engineering** | Reproducible environment, useful tests, CI and documented operating procedures |
| **Presentation** | Screenshots from actual runs, measured results, technical notes and an interview explanation |

We move to the next product once the current one has a demonstrable, documented release. Later enhancements stay in that product's backlog.

## Documentation planned for each project

- `README.md`: business value, actual status, screenshots, quick start and main links.
- `docs/business-case.md`: user, problem, decision and expected value.
- `docs/architecture.md` and `docs/adr/`: components and reasons for key decisions.
- `docs/data-model.md` and `docs/data-quality.md`: definitions, provenance and controls.
- `docs/methodology.md` and `docs/results.md`: method, evaluation, measured findings and limitations.
- `docs/deployment.md`: configuration, access requirements, costs to assess, monitoring and recovery.
- `docs/presentation.fr.md`: French learning guide, glossary and interview preparation.

## Evidence and scope

Business value will be supported by measured results, with the dataset and evaluation conditions stated. Synthetic examples will be labelled. A CV-to-market match score, for example, will describe skill coverage within the collected offers; it will not be presented as a hiring probability.

The initial **FinanceOps Control Tower** idea is recorded as a previous proposal. It is outside the current five-project sequence and has not been silently merged into LuxRisk, which addresses a different business problem.

Detailed data sources, service choices and access conditions will be verified during the relevant project's implementation. Technologies in the briefs are proposed components, not a requirement to use every tool regardless of need.
