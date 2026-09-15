#!/usr/bin/env python3
"""Audit how registered source families are represented in analysis evidence."""

from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "manifests/source-registry.json"
OUT = ROOT / "analysis/US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.md"

registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
source_texts = []
base = ROOT / "analysis"
for dirpath, dirnames, filenames in os.walk(base):
    # Prune captured/raw data directories before traversal; these files are
    # deliberately outside the source-family coverage corpus.
    dirnames[:] = [name for name in dirnames if name != "data"]
    for filename in filenames:
        path = Path(dirpath) / filename
        if path == OUT or path.suffix.lower() not in {".md", ".json", ".txt"}:
            continue
        try:
            if path.stat().st_size > 2_000_000:
                continue
            source_texts.append((path, path.read_text(encoding="utf-8", errors="ignore")))
        except OSError:
            continue

def norm_host(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return host.removeprefix("www.")

rows = []
for source in registry["sources"]:
    host = norm_host(source["url"])
    rows.append({"id": source["id"], "name": source["name"], "url": source["url"], "host": host})

# Count in lowercase strings using the C-level string operations. This avoids
# the repeated Python regex scans that made the original audit scale poorly.
counts = {row["id"]: {"exact": 0, "host_refs": 0, "search_refs": 0,
                       "evidence_refs": 0, "record_exact": 0,
                       "evidence_files": 0} for row in rows}
for path, text in source_texts:
    lower = text.lower()
    is_search = path.name.startswith("source-search-")
    is_record = path.parent.name == "records"
    for row in rows:
        host_refs = lower.count(row["host"].lower())
        exact_refs = lower.count(row["url"].lower())
        if host_refs:
            counts[row["id"]]["host_refs"] += host_refs
            counts[row["id"]]["search_refs" if is_search else "evidence_refs"] += host_refs
            if not is_search:
                counts[row["id"]]["evidence_files"] += 1
        counts[row["id"]]["exact"] += exact_refs
        if is_record:
            counts[row["id"]]["record_exact"] += exact_refs

for row in rows:
    row.update(counts[row["id"]])

used = [row for row in rows if row["host_refs"]]
evidence_used = [row for row in rows if row["evidence_refs"]]
record_used = [row for row in rows if row["record_exact"]]
exact_used = [row for row in rows if row["exact"]]
family_counts = Counter(row["host"] for row in used)

# Reverse view: retain domains cited by evidence that are not covered by a
# registered source family. Subdomains count as covered by their registered
# parent (for example api.bls.gov by bls.gov).
observed_hosts = Counter()
observed_examples = defaultdict(list)
for path, text in source_texts:
    for match in re.findall(r"https?://[^\s\"<>]+", text, flags=re.IGNORECASE):
        url = match.rstrip(".,);]")
        host = norm_host(url)
        if not host:
            continue
        covered = any(host == row["host"] or host.endswith("." + row["host"]) for row in rows)
        if covered:
            continue
        observed_hosts[host] += 1
        if len(observed_examples[host]) < 3:
            observed_examples[host].append(str(path.relative_to(ROOT)))
reverse_rows = sorted(observed_hosts.items(), key=lambda item: (-item[1], item[0]))

review_classifications = {
    "doi.org": ("citation/index host", "Do not register; retain DOI as a source identifier and preserve the underlying publisher or institution separately."),
    "theguarantors.com": ("commercial case source", "Do not register as a recurring family yet; preserve product terms and treat the vendor material as case-specific evidence."),
    "support.sayrhino.com": ("commercial support host", "Do not register; support content is a product-route citation, not an independent recurring evidence family."),
    "btq-kassel.de": ("case-specific institution", "Retain as a cited interview/organization record; promote only if a maintained recurring evidence series is acquired."),
    "cfpnet.com": ("case-specific market source", "Retain the California FAIR Plan citation, but use California DOI and official plan records as the durable source family."),
    "cage.report": ("delivery/lookup host", "Do not register; use official DLA CAGE records as the authoritative identity source."),
    "docs.google.com": ("delivery/repository host", "Do not register; preserve the underlying NBER, institution, or document identity and access route."),
    "flipsnack.com": ("publication delivery host", "Do not register; preserve the county report and issuer as the source family."),
    "services.arcgis.com": ("data delivery host", "Do not register; preserve FEMA or agency ownership and the layer/service query separately."),
    "business.columbia.edu": ("academic case citation", "Retain as a study or institutional page citation; it is not yet a recurring maintained source family in this atlas."),
    "cambridge.org": ("academic publisher", "Retain the cited paper/publisher route; promote the specific research program only when it becomes a maintained acquisition lane."),
    "github.com": ("code/reproducibility host", "Do not register; preserve repository, release, commit, and upstream institution separately."),
    "help.theguarantors.com": ("commercial support host", "Do not register; treat as product documentation under the commercial case source."),
    "ilostat.github.io": ("official delivery/documentation host", "Do not register separately; keep ILOSTAT as the source family and preserve this route as a delivery/access artifact."),
    "leapeasy.com": ("commercial case source", "Do not register as a recurring family yet; preserve product terms and use official state/regulatory records for durable claims."),
    "sayrhino.com": ("commercial case source", "Do not register as a recurring family yet; preserve product terms and use official state/regulatory records for durable claims."),
    "sites.google.com": ("delivery/repository host", "Do not register; preserve the NBER paper, author, institution, or source record separately."),
    "support.leapeasy.com": ("commercial support host", "Do not register; support content is a product-route citation, not an independent recurring evidence family."),
    "dropbox.com": ("file delivery host", "Do not register; preserve the NBER or author-provided artifact, version, and hash."),
    "ftrebbi.com": ("author/project host", "Retain as a paper or author-data route; use the NBER record as the durable research family."),
    "investors.capgemini.com": ("company disclosure host", "Do not register separately; preserve Capgemini as the company source family and the report/version as the evidence item."),
    "tse-fr.eu": ("academic/case citation", "Retain the cited study route; it is not currently a maintained recurring family in the atlas."),
    "academic.oup.com": ("academic publisher", "Retain the cited paper/publisher route; promote a recurring research family only when a sustained acquisition lane exists."),
    "icpsr.github.io": ("data delivery/documentation host", "Do not register separately; preserve ICPSR or the originating survey as the durable source family."),
    "journals.uchicago.edu": ("academic publisher", "Retain the cited paper/publisher route; it is not currently a maintained recurring family in the atlas."),
    "open.gsa.gov": ("government API delivery host", "Do not register separately; preserve GSA/USAspending as the durable source family and the endpoint as the query route."),
    "cbp.gov": ("federal delivery and border source", "Do not register separately for the current CPSC case; preserve CBP as the official import/border comparator and promote it only if import surveillance becomes a maintained acquisition lane."),
    "nasbo.org": ("state-fiscal policy source", "Retain as a policy-research comparator for state fiscal capacity; promote it to a maintained source family only when recurring NASBO vintages are acquired and compared."),
}

lines = [
    "# Source registry coverage audit v1",
    "",
    f"**Checked:** {date.today().isoformat()}",
    "",
    "This control compares the registered source universe with the files under",
    "`analysis/`. It distinguishes a registered source from evidence that uses",
    "the source's domain. A domain hit can reflect a source-search packet, a",
    "record, a finding, or a related-source citation; it is not a quality score",
    "or proof that every source item was read in full.",
    "",
    f"- Registered source entries: **{len(rows)}**",
    f"- Entries with a domain reference anywhere in analysis: **{len(used)}**",
    f"- Entries with a domain reference outside source-search packets: **{len(evidence_used)}**",
    f"- Entries with an exact source URL in a machine record: **{len(record_used)}**",
    f"- Entries with an exact registered-URL reference: **{len(exact_used)}**",
    f"- Registered entries with no analysis-domain hit: **{len(rows) - len(used)}**",
    "",
    "## Coverage states",
    "",
    "- **evidence-bearing:** the source domain appears outside a source-search",
    "  packet, in a record, finding, layer, bridge, or other analysis artifact.",
    "- **machine-record URL:** the exact registered URL appears in an",
    "  `analysis/records/*.json` object.",
    "- **search-only:** the domain appears only in source-search packets and is",
    "  not yet visible in a substantive evidence artifact.",
    "- **exact URL referenced:** the registered landing URL itself appears in",
    "  the analysis corpus.",
    "- **no hit:** the source is registered but is not visible in the analysis",
    "  corpus; it remains a candidate acquisition or search lane.",
    "",
    "## Registered sources",
    "",
    "| Source | Role | Search refs | Evidence refs | Evidence files | Record exact URL | State |",
    "|---|---|---:|---:|---:|---:|---|",
]
for row, source in zip(rows, registry["sources"]):
    if row["evidence_refs"]:
        state = "evidence-bearing" + ("; machine-record URL" if row["record_exact"] else "")
    elif row["search_refs"]:
        state = "search-only"
    else:
        state = "no hit"
    role = source.get("role", "").replace("|", "\\|")
    lines.append(f"| [{source['name']}]({source['url']}) | {role} | {row['search_refs']} | {row['evidence_refs']} | {row['evidence_files']} | {row['record_exact']} | {state} |")

lines += [
    "",
    "## Reverse audit: observed domains outside the registry",
    "",
    "This is a review queue, not an automatic registration list. It excludes",
    "subdomains covered by a registered parent (for example `api.bls.gov` under",
    "BLS). Remaining domains may be mirrors, delivery hosts, partner sites, or",
    "one-off citations. Promote a domain only when it represents a durable source",
    "family that will be acquired, compared, or maintained over time.",
    "",
    f"- Observed domains outside registered families: **{len(reverse_rows)}**",
    f"- Review queue shown: **{min(len(reverse_rows), 40)}** highest-frequency domains",
    "",
    "| Domain | References | Example evidence files |",
    "|---|---:|---|",
]
for host, count in reverse_rows[:40]:
    examples = "; ".join(f"`{path}`" for path in observed_examples[host])
    lines.append(f"| `{host}` | {count} | {examples} |")

lines += [
    "",
    "## Reverse-audit decisions",
    "",
    "The table below records the current disposition of every observed outside",
    "domain. A non-registration decision is deliberate: the domain may still",
    "be useful evidence, but it is not promoted to a maintained source family",
    "without a recurring acquisition need and source-specific metadata.",
    "",
    "| Domain | Classification | Current decision |",
    "|---|---|---|",
]
for host, _count in reverse_rows:
    classification, decision = review_classifications.get(
        host, ("unclassified review candidate", "Requires manual review before promotion or exclusion."))
    lines.append(f"| `{host}` | {classification} | {decision} |")

lines += [
    "",
    "## Interpretation rule",
    "",
    "A source with no hit is not a failed source; it is an explicit breadth gap",
    "or a source that has not yet been used in the current corpus. A domain hit",
    "may come from a related citation rather than a direct estimate. Promotion",
    "still requires a source record with unit, date, geography, denominator,",
    "method, uncertainty, subgroup, counterexample, and boundary.",
    "",
    "Generated by `scripts/audit_source_registry_coverage.py`.",
]
OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"AUDITED {len(rows)} registered sources: {len(used)} domain-referenced, {len(exact_used)} exact-URL-referenced, {len(rows)-len(used)} no-hit")
