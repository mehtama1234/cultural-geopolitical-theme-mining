# SHED panel weight-audit layer v1

The official 2024 and 2025 SHED public-use CSV archives were rechecked for the
uncertainty gate on the 2024–2025 recontact panel. Both files contain main and
panel weight fields, but neither exposes replicate-weight, BRR, jackknife,
bootstrap, or variance-estimation columns in the public-use CSV.

This confirms the boundary on the existing panel persistence results: they can
be reproduced as weighted descriptive transitions among recontacted
respondents, but design-based standard errors or confidence intervals cannot be
claimed from the downloaded public-use fields alone. A future release,
restricted-use design file, or documented replicate-weight method is required
before promoting uncertainty estimates.

The audit is recorded in
[`shed-panel-weight-audit-2026-09-13.json`](shed-panel-weight-audit-2026-09-13.json)
and uses the official [SHED data releases](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
