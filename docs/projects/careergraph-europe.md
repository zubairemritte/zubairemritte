[← Profile](../../README.md) · [All projects](../README.md)

![CareerGraph Europe](../../assets/identity/careergraph-v02.svg)

# CareerGraph Europe

**Skills, with evidence.**  
**Status:** working local release 0.2. [Code, quickstart and full technical documentation](https://github.com/zubairemritte/careergraph-europe).

## The business question

Given a selected job-offer sample and a current skill set, which additional skill would complete the detected skill set of more offers?

The product connects labour-market analysis with data-quality controls and an explainable user decision. Each result is conditional on its source, country, role, publication window and extraction method.

## What the first release does

- Configures 16 European countries through an ISO country variable, independently of the source connector.
- Collects a bounded real offer sample through a verified public JobTech connector.
- Retrieves official Eurostat vacancy statistics as separate economic context.
- Validates records, removes conservative duplicates and retains dated collection audits.
- Extracts 24 curated skill labels with evidence snippets and versioned aliases.
- Calculates frequencies, co-occurrence relationships and additional coverage from one skill.
- Exposes the analysis through a read-only FastAPI service and an English browser interface.
- Provides a deterministic offline demonstration, eight small fixture checks and strict static type checking.
- Uses documented functions, typed data contracts, provider classes and Poetry with locked versions.

The interface uses explicit skill selection. CV parsing, semantic extraction and a hosted production service are not implemented.

## Coverage is part of the result

The product is designed for major European markets. A country variable selects one of 16 configured ISO alpha-2 codes independently of the provider.

Datasets are collected through authorised public APIs from established European employment services. Every source must have verified access, reuse terms and workplace coverage before activation. Official European statistics provide separate economic context.

Actual offer coverage currently comes from the verified JobTech connector for Swedish workplaces. Other countries remain visibly unconnected until their sources have been validated and implemented. A separately labelled synthetic demo exercises all 16 country filters.

Eurostat availability is tracked by country and quarter. The broad vacancy rate is not interpreted as a data-professional vacancy rate.

## An explainable calculation

If the selected skills are Python and SQL, an offer mentioning Python, SQL and dbt has one missing detected skill: dbt. Adding dbt completes that detected set. An offer still missing both Docker and AWS is not covered by adding only Docker.

The score counts additional offers in the observed sample. It is not a hiring probability, a judgement of competence or a causal estimate.

## Engineering choices

**Implemented:** Python, SQL, SQLite, FastAPI, browser-native HTML/CSS/JavaScript, Poetry, exact dependency versions, typed connector classes, automated checks and CI configuration. A Docker recipe is included; the release report records its verification status.

A successful run is committed atomically. Failed refreshes do not replace the last successful sample. Raw live offer bodies and personal preparation files are excluded from public GitHub content.

The [architecture decisions](https://github.com/zubairemritte/careergraph-europe/blob/main/docs/decisions.md) explain why the first release starts with a small reproducible system and an inspectable extraction baseline.

## Inspect the evidence

- [Run the project](https://github.com/zubairemritte/careergraph-europe/blob/main/docs/quickstart.md)
- [Read the formulas and limits](https://github.com/zubairemritte/careergraph-europe/blob/main/docs/methodology.md)
- [Check the source register](https://github.com/zubairemritte/careergraph-europe/blob/main/docs/sources.md)
- [Review executed checks and release limitations](https://github.com/zubairemritte/careergraph-europe/blob/main/docs/release-0.2.md)
