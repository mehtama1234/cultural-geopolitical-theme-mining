"""Validate the connected US reading atlas and its generated editions."""
import json
import re
from html import escape
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "manifests/us-theme-connections.json").read_text())
md = (ROOT / "analysis/us-theme-atlas.md").read_text()
html = (ROOT / "site/us-theme-atlas.html").read_text()

nodes = {item["id"]: item for item in manifest["nodes"]}
themes = {item["id"]: item for item in manifest["themes"]}
assert len(nodes) == len(manifest["nodes"]), "duplicate topic id"
assert len(themes) == len(manifest["themes"]), "duplicate theme id"
assert nodes and themes

for node in nodes.values():
    assert node["theme"] in themes
    assert (ROOT / node["source_record"]).is_file()
    assert node["title"] in md and node["title"] in html
    check = node.get("evidence_check")
    if check:
        assert check["source"].startswith("https://")
        assert check["title"] in md and escape(check["title"]) in html

edges = manifest["edges"]
edge_pairs = set()
for edge in edges:
    assert edge["from"] in nodes and edge["to"] in nodes
    assert edge["type"] in {"open", "comparison"}
    assert edge["relation"] and edge["limit"]
    assert edge["id"] not in edge_pairs
    edge_pairs.add(edge["id"])

for path in manifest.get("reading_paths", []):
    topics = path["topics"]
    assert len(topics) >= 2
    assert all(topic in nodes for topic in topics)
    pairs = {frozenset((edge["from"], edge["to"])) for edge in edges}
    assert all(frozenset(pair) in pairs for pair in zip(topics, topics[1:]))
    assert path["title"] in md and path["title"] in html

ids = re.findall(r'\bid="([^"]+)"', html)
assert not [key for key, count in Counter(ids).items() if count > 1], "duplicate HTML id"
assert "<a id=" not in md, "raw anchor artifact in Markdown"
assert f"{len(nodes)} of {len(nodes)} topics shown" in html
print(
    f"VALID atlas: {len(nodes)} topics, {len(themes)} themes, "
    f"{len(edges)} connections, {len(manifest.get('reading_paths', []))} paths"
)
