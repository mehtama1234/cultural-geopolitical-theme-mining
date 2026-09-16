# JASSM/LRASM subaward control surface audit v1

**Status:** supplier-visibility audit; no production, delivery, or leverage estimate  
**Checked:** 2026-09-16  
**Parent award:** `FA868224CB001`  
**Source:** local USAspending rich subaward artifact, retrieved 2026-09-14  
**Machine-readable audit:** [subaward control-surface audit](data/jassm-subaward-control-surface-audit-v1.json)

## Result

The rich local artifact contains recipient names, subaward descriptions, UEIs,
and performance locations for returned rows. This strengthens the observable
supplier/control layer between a prime award and a potential production
network. It still does not establish that any particular subaward produced a
missile, that output was delivered or accepted, or that a supplier could be
replaced at acceptable cost.

| Surface | What the local artifact can show | What it cannot show alone |
|---|---|---|
| Prime award | Parent award `FA868224CB001` and Lockheed Martin prime context | Delivered capability or customer readiness |
| Recipient network | Named subordinate recipients and their reported subaward amounts | Complete tier map or supplier market share |
| Entity identity | UEIs on returned rows; selected legal-name/CAGE reconciliation elsewhere | Ownership/control rights for every row or effective production control |
| Place | Sub-recipient performance locations, including state/city fields | Which plant performed the work or local employment/incidence |
| Component description | Text descriptions for returned subawards | Quantity produced, quality, delivery, acceptance, inventory, or operational use |

## Quantitative checkpoint

The audit reports the exact row count, unique recipient-name count, returned
amount, UEI/location coverage, state distribution, and top-five share in the
machine-readable output. Those are properties of this returned extract. The
retrieval is not a complete procurement census and the concentration share is
not a defense-industrial market-share estimate.

The correct interpretation is a control-surface lead:

```text
prime award
  -> reported subordinate recipient and UEI
  -> reported performance place and component description
  -> [open] facility output, workforce, inputs, delivery, acceptance
  -> [open] maintenance, replacement, partner options, and external response
```

The recipient and place layers must not be collapsed. One legal name can map to
multiple facilities, and a performance location does not prove that the
reported item was manufactured there.

## Broader-program implication

This is the industrial and geopolitical analogue of the practical-exit
boundary developed elsewhere in the atlas: visible institutional transactions
can be detailed while the consequential actor-level outcome remains hidden.
The procurement system exposes who was paid and where a record points before
it exposes whether a partner received usable capability, whether the system is
replaceable, or whether another state changed behavior.

## Reproduction and storage boundary

```text
python3 scripts/audit_jassm_subaward_control_surface.py
```

The script reads the existing local JSON response, downloads no data, and does
not perform new entity linkage.
