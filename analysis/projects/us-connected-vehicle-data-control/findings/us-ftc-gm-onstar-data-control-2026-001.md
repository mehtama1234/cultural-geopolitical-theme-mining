# Finding 001: A connected-vehicle privacy control can carry a service trade-off

**Status:** bounded platform-control and consumer-choice finding · **Checked:** 2026-09-22

## The finding in plain language

The FTC's 2026 order concerning GM and OnStar requires formal routes for U.S. consumers to request copies or deletion of connected-vehicle data, opt out of certain collection, and—where the vehicle technology permits—disable precise geolocation collection. GM's privacy statement also describes request channels, a possible 45-day processing window, and in-vehicle privacy settings for some model-year 2019-and-later vehicles.

But the control is not absolute. GM says some data may still be collected after unenrollment to restore connectivity or address high-voltage-battery overheating. The availability of controls also depends on vehicle model, technology, service enrollment, state, and safety or emergency exceptions.

```text
connected vehicle collects data
  -> consumer requests access, deletion, opt-out, or disablement
  -> verification and technology/legal conditions
  -> privacy control or residual collection
  -> [open] service loss, safety trade-off, trust, switching, or mobility effect
```

## What this adds to the broader atlas

This is a sharper version of the practical-control problem. A right can exist and a firm can publish a route while the consumer still has to choose between privacy and services they value—or may not know what remains collected after unenrollment.

The unresolved issue is not simply whether a privacy policy exists. It is whether people can understand the boundary, use the control, preserve necessary safety and mobility functions, and verify what happened afterward.

The safety exceptions should not automatically be read as wrongdoing. They may protect occupants or vehicle systems. The open question is whether those exceptions are visible, understandable, and contestable to the person making the choice.

## What the source does not show

- The order and privacy statement do not report request volume, completion, deletion verification, or residual exposure.
- Control availability varies by vehicle model/year, technology, enrollment, state, and exception.
- A formal route does not prove that a consumer can use it without losing valued services.
- The evidence does not measure trust, switching, mobility, safety, or political response.
- It does not show whether data is re-collected or shared after a control is used.

## Next decisive test

Obtain a named implementation record that follows one consumer request through verification, outcome, residual collection, service effect, appeal, and later provider or vehicle choice.

## Sources

- [FTC final GM/OnStar order announcement](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers)
- [GM U.S. privacy statement](https://www.gm.com/privacy-statement)
- [Machine-readable source record](../../../records/us-ftc-gm-onstar-data-control-order-2026.json)

**Evidence status:** the FTC order and GM statement establish formal controls, channels, conditions, and exceptions; actual consumer use, deletion, residual exposure, and service trade-offs remain open.
