#!/usr/bin/env python3
"""Build a reader-facing, searchable view of the durable source registry."""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "manifests/source-registry.json").read_text(encoding="utf-8"))
sources = registry["sources"]

def host(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")

corpus = []
for dirpath, dirnames, filenames in os.walk(ROOT / "analysis"):
    dirnames[:] = [name for name in dirnames if name != "data"]
    for filename in filenames:
        path = Path(dirpath) / filename
        if path.suffix.lower() not in {".md", ".json", ".txt"}:
            continue
        try:
            corpus.append(path.read_text(encoding="utf-8", errors="ignore").lower())
        except OSError:
            continue

usage: dict[str, tuple[int, int]] = {}
for source in sources:
    domain = host(source["url"])
    counts = [text.count(domain) for text in corpus]
    usage[source["id"]] = (sum(counts), sum(1 for count in counts if count))

def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

cards = []
for source in sources:
    types = ", ".join(source.get("source_types", []))
    references, artifacts = usage[source["id"]]
    search = " ".join([
        source.get("name", ""), source.get("role", ""), types,
        source.get("access_notes", ""),
    ]).lower()
    cards.append(f'''<article class="card" data-search="{esc(search)}">
<p class="eyebrow">{esc(source["id"])}</p>
<h2><a href="{esc(source["url"])}">{esc(source["name"])}</a></h2>
<p class="role">{esc(source.get("role", ""))}</p>
<p class="usage"><strong>{references}</strong> domain references across <strong>{artifacts}</strong> analysis artifacts</p>
<p class="types"><strong>Evidence types:</strong> {esc(types)}</p>
<details><summary>Use and limits</summary><p>{esc(source.get("access_notes", ""))}</p><p class="small">{esc(source.get("license_note", ""))}</p></details>
</article>''')

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Searchable source-family map for the Cultural, Social, and Geopolitical Theme Mining program.">
<title>Source family map · Cultural, Social, and Geopolitical Theme Mining</title>
<style>
:root{{--paper:#f5f3ed;--ink:#18322d;--muted:#566a63;--line:#cbd8d0;--green:#174f43;--gold:#b86b2b;--card:#fffefa;--blue:#e8eee9}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 system-ui,sans-serif}}
main{{max-width:1160px;margin:auto;padding:24px 22px 84px}}a{{color:var(--green);text-underline-offset:4px}}
nav{{color:var(--muted);white-space:nowrap;overflow-x:auto;padding-bottom:3px}}header{{padding:44px 0 30px;border-bottom:1px solid var(--line)}}
h1,h2{{font-family:Georgia,serif;font-weight:normal;line-height:1.12}}h1{{font-size:clamp(2.7rem,7vw,5.5rem);max-width:900px;margin:16px 0}}h2{{font-size:1.55rem;margin:8px 0 12px}}
.lede{{font-size:1.22rem;max-width:850px}}.note{{border-left:4px solid var(--gold);padding-left:18px;color:var(--muted);max-width:850px}}
.controls{{position:sticky;top:0;z-index:3;background:rgba(245,243,237,.97);padding:16px 0;border-bottom:1px solid var(--line);margin-top:24px}}
label{{display:block;color:var(--muted);font-size:.9rem}}input{{display:block;width:100%;margin-top:6px;padding:13px 14px;border:1px solid #78938a;border-radius:7px;background:var(--card);font:inherit;color:var(--ink)}}
#count{{color:var(--green);font-weight:600;margin:10px 0 0}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:26px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:22px}}.eyebrow,.types{{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--green)}}
.role{{font-size:1.05rem}}.usage{{color:var(--green);font-size:.92rem}}.types{{letter-spacing:.02em;text-transform:none;color:var(--muted)}}details{{border-top:1px solid var(--line);padding-top:11px;margin-top:16px}}summary{{cursor:pointer;font-weight:600}}.small{{font-size:.9rem;color:var(--muted)}}[hidden]{{display:none!important}}
:focus-visible{{outline:3px solid var(--gold);outline-offset:4px}}@media(max-width:720px){{main{{padding:18px 16px 60px}}.grid{{grid-template-columns:1fr}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style></head><body><main>
<nav><a href="index.html">Research home</a> · <a href="reading-room.html">Guided route</a> · <a href="us-source-coverage.html">Project coverage</a> · source family map</nav>
<header><p class="eyebrow">Evidence architecture</p><h1>The source family map</h1>
<p class="lede">The recurring institutions, surveys, research programs, public records, firms, and technical sources that feed the living trend atlas.</p>
<p class="note">This is a source universe, not a claim that every source is used equally or that sources measure the same thing. The usage line counts domain mentions in the analysis corpus; it is an audit signal, not a quality score or proof that every cited item was read in full. Each card keeps the source’s role and interpretation boundary visible. Findings must still preserve unit, date, geography, denominator, method, uncertainty, subgroup differences, and counterexamples.</p></header>
<section class="controls"><label for="search">Find a source family by institution, topic, or evidence type<input id="search" type="search" placeholder="Try IMF, household survey, regulation, energy, work, or consumer"></label><p id="count" role="status" aria-live="polite">{len(sources)} source families shown</p></section>
<section class="grid">{"".join(cards)}</section>
<footer><p><a href="reading-room.html">Return to the reading room</a> · <a href="theme-trends.html">Read theme trends</a> · <a href="US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.html">Open the coverage audit</a></p></footer>
<script>const input=document.querySelector('#search'),cards=[...document.querySelectorAll('.card')],count=document.querySelector('#count');function filter(){{const q=input.value.toLowerCase().trim();let n=0;cards.forEach(card=>{{card.hidden=Boolean(q&&!card.dataset.search.includes(q));if(!card.hidden)n++}});count.textContent=n+' of '+cards.length+' source families shown'}}input.addEventListener('input',filter);</script>
</main></body></html>'''

(ROOT / "site/source-registry.html").write_text(page, encoding="utf-8")
print(f"Built source family map for {len(sources)} sources.")
