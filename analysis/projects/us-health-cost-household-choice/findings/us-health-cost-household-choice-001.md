# Health spending can rise while household payment and health direction diverge

**Status:** provisional longitudinal material/health finding · **Checked:** 2026-09-14

## The bounded finding

The MEPS Panel 27 Longitudinal Public Use File shows why health spending is
not a single welfare measure. Among the repeated persons observed across 2022
and 2023, mean total health expenditure rose while the paired mean out-of-
pocket change was negative. Within the same paired sample, some people
reported improved health, some worsened health, and most reported no change.

The safe conclusion is:

> Health-cost protection, total system spending, and a person's health
> direction are separate currencies that can move in different directions.

This is a weighted descriptive longitudinal result. It does not identify the
bill, provider, insurer, employer, policy, or household decision that produced
any person's change.

## What the panel measures

MEPS Panel 27 follows civilian noninstitutionalized US persons across the 2022
and 2023 calendar years. The extraction uses the released longitudinal weight
(`LONGWT`) and retains valid-field denominators.

| Measure | 2022 | 2023 | Paired 2022→2023 result |
|---|---:|---:|---:|
| Mean total health expenditure/person | $6,971.74; n=8,226 | $7,328.55; n=8,175 | +$630.83; n=7,812 |
| Mean out-of-pocket expenditure/person | $961.32 | $970.57 | −$50.50; n=7,812 |
| Uninsured at any time | 6.89% | 5.92% | Not a paired change estimate |
| Continuous coverage | 56.35% | 56.99% | Not a paired change estimate |
| Perceived health improved | — | — | 21.01% |
| Perceived health worsened | — | — | 22.85% |
| Perceived health unchanged | — | — | 56.14% |

The expenditure totals and paired changes use different valid-field bases. The
paired health-direction comparison is limited to persons with all five rounds
and valid paired expenditure and perceived-health fields. Perceived health is
an ordinal self-report, not a clinical diagnosis or treatment-success measure.

### Design-based precision

The extraction now uses the released `LONGWT`, `VARSTR`, and `VARPSU` with
Taylor linearization. The intervals below are normal approximations; they do
not resolve expenditure skewness, attrition, nonresponse, or subgroup
composition.

| Estimate | Point estimate | SE | Approximate 95% interval |
|---|---:|---:|---:|
| 2022 mean total health expenditure | $6,971.74 | $296.74 | $6,390.13–$7,553.35 |
| 2023 mean total health expenditure | $7,328.55 | $265.46 | $6,808.24–$7,848.85 |
| Paired total-expenditure change | +$630.83 | $245.77 | +$149.11–$1,112.55 |
| Paired out-of-pocket change | −$50.50 | $63.32 | −$174.60–$73.61 |
| Paired health improved | 21.01% | 0.66 pp | 19.71–22.31% |
| Paired health worsened | 22.85% | 0.76 pp | 21.35–24.35% |

The interval for paired out-of-pocket change includes zero. The total-
expenditure change is positive under this approximation, but remains
descriptive and does not establish why spending changed or whether it improved
household security.

### Work continuity is a separate endpoint

The same panel also permits a bounded employment comparison, but its valid
universe is different from the health-cost universe. Among 6,442 persons with
all five rounds and valid employment status in rounds 3 and 5:

| Employment endpoint | Share | SE | Approximate 95% interval |
|---|---:|---:|---:|
| Employed in both endpoint rounds | 62.08% | 0.86 pp | 60.40–63.76% |
| Employed → not employed | 2.77% | 0.27 pp | 2.23–3.31% |
| Not employed → employed | 5.05% | 0.40 pp | 4.27–5.83% |
| Person wage-income change, separate valid paired wage universe | +$2,012.35 | $524.12 | $985.07–$3,039.62 |

These fields do not identify hours, job quality, schedule control, leave,
employer action, or whether health costs caused a transition. They add a
measured work-continuity endpoint to the architecture while preserving the
distinction between a health-cost movement and a labor-market outcome.

## The material gradient

The paired result does not imply that health direction follows a simple
income gradient:

| Baseline 2022 family income-to-poverty category | Total-expenditure change/person | Out-of-pocket change/person | Health improved | Health worsened | n |
|---|---:|---:|---:|---:|---:|
| Poor/negative income | +$803.21 | +$4.85 | 23.49% | 27.03% | 1,191 |
| Near-poor income | +$639.02 | −$433.02 | 21.15% | 19.06% | 372 |
| Low income | +$664.26 | +$39.51 | 23.66% | 24.25% | 1,093 |
| Middle income | +$1,005.78 | +$47.44 | 22.19% | 23.01% | 2,179 |
| High income | +$322.19 | −$125.05 | 18.74% | 21.47% | 2,977 |

These are descriptive cells, not adjusted estimates. Income categories combine
different age, health, insurance, employment, family, provider-price, and
utilization compositions. The near-poor out-of-pocket decline is especially
unsafe to interpret without subgroup-specific precision, coverage transitions,
and the underlying service mix.

## The mechanism under test

```text
health need and treatment
  -> insurer/public coverage, provider price, and payment obligation
  -> total spending, out-of-pocket cost, debt, time, or care substitution
  -> treatment continuity and perceived health direction
  -> work, family care, household security, trust, and political meaning
```

The panel directly supports repeated expenditure, coverage, perceived-health,
and bounded employment/wage observation. It does not measure the time and care
substitution in the middle or the household, institutional, and political
outcomes at the end.

## What the non-synchronization means

An increase in total expenditure can reflect more care, higher prices, a change
in service mix, serious illness, or other composition. A fall in paired
out-of-pocket spending can reflect coverage, timing, utilization, or valid-field
selection; it is not proof that households became financially safer. Health can
worsen while out-of-pocket spending falls, and it can improve while spending
rises.

This is precisely why the atlas should not label total health expenditure as
household burden or out-of-pocket spending as the entire cost of care. The
unmeasured cost may appear in unpaid family time, missed work, travel, delayed
treatment, debt, or reduced choice.

## Counterexamples and limits

- A person with higher spending may receive valuable treatment and experience
  better health, while another with low spending may forgo needed care.
- Public or private coverage can reduce out-of-pocket cost while total system
  spending rises.
- Lower out-of-pocket spending can result from fewer services, not better
  protection.
- Perceived health may remain stable despite substantial treatment or time
  burden, and may worsen for reasons unrelated to medical spending.
- Panel attrition, valid-field selection, longitudinal weighting, normal
  approximation, expenditure skewness, and subgroup composition limit precision
  and subgroup inference.

## Next test

Link the panel's spending and coverage changes to treatment continuity, unmet
need, medical debt, employment and hours, unpaid care, travel, food/housing
trade-offs, and later recovery. Stress-test the Taylor estimates against
alternative valid-field universes and skew-robust or transformed expenditure
summaries, while preserving the distinct universes for total expenditure,
out-of-pocket expenditure, coverage, perceived health, and work/care outcomes.

The strongest counterexample is a person whose coverage protects out-of-pocket
room while treatment and health worsen for another reason. The strongest
end-to-end evidence would observe a dated care event, the payment and time
response, the protected or sacrificed need, and later health or work recovery
in the same person or household.

## Sources

- [MEPS HC-252 Panel 27 longitudinal public-use file](https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-252)
- [Panel 27 documentation](https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252doc.pdf)
- [Panel 27 codebook](https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252cb.pdf)
- [Machine-readable MEPS record](../../../records/us-meps-panel27-health-cost-longitudinal-2022-2023.json)
- [MEPS longitudinal layer](../../us-household-calendar-integration/meps-panel27-health-cost-longitudinal-layer-v1.md)

**Evidence status:** repeated weighted person-level descriptive evidence;
design-based uncertainty, treatment/time mechanisms, household adaptation,
institutional response, and political meaning remain open.
