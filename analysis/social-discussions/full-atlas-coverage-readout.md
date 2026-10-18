# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **29**
- Exact linked social items: **32**
- Record statuses: `{'augmented': 29, 'documented_access_gap': 6, 'in_review': 15, 'queued': 1928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 3 |
| `linkedin:documented_access_gap` | 32 |
| `linkedin:not_started` | 1,943 |
| `reddit:augmented` | 27 |
| `reddit:documented_access_gap` | 8 |
| `reddit:not_started` | 1,943 |
| `x:documented_access_gap` | 35 |
| `x:not_started` | 1,943 |
| `youtube:documented_access_gap` | 35 |
| `youtube:not_started` | 1,943 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
