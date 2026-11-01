#!/usr/bin/env python3
"""Acquire and summarize ORA mobile-repair outcomes without publishing raw rows."""

from __future__ import annotations

import collections
import csv
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis" / "external-trend-intelligence"
OUTPUT = ANALYSIS / "open-repair-alliance-mobile-snapshot.json"
URL = "https://openrepair.org/wp-content/uploads/2026/10/OpenRepairData_v0.3_aggregate_202607.zip"


def main() -> int:
    data = urllib.request.urlopen(URL, timeout=120).read()
    digest = "sha256:" + hashlib.sha256(data).hexdigest()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        csv_name = next(name for name in archive.namelist() if name.endswith("_eee.csv"))
        rows = [row for row in csv.DictReader(io.TextIOWrapper(archive.open(csv_name), encoding="utf-8")) if row.get("product_category") == "Mobile"]
        schema = json.loads(archive.read("tableschema.json"))

    def summarize(subset: list[dict[str, str]]) -> dict:
        statuses = collections.Counter(row.get("repair_status") or "Missing" for row in subset)
        barriers = collections.Counter(row.get("repair_barrier_if_end_of_life") or "Missing" for row in subset)
        years = collections.Counter((row.get("event_date") or "")[:4] or "Missing" for row in subset)
        ages = [int(row["product_age"]) for row in subset if row.get("product_age", "").isdigit()]
        return {
            "record_count": len(subset),
            "status_counts": dict(sorted(statuses.items())),
            "status_percentages": {key: round(value * 100 / len(subset), 2) for key, value in sorted(statuses.items())} if subset else {},
            "barrier_counts_top": barriers.most_common(12),
            "event_year_counts": dict(sorted(years.items())),
            "product_age_observed_count": len(ages),
            "product_age_median_years": sorted(ages)[len(ages) // 2] if ages else None,
            "missingness": {field: sum(not row.get(field) for row in subset) for field in ("country", "event_date", "repair_status", "product_age", "brand", "repair_barrier_if_end_of_life")},
        }

    us_rows = [row for row in rows if row.get("country") == "USA"]
    country_counts = collections.Counter(row.get("country") for row in rows)
    payload = {
        "schema": "external-trend-intelligence.open-repair-alliance-mobile-snapshot.v1",
        "acquisition_id": "ora-ords-v03-mobile-aggregate-202607",
        "status": "acquired_phone_specific_global_community_repair_proxy_not_policy_outcome",
        "retrieved_at": "2026-10-31",
        "source": {
            "publisher": "Open Repair Alliance",
            "dataset": "Open Repair Data Standard v0.3 aggregate EEE file",
            "download_page": "https://openrepair.org/open-data/downloads/",
            "download_url": URL,
            "schema_url": "https://standard.openrepair.org/",
            "license": "CC BY-SA 4.0",
            "artifact_sha256": digest,
            "raw_member": csv_name,
            "archive_member_count": len(schema.get("resources", [])) if isinstance(schema, dict) else None,
            "reported_release_scope": "Data updated October 2026, including records through July 2026.",
        },
        "filter": {
            "field": "product_category",
            "value": "Mobile",
            "interpretation": "ORA's mobile category is the closest available phone-specific category; retain partner_product_category for any future row-level analysis.",
        },
        "coverage": {
            "mobile_record_count": len(rows),
            "country_count": len(country_counts),
            "countries_top": country_counts.most_common(15),
            "us_mobile_record_count": len(us_rows),
            "global_event_years": sorted({(row.get("event_date") or "")[:4] for row in rows}),
        },
        "global_mobile": summarize(rows),
        "us_mobile": summarize(us_rows),
        "units": {
            "record": "one logged repair attempt/item observed at a participating community repair event",
            "repair_status": "ORA categorical outcome (Fixed, Repairable, End of life, Unknown)",
            "product_age": "years where supplied by the data provider",
            "event_date": "date of logged repair event",
        },
        "uncertainty": "This is a convenience/community-event sample, not a probability sample or census of repair transactions. Missing product age and barrier fields are preserved in counts; no sampling variance is supplied.",
        "interpretation_boundary": "The artifact measures observed mobile items brought to participating repair events. It does not estimate US population repair demand, policy exposure, prices, waiting time, replacement decisions, or device-life effects.",
        "counter_signal": "High observed fix rates may reflect self-selection of repairable items, volunteer expertise, event access, partner composition, and country mix; low end-of-life counts cannot be interpreted as low replacement or disposal.",
        "pooling_decision": "do_not_pool_with_census_industry_proxies_state_policy_or_global_ewaste",
        "falsifier": "A later ORA release, or a verified US transaction/consumer panel, shows materially different mobile repair direction or timing from this community-event proxy.",
        "next_action": "Screen USA rows and event dates against New York and Colorado policy effective dates only as descriptive context; acquire a representative US transaction or consumer outcome before any policy or company claim.",
        "rights_basis": "ORA publishes the aggregate dataset under CC BY-SA 4.0; retain attribution and share-alike notices, the exact archive checksum, and field-level transformation notes.",
        "boundary": "This is the first acquired phone-specific outcome proxy in the observatory, but it remains an external descriptive community-repair signal and does not qualify a policy effect.",
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} mobile rows; {len(us_rows)} USA rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
