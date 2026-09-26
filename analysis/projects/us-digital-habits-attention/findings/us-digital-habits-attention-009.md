# Finding 305: A vehicle-data privacy order can create formal control without proving usable privacy

**Status:** bounded platform/data-governance implementation finding · **Checked:** 2026-09-20

## The bounded finding

The FTC's finalized January 2026 order concerning GM and OnStar requires
consumer-control routes for connected-vehicle data. The order describes a way
for U.S. consumers to request a copy of their data, seek deletion, disable
precise geolocation collection where the vehicle supports it, and opt out of
geolocation and driving-behavior data collection subject to stated exceptions.

This is a distinct platform/data stage because it turns privacy from a general
principle into formal control surfaces attached to a real product relationship.
It still does not show that customers found the controls, used them, obtained
complete deletion, avoided downstream use, or changed vehicles or trust.

GM's current U.S. privacy statement makes the implementation layer more
concrete. It directs consumers to a verifiable request form or phone route,
does not accept privacy requests by email, says some requests may take up to
45 days, and makes location disabling dependent on vehicle technology and model
year. It also says that unenrollment can leave limited safety or emergency
collection in place. These are observable route constraints—not evidence that
any consumer completed a request or obtained verified deletion.

```text
connected-vehicle data collection and sharing
  -> FTC order creates access, deletion, disable, and opt-out routes
  -> form/phone/vehicle-setting route with verification, timing, and eligibility constraints
  -> customer request and firm response [unobserved]
  -> verified deletion or reduced exposure [unobserved]
  -> continued use, switching, trust, or mobility consequence [unobserved]
```

## Why it matters for the larger atlas

The digital lane has often had to stop at platform reach, concern, or a legal
right to challenge. This case adds a more concrete remedy design: the user can
be treated as having a control claim over a data stream that is tied to a
physical service and potentially sensitive movements. That connects:

- platforms, data, and attention;
- consumer power and recourse;
- trust, identity, and meaning;
- unequal exposure and status; and
- firm and public-system power.

It also exposes a recurring conversion problem. “A route exists” is not the
same as “the user can reach it,” “the firm completes it,” or “the data is gone.”
Disabling collection may itself have service, safety, convenience, or vehicle-
function trade-offs. The durable consumer outcome is therefore not encoded in
the order.

## Evidence boundary

- This is one named enforcement order, not a prevalence estimate for vehicle
  tracking or a representative customer study.
- The order records formal obligations, not request volume, response time,
  completion, deletion verification, or residual data.
- GM's published implementation route adds a stated up-to-45-day processing
  window, no-email restriction, model-dependent location control, and safety or
  emergency exceptions; it still does not report actual request completion or
  verified deletion.
- A legal opt-out or deletion route does not prove that a customer knows about
  it, can use it, or can do so without losing a valued service.
- The FTC allegations and order do not establish the experience of every GM or
  OnStar customer, nor do they measure later trust, switching, or mobility.

## Next test

Obtain an authorized, de-identified implementation ledger with vehicle/account
eligibility, request type, submission channel, acknowledgment, firm decision,
completion date, deletion or disable verification, exception reason, service
effect, repeat contact, continued use, switching, and trust or complaint
follow-up. Keep formal availability, attempted use, completed control, and
verified outcome as separate stages.

## Sources

- [FTC final order and press release](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers)
- [FTC GM/OnStar case record](https://www.ftc.gov/legal-library/browse/cases-proceedings/2323091-general-motors-llc-onstar-llc)
- [GM U.S. Consumer Privacy Statement](https://www.gm.com/privacy-statement)
- [Machine-readable trend record](../../../records/us-ftc-gm-onstar-data-control-order-2026.json)

**Evidence status:** reported firm-level enforcement remedy design. Actual
consumer use, data deletion, reduced exposure, service trade-off, trust,
switching, and practical exit remain open.
