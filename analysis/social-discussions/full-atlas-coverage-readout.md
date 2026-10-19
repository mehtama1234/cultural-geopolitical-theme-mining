# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **2,014**
- Atlas records with at least one exact linked social item: **340**
- Exact linked social items: **348**
- Record statuses: `{'augmented': 336, 'documented_access_gap': 1667, 'queued': 11}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 302 |
| `linkedin:documented_access_gap` | 1,703 |
| `linkedin:not_started` | 9 |
| `reddit:augmented` | 41 |
| `reddit:documented_access_gap` | 1,962 |
| `reddit:not_started` | 11 |
| `x:documented_access_gap` | 2,003 |
| `x:not_started` | 11 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 2,002 |
| `youtube:not_started` | 11 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
