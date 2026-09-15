#!/usr/bin/env python3
"""Fetch and persist a public DLA CAGE detail record by CAGE code."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from datetime import datetime, timezone
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.parse import quote, urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener

BASE_URL = "https://cage.dla.mil"


def text_field(page: str, label: str) -> str | None:
    pattern = rf"(?:<label>{re.escape(label)}</label>\s*<span>|<td class=\"detail-left-col\">\s*{re.escape(label)}\s*</td>\s*<td class=\"detail-right-col(?:-address)?\">)(.*?)(?:</span>|</td>)"
    match = re.search(pattern, page, flags=re.I | re.S)
    if not match:
        return None
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<.*?>", "", match.group(1)))).strip() or None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cage", required=True, help="Five-character CAGE code")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(jar))
    agreement_request = Request(f"{BASE_URL}/Home/UsageAgree", headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    agreement_page = opener.open(agreement_request, timeout=60).read().decode("utf-8", errors="replace")
    token_match = re.search(r'name="__RequestVerificationToken"[^>]+value="([^"]+)"', agreement_page, flags=re.I)
    if token_match:
        agreement_data = urlencode({"__RequestVerificationToken": token_match.group(1), "returningURL": ""}).encode("utf-8")
        opener.open(Request(f"{BASE_URL}/Home/UsageAgree", data=agreement_data, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0", "Content-Type": "application/x-www-form-urlencoded"}, method="POST"), timeout=60).read()
    search_url = f"{BASE_URL}/Search/Results?page=1&q={quote(args.cage)}"
    search_request = Request(search_url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    search_page = opener.open(search_request, timeout=60).read().decode("utf-8", errors="replace")
    detail_match = re.search(rf"/Search/Details\?id=(\d+)[^>]*>Details", search_page, flags=re.I)
    if not detail_match:
        raise SystemExit(f"No DLA CAGE detail link found for {args.cage}")
    detail_url = f"{BASE_URL}/Search/Details?id={detail_match.group(1)}"
    detail_request = Request(detail_url, headers={"User-Agent": "cultural-geopolitical-theme-mining/1.0"})
    raw = opener.open(detail_request, timeout=60).read()
    page = raw.decode("utf-8", errors="replace")
    address_match = re.search(r"<td class=\"detail-right-col-address\">(.*?)</td>", page, flags=re.I | re.S)
    address = None
    if address_match:
        address = re.sub(r"\s+", " ", html.unescape(re.sub(r"<.*?>", " ", address_match.group(1)))).strip()
    parent_match = re.search(r"<label>CAGE</label><span><a href=\"[^\"]+\">([^<]+)</a></span>\s*</div>\s*<div><label>Company Name</label><span>([^<]+)", page, flags=re.I | re.S)
    output = {
        "format": "dla-cage-detail-v1",
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "search_endpoint": search_url,
        "detail_endpoint": detail_url,
        "cage_query": args.cage,
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "record": {
            "legal_business_name": text_field(page, "Legal Business Name"),
            "address": address,
            "cage": text_field(page, "CAGE"),
            "uei": text_field(page, "UEI"),
            "status": text_field(page, "Status"),
            "cage_update_date": text_field(page, "CAGE Update Date"),
            "cage_expiration": text_field(page, "CAGE Expiration"),
            "parent_cage": parent_match.group(1).strip() if parent_match else None,
            "parent_company_name": parent_match.group(2).strip() if parent_match else None,
        },
        "boundary": "Public DLA CAGE detail record for one CAGE identifier; it establishes the displayed entity identity, address, status, UEI, and linked parent fields at retrieval time, not the location of every subaward action, ownership rights beyond displayed relationships, workforce, production, delivery, or local incidence.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "response_sha256": output["response_sha256"], "record": output["record"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
