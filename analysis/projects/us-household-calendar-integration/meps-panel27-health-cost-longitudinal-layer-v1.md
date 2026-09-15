# MEPS Panel 27 health-cost longitudinal layer v1

The 2023 MEPS Panel 27 Longitudinal Public Use File adds a repeated person
and health-cost layer to the material/time/care program. It follows the same
panel persons across the 2022 and 2023 calendar years and contains annual
health expenditures, out-of-pocket spending, insurance status, family income,
employment, and perceived health fields.

| Observation | Total health expenditure | Out-of-pocket expenditure | Uninsured any time | Continuous coverage |
|---|---:|---:|---:|---:|
| 2022 | $6,971.74 (n=8,226) | $961.32 | 6.89% | 56.35% |
| 2023 | $7,328.55 (n=8,175) | $970.57 | 5.92% | 56.99% |
| 2022→2023 paired sample | +$630.83 (n=7,812) | -$50.50 | — | — |

In the valid paired health-status comparison, 21.01% improved, 22.85%
worsened, and 56.14% remained unchanged. The pairing is limited to persons
with `ALL5RDS=1` and valid expenditure and perceived-health fields. Health
status is an ordinal self-report, not a clinical outcome.

The baseline material gradient is not a simple health-direction gradient. In
the paired sample, health improved for 23.49% of the poor/negative-income
category and 18.74% of the high-income category; health worsened for 27.03%
and 21.47%, respectively. Mean total-expenditure change was +$803.21 and
+$322.19 per person in those two groups. The income categories are the
official MEPS family-income-to-poverty categories; these are descriptive
subgroups, not adjusted estimates.

The useful program signal is a non-synchronization result: aggregate health
expenditure rose in the panel, while the paired mean out-of-pocket change was
negative, and health improvement and worsening both occurred at meaningful
rates. This keeps health cost, insurance protection, and health experience as
separate currencies rather than collapsing them into one welfare score.

Estimates use the released MEPS longitudinal weight (`LONGWT`) and now use
`VARSTR` and `VARPSU` for Taylor-linearized standard errors. The paired total-
expenditure change is +$630.83 (SE $245.77; approximate 95% interval
$149.11–$1,112.55), while the paired out-of-pocket change is −$50.50 (SE
$63.32; approximate 95% interval −$174.60–$73.61). The extraction preserves
the official ASCII layout and archive hashes. These normal-approximation
intervals do not resolve expenditure skewness, attrition, nonresponse, or
subgroup composition.

The same five-round panel adds a bounded work endpoint. Among 6,442 persons
with valid EMPST3/EMPST5 status, 62.08% were employed in both endpoint rounds
(SE 0.86 percentage points), 2.77% moved from employed to not employed (SE
0.27 points), and 5.05% moved from not employed to employed (SE 0.40 points).
The paired person wage-income change was +$2,012.35 (SE $524.12) in its own
valid paired wage universe. These are continuity and income measures, not job
quality, schedule control, or evidence that health cost caused employment
change.

This layer strengthens the material condition → health-cost/coverage → health
outcome arrow. It does not identify a particular bill, provider, insurer,
employer, price, or policy as the cause; it does not measure household time,
care substitution, treatment delay, trust, political action, consumer exit, or
geopolitical consequence. Panel retention and valid-field selection remain
open sources of uncertainty.

[Machine-readable record](../../records/us-meps-panel27-health-cost-longitudinal-2022-2023.json)  
Analysis script: `scripts/analyze_meps_panel27_longitudinal.py`

Sources: [MEPS HC-252 public-use file page](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-252),
[Panel 27 documentation](https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252doc.pdf),
and [Panel 27 codebook](https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252cb.pdf).
