# Cash-transfer recovery-currency crosswalk v1

**Checked:** 2026-09-25 · **Status:** bounded cross-study synthesis

## Question

What does additional cash actually buy for a household, and which parts of the
chain remain unobserved?

The current U.S. evidence does not support a single “cash worked” variable.
Randomized and policy-induced designs show distinct currencies:

```text
transfer
  -> spending / income / debt
  -> time allocation / care / mobility / credit
  -> stress, satisfaction, and perceived room
  -> durable security, trust, action, or exit [mostly open]
```

The records below are not pooled. They differ in sample, treatment, timing,
outcome definitions, and denominator. The purpose is mechanism comparison, not
an average treatment effect.

## Evidence matrix

| Study | Treatment and unit | Observed conversion | What it does not establish |
|---|---|---|---|
| [NBER 32784](../../records/us-nber-unconditional-cash-consumption-balance-sheets-2024.json) | 1,000 people assigned $1,000/month versus 2,000 assigned $50/month for three years; two states | Spending rose by at least $300/month; housing and neighborhood mobility, self-reported financial health, and credit scores rose; asset gains were offset by debt, leaving near-zero net-worth effects | Bill-level relief, adequacy, care/time substitution, durable security, trust, action, or exit |
| [NBER 33737](../../records/us-nber-unconditional-cash-parental-investment-heterogeneity-2025.json) | Monthly unconditional cash; multisite U.S. randomized study; subgroup comparison | Latino families shifted nearly one-third of the transfer into child-focused spending; Black families reduced maternal work hours and increased early-learning time; total-income effects were similar across groups | Racial mechanism, care quality, treatment amount in the abstract, persistence, trust, or politics |
| [NBER 34040](../../records/us-nber-unconditional-cash-parenting-stress-2025.json) | $1,000/month versus $50/month for three years; randomized family study | Child spending and reported parenting improved; low-income families increased non-parental childcare use/quality; reported child difficulties and stress also rose | Whether reported stress is clinical deterioration or greater detection, durable wellbeing, or political response |
| [NBER 30379](https://www.nber.org/papers/w30379) | Monthly cash from birth; large multisite randomized study among families in poverty | Child-specific spending and mothers’ early-learning activities increased; no detectable maternal-labor, infant-childcare, general-expenditure, or subjective-wellbeing effect | Long-run security, political meaning, or whether early-learning gains persist |
| [NBER 27717](../../records/us-nber-eitc-maternal-time-use-children-2020.json) | EITC expansions since 2003; American Time Use Surveys; policy variation rather than random cash | Maternal work rose; home production, leisure, and total time with children fell, while almost none of the reduction was active investment time | A universal work effect, household childcare substitution, or later action |
| [NBER 32583](../../records/us-nber-eitc-parent-care-gap-2026.json) | Simulated EITC generosity linked to HRS; older-parent care by eligible daughters | A $500 generosity increase reduced daughter-to-parent care by 13–24 hours/month, with no measured replacement in tested channels | Care quality, unmet need, health, earnings, or total household welfare |
| [NBER 24770](../../records/us-nber-family-income-intergenerational-voting-2018.json) | Exogenous unconditional cash transfers with linked parents and children across generations | Adult children from initially poorer families had higher adult voting propensity; parents and children from initially better-off families showed no transfer effect | Immediate recipient voting, trust, approval, vote choice, or a universal resource-to-participation effect |
| [Health Affairs Scholar safety-net stigma study](../../records/us-health-affairs-safety-net-stigma-government-perceptions-2024.json) | 497 low-income California caregivers of young children; SNAP- and EITC-eligible analytic subsamples | SNAP participation and EITC receipt were associated with greater reported social stigma; overall government perceptions did not differ, while food-insecure SNAP participants also showed program stigma and discrimination | Cross-sectional convenience/snowball sample; no causal trust effect, national estimate, durable identity change, or political-action endpoint |
| [Oregon Medicaid voter-participation study](../../records/us-oregon-medicaid-lottery-voter-participation-2019.json) | Low-income uninsured Oregon adults selected or not selected in the 2008 Medicaid lottery | Coverage increased November 2008 presidential turnout by 2.5 percentage points, but did not increase later turnout through November 2010 | Historical local program; early turnout may reflect registration, administrative contact, health/financial security, or election-specific mobilization rather than generalized trust or durable political change |

## What the comparison supports

### Cash is converted through multiple household technologies

The same broad policy category can be converted into:

- immediate consumption and mobility;
- child-specific purchases;
- maternal time and early learning;
- formal or non-parental childcare;
- reduced paid work;
- reduced unpaid elder care; or
- debt-financed rather than net-worth recovery.

These are not interchangeable. A household can report better financial health
without higher net worth, more childcare without higher satisfaction, or more
early-learning time without more child-focused spending.

### The meaning of the income source may matter

The NBER 33737 record reports different marginal propensities to purchase
child-specific goods from government income versus maternal income across
subgroups. This is evidence about a possible signal or source-of-income
mechanism, not proof of a racial psychology. It means the atlas should preserve
whether the resource came from a transfer, wages, credit, tax refund, or
in-kind service rather than collapsing all household resources into income.

### More input is not the same as better outcome

The NBER 34040 study is a useful counterexample: spending and reported
parenting improved while reported child difficulty/stress also rose and
parental satisfaction did not change. The interpretation may include improved
detection from closer monitoring. The safe code is therefore:

```text
cash -> care input improves
cash -> observed problem/stress signal rises
cash -> satisfaction unchanged
```

not “cash improved family wellbeing” or “cash harmed children.”

### Work-contingent policy can move time in the opposite direction

The EITC records complement the unconditional-cash designs. Unconditional cash
can reduce maternal work or leave it unchanged, while EITC expansions increase
maternal work and reduce some home and child time. The contrast is not a simple
cash-versus-work moral judgment: conditioning, phase-in incentives, schedule,
childcare, benefit interactions, and source meaning differ.

### The political effect may be delayed and intergenerational

The NBER 24770 study is the strongest current bridge from unconditional cash to
voting, but its boundary matters. Transfer exposure raised adult children's
voting propensity when they came from initially poorer families, while parents
showed no effect. The evidence therefore supports a resource-to-political-
participation pathway through childhood household conditions or social/human
capital formation, not a claim that a current payment immediately makes an
adult recipient vote more or trust government more.

The APSR Moving to Opportunity study supplies a deliberately contrary place-
based test. Random housing-voucher offers reduced neighborhood poverty and
improved some child socioeconomic outcomes, yet later voting did not increase
for children, adult effects were null, and teen registration/turnout declined
under both voucher conditions. Material or neighborhood improvement is
therefore not sufficient by itself to produce political participation; dosage,
developmental stage, disruption, social integration, and outcome timing matter.

The contemporary welfare study adds a program-design counterexample: cash
assistance showed little association with political participation, while food
stamps were positively associated with registration and had opposing voting
associations depending on political attentiveness. Because this design uses
fixed-effects observational models, it should constrain interpretation rather
than be read as a causal transfer effect. It reinforces that benefit type,
administrative experience, stigma, attention, registration, and turnout must
remain separate.

The NBER welfare-reform voting study supplies a positive adult-voting estimate
under a different policy bundle: greater reform exposure was associated with
about a four-point relative voting advantage among low-income women, strongest
in presidential elections and in states with stronger work incentives. Its
proposed mediators were employment, education, and income. Because this is a
state-by-year policy-exposure design rather than randomized cash, it cannot be
averaged with the cash-transfer or EITC employment estimates; it demonstrates
that policy design and estimand determine the observed political endpoint.

The safety-net stigma study adds a trust/meaning boundary to the recovery
currency map. SNAP and EITC participation were associated with greater reported
social stigma, while overall government perceptions did not differ; among
food-insecure respondents, SNAP was additionally associated with program stigma
and discrimination. Because the study is cross-sectional and based on a
California convenience/snowball sample, it does not identify a causal trust
effect. It does show why material support, stigma, government perception, and
political action must remain separate currencies rather than being collapsed
into “institutional trust.”

The Oregon Medicaid lottery adds a causal public-system-to-action endpoint to
the map. Randomized access to coverage raised turnout in the November 2008
presidential election, with no detectable increase in later elections through
November 2010. This is a useful contrast to the unconditional-cash null and
the welfare-receipt observational results: the policy route, timing, election,
and population matter. The experiment does not reveal whether the early vote
response came through financial relief, health security, administrative contact,
new registration, or mobilization, so it should not be coded as a trust effect.

## Open middle and next decisive test

No record currently follows the same household from transfer receipt through a
named bill or care obligation, a substitution decision, perceived adequacy,
blame/fairness, institutional trust, and political action or exit.

The next decisive design should join, for the same randomized household or
administrative case:

```text
assignment and actual receipt
  -> dated bills, debt, care need, and work schedule
  -> spending, time, childcare, elder-care, mobility, and health response
  -> recovery adequacy and persistence after payments stop
  -> stress, satisfaction, fairness, and responsible-actor attribution
  -> complaint, trust, turnout, organizing, switching, continued use, or exit
```

It must preserve treatment contrast, compliance, attrition, subgroup universe,
pre-treatment resources, source-of-income framing, and adverse/null outcomes.
The present evidence justifies a multi-currency recovery map; it does not close
the household-to-political-action arrow.

## Source boundary

The canonical records preserve compact, source-traceable abstract findings and
retrieval hashes. This crosswalk does not reproduce raw data or re-estimate
effects. External primary sources: [NBER Working Paper 32784](https://www.nber.org/papers/w32784),
[NBER Working Paper 33737](https://www.nber.org/papers/w33737),
[NBER Working Paper 34040](https://www.nber.org/papers/w34040),
[NBER Working Paper 30379](https://www.nber.org/papers/w30379),
[NBER Working Paper 27717](https://www.nber.org/papers/w27717), and
[NBER Working Paper 32583](https://www.nber.org/papers/w32583), and [Health Affairs
Scholar, Association of Safety-Net Program Participation with Government
Perceptions, Welfare Stigma, and Discrimination](https://academic.oup.com/healthaffairsscholar/article/2/1/qxad084/7486464).
The [Quarterly Journal of Political Science Oregon Medicaid voter-participation
study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8021132/) is also retained as a
causal action contrast.
