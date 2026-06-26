from src.triage import classify_report


def test_crash_routes_to_parser_owner():
    result = classify_report("Crash on import", "Traceback points at parseReport")

    assert result.label == "bug"
    assert result.owner == "@maintainers/parser"
    assert result.needs_repro is False


def test_missing_steps_requests_repro():
    result = classify_report("It does not work", "No other details yet")

    assert result.label == "needs-repro"
    assert result.needs_repro is True
