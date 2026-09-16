# Project: US cost of living, trust, and political response

## Question

How do ordinary costs—food, housing, health care, energy, and debt—turn into trust, blame, identity, and political demand?

## Short end-to-end goal

Follow a real household experience from the bill or lost benefit to what the person does next, then test whether that experience changes how people judge firms, government, parties, or the economy.

```text
price, income, benefit, or job change
  -> household adjustment or loss
  -> view of personal and national conditions
  -> trust, blame, identity, or political demand
  -> policy, firm, media, or voting response
```

Do not assume that a bad economic view comes from a bad personal outcome. Test personal experience, party identity, news, local conditions, and policy changes separately.

The next executable design is the [political-response measurement specification](political-response-measurement-spec-v1.md). It keeps exposure, adjustment, interpretation, expression, and political action separate and defines the valid respondent, place, and event-study alternatives.

The [ANES 2024 source record](anes-2024-political-path-source-record-v1.md) maps a current respondent-level pre/post political layer to that design. Official SDA estimates are recorded in the [ANES panel judgment and action layer](anes-2024-panel-judgment-action-layer-v1.md); local microdata reproduction remains open.

The [CPS 2024 turnout and participation-friction layer](cps-2024-turnout-participation-friction-layer-v1.md) adds a separate population-level action endpoint: turnout, registration, and reported reasons for not voting. It is not joined to ANES or SHED respondents.

The [ANES 2024 political judgment layer](anes-2024-political-judgment-layer-v1.md) now adds weighted, complex-design cross-tabs for financial worry against national economic judgment, federal-government trust, and reported presidential vote. It is a separate respondent-level layer beside SHED, not a join to SHED or a causal economic-voting result.

The [economic adaptation, perception, and public action layer](economic-adaptation-perception-action-layer-v1.md)
records the broader cross-source distinction: consumer adaptation,
economic judgment, institutional trust, cultural meaning, and civic/political
action are separate measured outcomes. It keeps the missing attribution and
longitudinal middle visible.

The [Federal Reserve 2025 price-adaptation and judgment layer](federal-reserve-2025-price-adaptation-judgment-layer-v1.md)
adds current household reports of price pressure, adaptation, bill/food
hardship, personal financial well-being, and national economic judgment. It
keeps the material-to-political arrow open rather than treating adaptation as
proof of trust or voting change.

The [New York Fed EHI distributional layer](new-york-fed-economic-heterogeneity-layer-v1.md)
adds demographic and regional inflation, earnings, and spending context. Its
[December-to-April vintage comparison](new-york-fed-ehi-vintage-comparison-v1.md)
preserves the gasoline-driven reversal in 2026 rather than treating subgroup
exposure as static.

The [Pew source-environment and civic-action crosswalk](pew-source-environment-action-crosswalk-v1.md)
organizes news-source use, influencer exposure, attention, trust, civic styles,
and direct action as separate stages in the cultural/political pathway.

The current detailed findings preserve the same boundary across several
political meaning routes: [financial dissatisfaction can coexist with lower
trust without proving a vote mechanism](findings/us-cost-trust-politics-012.md),
and the broader [political meaning synthesis](findings/us-cost-trust-politics-013.md)
keeps personal and national economic judgment, trust/fairness, reported vote,
and civic action as distinct outputs. These findings are respondent-level
descriptive bridges, not a pooled economic-voting estimate; timing, attribution,
prior identity, source environment, and institutional response remain open.

The [party-conditioned ANES finding](findings/us-cost-trust-politics-014.md)
adds the identity counterexample directly: strong partisans' reported votes
remain concentrated across worry categories, while independents show more
visible worry/vote variation. The official SDA export has no reproduced
design-based standard errors, so this remains descriptive rather than causal.

The [regional price-and-firm-capacity finding](findings/us-cost-trust-politics-015.md)
adds the April 2026 New York Fed EHI release. It places regional household
price exposure, real gasoline adjustment, and small-firm employment
expectations beside one another while keeping household incidence, service
loss, trust, and political action open.

The [July 2026 Census HTOPS/HPS finding](findings/us-cost-trust-politics-016.md)
adds a current same-round household surface: expense and price pressure,
energy trade-offs, food and assistance routes, anxiety/loneliness, and trust in
federal statistics and Congress. It is a cross-sectional bridge, not a causal
price-to-trust result; replicate-weight precision, attribution, recovery, and
political action remain open.

The [March–May–July 2026 Census comparison](findings/us-cost-trust-politics-017.md)
now applies the official 80-replicate successive-difference formula to the
corrected cross-sectional files. It shows broad expense difficulty nearly flat
from May to July while food, energy, and institutional measures move on partly
different paths. The [2026 HTOPS/HPS vintage recheck](htops-2026-vintage-recheck-2026-09-14.md)
confirms that July remains the latest 2026 PUF and that March and May were
weight-corrected on September 10; no unlisted August wave is interpolated.
different paths; the snapshots are not a recontact panel.

The [April–June 2025 linked-panel finding](findings/us-cost-trust-politics-018.md)
uses 6,564 shared `SCRAMID` respondents to observe material, work, and selected
institutional transitions. The [linkage audit](htops-2025-panel-linkage-audit-v1.md)
keeps selected retention and the missing attrition-adjusted longitudinal weight
visible; this is a same-respondent descriptive bridge, not a causal population
panel.
The accompanying [attrition audit](data/htops-2025-panel-attrition-audit.json)
shows lower retention in lower-income, expense-difficulty, and baseline
food-insufficient cells, reinforcing the need for conditioning or a documented
longitudinal weight before population claims.
The [cross-lagged audit](data/htops-2025-cross-lagged-panel-audit.json) adds
baseline expense-pressure to later food, energy, job-loss, and Congress-
confidence cells, while keeping those associations separate from causality or
trust formation.

The [household financial-exposure finding](findings/us-cost-trust-politics-019.md)
adds the Federal Reserve 2025 savings, credit, linked credit-record, student-
loan, and retirement-account layers. It documents how liquidity buffers,
revolving balances, repayment strain, and long-run asset tapping are distinct
exposure channels; it does not treat them as a causal rate shock or as proof of
political response.

The next subgroup pass, [the material-to-institutional-judgment finding](findings/us-cost-trust-politics-020.md),
uses the retained April–June 2025 HTOPS respondents to show that expense
difficulty and confidence in Congress do not move through one uniform pattern
across income and race/ethnicity cells. It is a same-respondent descriptive
cross-lag with selection and attribution limits, not a causal hardship-to-trust
estimate.

The [real-wage and inflation finding](findings/us-cost-trust-politics-021.md)
adds a full-paper-audited NBER county study that separates price growth,
real-wage change, vote shares, margins, and turnout. The [stimulus and political
targeting comparison](findings/us-cost-trust-politics-022.md) adds an Italian
quasi-experimental transfer case as a mechanism comparison: consumption
targeting and electoral attribution can reward different recipient groups.
Neither comparison closes the US household-to-attribution-to-action arrow;
both sharpen the next US acquisition design.
The new [material-pressure political-translation finding](findings/us-cost-trust-politics-023.md)
consolidates the current HTOPS, ANES, and CPS boundary: material pressure can
coexist with different institutional judgments, persistence varies by measure,
and political identity and institution-specific trust must be kept separate
from action and vote mechanisms.

The new [synthetic-contact finding](findings/us-cost-trust-politics-026.md)
adds a controlled cultural/political encounter: an outgroup-representing AI
conversation increased immediate warmth and a costly choice of real
cross-partisan contact in preregistered online experiments, while the one-week
effect was small. The [source record](synthetic-contact-ai-source-record-v1.md)
and [public replication package](https://zenodo.org/records/20971465) preserve
the study-specific units, preprint status, and de-identified data/code boundary.
This is evidence about an intervention window, not durable depolarization,
electoral action, or population-scale political change.

The new [July expense-to-confidence finding](findings/us-cost-trust-politics-027.md)
adds a replicate-weighted same-round cross-tab to the material-to-institutional
judgment lane. Respondents reporting at least a little difficulty paying usual
expenses reported lower high confidence in federal statistical agencies and
Congress than respondents reporting no difficulty, while the two institutions
remain separate outcomes. The result is a cross-sectional association, not a
dated bill-to-trust pathway; the reproduction audit preserves the public-use
file hashes and successive-difference calculation.

The reader-facing [material-pressure to political-meaning synthesis](material-pressure-to-political-meaning-synthesis-v1.md)
puts the linked-panel follow-up cells, subgroup counterexamples, attrition
diagnostics, and institution-specific confidence boundary into one end-to-end
route. It shows material follow-up without automatic political translation and
defines the next event-level fields needed for attribution, action, remedy, and
recovery.

The [political-action menu synthesis](political-action-menu-not-ladder-synthesis-v1.md)
advances the next broad-program rotation. It keeps voting, contacting,
volunteering, information exposure, complaint, organizing, switching, and
withdrawal as distinct political responses with different resource and time
requirements.

## First working idea

People may judge the economy through the loss of choices—what they delay, stop, borrow for, or ask family to cover—not only through income. A policy can therefore change public feeling even after the direct money effect fades. This is a working idea, not a conclusion.

## Scope

- US households, customers, workers, voters, firms, and public institutions;
- prices, benefits, wages, debt, housing, health care, and energy;
- personal experience versus views of the national economy;
- differences by income, race, age, party, family type, and place;
- policy changes and firm behavior only where the timing and path can be checked.

## Writing rule

Use simple words. Say what changed, who felt it, what they did, and who they blamed. Do not call something “polarization,” “populism,” or “loss of trust” unless the survey or behavior measure shows it.
