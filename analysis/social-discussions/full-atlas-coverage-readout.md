# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **5**
- Exact linked social items: **7**
- Record statuses: `{'in_review': 25, 'queued': 1953}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:not_started` | 1,978 |
| `reddit:augmented` | 5 |
| `reddit:not_started` | 1,973 |
| `x:not_started` | 1,978 |
| `youtube:not_started` | 1,978 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
