# Financial access is broadening, but digital reach and financial room remain different surfaces

**Status:** provisional cross-country financial-inclusion finding · **Checked:** 2026-09-15  
**Question:** when financial life becomes more digitally connected, does that mean households have more room, more control, and more ability to recover from a shock?

## The short answer

The World Bank's Global Findex 2025 adds an important international and
demand-side layer to the US atlas. In the United States, account ownership
reached 97.0% of adults in the 2024 survey, up from 88.0% in 2011. The
female/male ownership gap moved from 7.9 percentage points in 2011 to roughly
zero in 2024. Mobile-phone ownership was 98.0% and smartphone ownership 92.6%
in 2024.

Those numbers establish broad formal access and connectivity. They do not show
that every adult has liquid savings, affordable credit, a secure payment route,
an understandable product, a human remedy, or the ability to leave a provider.
The central finding is therefore a separation:

> Financial infrastructure can become nearly universal at the level of account
> and device ownership while usable financial room, protection, and practical
> control remain unmeasured or uneven.

This is a useful counterweight to both “digital inclusion solves exclusion” and
“digital finance is only extraction.” The evidence shows expanded reach. The
distribution of benefit, risk, terms, and remedy requires a different layer of
observation.

## What this source contributes

Global Findex is a nationally representative adult survey conducted in 2024
across 141 economies, with roughly 145,000 adults overall. The 2025 edition
contains repeated account, saving, borrowing, payment, and emergency-fund
indicators, plus new connectivity measures for mobile phones, smartphones,
internet use, and digital safety. The country-level API slice used here is an
aggregate layer; the public microdata are a separate acquisition route.

The source is especially valuable for this program because it holds apart three
things that are often merged in public discussion:

1. **A formal account:** an institutional doorway.
2. **A connected device:** a possible access channel.
3. **Financial use and resilience:** what people do through the doorway and
   whether they can absorb a defined shock.

The first two are available for the United States in 2024. Several of the
third-layer US indicators are not returned for 2024, so the earlier 2014–2021
series are retained as historical context rather than silently extended.

## The US trajectory: the ownership gap narrowed sharply

| Measure | Earlier point | 2024 point | What it says | What it does not say |
|---|---:|---:|---|---|
| Account ownership, all adults | 88.0% in 2011 | 97.0% | Formal account access is now very broad | Whether the account is used, affordable, safe, or sufficient |
| Account ownership, women | 84.1% in 2011 | 97.1% | Female account ownership rose strongly | Whether women receive equal terms, control, safety, or credit access |
| Account ownership, men | 92.0% in 2011 | 96.9% | Male ownership was already high and remained high | Whether the apparent convergence extends to use or outcomes |
| Mobile-phone ownership | — | 98.0% | A mobile channel is nearly universal in the US aggregate | Whether the device, plan, data, or accessibility is practically usable |
| Smartphone ownership among phone owners | — | 92.6% | Most adults report a smartphone as their main phone | Whether apps, identity checks, passwords, and interfaces are accessible |

The account series is a repeated cross-section, not a panel. The movement from
2011 to 2024 may reflect real acquisition, replacement of unbanked adults in
the sample, changing definitions, survey error, or a combination. The trend is
still substantively important: the US aggregate account-access problem is no
longer well-described by a simple question of whether a formal account exists.

The next questions must move down the stack: can the person keep the account,
receive income or benefits into it, make a payment without penalty, recover
from fraud or error, borrow on workable terms, and switch or appeal when the
provider fails?

## The provider-side counterpoint: access stayed broad while infrastructure contracted

The IMF Financial Access Survey adds the institutional side of the US picture.
Its 2020–2024 administrative/provider-reported series show a contraction in
traditional commercial-bank infrastructure:

| Provider-side measure | 2020 | 2024 | Change | Interpretation boundary |
|---|---:|---:|---:|---|
| Commercial banks | 4,344 | 3,912 | −9.9% | Institution count, not customer access or market competition |
| Credit unions/credit cooperatives | 5,241 | 4,579 | −12.6% | Provider count, not member welfare or service availability |
| Commercial-bank branches excluding headquarters | 75,500 | 68,436 | −9.4% | Physical network, not travel time, hours, or service quality |
| Commercial-bank branches per 100,000 adults | 29.51 | 25.74 | −12.8% | Adult-normalized density, not a person-level access probability |
| Household commercial-bank deposits / GDP | 55.52% | 42.43% | −23.6% | Balance-to-GDP ratio, not household liquidity or adequacy |
| Household commercial-bank loans / GDP | 19.90% | 16.80% | −15.6% | Balance-to-GDP ratio, not credit approval, affordability, or repayment |

This is not a contradiction of the Findex result. It is the reason the atlas
keeps the layers separate. Adult-reported account ownership can rise while
institutions consolidate, branches contract, balances normalize relative to
GDP, and digital channels or nonbank routes become more important. The data do
not identify which of those mechanisms explains the divergence.

The physical-network decline may be convenient for a digitally capable customer
and costly for a person who needs cash, an identity check, a safe human contact,
or a remedy after an error. Provider counts cannot measure that distribution.
The next test must join place, customer, route, and event—not infer a welfare
effect from infrastructure contraction alone.

## The cross-country check: the US path is not a universal template

The selected IMF comparison weakens any claim that one global provider
trajectory explains financial access:

| Economy | Bank-count change | Branch-density change | What the counterexample does |
|---|---:|---:|---|
| United States | −9.9% | −12.8% | The US shows contraction on both provider surfaces |
| Canada | −5.1% | −10.6% | Similar direction, smaller bank-count change |
| Germany | −8.9% | −47.6% | Much sharper reported branch-density contraction |
| China | −4.7% | −0.5% | Bank count falls while density is nearly flat |
| India | −6.6% | +0.5% | Bank count falls while density and household-loan ratio rise |
| Brazil | +25.6% | −13.5% | Bank count rises while branch density falls |
| Mexico | +2.0% | −7.6% | Bank count rises while density falls |
| South Africa | −11.8% | −9.4% | Both provider measures contract, with a different balance path |

The India and Brazil rows are especially useful counterexamples. India reports
fewer commercial banks but slightly higher adult-normalized branch density and
a higher household commercial-bank loan ratio. Brazil reports more commercial
banks but lower branch density. Neither pattern tells us whether people are
better or worse off. It does tell us that provider count, physical density,
balance ratios, digital access, and household room are separate empirical
surfaces.

Some cells are unavailable in the returned FAS series—particularly household
deposit/loan ratios for several selected economies and branch-density data for
the United Kingdom. They are retained as missing, not imputed or ranked. The
[cross-country FAS record](../../../records/us-imf-fas-provider-cross-country-2020-2024.json)
preserves the endpoint values, response hashes, and missingness boundary.

## The country comparison: access and connectivity do not form one ladder

The 2024 selected-country slice makes the separation visible.

| Economy | Account | Mobile phone | Smartphone | Reading |
|---|---:|---:|---:|---|
| United States | 97.0% | 98.0% | 92.6% | Account and device reach are both high |
| Canada | 98.4% | 89.4% | 84.1% | Very high account ownership coexists with lower reported device reach |
| Germany | 98.3% | 92.0% | 84.5% | Formal access is broader than smartphone ownership |
| United Kingdom | 99.3% | 91.8% | 85.4% | Account ownership is not a device-ownership measure |
| China | 89.4% | 96.6% | 88.2% | Connectivity is high relative to formal account ownership |
| India | 89.0% | 66.5% | 42.0% | Formal account reach exceeds smartphone reach by a wide margin |
| Brazil | 86.4% | 92.1% | 71.8% | Device reach is broader than account ownership |
| South Africa | 81.1% | 87.0% | 67.5% | Phone access exceeds formal account access |
| Mexico | 53.0% | 83.3% | 64.5% | The largest selected gap is between phone and account access |

These are not a ranking of financial wellbeing. A phone can be shared, lost,
locked, unaffordable to keep connected, or unusable for an account's identity
requirements. An account can be dormant, expensive, inaccessible during an
outage, or useful only for a narrow transaction. The comparison is valuable
because it prevents the program from calling any one of these conditions “the
digital divide.”

The US has a one-point account-minus-phone gap and a 5.4-point phone-minus-
smartphone gap in the selected API estimates. That is a description of national
reach, not proof that the remaining adults are secure. In Mexico, by contrast,
phone ownership exceeds account ownership by about 30.2 points; in India,
mobile-phone ownership exceeds smartphone ownership by about 24.5 points.
Different gaps imply different next tests: formal access, device capability,
data affordability, identity, interface, or institutional trust.

## The earlier US use and resilience series is still needed

The 2024 release returns US account and connectivity measures, but several
financial-use indicators are unavailable in the returned US series. The API
also returns zero for the 2024 emergency-funds field; the World Bank's release
documentation warns that some indicators are unavailable for economies using
the abridged/high-income questionnaire. That zero is therefore preserved as a
data-availability boundary, not interpreted as “nobody could raise emergency
funds.”

For historical context, the available US series show:

| Measure | 2014 | 2017 | 2021 | Interpretation |
|---|---:|---:|---:|---|
| Made or received a digital payment | 92.0% | 91.1% | 93.0% | High reported use; no 2024 US value in this release slice |
| Saved any money | 75.6% | 79.3% | 78.6% | Saving is common but not the same as accessible emergency cash |
| Borrowed from a formal institution | 64.6% | 68.4% | 66.2% | Formal borrowing is not the same as affordable or successful borrowing |
| Could raise emergency funds within 30 days | 66.0% | 71.8% | 95.0% | Large movement requires wording/routing and design review |

The emergency-fund series is a particularly useful warning. A reported ability
to raise money within 30 days can include savings, family, work, asset sales, or
borrowing. It is a resilience perception and route measure, not a balance-sheet
observation. Its sharp 2021 movement should not be read as a clean population
improvement without a full comparability audit.

Likewise, digital-payment use does not reveal who paid a fee, who had a payment
reversed, who could dispute a transaction, who lost access during an outage, or
who had to use credit to maintain the payment. The payment is the visible event;
the terms and recovery path are the power question.

## A gender convergence finding with a remaining control question

The account-ownership gap nearly disappears in the US aggregate by 2024:
women are at 97.1% and men at 96.9%. That is a meaningful access result. It
should not be inflated into a general gender-equality result.

Formal ownership does not measure:

- who controls the password, device, or account;
- whose income or government payment enters the account;
- who can borrow and at what price;
- whose transaction is flagged or blocked;
- who bears fraud, overdraft, or identity-repair effort; or
- who can leave a provider without losing wages, benefits, history, or access.

The atlas therefore records the ownership convergence as an access-stage
finding and keeps gendered use, terms, safety, and remedy as open arrows. This
is the same discipline used elsewhere: an institutional doorway is not yet
control inside the institution.

## How it connects to the existing US evidence

Global Findex does not replace the household or institutional sources already
in the program. It changes the map by adding a clean comparison between
demand-side access and practical financial room.

| Existing layer | Findex adds | The combined question |
|---|---|---|
| Federal Reserve SHED | Household liquidity, hardship, adaptation, fraud loss, and recovery | Does formal access correspond to usable buffer and recovery for the same household? |
| SIPP | Monthly resources, work, benefits, utility and food outcomes | Does a payment or account route alter a later month of money, work, or hardship? |
| OFR | Financial-system structure and market plumbing | Which institutional layer sets the terms behind the household's access? |
| IMF Financial Access Survey | Provider counts, branches, adult-normalized access, and household balance ratios | Does provider-side capacity contract or change composition while user-reported access remains broad? |
| BEA/BLS | Income, consumption, prices, labor, and aggregate flows | Does broad financial access coexist with changing aggregate or household room? |
| CFPB/FTC | Complaint visibility, firm response, fraud reports, and consumer protection | Can an account holder reach correction, remedy, and exit after failure? |
| IMF Financial Access Survey | Provider-side access and financial infrastructure | Do provider-side measures and user-reported access describe the same expansion? |
| World Bank Enterprise Surveys | Firm finance and infrastructure constraints | Does consumer financial connectivity translate into small-firm capacity or only payment reach? |

The important synthesis is not “more access is good” or “more digitization is
bad.” It is that the program now has a staged measurement architecture:

```text
device / account ownership
  -> payment, saving, borrowing, and emergency route
  -> price, fee, record, security, and remedy
  -> household food, housing, work, health, and time room
  -> trust, switching, exit, collective demand, or dependence
```

Findex observes the first two stages well in selected countries and years. The
US atlas has stronger household and institutional evidence for later stages,
but the same respondent is not yet followed through the complete chain.

## What the data do not establish

This pass does not establish that:

- account ownership caused financial resilience;
- smartphone ownership caused digital-payment use;
- the gender ownership convergence produced equal financial power;
- formal borrowing improved household welfare;
- digital payments reduced fees, fraud, or effort;
- a country-level access gap caused a cultural or political difference; or
- financial inclusion produced geopolitical leverage.

The source is a repeated cross-sectional survey with country-specific sampling
and questionnaire differences. Country-level indicators are often weighted
estimates without a common respondent count in the public API response. Some
indicators are absent for the US in 2024, and the absence is informative about
measurement coverage but not about the underlying population value.

## The next decisive test

The next financial-intermediation pass should use a same-person or same-account
design to connect access to practical room. The minimum record is:

1. account and device access, including shared use and interruption;
2. income, benefit, or wage payment route and timing;
3. payment, saving, borrowing, fee, overdraft, or fraud event;
4. available alternatives, family support, credit options, and provider choice;
5. correction, dispute, human contact, remedy, and time spent;
6. later food, housing, health, work, debt, and liquidity outcomes; and
7. trust, attribution, switching, non-use, exit, or collective demand afterward.

The highest-value comparison is not account holders versus non-account holders
alone. It is similar households with different buffers, terms, payment routes,
or remedy access, followed after a defined event. The counterexample must be
preserved: a digitally connected person may still have little room, while a
person using a less digital route may have strong family, institutional, or
cash alternatives.

## Reader's conclusion

The Global Findex 2025 sharpens one of the atlas's recurring themes: visible
reach is not the same as usable freedom. In the US, the formal doorway is now
almost universal, and the ownership gender gap has narrowed dramatically. The
harder social question has moved inside the doorway—who gets favorable terms,
who can transact safely, who can recover, who can refuse, and whose financial
record becomes the next gate.

That is the contribution of this pass: it expands the program's international
and financial-infrastructure coverage while keeping the household, consumer,
institutional, cultural, and political arrows open until a design can actually
follow them.

## Source and reproduction notes

- [World Bank Global Findex 2025 download-data page](https://www.worldbank.org/en/publication/globalfindex/download-data)
- [World Bank Global Findex 2025 report](https://www.worldbank.org/en/publication/globalfindex/report)
- [World Bank Microdata Library catalog record](https://microdata.worldbank.org/catalog/7860)
- [Machine-readable Global Findex financial-room record](../../../records/us-world-bank-global-findex-financial-room-2011-2024.json)
- [IMF Financial Access Survey provider-side audit](../imf-fas-provider-side-access-audit-2026-09-15.md)
- [Machine-readable IMF FAS US provider-capacity record](../../../records/us-imf-fas-provider-capacity-2020-2024.json)
- [IMF FAS selected-country comparison record](../../../records/us-imf-fas-provider-cross-country-2020-2024.json)
- [Reproducible country-level API extract](../data/world-bank-global-findex-2025-api-extract.json)
- Script: `scripts/analyze_world_bank_global_findex_2025.py`

The committed extract contains 117 API responses for nine economies and 13
indicators, with response hashes and the World Bank indicator catalog hash. It
was retrieved on 2026-09-15. The extract is a country-level slice; it does not
contain individual-level microdata or complex-design standard errors.
