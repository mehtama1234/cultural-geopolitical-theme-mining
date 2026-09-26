# External-data first pass: fragmented civic authority

**Checked:** 2026-09-25  
**Status:** provisional source-led trend/subtheme input  
**Scope:** U.S. social, cultural, and political life  
**Question:** Are Americans experiencing civic life as one shared institutional
system, or through different combinations of national institutions, local
communities, media, religion, and online sources?

The current BLS [Job Flexibilities and Work Schedules release](https://www.bls.gov/news.release/flex2.htm)
adds a U.S. labor-control baseline to the broader material-to-household route:
57% of wage-and-salary workers could vary start and stop times in 2024–25, 69%
said taking an hour or two off during work hours was not difficult, and 9% knew
their schedules one day or less ahead. Parents with children under 18 were more
likely to work at home, while lower-education workers were more likely to face
short notice. These are weighted descriptive statistics, not causal evidence
that flexibility improves care or household welfare.

## Why this is the first pass

This pass starts with external data and lets the recurring structure emerge
from the sources. It does not treat any one survey as a national theory, and it
does not combine the samples into one estimate.

## Source observations

### 1. Institutional confidence is low and politically conditional

Gallup's June 1–15, 2026 poll reports that average confidence in 14 major U.S.
institutions was 27%, near the historical low and below 30% for the fifth
straight year. Confidence in large technology companies fell to 20%, a new low
in that series. The party differences are large for several institutions: for
example, confidence in the presidency was 74% among Republicans, 19% among
independents, and 4% among Democrats; confidence in higher education was 23%,
38%, and 50%, respectively.

**Measured stage:** reported institutional confidence, by institution and
partisanship.  
**Not measured:** whether low confidence changes a specific person's use,
political action, switching, or exit.

The existing machine-readable [Gallup institutional-confidence
record](records/us-gallup-institutional-confidence-2026.json) preserves the
institution-specific and party-conditioned denominators separately. The key
comparison is not simply “trust is falling”: confidence remains much higher in
some institutions than others, and party control strongly conditions judgments
of institutions such as the presidency. Low confidence can therefore coexist
with continued dependence or use.

### 2. Civic engagement is segmented, not one-dimensional

Pew Research Center's July 9–December 5, 2025 study used a cluster analysis
of 19 questions covering political activity, civic involvement, religious
attendance, and attention to news. It identifies four engagement groups:
Mobilizers, Connectors, Spectators, and Outsiders. The groups are not one
political ladder: each is politically mixed, while the practical participation
profiles differ sharply.

Among the groups, reported 2024 voting was 87% for Mobilizers and Connectors,
49% for Spectators, and 41% for Outsiders. Contact with an elected official
was 65%, 13%, 7%, and 3%, respectively; volunteering was 77%, 42%, 17%, and
13%. Monthly religious attendance was 45%, 43%, 25%, and 24%. Pew's companion
panel comparison finds federal-government trust low across all four groups
(17%–22%), while national-news trust varies more (45% among Outsiders versus
62% among Mobilizers).

**Measured stage:** distinct combinations of participation, attention, and
information trust.  
**Not measured:** a dated pathway from hardship or institutional treatment to
membership in one group, or whether group membership produces later political
action.

The machine-readable source record is [Pew's public-life engagement-group
record](records/us-pew-public-life-engagement-groups-2025.json). It keeps the
cluster assignment, group-level behavior, federal-government trust, news trust,
and perceived-fairness measures separate.

### 3. The current Census data release creates a useful social-capacity surface

The Census Bureau's July 2026 HTOPS release, collected July 15–August 3,
contains tables on arts participation and availability, loneliness, social and
emotional support, telephone/video/in-person interaction, community engagement,
and trust in health information from doctors and artificial intelligence. It
also reports household economic, health, and employment measures in the same
release.

**Measured stage available for follow-up:** social connection, cultural
participation, community engagement, and source-specific information trust by
selected characteristics.  
**Not measured by the release description alone:** whether participation or
support protects a particular household from a later shock, or whether trust
produces institutional use, political action, or exit.

### 4. Social support and participation vary sharply by age

The downloaded HTOPS tables provide an initial descriptive measurement rather
than only a list of available topics. In the July 15–August 3, 2026 release:

| Measure | Total adults | 18–34 | 35–49 | 50–64 | 65+ |
|---|---:|---:|---:|---:|---:|
| Always/usually obtain social-emotional support | 61.8% | 47.8% | 59.5% | 66.4% | 76.1% |
| Never obtain social-emotional support | 9.6% | 6.8% | 13.7% | 10.6% | 7.7% |
| Attend religious services 12+ times/year | 25.9% | 16.9% | 24.9% | 27.8% | 35.7% |
| Attend clubs/organizations 12+ times/year | 13.8% | 9.6% | 13.0% | 13.5% | 20.1% |
| Attend live music, dance, or theater in past 4 weeks | 20.5% | 22.5% | 21.8% | 18.9% | 18.3% |
| Went to the movies in past 4 weeks | 22.6% | 23.5% | 32.1% | 18.3% | 15.8% |

These are population estimates calculated from the published count columns;
they are rounded to one decimal place. The support and organized-participation
measures point in the same broad direction: older adults report more regular
support and formal participation. Cultural consumption is different: younger
adults report slightly more live-performance attendance, while the highest
movie attendance is among adults 35–49.

### 5. Domain-specific authority is not the same as general institutional trust

In the same HTOPS release, 65.7% of adults report “a great deal” or “quite a
lot” of trust in health information from a doctor, compared with 15.2% for AI
tools. Doctor trust is highest among adults 65+ at 72.1%; AI trust is highest
among adults 50–64 at 17.1% and lowest among adults 65+ at 12.5%.

This does not show that AI is replacing doctors. It does show that the
authority question is domain-specific and age-differentiated: low national
institutional confidence cannot be used as a proxy for every source of
practical authority.

**Census limitation:** the Bureau labels these estimates experimental and
warns that subgroup estimates may have small sample sizes and large standard
errors. The percentages are descriptive; they are not tests of age effects or
causal explanations.

The machine-readable source record is [the HTOPS social-support and authority
record](records/us-census-htops-social-support-community-authority-2026.json).
It preserves the published denominator, age percentages, workbook hashes,
standard-error download links, and the descriptive boundary.

## Provisional recurring subtheme

### Fragmented civic authority

The three source families point toward a bounded subtheme: Americans may not be
relating to “institutions” as one unified trust system. Instead, civic meaning
and practical judgment may be distributed across national institutions, local
communities, peer and media networks, religious participation, online sources,
and domain-specific authorities such as doctors or AI systems.

This is an **inference across sources**, not a directly measured causal result.
The evidence supports three narrower claims:

1. aggregate institutional confidence is persistently weak;
2. confidence differs sharply by institution and partisan identity; and
3. civic/news/religious participation forms multiple engagement profiles whose
   action and information-trust patterns differ; and
4. social support and formal participation are age-structured in the current
   HTOPS release, while cultural activity has different age gradients by form.

The stronger claim—that fragmented authority is changing political behavior or
legitimacy—remains open.

The first Census measurement and the Pew profiles slightly refine the subtheme.
They suggest that
fragmentation may involve at least two different structures:

- **social-capacity stratification:** regular support and formal group
  participation are much more common among older adults than younger adults;
- **authority specialization:** practical trust is high for doctors, low for
  AI, and varies by age rather than tracking a single generalized trust level.

The arts results also caution against a simple “older people participate more”
story: cultural activity has different age gradients depending on the form of
participation.

### 6. Kindness is a visible social capacity, but its conversion is uneven

Gallup's March 2–18, 2026 Values in Action survey finds that 60% of adults
often or very often see people treating others with kindness and respect, and
65% experienced an act of kindness in their community many or a few times in
the prior week. Yet only 52% are very comfortable initiating a kind act toward
a stranger; that share is 64% among adults 65 and older, 49% among adults
30–49, and 35% among adults 18–29.

The conditional pattern is useful but bounded: roughly 80% of people who
received kindness many times in the prior week are very comfortable initiating
it, compared with 54% among those receiving it a few times and under 40% among
those receiving it once or not at all. The relationship may indicate
reciprocity, but it may also reflect sociability, safety, local opportunity,
or a generally positive outlook. The survey is cross-sectional and does not
observe actual help delivered, adequacy, institutional response, or later
civic action.

This adds a distinct social-capacity subtheme: interpersonal kindness can be
common without equal confidence to initiate it. Exposure may be a conversion
condition, but age and recent-exposure gaps show that the capacity is unevenly
distributed. The machine-readable [Gallup kindness and reciprocity
record](records/us-gallup-kindness-observation-reciprocity-2026.json) keeps
exposure, initiation comfort, perceived national kindness, and the causal
boundary separate.

### 7. Corruption perception is a broad legitimacy signal, not an audit

Gallup's September 2, 2026 World Poll release reports that 89% of U.S. adults
say corruption is widespread in government, up from 79% in 2025 and 73% in
2024. The perception is broad across parties: 91% of Democrats, 90% of
independents, and 83% of Republicans say corruption is widespread. Gallup also
reports that 71% see corruption as widespread in business, leaving an
18-point government-versus-business perception gap.

The cross-national comparison adds context but not a causal explanation. In
the closest comparable 2025 year, the U.S. estimate was 79% versus a 59% OECD
median. These are public perceptions, not verified corruption events,
administrative findings, or bribery exposure. The partisan convergence may
reflect shared alarm while still arising from different experiences, party
control, information, or expectations of government.

This sharpens the fragmented-authority subtheme: public legitimacy may be
weakening through a perception that the state is broadly compromised, even
while the public does not necessarily transfer trust to business or private
alternatives. The machine-readable [Gallup government-corruption perception
record](records/us-gallup-government-corruption-perception-2026.json) keeps
trend, party, government/business, and OECD comparisons separate.

### 8. Economic-system labels are separating from firm legitimacy

Gallup's August 3–24, 2026 Poll Social Series finds that 43% of adults view
socialism positively, compared with 55% for capitalism, 77% for free enterprise,
95% for small business, and 35% for big business. The pattern is strongly
structured: adults ages 18–34 rate socialism more positively than capitalism
(57% versus 43%), while adults 55 and older show the reverse (34% versus 65%).
Among independents, socialism rose to 45% while big-business favorability fell
to 32%; among Democrats, socialism was 65% and capitalism 35%; among
Republicans, socialism was 14% and capitalism 75%.

The key insight is not a simple move from markets to socialism. Small business
remains nearly universally popular, and free enterprise remains broadly
positive. The more bounded reading is selective dissatisfaction with large
firms and the distributional or moral meanings attached to capitalism, with
different age and party vocabularies. These are label favorabilities, not
policy platforms, voting, employment, spending, or observed firm conduct. The
machine-readable [Gallup economic-concepts and market-legitimacy
record](records/us-gallup-economic-concepts-market-legitimacy-2026.json) keeps
overall, party, age, and repeated-trend surfaces separate.

### National frustration can coexist with stronger local democratic ratings

The 2026 Gallup/Kettering Democracy for All survey adds a political-legitimacy
layer. Fifty-six percent of U.S. adults said national democracy was doing very
or moderately poorly, compared with 19% who said it was doing well. Only 28%
trusted that political leaders would be held accountable to the laws and
Constitution. Yet the local referent was less negative: 34% rated democracy in
their own city or town positively and 21% negatively.

This does not prove that people are transferring legitimacy from national to
local institutions. It establishes a testable contrast: national democratic
performance judgments and local democratic judgments are not identical. Local
leaders, neighbors, and concrete community experience may be potential sources
of legitimacy even while national institutions are judged poorly.

The machine-readable [Gallup/Kettering democracy record](records/us-gallup-kettering-democracy-local-national-legitimacy-2026.json)
keeps the overall sample, measures, methodology, and access boundary visible.

### Participation also has an interface and invitation problem

A separate Gallup/Kettering study of more than 20,000 Americans is a useful
counterexample to a simple time-scarcity explanation. Sixty-nine percent
reported at least some regular free time, and among adults with at least six
hours of free time on weekdays or weekends, 31% participated in community
improvement activity, 35% wanted to but did not, and 34% did not want to.
Among would-be participants with ample free time, 54% said they were unsure how
to get involved and 51% said they had not been invited or encouraged. Work and
family obligations were reported at nearly the same rate by would-be
participants (46%) and actual participants (45%).

This suggests a further subtheme: **civic capacity requires a usable entry
route**. Time is one constraint, but information, invitation, welcome, and a
credible belief that participation matters may determine whether available time
converts into action. The result is descriptive and self-reported; it does not
prove that an invitation would produce participation.

The [community-involvement record](records/us-gallup-community-involvement-information-invitation-2026.json)
preserves this counterexample separately from the democratic-legitimacy survey.

### Material pressure does not translate into one uniform trust response

The existing linked HTOPS record provides a more direct conversion test. It
joins April 15–29, 2025 reported expense difficulty to June 16–25, 2025
Congress confidence for retained respondents, with 80 successive-difference
replicate weights. The relationship is subgroup-conditioned rather than
monotonic: among respondents below $25,000, high Congress confidence was 27.1%
when any expense difficulty was reported and 26.1% when no difficulty was
reported; among respondents at $75,000–$99,999, the corresponding values were
13.5% and 20.8%. Among Black respondents, the difficulty group was higher
(19.9% versus 12.6%), while among White respondents it was lower (12.8% versus
15.9%).

This is a useful counterexample to a simple material-pressure-to-distrust
story. Expense difficulty, identity, prior political judgment, and institutional
meaning may interact differently across groups. The [HTOPS material-to-trust
subgroup record](records/us-htops-material-trust-subgroups-2025.json) preserves
the linked sample and replicate-weight uncertainty; it is not an
attrition-adjusted national panel or a causal estimate.

### Party labels conceal value-based coalition differences

Pew's 2026 political typology supplies a separate cultural-political layer. It
classifies 10,357 adults into nine groups using 30 questions about government,
economics, immigration, social values, national identity, and foreign policy.
The two highly ideological right-anchor groups represent 21% of adults and the
two highly ideological left-anchor groups 17%, while the Unconventional Right
is 23%, the Order and Opportunity coalition is 18%, and a Tuned-Out Middle is
9%.

Within the right, views also vary: support for making abortion illegal in most
or all cases is 83% among Faith and Flag Conservatives, 73% among the No
Apologies Right, 46% among Pragmatic Right identifiers, and 43% among the
Unconventional Right. In foreign-policy terms, 71% of adults say it is at
least somewhat important for the U.S. to be the world's only military
superpower, while 62% say the U.S. should consider allies' interests even when
that requires compromise.

The implication is not that nine groups replace party identity. It is that
party labels are an insufficient shortcut for cultural meaning, coalition
boundaries, or geopolitical preference. The [Pew coalition-typology
record](records/us-pew-political-typology-values-coalitions-2026.json) keeps
these cluster-derived comparisons separate from behavior, turnout, and policy
effects.

### Religion can regain salience without a mandate for direct electoral control

Pew's April 6–12, 2026 American Trends Panel survey of 3,592 adults adds a
religion-and-public-life layer. Thirty-seven percent said religion is gaining
influence in American life, up from 18% in February 2024, while 61% said it is
losing influence. Fifty-five percent had a net positive view of religion's
influence, but the partisan split was 75% among Republicans and Republican
leaners versus 38% among Democrats and Democratic leaners.

The boundary is important: 79% said houses of worship should not endorse
candidates and 66% said they should keep out of day-to-day political matters.
At the same time, familiarity with the term Christian nationalism rose from
45% in 2024 to 59% in 2026, while 17% favored declaring Christianity the
official religion. This supports **religious salience with constrained
institutional mandate**, not a single religious-political realignment. The
[Pew religion/public-life record](records/us-pew-religion-public-life-church-state-2026.json)
keeps perceived influence, normative boundaries, partisan meaning, and
church-state preferences separate from participation, mobilization, policy, or
vote outcomes.

Gallup supplies a needed subgroup counterexample to a simple national decline
story. In its 2024–2025 biennial aggregates, 42% of men ages 18–29 said
religion was very important, up from 28% in 2022–2023 and near the 43% recorded
in 2000–2001. Young women were at 29%, while young-men monthly-or-more service
attendance reached 40% versus 39% among young women. Young men's religious
affiliation was 63% versus 60% among young women.

The bounded insight is **aggregate religious decline can contain a
young-men/gender reversal**, with importance, attendance, and affiliation moving
as separate currencies. Gallup's biennial repeated cross-sections do not show
whether the reversal persists, what causes it, or whether it produces
congregational growth, political mobilization, or civic action. The [Gallup
young-men religiosity record](records/us-gallup-young-men-religiosity-gender-reversal-2024-2025.json)
preserves the subgroup and measurement boundaries.

### Material strain can weaken efficacy while preserving conditional willingness to act

CIRCLE and When We All Vote's January–February 2026 survey of 5,549 adults ages
18–29 adds a younger-person conversion surface. Sixty percent reported
sometimes or often having trouble meeting basic needs. Among financially
struggling youth, 64% said their vote did not matter, compared with 53% among
financially stable youth; life satisfaction was 57% versus 88%. Housing and
utilities were the top reported economic concern at 66%, followed by groceries
and everyday items at 62%.

The same source reports that struggling youth were more likely to say they
would participate when their voice mattered, communities changed, and
candidates followed through. This is a useful boundary: hardship can reduce
perceived efficacy without eliminating willingness to act when a credible route
to results exists. It is not evidence that hardship caused nonvoting, and the
survey does not observe the eventual 2026 vote or a later institutional
response. The [CIRCLE youth financial-strain record](records/us-circle-youth-financial-strain-political-engagement-2026.json)
keeps the conditional participation result separate from the material and
well-being measures.

### Cultural-loss anxiety is not the same thing as democratic-performance approval

PRRI's May 1–18, 2026 American Identity Survey adds a cultural-meaning layer to
the legitimacy pattern. Sixty-eight percent said the country is in real danger
of losing important democratic rights and freedoms, while 29% said those rights
will remain protected. At the same time, 60% said America is in danger of
losing its culture and identity, only 18% were extremely or very proud of how
democracy is working today, and 51% were extremely or very proud of being
American.

The economic and generational layer is also distinct: 49% said the American
Dream still holds true, down six points from 2024, while only 36% of adults
ages 18–29 agreed. This suggests a bounded subtheme of **threatened rights,
contested cultural continuity, and weakening mobility confidence**—three
perceptions that can travel together but should not be treated as one latent
attitude or as evidence of objective institutional decline. PRRI reports these
measures across party, religious, Christian-nationalism, and age groups, but
the survey does not establish causes, later action, or actual changes in rights,
culture, mobility, or democratic performance. The [PRRI identity and rights
record](records/us-prri-american-identity-democratic-rights-culture-2026.json)
keeps those surfaces separate.

### Civic reach can rebound while the time intensity of participation thins

The Census Bureau/AmeriCorps 2023 Civic Engagement and Volunteering Supplement
adds a population-level conversion boundary. Formal volunteering rose from
23.2% in 2021 to 28.3% in 2023, and informal help or exchange of favors with
neighbors rose from 51.7% in 2019 to 54.2% in 2023. But among formal volunteers,
mean annual hours fell from 96.5 in 2017 to 70 in 2023, while median hours fell
from 40 to 24. Eighteen percent of formal volunteers served fully or partly
online; those volunteers reported 95 mean hours versus 64 among in-person-only
volunteers.

The bounded insight is **civic reach and civic depth can move in opposite
directions**. More people may enter formal or informal routes while the average
time available per participant becomes thinner, more flexible, or differently
composed. These are repeated cross-sectional estimates, not matched-person
change: they do not show who reduced hours, why, whether online work replaced
travel, or whether service was adequate or sustained. The [Census/AmeriCorps
civic reach and time record](records/us-census-americorps-civic-reach-time-2023.json)
keeps formal volunteering, neighbor help, online participation, and time
intensity as separate measures.

### Social trust is a conversion condition, not proof of institutional performance

Pew's March 2025 American Trends Panel survey provides a tighter same-survey
bridge. Among 9,482 U.S. adults, 26% said they knew all or most of their
neighbors, 59% had a neighbor they would feel comfortable asking to keep
emergency keys, 76% said they would likely bring in mail or water plants for an
out-of-town neighbor, and 72% said they would likely conserve water or
electricity if asked by a public official. Among Pew's generalized-social-
trust groups, the corresponding willingness to help a neighbor was 82% for
trusters versus 67% for distrusters; willingness to conserve after a public
official's request was 78% versus 64%.

This closes a small but important middle arrow: **social trust is associated
with stated cooperative capacity across both interpersonal and public-request
contexts**. It does not show that trust caused willingness, that a public
request occurred, or that anyone actually complied or received adequate help.
The [Pew neighbor-trust/public-request record](records/us-pew-neighbor-trust-public-request-2025.json)
keeps the same-survey association separate from observed civic action,
institutional performance, and later political behavior.

### Communal infrastructure can convert ties into action while preserving unequal access

Pew's 2023–24 Religious Landscape Study supplies a counterexample to treating
community participation as only an invitation deficit. Among 565 current
Latter-day Saint respondents, 72% reported volunteering in the prior year,
compared with 41% of U.S. adults overall, and 48% said most people can be
trusted, compared with 34% overall. But volunteering was 91% among members with
a bachelor's degree or more versus 61% among those with less education, and
80% in the Mountain region versus 62% elsewhere in the country.

The bounded insight is **community infrastructure can convert belonging into
reported action without equalizing who participates or who benefits**. The
source does not identify whether volunteering was congregational, how many
hours it required, whether it was burdensome, or whether it produced political
influence or durable belonging. The [Pew communal-trust and volunteering
record](records/us-pew-latter-day-saints-communal-trust-volunteering-2026.json)
therefore functions as a structured counterexample, not a causal estimate or a
general religious-community effect.

Gallup adds a third distinction: national institutional confidence is a
political and institution-specific judgment, not a universal measure of whether
people have usable local, professional, cultural, or digital authorities. The
working subtheme is therefore better stated as **plural authority under weak
shared national confidence**.

## Conversion map: what the external data now supports

| Stage | Evidence now available | What remains open |
|---|---|---|
| Social connection and generalized trust | Pew's neighbor survey links social-trust classification to stated neighborly help and willingness to respond to a public conservation request. | Actual request, compliance, assistance delivered, adequacy, and later trust change. |
| Usable entry route | Gallup/Kettering reports information, invitation, and efficacy barriers among people who say they want community involvement; Census/AmeriCorps shows formal and informal participation reach. | Whether a specific invitation or information route produces participation for the same person. |
| Communal infrastructure | Pew's Latter-day Saint comparison shows high reported volunteering and generalized trust with internal education and regional gaps. | Role access, hours, burden, recipient, institutional response, and durable belonging. |
| Reported civic action | Pew's engagement profiles distinguish voting, volunteering, group/religious participation, and contact with elected officials; federal trust remains low across all four profiles. | The dated trigger, attribution, material context, and later institutional response for the same respondent. |
| Congressional contact and perceived responsiveness | Ohio State IDEA's 2025 survey finds 21.7% reporting recent congressional contact, 72.1% saying people like them would like to discuss important issues with Congress, and 40.5% of noncontact respondents saying members do not care about concerns like theirs. | Verified contact, office response, issue resolution, satisfaction, and whether a credible two-way channel changes later action or trust. |
| Deliberative interaction and downstream response | Two randomized Ohio State field experiments with Members of Congress measured real-time online town halls, post-session trust/approval, policy agreement, voting intention, and a post-election vote report; Study 2 reports approximately +11% of scale for trust and approval, +10.5 points in vote intention, and +13.1 points in reported vote. | Contemporary generalization, ordinary constituent contact, response outside a selected interaction, durability, and whether the office resolves a constituent problem. |
| Local agency versus national confidence | Trust for Civic Life's small returning subset reports falling national political trust while local agency and belonging hold steady. | Representative coverage, attrition-adjusted change, delivered local outcomes, and whether local agency transfers into national or political action. |

The end-to-end insight is deliberately modest: **civic conversion is layered
rather than linear**. Social trust may support stated cooperation;
organizations may create routes into reported action; and local agency may
remain usable while national confidence weakens. No current source closes the
full chain from a dated social condition through invitation or institutional
encounter to actual action, response, recovery, and durable trust for the same
person. That open middle is the next acquisition target.

### Contact willingness can coexist with low expected institutional payoff

Ohio State's Institute for Democratic Engagement and Accountability survey of
1,001 adults, fielded August 20–October 2, 2025, adds a congressional-contact
surface. About 21.7% reported contacting or trying to contact a House or Senate
member in the prior year, while 72.1% agreed that people like them would like
to discuss important issues with Members of Congress. Among respondents who had
not contacted a member, 40.5% said members do not care about concerns like
theirs, 37.1% said contacting was too difficult, 34.7% expected members would
not change their minds, and 21.7% cited time cost. Although 64.9% said their
representatives were at least somewhat interested in what they had to say, only
14% trusted Congress to do what is right most of the time.

This adds a concrete **voice-to-payoff gap**: interest in speaking is much
larger than observed or reported contact, and perceived listening is not the
same as trust, response, or issue resolution. The [IDEA constituent-engagement
record](records/us-osu-idea-constituent-engagement-responsiveness-2025.json)
keeps the full sample, noncontact subgroup, and contacted subgroup separate;
the survey does not verify contacts or observe office responses.

### A real two-way interaction can move trust and political behavior—but only under bounded conditions

Ohio State's randomized field experiments provide the strongest causal bridge in
this first pass. In 2006, 1,259 people who had expressed willingness to join an
online town hall were randomly assigned to a deliberative session with one of
12 Members of Congress or to an information-only condition. The design used
pre-session, post-session, and post-election surveys, and separated policy
agreement from trust, approval, and vote outcomes. A second study in 2008
assigned 462 of 900 participants around a session with Senator Carl Levin; 175
attended. The study reports approximately 11% of the measurement scale in
increased trust and approval, a 10.5-point increase in vote intention, and a
13.1-point increase in reported post-election vote, with the last estimate
weaker statistically (P=0.073).

This closes the chain **assigned two-way interaction → trust/approval →
political behavior** for a selected experimental population. It does not close
ordinary constituent contact → office response → issue resolution, and it is
not evidence that today's digital town halls would have the same effects. The
[congressional town-hall field-experiment record](records/us-osu-congressional-townhall-field-experiment-trust-vote-2006-2008.json)
keeps causal exposure, attendance, participant selection, follow-up timing, and
generalization limits explicit.

### Telephone town halls separate procedural satisfaction from representative trust

A related field experiment with four Members and eight telephone town halls
enrolled 1,005 constituents and analyzed 222 people who completed both pretest
and posttest. Participation improved evaluations of the telephone-town-hall
platform by about 6% of the response scale and trust/approval of the Member by
about 4%. A modified format—one topic plus nonpartisan briefing materials—added
about 5% of the response scale to evaluations of the forum, but did not
significantly improve Member attitudes relative to the standard format. The
[telephone-town-hall record](records/us-osu-telephone-townhall-field-experiment-platform-member-trust-2019.json)
therefore adds a useful distinction: better deliberative design can improve
procedural experience without automatically producing stronger representative
trust. The high attrition, self-selection, all-Democratic-Member setting, and
absence of a true no-event control keep this as bounded causal evidence rather
than a current prevalence estimate.

### Office response can be measurable without proving substantive representation

Kreps and Kriner's randomized 2020 audit sent 32,398 policy emails to state
legislators, alternating human-written and GPT-3-generated messages across six
issues and ideological directions. Offices responded to 17.3% of human-written
emails and 15.4% of machine-generated emails: a statistically significant but
small 1.9-point gap. Median reply length was 322 words for human messages and
272 for machine messages, with nearly identical interquartile ranges. This
adds a concrete **message-to-office-response** layer, while also showing why
response is not the same as receipt, substantive answer, policy influence, or
issue resolution. The [AI constituent-email record](records/us-cornell-ai-constituent-email-legislative-response-2020.json)
keeps the state-legislator scope, deceptive-audit design, issue variation, and
federal-generalization boundary explicit.

### Political-resource cues can change the quality of access before any policy response

Kalla and Broockman's randomized field experiment sent otherwise identical
meeting requests to 191 House offices, describing prospective attendees either
as local constituents or as local campaign donors. Meetings with a Member or
Chief of Staff occurred for 2.4% of constituent-described requests versus 12.5%
when donor status was revealed. Access to any senior staffer was 5.5% versus
18.8%, and every scheduled meeting was confirmed as occurring with the promised
office representative. This adds a **resource cue → access seniority** layer
before response or policy influence. The [congressional-access record](records/us-kalla-broockman-campaign-donor-congressional-access-2013.json)
keeps the randomized office unit and organized-advocacy setting explicit: it
does not show that donor access produced a legislative result or that every
ordinary constituent lacks a route to staff.

### Equal routine reply rates do not erase unequal access or unequal outcomes

Carnes and Holbein's four randomized correspondence experiments sent routine
casework requests to state legislators, public school principals, and mayors.
Across 4,492 messages, less-affluent-coded senders received replies 16.6% of
the time versus 15.8% for more-affluent-coded senders; the pooled difference
was not statistically significant, and the 95% interval ruled out a class bias
larger than 1.32 percentage points. The [casework-class record](records/us-carnes-holbein-casework-social-class-response-2012-2013.json)
is a useful counterexample to a single “rich always get better response” story.
It does not negate donor-based access differences, demographic disparities,
unequal ability to formulate a request, or unequal resolution after a reply.

### Credible district information can move a legislator's actual vote

Butler and Nickerson surveyed 10,690 New Mexico voters about spending proposals,
sent district-specific results to a randomly selected half of the 70-member
state House, and observed a subsequent tax-rebate vote. The treated legislators'
votes tracked district opinion strongly while the control relationship was near
zero (rho = -0.07). In the raw vote table, 84.4% of controls voted yes versus
68.6% of treated legislators, with effects concentrated in districts where
support for the spending proposal was low. The [constituency-information
record](records/us-butler-nickerson-constituency-information-legislative-vote-2008.json)
closes an information → legislative-vote arrow, but not contact → information,
vote → implementation, or vote → household benefit.

### The vote was followed by statutory program design, not yet verified household receipt

The same New Mexico episode can be extended one step with official legislative
records. Senate Bill 24 enacted a refundable personal-income-tax credit for
eligible 2007 tax filers, with filing-status, income-band, and dependent-based
amounts, plus an administrative appropriation. The Legislative Council Service
described the final package as less than $60 million and noted the chapter's
refundable-credit structure. The [SB24 vote-to-implementation record](records/us-new-mexico-sb24-vote-to-refundable-credit-implementation-2008.json)
therefore closes **vote → enacted program design** for a named episode. It does
not show claims, payment timing, take-up, adequacy, household relief, or that
the constituency-information treatment caused enactment.

### The enacted credit had a projected distribution route, but not realized receipt data

The New Mexico Legislative Finance Committee's August 2008 fiscal-impact report
adds an administrative planning layer. Using Taxation and Revenue Department
information, it estimated 786,500 eligible returns, $87.6 million in total
benefits, an average benefit of $111, and roughly 20% of filers excluded by
income thresholds. It specified refund-versus-liability-reduction routes,
systems work, mailed checks, outreach, and a highlighted tax form. These are
projections and plans—not observed claims, checks, timing, take-up, or household
relief. The [SB24 fiscal-impact record](records/us-new-mexico-sb24-fiscal-impact-planned-distribution-2008.json)
therefore extends the chain to **enacted rule → planned administrative route**
while keeping realized receipt open.

### Local agency can remain usable while national political trust falls

The Trust for Civic Life's October 2025 survey of people reached through 24
rural Civic Hub networks reports 70% average trust in local organizations,
90% saying they personally have power to make a positive difference where they
live, and about 75% saying neighbors and local organizations can come together
to solve problems. Only 11% said national leaders ensure their voice matters.
Among the small returning subset shown in the report, national political trust
fell 46% from fall 2024 to fall 2025 while local trust, agency, and belonging
held steady.

This sharpens the scale distinction into **local usability without national
political confidence**. It is not a representative rural estimate: respondents
were recruited through participating networks, and the returning comparison is
reported for only 90 people without a full attrition-adjusted panel design.
Local agency may reflect selection into community networks, familiarity with
local organizations, or different question frames. The [Trust for Civic Life
record](records/us-trust-civic-life-rural-local-agency-2025.json) keeps the
local capacity measures and the small returning comparison separate from the
national surveys.

### AAPI identity combines pluralist ideals with immigration-status caution

The AAPI Data/AP-NORC April 20–28, 2026 probability-panel survey of 1,075
AAPI adults adds a distinct subgroup lens. Eighty percent called the American
Dream important to U.S. identity, 79% said the same of a democratically elected
government, and 73% of mixing cultures and values from around the world. Yet
64% said the United States used to be a great place for immigrants but is not
anymore, while only 30% said it is a great place for immigrants now.

The exposure surface is behavioral rather than only attitudinal: 51% said they
or someone they know had carried documentation, changed travel plans, altered
daily routines, or faced detention/deportation because of immigration status;
41% reported the documentation item and 34% the travel item, versus 25% and
18% in the general-population comparison. The same source reports support for
cultural maintenance (58%), fluent English (54%), home-language maintenance
(49%), and blending into American society (48%).

This suggests a bounded subtheme: **pluralist national ideals can coexist with
status-related behavioral caution and a weakened sense of immigrant welcome**.
It does not establish legal-status composition, discrimination prevalence,
policy causation, safety, migration, or a unified AAPI political bloc. The
[AAPI Data/AP-NORC record](records/us-apnorc-aapi-immigration-status-identity-2026.json)
keeps values, national judgment, reported behavior, cultural integration, and
citizenship opinions separate.

### Immigration concern can become family-level nonuse of essential routes

The Urban Institute's December 2025 Well-Being and Basic Needs Survey analysis
provides a stronger conversion surface. Among 2,234 adults in immigrant
families, 18% reported that they or someone in the family did not engage in at
least one listed essential activity because they did not want to draw attention
to immigration status. The listed routes include not going to work (9%), not
driving (11%), not visiting health care (8%), and not participating in
religious services or community events (9%).

Mixed-status families reported higher worry than immigrant families without
undocumented members about visiting a doctor (29% versus 10%), going to work
(38% versus 8%), sending children to school or child care (37% versus 11%), and
talking to police (38% versus 10%). About 12% reported avoiding safety-net
programs because of green-card concerns and 9% because of data-sharing
concerns.

This supports a bounded chain of **status-related concern → precaution or
avoidance → reduced access to work, care, community, and benefits**. It is still
not a causal event ledger: the data are retrospective, family-level, and do not
identify the exact legal status, enforcement event, agency action, forgone
amount, or recovery. The [Urban immigrant-family record](records/us-urban-wbns-immigrant-family-disengagement-services-2025.json)
preserves those boundaries and supplies the next route for protected-person or
household follow-up.

### Enforcement fear can reduce public-safety reporting while reported crime stays flat

The Census Center for Economic Studies working paper *Community Engagement and
Public Safety* adds a causal policy-to-public-safety mechanism. Using Secure
Communities policy variation, the authors report that the policy reduced the
likelihood that Hispanic victims reported crimes to police and increased
offending against Hispanics. The number of reported crimes was unchanged,
because the opposing reporting and offending movements masked one another; the
paper estimates that a 10% decline in reporting increased offending by 7.9%.

This is stronger than a general trust or avoidance association, but it remains
bounded: the study concerns one historical policy, Hispanic victims, and
policy/crime/reporting measures. It does not establish that every enforcement
program or jurisdiction behaves the same way, identify every reason for
nonreporting, measure all victimization, or show later trust or collective
action. The [Census enforcement-reporting record](records/us-census-immigration-enforcement-victim-reporting-public-safety-2026.json)
therefore adds **enforcement fear → reporting behavior → public-safety
consequence**, while preserving the remaining open household and institutional
arrows.

## Why it matters across the 14-theme atlas

This candidate connects:

- **Trust, identity, and cultural meaning:** which authorities are treated as
  credible and how legitimacy is assigned;
- **Political judgment and civic participation:** who participates, watches,
  withdraws, or acts through local rather than national channels;
- **Platforms, data, and digital agency:** how online sources and AI enter the
  information environment;
- **Public systems and administrative access:** whether trust affects use of
  benefits, care, complaints, or appeals; and
- **Consumer and firm power:** whether declining trust changes reliance on
  platforms, large technology companies, or local alternatives.

These are thematic connections only. The current sources do not establish one
shared respondent-level chain across them.

### 9. The July release separates social capacity, material room, and authority

The follow-up comparison across the official July HTOPS tables finds that
social support, organized participation, material pressure, and information
authority do not form one common subgroup scale. Adults 65 and older report
more regular social/emotional support and club participation than younger
adults, while younger adults report greater expense and food pressure. Doctor
and AI trust have different age and race/ethnicity gradients: for example,
Asian respondents show comparatively high doctor and AI trust alongside lower
reported expense and food strain, while Black respondents show higher strain
and lower doctor trust. Hispanic respondents show comparatively high AI trust
despite lower support and club participation than the White non-Hispanic
group.

The July public-use file then closes one adjacent arrow at respondent level:
among 12,088 valid records, loneliness rises from 1.70% in the no-difficulty
group to 22.83% in the very-difficult group, while always/usually obtaining
support falls from 75.12% to 39.48%. Doctor trust, federal-statistics trust,
and Congress confidence also fall across the expense groups. AI trust is the
counterexample: it is broadly flat across the first three groups and lower in
the very-difficult group. The [HTOPS July social-capacity and authority
subgroup memo](projects/us-cost-trust-politics/htops-july-social-capacity-authority-subgroup-synthesis-v1.md)
and [canonical same-respondent record](records/us-census-htops-july-material-social-authority-same-respondent-2026.json)
preserve the PUF hash, 80 replicate-weight standard errors, and the boundary:
this is a same-round association, not a causal or longitudinal transition.
The PUF does not show which authority a particular person used, whether the
information was accurate, or whether it produced help, action, non-use, or
exit.

The [Pew source-environment and civic-action crosswalk](projects/us-cost-trust-politics/pew-source-environment-action-crosswalk-v1.md)
now performs the conceptual three-source join: Census supplies material room
and within-record authority differences, Pew supplies multidimensional civic
styles and action, and Gallup supplies institution-specific legitimacy. The
result is a bounded inference—fragmented civic authority under unequal
practical room—not a pooled trust score or causal respondent chain.

Pew's separate March 2020–February 2025 repeated-respondent analysis adds a
longitudinal trust transition: 25% changed their generalized social-trust
answer, with 14% gaining trust and 11% losing it, and respondents who did not
live comfortably more likely to lose trust. The [Pew social-trust longitudinal
record](records/us-pew-social-trust-financial-wellbeing-longitudinal-2020-2025.json)
strengthens the timing layer but does not identify a dated material event,
responsible actor, remedy, or later political action.

A separate comparative causal study adds an action-side mechanism without being
silently generalized to the United States. An American Political Science Review
study uses German bank-calendar/payment timing as a natural experiment: when
the same income had to stretch across a longer month, poor respondents' turnout
intentions fell and affected elections had lower turnout, with the largest
effects near month-end. The [comparative acute-hardship
record](records/comparative-apsr-acute-financial-hardship-turnout-germany-2021.json)
supports a resource/efficacy mechanism while preserving the gap: it does not
measure U.S. trust change, attribution, remedy, or the Census/Pew respondents'
votes.

A new U.S. policy-specific bridge comes from NBER Working Paper 34980. Using
EITC expansions and 1990s welfare reform as instruments for employment among
lower-income mothers, the paper's abstract reports lower turnout, registration,
political knowledge, and civic engagement, alongside increased conservatism.
The [NBER employment-to-politics record](records/us-nber-eitc-employment-mothers-voting-identity-2026.json)
adds a useful counterexample to treating work as automatic political capacity:
employment can change income, schedule, childcare, benefit status, workplace
networks, and identity together. It remains a working-paper abstract boundary,
not a universal employment or partisan-effect estimate.

The companion NBER Working Paper 27717 supplies the time-and-care layer needed
to interpret that result. Using American Time Use Surveys around EITC
expansions since 2003, it reports more maternal work and less time in home
production, leisure, and time with children; almost none of the reduction in
time with children came from active investment-related activities. The effects
are concentrated among socioeconomically disadvantaged mothers, especially
unmarried mothers and mothers of young children. The [NBER maternal-time-use
record](records/us-nber-eitc-maternal-time-use-children-2020.json) keeps this
as a separate policy-to-time observation: it makes “usable room” measurable
without claiming that lower total time with children means lower developmental
investment, or that the same households later changed political identity.

The NBER two-state cash-transfer experiment adds a durability boundary. Its
$1,000-per-month assignment versus $50 for three years increased expenditures
by at least $300 per month, with the largest spending effects in housing, food,
and car expenses, and increased housing-unit and neighborhood mobility. It
also improved self-reported financial health and credit scores, but asset gains
were offset by higher debt, leaving near-zero net-worth effects. The [NBER
consumption/balance-sheet record](records/us-nber-unconditional-cash-consumption-balance-sheets-2024.json)
therefore separates immediate household room from durable balance-sheet
recovery rather than treating either as a generic “cash worked” outcome.

The related NBER parenting study adds a counterexample inside the care layer.
A randomized $1,000-per-month transfer versus $50 for three years increased
child spending and reported parenting quality, with the largest parenting
improvements among the lowest-income families and increased use and quality of
non-parental childcare. Yet it also increased reported child developmental
difficulties and stress, possibly because closer monitoring revealed more
problems; parental satisfaction and several other outcomes did not change. The
[NBER parenting/stress record](records/us-nber-unconditional-cash-parenting-stress-2025.json)
keeps care inputs, observed difficulty, and wellbeing as distinct currencies.

The randomized-transfer literature adds a second counterexample to one-size-
fits-all recovery. NBER Working Paper 33737 reports similar effects on income,
earnings, and total household expenditures across racial and ethnic groups,
but different parental-investment responses: Latino families increased
child-focused spending by nearly one-third of the transfer with no maternal-
employment or child-time effect, while Black families reduced maternal work
hours and increased early-learning time with no child-focused-spending effect.
The [NBER parental-investment record](records/us-nber-unconditional-cash-parental-investment-heterogeneity-2025.json)
keeps this as a randomized redistribution → adaptation observation. It does
not infer racial mechanism, care quality, durable work change, or later trust
and political action from the subgroup pattern.

The cash-transfer portfolio now reaches a political endpoint through NBER
Working Paper 24770. Exogenous unconditional transfers increased adult
children's voting propensity when they came from initially poorer families,
but had no effect on parents or on children from initially better-off families.
The [family-income/voting record](records/us-nber-family-income-intergenerational-voting-2018.json)
therefore supports a delayed intergenerational resource/social-capital route,
not an immediate adult-recipient turnout, trust, or vote-choice effect.

A complementary APSR Moving to Opportunity study supplies a place-based
counterexample. Random housing-voucher offers reduced neighborhood poverty and
improved some child socioeconomic outcomes, yet later child turnout did not
increase, adult effects were null, and teen registration/turnout declined. The
[MTO voting record](records/comparative-apsr-moving-to-opportunity-voting-2024.json)
keeps socioeconomic improvement, neighborhood integration, developmental stage,
disruption, and political participation as separate stages.

Contemporary welfare data provide a further boundary: cash assistance shows
little association with participation, food stamps are positively associated
with registration, and food-stamp voting associations vary by political
attentiveness. The [welfare-participation record](records/us-social-problems-welfare-receipt-political-participation-2022.json)
keeps this as a fixed-effects observational heterogeneity result, not a causal
benefit effect or a general welfare-to-trust claim.

The NBER welfare-reform voting study provides a positive contrast under a
different design. Greater exposure to 1990s reform was associated with roughly
a four-percentage-point relative advantage in presidential voting among
low-income women, with stronger effects in Democratic states and states with
stronger work incentives. The [welfare-reform voting record](records/us-nber-welfare-reform-womens-voting-2016.json)
keeps this state-by-year policy-exposure estimate separate from both the
observational welfare study and the EITC employment-instrument result.

The Health Affairs Scholar safety-net study adds a direct stigma/meaning
surface. Among 497 low-income California caregivers of young children, SNAP
participation and EITC receipt were each associated with greater reported social
stigma, while overall government perceptions did not differ. Among food-insecure
respondents, SNAP was additionally associated with program stigma and
discrimination. The result is cross-sectional and based on a convenience/snowball
sample, so it is not a causal trust estimate or a national program effect. It
does, however, preserve an important boundary: material support can coexist
with a stigma cost without producing a uniform change in government perception.
The [canonical safety-net stigma record](records/us-health-affairs-safety-net-stigma-government-perceptions-2024.json)
keeps participation, stigma, government perception, and action separate.

The Oregon Medicaid lottery adds a causal public-system-to-vote endpoint.
Randomized access to Medicaid increased November 2008 presidential turnout by
2.5 percentage points, approximately 7% relative to the control group, with
larger effects among men and residents of Democratic counties. There was no
evidence of increased turnout in later elections through November 2010. The
early result may reflect registration, administrative contact, health or
financial security, or election-specific mobilization; it is not a generalized
trust or durable realignment estimate. The [canonical Oregon Medicaid voter
record](records/us-oregon-medicaid-lottery-voter-participation-2019.json) keeps
the action endpoint and mechanism boundary separate.

The Oxford Economic Papers UAS study adds an observational mobilization
counterexample. Among 2,367 adults with at least five repeated income
observations before the 2016 presidential-election poll, greater
income-history insecurity predicted a higher reported probability of voting and
greater Trump support, conditional on current resources, with lower Clinton
support. The index uses modeled income bands and the outcomes are reported
probabilities, so this is not a causal hardship effect or a ballot-validated
turnout estimate. It does show why the atlas must preserve both withdrawal and
mobilization routes under material insecurity. The [canonical UAS economic-
insecurity record](records/us-oxford-economic-insecurity-political-preferences-2023.json)
keeps the panel and inference boundary explicit.

The Social Problems urban-poor study adds a government-encounter layer. In a
sample of 462 low-income men and women in one of the poorest congressional
districts, severe economic hardship and formative contact with government
agents were associated with greater willingness to participate in the political
system, while material resources and demographic attributes structured activism.
The study is observational and geographically narrow; it does not establish a
causal agency encounter, national prevalence, validated turnout, or generalized
trust change. Its value is to show that the manner of encountering government
can condition whether hardship becomes withdrawal, grievance, or participation.
The [canonical urban-poor government-contact record](records/us-social-problems-urban-poor-government-contact-activism-2001.json)
keeps the encounter and action boundary explicit.

The NBER meaning-at-work experiment adds a worker-centered firm comparison.
Across 2,976 white-collar employees followed for two years, a randomized
purpose intervention increased performance; low performers either improved or
left; the meaning/pay tradeoff flattened as low-meaning/high-pay workers exited;
and parental-leave behavior and bonuses changed. This observes a firm-level
meaning-to-work outcome route, but not durable control, bargaining power,
household security, or political action. The [canonical meaning-at-work
record](records/us-nber-meaning-at-work-purpose-intervention-2025.json) keeps
worker performance, exit, compensation, and household welfare separate.

The NBER autonomy-of-labor experiment adds a task-level causal mechanism. Among
476 U.S.-located online workers, high autonomy increased preventative-effort
take-up by 9.7 percentage points because workers could allocate skippable work
across two receipt sets. This is not a general earnings, gig-work, household,
or bargaining estimate; it shows that usable discretion can change how workers
manage risk and effort. The [canonical autonomy-of-labor record](records/us-nber-autonomy-labor-risk-prevention-2022.json)
keeps task control, risk management, and broader worker welfare separate.

The comparative IZA job-flexibility study extends that mechanism into the
household. In 464 Dutch couples with children, a collective model links
parent-specific schedule and telecommuting flexibility to market work,
childcare, chores, household resources, and modeled child well-being. The
simulations generally narrow gender gaps in paid and domestic work, but do not
produce a uniform child-well-being gain; lower wages accompanying flexibility
reduce household resources, and the parent receiving flexibility matters. This
is a structural comparative result, not a U.S. causal estimate. The [canonical
record](records/comparative-iza-job-flexibility-intrahousehold-child-wellbeing-2026.json)
keeps worker control, care time, pay, and household welfare separate.

## Next decisive test

The July PUF subgroup screen and the conceptual Pew/Gallup crosswalk are now
complete. The next decisive test is a common respondent or designed episode
that adds source encountered, attribution, and action or non-use to the
material-pressure and authority measures. Until that exists, compare the July
cross-sectional results with March and May releases without treating the 2026
files as a panel, and use Pew/Gallup as separate constraints rather than
joining their samples.

The next test should ask whether the apparent fragmentation is primarily:

- a social-capacity pattern, where local/community ties remain stronger than
  national institutions;
- an information-authority pattern, where people substitute peers, media,
  influencers, or AI for formal institutions; or
- a partisan legitimacy pattern, where confidence changes mainly with control
  of national political power.

Do not claim a causal trend until a repeated or matched source supplies timing,
or until a source directly measures the relevant behavior or institutional use.

## External sources

- [U.S. Census Bureau, July 2026 HTOPS tables](https://www.census.gov/data/tables/2026/demo/hhp/2607.html)
- [Gallup, Confidence in U.S. Institutions Remains Near All-Time Low](https://news.gallup.com/poll/712436/confidence-institutions-remains-near-time-low.aspx)
- [Pew Research Center, How Americans Are Engaged With News, Politics, Religion and Civic Life](https://www.pewresearch.org/journalism/2026/07/16/how-americans-are-engaged-with-news-politics-religion-and-civic-life/)
- [AAPI Data/AP-NORC, Most AAPI adults agree that the United States used to be a great place for immigrants](https://apnorc.org/projects/most-aapi-adults-agree-that-the-united-states-used-to-be-a-great-place-for-immigrants-but-is-not-anymore/)
- [Urban Institute, Immigrant Families Disengaged from Public Life and Essential Services Because of Immigration Concerns in 2025](https://www.urban.org/research/publication/immigrant-families-disengaged-public-life-and-essential-services-because)
- [U.S. Census Center for Economic Studies, Community Engagement and Public Safety](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-23.html)
- [Pew Research Center, How Americans Feel About Religion's Influence in Government and Public Life](https://www.pewresearch.org/religion/2026/05/14/how-americans-feel-about-religions-influence-in-government-and-public-life/)
- [Gallup, Rise in Young Men's Religiosity Realigns Gender Gaps](https://news.gallup.com/poll/708410/young-men-religious-gains-realign-gender-gap.aspx)
- [Gallup, Americans Think Kindness Prevails](https://news.gallup.com/poll/708569/americans-think-kindness-prevails.aspx)
- [American Political Science Review, Acute Financial Hardship and Voter Turnout](https://www.cambridge.org/core/journals/american-political-science-review/article/acute-financial-hardship-and-voter-turnout-theory-and-evidence-from-the-sequence-of-bank-working-days/5B5A872CA63098D5B6A3FCC53B9B6C29)
- [NBER, Does Employment Shift Mothers' Voting Behavior and Political Identity?](https://www.nber.org/papers/w34980)
- [NBER, The EITC and Maternal Time Use: More Time Working and Less Time with Kids?](https://www.nber.org/papers/w27717)
- [NBER, Money or Time? Heterogeneous Effects of Unconditional Cash on Parental Investments](https://www.nber.org/papers/w33737)
- [NBER, The Impact of Unconditional Cash Transfers on Consumption and Household Balance Sheets](https://www.nber.org/papers/w32784)
- [NBER, The Impact of Unconditional Cash Transfers on Parenting and Children](https://www.nber.org/papers/w34040)
- [NBER, Family Income and the Intergenerational Transmission of Voting Behavior](https://www.nber.org/papers/w24770)
- [NBER, Effects of Welfare Reform on Women's Voting Participation](https://www.nber.org/papers/w22052)
- [Health Affairs Scholar, Association of Safety-Net Program Participation with Government Perceptions, Welfare Stigma, and Discrimination](https://academic.oup.com/healthaffairsscholar/article/2/1/qxad084/7486464)
- [Quarterly Journal of Political Science, The Impact of Medicaid Expansion on Voter Participation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8021132/)
- [Oxford Economic Papers, Economic Insecurity and Political Preferences](https://academic.oup.com/oep/article/75/3/802/6693580?login=true)
- [Social Problems, Political Participation of the Urban Poor](https://academic.oup.com/socpro/article-abstract/48/3/362/2276162)
- [NBER, Meaning At Work](https://www.nber.org/papers/w33843)
- [NBER, Risk Management and the Autonomy of Labor](https://www.nber.org/papers/w30793)
- [IZA, Twenty-Five Hours in a Day: On Job Flexibility and the Intrahousehold Allocation of Time and Money](https://docs.iza.org/dp17505.pdf)
- [BLS, Job Flexibilities and Work Schedules — 2024-2025](https://www.bls.gov/news.release/flex2.htm)
- [American Political Science Review, The Long-Term Effects of Neighborhood Disadvantage on Voting Behavior](https://www.cambridge.org/core/journals/american-political-science-review/article/longterm-effects-of-neighborhood-disadvantage-on-voting-behavior-the-moving-to-opportunity-experiment/4896C6743CF5D53DDD067D51D93A8CA7)
- [Gallup, Record-High 89% in U.S. Say Government Corruption Widespread](https://news.gallup.com/poll/713933/record-high-say-government-corruption-widespread.aspx)
- [Gallup, Socialism's Positive Rating Tops 40% for First Time](https://news.gallup.com/poll/714653/socialism-positive-rating-tops-first-time.aspx)
