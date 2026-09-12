"""Check the minimum parity contract between a finding memo and its HTML page.

The HTML pages may have a different layout, but they must retain the finding's
title, source links, and the reader-facing sections that keep claims bounded.
This is a publishing check, not a claim that two formats have identical prose.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def clean(value: str) -> str:
    return " ".join(value.lower().split())


def sources(markdown: str) -> list[str]:
    return [url for url in re.findall(r"https?://[^)\s]+", markdown) if "github.com" not in url]


def main() -> int:
    failures = []
    checked = 0
    for memo in sorted((ROOT / "analysis/findings").glob("*-matched-evidence-001.md")):
        page = ROOT / "site" / f"{memo.stem}.html"
        checked += 1
        if not page.exists():
            failures.append((memo.name, "missing HTML page"))
            continue
        md = memo.read_text()
        parser = Text()
        parser.feed(page.read_text())
        html = clean(" ".join(parser.parts))
        title_match = re.search(r"^# (.+)$", md, re.M)
        if not title_match or clean(title_match.group(1)) not in html:
            failures.append((memo.name, "title is not present in HTML"))
            continue
        missing_urls = [url for url in sources(md) if url.lower() not in page.read_text().lower()]
        if missing_urls:
            failures.append((memo.name, f"{len(missing_urls)} source URL(s) missing"))
            continue
        required = {
            "deeper finding": "the deeper finding",
            "next test": "next test",
            "reading rule": "reading rule",
        }
        absent = [label for label, needle in required.items() if needle not in html]
        if absent:
            failures.append((memo.name, "missing section(s): " + ", ".join(absent)))
            continue
        print(f"MATCHED {memo.name}")
    print(f"Checked {checked} finding pages")
    for name, reason in failures:
        print(f"STALE {name}: {reason}")
    if failures:
        print(f"Parity failures: {len(failures)}")
        return 1
    print("Parity passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
