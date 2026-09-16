# CES medical-affordability/action reproduction audit

**Checked:** 2026-09-16  
**Status:** reproduced local screening output; not a new estimate  
**Purpose:** verify that the existing material-exposure → attribution/action
layer remains reproducible from the already acquired local files

## Reproduction result

The existing analysis was rerun against the local 2018 and 2020 CES crisis
module extracts. Both files contain 1,000 valid module rows in the analysis,
and the key descriptive and model-screen results match the committed
[trend record](../../records/us-cces-medical-affordability-political-participation-2018-2020.json)
at the published precision.

| Check | 2018 | 2020 |
|---|---:|---:|
| Weighted medical-expense-crisis share | 27.673% | 14.308% |
| Medical-crisis contact-official share | 23.308% | 28.258% |
| Medical-crisis protest share | 7.149% | 9.076% |
| Adjusted contact odds ratio | 1.694 (1.106–2.593) | 1.799 (1.023–3.164) |
| Crisis rows used in descriptive group | 257 | 152 |

The pooled contact screen also reproduced an odds ratio of **1.831** with a
model-robust interval of **1.219–2.750** across 1,771 complete cases. The
hardship × 2020 interaction remained non-significant in the existing screen
(OR **0.956**, model-robust interval **0.488–1.871**). These intervals are
screening diagnostics, not CES design-based uncertainty estimates.

## Source integrity

The local source hashes match the acquisition manifest:

| File | SHA-256 |
|---|---|
| `CCES18_crisis_vv.tab` | `c61ccc59c7f9232cbb7abd420654b907cb0997433c80ce0efe391d4f257d3d58` |
| `CCES20_crisis_vv.tab` | `10fe9927942f345b9b39f58b4c07daa130baa997537f4cecfe76e6d7c024cd1e` |

The rerun output was written outside the repository at
`/tmp/cgtm-ces-medical-affordability-action-recheck.json` and had SHA-256
`2ac94160eda6f9c95b03d9f36ff21c3d290b7bec96b33109c59fe671bfa119d7`.
No source file was downloaded during this audit.

## Interpretation boundary

This recheck strengthens reproducibility of a same-respondent descriptive
screen that measures reported medical-expense hardship, attribution, and
political actions. It does not add a dated bill, care/payment adaptation,
institutional remedy, trust change, recovery, switching, or exit outcome. The
2018/2020 questions refer to broad prior-year conditions; the `teamweight`
results use model-robust HC1 screening rather than reproduced CES
design-based variance. Health, income, insurance, prior turnout, other crises,
political identity, and selection remain alternative explanations.

## Reproduction command

```bash
python3 scripts/analyze_ces_medical_affordability_political_action.py \
  --input-2018 /tmp/personal-crisis-rep/CCES18_crisis_vv.tab \
  --input-2020 /tmp/personal-crisis-rep/CCES20_crisis_vv.tab \
  --output /tmp/cgtm-ces-medical-affordability-action-recheck.json
```

Related: [CES political-action acquisition audit](politics-personal-crisis-medical-affordability-participation-audit-v1.md),
[material-to-action status ledger](../../US-BROAD-MATERIAL-TO-ACTION-STATUS_V1.md),
and [material pressure to political meaning](../us-cost-trust-politics/material-pressure-to-political-meaning-synthesis-v1.md).
