# Claim-source reachability audit — 2026-10-30

## Scope

This audit checks the 40 URLs in
`CLAIM-SOURCE-REVIEW-2026-10-30.csv`. It tests HTTP reachability and final
redirect location only. It does not validate the source’s substantive claim,
method, date, population, authority or evidence quality.

## Results

- **29 endpoints returned HTTP 200** from the shell or retry pass, and **9 of
  the former 403 endpoints were retrievable through the browser path**.
- **0 endpoints remain unresolved after alternate-route review:** UNECE is
  represented by an accessible official summary and IPCC by the stable AR6
  Technical Summary PDF.
- **0 endpoints returned 404, 5xx or transport errors** in the final ledger.
- One DOE carbon-removal report URL returned 404 and was replaced by a stable
  official DOE program page. The claim was downgraded to partial support because
  the replacement page does not prove the report-level maturity statement.
- The NICE URL redirected from the PDF resource path to the guidance page; this
  is recorded as reachable, not as proof that the guidance closes long-term
  clinical value.

## Interpretation

The original restricted endpoints were access restrictions, not evidence that
the sources were dead or that the claims were true. Nine were resolved through
browser retrieval and two more through stable alternate official routes. The
UNECE row now uses an official summary rather than pretending the full report
was retrieved; the IPCC row uses the official Technical Summary PDF and keeps
the scenario-versus-project outcome boundary.

Reachability is therefore a separate status from substantive support:

```text
HTTP response -> retrievable endpoint -> document identity and method
  -> exact claim support -> named outcome and counterexample
```

The next pass should retrieve the 11 restricted sources through a permitted
browser or stable official PDF/download route, capture title, author, date,
population, method and relevant page/section, and then update the claim ledger
only if the source actually supports the stated stage.
