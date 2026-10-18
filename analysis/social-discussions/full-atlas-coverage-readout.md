# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **31**
- Exact linked social items: **34**
- Record statuses: `{'augmented': 31, 'documented_access_gap': 6, 'in_review': 13, 'queued': 1928}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 3 |
| `linkedin:documented_access_gap` | 34 |
| `linkedin:not_started` | 1,941 |
| `reddit:augmented` | 29 |
| `reddit:documented_access_gap` | 8 |
| `reddit:not_started` | 1,941 |
| `x:documented_access_gap` | 37 |
| `x:not_started` | 1,941 |
| `youtube:documented_access_gap` | 37 |
| `youtube:not_started` | 1,941 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
