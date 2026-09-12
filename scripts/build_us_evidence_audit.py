"""Build an audit of topic evidence and semantic-map coverage."""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "manifests/us-theme-connections.json").read_text())
themes = {x["id"]: x for x in manifest["themes"]}
edges = manifest["edges"]
paths = manifest["reading_paths"]
records = []
for node in manifest["nodes"]:
    source = ROOT / node["source_record"]
    text = source.read_text()
    records.append({
        "id": node["id"], "title": node["title"], "theme": node["theme"],
        "theme_title": themes[node["theme"]]["title"],
        "sources": len(re.findall(r"\[[^\]]+\]\(https?://[^)\s]+\)", text)),
        "links": sum(node["id"] in (e["from"], e["to"]) for e in edges),
        "paths": sum(node["id"] in p["topics"] for p in paths),
        "checked": bool(node.get("evidence_check")),
        "source_record": node["source_record"],
    })
records.sort(key=lambda x: (x["theme_title"], x["title"]))
checked = sum(x["checked"] for x in records)

md = ["# US evidence and map audit", "", f"This audit covers {len(records)} topic records, {len(edges)} semantic links, and {len(paths)} reading paths.", "It shows coverage, not proof that every source or connection has been fully reviewed.", "", f"**Evidence checks recorded:** {checked}/{len(records)}", "", "## How to read this", "", "A source packet is the opening search record. An evidence check is a later, specific check recorded in the topic card. A semantic link is a declared comparison or question to test. A reading path joins topics for investigation; it is not a proven cause-and-effect chain.", "", "## Topic audit", "", "| Topic | Theme | Sources | Links | Paths | Evidence check | Source notes |", "|---|---|---:|---:|---:|---|---|"]
for x in records:
    md.append(f"| [{x['title']}](../site/us-theme-atlas.html#{x['id']}) | {x['theme_title']} | {x['sources']} | {x['links']} | {x['paths']} | {'yes' if x['checked'] else 'opening only'} | [open]({x['source_record']}) |")
md += ["", "## What this audit cannot prove", "", "- A source count does not measure source quality or full-study review.", "- An evidence check does not join every household, firm, policy, and later outcome.", "- A semantic link does not prove that two topics affect the same people.", "- A completed memo explains a question; it does not close the open gaps.", "", "## Next use", "", "Sort by the fewest sources, links, or paths. Choose one bridge, find matched records over time, and keep the counterexample and missing step visible."]
(ROOT / "analysis/us-evidence-audit.md").write_text("\n".join(md) + "\n")

cards = []
for x in records:
    state = "checked" if x["checked"] else "opening only"
    css = "good" if x["checked"] else "open"
    cards.append(f'<article class="card" data-search="{escape((x["title"]+" "+x["theme_title"]+" "+x["id"]).lower(), quote=True)}" data-theme="{escape(x["theme"], quote=True)}" data-state="{state}"><p class="eyebrow">{escape(x["theme_title"])}</p><h2><a href="us-theme-atlas.html#{escape(x["id"], quote=True)}">{escape(x["title"])}</a></h2><div class="metrics"><span><b>{x["sources"]}</b> sources</span><span><b>{x["links"]}</b> links</span><span><b>{x["paths"]}</b> paths</span></div><p class="state {css}">{state}</p><p><a href="../{escape(x["source_record"], quote=True)}">Open source notes</a></p></article>')
options = "".join(f'<option value="{escape(x["id"], quote=True)}">{escape(x["title"])}</option>' for x in manifest["themes"])
style = ":root{--paper:#f5f3ed;--ink:#182c2a;--muted:#526560;--line:#cdd7cf;--accent:#155f51;--gold:#b96722}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:30px 24px 80px}a{color:var(--accent);text-underline-offset:4px}h1,h2{font-family:Georgia,serif;font-weight:normal;line-height:1.15}h1{font-size:clamp(2.6rem,6vw,4.8rem);max-width:850px;margin:38px 0 18px}h2{font-size:1.35rem;margin:8px 0 14px}.lede{font-size:1.2rem;max-width:820px}.summary{background:var(--accent);color:#f8f6ef;padding:26px;border-radius:12px;margin:30px 0;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.summary b{display:block;font:2.1rem Georgia,serif}.controls{position:sticky;top:0;z-index:2;background:var(--paper);padding:15px 0;border-bottom:1px solid var(--line);display:flex;gap:14px;flex-wrap:wrap}label{display:flex;flex-direction:column;gap:5px;flex:1;min-width:220px}input,select{font:inherit;padding:12px;border:1px solid #78938a;border-radius:6px;background:white;color:var(--ink)}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin-top:25px}.card{background:#fffefa;border:1px solid var(--line);border-radius:10px;padding:20px;min-width:0}.eyebrow{color:var(--accent);font-size:.72rem;letter-spacing:.08em;text-transform:uppercase}.metrics{display:flex;gap:14px;flex-wrap:wrap;color:var(--muted);font-size:.9rem}.metrics b{color:var(--ink);font-size:1.2rem}.state{display:inline-block;border-radius:999px;padding:3px 10px;font-size:.8rem}.good{background:#dceee2;color:#175c40}.open{background:#f5e3c8;color:#884313}[hidden]{display:none!important}:focus-visible{outline:3px solid var(--gold);outline-offset:4px}.skip{position:absolute;left:-9999px}.skip:focus{left:15px;top:10px;background:#fff;padding:10px}@media(max-width:800px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}.summary{grid-template-columns:1fr 1fr}}@media(max-width:560px){main{padding:22px 16px}.grid{grid-template-columns:1fr}.summary{grid-template-columns:1fr}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}"
script = "const q=document.querySelector('#search'),t=document.querySelector('#theme'),s=document.querySelector('#state'),cards=[...document.querySelectorAll('.card')],count=document.querySelector('#count');function filter(){const word=q.value.toLowerCase().trim(),theme=t.value,state=s.value;let n=0;cards.forEach(c=>{c.hidden=(word&&!c.dataset.search.includes(word))||(theme&&c.dataset.theme!==theme)||(state&&c.dataset.state!==state);if(!c.hidden)n++});count.textContent=n+' of '+cards.length+' topics shown'+(n?'':'. Try a different search or filter.')}q.addEventListener('input',filter);t.addEventListener('change',filter);s.addEventListener('change',filter);"
html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>US evidence and map audit</title><style>'+style+'</style></head><body><a class="skip" href="#topics">Skip to audit</a><main><nav><a href="index.html">Research home</a> / <a href="us-theme-atlas.html">US connections</a> / Evidence audit</nav><header><p class="eyebrow">Research coverage, not a confidence score</p><h1>What is connected, and how well is it checked?</h1><p class="lede">A practical audit of the current US research map. It shows where we have an evidence check and where a topic still rests on its opening search record.</p></header><section class="summary" aria-label="Audit totals"><div><b>'+str(len(records))+'</b>topics</div><div><b>'+str(len(edges))+'</b>semantic links</div><div><b>'+str(len(paths))+'</b>reading paths</div><div><b>'+str(checked)+'/'+str(len(records))+'</b>evidence checks</div></section><p class="note">A source packet is an opening search record. A link is a comparison or question to test. A reading path is a route through related topics. None of these alone proves a full causal chain.</p><div class="controls"><label>Find a topic<input id="search" type="search" placeholder="Try housing, care, credit or work"></label><label>Theme<select id="theme"><option value="">All themes</option>'+options+'</select></label><label>Evidence state<select id="state"><option value="">All states</option><option value="checked">Evidence check recorded</option><option value="opening only">Opening record only</option></select></label></div><p id="count" role="status" aria-live="polite">'+str(len(records))+' of '+str(len(records))+' topics shown</p><div id="topics" class="grid">'+"".join(cards)+'</div><footer><p><a href="us-theme-atlas.html">Return to connected atlas</a> · <a href="../analysis/us-evidence-audit.md">Read Markdown edition</a> · <a href="us-big-picture-synthesis.html">Read big-picture synthesis</a></p></footer><script>'+script+'</script></main></body></html>'
html = html.replace('<nav><a href="index.html">Research home</a> / <a href="us-theme-atlas.html">US connections</a> / Evidence audit</nav>', '<nav><a href="index.html">Research home</a> · <a href="us-theme-atlas.html">Connections</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-source-coverage.html">Source coverage</a> / Evidence audit</nav>')
(ROOT / "site/us-evidence-audit.html").write_text(html)
print(f"Built evidence audit for {len(records)} topics, {len(edges)} links, {len(paths)} paths.")
