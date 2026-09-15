#!/usr/bin/env python3
"""Build a bounded historical GSS financial-satisfaction/trust comparison."""
import argparse, hashlib, json
from pathlib import Path
import pandas as pd

YEARS = [1972, 1980, 1990, 2000, 2010, 2014, 2018, 2022, 2024]

def share(frame, field, condition, target):
    x = frame[frame[field].notna() & condition].copy()
    return {'value': round(float(((x[field] == target) * x.wtssps).sum() / x.wtssps.sum() * 100),4), 'unit':'percent of valid weighted respondents', 'value_type':'weighted_share', 'unweighted_n':int(len(x)), 'weighted_denominator':round(float(x.wtssps.sum()),2)}

def proportion(frame, field, target):
    return share(frame, field, frame[field].notna(), target)

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=Path, required=True)
parser.add_argument('--archive', type=Path, required=True)
parser.add_argument('--hash-file', type=Path)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
hash_file = args.hash_file or args.data
d = pd.read_pickle(args.data) if args.data.suffix == '.pkl' else pd.read_stata(args.data, columns=['year','satfin','trust','fair','wtssps'], convert_categoricals=False)
d = d[d.wtssps.notna() & (d.wtssps > 0)].copy()
observations=[]
for year in YEARS:
    frame=d[(d.year==year) & d.satfin.isin([1,2,3])].copy()
    measures={
      'not_satisfied_at_all': proportion(frame,'satfin',3),
      'trust_most_people_among_not_satisfied': share(frame,'trust',(frame.satfin==3) & frame.trust.notna(),1),
      'trust_most_people_among_pretty_well_satisfied': share(frame,'trust',(frame.satfin==1) & frame.trust.notna(),1),
      'people_try_to_be_fair_among_not_satisfied': share(frame,'fair',(frame.satfin==3) & frame.fair.notna(),2),
      'people_try_to_be_fair_among_pretty_well_satisfied': share(frame,'fair',(frame.satfin==1) & frame.fair.notna(),2)}
    observations.append({'period':str(year),'denominator':{'value':int(len(frame)),'unit':'GSS respondents with valid financial-satisfaction category and positive WTSSPS','value_type':'unweighted_respondent_count'},'measures':measures,'method':'Historical GSS cumulative file; WTSSPS person post-stratification weight; year-specific valid universes retained for financial satisfaction, trust, and fairness. Anchor years are reported to keep the comparison readable.','uncertainty':'Weighted descriptive trend screen without design-based standard errors. GSS question routing, survey mode, sampling, nonresponse, and variable availability differ across years; this is not a harmonized causal trend estimate.','subgroup':'All respondents with valid financial-satisfaction category; trust and fairness measures are conditional on their own valid fields.','counterinterpretation':'The repeated association may reflect cohort, education, age, race, health, party identity, survey mode, changing question administration, or broad changes in social trust rather than financial satisfaction itself.','source_url':'https://gss.norc.org/get-the-data.html','retrieval_hash':'sha256:'+hashlib.sha256(args.archive.read_bytes()).hexdigest()+'; dta:sha256:'+hashlib.sha256(hash_file.read_bytes()).hexdigest(),'status':'compared'})
record={'format':'us-trend-observation-record-v1','trend_id':'us-gss-financial-trust-historical-1972-2024','title':'Financial dissatisfaction and generalized trust show a persistent but non-causal historical association','theme_ids':['cost','voice','work'],'program_theme_ids':['household_room_consumption','trust_identity_meaning','political_judgment_action','unequal_exposure_status','work_control_bargaining'],'source_unit':'GSS cumulative cross-sectional respondent with positive WTSSPS weight','geography':'United States','observations':observations,'related_sources':[{'source_url':'https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook%20R3.pdf','claim':'NORC documents the historical variables, question wording, response codes, and 2024 design changes.','status':'official-definition'},{'source_url':'https://gss.norc.org/get-the-data/stata.html','claim':'NORC provides the cumulative 1972–2024 Stata file used for this screen.','status':'official-data'}],'boundary':'This is an anchor-year descriptive screen from the cumulative GSS file. It does not establish that financial dissatisfaction causes declining trust or fairness judgments, nor does it provide a consistent unbroken annual series. Several years lack comparable field coverage; the 2024 multi-mode/design change and the use of WTSSPS rather than the 2024 nonresponse-adjusted WTSSNRPS weight require separate harmonization before formal trend inference.','retrieval_hash':'sha256:'+hashlib.sha256(args.archive.read_bytes()).hexdigest()}
args.output.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'output':str(args.output),'records':len(d),'observations':len(observations)},indent=2))
