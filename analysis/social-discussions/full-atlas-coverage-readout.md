# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **38**
- Exact linked social items: **41**
- Record statuses: `{'augmented': 38, 'documented_access_gap': 16, 'in_review': 21, 'queued': 1903}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 3 |
| `linkedin:documented_access_gap` | 51 |
| `linkedin:not_started` | 1,924 |
| `reddit:augmented` | 36 |
| `reddit:documented_access_gap` | 18 |
| `reddit:not_started` | 1,924 |
| `x:documented_access_gap` | 54 |
| `x:not_started` | 1,924 |
| `youtube:documented_access_gap` | 54 |
| `youtube:not_started` | 1,924 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
