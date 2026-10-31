# Company trend-intelligence records

This folder is the operating layer for the company-facing goal in
`COMPANY_TREND_INTELLIGENCE_GOAL_V1.md`.

Start with the [company trend-intelligence index](INDEX.md), then use the
schema and template to extend the record set.

The existing 14-theme atlas remains the evidence base. These records add the
business translation needed by strategy, product, risk, finance, operations,
people, and public-affairs teams.

## Record contract

- `schema.json` defines the required machine-readable fields.
- `portfolio.json` exposes the current records and portfolio lens to a frontend
  or downstream analysis.
- `board.html` is a lightweight browser reader for the JSON portfolio.
- `TEMPLATE.md` is the plain-language authoring template.
- A record must preserve the source claim, mechanism, affected groups,
  uncertainty, counterevidence, business exposure, indicators, and next test.

Do not call a candidate a confirmed trend merely because it is repeated in
news or public discussion. Public discussion can discover a signal; research,
official records, market data, or other independent evidence must qualify or
confirm it.

Validate the portfolio and every linked record with:

```bash
python3 scripts/validate_company_trend_intelligence.py
```

## Lifecycle

```text
signal -> candidate -> evidence check -> qualified/confirmed/rejected
       -> company translation -> indicators -> monitored finding
```

The business translation is a hypothesis unless the underlying business effect
is directly measured. Keep scenarios, implications, and recommendations
separate from observed results.
