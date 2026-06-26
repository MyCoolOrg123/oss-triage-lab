from dataclasses import dataclass


@dataclass(frozen=True)
class TriageResult:
    label: str
    owner: str
    needs_repro: bool


def classify_report(title: str, body: str) -> TriageResult:
    text = f"{title} {body}".lower()

    if "duplicate" in text or "same as" in text:
        return TriageResult("duplicate", "@maintainers/community", False)

    if "traceback" in text or "crash" in text:
        return TriageResult("bug", "@maintainers/parser", False)

    if "label" in text or "route" in text:
        return TriageResult("routing", "@maintainers/community", False)

    return TriageResult("needs-repro", "@maintainers/qa", True)
