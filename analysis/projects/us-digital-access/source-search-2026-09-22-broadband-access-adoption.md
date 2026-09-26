# Source search: broadband availability, adoption, and choice

**Search date:** 2026-09-22  
**Geography:** United States  
**Status:** bounded pass complete; technical availability is not the same as subscription or practical choice

## Working question

If a household is inside a broadband service area, what still has to happen
before the connection becomes usable access?

## Opening sources

| ID | Source | What it tells us | Status | Limit |
|---|---|---|---|---|
| US-FCC-SECTION706-2024 | [FCC 2024 Section 706 report](https://docs.fcc.gov/public/attachments/FCC-24-136A1.pdf) | FCC reports adoption and provider-choice measures, including their denominators and speed thresholds. | Official FCC report | It does not show a household’s bill, device, reliability, actual use, or benefit from connection. |
| US-FCC-CONNECT2HEALTH-2025 | [FCC broadband data definitions](https://c2h.fcc.gov/bh-data.html) | FCC’s current mapping platform keeps access, adoption, speed, provider count, devices, and rural access as distinct measures. | Official FCC data documentation | The platform’s definitions are not a household-level longitudinal outcome. |

## First pattern

```text
service available at a location
  -> household can subscribe at a qualifying speed
  -> price, provider choice, device, reliability, and actual use
  -> [open] work, education, health, social connection, and civic benefit
```

FCC reports that at year-end 2023 about 53% of households subscribed to fixed
terrestrial broadband at the 100/20 Mbps benchmark when that service was
available; about 26% subscribed at the 940/500 Mbps long-term goal when it was
available. For year-end 2022, FCC reported 7.9% of households had no terrestrial
fixed provider offering 100/20 Mbps, while 37.4% had one provider, 36.6% had
two, and 18.2% had three or more under the report's combined wireline/fixed-
wireless comparison.

## Counterpoint to keep visible

The 53% figure is not the share of all households with broadband and not a
service-quality or affordability rate. It is adoption among households where
qualifying service was available. Provider count does not prove a meaningful
substitute, and availability does not prove a successful installation or stable
use.

## Decision rule

Keep map availability, speed, subscription, provider choice, price, device,
reliability, installation, actual use, and downstream benefit separate. Reopen
this lane only with a household or location-linked record that adds cost,
service quality, and use.
