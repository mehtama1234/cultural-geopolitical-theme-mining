"""Build readable finding pages from the Markdown source of truth.

This deliberately uses the Markdown memo as the content source. The page
layout is shared, so a deeper memo cannot silently leave an older HTML summary
behind.
"""

import re
import os
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]

STYLE = """:root{--paper:#f5f3ed;--ink:#18322d;--muted:#566a63;--line:#cbd8d0;--green:#174f43;--gold:#b86b2b;--blue:#e8eee9;--card:#fffefa}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.72 system-ui,sans-serif}main{max-width:960px;margin:auto;padding:24px 22px 84px}a{color:var(--green);text-underline-offset:4px}nav{font-size:.95rem}header{padding:34px 0 26px;border-bottom:1px solid var(--line)}h1,h2,h3{font-family:Georgia,serif;font-weight:normal;line-height:1.12}h1{font-size:clamp(2.7rem,7vw,5.5rem);margin:20px 0}h2{font-size:2.1rem;margin:58px 0 16px;scroll-margin-top:20px}h3{font-size:1.4rem;scroll-margin-top:20px}.eyebrow{color:var(--green);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}.lede{font-size:1.28rem;max-width:820px}.memo{padding-top:8px}.memo table{border-collapse:collapse;width:100%;background:var(--card);margin:22px 0;display:block;overflow-x:auto}.memo th,.memo td{border:1px solid var(--line);padding:13px;text-align:left;vertical-align:top;min-width:150px}.memo th{color:var(--muted);font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}.memo blockquote{border-left:4px solid var(--gold);margin:24px 0;padding-left:20px;font:1.3rem/1.5 Georgia,serif}.memo pre{background:var(--blue);padding:20px;border-radius:10px;overflow:auto;white-space:pre-wrap}.memo code{background:var(--blue);padding:2px 5px;border-radius:4px}.memo hr{border:0;border-top:1px solid var(--line);margin:38px 0}.memo img{max-width:100%}.note{border-left:4px solid var(--gold);padding-left:18px;color:var(--muted)}.reader-guide{display:grid;grid-template-columns:minmax(0,1fr) minmax(230px,.55fr);gap:18px;margin:26px 0 8px}.reader-guide>div,.toc{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:16px 18px}.reader-guide p{margin:0}.reader-guide strong{color:var(--green)}.toc{font-size:.92rem}.toc-title{margin:0 0 8px;color:var(--muted);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase}.toc ul{margin:0;padding-left:18px}.toc li{margin:4px 0}.toc h3{font:inherit;margin:0}.toc .toc-sub{padding-left:14px;font-size:.88rem}@media(max-width:700px){body{font-size:17px}main{padding:18px 16px 60px}.memo table{font-size:.92rem}.reader-guide{grid-template-columns:1fr}}.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:10px;background:white;padding:10px;z-index:2}:focus-visible{outline:3px solid var(--gold);outline-offset:4px}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

# Keep the reading rail visible on wide screens and make long memos usable on
# paper; the mobile rule below returns it to normal flow.
STYLE += ".toc{position:sticky;top:14px;height:max-content;max-height:calc(100vh - 28px);overflow:auto}.site-nav{color:var(--muted);white-space:nowrap;overflow-x:auto;padding-bottom:3px}.reader-nav{position:sticky;top:0;z-index:4;display:flex;gap:8px;align-items:center;margin:0 -22px;padding:10px 22px;background:rgba(245,243,237,.97);border-bottom:1px solid var(--line);white-space:nowrap;overflow-x:auto}.reader-nav a{padding:5px 10px;border:1px solid transparent;border-radius:999px;text-decoration:none}.reader-nav a:hover,.reader-nav a:focus-visible{border-color:var(--line);background:var(--card)}.reader-nav .reader-nav-label{margin-right:4px;color:var(--muted);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}@media(max-width:700px){.toc{position:static;max-height:none}.reader-nav{margin:0 -16px;padding-left:16px;padding-right:16px}}@media print{body{background:white;color:black;font-size:11pt}main{max-width:none;padding:0}.reader-guide,.reader-nav{display:none}nav,footer,.skip{display:none}.memo a{color:black;text-decoration:none}.memo table{display:table;overflow:visible;font-size:9pt}.memo h1,.memo h2,.memo h3{break-after:avoid}.memo p,.memo table{break-inside:avoid}}"


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def clean(value: str) -> str:
    return " ".join(value.lower().split())


def heading_text(fragment: str) -> str:
    """Return readable text from a rendered heading fragment."""
    parsed = Text()
    parsed.feed(fragment)
    return " ".join(" ".join(parsed.parts).split())


def add_heading_ids_and_toc(body: str) -> tuple[str, str]:
    """Give section headings stable anchors and build a compact contents rail."""
    used: dict[str, int] = {}
    entries: list[tuple[int, str, str]] = []
    pattern = re.compile(r"<h([23])>(.*?)</h\1>", re.S)

    def replace(match: re.Match[str]) -> str:
        level = int(match.group(1))
        label = heading_text(match.group(2))
        base = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-") or "section"
        used[base] = used.get(base, 0) + 1
        slug = base if used[base] == 1 else f"{base}-{used[base]}"
        entries.append((level, label, slug))
        return f'<h{level} id="{escape(slug, quote=True)}">{match.group(2)}</h{level}>'

    body = pattern.sub(replace, body)
    if not entries:
        return body, ""
    links = []
    for level, label, slug in entries:
        cls = ' class="toc-sub"' if level == 3 else ""
        links.append(f'<li{cls}><a href="#{escape(slug, quote=True)}">{escape(label)}</a></li>')
    toc = '<nav class="toc" aria-label="On this page"><p class="toc-title">On this page</p><ul>' + "".join(links) + "</ul></nav>"
    return body, toc


def should_rebuild(memo: Path, page: Path) -> bool:
    if not page.exists():
        return True
    current_page = page.read_text()
    if '.toc{position:sticky' not in current_page or 'class="reader-nav"' not in current_page:
        return True
    # Content heuristics below are useful for repairing legacy pages, but they
    # must not suppress an ordinary source edit.  A published page whose
    # Markdown source is newer is stale even if it still contains all of the
    # old section markers.
    if memo.stat().st_mtime_ns > page.stat().st_mtime_ns:
        return True
    source = memo.read_text()
    current = current_page
    # A page served with ``python -m http.server --directory site`` cannot
    # resolve repository-relative Markdown/JSON links outside site/. Rebuild
    # older pages that still contain those links so the published view stays
    # readable on its own.
    if 'href="../analysis/' in current or "href='../analysis/" in current:
        return True
    parsed = Text()
    parsed.feed(current)
    visible = clean(" ".join(parsed.parts))
    title = re.search(r"^# (.+)$", source, re.M)
    if not title or clean(title.group(1)) not in visible:
        return True
    urls = re.findall(r"https?://[^)\s]+", source)
    if any(url.lower() not in current.lower() for url in urls):
        return True
    return (
        not any(needle in visible for needle in ("the deeper finding", "the argument has limits", "what this changes", "the connection", "the useful surprise", "the control problem", "the important split"))
        or not any(needle in visible for needle in ("next test", "the next test is", "what would change the finding"))
        or "reading rule" not in visible
    )


def rewrite_published_links(body: str, memo: Path, published_outputs: dict[Path, str] | None = None) -> str:
    """Translate Markdown-relative links into links valid from ``site/``.

    A Markdown memo is authored relative to its own directory (usually
    ``analysis/findings`` or a project directory).  The rendered page lives
    under ``site/``, so copying those hrefs verbatim silently breaks links to
    source records, project layers, and other Markdown evidence.  Only links
    that resolve inside this repository are rewritten; external URLs and
    unresolved references are left untouched so the source remains visible.
    """
    pattern = re.compile(r'(\bhref=["\'])([^"\']+)(["\'])')

    def replace(match: re.Match[str]) -> str:
        prefix, href, suffix = match.groups()
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
            return match.group(0)
        source_target = (memo.parent / parts.path).resolve()
        try:
            source_target.relative_to(ROOT.resolve())
        except ValueError:
            return match.group(0)
        if not source_target.exists():
            return match.group(0)
        # Prefer a published HTML counterpart when the linked Markdown memo
        # has one. This keeps cross-finding links usable from a site-only
        # server while leaving source files without a rendered counterpart
        # explicit in the source record.
        if source_target.suffix.lower() == ".md":
            planned_name = (published_outputs or {}).get(source_target)
            html_target = ROOT / "site" / (planned_name or f"{source_target.stem}.html")
            if planned_name or html_target.exists():
                published_target = os.path.relpath(html_target, ROOT / "site").replace(os.sep, "/")
                return f"{prefix}{urlunsplit((parts.scheme, parts.netloc, published_target, parts.query, parts.fragment))}{suffix}"
        published_target = os.path.relpath(source_target, ROOT / "site").replace(os.sep, "/")
        return f"{prefix}{urlunsplit((parts.scheme, parts.netloc, published_target, parts.query, parts.fragment))}{suffix}"

    return pattern.sub(replace, body)


def render(memo: Path, published_outputs: dict[Path, str] | None = None) -> str:
    source = memo.read_text()
    title_match = re.search(r"^# (.+)$", source, re.M)
    title = title_match.group(1) if title_match else memo.stem
    body = markdown.markdown(source, extensions=["tables", "fenced_code", "sane_lists"])
    body = rewrite_published_links(body, memo, published_outputs)
    body, toc = add_heading_ids_and_toc(body)
    guide = f'''<div class="reader-guide"><div><p><strong>How to read:</strong> start with the bounded finding, then inspect the evidence table or measures, the interpretation, the counterexamples, and the next test. The page keeps direct observations separate from proposed connections.</p></div>{toc}</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{escape(title)}"><title>{escape(title)}</title><style>{STYLE}</style></head><body><a class="skip" href="#finding">Skip to finding</a><main><nav class="site-nav"><a href="index.html">Research home</a> · <a href="us-theme-atlas.html">Connections</a> · <a href="us-big-picture-synthesis.html">Big picture</a> · <a href="us-matched-evidence.html">Matched evidence</a></nav><nav class="reader-nav" aria-label="Reader navigation"><span class="reader-nav-label">Read</span><a href="reading-room.html">Guided route</a><a href="review-guide.html">Review guide</a><a href="theme-trends.html">Theme trends</a><a href="us-program-dashboard.html">Program dashboard</a><a href="source-registry.html">Source families</a><a href="us-source-coverage.html">Project coverage</a><a href="us-evidence-audit.html">Evidence controls</a></nav><header><p class="eyebrow">Connected US finding · source-traceable memo</p><div class="lede">Full current Markdown record, presented in a responsive reading layout.</div></header>{guide}<article id="finding" class="memo">{body}</article><footer><p><a href="us-evidence-audit.html">Open the evidence audit</a> · <a href="us-program-dashboard.html">Open the program dashboard</a> · <a href="#finding">Back to top</a></p><p class="note">Claims, limits, and open questions are kept together. The repository Markdown remains the source record; this page is the published reading view.</p></footer></main></body></html>'''


def main():
    rebuilt = 0
    checked = 0
    # Render both the cross-program matched-evidence records and the deeper
    # project-level finding memos. The Markdown files remain the source of
    # truth; this only adds the shared reading layout to project findings.
    memos = list((ROOT / "analysis/findings").glob("*-matched-evidence-001.md"))
    # Program-level path memos use the same source-of-truth and reading layout
    # as matched evidence, while retaining a distinct filename and meaning.
    memos.extend((ROOT / "analysis/findings").glob("*-path-001.md"))
    # Keep newer root-level findings visible even when their filenames use a
    # domain-specific suffix rather than the older matched/path conventions.
    memos.append(ROOT / "analysis/findings/us-doxo-bill-payment-hidden-fees-001.md")
    memos.append(ROOT / "analysis/findings/us-grubhub-platform-remedy-001.md")
    memos.append(ROOT / "analysis/findings/us-snap-data-governance-accountability-001.md")
    memos.extend((ROOT / "analysis/projects").glob("**/findings/*.md"))
    # A small number of project audits are reader-facing evidence memos even
    # though they are not findings. Keep them in this shared renderer so the
    # server publishes the acquisition boundary alongside the findings.
    memos.append(ROOT / "analysis/projects/us-customer-automation-recourse/cfpb-public-event-ledger-acquisition-audit-2026-09-14.md")
    memos.append(ROOT / "analysis/projects/us-customer-automation-recourse/cfpb-api-vintage-refresh-2026-09-14.md")
    memos.append(ROOT / "analysis/projects/us-customer-automation-recourse/cfpb-route-vintage-recheck-2026-09-15.md")
    memos.append(ROOT / "analysis/projects/us-customer-automation-recourse/cfpb-2024-aggregation-refresh-2026-09-13.md")
    memos.append(ROOT / "analysis/projects/ai-work-control/world-bank-wbes-ai-access-recheck-2026-09-14.md")
    memos.append(ROOT / "analysis/projects/ai-work-control/ilostat-access-audit-2026-09-15.md")
    memos.append(ROOT / "analysis/projects/ai-work-control/nber-w33795-shifting-work-patterns-source-record-v1.md")
    memos.append(ROOT / "analysis/projects/ai-work-control/chatham-house-data-trust-governance-layer-v1.md")
    memos.append(ROOT / "analysis/projects/us-cost-trust-politics/htops-2025-panel-linkage-audit-v1.md")
    # Publish the material/time/care bridge itself, not only its matched
    # finding, so the cross-source comparison remains readable as a durable
    # program artifact.
    memos.append(ROOT / "analysis/projects/us-household-calendar-integration/price-pressure-time-social-participation-cross-source-bridge-v1.md")
    # Publish the care-cost/time/work cross-source finding as a first-class
    # program memo even though it lives at the repository-level findings path.
    memos.append(ROOT / "analysis/findings/us-care-cost-time-work-currency-cross-source-001.md")
    # Promote the automatic-saving multi-currency bridge into the program-level
    # reading surface; the project findings remain the detailed source records.
    memos.append(ROOT / "analysis/findings/us-automatic-saving-multi-currency-policy-bridge-001.md")
    # Keep the atlas-level cross-source synthesis readable from the server as
    # well as from the repository control records.
    memos.append(ROOT / "analysis/US-CROSS-SOURCE-TREND-SYNTHESIS_V1.md")
    # Publish the curated review route so readers can move from the broad goal
    # to representative writeups without first learning the repository tree.
    review_guide = ROOT / "REVIEW-GUIDE_V1.md"
    memos.append(review_guide)
    # Publish the curated AI/work review packet and the representative case
    # records it names, so the review route is usable from the site rather than
    # requiring readers to navigate the repository tree.
    review_packet = ROOT / "REVIEW-PACKET_AI-WORK-CONTROL_V1.md"
    memos.append(review_packet)
    ai_work_synthesis = ROOT / "analysis/projects/ai-work-control/anticipatory-to-remedial-worker-control-synthesis-v1.md"
    memos.append(ai_work_synthesis)
    memos.append(ROOT / "analysis/projects/ai-work-control/australian-platform-deactivation-cross-case-synthesis-v1.md")
    ai_work_reader_records = [
        ROOT / "analysis/projects/ai-work-control/amazon-bandameeda-deactivation-remedy-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-kumar-merits-dismissal-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-warraich-unfair-deactivation-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-warraich-remedy-followup-recheck-v1.md",
        ROOT / "analysis/projects/ai-work-control/platform-remedy-implementation-depth-audit-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-khan-reactivation-lost-pay-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-rehman-formal-reactivation-lost-remuneration-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-hotak-access-restoration-followup-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/australian-lost-pay-order-followups-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-waheed-merits-remedy-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-satbir-singh-eligibility-dismissal-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-phillipps-lewis-eligibility-stay-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-phillipps-lewis-post-hotak-followup-audit-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-kyei-timing-extension-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-mohamed-merits-compliant-process-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/uber-ali-code-noncompliance-no-unfairness-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/ibm-germany-works-council-ai-framework-governance-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/microsoft-germany-works-council-copilot-deployment-record-v1.md",
        ROOT / "analysis/projects/ai-work-control/data/microsoft-places-technical-control-surface-source-note-v1.md",
        ROOT / "analysis/projects/ai-work-control/australian-platform-deactivation-case-census-v1.md",
        ROOT / "analysis/projects/ai-work-control/australian-remedy-implementation-acquisition-audit-2026-09-15.md",
        ROOT / "analysis/projects/ai-work-control/australia-malaysia-cambodia-stage-compatible-comparison-v1.md",
        ROOT / "analysis/projects/ai-work-control/global-platform-remedy-comparison-v1.md",
        ROOT / "analysis/projects/ai-work-control/remedy-spectrum-cross-domain-synthesis-v1.md",
        ROOT / "analysis/projects/ai-work-control/findings/ai-work-control-087.md",
        ROOT / "analysis/projects/ai-work-control/findings/ai-work-control-088.md",
        ROOT / "analysis/projects/ai-work-control/findings/ai-work-control-089.md",
        ROOT / "analysis/projects/ai-work-control/findings/ai-work-control-090.md",
    ]
    memos.extend(ai_work_reader_records)
    # Publish the capability/dependence bridge and its World Bank capability
    # layer so the geopolitical route is readable without leaving the server.
    memos.append(ROOT / "analysis/projects/ai-work-control/domestic-capacity-dependence-state-leverage-cross-source-bridge-v1.md")
    memos.append(ROOT / "analysis/projects/ai-work-control/capability-dependence-local-power-layer-v1.md")
    # Publish the worker/workplace event-ledger specification alongside the
    # findings so the missing same-unit acquisition contract is inspectable.
    memos.append(ROOT / "analysis/projects/ai-work-control/worker-workplace-event-ledger-v1.md")
    # Publish the public-system same-episode implementation contract alongside
    # the public findings; this is the main route from aggregate transitions to
    # notice, effort, remedy, protected/sacrificed outcomes, and recovery.
    memos.append(ROOT / "analysis/projects/us-safety-net-access/same-episode-event-ledger-implementation-v1.md")
    # Publish the WBNS/ICPSR acquisition gate so the strongest next public-
    # system route is readable with its access boundary and no-estimate rule.
    memos.append(ROOT / "analysis/projects/us-safety-net-access/wbns-public-use-route-acquisition-audit-v1.md")
    memos.append(ROOT / "analysis/projects/us-safety-net-access/wbns-2025-age-care-material-security-layer-v1.md")
    # Publish the durable continuity and current-status records so the
    # long-term program state is inspectable from the same server.
    memos.append(ROOT / "analysis/US-BROAD-PROGRAM-CONTINUITY-LEDGER_V1.md")
    memos.append(ROOT / "analysis/US-BROAD-CURRENT-STATUS-AUDIT_V1.md")
    memos.append(ROOT / "analysis/US-TREND-METADATA-COVERAGE-AUDIT_V1.md")
    # Keep the source-registry control server-visible as well; source breadth
    # is part of the published program state, not only a local audit artifact.
    memos.append(ROOT / "analysis/US-SOURCE-REGISTRY-COVERAGE-AUDIT_V1.md")
    # Publish the arrow-level evidence matrix as a navigable control record;
    # it is the bridge between project findings and the end-to-end program.
    memos.append(ROOT / "analysis/US-BROAD-EVIDENCE-MATRIX_V1.md")
    # Give the cultural/meaning lane a stable reader route instead of exposing
    # its project README only through repository navigation.
    cultural_politics_readme = ROOT / "analysis/projects/us-cost-trust-politics/README.md"
    memos.append(cultural_politics_readme)
    # Publish the material-to-political-meaning synthesis as a long-form route
    # across the linked HTOPS panel, subgroup contrasts, and open attribution
    # and action arrows.
    material_political_synthesis = ROOT / "analysis/projects/us-cost-trust-politics/material-pressure-to-political-meaning-synthesis-v1.md"
    memos.append(material_political_synthesis)
    # Publish the cross-scale political-meaning synthesis so county-level
    # purchasing power, ANES respondent judgment, and HTOPS household
    # persistence remain readable as related but non-interchangeable paths.
    material_pressure_scale_synthesis = ROOT / "analysis/projects/us-cost-trust-politics/material-pressure-scale-meaning-synthesis-v1.md"
    memos.append(material_pressure_scale_synthesis)
    # Give the material/time/care lane a single reader route that synthesizes
    # the validated SIPP, ATUS, SHED, and MEPS surfaces without implying a
    # same-household causal join that the current data do not support.
    material_time_care_program = ROOT / "analysis/projects/us-household-calendar-integration/material-time-care-program-v1.md"
    memos.append(material_time_care_program)
    # Give the geopolitical/state-capacity lane a reader route that preserves
    # the allocation -> procurement -> realization -> response distinctions.
    state_capacity_program = ROOT / "analysis/projects/ai-work-control/state-capacity-geopolitical-program-v1.md"
    memos.append(state_capacity_program)
    jassm_realization_synthesis = ROOT / "analysis/projects/ai-work-control/jassm-lrasm-procurement-to-capability-realization-synthesis-v1.md"
    memos.append(jassm_realization_synthesis)
    # Give the safety-net lane a stable reader route across program scale,
    # administrative handling, lived barriers, and the same-episode design.
    safety_net_readme = ROOT / "analysis/projects/us-safety-net-access/README.md"
    memos.append(safety_net_readme)
    # Publish the public-help route as a reader-facing synthesis across
    # administrative timeliness, lived barriers, material buffering, and
    # institution-specific confidence.
    public_help_route_synthesis = ROOT / "analysis/projects/us-safety-net-access/public-help-route-buffer-judgment-synthesis-v1.md"
    memos.append(public_help_route_synthesis)
    memos.append(ROOT / "analysis/projects/us-immigration-local-demand/wbns-2025-immigration-concerns-essential-activity-chilling-layer-v1.md")
    # Give the consumer-power lane a stable reader route from firm process to
    # visible complaint, response label, remedy, trust, and exit.
    consumer_recourse_readme = ROOT / "analysis/projects/us-customer-automation-recourse/README.md"
    memos.append(consumer_recourse_readme)
    # Publish the consumer-recourse synthesis as a long-form route from
    # household loss through complaint visibility, clocks, response labels,
    # and the still-open remedy/exit endpoint.
    consumer_recourse_synthesis = ROOT / "analysis/projects/us-customer-automation-recourse/consumer-recourse-visibility-remedy-synthesis-v1.md"
    memos.append(consumer_recourse_synthesis)
    exit_observability_audit = ROOT / "analysis/projects/us-customer-automation-recourse/practical-exit-observability-audit-v1.md"
    memos.append(exit_observability_audit)
    practical_exit_synthesis = ROOT / "analysis/projects/us-customer-automation-recourse/practical-exit-cross-domain-synthesis-v1.md"
    memos.append(practical_exit_synthesis)
    exit_ledger_implementation = ROOT / "analysis/projects/us-customer-automation-recourse/practical-exit-ledger-implementation-v1.md"
    exit_platform_dry_run = ROOT / "analysis/projects/us-customer-automation-recourse/practical-exit-platform-ledger-dry-run-v1.md"
    exit_cfpb_dry_run = ROOT / "analysis/projects/us-customer-automation-recourse/cfpb-practical-exit-contract-dry-run-v1.md"
    memos.append(exit_ledger_implementation)
    memos.append(exit_platform_dry_run)
    memos.append(ROOT / "analysis/projects/us-customer-automation-recourse/platform-remedy-field-availability-audit-v1.md")
    memos.append(exit_cfpb_dry_run)
    capacity_dependence_audit = ROOT / "analysis/projects/ai-work-control/capacity-dependence-realization-audit-v1.md"
    memos.append(capacity_dependence_audit)
    jassm_control_surface_audit = ROOT / "analysis/projects/ai-work-control/jassm-subaward-control-surface-audit-v1.md"
    memos.append(jassm_control_surface_audit)
    material_meaning_action_audit = ROOT / "analysis/projects/us-cost-trust-politics/material-meaning-action-endpoint-audit-v1.md"
    memos.append(material_meaning_action_audit)
    ai_work_control_endpoint_audit = ROOT / "analysis/projects/ai-work-control/ai-work-control-endpoint-audit-v1.md"
    memos.append(ai_work_control_endpoint_audit)
    named_workplace_system_stage_ledger = ROOT / "analysis/projects/ai-work-control/named-workplace-system-stage-ledger-v1.md"
    memos.append(named_workplace_system_stage_ledger)
    broad_same_case_episode_availability_audit = ROOT / "analysis/broad-same-case-episode-availability-audit-v1.md"
    memos.append(broad_same_case_episode_availability_audit)
    broad_next_episode_selection = ROOT / "analysis/broad-next-episode-selection-v1.md"
    memos.append(broad_next_episode_selection)
    # Give the household-finance lane a stable reader route across prices,
    # buffers, credit, firm terms, adaptation, and political meaning.
    household_finance_readme = ROOT / "analysis/projects/us-household-financial-pressure/README.md"
    memos.append(household_finance_readme)
    # Publish the same-respondent household-pressure synthesis as a reader
    # route from financial-condition paths through adaptation, health, care,
    # and the open recovery/meaning arrows.
    household_pressure_synthesis = ROOT / "analysis/projects/us-household-financial-pressure/financial-pressure-adaptation-recovery-synthesis-v1.md"
    memos.append(household_pressure_synthesis)
    # Give the aging/care lane a reader route from need to unpaid time, work,
    # money, health, family strain, and public response.
    aging_care_readme = ROOT / "analysis/projects/us-aging-care-strain/README.md"
    memos.append(aging_care_readme)
    aging_care_synthesis = ROOT / "analysis/projects/us-aging-care-strain/aging-care-hidden-second-job-synthesis-v1.md"
    memos.append(aging_care_synthesis)
    # Publish the next material/time/care bridge as a reader-facing route:
    # stable work hours, care constraints, tenure, and following hardship,
    # with the small-cell and non-causal boundaries kept in the text.
    work_room_synthesis = ROOT / "analysis/projects/us-household-calendar-integration/work-stays-still-household-room-shrinks-synthesis-v1.md"
    memos.append(work_room_synthesis)
    # Publish the same-record SIPP three-way diagnostic so the review route
    # exposes the new joint-constraint screen and its no-variance boundary.
    sipp_three_way_diagnostic = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-care-mortgage-three-way-diagnostic-v1.md"
    memos.append(sipp_three_way_diagnostic)
    sipp_following_outcomes_bridge = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-care-following-outcomes-bridge-v1.md"
    memos.append(sipp_following_outcomes_bridge)
    sipp_time_loss_gate = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-time-loss-following-gate-v1.md"
    memos.append(sipp_time_loss_gate)
    # Publish the local buffer-transition field-timing gate so the broad
    # material/time/care route exposes the negative result and its acquisition
    # boundary instead of implying monthly credit or savings movement.
    sipp_buffer_following_gate = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-buffer-following-gate-v1.md"
    memos.append(sipp_buffer_following_gate)
    # Give the local-place lane a reader route from firm formation and stocks
    # through practical reachability, belonging, and political context.
    local_business_readme = ROOT / "analysis/projects/us-local-business-place/README.md"
    memos.append(local_business_readme)
    # Publish the local-place synthesis as a long-form reader route. It joins
    # firm formation, nominal service capacity, mobility, care designations,
    # modeled need, and the still-open meaning/politics arrows in one place.
    local_business_synthesis = ROOT / "analysis/projects/us-local-business-place/place-capacity-access-meaning-synthesis-v1.md"
    memos.append(local_business_synthesis)
    # Give the housing/insurance lane a reader route from hazard and payment
    # pressure through coverage, repair, mobility, and public response.
    housing_insurance_readme = ROOT / "analysis/projects/us-housing-insurance-risk/README.md"
    memos.append(housing_insurance_readme)
    # Publish the CBO federal-exposure layer alongside the broader
    # housing/insurance route; its national aggregates and model outputs are
    # intentionally kept distinct from household and property observations.
    cbo_insurance_layer = ROOT / "analysis/projects/us-housing-insurance-affordability/cbo-climate-insurance-federal-exposure-layer-v1.md"
    memos.append(cbo_insurance_layer)
    fhfa_price_layer = ROOT / "analysis/projects/us-housing-insurance-affordability/fhfa-price-protection-recovery-layer-v1.md"
    memos.append(fhfa_price_layer)
    # Publish the housing/insurance/energy route as a single reader synthesis
    # while keeping payment, coverage, hazard, energy, and mobility units apart.
    cost_staying_put_synthesis = ROOT / "analysis/projects/us-housing-insurance-risk/cost-of-staying-put-synthesis-v1.md"
    memos.append(cost_staying_put_synthesis)
    # Give the energy lane a reader route across bills, housing, assistance,
    # payment timing, household trade-offs, and safe-temperature outcomes.
    energy_burden_readme = ROOT / "analysis/projects/us-energy-household-burden/README.md"
    memos.append(energy_burden_readme)
    # Give the digital-attention lane a reader route from product incentives
    # through reach, use, trust, complaint, remedy, and exit.
    digital_attention_readme = ROOT / "analysis/projects/us-digital-habits-attention/README.md"
    memos.append(digital_attention_readme)
    # Publish a cross-source AI route that keeps population use, workplace
    # time, synthetic contact, product exit, and institutional inquiry as
    # separate evidence stages.
    ai_use_work_contact_exit = ROOT / "analysis/projects/us-digital-habits-attention/ai-use-work-contact-exit-synthesis-v1.md"
    memos.append(ai_use_work_contact_exit)
    imf_fas_access_audit = ROOT / "analysis/projects/us-financial-intermediation/imf-fas-provider-side-access-audit-2026-09-15.md"
    memos.append(imf_fas_access_audit)
    fdic_access_layer = ROOT / "analysis/projects/us-financial-intermediation/fdic-access-credit-alternative-routes-layer-v1.md"
    memos.append(fdic_access_layer)
    pew_state_fiscal_layer = ROOT / "analysis/projects/us-fiscal-news-household/pew-state-fiscal-buffer-service-capacity-layer-v1.md"
    memos.append(pew_state_fiscal_layer)
    financial_route_synthesis = ROOT / "analysis/projects/us-financial-intermediation/financial-access-route-recourse-public-capacity-synthesis-v1.md"
    memos.append(financial_route_synthesis)
    nydfs_insurance_layer = ROOT / "analysis/projects/us-housing-insurance-risk/new-york-dfs-complaint-availability-layer-v1.md"
    memos.append(nydfs_insurance_layer)
    energy_star_layer = ROOT / "analysis/projects/us-energy-household-burden/energy-star-label-cost-adoption-realization-layer-v1.md"
    memos.append(energy_star_layer)
    cpsc_safety_layer = ROOT / "analysis/projects/us-marketplace-product-safety/cpsc-hazard-recall-remedy-layer-v1.md"
    memos.append(cpsc_safety_layer)
    cms_nhe_layer = ROOT / "analysis/projects/us-health-cost-household-choice/cms-national-health-expenditure-system-household-layer-v1.md"
    memos.append(cms_nhe_layer)
    cms_meps_synthesis = ROOT / "analysis/projects/us-health-cost-household-choice/cms-meps-household-health-cost-end-to-end-synthesis-v1.md"
    memos.append(cms_meps_synthesis)
    memos.append(ROOT / "analysis/projects/us-health-cost-household-choice/end-to-end-status-matrix-v1.md")
    memos.append(ROOT / "analysis/projects/us-health-cost-household-choice/uas-health-cost-legitimacy-acquisition-audit-v1.md")
    memos.append(ROOT / "analysis/projects/us-health-cost-household-choice/hrs-health-cost-trust-acquisition-audit-v1.md")
    memos.append(ROOT / "analysis/projects/us-health-cost-household-choice/meps-2025-release-boundary-audit-2026-09-15.md")
    memos.append(ROOT / "analysis/projects/us-health-cost-household-choice/meps-2024-prescription-episode-boundary-v1.md")
    cfpb_health_bridge = ROOT / "analysis/projects/us-health-cost-household-choice/cfpb-event-ledger-health-cost-bridge-v1.md"
    memos.append(cfpb_health_bridge)
    cfpb_medical_visibility = ROOT / "analysis/projects/us-health-cost-household-choice/cfpb-2025-medical-debt-visibility-v1.md"
    memos.append(cfpb_medical_visibility)
    meps_2024_gate = ROOT / "analysis/projects/us-health-cost-household-choice/meps-2024-full-year-acquisition-gate-v1.md"
    memos.append(meps_2024_gate)
    memos.append(ROOT / "analysis/projects/us-health-cost-household-choice/meps-event-field-availability-audit-v1.md")
    # Publish the financial-power layer as a long-form reader route. It
    # connects liquidity, payment rails, credit records, institutional terms,
    # and exit while keeping the same-household event gap explicit.
    credit_liquidity_layer = ROOT / "analysis/projects/us-financial-intermediation/credit-liquidity-records-power-layer-v1.md"
    memos.append(credit_liquidity_layer)
    # Publish the macro-to-household financial-capacity synthesis as a reader
    # route across BEA, Federal Reserve, OFR, IMF, FAS, Findex, SHED, and NY Fed.
    macro_financial_capacity = ROOT / "analysis/projects/us-financial-intermediation/macro-to-household-financial-capacity-synthesis-v1.md"
    memos.append(macro_financial_capacity)
    # Publish the OECD worker-consultation experiment as a reader-facing
    # bridge between written governance rules and observed feature-level
    # negotiation, while preserving its small-sample and expected-outcome
    # boundaries.
    oecd_worker_consultation = ROOT / "analysis/projects/ai-work-control/oecd-worker-consultation-experiment-source-record-v1.md"
    memos.append(oecd_worker_consultation)
    # Publish the current ATUS annual comparison source memo itself, not only
    # the downstream finding, so readers can inspect the 2025 vintage and
    # annual-sample boundary alongside the reported comparison.
    atus_annual_comparison = ROOT / "analysis/projects/us-household-calendar-integration/atus-time-care-annual-comparison-2024-2025-v1.md"
    memos.append(atus_annual_comparison)
    atus_eldercare_network = ROOT / "analysis/projects/us-aging-care-strain/atus-eldercare-network-time-capacity-synthesis-v1.md"
    memos.append(atus_eldercare_network)
    # Publish the O*NET/NBER acquisition gate so the task-taxonomy dependency
    # and its exact remaining semantic boundary are inspectable by readers.
    onet_metadata_gate = ROOT / "analysis/projects/ai-work-control/onet-release-metadata-gate-v1.md"
    memos.append(onet_metadata_gate)
    # Publish the source-method audit beside the O*NET gate so readers can
    # inspect what W35677 itself documents about its O*NET-derived hierarchy.
    nber_onet_method_audit = ROOT / "analysis/projects/ai-work-control/nber-w35677-paper-method-audit-2026-09-14.md"
    memos.append(nber_onet_method_audit)
    nber_index_acquisition = ROOT / "analysis/projects/ai-work-control/nber-w35677-index-acquisition-v1.md"
    memos.append(nber_index_acquisition)
    # Publish the tenure-conditioned SIPP transition layer as a reader-facing
    # evidence memo, keeping the full-file same-person transition and its
    # tenure boundary visible alongside the broader household-room route.
    sipp_utility_work_tenure = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-work-tenure-following-layer-v1.md"
    memos.append(sipp_utility_work_tenure)
    # Publish the compatible annual care-universe bridge beside the monthly
    # utility/tenure work transition, keeping the mixed-clock boundary explicit.
    sipp_utility_tenure_childcare = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-tenure-childcare-layer-v1.md"
    memos.append(sipp_utility_tenure_childcare)
    sipp_utility_option_stack = ROOT / "analysis/projects/us-household-calendar-integration/sipp-utility-tenure-care-work-option-stack-synthesis-v1.md"
    memos.append(sipp_utility_option_stack)
    # Publish the remaining atlas control records so the theme scope,
    # comparison safeguards, and extraction method are inspectable together.
    memos.append(ROOT / "analysis/US-BROAD-THEME-COVERAGE-MATRIX_V1.md")
    memos.append(ROOT / "analysis/US-BROAD-COUNTEREXAMPLE-REGISTER_V1.md")
    memos.append(ROOT / "analysis/US-BROAD-THEME-INVENTORY_V1.md")
    memos.append(ROOT / "analysis/US-BROAD-TREND-EXTRACTION-PROTOCOL_V1.md")
    output_names = {
        cultural_politics_readme: "us-cost-trust-politics-program.html",
        material_political_synthesis: "material-pressure-to-political-meaning-synthesis-v1.html",
        material_pressure_scale_synthesis: "material-pressure-scale-meaning-synthesis-v1.html",
        material_time_care_program: "material-time-care-program-v1.html",
        state_capacity_program: "state-capacity-geopolitical-program-v1.html",
        safety_net_readme: "us-safety-net-access-program.html",
        public_help_route_synthesis: "public-help-route-buffer-judgment-synthesis-v1.html",
        consumer_recourse_readme: "consumer-recourse-program.html",
        consumer_recourse_synthesis: "consumer-recourse-visibility-remedy-synthesis-v1.html",
        exit_observability_audit: "practical-exit-observability-audit-v1.html",
        practical_exit_synthesis: "practical-exit-cross-domain-synthesis-v1.html",
        exit_ledger_implementation: "practical-exit-ledger-implementation-v1.html",
        exit_platform_dry_run: "practical-exit-platform-ledger-dry-run-v1.html",
        ROOT / "analysis/projects/us-customer-automation-recourse/platform-remedy-field-availability-audit-v1.md": "platform-remedy-field-availability-audit-v1.html",
        exit_cfpb_dry_run: "cfpb-practical-exit-contract-dry-run-v1.html",
        capacity_dependence_audit: "capacity-dependence-realization-audit-v1.html",
        jassm_control_surface_audit: "jassm-subaward-control-surface-audit-v1.html",
        material_meaning_action_audit: "material-meaning-action-endpoint-audit-v1.html",
        ai_work_control_endpoint_audit: "ai-work-control-endpoint-audit-v1.html",
        named_workplace_system_stage_ledger: "named-workplace-system-stage-ledger-v1.html",
        broad_same_case_episode_availability_audit: "broad-same-case-episode-availability-audit-v1.html",
        broad_next_episode_selection: "broad-next-episode-selection-v1.html",
        household_finance_readme: "household-financial-pressure-program.html",
        household_pressure_synthesis: "financial-pressure-adaptation-recovery-synthesis-v1.html",
        aging_care_readme: "aging-care-strain-program.html",
        aging_care_synthesis: "aging-care-hidden-second-job-synthesis-v1.html",
        work_room_synthesis: "work-stays-still-household-room-shrinks-synthesis-v1.html",
        local_business_readme: "local-business-place-program.html",
        local_business_synthesis: "place-capacity-access-meaning-synthesis-v1.html",
        housing_insurance_readme: "housing-insurance-risk-program.html",
        cost_staying_put_synthesis: "cost-of-staying-put-synthesis-v1.html",
        energy_burden_readme: "energy-household-burden-program.html",
        digital_attention_readme: "digital-habits-attention-program.html",
        ai_use_work_contact_exit: "ai-use-work-contact-exit-synthesis-v1.html",
        nber_onet_method_audit: "nber-w35677-paper-method-audit-2026-09-14.html",
        nber_index_acquisition: "nber-w35677-index-acquisition-v1.html",
        sipp_utility_work_tenure: "sipp-utility-work-tenure-following-layer-v1.html",
        sipp_utility_tenure_childcare: "sipp-utility-tenure-childcare-layer-v1.html",
        sipp_buffer_following_gate: "sipp-utility-buffer-following-gate-v1.html",
        imf_fas_access_audit: "imf-fas-provider-side-access-audit-2026-09-15.html",
        credit_liquidity_layer: "credit-liquidity-financial-power-layer-v1.html",
        macro_financial_capacity: "macro-to-household-financial-capacity-synthesis-v1.html",
        oecd_worker_consultation: "oecd-worker-consultation-experiment-source-record-v1.html",
        atus_annual_comparison: "atus-time-care-annual-comparison-2024-2025-v1.html",
        review_guide: "review-guide.html",
        review_packet: "review-packet-ai-work-control.html",
        ai_work_synthesis: "anticipatory-to-remedial-worker-control-synthesis-v1.html",
        cfpb_health_bridge: "cfpb-event-ledger-health-cost-bridge-v1.html",
        cfpb_medical_visibility: "cfpb-2025-medical-debt-visibility-v1.html",
    }
    published_outputs = {path.resolve(): name for path, name in output_names.items()}
    for memo in sorted(memos):
        page = ROOT / "site" / output_names.get(memo, f"{memo.stem}.html")
        checked += 1
        if should_rebuild(memo, page):
            page.write_text(render(memo, published_outputs))
            rebuilt += 1
            print(f"BUILT {page.relative_to(ROOT)}")
    print(f"Checked {checked} finding pages; rebuilt {rebuilt}.")


if __name__ == "__main__":
    main()
