# OSS Triage Lab

A public repository with intentionally small code and high-signal bug reports. Use
it to test Discord flows that reproduce, label, deduplicate, and route issues before
a maintainer opens the thread.

## Bot scenarios to try

- Convert Discord bug reports into GitHub issues with labels and reproduction steps.
- Ask whether a new report duplicates an existing issue.
- Ask the bot to identify the owner from `docs/triage-playbook.md`.
- Ask for a minimal repro command using the files in `tests/fixtures/`.
