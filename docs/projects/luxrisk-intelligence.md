[← Profile](../../README.md) · [All projects](../README.md)

![LuxRisk Intelligence](../../assets/luxrisk.svg)

# LuxRisk Intelligence

**Macroeconomic & financial indicators**  
**Status:** planned; product scope and evaluation design available below.

## The business question

Economic and financial analysts need to compare countries and explain changes using indicators that may arrive at different frequencies, use different units and be revised after publication. Which movements are material, and how reliable is the comparison?

The intended product is an analytical workspace for **traceable indicators and transparent scenarios**. It will connect my economics and statistics background with Python, SQL and BI.

## The intended user journey

An analyst selects a country and period, inspects a small set of economic indicators, compares peers and opens a source panel showing the unit, frequency, observation date and ingestion time. An anomaly or forecast can be investigated alongside the underlying series and the model's assumptions.

## Professional features in scope

- **Indicator catalogue:** definitions, source identifiers, units, frequency, geographic coverage and revision information where available.
- **Repeatable ingestion:** source adapters, validation, incremental loads and preserved raw responses.
- **Comparable analytical tables:** explicit unit conversions and frequency alignment; missing observations remain visible.
- **Country comparison:** peer groups and documented transformations such as annual change or standardised values.
- **Anomaly investigation:** show the observed value, expected range and explanation of the rule or model that raised the signal.
- **Forecasting:** compare a simple baseline with more complex methods using time-ordered evaluation.
- **Scenario explorer:** transparent user-selected assumptions and sensitivity analysis, clearly distinguished from forecasts.
- **Power BI reporting:** indicator drill-down, source traceability, data freshness and an exportable analytical summary.

## Proposed architecture and data

Candidate sources include the ECB, Eurostat and the World Bank. Specific series, API access, redistribution terms and publication frequencies will be checked during scoping.

Python ingestion feeds raw storage and a SQL warehouse; dbt is proposed for tested transformations. Power BI provides the analytical interface. Python supports forecasting and anomaly detection where the available history justifies them.

## Analytical controls

Country comparisons must respect differences in units, periods and definitions. Growth rates and levels will be labelled separately. Where historical data vintages are unavailable, backtests will explicitly state that limitation rather than claim a fully point-in-time simulation.

Any composite indicator will expose its components and weights. It will be labelled as a project-defined analytical indicator, not an official credit rating. Scenario outputs will remain conditional on their stated assumptions.

## Evaluation and release evidence

| Area | Evidence to produce |
| --- | --- |
| Data integrity | Unit, range, uniqueness, freshness and reconciliation checks against source records |
| Forecasting | Rolling or expanding-window evaluation against a naive baseline, with appropriate error metrics |
| Anomalies | A reviewed set of historical examples, including false alerts and limitations |
| BI | A country comparison with source drill-down and documented metric definitions |
| Reproduction | One documented command sequence from ingestion to refreshed analytical tables |

**First release boundary:** a small, well-documented set of countries and indicators with reliable ingestion and a useful BI report. Forecasts and scenarios follow once the historical data and baselines are validated.
