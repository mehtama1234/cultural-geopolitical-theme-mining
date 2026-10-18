# Full-atlas social coverage readout

This is a live control readout, not a completion claim.

- Atlas records: **1,978**
- Atlas records with at least one exact linked social item: **310**
- Exact linked social items: **315**
- Record statuses: `{'augmented': 310, 'documented_access_gap': 1615, 'queued': 53}`

## Platform attempt states

| Platform/status | Rows |
|---|---:|
| `linkedin:augmented` | 272 |
| `linkedin:documented_access_gap` | 1,653 |
| `linkedin:not_started` | 53 |
| `reddit:augmented` | 40 |
| `reddit:documented_access_gap` | 1,885 |
| `reddit:not_started` | 53 |
| `x:documented_access_gap` | 1,925 |
| `x:not_started` | 53 |
| `youtube:augmented` | 1 |
| `youtube:documented_access_gap` | 1,924 |
| `youtube:not_started` | 53 |

The queue is not complete until every row reaches a terminal state:
`augmented`, `documented_access_gap`, or `not_socially_applicable`.
