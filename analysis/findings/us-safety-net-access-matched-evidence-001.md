# A benefit can be lost without the need going away

## The argument

Eligibility is not access. A household can qualify for food or health help and still lose it because a form was late, an office closed, a notice was missed, or the proof demanded more time than the family had. A falling caseload can therefore mean higher earnings, a successful exit, or an administrative failure. The number alone cannot tell us which.

The key question is what happened after the benefit ended. Did work rise? Did food security improve? Or did the household buy less food, borrow, skip care, or return later? Exit is an event to explain, not a success label.

The deeper finding is that administration is part of the benefit. A program’s real value depends on the hours, travel, internet, language access, childcare, and attention required to receive it. A rule can be formally neutral and still remove more help from families with less spare time.

There are three different states that are often reported as one: a family is not eligible, a family is eligible but has not applied, and a family is enrolled but loses the benefit. Each points to a different problem. Income policy addresses the first. Outreach and trust affect the second. Notice, renewal, verification, and office design affect the third. A caseload number cannot separate them.

## Follow one renewal

A parent works irregular hours and receives SNAP. A renewal notice arrives while the family is moving. The parent cannot reach the office during work, has no stable internet, and misses the deadline. Benefits stop. The family buys less food, borrows from relatives, or works an extra shift. The need did not disappear; the route to help did.

That extra shift should not automatically be counted as program success. It may be a healthy increase in work, or it may replace food assistance at the cost of sleep and family time. Only household outcomes can separate the two.

Timing can make the loss sharper. A notice may arrive after a move, a paycheck may cross an eligibility line for one month, or a recertification may be due before the household is paid. The family can lose help before it has enough cash to replace it. If benefits later return, the gap may still have produced debt, skipped meals, or missed care. A later approval does not erase the cost of the interruption.

```text
food or income need
  -> eligibility, work rule, office distance, and renewal task
  -> benefit kept, lost, or never reached
  -> food, work, debt, health, and trust change
```

## What the sources actually establish

| Evidence | Meaning | Limit |
|---|---|---|
| NBER finds a 23-point increase in SNAP exits among incumbent participants after 18 months and no employment effect under a work requirement. | Exit does not prove more work. | The result belongs to a specific policy and setting. |
| NBER finds parents did not increase work but were much less likely to receive SNAP. | Aid can fall without the claimed work response. | We still need each household’s exact reason for exit. |
| NBER finds participation fell 7–9% over two years after an enrollment office closed in one state. | Distance can change access even when eligibility remains. | The result does not measure every later household outcome. |
| USDA summarizes evidence that SNAP improves food security and smooths food access across the month. | Losing access can create a real household cost. | The summary does not identify the cause of each exit. |

## What the 2025 SIPP transition layer adds

The newer Census SIPP analysis places observed SNAP transitions beside a
following-month material-hardship field. It uses 346,283 valid adjacent
person-month pairs and official 240-replicate Fay-BRR weights. The comparison
is descriptive: it does not estimate what SNAP caused, and the person-month
unit is not a complete household benefit spell.

| Observed transition | Valid pairs | Rent/mortgage hardship in the following record | Utility hardship in the following record |
|---|---:|---:|---:|
| No → No | 312,418 | 3.86% (SE 0.24 pp) | 5.86% (SE 0.31 pp) |
| No → Yes | 437 | 16.40% (SE 3.61 pp) | 20.80% (SE 3.49 pp) |
| Yes → No | 387 | 11.53% (SE 3.14 pp) | 20.83% (SE 4.41 pp) |
| Yes → Yes | 33,041 | 11.98% (SE 1.13 pp) | 18.61% (SE 1.38 pp) |

Three implications matter for the access question. First, entry is observed
amid material pressure rather than as a clean before/after rescue. Second,
exit is not equivalent to restored security: the exit group retains elevated
following-record hardship, especially for utilities. Third, continued receipt
also coexists with hardship, so participation and household protection are
separate stages. The intervals are wide for the rare entry and exit groups,
and “following” is record order rather than proof that a particular bill
arrived after the transition.

The companion reason layer shows that classified entries have multiple routes:
job loss or reduced wages, loss of other income, disability, family change,
and other reasons. Among classified entries, job loss/wage reduction is the
largest named category (57 pairs), while the exit categories include higher
income, family change, requirements, time limits, non-collection, and “not
worth the trouble.” Only 217 of 437 entries and 188 of 387 exits have a
classified reason. Unknown reason is therefore part of the boundary, not a
missing detail that can be silently dropped.

This SIPP layer strengthens the causal participation studies without closing
the household story. It shows that the observed public-system state and the
material outcome can diverge; it still does not observe the notice, route
effort, documents, benefit amount or timing, appeal, correction, food
quantity, debt, health, trust, or political response for the same episode.

See the [SIPP transition-to-hardship layer](../projects/us-safety-net-access/sipp-snap-transition-outcome-fay-brr-layer-v1.md)
and the [reason-by-hardship layer](../projects/us-safety-net-access/sipp-snap-transition-reason-outcome-fay-brr-layer-v1.md)
for the full denominators, intervals, reproduction commands, and field
boundaries.

## Current program context from USDA

The latest USDA ERS program summary anchors the access evidence in the scale of
the institution: SNAP averaged 42.1 million participants per month in FY2025,
with $101.7 billion in federal spending and an average benefit of $187.94 per
participant per month. The reported share of US residents receiving SNAP in an
average month was 12.3%, with state shares ranging from 21.9% to 4.7%.

For FY2024, USDA reports that 28% of SNAP households had earned income and 54%
of households with children had earned income; 62% had unearned income and 19%
had neither reported earned nor unearned income. Benefit distribution also
varied: 37% received the maximum for their household size and 9% the minimum.
These are participating-household and program-scale measures, not estimates
of the eligible nonparticipant population or benefit adequacy.

USDA ERS summarizes research that food security deteriorates before receipt and
improves afterward, while also noting that benefit changes affect food
spending and food insecurity. That research context supports the material
importance of access, but it is not a pooled estimate and does not identify
the same household's notice, route, interruption, debt, health, trust, or
political response. The [current USDA context layer](../projects/us-safety-net-access/usda-snap-fy2025-current-context-layer-v1.md)
keeps those official scale and research-summary claims separate from the NBER
causal route studies and SIPP transition estimates.

Sources: [NBER SNAP work requirements](https://www.nber.org/papers/w28877), [NBER parent study](https://www.nber.org/papers/w32441), [NBER office closure study](https://www.nber.org/papers/w34529), and [USDA SNAP research](https://www.ers.usda.gov/topics/food-nutrition-assistance/supplemental-nutrition-assistance-program-snap/key-statistics-and-research).

## The deeper finding

Administrative burden behaves like a household bill. It consumes work hours, travel, internet, language support, childcare, and attention. Families with a small cash cushion may also have the smallest time cushion, so the same renewal task costs them more.

The burden is not only inconvenience. It changes the return from applying. If a family must spend a day away from work, pay for transport, find childcare, copy documents, and wait for a decision, the expected benefit has to cover those costs before the family can justify the effort. A program can therefore be generous on paper and thin in practice for the people with the least room to apply.

The work rule creates another risk. If support falls quickly as earnings rise, a small increase in wages can leave the family with less total room after food, transport, childcare, and lost benefits. That does not mean work caused the hardship. It means the transition needs to be measured as a whole budget, not as earnings alone.

This creates a quiet political effect. When a program is hard to use, the public may see fewer recipients and infer less need. The people who disappeared from the rolls may still be buying less food or carrying more debt. A lower caseload can hide a weaker connection between public help and daily life.

That gap can change trust in both the program and the state. A person who is eligible but cannot complete the process may experience the rule as a broken promise. But distrust is an inference, not a measured result in the cited studies. It must be tested with the actual notice, burden, outcome, and later view of the household.

## What remains unknown

The studies do not show the same household’s application, notice, office trip, renewal, benefit, work, earnings, food security, borrowing, health, and return to the program. They also do not separate higher income from administrative failure in every exit.

They also do not tell us how much help was replaced by family support, a food bank, credit, or an extra shift, or whether the replacement lasted. A lower caseload and higher employment can occur at the same time as worse food security.

## Next test

Follow households before and after a rule or office change. Record the exact reason for exit, time spent, travel, internet, language, disability, childcare, work, food, borrowing, health, and return. Report both participation and what happened to the household after participation changed.

Build an event ledger around each renewal: notice date, deadline, documents requested, attempts made, hours lost, costs paid, decision date, benefit amount, and first missed or restored purchase. Match it to earnings, work hours, food security, debt, and care. Compare online, phone, mail, and in-person paths, and report the result by household type. This would show whether a rule changes need, or only changes who can complete the route to help.

## Reading rule

Do not call program exit a work success. Ask whether the household became safer, or simply lost the route to help.
