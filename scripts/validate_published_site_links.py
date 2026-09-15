"""Validate relative links in the generated static site."""

import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ATTR_RE = re.compile(r"(?:href|src)=[\"']([^\"'#]+)")
EXTERNAL_SCHEMES = {"http", "https", "mailto", "javascript", "data"}


def main() -> None:
    failures = []
    pages = sorted(SITE.glob("*.html"))
    for page in pages:
        for raw in ATTR_RE.findall(page.read_text(encoding="utf-8")):
            parsed = urlsplit(raw)
            if parsed.scheme in EXTERNAL_SCHEMES or parsed.netloc or parsed.path.startswith("/"):
                continue
            target = (page.parent / parsed.path).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                failures.append((page, raw, "outside repository"))
                continue
            if not target.exists():
                failures.append((page, raw, "missing target"))

    if failures:
        for page, raw, reason in failures:
            print(f"BROKEN {page.relative_to(ROOT)} -> {raw} ({reason})")
        raise SystemExit(f"INVALID published site links: {len(failures)} broken links")
    print(f"VALID published site links: {len(pages)} HTML pages checked")


if __name__ == "__main__":
    main()
