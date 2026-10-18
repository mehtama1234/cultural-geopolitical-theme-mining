# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **127**
- Exact linked social items: **132**
- Record statuses: `{'augmented': 127, 'documented_access_gap': 498, 'queued': 1353}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 89 |
| `linkedin:documented_access_gap` | 536 |
| `linkedin:not_started` | 1,353 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 585 |
| `reddit:not_started` | 1,353 |
| `x:documented_access_gap` | 625 |
| `x:not_started` | 1,353 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 624 |
| `youtube:not_started` | 1,353 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
