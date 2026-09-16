#!/usr/bin/env python3
"""Stage a privacy-minimized MEPS event ledger for the household-cascade design.

The output is a local JSONL research-design staging file, not a promoted
finding. It keeps a keyed hash instead of DUPERSID, one first event per person
and event family, month precision, payment and round context, and explicit
unknowns for care choice, institutional response, remedy, and recovery.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd
import pyreadstat


EVENTS = {
    "office": ("EVNTIDX", "OBDATEYR", "OBDATEMM", "OBSF24X"),
    "emergency_room": ("EVNTIDX", "ERDATEYR", "ERDATEMM", "ERFSF24X"),
    "inpatient": ("EVNTIDX", "IPBEGYR", "IPBEGMM", "IPFSF24X"),
}
PERSON_FIELDS = [
    "DUPERSID", "PANEL", "PERWT24F", "INSURC24", "POVCAT24", "EMPST53",
    "RTHLTH53", "PROBPY42", "DLAYCA42", "MEDDEBT42", "FWDEBT42", "EQDENY53",
]


def read(path: Path, columns: list[str]) -> pd.DataFrame:
    frame, _ = pyreadstat.read_dta(path, usecols=columns)
    return frame


def person_key(frame: pd.DataFrame) -> pd.Series:
    return frame["DUPERSID"].astype(str) + "|" + frame["PANEL"].round().astype(int).astype(str)


def clean(value: object) -> str:
    if pd.isna(value):
        return "unknown"
    return str(value)


def hash_key(value: str, salt: str) -> str:
    return hashlib.sha256((salt + "|" + value).encode("utf-8")).hexdigest()[:24]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hc256_file", type=Path)
    parser.add_argument("--office-file", type=Path, required=True)
    parser.add_argument("--emergency-room-file", type=Path, required=True)
    parser.add_argument("--inpatient-file", type=Path, required=True)
    parser.add_argument("--output-jsonl", type=Path, required=True)
    parser.add_argument("--audit-output", type=Path, required=True)
    parser.add_argument("--salt", required=True, help="ephemeral linkage salt; never commit it")
    args = parser.parse_args()

    person = read(args.hc256_file, PERSON_FIELDS)
    person = person.loc[pd.to_numeric(person["PERWT24F"], errors="coerce").gt(0)].copy()
    person["PERSON_KEY"] = person_key(person)
    person_lookup = person.set_index("PERSON_KEY")
    source_paths = {
        "office": args.office_file,
        "emergency_room": args.emergency_room_file,
        "inpatient": args.inpatient_file,
    }
    rows: list[dict[str, object]] = []
    family_counts: dict[str, int] = {}

    for family, path in source_paths.items():
        event_id, year_field, month_field, payment_field = EVENTS[family]
        event = read(path, ["DUPERSID", "PANEL", event_id, year_field, month_field, payment_field])
        event["PERSON_KEY"] = person_key(event)
        event["YEAR"] = pd.to_numeric(event[year_field], errors="coerce")
        event["MONTH"] = pd.to_numeric(event[month_field], errors="coerce")
        event["PAYMENT"] = pd.to_numeric(event[payment_field], errors="coerce")
        valid = (
            event["YEAR"].between(1900, 2024)
            & event["MONTH"].between(1, 12)
            & event["PAYMENT"].notna()
            & event["PERSON_KEY"].isin(person_lookup.index)
        )
        first = event.loc[valid].sort_values(["PERSON_KEY", "YEAR", "MONTH", event_id]).drop_duplicates("PERSON_KEY")
        family_counts[family] = int(len(first))
        for record in first.itertuples(index=False):
            context = person_lookup.loc[record.PERSON_KEY]
            stable_key = hash_key(str(record.PERSON_KEY), args.salt)
            event_date = f"{int(record.YEAR):04d}-{int(record.MONTH):02d}-01"
            source = f"MEPS 2024 {family} event file + HC-256 person file"
            rows.append({
                "episode_id": f"MEPS24-{family}-{stable_key}",
                "unit": "person",
                "event_date": event_date,
                "geography": "not included in staged local ledger",
                "trigger": f"first observed {family} event; underlying need is not identified",
                "practical_room_and_alternatives": (
                    f"self/family payment={clean(record.PAYMENT)}; insurance code={clean(context.INSURC24)}; "
                    f"poverty category={clean(context.POVCAT24)}; alternatives not observed"
                ),
                "choice_and_tradeoff": (
                    f"reported round cost-related-care-delay code={clean(context.DLAYCA42)}; "
                    "event-specific care choice and household trade-off are not identified"
                ),
                "institutional_route": (
                    f"reported round denial/prior-authorization code={clean(context.EQDENY53)}; "
                    "provider/insurer response, appeal, and authority are not identified"
                ),
                "remedy_verification": "verified correction, payment arrangement, coverage restoration, or no remedy is unknown",
                "followup_outcomes": (
                    f"round context: employment={clean(context.EMPST53)}, perceived health={clean(context.RTHLTH53)}, "
                    f"medical bill problem={clean(context.PROBPY42)}, medical debt={clean(context.MEDDEBT42)}, "
                    f"collector contact={clean(context.FWDEBT42)}; not event-specific recovery"
                ),
                "meaning_and_action": "trust, attribution, civic action, switching, and exit are not observed",
                "denominator": "positive-weight persons with one valid first event in this event-family file; not a population estimate",
                "date_precision": "month; day unavailable in the public-use event file",
                "missingness": "trigger severity, alternatives, care choice, household payer, remedy, and meaning/action are missing",
                "counterexample": "compare with another valid first-event person in the same family; no matched counterexample is constructed here",
                "source_and_uncertainty": f"exact DUPERSID+PANEL join before keyed-hash removal; {source}; weighted context not estimated in this row-level stage",
                "evidence_status": "observed",
                "stages": {
                    "trigger": {"status": "observed", "observation": f"first dated {family} event", "source": source},
                    "practical_room_and_alternatives": {"status": "observed", "observation": f"payment={clean(record.PAYMENT)} and round context; alternatives unknown", "source": source},
                    "choice_and_tradeoff": {"status": "reported", "observation": f"round care-delay code={clean(context.DLAYCA42)}; event-specific choice unknown", "source": source},
                    "institutional_route": {"status": "reported", "observation": f"round denial/prior-authorization code={clean(context.EQDENY53)}; response unknown", "source": source},
                    "remedy_verification": {"status": "unknown", "observation": "not measured", "source": source},
                    "followup_outcomes": {"status": "reported", "observation": f"round bill={clean(context.PROBPY42)}, debt={clean(context.MEDDEBT42)}, collector={clean(context.FWDEBT42)}; not event-specific recovery", "source": source},
                    "meaning_and_action": {"status": "unknown", "observation": "not measured", "source": source},
                },
            })

    args.output_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with args.output_jsonl.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    digest = hashlib.sha256(args.output_jsonl.read_bytes()).hexdigest()
    audit = {
        "schema": "us-household-constraint-cascade-ledger-v1",
        "status": "local_staging_only",
        "rows": len(rows),
        "family_counts": family_counts,
        "output_sha256": digest,
        "privacy": "DUPERSID is not written; episode IDs are keyed hashes using an ephemeral caller-supplied salt",
        "limitations": "This staging file does not observe the original need, care choice, alternatives, household trade-off, institutional response, verified remedy, trust, action, or recovery for the event.",
        "source_files": {name: str(path) for name, path in source_paths.items()},
    }
    args.audit_output.parent.mkdir(parents=True, exist_ok=True)
    args.audit_output.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
