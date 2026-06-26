# Triage Playbook

## Labels

- `bug`: confirmed behavior regression or runtime failure.
- `needs-repro`: missing steps or fixture.
- `duplicate`: already tracked by another issue.
- `routing`: label or owner assignment problem.
- `good first issue`: small, well-scoped fix with a clear test.

## Routing

| Area | Owner | Signal |
| --- | --- | --- |
| Parser | `@maintainers/parser` | Stack traces mentioning `parseReport`. |
| Labels | `@maintainers/community` | Missing or conflicting labels. |
| Fixtures | `@maintainers/qa` | Broken repro files or flaky tests. |

## Repro command

```bash
python -m pytest tests/test_triage.py -q
```
