# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **176**
- Exact linked social items: **181**
- Record statuses: `{'augmented': 176, 'documented_access_gap': 674, 'queued': 1128}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 138 |
| `linkedin:documented_access_gap` | 712 |
| `linkedin:not_started` | 1,128 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 810 |
| `reddit:not_started` | 1,128 |
| `x:documented_access_gap` | 850 |
| `x:not_started` | 1,128 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 849 |
| `youtube:not_started` | 1,128 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
