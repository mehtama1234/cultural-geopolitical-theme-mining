# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **36**
- Exact linked social items: **39**
- Record statuses: `{'augmented': 36, 'documented_access_gap': 16, 'in_review': 23, 'queued': 1903}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 3 |
| `linkedin:documented_access_gap` | 49 |
| `linkedin:not_started` | 1,926 |
| `reddit:augmented` | 34 |
| `reddit:documented_access_gap` | 18 |
| `reddit:not_started` | 1,926 |
| `x:documented_access_gap` | 52 |
| `x:not_started` | 1,926 |
| `youtube:documented_access_gap` | 52 |
| `youtube:not_started` | 1,926 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
