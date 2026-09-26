# Consumer power and recourse: source-led subtheme map v1

**Checked:** 2026-09-24  
**Scope:** 165 current registry records carry the
`consumer_power_recourse` program-theme label. This map identifies the
repeated consumer structures within them. It does not infer a consumer-harm
rate from complaint, enforcement, or product-specific evidence.

## What the source material supports

The records repeatedly distinguish:

> an offer from an understood offer; a nominal alternative from a usable
> comparison; a complaint response from correction; and a settlement or refund
> fund from individual recovery.

## 1. Search friction can preserve price differences and firm revenue

The [rideshare comparison record](records/us-nber-uber-lyft-price-dispersion-search-frictions-2025.json)
audited identical Uber and Lyft trips in New York City and found price
differences, while only about 16.1% of people opening one app also opened the
other. The study estimates that comparison friction increases annual gross
booking volume by more than $300 million in New York City. It does not observe
each rider's time constraint, accessibility need, wait time, safety, transit
alternative, trip quality, or avoidable overpayment.

The [browser choice-screen record](records/comparative-nber-browser-defaults-active-choice-2026.json)
provides a separate comparative mechanism: EU choice screens were followed by
a 91% increase in Firefox use on iOS and 13% on Android relative to the
study's counterfactual, with rollout design differing across platforms. It
does not establish U.S. behavior, comprehension, privacy, or welfare.

**Supported subtheme:** alternatives can exist but remain weak constraints on
seller power when discovering and comparing them costs attention or effort.  
**Not established:** the value of comparison to individual consumers or the
net benefit of any given default.

## 1a. Repeated online search can improve price discovery while creating its own time and attention cost

The [eBay consumer-search record](records/us-nber-ebay-consumer-search-costs-lower-prices-2015.json)
follows search and purchase behavior in one online-marketplace setting. It
reports an average of 36 searches per purchase across three distinct days, with
most search sessions ending without a purchase; the study estimates a search
cost of about 25 cents per search page and examines how more search relates to
lower prices. This is a purchasing and price-discovery route, not merely a
stated intention to compare.

**Supported subtheme:** consumer price power can require repeated inquiry,
refinement, and delayed choice before a purchase; the money price and the
search cost are separate components of a transaction.  
**Not established:** product quality, delivery, returns, seller treatment,
the full value of time and attention, a household welfare gain, or whether
search costs and savings are equally distributed by income, disability,
language, product, or digital access. The eBay setting does not represent all
platforms or purchases.

## 2. Payment interfaces can convert convenience into time, fee, and service risk

The [Doxo bill-payment record](records/us-ftc-doxo-bill-payment-hidden-fees-2026.json)
preserves the FTC's case evidence that 30% of heavy users in one internal
survey incorrectly believed Doxo was the only way to pay their bills. The
complaint alleged unclear add-on fees, subscription terms, and payment-timing
failures; the August 2026 order set a $2.1 million monetary judgment and
required clearer disclosures and cancellation. The record does not identify a
person-level fee burden, bill status, hardship, or redress receipt.

**Supported subtheme:** the route used to make a routine payment can itself
become a consumer-power question, especially when affiliation, fees, timing,
and cancellation are unclear.  
**Not established:** how often the alleged mechanism caused arrears, shutoff,
insurance lapse, or financial distress.

## 3. A complaint response label is not a measure of remedy adequacy

The [CFPB response-routes record](records/us-cfpb-product-response-routes-2024-2025.json)
shows strongly product-shaped published response labels in 2024. For example,
77.8% of 52,901 checking/savings complaints were coded as receiving an
explanation, compared with 15.0% coded monetary relief; among 156,242
debt-collection complaints, 29.0% were coded non-monetary relief and 0.25%
monetary relief. These are published complaint records, not customer
denominators or verified outcomes.

**Supported subtheme:** an institution's recorded response route is a visible
administrative stage that varies by product.  
**Not established:** whether the error, charge, debt, credit record, access
problem, or trust damage was corrected for a particular person.

## 3a. Administrative timing fields can describe different clocks, not one service-delay measure

The [student-loan timing-field audit](records/us-cfpb-student-loan-timing-field-audit-2024-2025.json)
keeps two published CFPB fields separate for product-filtered complaint
records. In 2024, the `company_response` category coded 0.33% of 14,685
student-loan complaints as untimely while the distinct `timely` field was `No`
for 5.64%. In 2025, those figures were 15.92% of 21,333 and 30.40%,
respectively. The fields may identify different processing stages or coding
rules; their gap is not proof that either measure is wrong or that a borrower
waited a known number of days.

**Supported subtheme:** complaint data can reveal institutional route and
classification changes while still lacking a common service clock. Response
label, timely-status field, elapsed time, correction, and borrower outcome
need to remain distinct variables.

**Not established:** actual response duration, payment interruption, servicing
failure, individual remedy adequacy, borrower harm, or a causal year-over-year
deterioration.

## 3b. Complaint intake, routing, published labels, and closed cases are different recourse denominators

The [CFPB annual-response record](records/us-cfpb-annual-response-trend-2020-2025.json)
(`us-cfpb-published-response-endpoint-2020-2025`)
shows why a complaint-system headline cannot be read as one outcome series. In
the published-record API snapshot, the monetary-relief label fell from 2.91%
of 444,837 records received in 2020 to 0.48% of 5,452,107 records received in
2025; non-monetary relief rose through 2024 then fell to 40.63% in 2025, while
the explanation label was 58.71%. Product mix, routing, publication, coding,
and index changes mean those shifts do not identify a change in consumer
remedies.

The CFPB's separately framed 2025 annual report supplies upstream operations:
6.64 million complaints received, about 5.98 million sent to companies, 97%
of those sent within one day, more than 99% receiving a timely company
response, and about 5.42 million closed with an explanation or relief after a
company confirmed a commercial relationship. Received complaints are not
unique people, and the annual-report universe differs from the published API
snapshot.

**Supported subtheme:** consumer recourse has at least four observable clocks:
complaint intake, institutional routing, company response, and an
administratively closed label. Large throughput and timely response can coexist
with an unknown substantive correction rate.

**Not established:** a representative harm rate, error correction, payment or
credit-record repair, adequacy or receipt of relief, trust, switching, or
household recovery; nor a causal interpretation of the annual label shifts.

## 3b.1. Fast institutional routing is not the same as a visible or monetary remedy

The [CFPB case-route sample audit](records/us-cfpb-case-route-sample-2024.json)
uses four capped 500-record 2024 product samples, so it is a route-field audit
rather than a population estimate. Median receipt-to-company-send time ranged
from 0.056 hours for credit-reporting complaints to 0.466 for mortgage
complaints; the student-loan routing 90th percentile was 23.718 hours. But
public-response fields appeared for 31.4% of the credit-reporting sample and
51.8% of the mortgage sample. The closed-with-monetary-relief label was 14.4%
in checking/savings, 1.4% in mortgages, and 1.2% in student loans; explanation
labels were much more common in the latter two products (95.2% and 97.4%).

**Supported subtheme:** receipt, agency routing, company-visible response,
administrative closure, and a monetary-relief label are product-specific
recourse stages. Rapid routing cannot stand in for correction, restoration, or
consumer-recognized remedy.  
**Not established:** a representative product-wide frequency, company response
duration, the cause of product differences, a correction of the underlying
error, received money, account or credit repair, later trust, switching, or
household recovery. The sample is capped in retrieval order and unweighted.

## 3c. An enforcement order can document a servicing-to-household exposure route without verifying restoration

The [Citibank student-loan servicing remedy record](records/us-cfpb-citibank-student-loan-servicing-remedy-2017.json)
keeps the documented failure mechanisms and the remedy order together without
turning either into a borrower-recovery result. As of June 2017, Citibank or
its affiliate serviced approximately 253,000 private education loans valued at
about $2.3 billion. The CFPB found that, among other practices, borrowers were
misled about qualified-interest tax deductions: about 640,692 borrowers making
interest payments in 2010--12 had not filed the required W-9S, roughly 85% of
interest payers in that period. The order also addresses wrongly ended
in-school deferments, late fees, capitalized interest, overstated minimum
payments, and deficient co-signer-release notices.

The 2017 action ordered $3.75 million in restitution, a $2.75 million civil
penalty, reversal of erroneous interest and late fees, accurate interest
information, and adverse-action disclosures. Those are institutionally
observable correction requirements, not receipt, tax filing, credit repair, or
financial-capacity outcomes for a particular borrower.

**Supported subtheme:** a consumer-finance service failure can travel through
information, tax eligibility, payment calculation, and account-status routes
before a regulator creates a correction route. A consent order makes the
failure and required controls legible while preserving the gap between ordered
redress and restored household position.

**Not established:** the number receiving each remedy, restitution timing or
amount per borrower, claimed tax benefit, prevalence across student-loan
servicing, later repayment or credit outcomes, complaint effort, trust,
switching, or household recovery.

## 4. Cancellation and refund enforcement make exit friction visible before recovery is known

The [Shutterstock subscription record](records/us-ftc-shutterstock-subscription-cancellation-2026.json)
preserves FTC allegations of renewal and cancellation friction and a proposed
$3.5 million settlement. Its public case materials do not show the prevalence
of unwanted renewal, account-level cancellation success, loss, refund
receipt, or recurrence prevention.

The separate [Amazon Prime redress record](records/us-ftc-amazon-prime-enrollment-refunds-2026.json)
documents about $845.2 million issued and $235.5 million accepted across
recorded payment phases as of September 2026. Aggregate issued and accepted
dollars are not an individual recovery rate; continued use, switching,
remaining loss, and trust are not observed.

**Supported subtheme:** remedy design can reduce claim burden or expose exit
friction while leaving delivery and adequacy as distinct endpoints.  
**Not established:** who was made whole, which consumer remained harmed, or
whether the underlying practice stopped.

## 5. Consumer choice increasingly includes data, screening, and surveillance power

The [rental-proptech record](records/us-gao-rental-proptech-screening-pricing-privacy-2025.json)
maps tools across rental advertising, screening, rent-setting, and facial
recognition. GAO identifies possible benefits in search and management as well
as risks from inaccurate records, algorithmic pricing, discriminatory steering,
and surveillance. All 10 public housing agencies interviewed about facial
recognition said further guidance would help; HUD projected written guidance
for December 2026. The selected interviews and risk mechanisms are not
national prevalence estimates.

**Supported subtheme:** a consumer's ability to obtain housing or another
service increasingly depends on the data, model, and identity checks applied
before the person can bargain or appeal.  
**Not established:** a national rate of inaccurate screening, discrimination,
rent increase, privacy loss, or corrected outcome.

## 6. Credit products convert immediate purchasing room into separate cost, dispute, and visibility routes

The [CFPB credit-card-market record](records/us-cfpb-credit-card-market-2025.json)
reports $1.2 trillion in balances, 25.2% average APR, $160 billion interest
assessed, $31.3 billion fees, and $9.8 billion disputed charges in distinct
market/account universes. Forty percent of disputes involved cancelled recurring
transactions. Assessed charges and disputes are not payments, erroneous
charges, successful correction, or household welfare.

The [medical-collections record](records/us-cfpb-medical-collections-credit-response-2022-2025.json)
shows how a care-cost route can become credit visibility: consumers with newly
reported medical collections had low pre-reporting average scores and a
further 12-point event-time decline; reporting-rule relief remained partial and
a 2025 federal rule was vacated. Report removal is not debt resolution, care
access, or improved household security.

The [Credit Karma refund record](records/us-ftc-credit-karma-wasted-time-refunds-2026.json)
preserves alleged pre-approved offer/application/denial/time/score harm,
more-than-$2.3 million in 2024 refunds, and a 2026 reissue route. The public
record lacks claimant denominator, individual receipt, score correction,
restored credit access, or durable switching.

**Supported subtheme:** financial consumer power depends on the whole route
from offer and application through pricing, reporting, dispute, correction,
and subsequent access—not simply whether a card or refund exists.  
**Not established:** an individual debt/score causal sequence, remedy adequacy,
or durable financial recovery.

## 6a. The public card-offer menu is a pricing and eligibility surface, not a borrower outcome

The [CFPB card-terms record](records/us-cfpb-tccp-card-terms-2025.json)
inspects 663 public product rows from the July–December 2025 Terms of Credit
Card Plans survey. Of 625 rows offering a purchase APR, the product-level
median advertised APR was 24.49%, with median listed minimum and maximum APRs
of 18.49% and 27.49%; 396 rows reported purchase APR variation by credit tier.
The file contains 149 introductory-APR offers, 236 balance-transfer offers,
654 late-fee fields, 113 numeric annual-fee fields with a $95 median, and 235
rows mentioning cashback rewards. These are unweighted plan terms, not market
shares or account outcomes.

**Supported subtheme:** advertised price, credit-tier segmentation, promotion,
fee, and reward design are separate upstream conditions for consumer borrowing.
The existence of a product menu does not show that a household can qualify,
obtain the low rate, avoid a fee, use a transfer, or capture a reward.  
**Not established:** approval, realized APR, balance, interest paid, late fee
paid, reward value, repayment, hardship, switching, or remedy. Product rows
are not cardholders, transactions, or market-weighted offers.

## 6b. A score can become part of the credit risk it is meant to predict

The [credit-score feedback record](records/us-nber-self-fulfilling-credit-scores-default-2026.json)
uses a fourteen-day inquiry-counting cutoff that can lower a U.S. consumer's
credit score by about five points without adding a new credit-report fact. In
the regression-discontinuity design, default did not respond among consumers
with clean records. Among consumers with prior derogatory marks, however,
default rose 3.2 percentage points over two years; the paper estimates that at
least 13% of the score–default relationship for that group was self-fulfilling.

**Supported subtheme:** a financial classification can become an active risk
channel for a defined higher-risk group. Reported score, lender decision,
credit availability, borrowing terms, and later default are distinct stages,
even when a score change itself has a causal downstream effect.

**Not established:** which lender changed an approval, rate, limit, or timing
decision; the relevant contract path; rent, insurance, work, utility, or
household consequences; later recovery; or a universal effect of every score
movement. The result is local to consumers near the inquiry cutoff.

## 6c. A bank account, a usable transaction route, and mainstream credit are different forms of consumer access

The [FDIC financial-access record](records/us-fdic-unbanked-underbanked-households-2023.json)
separates household account ownership from how a household transacts and
borrows. In 2023, 4.2% of U.S. households (about 5.6 million) were unbanked,
while 14.2% (about 19.0 million) were underbanked: they had an account but had
used at least one specified nonbank transaction or credit service during the
prior year. A further 15.7% of all households had no mainstream credit in the
survey's classification frame—78.4% among unbanked households and 13.0% among
banked households. These classifications do not say whether nonbank use was a
costly substitute, a deliberate convenience, or both.

The same source keeps digital transaction adoption and payment performance
separate. It reports 49.7% using a nonbank online payment service, 5.9% using
a prepaid card, and 3.9% using buy-now-pay-later; about one in eight
BNPL-using households reported a late or missed payment. Among unbanked
households, distrust of banks was the second-most-cited main reason for not
having an account. Different question universes mean none of those shares is a
common risk rate.

**Supported subtheme:** formal account access, payment-channel choice,
mainstream-credit visibility, and payment performance are related but distinct
consumer routes. A household can be banked while relying on nonbank services,
or can transact digitally while still lacking mainstream-credit access.

**Not established:** transaction fees, credit approval, pricing, liquidity,
account safety, geographic access, whether nonbank use improves or worsens a
given household's options, a causal role for trust, dispute or remedy outcome,
or later financial recovery.

## 6d. Account access, nonbank substitution, and post-fraud switching are different financial-security routes

The [banking-substitution and recourse record](records/us-federal-reserve-banking-substitution-recourse-2025.json)
uses 2025 Federal Reserve household-survey results to retain those routes as
separate conditional measures. Six percent of adults were unbanked, including
21% of adults with family income below $25,000 and 1% with income of at least
$100,000. Among banked adults, 12% reported an overdraft fee in the prior year
(17% for the under-$25,000 subgroup). Nonbank check-cashing or money-order use
was reported by 12% of all adults, 11% of banked adults, and 28% of unbanked
adults; use can be convenience, constraint, or both.

The same survey creates a distinct fraud-response path. Among adults reporting
non-credit-card fraud, 65% lost money, 35% had some money not recovered, 67%
communicated with a financial provider, 38% reported to an authority or credit
bureau, and 12% changed bank or financial provider. These are different
response actions and do not reveal a completed dispute or a safe alternative.

**Supported subtheme:** formal account status, transaction-channel
substitution, fee exposure, recovery burden, provider contact, reporting, and
provider change are separate consumer-power stages. Being banked does not make
the remedy or exit route observable.

**Not established:** provider responsibility, dispute success, timing,
individual account quality, transaction price or travel burden, whether a
provider change was feasible or protective, repeat fraud, trust change, or
durable financial recovery. The cross-sectional self-reports do not identify a
causal account or overdraft effect.

## 7. Removing a visible fee produces immediate relief, but later recovery depends on liquidity

The [bank-fee record](records/us-nber-bank-fees-household-financial-wellbeing-2017-2022.json)
uses transaction data and staggered large-bank NSF/overdraft policy changes.
Eliminating NSF fees immediately reduced charges across the income distribution.
Relaxed overdraft policies reduced fees mainly for wealthier, more liquid
customers; only that group later showed lower late fees, interest,
account-maintenance fees, and alternative-finance use. Financial stress did
not substantially fall among more vulnerable households.

**Supported subtheme:** a price protection can be broad at the charge stage
while its ability to restore room is filtered by pre-existing liquidity.
Immediate fee relief, a successful bill payment, and later financial recovery
are different outcomes.
**Not established:** the original bill or essential need, household tradeoffs,
the net value of overdraft access, causal effects for every bank, or welfare
after the observation window.

## 8. Fraud recourse includes money, recovery failure, and time spent fighting the incident

The [household-fraud record](records/us-federal-reserve-household-fraud-recovery-2024.json)
estimates that 21% of adults experienced financial fraud in 2024. Among adults
with non-credit-card fraud, 63% lost money and 32% had some unrecovered money;
the survey estimates $84 billion in loss, $21 billion recovered, and $63
billion in net direct consumer loss. About 30% spent ten or more hours dealing
with or recovering from the incident. These are self-reported weighted
estimates, not a verified case register.

**Supported subtheme:** a fraud outcome has at least three distinct consumer
currencies: direct money loss, unrecovered balance, and recovery labor. A
refund or provider contact cannot be read as resolving all three.
**Not established:** firm responsibility, remedy adequacy, later trust,
switching, or a causal consumer-protection effect; age comparisons do not
identify an age mechanism.

## 8a. A reported agency recovery is not a verified restored-security endpoint

The [linked HTOPS fraud-loss follow-up record](records/us-htops-fraud-loss-following-trust-2025.json)
follows April-to-June 2025 public-use respondents by exact identifier. It
retains 184 respondents reporting both exposure and money loss, 51 reporting
loss plus reporting, and only 11 reporting loss, reporting, and agency
recovery. In the last group, the later unable-to-pay-energy-bill screen was
78.80%, but the group is too small and selectively retained for that share to
serve as a population estimate or a recovery-effect test. The institution
items are retained as coded-response screens, not relabeled as high or low
trust.

**Supported subtheme:** a claimed recovery route can be observable in a panel
while its sample is too thin to demonstrate restored material security or an
institutional consequence. Loss, reporting, agency recovery, later bill
pressure, and trust are separate measurement stages.  
**Not established:** a dated fraud incident, who was responsible, repayment
amount or timing, agency action, a causal recovery effect, provider switching,
trust change, political action, or exit. The linked groups do not have equal
denominators and are not a sequence of comparable incident cohorts.

## 9. Payment choice can become a service-continuity issue when infrastructure fails

The [payment-resilience record](records/us-nber-payment-method-resilience-disaster-outages-2026.json)
links disaster/outage, transaction, scanner, and survey surfaces. Natural
disasters, especially hurricanes, were associated with persistent outages and
sharply lower expenditure; spending rose before disasters largely through
credit, then digital payments fell and cash use rose in outages. Nearly half
of surveyed consumers could not use their preferred electronic payment during
an outage, and greater cash access was associated with more completed
transactions.

The [Census incentive-payment preference record](records/us-census-incentive-payment-preferences-digital-cash-2026.json)
observes an earlier design stage rather than a disruption outcome. In a large
nonprobability survey, most respondents preferred electronic bank transfer or
digital gift cards for hypothetical $5 and $40 incentives, while about 5%
preferred physical cash at either amount. The source describes that smaller
cash-preferring group as mostly young, low-income, and without a college
degree. It does not disclose the abstract's exact sample count or establish
bank/device access, actual payment receipt, fees, privacy, or whether stated
preference predicts completed use.

**Supported subtheme:** payment access is part of consumer resilience, not just
a checkout preference. Digital availability, cash holdings, credit-financed
preparation, stated preference, and ability to complete a transaction become
different gates during a disruption or payment-design decision.
**Not established:** whether essential food, medicine, fuel, or care was
obtained, later debt repayment, household recovery, a representative cash
preference, or a universal cash-policy effect.

## 10. Time and opportunity cost are part of the price of an attention-intensive service

The [time-intensive platform record](records/us-nber-time-intensive-platform-consumption-2026.json)
reports two Facebook/Instagram field experiments that varied ad load, the
setting's primary user cost. Demand response was low-elasticity, and the
analysis treats substitution across online activity and offline time use as
part of platform competition. Its diversion and de-merger conclusions are
modeled; the authors disclose litigation work for Meta.

**Supported subtheme:** a zero-dollar consumer product can still carry a
meaningful price in attention and foregone online/offline alternatives. Low
response to ad load does not itself reveal high satisfaction, low harm, or a
lack of usable alternatives.
**Not established:** well-being, sleep, work/care displacement, dependence,
practical exit, realized consumer surplus, or the effect of an actual
structural separation.

## 11. Banking inertia can reduce competitive pressure while supporting deposit stability

The [banking-inertia record](records/us-nber-sleepy-deposits-switching-stability-2025.json)
uses account opening and closure data from more than 900 banks. Only about
5%–15% of depositors open a new account annually, and closures are more often
driven by moving or death than rate shopping. The authors model sleepiness as
about 57% of average deposit-franchise value, softening competition—especially
for low-quality banks in low-concentration markets—while also reducing modeled
default probabilities during 2023 turmoil. It does not observe each depositor's
rate gap, fees, needs, or reason for staying.

**Supported subtheme:** staying with a financial provider can have a dual
effect: it may weaken service/rate competition while supporting stable funding;
consumer switching is not a one-direction welfare measure.  
**Not established:** whether a specific depositor benefited or lost, why they
stayed, or whether safe switching is equally available.

## 12. A service-entry rule can change the worker pool without improving every measured consumer outcome

The [rideshare licensing record](records/us-nber-uber-occupational-licensing-consumer-outcomes-2026.json)
uses trip-level Uber data, a New York/New Jersey comparison, and Houston
deregulation. It finds no consistent evidence that licensing improved measured
ratings or telematics outcomes; after Houston deregulation, entrants were
indistinguishable on those measures from previously licensed drivers despite
age and experience differences. The study does not cover fares, wait times,
cancellations, rare severe incidents, disability access, worker income, or all
cities.

**Supported subtheme:** a consumer-protection rule can alter service entry
without establishing better average observed quality; worker screening,
consumer access, and safety are separate empirical endpoints.  
**Not established:** the value of licensing for serious incidents, price,
availability, accessibility, worker conditions, or trust.

## 13. A refund program has a payment-receipt funnel after eligibility is established

The [FTC refund-funnel record](records/us-ftc-refund-cashing-reissue-funnel-2024.json)
reports 4.35 million consumers sent first-distribution payments in 33 2024 FTC
cases, but 2.79 million had cashed a payment to date (64.2% in that table).
Across 25 programs closed in 2024, 65.7% of people sent a payment cashed at
least one, with $127.58 average returned per person. In the Amazon Flex
example, a Zelle reissue raised participation from 90.3% to 92.3%. Cashing and
channel reach are administrative endpoints rather than adequate compensation.

**Supported subtheme:** remedy delivery has its own sequence—eligibility,
contact, payment channel, receipt/cashing, reissue, and closure—between a
formal order and usable consumer recovery.  
**Not established:** whether any recipient was made whole, the underlying harm
was corrected, or later trust, use, switching, and household security changed.

## 13a. Housing-fee redress can distribute money while the renter's housing outcome remains unobserved

The [Invitation Homes renter-refund record](records/us-ftc-invitation-homes-renter-refunds-2026.json)
adds a lease-specific remedy route. The FTC reported more than $47.2 million in
checks sent to 444,131 eligible people in March 2026 after alleged undisclosed
smart-home and utility-management fees and alleged move-out charges for normal
wear, pre-existing damage, or renovations. The payment population excludes
people who had already received a credit or refund; checks sent and aggregate
distribution are not a cashing rate or a unique-household recovery measure.

**Supported subtheme:** an advertised price, a later lease or move-out charge,
and a consumer-protection payment are sequential housing-consumer events. A
large reported distribution makes a remedy program observable without turning
it into evidence of restored bargaining power or housing security.  
**Not established:** the payment amount or receipt for any renter, full
restitution, current rent burden, repair, eviction exposure, staying versus
moving, landlord switching, local alternatives, trust, or practical exit.

## 13b. A recall progress percentage can be an implementation field, not a completed safety outcome

The [CPSC recall-progress record](records/us-cpsc-recall-mpr-progress-heterogeneity-2026.json)
(`us-cpsc-recall-mpr-progress-heterogeneity-2026`)
uses a bounded August 2026 Monthly Progress Report snapshot of 17 selected
recall-key rows. Sixteen rows reported a numeric consumer-level correction
percentage ranging from 0% to 44%; one was 0% and one was blank. Reported
total correction ranged from 0% to 50%. The CPSC sheet itself notes that its
consumer-level denominator may differ from products recalled, and the rows
have different reporting durations, product scopes, and blank-field meanings.

**Supported subtheme:** a recall's notice, manufacturer/distributor/retailer
action, consumer-level progress field, and total correction field are separate
administrative stages. A percentage can make implementation visible without
identifying purchasers reached or safely restored.

**Not established:** a common recall completion rate, consumer exposure or
notice, appointment/repair/replacement receipt, safe use, residual cost,
comparative firm performance, trust, switching, or exit. This purposive
17-row snapshot is not a representative recall sample.

## 13c. A payment-processor refund can address an exit fee while practical replacement remains unobserved

The [First American payment-processor refund record](records/us-ftc-first-american-payment-processor-refunds-2026.json)
tracks an FTC remedy program for small businesses charged alleged hidden or
unauthorized fees, including early-termination and zombie charges. The FTC
reported more than $2.6 million distributed through checks sent to 5,588
businesses after a $4.9 million settlement; as of the record's January 2026
status, claims were still under review and the final refund amount depended in
part on the number of businesses filing. Eligible businesses are a
remedy-program population, not a representative small-business sample.

**Supported subtheme:** payment processing can create an exit-cost route:
enrollment, fee, attempted departure, enforcement, payment delivery, and
receipt are separate stages. A remedy can make a disputed fee observable while
the alternative-provider and business-continuity question remains open.
**Not established:** individual payment amount or cashing, fee incidence,
successful switching, processor alternatives, transaction capacity, customer
relationships, revenue, business survival, full restitution, or durable trust.
The record does not turn an exit-fee allegation into proof that every business
was unable to leave.

## 14. Broker consent can fail before a consumer can contest a health-plan change

The [Marketplace broker-consent record](records/us-gao-marketplace-broker-consent-2026.json)
finds federal Marketplace agents/brokers must be licensed and registered, but
CMS consent controls were weak: access was not limited to an already-associated
broker, consumers were not informed of all actions, newer procedures were not
always used, and identity confirmation was limited. Confirmed unauthorized
enrollment/plan-switch complaints grew more than fourfold from 2023 to 2025;
at least 160,000 2024 applications had likely unauthorized changes. Selected
state marketplaces used stronger controls such as one-time passcodes. The
record does not show final resolution or coverage duration.

**Supported subtheme:** formal representation, valid consent, plan continuity,
notice, correction, and care access are sequential consumer-control stages—not
one broker relationship.  
**Not established:** national prevalence, lasting coverage loss, care
disruption, financial harm, or trust after correction.

## 14a. Reported insurance friction is paired with care and bill problems, but the event order is not observed

The [MEPS denial and prior-authorization friction record](records/us-meps-2024-event-institutional-friction.json)
joins people with a first dated 2024 office, emergency-room, or inpatient event
to an annual report of insurance denial or prior-authorization delay. For the
office-event group, reported care delay was 15.6% among people reporting that
friction versus 5.8% among those not reporting it; the respective medical-debt
shares were 24.9% and 13.3%, and bill-problem shares 16.2% and 5.9%. The
pattern is also visible in the emergency-room and inpatient strata. Each is a
weighted same-round comparison, not a claim-level sequence: the annual
friction screen has no decision date, claim identifier, appeal, or resolution.

**Supported subtheme:** an institutional consumer-control problem can coexist
with delayed care and constrained financial room across observed care-event
channels. Event occurrence, plan decision, authorization process, clinical
care, bill, debt, appeal, and remedy are different consumer stages.
**Not established:** that denial or authorization delay preceded the selected
event, caused care delay, debt, or a bill problem; the effects of private
coverage; or later care completion, health, repayment, plan correction, trust,
switching, or exit. Severity, prior debt, coverage, and service selection can
generate both reported friction and the observed outcomes.

## Cross-subtheme finding and next test

The [CPSC recall-implementation record](records/us-cpsc-vrurc-recall-implementation-2023-2026.json)
shows why a recall remedy needs its own realization ledger: a 2023 notice for
about 190,000 chargers offered free replacement after a reported fire, while a
2026 progress row reported 64,963 consumer-level corrections but used a
256,845-product denominator. The mismatch may reflect valid scope or
denominator differences. A notice, a firm-reported correction, replacement
receipt, safe restoration, and consumer recovery remain distinct endpoints.

```text
offer, default, fee, search result, screening rule, consent, or system disruption
  -> understanding, liquidity, attention, payment availability, comparison, and control
  -> payment, contract, application, complaint, cancellation, appeal, or recovery effort
  -> correction, refund, alternative, remaining loss, and time cost
  -> trust, future use, exit, and firm response
```

Most public sources observe an early or middle stage. The next decisive records
need a consumer- or case-linked sequence that retains the offer encountered,
information and comparison route, charge or decision, effort and time cost,
complaint or cancellation attempt, remedy receipt, residual loss, alternative
service, and later use or trust.

## Related atlas surfaces

- [14-theme readout](US-BROAD-CURRENT-14-THEME-READOUT_V1.md)
- [source-led platform subtheme map](US-BROAD-PLATFORM-SOURCE-LED-SUBTHEME-MAP_V1.md)
- [consumer recourse synthesis](projects/us-customer-automation-recourse/consumer-recourse-visibility-remedy-synthesis-v1.md)
- [source-promotion audit](US-BROAD-SOURCE-PROMOTION-AUDIT_V1.md)
