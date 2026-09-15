#!/usr/bin/env python3
"""Measure bounded supplier concentration in the committed JASSM/LRASM subaward extract."""
import collections, hashlib, json, re
from pathlib import Path

INPUT = Path('analysis/projects/ai-work-control/data/usaspending-jassm-lrasm-subawards-2026-09-13.json')
OUT = Path('analysis/records/usaspending-jassm-lrasm-supplier-concentration-2024-2025.json')

source = json.loads(INPUT.read_text())
rows = source['response']['results']
amounts = collections.defaultdict(float)
counts = collections.Counter()
for row in rows:
    name = row.get('recipient_name') or 'Missing recipient'
    amounts[name] += float(row.get('amount') or 0)
    counts[name] += 1
total = sum(amounts.values())
ranked = sorted(((value / total, name, value, counts[name]) for name, value in amounts.items()), reverse=True)
hhi = sum(share * share for share, *_ in ranked)
repeat_recipients = sum(count > 1 for count in counts.values())
top5 = sum(item[0] for item in ranked[:5])
top10 = sum(item[0] for item in ranked[:10])

terms = ['TRANSCEIVER','MICROCIRCUIT','PRINTED WIRING','BEARING','ENGINE','ANTENNA','WING','TAIL','WARHEAD','FUZ','POWER','CONNECTOR','OPTIC','PROCESSOR','COVER','HOSE']
term_counts = collections.Counter()
for row in rows:
    description = re.sub(r'[^A-Z0-9 ]', ' ', (row.get('description') or '').upper())
    for term in terms:
        if term in description:
            term_counts[term] += 1

hash_value = source.get('response_sha256') or hashlib.sha256(INPUT.read_bytes()).hexdigest()
method = 'Official USAspending committed subaward response for one JASSM/LRASM parent award; recipient amounts are summed by reported recipient name; concentration is computed on returned-record reported amounts.'
uncertainty = 'Single parent award and one returned page; recipient names are not reconciled to legal-entity or parent ownership; subaward visibility, amendments, subordinate tiers, locations, and production are incomplete. HHI and top-recipient shares describe this extract, not a defense-industrial market.'
boundary = 'Supplier-name breadth is not replaceability, competition, production capacity, delivery, or geopolitical leverage. Reported component descriptions are not a bill of materials, output count, or proof of integration.'

obs = [
    {
        'period':'2024-10-23 through 2025-02-28; supplier concentration in returned subaward records',
        'denominator':{'value':len(rows),'unit':'returned USAspending subaward records linked to one parent award','value_type':'unweighted_record_count'},
        'measures':{
            'reported_subaward_amount':{'value':round(total,2),'unit':'nominal US dollars in returned records','value_type':'reported'},
            'distinct_reported_recipients':{'value':len(amounts),'unit':'recipient names','value_type':'count'},
            'top_5_recipient_share':{'value':round(top5*100,4),'unit':'percent of returned-record amount','value_type':'share'},
            'top_10_recipient_share':{'value':round(top10*100,4),'unit':'percent of returned-record amount','value_type':'share'},
            'recipient_amount_hhi':{'value':round(hhi,6),'unit':'sum of squared recipient amount shares in returned extract','value_type':'derived_concentration_index'},
            'repeat_recipient_count':{'value':repeat_recipients,'unit':'recipient names appearing in more than one returned record','value_type':'count'},
        },
        'method':method,'uncertainty':uncertainty,'subgroup':'Reported recipient names ranked by summed amount','counterinterpretation':boundary,'source_url':'https://api.usaspending.gov/api/v2/subawards/','retrieval_hash':'sha256:'+hash_value,'status':'inferred'
    },
    {
        'period':'2024-10-23 through 2025-02-28; description-visible component terms',
        'denominator':{'value':len(rows),'unit':'returned USAspending subaward records','value_type':'unweighted_record_count'},
        'measures':{
            'records_with_component_description':{'value':sum(bool(row.get('description')) for row in rows),'unit':'records with nonblank description','value_type':'count'},
            'description_term_counts':{'value':dict(term_counts),'unit':'records containing coded text terms; overlapping terms allowed','value_type':'qualitative_text_count'},
        },
        'method':'Case-insensitive presence coding of selected terms in returned free-text subaward descriptions; terms are overlapping examples, not a component taxonomy.',
        'uncertainty':uncertainty,'subgroup':'Description-visible component and assembly terms','counterinterpretation':boundary,'source_url':'https://api.usaspending.gov/api/v2/subawards/','retrieval_hash':'sha256:'+hash_value,'status':'inferred'
    }
]
record = {'format':'us-trend-observation-record-v1','trend_id':'usaspending-jassm-lrasm-supplier-concentration-2024-2025','title':'A broad supplier-name surface can remain financially concentrated','theme_ids':['cost','work','voice'],'program_theme_ids':['firm_sector_market_power','infrastructure_technology_dependency','work_control_bargaining','geopolitical_state_consequences'],'source_unit':'USAspending subaward records linked to one DoD JASSM/LRASM parent contract','geography':'United States parent award; subordinate recipient locations are not supplied in this extract','observations':obs,'related_sources':[{'source_url':'https://api.usaspending.gov/docs/endpoints','claim':'USAspending documents the subaward endpoint and returned award fields.','status':'official-method'}],'boundary':boundary,'retrieval_hash':'sha256:'+hashlib.sha256(INPUT.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'output':str(OUT),'records':len(rows),'recipients':len(amounts),'top5_share':round(top5*100,4),'top10_share':round(top10*100,4),'hhi':round(hhi,6)},indent=2))
