[← Profile](../../README.md) · [All projects](../README.md)

![Data Platform Lab](../../assets/identity/platform.svg)

# Data Platform Lab

**Reproducible cloud data infrastructure**  
**Status:** planned. The project will demonstrate platform behaviour through a small, fully documented workload.

## The business question

A successful pipeline run is only the beginning. Can another engineer deploy it, understand the data, diagnose a failed load, replay a period and retire the infrastructure without losing control of costs?

The intended users are data engineers and platform owners. The business value is dependable delivery of defined analytical tables with traceable operations.

## Professional features in scope

- **Versioned infrastructure:** Terraform configuration, explicit variables and separated environments.
- **Raw and analytical layers:** a documented path from source records to staging, core models and business-facing marts.
- **Orchestration:** dependencies, retries, timeout behaviour, scheduled runs and controlled backfills.
- **Idempotence:** rerunning a period should not silently duplicate records.
- **Quality contracts:** schema, uniqueness, completeness, reconciliation and freshness checks appropriate to the workload.
- **Metadata and lineage:** describe source ownership, transformations and the relationships between published tables.
- **CI:** reviewable checks for code, transformations and infrastructure configuration.
- **Observability:** structured logs, execution state, data freshness and actionable failure information.
- **Operations:** setup, recovery, access management, cost monitoring and teardown instructions.

## Proposed architecture

An AWS implementation is the target: S3 for raw storage, a warehouse such as Redshift, dbt for transformations and Airflow for orchestration. A catalogue such as OpenMetadata is a possible extension, depending on operational cost and complexity.

A local development path will make the core transformations and tests reproducible. Cloud-specific behaviour will be validated separately; passing a local run will not be described as proof of a successful cloud deployment.

## A demonstrable workload

Use a small public dataset with clear reuse terms, or a labelled synthetic operational dataset. Keep the domain simple enough that the review can focus on platform reliability.

Include a normal batch, a duplicate batch, a late-arriving record and a deliberate schema error. These scenarios make reruns, quality gates and recovery behaviour inspectable.

## Evaluation and release evidence

| Scenario | Evidence to produce |
| --- | --- |
| Fresh setup | Documented infrastructure plan and successful deployment in an authorised account |
| Normal load | Source-to-mart counts, useful quality checks and traceable run metadata |
| Duplicate / replay | Demonstrated idempotence or a clearly documented replacement policy |
| Bad input | A visible, actionable failure without silently publishing invalid tables |
| Recovery | A documented correction and successful replay |
| Cost control | Resource inventory, assessed costs, budget settings and verified teardown steps |

The deployment budget and access requirements will be agreed before provisioning. Secrets will be supplied through appropriate environment or secret-management configuration, not committed to the repository.

**First release boundary:** one complete workload with reproducible transformations, quality gates and a recovery demonstration. Larger-scale claims require separate measurement.
