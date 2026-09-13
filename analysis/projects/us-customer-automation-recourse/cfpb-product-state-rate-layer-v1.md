# CFPB product × state complaint-rate layer v1

**Checked:** 2026-09-13  
**Source:** CFPB Consumer Complaint Database API, product-filtered 2024 published records; Census 2024 resident-population estimates  
**Unit:** published complaint record normalized by resident population  
**Status:** place/product visibility comparison; not a consumer-harm, market-share, or remedy rate

## Why this is a different layer

The earlier geography layer showed that total published complaint counts differ
by state. That total is dominated by credit-reporting records. This pass asks a
narrower question: does the visible complaint geography change when the product
is held approximately constant?

```text
financial product and local context
  -> complaint access, product exposure, and issue mix
  -> published complaint record
  -> company response and possible remedy
```

Only the published-record arrow is measured here. A state rate is not the rate
at which residents were harmed, complained, received relief, or switched.

## Calculation

For each product slice:

`published complaints in state / Census resident population in 2024 × 100,000`.

The API returned state aggregations for each product. The comparison retains
the 50 states and Washington, D.C.; territories, military codes, and other
non-state codes are excluded from the denominator comparison. The product
filters were:

- Credit card: 76,109 published records;
- Checking or savings account: 52,901;
- Mortgage: 21,474;
- Debt collection: 156,242;
- Student loan: 14,685; and
- Vehicle loan or lease: 13,378.

## Highest published-record rates by product

| Product | Highest state/rate | Second | Third |
|---|---|---|---|
| Credit card | DC 65.4 / 100k (459) | DE 38.5 (405) | NV 33.3 (1,087) |
| Checking/savings | DC 49.1 (345) | NV 24.8 (809) | GA 23.3 (2,608) |
| Mortgage | DC 20.5 (144) | MD 13.3 (836) | DE 12.8 (135) |
| Debt collection | GA 114.6 (12,812) | TX 83.8 (26,230) | FL 77.7 (18,150) |
| Student loan | DC 18.7 (131) | MA 7.7 (552) | MD 7.2 (449) |
| Vehicle loan/lease | DE 10.0 (105) | GA 9.9 (1,104) | DC 9.7 (68) |

The DC, Delaware, and Nevada values demonstrate why both rate and count must
be shown. A high normalized rate can rest on a small number of records, and
state of complaint is not necessarily state of residence or product use. The
debt-collection pattern is materially different from the credit-card and
mortgage patterns: Georgia, Texas, and Florida have both high normalized rates
and much larger counts in this snapshot.

## What this adds to the societal map

1. **Consumer problems are product-shaped and place-shaped.** Holding product
   approximately constant changes the geography of recorded visibility.
2. **Institutional access is part of consumer culture.** Awareness, digital
   access, language, legal help, firm exposure, and expectations about remedy
   can all affect whether a problem becomes a CFPB record.
3. **A firm or regulator should not read a national average as universal.**
   Product-specific local patterns identify where issue mix, servicing,
   customer composition, or complaint access needs examination.
4. **The counterexample remains important.** A high complaint rate may reflect
   stronger reporting and access rather than worse underlying service; a low
   rate may reflect dependence, low awareness, or inability to escalate.

## Arrow ledger

| Arrow | Status | Safe conclusion | Missing evidence |
|---|---|---|---|
| Product/place → published complaint visibility | Compared | Product-specific state rates differ substantially | Customer/account denominators, issue mix, access, and residence validation |
| Complaint → company response | Available in CFPB fields | Response and timeliness can be cross-tabbed in a case-level extract | Verified adequacy and follow-through |
| Response → remedy or exit | Open | A response label is not a consumer outcome | Repeat contact, dispute, account closure, switching, later finances |
| Place/product pattern → cultural meaning or politics | Open | Geography identifies a sampling frame for trust and attribution work | Same-case meaning, source, organizing, and political action |

## Limits

- Complaint counts are published records, not all complaints and not all harm.
- Population is a rough denominator; product ownership and account exposure are
  not resident-population counts.
- State codes may represent mailing, residence, or other reporting conventions;
  they should not be treated as precise local incidence without field auditing.
- Product categories and complaint systems changed over time; this is a 2024
  snapshot, not a trend by itself.
- No causal comparison or ranking of states, products, firms, or consumers is
  justified from these rates.

## Reproduction

```text
python3 scripts/analyze_cfpb_product_state_rates.py \
  --population /tmp/census-pop-2024.xlsx \
  --slice credit-card=/tmp/cfpb-credit-card-2024.json \
  --slice checking-savings=/tmp/cfpb-checking-savings-2024.json \
  --slice mortgage=/tmp/cfpb-mortgage-2024.json \
  --slice debt-collection=/tmp/cfpb-debt-collection-2024.json \
  --slice student-loan=/tmp/cfpb-student-loan-2024.json \
  --slice vehicle-loan=/tmp/cfpb-vehicle-loan-2024.json \
  --output /tmp/cfpb-product-state-rates-2024.json
```

Related: [CFPB complaint-response layer](cfpb-complaint-response-descriptive-layer-v1.md),
[CFPB geography-normalized layer](cfpb-state-population-normalized-layer-v1.md),
and the [consumer recourse/exit bridge](consumer-recourse-power-exit-cross-source-bridge-v1.md).
