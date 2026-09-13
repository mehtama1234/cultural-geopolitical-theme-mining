#!/usr/bin/env python3
"""Join CFPB product complaint visibility to CBP finance-sector state context."""

from __future__ import annotations

import argparse
import csv
import io
import json
import zipfile
from pathlib import Path


FIPS = {
    "01":"AL","02":"AK","04":"AZ","05":"AR","06":"CA","08":"CO","09":"CT","10":"DE","11":"DC",
    "12":"FL","13":"GA","15":"HI","16":"ID","17":"IL","18":"IN","19":"IA","20":"KS","21":"KY",
    "22":"LA","23":"ME","24":"MD","25":"MA","26":"MI","27":"MN","28":"MS","29":"MO","30":"MT",
    "31":"NE","32":"NV","33":"NH","34":"NJ","35":"NM","36":"NY","37":"NC","38":"ND","39":"OH",
    "40":"OK","41":"OR","42":"PA","44":"RI","45":"SC","46":"SD","47":"TN","48":"TX","49":"UT",
    "50":"VT","51":"VA","53":"WA","54":"WV","55":"WI","56":"WY",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cbp-state", type=Path, required=True)
    parser.add_argument("--population", type=Path, required=True)
    parser.add_argument("--complaints", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    population = {}
    import openpyxl
    ws = openpyxl.load_workbook(args.population, data_only=True, read_only=True).active
    names = {"Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","District of Columbia":"DC","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"}
    for row in ws.iter_rows(min_row=9, values_only=True):
        if isinstance(row[0], str) and row[0].startswith(".") and row[0][1:] in names:
            population[names[row[0][1:]]] = int(row[6])

    finance = {}
    with zipfile.ZipFile(args.cbp_state) as archive:
        member = next(name for name in archive.namelist() if name.endswith(".txt"))
        with archive.open(member) as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8"))
            for row in reader:
                if row.get("naics") != "52----" or row.get("lfo") != "-":
                    continue
                state = FIPS.get(row.get("fipstate", ""))
                if state in population:
                    finance[state] = {"establishments": int(row["est"]), "employees": int(row["emp"])}

    complaints = json.loads(args.complaints.read_text(encoding="utf-8"))["products"]
    states = {}
    for state, pop in population.items():
        if state not in finance:
            continue
        item = {"population": pop, **finance[state]}
        item["finance_establishments_per_100k"] = 100_000 * item["establishments"] / pop
        item["finance_employees_per_100k"] = 100_000 * item["employees"] / pop
        item["complaints"] = {
            product: data["states"].get(state)
            for product, data in complaints.items()
            if state in data["states"]
        }
        states[state] = item

    output = {
        "format": "us-cfpb-cbp-finance-state-context-v1",
        "cbp_year": 2023,
        "complaint_year": 2024,
        "states": states,
        "boundary": "CBP finance-sector presence and CFPB published complaint visibility are different, time-misaligned context measures; no causal or harm-rate estimate.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
