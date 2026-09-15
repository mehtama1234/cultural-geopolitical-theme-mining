# Auto-IRA cross-paper reconciliation layer v1

**Checked:** 2026-09-14  
**Status:** evidence reconciliation; do not pool estimates

## Why the two papers are not one result

The project now contains two 2026 Auto-IRA studies using SIPP-related evidence,
but they answer different questions with different policy contrasts and outcome
sets.

| Dimension | Bloomfield, Dao, Lee & Slavov, NBER w35373 | Rao, Dao & Lee, CRI WP 2026-02 |
|---|---|---|
| Main question | How Oregon Auto-IRA exposure changes household balance sheets | Whether state Auto-IRA mandates change retirement timing and Social Security claiming |
| Policy contrast | Private-sector workers likely exposed to OregonSaves compared with similar workers in states not yet adopting; firm-size rollout contributes to exposure | Seven early-adopter states compared with non-adopter states using staggered adoption |
| Publicly available unit | SIPP comparison; exact analytic counts unavailable in the accessible summary | 1,803,085 retirement-timing person-wave observations; 1,801,923 claiming observations |
| Main design detail | Policy exposure and firm-size rollout, as described in the NBER abstract/Georgetown summary | Callaway–Sant’Anna staggered difference-in-differences, population weights, state/year fixed effects, controls, state-clustered wild-bootstrap errors |
| Main outcomes | IRA and employer-plan ownership/assets; checking/savings ownership/balances; credit-card debt incidence/balance | Retirement before age 65/67, delayed retirement, Social Security claiming windows; ownership/assets and household-finance mechanism outcomes |
| Reported headline direction | Ownership/assets and checking/savings margins increase; credit-card debt rises modestly | Early retirement/claiming decline; later retirement/claiming rise; no statistically significant total retirement-asset change in the full-controls model |
| Balance-sheet details | IRA ownership +2.7pp to 12.7%; IRA balances >$8,500; credit-card debt incidence +2pp; balance +$90, as reported in the companion summary | Model-3 retirement assets +$20,143, not statistically significant; checking balance −$247.23, not significant; unsecured debt −$236.41, p<0.10; monthly earnings +$102.3, p<0.01 |

## What can be reconciled

The studies are consistent at the broad institutional level: automatic workplace
saving can change more than an account-ownership indicator. Both examine
spillovers into household or life-course decisions, and both motivate a
liquidity/behavioral interpretation rather than treating enrollment as the final
outcome.

The different balance-sheet directions are not automatically contradictory. The
NBER paper's reported checking/savings result is an ownership-and-balance
finding in an Oregon/firm-size exposure design. The CRI paper's checking result
is a separate full-sample mechanism outcome in a seven-state staggered design,
and the relevant estimate is not statistically significant in the full-controls
model. The NBER credit-card result and CRI unsecured-debt result also refer to
different debt concepts and designs.

The retirement-asset estimates should likewise remain separate. The NBER summary
reports more than $8,500 in IRA balances, while the CRI paper reports no
statistically significant total retirement-asset change in its full-controls
model and explicitly cannot identify whether an account is an Auto-IRA or a
401(k). These are not commensurate enough to average.

## What remains unresolved

The accessible NBER material does not expose its exact sample counts, full
specification, standard errors, account/debt definitions, or subgroup tables.
The CRI paper does expose those details for its own design, but not a common
cross-paper microdata extract. We therefore cannot determine whether the
differences arise from:

- Oregon-only versus seven-state treatment exposure;
- firm-size rollout versus state-adoption timing;
- different SIPP panels, years, or worker universes;
- different account, balance, checking, credit-card, and unsecured-debt
  definitions;
- different treatment intensity or time since adoption;
- different controls, weighting, or outcome construction; or
- genuinely heterogeneous household responses.

The correct next test is a harmonized replication table using both papers' code
or appendices: same SIPP years, private-sector and age universes, treatment
definition, firm-size exposure, state cohort, account/debt variables, weights,
and inference. Until then, the atlas should carry two linked records and label
the apparent disagreement as an estimand/sample boundary.

## Sources

- [NBER Working Paper 35373 page](https://www.nber.org/papers/w35373)
- [NBER/Georgetown balance-sheet summary page](https://cri.georgetown.edu/states/state-reports-and-briefs/)
- [Georgetown retirement-timing working paper](https://cri.georgetown.edu/wp-content/uploads/2026/06/CRI_WP_Rao_Dao_Lee_AutoIRA_final.pdf)
- [Georgetown retirement-timing issue brief](https://cri.georgetown.edu/wp-content/uploads/2026/07/Manita-Rao-et-al.-_Issue-Brief-Beyond-Account-Ownership-.pdf)
