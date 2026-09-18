# Finding 002: A recall remedy can move safety work and proof onto the consumer

**Status:** provisional current CPSC remedy-design finding · **Checked:** 2026-09-17
**Unit:** public product-recall notice and remedy instructions; not an affected-consumer sample

## The bounded finding

The current CPSC recall pages show that a safety intervention is not complete
when a notice is posted or a remedy is named. In several current notices, the
consumer must stop using the product, register with the firm, destroy or
dispose of it, upload photographic proof, and then wait for a refund,
replacement, credit, or repair. One current notice also says a previous repair
was ineffective and offers a new professional repair. These instructions make
the consumer’s effort, evidence, disposal capacity, and access to the remedy
part of the safety system.

This is not evidence that any named consumer completed the process. It is a
source-level finding about remedy design and implementation burden:

```text
hazard notice
  -> stop use / isolate product
  -> register, contact firm, destroy, dispose, or document
  -> refund, replacement, credit, repair, or new instruction
  -> [open] receipt, safety restoration, residual cost, repeat failure,
     trust, repeat purchase, or exit
```

## What the current notices expose

| Current CPSC notice | Stated remedy path | Consumer-side work or risk | What is not observed |
|---|---|---|---|
| Melissa & Doug fire-truck activity board, about 84,000 units | Register for a free replacement, a $30 check, or a $40 store credit; remove batteries, mark the product, cut the hose, upload a photo, and dispose of it | Registration, product modification, destruction, proof upload, disposal, and choice among remedies | Whether purchasers saw the notice, completed registration, received the selected remedy, or bought another product |
| Sauna360 Tylö Halmstad and Kiruna hybrid saunas, about 6,000 units | Stop use and contact the firm for a free professional retrofit; the notice says the prior 2025 repair was ineffective | A repeat safety event after an earlier repair; arranging access to a professional installer and interrupting use | Which households received the first repair, experienced harm, obtained the second repair, or remained exposed |
| Colerinsec magnetic toy sets, about 38,507 units | Take away from children, stop use, contact the firm for a full refund, destroy the toy, and submit a disposal photo | Immediate child-safety action, destruction, proof, and disposal before refund | Awareness, refund receipt, disposal cost, replacement, injury avoidance, or secondary-market circulation |
| SHEIN Montessori teething toys, about 644 units | Stop use, take away from children, cut the silicone strings, send a photo, and dispose of the toy to receive a refund | Destruction and evidence requirements, with a platform/retailer contact route | Consumer notice reach, response, refund, replacement need, or continued availability elsewhere |
| LANCHEZ pressure washers, 329 units | Unplug, cut the power cord, send a photo showing the model number, and dispose of the product for a full refund | A potentially hazardous product must be made unusable by the consumer before remedy | Whether the consumer can safely destroy it, pays for disposal, receives funds, or loses needed equipment |

The notice page is a live source. CPSC states that its recall data are updated
weekly as new notices are announced and that recall-remedy data may change
daily with company operating status or remedy availability. The examples are
therefore a current design sample, not a fixed historical cohort. Counts of
units are recalled units, not verified exposed households or remedy claims.

## What this adds to the broad map

### 1. Remedy access has an operational price

A nominal “full refund” may require a consumer to find the notice, identify the
model, stop use, contact the firm, destroy the item, dispose of it, and prove
the action. That can impose time, documentation, disposal, replacement, and
safety costs before any payment arrives. A replacement or store credit may
protect product value differently from a cash refund. These are not equivalent
forms of recovery.

The burden is especially visible when the product is large, installed,
essential, expensive to replace, or unsafe to handle. The public notice does
not reveal whether local disposal is free, whether the consumer has transport,
whether the product is needed for work or care, or whether the firm provides a
safe collection route. Those missing fields are part of the consumer-power
question, not administrative trivia.

### 2. “Repair” is not a single stable endpoint

The Sauna360 notice is a useful temporal counterexample. A previous repair did
not end the safety story; the company now offers another repair with a
professional installer. A repair can therefore be nominally completed while
the hazard persists or the fix proves inadequate. The relevant endpoint is not
repair offered or repair attempted but verified safe restoration and durable
non-recurrence.

This matters for the broader atlas’s institutional-remedy vocabulary. An order,
notice, refund offer, repair, replacement, or instruction is a different stage
from receipt, correction, safety, household recovery, trust, and exit.

### 3. Proof requirements create an evidence asymmetry

The firm and regulator can observe a submitted photograph or registration, but
the public notice does not provide a denominator for all exposed consumers or
all eligible units. The public record can therefore show that a remedy route
exists and perhaps how many units were recalled without showing the share that
successfully converted exposure into safe recovery.

Photo proof may reduce fraud and help a firm verify disposal, but it can also
exclude consumers with limited connectivity, limited time, inaccessible
interfaces, language barriers, privacy concerns, or no safe way to destroy the
product. A proof requirement is thus both a control mechanism and a possible
access barrier. The notice alone cannot determine which effect dominates.

### 4. Consumer choice is structured, not frictionless

The Melissa & Doug notice offers a replacement, a check, or store credit, but
the values differ. Choice is therefore not simply “remedy available”; it is a
decision under product need, liquidity, inconvenience, trust, and future use.
The record does not show whether consumers preferred cash, whether credit
kept them tied to the seller, or whether replacement preserved a needed
function. Those are the cultural and consumer-power endpoints the next data
layer should measure.

## What is measured and what is not

The notices support the following source-level classifications:

```text
recall posted              = measured institutional warning
units listed               = measured recalled-product scale
remedy described           = measured offered route
consumer action instructed = reported required action
consumer action completed  = not observed here
remedy received            = not observed here
safe restoration           = not observed here
avoided harm               = not observed here
trust / repurchase / exit  = not observed here
```

The CPSC Recall Data API and the recall page provide machine-readable and
searchable product-level fields such as recall identity, date, manufacturer,
product, units, hazard, injury, remedy, and remedy option. CPSC also publishes
Monthly Progress Reports supplied by recalling firms. The existence of those
fields makes a product-level implementation study feasible, but it does not
make the consumer-level denominator or receipt observable by itself.

## Counterexamples and limits

- A free professional repair may impose less consumer effort than destruction
  and photo proof; remedy burden varies by product and route.
- A refund, replacement, and store credit can have different economic value;
  the notice cannot tell us which is adequate for a particular household.
- The current page is dynamic. A remedy can become unavailable or change as a
  company’s operating status changes, so a later recheck may not reproduce the
  same wording or counts.
- Recalled units are not purchasers, exposed households, claims, payments, or
  avoided injuries.
- A destruction instruction can reduce secondary-market exposure while also
  shifting disposal cost and safety risk to the consumer.
- A second repair notice does not prove that the first repair failed for every
  unit or that the new repair will be durable.
- The examples are selected from current notices and cannot estimate the
  prevalence of proof requirements or remedy failure across all recalls.

## Next decisive test

Use one small product cohort and join product-level recall records to monthly
progress reports and, where lawfully available, a consumer-facing contact or
remedy ledger:

```text
product/model/UPC and exposure route
  -> notice date and notice channel
  -> consumer awareness and stop-use action
  -> registration/contact, effort, destruction/disposal, and alternative
  -> refund/replacement/repair offered and received
  -> delay, residual cost, injury or avoided harm, repeat repair
  -> trust, repurchase, seller/platform switching, complaint, or non-use
```

The first storage-light acquisition should use one recall family and one
bounded Monthly Progress Report file, inspect the sheet schema and reporting
periods, and filter locally to the recall number before retaining any derived
rows. Do not download the full historical dataset until the report contains a
recall key, eligible-unit denominator, action/receipt fields, and a defensible
estimand. If those fields are absent, retain the exact absence as an
implementation boundary rather than promote aggregate recall-response rates as
consumer recovery.

## Provenance and storage boundary

This pass read the official CPSC recall and data pages only. No CPSC report PDF,
full recall export, or Monthly Progress Report workbook was downloaded. The
current examples and remedy wording should be rechecked before any quantitative
use because the source is live and remedy data can change daily.

- [CPSC recalls and product safety warnings](https://www.cpsc.gov/Recalls)
- [CPSC data/API page](https://www.cpsc.gov/es/node/49820)
- [CPSC monthly progress reports](https://www.cpsc.gov/Data/Monthly-Progress-Reports)
- [CPSC Recall API information](https://www.cpsc.gov/es/node/5808)
