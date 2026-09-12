"""Build readable finding pages from the Markdown source of truth.

This deliberately uses the Markdown memo as the content source. The page
layout is shared, so a deeper memo cannot silently leave an older HTML summary
behind.
"""

import re
from html import escape
from html.parser import HTMLParser
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]

STYLE = """:root{--paper:#f5f3ed;--ink:#18322d;--muted:#566a63;--line:#cbd8d0;--green:#174f43;--gold:#b86b2b;--blue:#e8eee9;--card:#fffefa}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.72 system-ui,sans-serif}main{max-width:960px;margin:auto;padding:24px 22px 84px}a{color:var(--green);text-underline-offset:4px}nav{font-size:.95rem}header{padding:34px 0 26px;border-bottom:1px solid var(--line)}h1,h2,h3{font-family:Georgia,serif;font-weight:normal;line-height:1.12}h1{font-size:clamp(2.7rem,7vw,5.5rem);margin:20px 0}h2{font-size:2.1rem;margin:58px 0 16px}h3{font-size:1.4rem}.eyebrow{color:var(--green);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}.lede{font-size:1.28rem;max-width:820px}.memo{padding-top:8px}.memo table{border-collapse:collapse;width:100%;background:var(--card);margin:22px 0;display:block;overflow-x:auto}.memo th,.memo td{border:1px solid var(--line);padding:13px;text-align:left;vertical-align:top;min-width:150px}.memo th{color:var(--muted);font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}.memo blockquote{border-left:4px solid var(--gold);margin:24px 0;padding-left:20px;font:1.3rem/1.5 Georgia,serif}.memo pre{background:var(--blue);padding:20px;border-radius:10px;overflow:auto;white-space:pre-wrap}.memo code{background:var(--blue);padding:2px 5px;border-radius:4px}.memo hr{border:0;border-top:1px solid var(--line);margin:38px 0}.memo img{max-width:100%}.note{border-left:4px solid var(--gold);padding-left:18px;color:var(--muted)}footer{border-top:1px solid var(--line);margin-top:60px;padding-top:22px}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:10px;background:white;padding:10px;z-index:2}:focus-visible{outline:3px solid var(--gold);outline-offset:4px}@media(max-width:700px){body{font-size:17px}main{padding:18px 16px 60px}.memo table{font-size:.92rem}}
"""


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def clean(value: str) -> str:
    return " ".join(value.lower().split())


def should_rebuild(memo: Path, page: Path) -> bool:
    if not page.exists():
        return True
    source = memo.read_text()
    current = page.read_text()
    parsed = Text()
    parsed.feed(current)
    visible = clean(" ".join(parsed.parts))
    title = re.search(r"^# (.+)$", source, re.M)
    if not title or clean(title.group(1)) not in visible:
        return True
    urls = re.findall(r"https?://[^)\s]+", source)
    if any(url.lower() not in current.lower() for url in urls):
        return True
    return (
        not any(needle in visible for needle in ("the deeper finding", "the argument has limits", "what this changes", "the connection", "the useful surprise", "the control problem", "the important split"))
        or not any(needle in visible for needle in ("next test", "the next test is", "what would change the finding"))
        or "reading rule" not in visible
    )


def render(memo: Path) -> str:
    source = memo.read_text()
    title_match = re.search(r"^# (.+)$", source, re.M)
    title = title_match.group(1) if title_match else memo.stem
    body = markdown.markdown(source, extensions=["tables", "fenced_code", "sane_lists"])
    md_link = f"../analysis/{memo.relative_to(ROOT / 'analysis')}"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(title)}"><title>{escape(title)}</title><style>{STYLE}</style></head><body><a class="skip" href="#finding">Skip to finding</a><main><nav><a href="index.html">Research home</a> · <a href="us-theme-atlas.html">Connections</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-matched-evidence.html">Matched evidence</a></nav><header><p class="eyebrow">Connected US finding · source-traceable memo</p><div class="lede">Full current Markdown record, presented in a responsive reading layout.</div></header><article id="finding" class="memo">{body}</article><footer><p><a href="{escape(md_link, quote=True)}">Read the Markdown record</a> · <a href="us-evidence-audit.html">Open the evidence audit</a></p><p class="note">Claims, limits, and open questions are kept together. A connection is not proof of cause.</p></footer></main></body></html>'''


def main():
    rebuilt = 0
    checked = 0
    for memo in sorted((ROOT / "analysis/findings").glob("*-matched-evidence-001.md")):
        page = ROOT / "site" / f"{memo.stem}.html"
        checked += 1
        if should_rebuild(memo, page):
            page.write_text(render(memo))
            rebuilt += 1
            print(f"BUILT {page.relative_to(ROOT)}")
    print(f"Checked {checked} finding pages; rebuilt {rebuilt}.")


if __name__ == "__main__":
    main()
