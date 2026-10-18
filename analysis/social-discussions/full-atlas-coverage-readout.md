# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **237**
- Exact linked social items: **242**
- Record statuses: `{'augmented': 237, 'documented_access_gap': 963, 'queued': 778}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 199 |
| `linkedin:documented_access_gap` | 1,001 |
| `linkedin:not_started` | 778 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,160 |
| `reddit:not_started` | 778 |
| `x:documented_access_gap` | 1,200 |
| `x:not_started` | 778 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,199 |
| `youtube:not_started` | 778 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
