"""Build a plain-language source coverage index for the US project packets."""
import re
from urllib.parse import urlparse
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
records = []
for path in sorted((ROOT / "analysis/projects").glob("*/source-search-*.md")):
    text = path.read_text()
    heading = re.search(r"^# Source search: (.+)$", text, re.M)
    question = re.search(r"^## Working question\n\n(.+)$", text, re.M)
    status = re.search(r"^\*\*Status:\*\* (.+)$", text, re.M)
    sources = []
    for row in text.splitlines():
        if not row.startswith("|") or row.startswith("|---") or row.startswith("| ID"):
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        links = re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", row)
        if len(cells) >= 2 and links:
            sources.append({"label": links[0][0], "url": links[0][1], "what": cells[2] if len(cells) > 2 else ""})
    gaps = []
    match = re.search(r"## (?:Main gaps|Known gaps)\n\n(.*?)(?=\n## |\Z)", text, re.S)
    if match:
        gaps = [re.sub(r"^[-*]\s+", "", line).strip() for line in match.group(1).splitlines() if line.strip().startswith(("-", "*"))]
    records.append({
        "project": path.parent.name,
        "title": heading.group(1) if heading else path.parent.name,
        "question": question.group(1) if question else "",
        "status": status.group(1) if status else "",
        "sources": sources,
        "gaps": gaps,
        "path": str(path.relative_to(ROOT)),
    })
def family(url):
    host = urlparse(url).netloc.lower()
    if "nber.org" in host:
        return "NBER"
    if "hbs.edu" in host or "library.hbs.edu" in host:
        return "HBS"
    named = {
        "federalreserve.gov": "Federal Reserve",
        "bls.gov": "BLS",
        "census.gov": "Census",
        "cms.gov": "CMS",
        "consumerfinance.gov": "CFPB",
        "ftc.gov": "FTC",
        "hhs.gov": "HHS",
        "sba.gov": "SBA",
        "bea.gov": "BEA",
        "treasury.gov": "Treasury",
        "imf.org": "IMF",
        "bis.org": "BIS",
        "iea.org": "IEA",
        "financialresearch.gov": "OFR",
        "worldbank.org": "World Bank",
        "pewresearch.org": "Pew Research",
    }
    for domain, name in named.items():
        if host == domain or host.endswith("." + domain):
            return name
    if host.endswith(".gov") or ".gov/" in url:
        return "Other government"
    if "uchicago.edu" in host or "academic.oup.com" in host:
        return "Academic publisher"
    return "Other"

families = {}
for record in records:
    record["families"] = sorted({family(source["url"]) for source in record["sources"]})
    for source in record["sources"]:
        label = family(source["url"])
        families[label] = families.get(label, 0) + 1
assert records

md = ["# US source coverage", "", f"{len(records)} project packets are recorded below. This is a coverage index, not a claim that the source universe is complete.", ""]
md += ["**Source families recorded:** " + "; ".join(f"{name}: {count}" for name, count in sorted(families.items())), ""]
for record in records:
    md += [f"## {record['title']}", "", f"**Project:** `{record['project']}`", "", f"**Status:** {record['status']}", "", f"**Question:** {record['question']}", "", f"**Sources recorded:** {len(record['sources'])}", ""]
    md += [f"- [{s['label']}]({s['url']})" for s in record["sources"]]
    if record["gaps"]:
        md += ["", "**Open gaps:**"] + [f"- {gap}" for gap in record["gaps"]]
    md += ["", f"[Open the source-search record]({record['path']})", ""]
(ROOT / "analysis/us-source-coverage.md").write_text("\n".join(md))

cards = []
for record in records:
    source_list = "".join(f'<li><a href="{escape(s["url"], quote=True)}">{escape(s["label"])}</a></li>' for s in record["sources"])
    gaps = "".join(f"<li>{escape(gap)}</li>" for gap in record["gaps"])
    cards.append(f'''<article class="card" data-search="{escape((record["title"]+" "+record["project"]+" "+record["question"]).lower(), quote=True)}" data-families="{escape(" ".join(record["families"]), quote=True)}">
<p class="eyebrow">{escape(record["status"])}</p><h2>{escape(record["title"])}</h2><p>{escape(record["question"])}</p>
<p class="count">{len(record["sources"])} sources recorded</p><details><summary>Sources</summary><ul>{source_list}</ul></details>
{f'<details><summary>Open gaps ({len(record["gaps"])})</summary><ul>{gaps}</ul></details>' if record["gaps"] else ''}
<p><a href="../{escape(record["path"], quote=True)}">Open source notes</a></p></article>''')
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>US source coverage</title>
<style>:root{{--paper:#f5f3ed;--ink:#182c2a;--muted:#526560;--line:#cdd7cf;--accent:#155f51}}*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 system-ui,sans-serif}}main{{max-width:1080px;margin:auto;padding:34px 24px 80px}}a{{color:var(--accent)}}h1,h2{{font-family:Georgia,serif;font-weight:normal;line-height:1.15}}h1{{font-size:clamp(2.6rem,6vw,4.5rem);max-width:800px;margin:42px 0 20px}}h2{{font-size:1.45rem;margin:8px 0 14px}}.lede{{font-size:1.2rem;max-width:760px}}.controls{{position:sticky;top:0;background:var(--paper);padding:16px 0;border-bottom:1px solid var(--line);z-index:2}}input{{font:inherit;padding:12px;width:100%;border:1px solid #78938a;border-radius:6px}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:25px}}.card{{background:#fffefa;border:1px solid var(--line);border-radius:10px;padding:24px}}.eyebrow{{font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}}.count{{color:var(--accent);font-weight:600}}details{{border-top:1px solid var(--line);padding:12px 0}}summary{{cursor:pointer;font-weight:600}}li{{margin:7px 0}}[hidden]{{display:none!important}}:focus-visible{{outline:3px solid #b96722;outline-offset:4px}}@media(max-width:720px){{main{{padding:24px 16px}}.grid{{grid-template-columns:1fr}}}}</style></head><body><main>
<nav><a href="index.html">Research home</a> / source coverage</nav><h1>US source coverage</h1><p class="lede">{len(records)} project packets are recorded below. This is a coverage index, not a claim that the source universe is complete.</p><p class="families">{" · ".join(f"{name}: {count}" for name, count in sorted(families.items()))}</p>
<div class="controls"><label>Find a project or question<input id="search" type="search" placeholder="Try housing, care, AI or political trust"></label><label>Filter by source family<select id="family"><option value="">All source families</option>{''.join(f'<option value="{escape(name, quote=True)}">{escape(name)}</option>' for name in sorted(families))}</select></label><p id="count" role="status" aria-live="polite">{len(records)} of {len(records)} projects shown</p></div><div class="grid">{"".join(cards)}</div>
<script>const input=document.querySelector('#search'),family=document.querySelector('#family'),cards=[...document.querySelectorAll('.card')],count=document.querySelector('#count');function filter(){{const q=input.value.toLowerCase().trim(),f=family.value;let n=0;cards.forEach(c=>{{c.hidden=(q&&!c.dataset.search.includes(q))||(f&&!c.dataset.families.split(' ').includes(f));if(!c.hidden)n++}});count.textContent=n+' of '+cards.length+' projects shown'+(n?'':'. Try fewer words or choose all source families.')}}input.addEventListener('input',filter);family.addEventListener('change',filter);</script></main></body></html>'''
(ROOT / "site/us-source-coverage.html").write_text(html)
print(f"Built source coverage for {len(records)} projects.")
