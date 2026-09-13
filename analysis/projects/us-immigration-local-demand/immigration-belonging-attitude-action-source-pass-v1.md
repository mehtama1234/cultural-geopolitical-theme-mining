# Immigration, belonging, attitude, and action: source pass v1

**Checked:** 2026-09-13  
**Status:** direct respondent-level source layer; not joined to county conditions yet

## Why this pass exists

The place panel measures population change, housing pressure, crowding,
language access, vacancies, and service or sector capacity. Those indicators
describe context. They do not reveal whether residents interpret change as
opportunity, unfairness, loss of control, welcome, threat, or institutional
failure. This pass records the direct cultural-political sources needed for
that endpoint.

## Source map

| Source | Unit and coverage | Direct measures available | Safe use | Boundary |
|---|---|---|---|---|
| [Pew: immigration attitudes and the 2024 election](https://www.pewresearch.org/politics/2024/06/06/immigration-attitudes-and-the-2024-election/) | US adults/registered voters, April 8–14, 2024 | views of undocumented immigrants staying legally, party/election alignment, cultural and national interpretations | measure policy preference, identity alignment, and partisan meaning | national survey; not a county-level effect or causal estimate |
| [Pew: what would improve the immigration system](https://www.pewresearch.org/politics/2024/02/15/what-would-improve-the-u-s-immigration-system/) | US adults, January 16–21, 2024 | judgments of proposed border and immigration policies | compare preferred remedies and perceived institutional solutions | policy opinions do not identify the respondent’s local exposure or later action |
| [Pew: views of the US–Mexico border situation](https://www.pewresearch.org/politics/2024/02/15/how-americans-view-the-situation-at-the-u-s-mexico-border-its-causes-and-consequences/) | US adults, January 16–21, 2024 | perceived severity, causes, consequences, and preferred government response | measure attribution and legitimacy judgments | perceived cause is not verified cause; national border framing is not local experience |
| [Pew: immigrants and the US job market](https://www.pewresearch.org/short-reads/2024/10/21/most-us-voters-say-immigrants-no-matter-their-legal-status-mostly-take-jobs-citizens-dont-want/) | US registered voters, August 2024 | perceived labor-market complement/substitution and partisan differences | test economic attribution and consumer/worker narrative | perception is not an estimate of labor-market impact |
| [ANES 2024 Time Series Study](https://electionstudies.org/data-center/2024-time-series-study/) and its [user guide/codebook](https://electionstudies.org/wp-content/uploads/2025/05/anes_timeseries_2024_userguidecodebook_20250430.pdf) | US eligible-voter respondents in a national election study | immigration evaluations plus vote, ideology, trust, and political judgments; exact variables are now mapped below | build a respondent-level attitude-to-action record and, where supported, repeated/panel comparisons | do not publish a variable as measured until its wording, universe, missing codes, weights, and release are verified |

## What these sources let us separate

```text
local/material exposure (place panel)
  + personal contact and information (survey, if measured)
  -> perceived economic, cultural, or institutional effect
  -> attribution and fairness judgment
  -> belonging, threat, trust, or legitimacy
  -> policy preference, vote, contact, organizing, or withdrawal
```

The current source pass supports the middle and political endpoint at national
scale. It does not yet establish the complete arrow from a specific county’s
capacity conditions to a resident’s meaning or action.

## Extraction contract for the next data pass

For each respondent, preserve:

- survey wave, field dates, unit, weights, and missingness;
- immigration policy preference and perceived economic/cultural effects;
- perceived cause, responsible actor, fairness, and government competence;
- trust, identity, belonging, threat/opportunity, and social distance where
  directly asked;
- vote, turnout, contact, protest, volunteering, organizing, or other action;
- nativity, race/ethnicity, language, income, tenure, age, work, party, and
  geography only where the source supports them;
- whether the item is a reported belief, a reported action, or an externally
  measured condition.

The first join should be a contextual place crosswalk, not an invented causal
match: survey geography must be documented, and national respondents should
remain national respondents when no valid local identifier exists.

## Verified ANES 2024 variable map

The official codebook identifies a usable immigration battery in the
post-election interview. The variable names and response universes below are
now verified against the release documentation, but no estimates are claimed
here until the downloadable microdata or a reproducible SDA extract is
captured.

| Stage | Variable | Question or measure | Interpretation |
|---|---|---|---|
| Policy demand | `V242227` | whether permitted immigration levels should increase, stay the same, or decrease | desired scale of immigration |
| Labor attribution | `V242228` | likelihood that recent immigration takes jobs from people already here | perceived job competition |
| Crime attribution | `V242229`, strength `V242230`, summary `V242231x` | whether illegal immigration increases, decreases, or has no effect on US crime | perceived public-safety effect and intensity |
| Legal inclusion | `V242232` | favor/oppose/neither for a conditional path to citizenship for unauthorized immigrants | inclusion, deservingness, and policy boundary |
| Economic meaning | `V242235` | whether immigrants are good or bad for America’s economy | perceived aggregate economic effect |
| Cultural incorporation | `V242236` | importance of adapting to US customs and traditions | assimilation/integration norm |
| Institutional trust | `V241229` | frequency of trusting the federal government to do what is right | general institutional trust, not immigration-specific trust |
| Institutional attribution | `V241231`, `V241232` | whether government serves a few interests and whether it wastes tax money | perceived capture and competence |
| Political action | `V242066`, `V242067` | reported presidential turnout and candidate choice | post-election reported action |

The immigration battery is especially useful because it separates economic,
crime, legal-status, and cultural interpretations rather than collapsing them
into a single pro/anti-immigration score. `V242232` also has a documented
response universe for respondents who answer the favor/oppose question; its
strength follow-up was not yet available in the preliminary codebook and must
not be treated as an observed measure until the current release is checked.

The current ANES release page reports 5,521 pre-election completions and
4,964 post-election re-interviews, with fresh cross-sectional and
2016–2020–2024 panel components. It instructs analysts to use weights and
account for the complex sample design. The panel is therefore a potential
repeated-respondent route, but not every post-election immigration variable
automatically supports a within-person estimate.

## Acquisition result

The official release page exposes CSV, SPSS, Stata, syntax, codebook, and
questionnaire resources. The current environment can read the official web
documentation and codebook, but the direct CSV route returns a publisher web
challenge. Until the file is acquired or the same table is reproduced through
the official SDA interface, this remains a verified variable specification,
not an empirical immigration-attitude result.

## Counterexamples required

Keep at least four kinds of counterexample in the comparison:

1. high growth/capacity with welcoming or opportunity-oriented responses;
2. low measured local change with strong anti-outsider attribution;
3. capacity strain where residents blame institutions or ownership rather
   than newcomers;
4. strong policy attitude with no reported civic action, and civic action
   without a matching local material exposure.

## Current conclusion

Immigration is not one societal trend in this program. It is a bundle of
material, cultural, political, and consumer questions: who arrives; what
workers, firms, households, and public systems do; who bears costs; how people
attribute those costs; whether people feel they belong or retain control; and
what they then buy, avoid, vote for, organize around, or demand from the
state. The place panel and the respondent survey must remain separate until a
valid crosswalk and matching design are available.

## Next executable step

Acquire the ANES 2024 release files and codebook, identify the exact immigration,
trust, attribution, and action variables, document denominators and weights,
then add a small respondent-level extraction table. Do not claim a county
opinion estimate until geography and sample support it.
