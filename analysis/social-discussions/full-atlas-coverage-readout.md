# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **279**
- Exact linked social items: **284**
- Record statuses: `{'augmented': 279, 'documented_access_gap': 1396, 'queued': 303}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 241 |
| `linkedin:documented_access_gap` | 1,434 |
| `linkedin:not_started` | 303 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,635 |
| `reddit:not_started` | 303 |
| `x:documented_access_gap` | 1,675 |
| `x:not_started` | 303 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,674 |
| `youtube:not_started` | 303 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
