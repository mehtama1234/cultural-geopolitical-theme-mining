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
    "us-owner-household-business-matched-evidence-001": ("Work / cost", "family bill → business cash → firm and local life", "worker, customer, and closure effects"),
    "us-small-business-disaster-liquidity-matched-evidence-001": ("Work / cost / place", "disaster → recovery credit → firm and local options", "worker, customer, household, and repayment effects"),
    "us-medical-debt-relief-matched-evidence-001": ("Cost / health / voice", "illness → bill → debt record → relief", "health, care, and original-bill effects"),
    "us-small-business-support-size-cutoff-matched-evidence-001": ("Work / cost / voice", "eligibility rule → public demand → firm survival", "customer, worker, and owner-household effects"),
    "us-local-business-place-matched-evidence-001": ("Work / place / voice", "local conditions → application → lasting firm", "services, belonging, and political effects"),
    "us-vehicle-repair-household-matched-evidence-001": ("Cost / work / time", "repair bill → cash timing → access", "same-household work, care, and later-debt effects"),
    "us-safety-net-access-matched-evidence-001": ("Cost / time / voice", "need → rule and access → benefit kept or lost", "same-household food, work, debt, health, and trust effects"),
    "us-transfer-design-household-matched-evidence-001": ("Cost / time / voice", "aid form → spending choice → household security", "food security, care, trust, and long-run security"),
    "us-rental-assistance-eviction-matched-evidence-001": ("Cost / housing / voice", "rent shock → aid or counsel → housing case", "lasting housing, credit, work, and health effects"),
    "us-rent-guarantee-insurance-matched-evidence-001": ("Cost / housing / finance", "rent risk → pre-shock insurance → housing security", "market access, landlord response, and later tenant outcomes"),
    "us-rent-guarantee-market-matched-evidence-001": ("Cost / housing / finance", "lease screen → guarantee premium → tenant repayment risk", "lasting access and post-claim household debt"),
    "us-rent-guarantee-provider-comparison-matched-evidence-001": ("Cost / housing / finance", "provider screen → paid guarantee → landlord protection → tenant debt", "state terms, claims, repayment, and renewals"),
    "us-rent-guarantee-state-terms-matched-evidence-001": ("Cost / housing / voice", "provider → state filing → policy terms → tenant risk", "state policy forms, prices, and post-claim outcomes"),
    "us-rent-guarantee-four-state-matched-evidence-001": ("Cost / housing / voice", "state rule → policy form → claim → tenant duty", "current rates, claims, repayment, and renewal by state"),
    "us-rent-guarantee-claim-mechanics-matched-evidence-001": ("Cost / housing / voice", "default → claim process → landlord payment → tenant recovery risk", "claim timing, disputes, and housing outcome"),
    "us-inflation-price-perception-matched-evidence-001": ("Cost / voice / customer", "price and wage change → buying power → trust pressure", "same-household basket, substitution, and vote"),
    "us-inflation-measurement-household-basket-matched-evidence-001": ("Cost / customer / voice", "price index + wage + spending → household basket", "same-household substitution, debt, trust, and vote"),
    "us-inflation-cex-basket-build-matched-evidence-001": ("Cost / customer / voice", "income + tenure → spending pattern → possible pressure", "same-family purchases and later response"),
    "us-tariff-price-pass-through-matched-evidence-001": ("Cost / customer / voice / work", "trade rule → import cost → retail price → household choice", "firm margins, household exposure, and political response"),
    "us-economic-voting-real-wages-matched-evidence-001": ("Cost / voice / work", "local prices + pay → buying power → blame → vote or turnout", "individual burden, policy knowledge, and cause"),
    "us-energy-household-burden-matched-evidence-001": ("Cost / housing / work / voice", "home condition + energy price → bill pressure → sacrifice", "health, work, housing, and trust outcome"),
    "us-health-cost-household-choice-matched-evidence-001": ("Cost / health / work / voice", "medical cost → care choice → debt or work shock", "same-household health, income, and trust result"),
    "us-consumer-credit-liquidity-matched-evidence-001": ("Cost / finance / voice", "bill shock → cash gap → credit → future room", "same-household repayment and later access"),
    "us-hidden-fees-price-salience-matched-evidence-001": ("Cost / customer / finance / voice", "headline price → late cost → choice → final burden", "same-household cost, quality, and repeat choice"),
    "us-bank-fees-household-wellbeing-matched-evidence-001": ("Cost / finance / voice", "low account cash → fee or overdraft → later cost", "payment success and household recovery"),
    "us-bank-depositor-inertia-matched-evidence-001": ("Cost / finance / voice", "account habit → switching effort → lower return or stable funding", "customer net return and bank stability"),
    "us-benefit-cliff-work-choice-matched-evidence-001": ("Cost / work / voice", "earnings rise → aid changes → real household room", "same-family net resources and work outcome"),
    "us-family-support-hidden-safety-net-matched-evidence-001": ("Cost / family / work / voice", "household shock → family help → helper cost", "receiver and helper's later stability"),
    "us-childcare-work-cost-matched-evidence-001": ("Cost / family / work / voice", "child care need → paid or unpaid care → work change", "same-family income, quality, and stability"),
    "us-aging-care-strain-matched-evidence-001": ("Cost / family / work / voice", "aging or illness → unpaid care → work and money loss", "care quality, caregiver recovery, and public support"),
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
