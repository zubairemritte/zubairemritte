[← Profile](../../README.md) · [All projects](../README.md)

![PricePulse AI](../../assets/identity/pricepulse.svg)

# PricePulse AI

**Retail pricing intelligence & causal machine learning**  
**Status:** planned. This independent portfolio product builds on methods relevant to my pricing experience; it will use separately sourced or explicitly synthetic data.

## The business question

A pricing analyst needs to understand whether a price movement is unusual, how a product compares with relevant alternatives and whether a pricing intervention changed demand. These are different questions and require different evidence.

## A product built in two evidence-based stages

### 1. Price intelligence

Candidate public price observations, such as Open Prices, can support product / location comparisons, normalised unit prices, promotion signals, historical trends and anomaly investigation. Coverage, licence and refresh behaviour must be verified before choosing the source.

This stage will preserve product identity, package size, currency, location and observation date. Comparisons will avoid treating different quantities or periods as equivalent.

### 2. Demand and causal analysis

Demand forecasting, elasticity estimation and causal evaluation require **sales or demand information**, plus relevant covariates and an appropriate design. Price observations alone are insufficient.

This stage therefore depends on finding a suitable licensed sales dataset, or creating a clearly labelled simulation for controlled experiments. It will not use confidential Carrefour data. If the evidence cannot support a causal claim, the output will remain descriptive or predictive.

## Professional features in scope

- Product identity and unit-price normalisation, with data-quality checks.
- Comparable peer groups and an investigation view for unusual price changes.
- Forecast baselines and time-based evaluation, with leakage checks.
- Causal analysis with explicit assumptions, control selection, placebo checks and sensitivity analysis when the data supports it.
- Scenario exploration with documented constraints, rather than an unexplained “optimal price”.
- Experiment tracking and versioned model artefacts; MLflow is a proposed component.
- A prediction API and dashboard, with input validation and model / data version information.
- Monitoring of input drift and, when outcome labels arrive, predictive performance.

## Proposed architecture

Python / SQL pipelines feed a warehouse such as BigQuery. Separate modules handle price comparisons, predictive modelling and causal studies. FastAPI exposes validated model outputs, while a dashboard supports business investigation. Docker and CI will make the execution path reproducible.

The technical scope will be matched to the available data. No forecasting or optimisation component will be added solely to make the stack longer.

## Evaluation and release evidence

| Question | Evidence to produce |
| --- | --- |
| Is the comparison valid? | Product, quantity, currency and period checks; a reviewed sample of comparisons |
| Is the forecast useful? | Time-based holdout results against a simple baseline, reported by relevant segments |
| Is there support for a causal effect? | Identification assumptions, diagnostics, placebo / robustness checks and uncertainty |
| Does monitoring help? | A documented simulation of a change, with alert behaviour and known blind spots |
| Is the product usable? | A repeatable pricing investigation from source data to a documented finding |

**First release boundary:** a reliable price-intelligence workflow. Demand modelling and causal evaluation are subsequent releases gated by data suitability.
