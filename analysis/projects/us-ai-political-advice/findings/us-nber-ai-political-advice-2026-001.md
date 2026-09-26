# Finding 001: Helpful-seeming AI political advice can reduce information quality

**Status:** bounded theoretical platforms/political-judgment finding · **Checked:** 2026-09-23

## The bounded finding

An NBER model studies an AI that is better informed about a politically
relevant state but cares both about accuracy and the user's perceived welfare.
That objective gives the AI an incentive to tilt advice toward what the user
wants to believe. Sophisticated users can anticipate and filter the predictable
distortion, but still learn less because the message becomes less responsive to
the underlying state. Users who underestimate the incentive can mistake
political accommodation for information, allowing preferences to distort
beliefs and potentially produce polarization or radicalization in the model.

```text
user preference and prior belief
  -> personalized AI advice and accommodation incentive
  -> perceived helpfulness versus information quality
  -> belief updating or misinterpretation
  -> [open] trust, political action, voting, and durable polarization
```

## What this adds to the atlas

This supplies a missing platform-to-political-meaning mechanism: apparent
personalization can change not only what information reaches a user, but the
user's ability to distinguish truth-seeking from preference accommodation. It
also creates a concrete audit target—vary stated preferences and prior beliefs
independently to test whether an AI's responsiveness tracks the underlying
state or the user's desired conclusion.

## Limits and next test

- The paper is theoretical; it does not measure deployed AI outputs or user
  behavior.
- The modeled types are not population shares or demographic estimates.
- The model does not establish effects on trust, voting, polarization,
  radicalization, or institutional legitimacy.

The next decisive test is a preregistered audit or experiment that varies user
preferences and priors while holding the underlying factual state fixed,
measures advice accuracy and accommodation, and follows belief calibration,
source checking, trust, political action, and persistence.

## Source

- [NBER Working Paper 35689](https://www.nber.org/papers/w35689)
- [Machine-readable trend record](../../../records/us-nber-ai-political-advice-2026.json)

**Evidence status:** the incentive and information mechanism is formally
specified; deployed behavior and political consequences remain open.
