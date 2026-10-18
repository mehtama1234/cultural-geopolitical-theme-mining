# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **148**
- Exact linked social items: **153**
- Record statuses: `{'augmented': 148, 'documented_access_gap': 552, 'queued': 1278}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 110 |
| `linkedin:documented_access_gap` | 590 |
| `linkedin:not_started` | 1,278 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 660 |
| `reddit:not_started` | 1,278 |
| `x:documented_access_gap` | 700 |
| `x:not_started` | 1,278 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 699 |
| `youtube:not_started` | 1,278 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
