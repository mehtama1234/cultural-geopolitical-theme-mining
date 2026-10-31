# Claim-source reachability audit — 2026-10-30

## Scope

This audit checks the 40 URLs in
`CLAIM-SOURCE-REVIEW-2026-10-30.csv`. It tests HTTP reachability and final
redirect location only. It does not validate the source’s substantive claim,
method, date, population, authority or evidence quality.

## Results

- **29 endpoints returned HTTP 200** from the shell or retry pass, and **9 of
  the former 403 endpoints were retrievable through the browser path**.
- **2 endpoints remain unresolved:** UNECE and IPCC returned HTTP 403 through
  both the shell and browser retrieval paths.
- **0 endpoints returned 404, 5xx or transport errors** in the final ledger.
- One DOE carbon-removal report URL returned 404 and was replaced by a stable
  official DOE program page. The claim was downgraded to partial support because
  the replacement page does not prove the report-level maturity statement.
- The NICE URL redirected from the PDF resource path to the guidance page; this
  is recorded as reachable, not as proof that the guidance closes long-term
  clinical value.

## Interpretation

The 2 remaining 403 responses are access restrictions, not evidence that the
sources are dead or that the claims are true. Nine former 403 responses were
resolved through browser retrieval and are marked `browser_retrievable`; the
UN endpoints were among them. The UNECE and IPCC sources still require a
permitted browser, alternate official PDF or document mirror.

Reachability is therefore a separate status from substantive support:

```text
HTTP response -> retrievable endpoint -> document identity and method
  -> exact claim support -> named outcome and counterexample
```

The next pass should retrieve the 11 restricted sources through a permitted
browser or stable official PDF/download route, capture title, author, date,
population, method and relevant page/section, and then update the claim ledger
only if the source actually supports the stated stage.
