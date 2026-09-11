"""Build the US reading atlas and matching Markdown from one connection record."""
import json
import re
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "manifests/us-theme-connections.json").read_text())
nodes = {n["id"]: n for n in data["nodes"]}
assert len(nodes) == len(data["nodes"])
themes = {t["id"]: t for t in data["themes"]}
for n in nodes.values():
    assert n["theme"] in themes
    assert (ROOT / n["source_record"]).is_file()
for link in data["edges"]:
    assert link["from"] in nodes and link["to"] in nodes
    assert link["type"] in ("open", "comparison")
    assert link["relation"] and link["limit"]

intro = "Eight short research passes, connected through everyday choices. These are early readings of the collected sources. The map helps us find related questions; it does not prove that one trend causes another."
big = "Across the packets, a recurring question is what disappears when a household keeps its spending under control: insurance cover, a medical visit, savings or free time. A second question is whether people can get help or leave when a service fails them. These are proposed themes. We have not established that they are worsening together, affect the same households, or explain political behavior."
md = ["# US life: the connections", "", intro, "", "## The bigger picture", "", big, ""]
parts = []
for theme in data["themes"]:
    md += ["## " + theme["title"], "", theme["meaning"], ""]
    cards = []
    for n in nodes.values():
        if n["theme"] != theme["id"]:
            continue
        text = (ROOT / n["source_record"]).read_text()
        sources = list(dict.fromkeys(re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", text)))
        related = [x for x in data["edges"] if n["id"] in (x["from"], x["to"])]
        md += ["### " + n["title"], "", n["summary"], "", "**Question:** " + n["question"], "", "**Subthemes:** " + "; ".join(n["subthemes"]), "", "**Limit:** " + n["limit"], "", "Sources collected in the opening pass; listing a source does not mean its full study has been reviewed.", ""]
        md += [f"- [{label}]({url})" for label, url in sources]
        md += ["", "Connections:", ""]
        links = []
        for x in related:
            other = nodes[x["to"] if x["from"] == n["id"] else x["from"]]
            label = "Comparison" if x["type"] == "comparison" else "Question to test"
            md += [f"- {label}: {x['relation']}. Related topic: {other['title']}. {x['limit']}"]
            links.append(f'<li><span class="tag">{label}</span><a href="#{other["id"]}">{e(x["relation"])}</a><p>{e(x["limit"])}</p></li>')
        md += [""]
        source_html = "".join(f'<li><a href="{e(url, quote=True)}">{e(label)}</a></li>' for label, url in sources)
        cards.append(f'''<article id="{n["id"]}" class="card" tabindex="-1" data-theme="{n["theme"]}">
<p class="eyebrow">{e(n["status"])}</p><h3>{e(n["title"])}</h3>
<p class="summary">{e(n["summary"])}</p><p><strong>{e(n["question"])}</strong></p>
<p class="sub">{e(" · ".join(n["subthemes"]))}</p><p class="limit"><strong>What remains uncertain:</strong> {e(n["limit"])}</p>
<details><summary>See the connections ({len(related)})</summary><ul class="connections">{"".join(links)}</ul></details>
<details><summary>Sources and research notes ({len(sources)})</summary><p>Collected in the opening pass. Full studies may still need review.</p><ul>{source_html}</ul><a href="../{n["source_record"]}">Open the source notes</a></details>
</article>''')
    parts.append(f'<section class="theme" id="theme-{theme["id"]}"><h2>{e(theme["title"])}</h2><p>{e(theme["meaning"])}</p><div class="grid">{"".join(cards)}</div></section>')
style = """
:root{--paper:#f5f3ed;--ink:#182c2a;--muted:#526560;--line:#cdd7cf;--accent:#155f51}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:24px}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.65 system-ui,sans-serif}
main{max-width:1180px;margin:auto;padding:36px 24px 80px}a{color:var(--accent);text-underline-offset:4px}
h1,h2,h3{font-family:Georgia,serif;line-height:1.15;font-weight:normal}h1{font-size:clamp(2.5rem,6vw,4.8rem);max-width:850px;margin:24px 0}
h2{font-size:2rem;margin:54px 0 12px}h3{font-size:1.7rem;margin:8px 0 20px}
header>p{max-width:760px}.eyebrow{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}
.big{background:#193f36;color:#f7f6ef;padding:28px;border-radius:12px;margin:32px 0}.big h2{margin:0 0 14px}.big p{max-width:900px}
.controls{padding:20px 0;border-bottom:1px solid var(--line);display:flex;gap:18px;flex-wrap:wrap}
label{display:flex;flex-direction:column;gap:6px;flex:1;min-width:220px;font-size:.9rem}
input,select{font:inherit;padding:13px;border:1px solid #78938a;border-radius:6px;background:white;color:var(--ink);width:100%}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}.card{background:#fffefa;border:1px solid var(--line);border-radius:10px;padding:28px;overflow-wrap:anywhere;scroll-margin-top:24px}
.summary{font-size:1.1rem}.sub{color:var(--accent);font-size:.88rem}.limit{color:var(--muted);font-size:.93rem}
details{border-top:1px solid var(--line);padding:15px 0}summary{cursor:pointer;font-weight:600;min-height:30px}
li{margin:12px 0}.connections{list-style:none;padding:0}.connections p{font-size:.9rem;color:var(--muted);margin:6px 0}
.tag{display:block;font-size:.73rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:5px}
:focus-visible{outline:3px solid #b96722;outline-offset:5px}.card:target{border:2px solid var(--accent)}
[hidden]{display:none!important}footer{margin-top:40px;color:var(--muted)}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:8px;background:white;padding:10px}
@media(max-width:720px){.grid{grid-template-columns:1fr}main{padding:24px 16px}.card{padding:22px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{.controls{display:none}.grid{display:block}.card{break-inside:avoid;margin-bottom:18px}body{background:white}}
"""
script = """
const search=document.querySelector('#search'), select=document.querySelector('#filter');
const cards=[...document.querySelectorAll('.card')], status=document.querySelector('#count');
function filter(){
 const words=search.value.toLowerCase().trim().split(/\\s+/).filter(Boolean);
 let count=0;
 cards.forEach(card=>{
  card.hidden=!(words.every(w=>card.textContent.toLowerCase().includes(w)) && (!select.value||card.dataset.theme===select.value));
  if(!card.hidden)count++;
 });
 document.querySelectorAll('.theme').forEach(section=>section.hidden=![...section.querySelectorAll('.card')].some(c=>!c.hidden));
 status.textContent=count+' of '+cards.length+' topics shown'+(count?'':'. Try fewer words or choose all themes.');
}
search.addEventListener('input',filter);select.addEventListener('change',filter);
function reveal(){
 const id=decodeURIComponent(location.hash.slice(1)), target=document.getElementById(id);
 if(target?.classList.contains('card')){
  search.value='';select.value='';filter();
  requestAnimationFrame(()=>{target.scrollIntoView();target.focus({preventScroll:true});});
 }
}
window.addEventListener('hashchange',reveal);reveal();
"""
options = "".join(f'<option value="{t["id"]}">{e(t["title"])}</option>' for t in data["themes"])
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>US life — the connections</title><style>{style}</style></head>
<body><a class="skip" href="#topics">Skip to topics</a><main>
<nav><a href="index.html">Research home</a> / US life</nav>
<header><p class="eyebrow">A connected reading guide · First pass</p><h1>What people pay.<br>What people give up.</h1><p>{e(intro)}</p></header>
<aside class="big"><h2>The bigger picture</h2><p>{e(big)}</p></aside>
<div class="controls"><label>Find a topic or connection<input id="search" type="search" placeholder="Try care, time, trust or insurance"></label>
<label>Read by theme<select id="filter"><option value="">All themes</option>{options}</select></label></div>
<p id="count" role="status" aria-live="polite">8 of 8 topics shown</p>
<noscript><p>All topics, connections and sources are readable below. Search requires JavaScript.</p></noscript>
<div id="topics">{"".join(parts)}</div>
<footer><p>Connections marked “Question to test” are unproven. Several topics share sources, so their agreement is not independent confirmation.</p><a href="../analysis/us-theme-atlas.md">Read the same notes in Markdown</a></footer>
</main><script>{script}</script></body></html>'''
md += ["## Reading rule", "", "Connections marked Question to test are unproven. Several topics share sources, so their agreement is not independent confirmation.", ""]
(ROOT / "analysis/us-theme-atlas.md").write_text("\n".join(md))
(ROOT / "site/us-theme-atlas.html").write_text(html)
print(f"Built {len(nodes)} topics, {len(themes)} themes, {len(data['edges'])} connections.")

