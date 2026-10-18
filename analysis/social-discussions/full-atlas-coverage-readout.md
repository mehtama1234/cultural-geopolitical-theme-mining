# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **266**
- Exact linked social items: **271**
- Record statuses: `{'augmented': 266, 'documented_access_gap': 1234, 'queued': 478}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 228 |
| `linkedin:documented_access_gap` | 1,272 |
| `linkedin:not_started` | 478 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,460 |
| `reddit:not_started` | 478 |
| `x:documented_access_gap` | 1,500 |
| `x:not_started` | 478 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,499 |
| `youtube:not_started` | 478 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
