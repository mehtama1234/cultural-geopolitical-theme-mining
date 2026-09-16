# Utility pressure changes the option stack across housing, work, and care

**Checked:** 2026-09-15  
**Status:** same-person SIPP cross-lag synthesis with Fay-BRR uncertainty; no causal claim

## The question

When a household reports difficulty paying utility bills, does the pressure
appear in a single outcome, or does it occupy a wider option stack involving
housing tenure, work movement, child-care arrangements, and resource changes?
The corrected 2025 SIPP full-file slice can place several of these measures on
the same person-month frame, while preserving the fact that they are not all
measured on the same clock.

The safe chain is:

```text
utility-payment difficulty at month t
  + housing tenure and work-limiting status
  -> next-month earnings/hours or resource/job movement
  -> annual child-care work-prevention report
  -> household room and care alternatives [partly observed]
  -> health, stability, recovery, and trust [open]
```

## What the same-person estimates show

The adjacent-month utility/tenure screen finds hours movement in roughly 7.6%
of utility-difficulty pairs for both owners/buyers and renters, compared with
4.93% for owners/buyers without reported difficulty and 5.96% for renters
without difficulty. The contrast is not a simple tenure story: within the
difficulty cells the renter and owner/buyer estimates are close.

The separate utility/tenure/care screen reports annual child-care work
prevention of 9.35% among utility-difficulty owners/buyers and 8.13% among
difficulty renters, compared with 2.84% and 5.01% in the corresponding
no-difficulty cells. The difficulty cells are small, and this annual fall
care measure should not be read as a monthly response to a utility bill.

The corrected resource/job/work-limitation cross-lag adds a reverse-direction
contrast: among work-limited respondents, next-month resource-band movement
is 4.77% for owners/buyers with one job and 6.12% for renters with one job;
for two-job cells it is 3.53% and 7.37%, respectively. The latter cells are
small and are retained as a watchpoint, not a stable ranking. Resource-band
movement has no direction here—it may be improvement, deterioration, or a
threshold crossing.

## Why the clocks must remain separate

The utility condition and tenure are observed on the monthly person-month
frame. Earnings and hours movement is measured in the following month. The
child-care work-prevention field belongs to an annual fall reference-parent
universe, conditioned on a December utility and tenure surface. It can be
placed beside the monthly result as a compatible option-stack layer, but it
cannot be called the next-month care response.

| Surface | Unit and clock | What it adds | What remains open |
|---|---|---|---|
| Utility difficulty + tenure | Person-month at *t* | Household condition and housing arrangement | Exact bill, arrears, shutoff, and payment timing |
| Earnings/hours movement | Same person at *t+1* | Short-run work-transition surface | Direction, desired hours, job quality, schedule control |
| Resource/job cross-lag | Same person at adjacent months | Resource and job-count movement conditioned on work limitation and tenure | Whether movement protected or sacrificed care/security |
| Child-care work prevention | Reference-parent annual fall measure | Reported care alternative constraint | Monthly timing, care intensity, provider quality, replacement support |

This separation prevents a common interpretive error: observing a household
condition and a later work or care measure does not identify a dated bill-to-
choice pathway. It does, however, show why a single “financial burden” score
would conceal different responses.

## Counterexamples and interpretation

- A renter and owner/buyer can show similar hours movement under utility
  difficulty while facing different rent, repair, insurance, or mobility risks.
- A household with no reported utility difficulty can still lack child-care
  alternatives or sacrifice food, savings, health, or rest.
- Higher earnings movement does not mean greater security; earnings may rise
  or fall, and a resource-band change has no direction in this output.
- Work limitation may change both the exposure and the available response;
  it is not a diagnosis of disability, nor evidence of accommodation.
- Utility difficulty is not a shutoff event, and child-care work prevention is
  not a measured monthly loss caused by the utility condition.

The relevant interpretation is therefore an option-stack pattern: housing
tenure and work limitation condition the ways material room moves, while care
constraints appear on a separate annual surface. The pattern is compatible
with constrained alternatives, but selection, seasonality, labor demand,
household composition, health, and reporting differences remain plausible
explanations.

## Smallest decisive next test

The next design should identify a dated utility bill, shutoff warning,
reconnection, or assistance decision and follow the same person/household at
one-, three-, and six-month windows. It should retain tenure, work limitation,
child-care provider/payment/help, care hours, work schedule, earnings,
utilities, food, housing, health, and recovery. The required counterexample is
a similar bill condition with a protected outcome because of payment help,
flexible work, nearby care, or another provider—not merely a person with a
different annual income band.

## Sources and reproduction

- [Utility difficulty, tenure, and next-month work movement](sipp-utility-work-tenure-following-layer-v1.md)
- [Utility difficulty, tenure, and child-care work prevention](sipp-utility-tenure-childcare-layer-v1.md)
- [Housing tenure and monthly transition surface under work limitation](findings/us-household-calendar-integration-040.md)
- [SIPP material/time/care acquisition plan](material-time-care-linkage-acquisition-plan-v1.md)
- [2025 SIPP public-use data](https://www.census.gov/programs-surveys/sipp/data/datasets/2025-data/2025.html)

The component analyses use `WPFINWGT` and 240 Fay-BRR replicate weights. Their
machine-readable outputs preserve separate valid-record denominators, output
hashes, and status-flag boundaries. Reproduction requires the authenticated
full-file slice and replicate archive under the paths documented in each
component memo; no raw SIPP archive is committed.

