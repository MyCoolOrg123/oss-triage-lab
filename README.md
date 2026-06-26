# OSS Triage Lab

OSS Triage Lab standardizes how maintainers classify reports from community
channels before they become engineering work.

## What lives here

- `docs/triage-playbook.md` defines labels, owners, and reproduction rules.
- `src/triage.py` contains the current report classifier.
- `tests/fixtures/` stores small reports used to reproduce common cases.
- `tests/test_triage.py` covers the expected routing behavior.

## Maintainer workflow

1. Confirm whether a report is reproducible or already tracked.
2. Assign one primary label and one owning group.
3. Add a fixture when a report cannot be evaluated from the original message.
