"""Build the index of completed matched-evidence passes."""
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
items = []
routes = {
    "us-payment-fee-matched-evidence-001": ("Cost", "payment fees → price → household money", "same-household net cost"),
    "us-customer-automation-matched-evidence-001": ("Voice", "automation → service → remedy", "human authority to change the answer"),
    "us-home-insurance-matched-evidence-001": ("Energy / housing", "risk → insurance → ability to stay", "move, default, or loss of coverage"),
    "us-cash-policy-matched-evidence-001": ("Voice / cost", "cash benefit → household room → economic mood", "trust, turnout, and voting"),
    "us-credit-record-matched-evidence-001": ("Cost / voice", "payment trouble → credit record → housing access", "same-household housing result"),
    "us-health-insurance-job-lock-matched-evidence-001": ("Work / cost", "health coverage → job choice → household security", "the full value of the job tradeoff"),
    "us-income-volatility-matched-evidence-001": ("Work / cost", "unstable pay → cash buffer → spending room", "the same worker's later household choices"),
    "us-local-prices-matched-evidence-001": ("Cost / place", "place → local prices → real buying power", "the same household's move and well-being result"),
}
for path in sorted((ROOT / "analysis/findings").glob("*-matched-evidence-001.md")):
    text = path.read_text()
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    short = re.search(r"## Short answer\n\n(.+?)(?=\n\n## )", text, re.S).group(1).replace("\n", " ")
    key = path.stem
    theme, route, open_question = routes.get(key, ("US map", "connected evidence", "next test"))
    items.append({"key": key, "title": title, "short": short, "theme": theme, "route": route, "open": open_question, "html": f"{key}.html", "md": str(path.relative_to(ROOT))})
assert items

md = ["# US matched-evidence passes", "", "These are the deeper checks completed after the opening source packets. Each one joins several records, names the connection, and keeps the missing step visible.", "", "## Reading order", ""]
for i, x in enumerate(items, 1):
    md += [f"### {i}. {x['title']}", "", f"**Theme:** {x['theme']}", f"**Route:** {x['route']}", f"**Still open:** {x['open']}", "", x["short"], "", f"[Read the HTML page](../site/{x['html']}) · [Read the Markdown memo]({x['md']})", ""]
(ROOT / "analysis/us-matched-evidence-index.md").write_text("\n".join(md))

cards = "".join(f'<article class="card"><p class="eyebrow">{escape(x["theme"])}</p><h2>{escape(x["title"])}</h2><p class="route">{escape(x["route"])}</p><p>{escape(x["short"])}</p><p class="open"><strong>Still open:</strong> {escape(x["open"])}</p><p><a href="{escape(x["html"], quote=True)}">Read the HTML page</a> · <a href="../{escape(x["md"], quote=True)}">Markdown memo</a></p></article>' for x in items)
html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>US matched-evidence passes</title><style>:root{{--paper:#f5f3ed;--ink:#18322d;--muted:#566a63;--line:#cbd8d0;--green:#174f43;--gold:#b86b2b;--card:#fffefa}}*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:18px/1.7 system-ui,sans-serif}}main{{max-width:1080px;margin:auto;padding:28px 22px 80px}}a{{color:var(--green);text-underline-offset:4px}}h1,h2{{font-family:Georgia,serif;font-weight:normal;line-height:1.12}}h1{{font-size:clamp(2.7rem,7vw,5.3rem);max-width:850px;margin:38px 0 20px}}h2{{font-size:1.45rem;margin:8px 0 14px}}.eyebrow{{color:var(--green);font-size:.78rem;letter-spacing:.1em;text-transform:uppercase}}.lead{{font-size:1.3rem;max-width:820px}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:30px}}.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:24px}}.route{{color:var(--green);font-weight:600}}.open{{border-left:4px solid var(--gold);padding-left:16px;color:var(--muted)}}.skip{{position:absolute;left:-9999px}}.skip:focus{{left:15px;top:10px;background:white;padding:10px}}:focus-visible{{outline:3px solid var(--gold);outline-offset:4px}}@media(max-width:700px){{body{{font-size:17px}}main{{padding:22px 16px 60px}}.grid{{grid-template-columns:1fr}}}}</style></head><body><a class="skip" href="#passes">Skip to passes</a><main><nav><a href="index.html">Research home</a> · <a href="us-theme-atlas.html">Connections</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-evidence-audit.html">Evidence audit</a></nav><header><p class="eyebrow">Deeper checks of the connected map</p><h1>What has been checked beyond the opening search?</h1><p class="lead">Four short evidence passes follow a condition through household life, firm behavior, money, and public power. They are findings with limits, not final explanations.</p></header><p class="note">Read each route as a question. The words “still open” show the missing link that deserves the next test.</p><div id="passes" class="grid">{cards}</div><footer><p><a href="us-theme-atlas.html">Return to the connected atlas</a> · <a href="../analysis/us-matched-evidence-index.md">Read the Markdown index</a></p></footer></main></body></html>'''
html = html.replace("Four short evidence passes", f"{len(items)} short evidence passes")
(ROOT / "site/us-matched-evidence.html").write_text(html)
print(f"Built matched-evidence index for {len(items)} passes.")
