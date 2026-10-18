# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **302**
- Exact linked social items: **307**
- Record statuses: `{'augmented': 302, 'documented_access_gap': 1548, 'queued': 128}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 264 |
| `linkedin:documented_access_gap` | 1,586 |
| `linkedin:not_started` | 128 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,810 |
| `reddit:not_started` | 128 |
| `x:documented_access_gap` | 1,850 |
| `x:not_started` | 128 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,849 |
| `youtube:not_started` | 128 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
