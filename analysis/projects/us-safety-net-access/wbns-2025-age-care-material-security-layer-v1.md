# WBNS 2025 age, care, and material-security layer v1

**Status:** published cross-sectional context layer; no causal policy or
household recovery estimate  
**Checked:** 2026-09-16  
**Unit:** adults and families represented by the December 2025 WBNS; older
adult subgroup estimates are person-level survey reports with family outcomes
where noted  
**Machine record:** [age/care/material-security record](data/wbns-2025-age-care-material-security-layer-v1.json)

## Why this layer matters

The 2025 WBNS expansion adds approximately 2,500 adults age 65 and older to a
survey that previously focused on adults ages 18–64. That makes a previously
underrepresented transition visible in the broad atlas: care need, unpaid
caregiving, and material hardship can coexist in the same life-stage context,
but the published briefs do not provide a dated service episode, provider
choice, route burden, remedy, or later political action.

## Published 2025 observations

| Surface | Estimate | Unit and boundary |
|---|---:|---|
| Unmet personal assistance among older adults with disabilities | 24.0% | Adults 60+ with disabilities; any time in prior 12 months; noninstitutional settings |
| Unmet personal-care assistance | 7.7% | Older adults with disabilities; prior 12 months |
| Unmet routine-household-task assistance | 22.9% | Older adults with disabilities; prior 12 months |
| Unmet personal assistance among all adults 60+ | 11.3% | Includes adults with and without disabilities |
| Unmet assistance among older adults with daily-activity difficulty | 33.1% | Compared with 6.9% among those with other functional limitations |
| Food insecurity among older adults with unmet assistance | 39.3% | Family/household outcome reported in the prior 12 months |
| Forgone health care because of cost among older adults with unmet assistance | 44.4% | Family/household outcome reported in the prior 12 months |
| Heating/electricity payment problems among older adults with unmet assistance | 14.5% | Family/household outcome reported in the prior 12 months |
| Regularly helping an adult relative or friend | About 18% | Adults 60+; caregiving context, not a measured hours or cost estimate |
| Unmet assistance among Medicare beneficiaries 65+ with dual coverage | 24.8% | Compared with 9.9% among Medicare-only beneficiaries; need composition differs |

These figures establish co-occurring need and hardship surfaces. They do not
establish that unmet assistance caused food insecurity, medical-cost
avoidance, utility problems, or caregiving; nor do they identify whether paid
services, family support, public benefits, or another alternative would have
prevented the hardship.

## Mechanism boundary

```text
disability or aging-related need
  -> assistance unavailable or insufficient
  -> self-care / household-task burden and family substitution
  -> food, health-care, housing, or utility exposure
  -> protected or sacrificed outcome [not fully observed]
  -> trust, complaint, political action, or service exit [not observed]
```

The layer strengthens the material/time/care and unequal-exposure themes and
provides a counterexample to a simple “older age protects against hardship”
reading: aggregate age differences can coexist with high unmet assistance
among older adults with disabilities and with distinct Medicare/Medicaid
coverage patterns. The dual-enrollment contrast should not be read as a plan
effect because disability and functional-need composition differ between the
groups.

The 2025 round is also a vintage break for trend work. The WBNS project states
that the sample expanded to include older adults in 2025. Therefore 2025
all-age estimates must not be pooled with 2017–2024 working-age estimates
without an explicit age-universe and question-harmonization design.

## Smallest next test

Obtain the authenticated 2025 respondent file or a compatible published table
with exact denominators, weights, missingness, and assistance-route fields.
Then condition unmet assistance on income, race/ethnicity, disability type,
coverage, housing, food, unpaid-care time, and service alternatives. The
stronger end-to-end test remains a dated care-need or service-access episode
with route effort, paid/unpaid substitution, protected/sacrificed outcome,
remedy, and later recovery or action.

## Sources

- [Urban Institute: One in Four Older Adults with Disabilities Had Unmet Needs for Personal Assistance in 2025](https://howhousingmatters.org/research/publication/one-four-older-adults-disabilities-had-unmet-needs-personal-assistance-2025)
- [Urban Institute WBNS project page](https://www.urban.org/policy-centers/health-policy-center/projects/well-being-and-basic-needs-survey)
- [ICPSR 2024 WBNS study metadata and universe boundary](https://www.icpsr.umich.edu/web/HMCA/studies/39691)

