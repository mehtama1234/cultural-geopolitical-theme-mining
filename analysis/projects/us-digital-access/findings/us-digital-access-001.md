# Finding 001: Broadband being available does not mean a household can use it

**Status:** bounded digital-infrastructure and practical-access finding · **Checked:** 2026-09-22

## The finding in simple words

FCC reports that at the end of 2023 about 53% of households subscribed to
100/20 Mbps fixed terrestrial broadband when that service was available. That
does not mean only 53% of all households had broadband. It means the denominator
already excludes places where the service was not available.

FCC's 2022 provider-choice comparison also found that 7.9% of households had
no provider offering 100/20 Mbps, 37.4% had one, 36.6% had two, and 18.2% had
three or more under its combined wireline/fixed-wireless measure.

The practical route is:

```text
service advertised as available
  -> qualifying subscription
  -> price, provider choice, device, installation, and reliability
  -> actual use for work, school, health, connection, or civic life [open]
```

## What this adds to the broader atlas

This adds a digital version of the atlas's recurring “on paper versus usable”
pattern. A map can show a service area, and a provider can report an available
speed, while a household still faces price, device, installation, quality, or
switching barriers.

It also makes competition more concrete. Multiple providers on a map do not
automatically create a meaningful alternative if prices, contracts, quality,
or installation make switching unrealistic.

## Limits and counterexamples

- The 53% adoption figure uses a conditional denominator: households where
  qualifying service was available.
- Provider count is not the same as affordable or substitutable choice.
- Advertised speed is not measured delivered speed or reliability.
- The record does not follow a household into work, education, health, social
  connection, or civic outcomes.
- The adoption and provider-choice figures use different years and should not be
  read as one same-year household sequence.

## Next decisive test

Use a location- or household-linked record joining exact availability, quoted
price, installation, device access, delivered reliability, subscription,
switching, and downstream use. Preserve non-use, failed installation, and
successful use as separate outcomes.

## Sources

- [FCC 2024 Section 706 report](https://docs.fcc.gov/public/attachments/FCC-24-136A1.pdf)
- [FCC Connect2Health broadband data definitions](https://c2h.fcc.gov/bh-data.html)
- [Machine-readable record](../../../records/us-fcc-broadband-availability-adoption-choice-2022-2025.json)

**Evidence status:** official FCC data establish separate availability,
adoption, and provider-choice measures; price, quality, installation, actual
use, and downstream benefit remain open.
