# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **47**
- Exact linked social items: **52**
- Record statuses: `{'augmented': 45, 'documented_access_gap': 55, 'in_review': 25, 'queued': 1853}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 12 |
| `linkedin:documented_access_gap` | 90 |
| `linkedin:not_started` | 1,876 |
| `reddit:augmented` | 37 |
| `reddit:documented_access_gap` | 63 |
| `reddit:not_started` | 1,878 |
| `x:documented_access_gap` | 100 |
| `x:not_started` | 1,878 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 99 |
| `youtube:not_started` | 1,878 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
