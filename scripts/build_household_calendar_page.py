"""Build the reader-facing household-calendar research brief."""

from html import escape
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "analysis/US-HOUSEHOLD-CALENDAR-INTEGRATION_V1.md"
TARGET = ROOT / "site/us-household-calendar-integration.html"
STYLE = ":root{--paper:#f5f3ed;--ink:#18322d;--muted:#566a63;--line:#cbd8d0;--green:#174f43;--gold:#b86b2b;--blue:#e8eee9;--card:#fffefa}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.72 system-ui,sans-serif}main{max-width:960px;margin:auto;padding:24px 22px 84px}a{color:var(--green);text-underline-offset:4px}nav{font-size:.95rem}header{padding:34px 0 26px;border-bottom:1px solid var(--line)}h1,h2,h3{font-family:Georgia,serif;font-weight:normal;line-height:1.12}h1{font-size:clamp(2.7rem,7vw,5.5rem);margin:20px 0}h2{font-size:2.1rem;margin:58px 0 16px}.eyebrow{color:var(--green);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}.lede{font-size:1.28rem;max-width:820px}.memo{padding-top:8px}.memo table{border-collapse:collapse;width:100%;background:var(--card);margin:22px 0;display:block;overflow-x:auto}.memo th,.memo td{border:1px solid var(--line);padding:13px;text-align:left;vertical-align:top;min-width:150px}.memo th{color:var(--muted);font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}.memo blockquote{border-left:4px solid var(--gold);margin:24px 0;padding-left:20px;font:1.3rem/1.5 Georgia,serif}.memo pre{background:var(--blue);padding:20px;border-radius:10px;overflow:auto;white-space:pre-wrap}.memo li{margin:9px 0}.note{border-left:4px solid var(--gold);padding-left:18px;color:var(--muted)}footer{border-top:1px solid var(--line);margin-top:60px;padding-top:22px}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:10px;background:white;padding:10px;z-index:2}:focus-visible{outline:3px solid var(--gold);outline-offset:4px}@media(max-width:700px){body{font-size:17px}main{padding:18px 16px 60px}.memo table{font-size:.92rem}}"

source = SOURCE.read_text()
body = markdown.markdown(source, extensions=["tables", "fenced_code", "sane_lists"])
title = "The household calendar: a twelve-month test of connected pressure"
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(title)}"><title>{escape(title)}</title><style>{STYLE}</style></head><body><a class="skip" href="#brief">Skip to brief</a><main><nav><a href="index.html">Research home</a> · <a href="us-theme-atlas.html">Connections</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-matched-evidence.html">Matched evidence</a></nav><header><p class="eyebrow">US research design · connected household pressure</p><p class="lede">A bounded next study for testing when money, time, access, and control change together.</p></header><article id="brief" class="memo">{body}</article><footer><p><a href="../analysis/US-HOUSEHOLD-CALENDAR-INTEGRATION_V1.md">Read the Markdown brief</a> · <a href="us-big-picture-synthesis.html">Return to the big picture</a></p><p class="note">This is a research design, not evidence that every household follows every chain.</p></footer></main></body></html>'''
TARGET.write_text(html)
print(f"Built {TARGET.relative_to(ROOT)}")
