"""Validate the household-calendar design bundle as one publishable unit."""

import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    files = {
        "brief": ROOT / "analysis/US-HOUSEHOLD-CALENDAR-INTEGRATION_V1.md",
        "questionnaire": ROOT / "analysis/templates/US-HOUSEHOLD-CALENDAR-QUESTIONNAIRE_V1.md",
        "ledger": ROOT / "analysis/templates/US-HOUSEHOLD-CALENDAR-EVENT-LEDGER_V1.md",
        "claims": ROOT / "analysis/projects/us-household-calendar-integration/claims-ledger-v1.md",
        "schema": ROOT / "manifests/us-household-calendar-schema-v1.json",
        "fixture": ROOT / "analysis/samples/US-HOUSEHOLD-CALENDAR-SIMULATED_V1.json",
        "html": ROOT / "site/us-household-calendar-integration.html",
    }
    missing = [name for name, path in files.items() if not path.exists()]
    if missing:
        raise ValueError("missing bundle files: " + ", ".join(missing))
    schema = json.loads(files["schema"].read_text())
    fixture = json.loads(files["fixture"].read_text())
    if schema.get("format") != "us-household-calendar-schema-v1":
        raise ValueError("wrong schema format")
    if fixture.get("evidence_class") != "simulated_test_data":
        raise ValueError("fixture is not marked simulated")
    brief = files["brief"].read_text()
    for required in ("Bounded question", "The event ledger", "Five linked tests", "Privacy and data rules", "What would change the working picture"):
        if required not in brief:
            raise ValueError(f"brief is missing: {required}")
    questionnaire = files["questionnaire"].read_text()
    for required in ("Baseline", "Monthly money and time", "Event questions", "Optional public-judgment module"):
        if required not in questionnaire:
            raise ValueError(f"questionnaire is missing: {required}")
    claims = files["claims"].read_text()
    if claims.count("| HC-") < 8:
        raise ValueError("claims ledger has fewer than eight claims")
    parser = HTMLParser()
    parser.feed(files["html"].read_text())
    html = files["html"].read_text()
    if "household calendar" not in html.lower() or "simulated" not in html.lower():
        raise ValueError("HTML does not expose the brief and simulation warning")
    print("VALID household-calendar bundle: brief, questionnaire, ledger, claims, schema, fixture, HTML")
    return 0


if __name__ == "__main__":
    sys.exit(main())
