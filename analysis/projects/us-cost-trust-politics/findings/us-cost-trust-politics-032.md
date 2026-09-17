# Finding 032: Household expense difficulty tracks loneliness and support gaps more than contact frequency

**Status:** provisional same-round HTOPS social-connection finding
**Checked:** 2026-09-17
**Field window:** March 13–30, 2026
**Unit:** responding person, conditioned on reported household expense difficulty

## The bounded finding

In the corrected March 2026 HTOPS public-use file, reported household expense
difficulty is associated with a steep gradient in frequent loneliness, low
social and emotional support, and food insufficiency. The association is much
less monotonic for talking by telephone or video with close people. This is a
useful cultural and social counterexample: material pressure appears related to
the perceived quality or adequacy of connection more clearly than to one simple
measure of contact frequency.

This is a weighted cross-sectional description, not a causal estimate. The
expense question refers to the household's usual expenses in the last two
months; loneliness and support are current respondent perceptions; food refers
to the last seven days; and telephone/video contact refers to a typical week.
Different clocks and constructs are kept visible.

## What was measured

The extraction used these corrected-vintage variables:

| Variable | Coding retained | Interpretation |
|---|---|---|
| `EXPENSE_DIFFICULT` | 1 not at all; 2 a little; 3 somewhat; 4 very difficult | Household material-room condition over the last two months |
| `SOC_LONELY` | 1 always; 2 usually; 3 sometimes; 4 rarely; 5 never | Current frequency of feeling lonely; “frequent loneliness” below is 1 or 2 |
| `SOC_SUPPORT` | 1 always through 5 never | Current frequency of receiving needed social/emotional support; “low support” below is 4 or 5 |
| `SOC_TALK` | 1 never/less than weekly; 2 one or two; 3 three or four; 4 five or more times weekly | Typical weekly telephone/video contact with close people outside the household |
| `FD_SUFF` | 1 enough desired kinds; 2 enough but not always desired kinds; 3 sometimes not enough; 4 often not enough | Household food sufficiency in the last seven days; “food insufficiency” below is 3 or 4 |

The primary `PWEIGHT` was used for point estimates. The corrected replicate
file contains `PWEIGHT1`–`PWEIGHT80`; its `SCRAMID` coverage exactly matches
the 12,521-row PUF, with no duplicate or missing IDs, and `PWEIGHT0` matches
the primary PUF weight exactly. Standard errors below use the 80-replicate
successive-difference calculation documented for the HTOPS extraction family:

```text
SE = sqrt(sum((replicate estimate - full-sample estimate)^2) / 80)
```

The estimates are respondent-weighted conditional shares. Because expense
difficulty is household-reported but the other outcomes are respondent
reports, this is not a household-level loneliness prevalence estimate.

## Weighted results

Percentages are weighted valid shares within each expense-difficulty category;
`n` is the unweighted number of respondents in the category. `SE` is in
percentage points. Each outcome has its own valid denominator because missing
or non-universe codes are excluded item by item.

| Expense difficulty | n | Frequent loneliness % (SE) | Low support % (SE) | 5+ weekly phone/video talks % (SE) | Food insufficiency % (SE) |
|---|---:|---:|---:|---:|---:|
| Not at all difficult | 7,061 | 1.768 (0.125) | 14.017 (0.606) | 28.256 (0.629) | 0.746 (0.160) |
| A little difficult | 2,869 | 5.780 (0.712) | 14.690 (0.798) | 29.519 (1.355) | 4.694 (0.503) |
| Somewhat difficult | 1,273 | 8.783 (1.404) | 23.577 (1.343) | 28.141 (1.896) | 15.472 (1.699) |
| Very difficult | 556 | 30.239 (2.447) | 40.872 (3.019) | 21.837 (2.308) | 33.578 (2.438) |

The descriptive pattern is large and internally differentiated. Frequent
loneliness rises from 1.8% among respondents reporting no difficulty to 30.2%
among those reporting very difficult expenses. Low social/emotional support
rises from 14.0% to 40.9%. Food insufficiency rises from 0.7% to 33.6%.
By contrast, reporting five or more weekly telephone/video conversations is
about 28–30% in the first three categories and falls to 21.8% in the very
difficult category. The contact measure therefore does not reproduce the
perceived-support gradient.

These are point-estimate gradients. The extraction does not present a formal
joint model, pairwise contrast test, or causal effect. The very-difficult cell
also has the smallest unweighted denominator, so its uncertainty is wider.

## Age-conditioned check

The pattern is not confined to one broad age composition. Conditioning the
same screen on respondent age gives the following point estimates (standard
errors in percentage points) for the two endpoint expense categories:

| Age band | Expense difficulty | n | Frequent loneliness % (SE) | Low support % (SE) |
|---|---|---:|---:|---:|
| 25–44 | Not at all difficult | 1,198 | 1.903 (0.288) | 14.729 (1.346) |
| 25–44 | Very difficult | 201 | 32.770 (3.969) | 37.921 (4.120) |
| 45–64 | Not at all difficult | 2,272 | 1.964 (0.274) | 16.621 (0.789) |
| 45–64 | Very difficult | 243 | 26.465 (3.017) | 47.434 (4.575) |
| 65+ | Not at all difficult | 3,591 | 1.457 (0.185) | 10.984 (0.676) |
| 65+ | Very difficult | 112 | 27.976 (4.608) | 35.687 (4.153) |

The direction persists in all three age bands, while the relative downstream
currency changes: frequent loneliness is highest in the 25–44 very-difficult
cell, whereas low support is highest in the 45–64 very-difficult cell. The
small endpoint cells have wider uncertainty. This is a subgroup-conditioned
descriptive check, not evidence that age modifies a causal expense effect.

## What this adds to the broad atlas

### 1. Social connection has multiple currencies

The results separate at least three social currencies:

1. **contact opportunity:** how often a respondent talks with close people;
2. **subjective connection:** whether the respondent feels lonely; and
3. **support adequacy:** whether the respondent gets the social and emotional
   support they need.

A person can have regular contact without feeling supported, or can have lower
contact without reporting frequent loneliness. Treating all three as one
“social isolation” score would hide the mechanism that matters.

### 2. Material pressure may narrow the quality of connection before it removes contact

The very-difficult expense group does not simply report zero contact. Its
five-or-more weekly contact share is lower than the other groups, but the
largest movements are in loneliness and support adequacy. This is consistent
with several possible mechanisms: stress can change how contact is experienced;
financial constraints can make help feel unavailable or humiliating; social
ties can be present but unable to supply material relief; or health, work,
housing, and family conditions can jointly affect both expense difficulty and
connection.

The file cannot distinguish these explanations. The finding is valuable
precisely because it rejects a simplistic contact-only account.

### 3. Food insecurity is a material counterpoint, not a proxy for loneliness

Food insufficiency tracks expense difficulty even more sharply than contact
frequency, but food and social measures use different reference windows and
units. Food hardship is not evidence of loneliness; loneliness is not evidence
of food hardship. Their co-occurrence identifies a candidate compound-burden
route that requires a timed design.

## What the finding does not establish

- Expense difficulty did not necessarily cause loneliness or low support.
- Loneliness did not cause expense difficulty.
- The PUF does not identify the bill, price, creditor, employer, family member,
  or public institution responsible for the household condition.
- It does not measure alternatives, borrowing, informal aid received, service
  denial, remedy, recovery, or later trust and political action.
- Contact frequency is not relationship quality, practical help, reciprocity,
  or the ability to obtain material assistance.
- Social/emotional support is a subjective adequacy measure, not a count of
  helpers or delivered support.
- The corrected March design is cross-sectional; it cannot be joined to the
  2025 longitudinal HTOPS design as if the respondents were the same panel.
- The estimates are not a nationally causal gradient and should not be pooled
  with the separate 2025 or July 2026 snapshots without harmonization.

## Counterexamples retained

- Some respondents reporting a little or somewhat difficult expenses report
  frequent contact at rates near or above the no-difficulty group.
- Some respondents with no expense difficulty report low support or loneliness;
  material room is not the only determinant of social experience.
- Very difficult expense respondents still include people with frequent
  telephone/video contact, showing that contact can persist while adequacy
  deteriorates.
- The largest food gradient does not prove that food hardship is the mechanism
  behind the social gradient.

## Next decisive test

The smallest stronger design would use a valid repeated respondent or event
record to follow:

```text
dated expense, food, energy, work, health, or housing shock
  -> available money, time, alternatives, and informal/formal support
  -> contact, loneliness, and support adequacy
  -> help requested and help delivered
  -> food/security, recovery, trust, community engagement, or exit
```

It should distinguish contact from practical help, identify whether help was
requested or forced, preserve the actor and remedy route, and measure later
change rather than one current state. A place or subgroup comparison can be a
useful intermediate test, but it should not be presented as the same-person
causal path.

## Reproducibility and storage boundary

The corrected March PUF ZIP was used only from temporary storage and was not
added to the repository. The archive was 19 MB compressed and had SHA-256:
`7bcd56139bf3997901db78dbf75f20f0aeb0fa919b188c2d5b6ae9350df9c6d1`.
The raw archive should be removed after handoff; the finding retains only the
variable definitions, row counts, alignment audit, weighted estimates, and
method boundary.

Sources:

- [Census HTOPS/HPS PUF listing](https://www.census.gov/programs-surveys/household-pulse-survey/data/datasets.html)
- [Corrected March 2026 PUF](https://www2.census.gov/programs-surveys/demo/datasets/hhp/2026/topical/HTOPS_HPS_2603_CSV.zip)
- [March 2026 HTOPS table listing](https://www.census.gov/data/tables/2026/demo/hhp/2603.html)
- [March 2026 HTOPS release note and weighting correction](https://www.census.gov/newsroom/press-releases/2026/htops-data-tables.html)

Machine-readable record: [`analysis/records/us-census-htops-social-connection-expense-march-2026.json`](../../../records/us-census-htops-social-connection-expense-march-2026.json).

Reproduction script: [`scripts/analyze_htops_2026_social_connection.py`](../../../../scripts/analyze_htops_2026_social_connection.py), including the age-band check.
