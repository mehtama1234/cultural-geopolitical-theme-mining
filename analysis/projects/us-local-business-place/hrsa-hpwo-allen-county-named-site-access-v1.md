# HPWO Allen County named-site access checkpoint v1

**Checked:** 2026-09-20  
**Purpose:** test whether a primary-care shortage/designation record can be followed from an organization to a named service site and then toward usable care.

## What is observed

HRSA's primary-care HPSA file identifies **Health Partners of Western Ohio** in Allen County, Ohio as a designated Federally Qualified Health Center. The row names organization ID `0516380` and the organization address at 329 N West St, Lima.

The companion HRSA service-site file lists **North Lima Community Health Center**, 2001 N Cole St, Lima, under the same organization ID. The site is listed as active, permanent, and open 72 hours per week. Its schedule and operating calendar fields are unknown.

This is a stronger bridge than a county shortage label alone:

```text
designated HPSA
  -> named organization
  -> shared organization identifier
  -> named active service site
  -> listed weekly hours
```

It is still an administrative and nominal operating bridge, not a person-level care episode.

The [official North Lima patient-facing page](https://hpwohio.org/location/north-lima-community-health-center)
confirms the address, lists a site phone number, and names medical, oral-health,
behavioral-health, pharmacy, social-services, and substance-use services. It
displays several overlapping hour lines, including Monday-Friday 8 a.m.-8 p.m.,
Tuesday-Friday 8 a.m.-5:30 p.m., and Monday-Saturday 8 a.m.-8 p.m. Because the
page does not clearly label which service each line describes, it confirms a
public route but does not establish one unambiguous medical appointment
schedule.

The [HPWO contact page](https://hpwohio.org/contact-us) says its general email
form does not schedule appointments and directs patients to call their Health
Partners location or use the patient portal. The HRSA site file lists
`419-516-0327`, while the current North Lima page lists `419-549-5982`; the
public records do not explain the discrepancy. Thus the public route reaches a
phone/portal handoff, but not a verified appointment slot or wait time.

The linked [patient portal](https://www.myhealthrecord.com/Portal/SSO) is
login-gated. Its public surface exposes sign-in and account-recovery fields,
not appointment slots, wait times, or new-patient availability. The portal's
existence is therefore observed, but public booking visibility is not.

## What the organization says about the route

Health Partners' official medical page says:

- it is accepting new adult and pediatric patients and asks people to call for a first appointment;
- every location has a limited number of same-day appointments;
- it accepts Medicare, Medicaid, Medicaid managed care, and most commercial insurance;
- it will not turn someone away for inability to pay and offers payment plans and a sliding-fee scale.

Source: [Health Partners medical service page](https://hpwohio.org/service/medical).

Those statements are useful patient-facing route evidence, but they are stated at the organization level. They do not prove that North Lima has an open slot on a particular day, that a particular person's insurance is accepted, what the wait is, whether transportation or paperwork blocks use, or whether care was completed.

The same medical page adds a sharper substitution boundary: every location is
reported to have a limited number of same-day appointments, but Health Partners
also says it does not fill in for another community provider when that provider
is unavailable. Thus “same-day availability” is a limited organization policy,
not proof of an open North Lima slot or a general fallback for a patient who
cannot reach their regular clinician.

The provider's current [cost-of-care page](https://hpwohio.org/cost-of-care)
adds a more concrete affordability route. For uninsured patients, it lists
medical estimates of $5-$25 when a discount applies and $95-$350 without the
discount. Eligibility is based on family size and pre-tax income; keeping the
discount for more than 30 days requires an application and proof such as
paystubs, tax returns, benefit letters, or a benefits printout. These are
published estimates and eligibility rules, not a patient-specific bill or proof
that the discount was successfully obtained. The route therefore converts
price relief into an application-and-documentation burden before it becomes a
realized payment outcome.

## End-to-end status

| Stage | Status | Boundary |
|---|---|---|
| Shortage/designation | Observed | HRSA HPSA row |
| Organization identity | Observed | Shared BHCMIS organization ID |
| Named site | Observed | Active North Lima service-site row |
| Nominal operating capacity | Observed | 72 listed hours/week; permanent site |
| Site-facing contact and service route | Observed | Official site page lists phone and services |
| Site-facing hours clarity | Open | Multiple overlapping hour lines are displayed |
| Appointment-request route | Open | General email does not schedule; call or portal is required |
| Site-phone consistency | Open | HRSA and current HPWO page list different numbers |
| Portal exists | Observed | HPWO links to a patient portal |
| Public portal booking visibility | Open | Login-gated; no slots or wait times visible |
| New-patient route | Reported | HPWO organization-level statement |
| Affordability/insurance route | Reported | HPWO organization-level statement |
| Discount/payment implementation | Reported | Published $5-$25 discounted medical estimate, higher non-discount estimate, income/family-size screen, and proof-of-income requirement after 30 days |
| Same-day/fallback route | Open | Limited same-day appointments are reported organization-wide, but no site-specific slot is shown and the organization disclaims filling in for another provider |
| Site-specific appointment | Open | No slot, wait, or acceptance record |
| Completed care | Open | No person-level use record |
| Adequacy and recovery | Open | No health, time, money, continuity, or household result |

## Why this matters to the atlas

This case sharpens the program's central conversion test. A shortage designation can coexist with an active provider, listed hours, and a public route for new patients. The remaining gap is exactly where nominal capacity becomes lived access: appointment availability, insurance/payment handling for a person, travel and waiting burden, completed care, continuity, and later health or household recovery.

The record therefore advances the care-access arrow without promoting “active site” or “72 hours” into “usable care.”

Machine-readable record: [named-site access data](data/hrsa-hpwo-allen-county-named-site-access-2026-09-19.json).
