[← Profile](../../README.md) · [All projects](../README.md)

![AMLGraph](../../assets/amlgraph.svg?v=20261007)

# AMLGraph

**Explainable transaction-network investigations**  
**Status:** planned; a portfolio simulation using synthetic data.

## The business question

A transaction alert is useful only if an analyst can understand why it was raised and decide what to review. How can transaction relationships help prioritise investigation while making false positives visible?

The intended product is a simulated investigation workspace. It demonstrates data engineering, graph analysis and explainability; it is not a production compliance system or a legal determination of money laundering.

## The intended user journey

An analyst opens an alert queue, selects an account and sees the relevant transaction neighbourhood. A timeline explains the signals, amounts and time windows behind the alert. The analyst can inspect supporting transactions and record a simulated review outcome.

## Professional features in scope

- **Reproducible synthetic generator:** seeded accounts and transactions, ordinary activity and deliberately injected patterns, with separate ground-truth labels.
- **A coherent data model:** customers, accounts, transactions and scenario metadata with keys, timestamps and validation rules.
- **Graph features:** transaction relationships, time-bounded cycles, fan-in / fan-out patterns and concentration measures.
- **Transparent baselines:** documented rules before more complex anomaly or graph-learning models.
- **Investigation context:** trace each alert to the transactions and features that triggered it.
- **Prioritisation:** make score components, ranking and threshold choices inspectable.
- **Analyst workflow:** queue filters, an investigation panel and recorded simulated dispositions.
- **Data engineering:** incremental processing, duplicate protection and useful failure logs.

## Proposed architecture

Python generates and validates synthetic data. SQL models expose transaction-level and account-level features. A graph layer computes relationships; the first release can use an in-memory graph library before a graph database is justified. An API and dashboard provide the investigation workflow.

Graph machine learning is an optional later comparison. Its inclusion depends on whether it improves evaluation over transparent rules and simpler models.

## Evaluation design

Split data by time and, where appropriate, by entities or scenarios to reduce leakage. Keep the generator's hidden labels out of model features. Evaluate multiple seeds and scenarios, including patterns different from those used to tune rules.

Report precision / recall and precision at a fixed review budget on the synthetic ground truth. Show alert volumes, missed scenarios and false positives. A score describes the project's prioritisation logic, not a calibrated probability of criminal activity. Results on synthetic data do not establish real-world effectiveness.

## Release evidence

- A repeatable dataset generation and validation run.
- A documented baseline and evaluation split.
- An alert investigation that exposes the supporting transactions.
- A false-positive example and an explanation of why the system flagged it.
- A small evaluation report showing the effect of threshold and review-budget choices.

**First release boundary:** synthetic data, transparent rules, graph investigation and a reproducible evaluation. Advanced graph learning follows only if it adds measurable value.
