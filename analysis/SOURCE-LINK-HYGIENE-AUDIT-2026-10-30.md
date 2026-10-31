# Source-link hygiene audit — 2026-10-30

**Scope:** 327 `ROTATION-*.md` packets under `analysis/`.
**Purpose:** distinguish structural source-link coverage from source validity,
quality and substantive evidence closure.

## Snapshot

| Check | Result | Meaning |
|---|---:|---|
| Rotation Markdown packets scanned | 327 | Current packet population only; synthesis and audit files excluded. |
| HTTP/HTTPS URL occurrences | 2,489 | Literal links found in packet text. |
| Unique URL values | 2,273 | Repeated official sources are common across related packets. |
| URL values repeated at least twice | 188 | Duplication is not itself an error; it can show shared evidence or source concentration. |
| Packets with no literal URL | 1 | Priority provenance-repair queue. |
| Packets without a literal `## Sources` heading | 90 | A heading is a discoverability check, not proof that sources are absent. |

## Priority provenance-repair queue

These packets contain no literal HTTP/HTTPS URL and should be repaired or
explicitly marked as synthesis-only before being used as fresh evidence:

- `ROTATION-FX-ACCESS-TO-JUSTICE-LEGAL-AID-PEOPLE-CENTRED-2026-10-29.md`

## Interpretation and limits

This audit checks only literal URL presence and simple duplication. It does
not test HTTP reachability, publication date, source authority, quoted-claim
accuracy, paywalls, redirects, link rot, whether the URL supports the exact
claim, or whether the packet preserves a counterexample. A packet with many
URLs can still have weak evidence, and a packet with no URLs may be an early
concept note rather than a research claim.

The next repair pass should add source provenance to the 1 zero-URL packet,
add a consistent `## Sources` heading where sources are present but hard to
discover, and then run a reachability and claim-to-source review in batches.
Do not silently invent citations or treat this structural audit as substantive
validation.

## Re-run contract

Scan only `analysis/ROTATION-*.md`; count URLs matching `https?://[^)\\s>]+`,
count unique values and repeated values, identify files without a `## Sources`
or `## Sources and` heading, and list files with zero URLs. Record the date and
scope whenever the snapshot changes.
