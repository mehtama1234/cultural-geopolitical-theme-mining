# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **140**
- Exact linked social items: **145**
- Record statuses: `{'augmented': 140, 'documented_access_gap': 535, 'queued': 1303}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 102 |
| `linkedin:documented_access_gap` | 573 |
| `linkedin:not_started` | 1,303 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 635 |
| `reddit:not_started` | 1,303 |
| `x:documented_access_gap` | 675 |
| `x:not_started` | 1,303 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 674 |
| `youtube:not_started` | 1,303 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
