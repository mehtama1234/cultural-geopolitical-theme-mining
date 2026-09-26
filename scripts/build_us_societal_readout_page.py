"""Build the reader-facing HTML page for the current societal readout."""

from html import escape
from pathlib import Path
import re

import markdown

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "analysis/US-BROAD-CURRENT-SOCIETAL-CULTURAL-POLITICAL-READOUT_V1.md"
TARGET = ROOT / "site/US-BROAD-CURRENT-SOCIETAL-CULTURAL-POLITICAL-READOUT_V1.html"

STYLE = ":root{--paper:#f5f3ed;--ink:#18322d;--muted:#566a63;--line:#cbd8d0;--green:#174f43;--gold:#b86b2b;--blue:#e8eee9;--card:#fffefa}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.72 system-ui,sans-serif}main{max-width:960px;margin:auto;padding:24px 22px 84px}a{color:var(--green);text-underline-offset:4px}nav{font-size:.95rem}header{padding:34px 0 26px;border-bottom:1px solid var(--line)}h1,h2,h3{font-family:Georgia,serif;font-weight:normal;line-height:1.12}h1{font-size:clamp(2.7rem,7vw,5.5rem);margin:20px 0}h2{font-size:2.1rem;margin:58px 0 16px}h3{font-size:1.4rem}.eyebrow{color:var(--green);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}.lede{font-size:1.28rem;max-width:820px}.memo{padding-top:8px}.memo table{border-collapse:collapse;width:100%;background:var(--card);margin:22px 0;display:block;overflow-x:auto}.memo th,.memo td{border:1px solid var(--line);padding:13px;text-align:left;vertical-align:top;min-width:150px}.memo th{color:var(--muted);font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}.memo blockquote{border-left:4px solid var(--gold);margin:24px 0;padding-left:20px;font:1.3rem/1.5 Georgia,serif}.memo pre{background:var(--blue);padding:20px;border-radius:10px;overflow:auto;white-space:pre-wrap}.memo li{margin:9px 0}.note{border-left:4px solid var(--gold);padding-left:18px;color:var(--muted)}footer{border-top:1px solid var(--line);margin-top:60px;padding-top:22px}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:10px;background:white;padding:10px;z-index:2}:focus-visible{outline:3px solid var(--gold);outline-offset:4px}@media(max-width:700px){body{font-size:17px}main{padding:18px 16px 60px}.memo table{font-size:.92rem}}"

source = SOURCE.read_text(encoding="utf-8")
body = markdown.markdown(source, extensions=["tables", "fenced_code", "sane_lists"])

# The Markdown memo is authored relative to analysis/.  Published pages live
# under site/, so repository-local links need one explicit analysis/ hop.
body = re.sub(
    r'href="(?!https?://|#|\.\./)([^\"]+)"',
    lambda match: f'href="../analysis/{match.group(1)}"',
    body,
)

title = "What appears to be happening in American society"
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(title)}"><title>{escape(title)}</title><style>{STYLE}</style></head><body><a class="skip" href="#readout">Skip to readout</a><main><nav><a href="index.html">Research home</a> · <a href="reading-room.html">Reading room</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-theme-atlas.html">Connections</a></nav><header><p class="eyebrow">US societal, cultural, and political synthesis</p><p class="lede">A plain-language cross-source readout of what appears to be changing beneath visible events.</p></header><article id="readout" class="memo">{body}</article><footer><p><a href="../analysis/US-BROAD-CURRENT-SOCIETAL-CULTURAL-POLITICAL-READOUT_V1.md">Read the Markdown source</a> · <a href="US-BROAD-PLAIN-LANGUAGE-ATLAS-SUMMARY_V1.html">Plain-language atlas</a> · <a href="index.html">Research home</a></p><p class="note">This synthesis compares separate source families. It is not one sample, one causal model, or one household story.</p></footer></main></body></html>'''
TARGET.write_text(html, encoding="utf-8")
print(f"Built {TARGET.relative_to(ROOT)}")
