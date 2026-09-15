# Treasury FIO × FEMA NRI hazard-context layer v1

The 2022 Treasury ZIP-code market rows were assigned to a FEMA National Risk
Index county baseline through the official Census ZCTA-to-county relationship.
The assignment uses the county containing the largest reported land-area part
of each ZCTA and retains the approximation rather than treating a ZCTA as a
county.

Of 25,593 Treasury 2022 rows, 25,330 received FEMA context: 99.0%. Among the
matched rows, unweighted mean premiums were approximately $1,565 in counties
rated Relatively Low for composite expected annual loss, $1,698 in Relatively
Moderate counties, and $2,449 in Relatively High counties. The Very High group
had a lower mean premium of $1,928 but the highest mean nonrenewal rate, 1.271%,
versus 0.959% in the Relatively Low group.

This is intentionally not described as a monotonic hazard dose-response. The
Very High result is a counterexample: nonrenewal and premium levels need not
move together across modeled-risk bins. Asset value, rebuilding cost, insurer
mix, policy composition, state regulation, and data coverage all remain live
alternative explanations.

The supported bridge is now:

```text
modeled county hazard context
  -> different observed premium/nonrenewal profiles
  -> household coverage and affordability pressure (cross-source, not identified here)
  -> repairs, lending, mobility, public action, and politics (open)
```

The FEMA baseline is not a same-year household or insurance observation, and
the Treasury market window ends in 2022. The next test is a later insurance
market release or state filing panel, then compatible claims, property,
mortgage, repair, and move/stay outcomes.
