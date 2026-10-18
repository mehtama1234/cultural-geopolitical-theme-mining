# Cultural participation conversion stage audit

Status: fifty-sixth active depth artifact; checked 2026-10-18.

## Purpose

The cultural route asks what converts local supply, household room, identity,
and digital access into attendance, active creation, belonging, civic connection,
and repeat participation. This audit compares the available stages and keeps
survey populations, years, and methods separate.

## What we found

| Stage | Evidence | Signal | Boundary |
|---|---|---|---|
| Perceived local supply | U.S. Census HTOPS, July 2026 | 63.1% agreed that plenty of local arts/cultural opportunities existed | Perception is not venue inventory, affordability, transport, or accessible scheduling |
| Recent public attendance | Same HTOPS release | 20.5% attended live music, dance, or theater; 9.5% attended an art exhibit; 22.6% went to a movie in the prior four weeks | Attendance is not quality, belonging, repeat use, or causal access conversion |
| Household room | HTOPS income comparison | Live attendance ranged from 10.6% below $35,000 household income to 37.6% at $150,000 or more; loneliness ranged from 18.2% to 1.9% across those income groups | Income is not the only barrier; the arts and loneliness rows are not a same-person causal sequence |
| Active creation | HTOPS and ATUS | 17.9% reported creating/practicing/performing personal art in HTOPS; ATUS reports a long-run shift toward home-based and solitary creative activity | Private creation may be meaningful or socially connected; it is not equivalent to public attendance or civic action |
| Cultural identity and access | Creative Australia 2025 | Cultural-background arts engagement rose from 32% in 2022 to 40% in 2025; 49% of CALD respondents attended to engage their own background/community versus 32% of non-CALD respondents | Subgroup samples and general samples differ; cost, transport, language, and repeat use remain open |
| Cost and accessibility | Creative Australia and New Zealand 2025 | 60% named cost the biggest Australian barrier and 55% missed a wanted event because of cost; New Zealand reports 72% naming accessibility/convenience factors such as price, location, transport, or timing as enablers | Self-report does not identify the blocked event, actual price, or whether a subsidy would change attendance |
| Transaction gateway | Eurostat 2025 | 26.8% of EU people aged 16–74 bought event tickets online in the prior three months, up 3.8 percentage points from 2024; country shares ranged 11.4%–51.5% | Ticket purchase is not attendance, accessibility, affordability, repeat participation, or belonging |
| Civic conversion | NEA cross-survey analysis | Arts participation association with civic/community engagement was 4.86 incidence-rate ratio in the 2022 SPPA analytic sample, 1.17 in 2025 HTOPS, and approximately null overall in the 514-person GSS Arts Module sample (0.999) | Different samples and methods; the spread is evidence against a universal causal arts-to-civic effect |

The central result is a conversion gap: perceived supply and cultural identity
can be high while attendance, creation, and social connection remain uneven.
The strongest counterexample is not “culture has no effect”; it is that arts-to-
civic association changes sharply across compatible-looking analyses, while
private creation can rise or persist without proving public belonging or civic
action.

## Evidence ledger

| Arrow | Observed evidence | Missing decisive field |
|---|---|---|
| Supply → discovery/entry | Perceived supply and online ticket purchase | Venue inventory, price/fees, transport, disability/language access, and failed entry |
| Household room → attendance | Income gradients and cost barriers | Same-person budget, desired event, alternative, subsidy, and actual attendance |
| Identity → cultural connection | CALD/background-specific participation and attendance motives | Same-person identity, event setting, safety, recognition, and repeat behavior |
| Attendance/creation → meaning | Participation and reported arts engagement | Immediate meaning, companion/community, loneliness change, and wellbeing |
| Arts → civic connection | Cross-survey associations with a strong null counterexample | Person-level timing, prior networks, confounding, and later civic action |
| Participation → durable culture | Repeat-use questions and broad attendance measures | Ticket/attendance history, institutional response, creator livelihood, and exit |

## What this connects to

- **Household room:** price, transport, time, and care obligations turn cultural
  availability into unequal practical access.
- **Cultural identity:** participation may be a route to language, community,
  recognition, and belonging rather than a single attendance count.
- **Digital infrastructure:** ticketing and online cultural activity can widen
  reach while leaving physical, financial, and accessibility gaps intact.
- **Public legitimacy:** libraries, venues, festivals, and cultural programs are
  judged by whether people can enter and return, not only by supply claims.
- **Civic action:** cultural activity may correlate with civic connection, but
  the null and scale differences require a same-person design.

## Deeper question

**When does cultural access become shared belonging or civic connection, and
when does it remain private, occasional, or financially blocked participation?**

This is high learning value because the atlas has strong descriptive stages and
a real cross-survey reversal. It can be tested with one person/place episode
without treating attendance as a proxy for meaning or civic life.

## Bounded public discussion

The existing LinkedIn NEA discussion connects arts participation with civic
engagement and cultural-support policy. It is useful for the institutional
meaning layer, but it repeats report-level claims and is not independent
evidence of attendance, belonging, or civic action. Other bounded discussion
records in the atlas raise cost, access, identity, and local supply as practical
barriers; they remain interpretation rather than prevalence data.

## Challenge checks

- Perceived supply, ticket purchase, attendance, creation, belonging, and civic
  action were not collapsed into one participation rate.
- U.S., Australian, EU, and New Zealand populations and survey years were kept
  separate.
- The NEA association estimates were not treated as causal or universal; the
  GSS near-null comparison remains a counterexample.
- Home or solitary creation was not treated as social isolation or as a public
  civic benefit.
- Cost was not treated as the only explanation for nonattendance.
- Public discussion was used for meaning and policy interpretation only.

## Next test

Follow one person or place through:

```text
resources/identity/health/time | local supply | discovery and price/fees |
transport/accessibility | ticket purchase or non-use | shared attendance or
private/digital creation | companion/community | immediate meaning/belonging |
later loneliness/civic contact | repeat use/creator work | institutional response/exit
```

Require a dated activity or non-use episode, cost/access context, social
setting, immediate meaning, and later connection or repeat behavior. Preserve a
private-creation or nonparticipation counterexample before claiming cultural
activity produced belonging or civic action.

## Stopping rule

Do not call cultural participation belonging-producing, civic-building, or
socially isolating from supply, attendance, ticket purchase, creative activity,
survey association, or public discussion alone. Close this subtest only when
one compatible person/place episode links resources and access to social
setting, meaning, later connection, and repeat or exit behavior—or when the
source owner confirms those fields are unavailable.

## Source links

- [Cultural participation project](README.md)
- [Census HTOPS cultural supply](../../records/us-census-htops-arts-participation-community-supply-2026.json)
- [Census HTOPS arts, income, and loneliness](../../records/us-census-htops-arts-loneliness-income-2026.json)
- [NEA Great Connector](../../records/us-nea-great-connector-arts-civic-community-engagement-2026.json)
- [ATUS arts time use](../../records/us-ufl-ucl-arts-engagement-time-use-2003-2023-2026.json)
- [Creative Australia arts participation](../../records/comparative-creative-australia-national-arts-participation-2025-cultural-background-cost.json)
- [Eurostat online event tickets](../../records/comparative-eurostat-online-event-ticketing-2025-cultural-consumer-gateway.json)
- [Shared cultural participation bridge](shared-cultural-participation-civic-conversion-bridge-v1.md)
- [NEA public discussion](../../social-discussions/records/social-great-connector-arts-linkedin-001.json)
