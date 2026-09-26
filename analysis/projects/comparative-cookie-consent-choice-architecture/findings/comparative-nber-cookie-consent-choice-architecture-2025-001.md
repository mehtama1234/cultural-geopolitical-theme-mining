# Finding 001: Consent interface friction changes observed data-sharing choices

**Status:** bounded comparative platform and privacy-interface finding · **Checked:** 2026-09-23

## The bounded finding

NBER Working Paper 34025 combines a field experiment on cookie-consent banners
with survey and structural analysis. Without design manipulation, users accept
all cookies more than half the time. Placing options behind extra clicks shifts
users toward options that are easier to access, and many users dismiss banners
without making an explicit choice. The structural analysis reports that
browser-level consent can have larger modeled welfare gains than optimizing
site-specific banners because it removes repeated decision time.

```text
consent interface and default
  -> clicks, attention, comprehension, and dismissal
  -> data-sharing choice
  -> [open] actual data use, privacy, fraud, welfare, trust, and exit
```

## What this adds to the atlas

This identifies attention and repeated-decision time as practical currencies of
privacy control. It complements the browser-defaults finding: nominal choice
can change usage, while consent architecture can change the effort and path
through which a user makes—or fails to make—a data-sharing choice.

## Limits and next test

- The abstract does not provide the full experiment denominator or all user,
  site, device, and accessibility details.
- Acceptance, dismissal, or easier clicks do not prove informed consent or
  actual privacy protection.
- Browser-level welfare results are structural-model estimates, not observed
  long-run consumer-surplus or trust outcomes.
- The comparative online setting does not establish U.S. population effects or
  universal platform behavior.

The next decisive test is a user-level panel joining interface exposure,
accessibility, clicks, comprehension, consent, actual data sharing, downstream
use, fraud or targeting, time cost, complaint route, trust, and switching or
non-use.

## Source

- [NBER Working Paper 34025](https://www.nber.org/papers/w34025)
- [Machine-readable trend record](../../../records/comparative-nber-cookie-consent-choice-architecture-2025.json)

**Evidence status:** interface design changes observed consent behavior and a
model estimates repeated-decision costs; privacy, comprehension, welfare, and
exit remain open.
