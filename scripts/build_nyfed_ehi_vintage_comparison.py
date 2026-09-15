#!/usr/bin/env python3
"""Build a bounded comparison of the December 2025 and April 2026 NY Fed EHI vintages."""
from __future__ import annotations
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
old = json.loads((ROOT / "analysis/records/us-nyfed-economic-heterogeneity-2025.json").read_text())
new = json.loads((ROOT / "analysis/records/us-nyfed-economic-heterogeneity-april-2026.json").read_text())

def measures(record, index):
    return record["observations"][index]["measures"]

old_inf, new_inf = measures(old, 0), measures(new, 0)
old_earn, new_earn = measures(old, 1), measures(new, 1)
rows = [
    ("Hispanic inflation position", old_inf["hispanic_inflation_gap"]["value"], "below national average", new_inf["hispanic_relative_direction"]["value"], "constructed demographic-CPI position"),
    ("Rural inflation gap", "not recorded in this vintage", "—", new_inf["rural_inflation_gap"]["value"], "percentage points from national inflation"),
    ("Black/white earnings ratio", old_earn["black_to_white_earnings"]["value"], old_earn["black_to_white_earnings"]["unit"], new_earn["black_to_white_earnings"]["value"], new_earn["black_to_white_earnings"]["unit"]),
    ("Hispanic/white earnings ratio", old_earn["hispanic_to_white_earnings"]["value"], old_earn["hispanic_to_white_earnings"]["unit"], new_earn["hispanic_to_white_earnings"]["value"], new_earn["hispanic_to_white_earnings"]["unit"]),
    ("Noncollege/college earnings ratio", old_earn["noncollege_to_college_earnings"]["value"], old_earn["noncollege_to_college_earnings"]["unit"], new_earn["noncollege_to_college_earnings"]["value"], new_earn["noncollege_to_college_earnings"]["unit"]),
    ("Women/men earnings ratio", old_earn["women_to_men_earnings"]["value"], old_earn["women_to_men_earnings"]["unit"], new_earn["women_to_men_earnings"]["value"], new_earn["women_to_men_earnings"]["unit"]),
]
def fmt(value):
    return f"{value:.1f}" if isinstance(value, float) else str(value)

md = [
    "# New York Fed EHI vintage comparison: December 2025 to April 2026",
    "",
    "**Checked:** 2026-09-13  ",
    "**Status:** reproducible bounded vintage comparison",
    "",
    "## What changed",
    "",
    "The April 2026 vintage should not be read as a simple update to a fixed group ranking. It reports a gasoline-driven reversal in several inflation positions and a new real-spending response after the March 2026 shock. The table preserves missing prior-vintage values instead of manufacturing a change score.",
    "",
    "| Measure | December 2025 | April 2026 | Unit / interpretation |",
    "|---|---:|---:|---|",
]
for label, before, before_unit, after, after_unit in rows:
    md.append(f"| {label} | {fmt(before)} | {fmt(after)} | {after_unit} |")
md += [
    "",
    "## Spending response in the new vintage",
    "",
    "The April release reports that real gasoline and real retail-ex-auto spending fell for nearly all groups after the March 2026 gasoline shock. Lower-income groups reduced real gasoline spending more than higher-income groups, while higher-income groups increased nominal gasoline spending more. This is a group-level receipt-panel direction, not a same-household event-study estimate.",
    "",
    "## Reading rule",
    "",
    "The comparison is not a causal before/after estimate. Demographic inflation uses prior Consumer Expenditure Survey budget shares and CPI categories; earnings ratios condition on employment; spending uses Numerator receipts and permissioned-email data. The source also states that EHI indicators are not official estimates of the Federal Reserve System or FOMC.",
    "",
    "## Next test",
    "",
    "Align household fuel exposure, commuting and care trips, income, liquid assets, debt, actual prices, spending, and later trust or political judgment around a dated shock. Retain groups and households whose behavior did not change.",
    "",
    "## Sources",
    "",
    "- [December 2025 EHI record](../../records/us-nyfed-economic-heterogeneity-2025.json)",
    "- [April 2026 EHI record](../../records/us-nyfed-economic-heterogeneity-april-2026.json)",
    "- [New York Fed EHI release page](https://www.newyorkfed.org/research/economic-heterogeneity-indicators)",
]
(ROOT / "analysis/projects/us-cost-trust-politics/new-york-fed-ehi-vintage-comparison-v1.md").write_text("\n".join(md) + "\n")

table_rows = "".join(f"<tr><td>{html.escape(label)}</td><td>{html.escape(fmt(before))}</td><td>{html.escape(fmt(after))}</td><td>{html.escape(after_unit)}</td></tr>" for label, before, before_unit, after, after_unit in rows)
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>New York Fed EHI vintage comparison</title><style>:root{{--p:#f5f3ed;--i:#18322d;--m:#566a63;--l:#cbd8d0;--g:#174f43;--w:#b86b2b;--c:#fffefa}}*{{box-sizing:border-box}}body{{margin:0;background:var(--p);color:var(--i);font:18px/1.7 system-ui,sans-serif}}main{{max-width:960px;margin:auto;padding:25px 22px 80px}}a{{color:var(--g)}}h1,h2{{font-family:Georgia,serif;font-weight:normal;line-height:1.12}}h1{{font-size:clamp(2.7rem,7vw,5rem);margin:38px 0 20px}}h2{{font-size:2rem;margin:52px 0 15px}}.lead{{font:1.3rem/1.5 Georgia,serif;max-width:820px}}.note{{border-left:4px solid var(--w);padding:16px 20px;background:#fff8e9}}table{{border-collapse:collapse;width:100%;background:var(--c)}}th,td{{border:1px solid var(--l);padding:12px;text-align:left;vertical-align:top}}th{{color:var(--m);font-size:.82rem;text-transform:uppercase}}footer{{border-top:1px solid var(--l);margin-top:55px;padding-top:18px;color:var(--m)}}@media(max-width:650px){{body{{font-size:17px}}main{{padding:18px 15px}}table{{font-size:.9rem}}}}</style></head><body><main><nav><a href="index.html">Research home</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-program-dashboard.html">Program dashboard</a></nav><h1>New York Fed EHI vintage comparison</h1><p class="lead">December 2025 to April 2026: the distribution of inflation and spending changed after a gasoline shock.</p><div class="note"><strong>Bounded reading:</strong> this is a vintage comparison of derived group indicators and receipt-panel directions, not a household-level causal before/after estimate.</div><h2>What changed</h2><table><thead><tr><th>Measure</th><th>December 2025</th><th>April 2026</th><th>Unit / interpretation</th></tr></thead><tbody>{table_rows}</tbody></table><h2>Spending response</h2><p>Real gasoline and real retail-ex-auto spending fell for nearly all groups after the March 2026 gasoline shock. Lower-income groups reduced real gasoline spending more than higher-income groups, while higher-income groups increased nominal gasoline spending more.</p><h2>Reading rule</h2><p>The EHI inflation measure combines prior Consumer Expenditure Survey budget shares with CPI categories; earnings ratios condition on employment; spending uses Numerator receipts and permissioned-email data. The indicators are not official estimates of the Federal Reserve System or FOMC.</p><h2>Next test</h2><p>Align household fuel exposure, commuting and care trips, income, liquid assets, debt, actual prices, spending, and later trust or political judgment around a dated shock. Retain households whose behavior did not change.</p><footer><a href="../analysis/projects/us-cost-trust-politics/new-york-fed-ehi-vintage-comparison-v1.md">Read the Markdown record</a> · <a href="../analysis/records/us-nyfed-economic-heterogeneity-2025.json">December record</a> · <a href="../analysis/records/us-nyfed-economic-heterogeneity-april-2026.json">April record</a></footer></main></body></html>"""
(ROOT / "site/us-nyfed-ehi-vintage-comparison.html").write_text(page)
print("Built New York Fed EHI vintage comparison")

