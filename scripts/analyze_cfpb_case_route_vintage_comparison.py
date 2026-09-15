#!/usr/bin/env python3
"""Compare CFPB case-route fields across 2024 and 2025 API vintages."""
from __future__ import annotations

import hashlib, json, ssl
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/'
OUT = Path('analysis/records/us-cfpb-case-route-vintage-comparison-2024-2025.json')
PRODUCTS = ['Checking or savings account', 'Credit reporting or other personal consumer reports', 'Mortgage', 'Student loan']

def dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00')) if value else None

def fetch(year, product, size=500):
    query = {'date_received_min': f'{year}-01-01', 'date_received_max': f'{year+1}-01-01', 'product': product, 'size': str(size)}
    request = Request(BASE + '?' + urlencode(query), headers={'Accept':'application/json','User-Agent':'cultural-geopolitical-theme-mining/1.0'})
    with urlopen(request, timeout=120, context=ssl.create_default_context()) as response:
        raw = response.read()
    return json.loads(raw), hashlib.sha256(raw).hexdigest(), query

def share(counter, total, key):
    return round(100 * counter.get(key, 0) / total, 4) if total else None

def summarize(payload, raw_hash, query):
    rows = [hit.get('_source', {}) for hit in payload.get('hits', {}).get('hits', [])]
    lags = []
    field_presence = Counter()
    response = Counter()
    timely = Counter()
    public = Counter()
    web = Counter()
    for row in rows:
        for field in ('has_narrative','company_public_response','company_response','timely','date_received','date_sent_to_company'):
            if field in row:
                field_presence[field] += 1
        response[row.get('company_response') or 'Missing'] += 1
        timely[row.get('timely') or 'Missing'] += 1
        public['present' if row.get('company_public_response') else 'absent'] += 1
        web['present' if row.get('submitted_via') == 'Web' else 'other'] += 1
        received, sent = dt(row.get('date_received')), dt(row.get('date_sent_to_company'))
        if received and sent:
            lags.append((sent-received).total_seconds()/3600)
    lags.sort()
    total = len(rows)
    raw_measures = {
        'receipt_to_company_send_median_hours': lags[len(lags)//2] if lags else None,
        'receipt_to_company_send_p90_hours': lags[int(.9*(len(lags)-1))] if lags else None,
        'receipt_to_company_send_over_24_hours': 100*sum(x > 24 for x in lags)/len(lags) if lags else None,
        'same_calendar_day_routing': 100*sum(x < 24 for x in lags)/len(lags) if lags else None,
        'timely_yes': share(timely,total,'Yes'),
        'web_submission': share(web,total,'present'),
        'company_public_response_present': share(public,total,'present'),
        'closed_with_explanation': share(response,total,'Closed with explanation'),
        'closed_with_monetary_relief': share(response,total,'Closed with monetary relief'),
        'closed_with_non_monetary_relief': share(response,total,'Closed with non-monetary relief'),
        'has_narrative_field_present_in_payload': 100*field_presence['has_narrative']/total if total else None,
    }
    units = {
        'receipt_to_company_send_median_hours': 'hours',
        'receipt_to_company_send_p90_hours': 'hours',
        'receipt_to_company_send_over_24_hours': 'percent of sampled records',
        'same_calendar_day_routing': 'percent of sampled records',
        'timely_yes': 'percent of sampled records',
        'web_submission': 'percent of sampled records',
        'company_public_response_present': 'percent of sampled records',
        'closed_with_explanation': 'percent of sampled records',
        'closed_with_monetary_relief': 'percent of sampled records',
        'closed_with_non_monetary_relief': 'percent of sampled records',
        'has_narrative_field_present_in_payload': 'percent of sampled records with field present',
    }
    measures = {name: {'value': value, 'unit': units[name], 'value_type': 'estimate' if 'hours' in name else 'share'} for name, value in raw_measures.items()}
    return {
        'period': query['date_received_min'][:4],
        'product': query['product'],
        'denominator': {'value': total, 'unit': 'capped retrieval-order sample of published CFPB complaint records', 'value_type': 'unweighted_case_count'},
        'total_matching_records': payload.get('hits',{}).get('total',{}),
        'measures': measures,
        'field_presence': dict(field_presence),
        'method': 'Official CFPB complaint API; exact product filter, date_received window, and size=500 retrieval-order sample. Routing lag is date_sent_to_company minus date_received.',
        'uncertainty': 'Capped retrieval-order sample; no sampling standard error, complaint incidence rate, account denominator, or population weighting. Field presence is an API-schema diagnostic, not a narrative prevalence estimate.',
        'subgroup': product,
        'counterinterpretation': 'Company response and timely fields are administrative labels; routing lag is not company resolution or verified remedy. Product mix, complaint propensity, publication rules, API indexing, and field-vintage changes can produce the contrast.',
        'source_url': 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/',
        'retrieval_hash': 'sha256:' + raw_hash,
        'status': 'compared',
    }

observations = []
for year in (2024, 2025):
    for product in PRODUCTS:
        payload, raw_hash, query = fetch(year, product)
        observations.append(summarize(payload, raw_hash, query))

record = {
    'format':'us-trend-observation-record-v1',
    'trend_id':'us-cfpb-case-route-vintage-comparison-2024-2025',
    'title':'CFPB case-route labels and API fields change across complaint vintages',
    'theme_ids':['cost','time','voice','work'],
    'program_theme_ids':['consumer_power_recourse','public_systems_feedback','firm_sector_market_power','time_hidden_price','trust_identity_meaning'],
    'source_unit':'Capped retrieval-order sample of published CFPB complaint records with case-level route fields',
    'geography':'United States complaint records; consumer state and ZIP are reported fields',
    'observations':observations,
    'related_sources':[{'source_url':'https://cfpb.github.io/api/ccdb/fields.html','claim':'Official CFPB field reference defines the public complaint fields and their labels.','status':'official-definition'},{'source_url':'https://www.consumerfinance.gov/data-research/consumer-complaints/','claim':'Official CFPB complaint database describes the published complaint system and its limitations.','status':'official-source'}],
    'boundary':'This is an API-vintage and route-field comparison, not a consumer-harm, remedy, or service-quality estimate. The 2025 response omits has_narrative in the returned sample, so it cannot be compared with 2024 narrative prevalence. Timely is not substituted for elapsed routing time, and routing is not remedy.',
    'retrieval_hash':'derived from per-observation raw API hashes',
}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'output':str(OUT),'observations':len(observations)},indent=2))
