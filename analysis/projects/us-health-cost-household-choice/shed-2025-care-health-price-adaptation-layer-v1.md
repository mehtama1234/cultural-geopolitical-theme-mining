# SHED 2025 care, health, and price-adaptation layer v1

**Checked:** 2026-09-12  
**Unit:** US adult respondent; 2025 Federal Reserve SHED  
**Method:** weighted descriptive percentages using `weight`; each measure uses its own nonmissing denominator; no design-based standard errors or causal estimate

## The question

Does financial pressure take a different form when people face medical-cost
concerns, unpaid adult care, poorer health, or outside help with medical bills?
This adds care and health to the broader societal adaptation map. It does not
claim that health caused the financial response or reduce care to one household
story.

```text
health need, care responsibility, or medical cost
  -> money, time, coverage, and work constraints
  -> substitution, reduced use, saving cuts, borrowing, delay, or extra work
  -> unpaid care, family help, food/housing tradeoff, health, and security
  -> public-system demand, firm response, trust, and political meaning
```

## Medical-cost concern

| Medical debt/affording care concern | Prices worsened finances | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Worked more/got job | Three-month funds |
|---|---:|---:|---:|---:|---:|---:|---:|
| Not a concern | 43.6 | 50.2 | 45.9 | 33.6 | 10.3 | 11.0 | 65.1 |
| Minor concern | 61.4 | 66.6 | 64.7 | 46.6 | 17.0 | 18.2 | 51.0 |
| Major concern | 77.4 | 81.5 | 78.8 | 58.3 | 27.8 | 26.6 | 39.4 |

The gradient is strong across reported medical-cost concern: respondents with a
major concern report more substitution, reduced use, saving cuts, borrowing,
and extra work, with less emergency capacity. This is an alignment between
medical-financial concern and price adaptation, not evidence that a particular
medical bill caused a particular response.

## Unpaid adult care

| Regularly provides unpaid care to an adult relative/friend | Prices worsened finances | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Worked more/got job | Three-month funds |
|---|---:|---:|---:|---:|---:|---:|---:|
| No | 55.8 | 61.0 | 57.8 | 40.2 | 14.6 | 15.5 | 55.7 |
| Yes | 65.8 | 68.1 | 68.7 | 46.5 | 22.2 | 24.0 | 50.6 |

Respondents reporting regular unpaid adult care also report more reduced use,
borrowing, and additional work. Care is therefore a possible mechanism that
links health cost to both money and time. The cross-sectional source does not
show the care hours, recipient's condition, who else helped, or which need was
displaced.

## Self-rated health

| Self-rated health | Prices worsened finances | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Worked more/got job | Three-month funds |
|---|---:|---:|---:|---:|---:|---:|---:|
| Excellent | 46.2 | 51.2 | 49.9 | 34.0 | 8.4 | 14.2 | 66.5 |
| Very good | 52.1 | 56.5 | 54.1 | 37.7 | 10.4 | 15.5 | 65.7 |
| Good | 59.8 | 62.3 | 59.8 | 43.7 | 16.2 | 16.2 | 54.8 |
| Fair | 68.3 | 70.9 | 66.7 | 49.5 | 22.3 | 16.0 | 40.5 |
| Poor | 66.3 | 66.7 | 70.3 | 53.2 | 28.4 | 13.0 | 26.6 |

The health gradient is clearest for reduced use, borrowing, saving cuts, and
emergency capacity. Lower additional-work percentages among people reporting
poor health should not be read as lower pressure: health limitations may reduce
the ability to respond through labor.

## Outside help for medical expenses, debt, or insurance

| Received outside medical help in prior 12 months | Prices worsened finances | Cheaper products | Used less/stopped | Reduced savings | Increased borrowing | Worked more/got job | Three-month funds |
|---|---:|---:|---:|---:|---:|---:|---:|
| No | 57.0 | 61.2 | 58.6 | 40.7 | 14.8 | 16.1 | 56.0 |
| Yes | 66.5 | 77.9 | 75.9 | 57.8 | 32.5 | 30.6 | 36.7 |

Outside help is a response and a marker of need, not proof of recovery. The
group receiving help reports more adaptations and less emergency capacity;
this cannot tell whether help prevented an even worse outcome, arrived after a
crisis, or transferred cost to family, friends, charities, or another system.

## What this adds to the broad societal program

1. **Medical cost is a distinct pressure channel.** It aligns with consumer
   adaptation more strongly than a generic “prices are high” label, but exact
   events and direction remain open.
2. **Care converts money into time and labor.** Unpaid adult care and additional
   work can coexist, suggesting that social reproduction may absorb pressure
   through both paid and unpaid time.
3. **Health can constrain the adaptation menu.** Poor-health respondents report
   less additional work but more borrowing, reduced use, and lower buffers; the
   available response is not simply “work more.”
4. **Help can signal protection and unresolved exposure.** Outside medical help
   may protect care while also showing that the household could not absorb the
   cost alone.
5. **Downstream meaning remains separate.** These patterns do not establish
   trust, stigma, blame, firm exit, public demand, or political action.

## Arrow ledger

| Arrow | Status | Safe current conclusion | Missing test |
|---|---|---|---|
| Medical-cost concern → financial adaptation | Reported / Compared | Major concern aligns with more substitution, reduced use, saving cuts, borrowing, and extra work | Dated bill, coverage, price, care need, and response for the same person |
| Unpaid care → money/time pressure | Reported / Compared | Caregivers report different adaptation and work patterns | Care hours, recipient need, paid help, family transfer, and displaced work/social time |
| Health limitation → adaptation capacity | Compared / Open | Health categories show different menus, including less additional work in poor health | Functional limitation, job control, care cost, coverage, and later outcome |
| Outside help → security/recovery | Open | Help coexists with substantial adaptation and lower buffers | Amount, source, timing, counterfactual need, and later food/health/debt recovery |
| Adaptation → trust, institutional demand, or political action | Open | Care/financial pressure is a material exposure layer | Attribution, dignity, stigma, source, trust, complaint, exit, and action |

## Next bounded test

Follow a dated medical or caregiving event through coverage, quoted and final
cost, paid and unpaid care, work hours, food/housing/transport tradeoffs, debt,
outside help, health, and recovery at one, six, and twelve months. Compare
people with similar care need but different insurance, cash buffer, job
control, family support, and local access. Include a counterexample where a
major concern did not produce borrowing or reduced use, and a case where help
arrived but the underlying health or time loss persisted.

## Reproduction and limits

```text
python3 scripts/analyze_shed_price_pressure_care_health.py \
  --input /path/to/SHED_2025.csv.zip \
  --output /tmp/shed-price-pressure-care-health.json
```

The raw file has 12,934 respondent rows. The measures are self-reported and
cross-sectional; medical concern, care, health, and outside-help questions have
different nonmissing universes. No standard errors are calculated here, and
the tables do not identify a household bill, a causal health event, care
quality, or later recovery. The analysis uses the official [Federal Reserve
SHED data release](https://www.federalreserve.gov/consumerscommunities/shed_data.htm).
