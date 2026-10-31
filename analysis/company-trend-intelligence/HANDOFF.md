# Company trend-intelligence handoff

## What is now in place

The repository has a company-facing layer over the 14-theme cultural, social,
financial, institutional, and geopolitical atlas.

- [Goal](../../COMPANY_TREND_INTELLIGENCE_GOAL_V1.md) — the governing purpose.
- [Index](INDEX.md) — the human reading route.
- [Portfolio](PORTFOLIO.md) — cross-domain interpretation.
- [Portfolio JSON](portfolio.json) — frontend/downstream data contract.
- [Portfolio CSV](portfolio.csv) — spreadsheet and BI export.
- [Board](board.html) — lightweight browser reader.
- [Decision playbook](DECISION-PLAYBOOK.md) — weekly, monthly, and quarterly use.
- [Schema](schema.json) and [template](TEMPLATE.md) — record contract.
- [Validator](../../scripts/validate_company_trend_intelligence.py) — integrity check.

## Current record set

There are six qualified trend records:

1. AI and workplace control.
2. Consumer recourse and practical exit.
3. Geopolitical capability and permission.
4. Cultural and language technology.
5. Infrastructure capacity and reliable benefit.
6. Household financial pressure and navigation work.

These are not universal forecasts or company rankings. They are evidence-backed
trend candidates with explicit business exposure, confidence, time horizon,
leading indicators, limitations, and next tests.

## Frontend integration

For a static or app frontend, load `portfolio.json` and render:

- `title`, `status`, `confidence`, and `horizon` as the card header;
- `domains` as filters or tags;
- `decision_owners` as audience routing;
- `open_test` as the uncertainty callout;
- `path` as the link to the full evidence-backed record.

The board uses the same JSON contract and is a reference implementation. The
Markdown records remain the source of interpretation and limitations.

## Validation and local preview

From the repository root:

```bash
python3 scripts/validate_company_trend_intelligence.py
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/analysis/company-trend-intelligence/board.html
```

The validator checks JSON, CSV, record paths, IDs, titles, required headings,
statuses, confidence, and horizons.

## Evidence boundary

The current layer proves that the records are traceable and decision-oriented.
It does not yet prove company-specific causal impact, revenue lift, retention,
market share, or geopolitical prediction. Those require named-company exposure,
time-aligned business metrics, and the next tests stated in each record.

Future records should use the same contract and should not be promoted from
signal to qualified trend without direct evidence, a mechanism, a counterexample,
business exposure, leading indicators, and a test that could change the finding.
