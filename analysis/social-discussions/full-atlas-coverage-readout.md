# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **14**
- Exact linked social items: **17**
- Record statuses: `{'in_review': 20, 'augmented': 5, 'queued': 1953}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 2 |
| `linkedin:documented_access_gap` | 3 |
| `linkedin:not_started` | 1,973 |
| `reddit:augmented` | 13 |
| `reddit:documented_access_gap` | 1 |
| `reddit:not_started` | 1,964 |
| `x:documented_access_gap` | 5 |
| `x:not_started` | 1,973 |
| `youtube:documented_access_gap` | 5 |
| `youtube:not_started` | 1,973 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
