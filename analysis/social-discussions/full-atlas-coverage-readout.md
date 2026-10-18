# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **259**
- Exact linked social items: **264**
- Record statuses: `{'augmented': 259, 'documented_access_gap': 1166, 'queued': 553}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 221 |
| `linkedin:documented_access_gap` | 1,204 |
| `linkedin:not_started` | 553 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,385 |
| `reddit:not_started` | 553 |
| `x:documented_access_gap` | 1,425 |
| `x:not_started` | 553 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,424 |
| `youtube:not_started` | 553 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
