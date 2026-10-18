# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **106**
- Exact linked social items: **111**
- Record statuses: `{'augmented': 106, 'documented_access_gap': 394, 'queued': 1478}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 68 |
| `linkedin:documented_access_gap` | 432 |
| `linkedin:not_started` | 1,478 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 460 |
| `reddit:not_started` | 1,478 |
| `x:documented_access_gap` | 500 |
| `x:not_started` | 1,478 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 499 |
| `youtube:not_started` | 1,478 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
