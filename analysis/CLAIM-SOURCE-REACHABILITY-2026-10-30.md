# Claim-source reachability audit — 2026-10-30

## Scope

This audit checks the 40 URLs in
`CLAIM-SOURCE-REVIEW-2026-10-30.csv`. It tests HTTP reachability and final
redirect location only. It does not validate the source’s substantive claim,
method, date, population, authority or evidence quality.

## Results

- **29 endpoints returned HTTP 200** after the retry pass.
- **11 endpoints remained HTTP 403** under both the default request and a
  browser-like request with standard HTML/PDF accept headers.
- **0 endpoints returned 404, 5xx or transport errors** in the final ledger.
- One DOE carbon-removal report URL returned 404 and was replaced by a stable
  official DOE program page. The claim was downgraded to partial support because
  the replacement page does not prove the report-level maturity statement.
- The NICE URL redirected from the PDF resource path to the guidance page; this
  is recorded as reachable, not as proof that the guidance closes long-term
  clinical value.

## Interpretation

The 11 remaining 403 responses are access restrictions, not evidence that the
sources are dead or that the claims are true. They require manual/browser or
alternate official-document review. The two UN endpoints that initially
returned 403 resolved under the retry request and are now marked reachable.

Reachability is therefore a separate status from substantive support:

```text
HTTP response -> retrievable endpoint -> document identity and method
  -> exact claim support -> named outcome and counterexample
```

The next pass should retrieve the 11 restricted sources through a permitted
browser or stable official PDF/download route, capture title, author, date,
population, method and relevant page/section, and then update the claim ledger
only if the source actually supports the stated stage.
