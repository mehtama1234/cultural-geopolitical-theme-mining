#!/usr/bin/env python3
"""Build a weighted 2024 GSS financial-position, trust, and politics layer."""
import hashlib, json
from pathlib import Path
import pandas as pd

DATA = Path('/tmp/gss2024/2024/GSS2024.dta')
ARCHIVE = Path('/tmp/gss2024_stata.zip')
OUT = Path('analysis/records/us-gss-financial-trust-politics-2024.json')
cols = ['wtssnrps','satfin','finalter','finrela','trust','fair','polviews','partyid','whovote24','whovote24a']
d = pd.read_stata(DATA, columns=cols, convert_categoricals=False)
d = d[d.wtssnrps.notna() & (d.wtssnrps > 0)].copy()
d['candidate_valid'] = d.whovote24.isin([1,2,3,4]) | d.whovote24a.isin([1,2,3,4])
d['candidate_trump'] = ((d.whovote24 == 1) | (d.whovote24a == 1)).astype(float)
d['candidate_harris'] = ((d.whovote24 == 2) | (d.whovote24a == 2)).astype(float)

def share(frame, field, condition):
    x = frame[frame[field].notna()].copy()
    return {'value': round(float((condition.loc[x.index].astype(float) * x.wtssnrps).sum() / x.wtssnrps.sum() * 100),4), 'unit':'percent of valid weighted respondents', 'value_type':'weighted_share', 'unweighted_n':int(len(x)), 'weighted_denominator':round(float(x.wtssnrps.sum()),2)}

def make_obs(period, frame, measures, subgroup, universe):
    return {'period':period,'denominator':{'value':int(len(frame)),'unit':'GSS 2024 respondents with positive nonresponse-adjusted post-stratification weight','value_type':'unweighted_respondent_count'},'measures':measures,'method':'2024 GSS cross-section weighted with WTSSNRPS, the person post-stratification weight adjusted for nonresponse; subgroup-specific valid universes retained.','uncertainty':'Weighted descriptive comparison without design-based standard errors in this pass. The 2024 multi-mode design, module-specific missingness, and observational cross-tabs remain important uncertainty sources.','subgroup':subgroup,'counterinterpretation':'Financial position, generalized trust, ideology, party identification, and vote intention may be jointly structured by age, education, race, health, media, prior identity, and local conditions; this does not establish a financial cause.','source_url':'https://gss.norc.org/get-the-data.html','retrieval_hash':'sha256:'+hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()+'; dta:sha256:'+hashlib.sha256(DATA.read_bytes()).hexdigest(),'status':'compared','universe_note':universe}

obs=[]
for code,label in [(1,'pretty well satisfied'),(2,'more or less satisfied'),(3,'not satisfied at all')]:
    g=d[d.satfin==code]
    measures={
      'people_can_be_trusted':share(g,'trust',g.trust==1),
      'people_try_to_be_fair':share(g,'fair',g.fair==2),
      'liberal_or_slightly_liberal':share(g,'polviews',g.polviews.isin([1,2,3])),
      'conservative_or_slightly_conservative':share(g,'polviews',g.polviews.isin([5,6,7]))}
    obs.append(make_obs('2024; financial satisfaction: '+label,g,measures,'Financial satisfaction category: '+label,'Trust and fairness are module-specific valid fields; ideology estimates use their own valid field universe.'))

for code,label in [(1,'better'),(2,'worse'),(3,'stayed same')]:
    g=d[d.finalter==code]
    candidate_valid = g.whovote24.isin([1,2,3,4]) | g.whovote24a.isin([1,2,3,4])
    g = g[g.candidate_valid].copy()
    measures={'people_can_be_trusted':share(g,'trust',g.trust==1),'people_try_to_be_fair':share(g,'fair',g.fair==2),'reported_or_intended_Trump_vote':share(g,'candidate_valid',g.candidate_trump==1),'reported_or_intended_Harris_vote':share(g,'candidate_valid',g.candidate_harris==1)}
    obs.append(make_obs('2024; financial situation trajectory: '+label,g,measures,'Financial trajectory: '+label,'The candidate variables combine pre/post-July 2024 GSS forms; they measure reported intention, not verified turnout or completed vote.'))

record={'format':'us-trend-observation-record-v1','trend_id':'us-gss-financial-trust-politics-2024','title':'Financial position coexists with distinct trust, fairness, and political orientations','theme_ids':['cost','voice','work'],'program_theme_ids':['household_room_consumption','trust_identity_meaning','political_judgment_action','unequal_exposure_status','work_control_bargaining'],'source_unit':'GSS 2024 cross-sectional respondent with nonresponse-adjusted post-stratification weight','geography':'United States','observations':obs,'related_sources':[{'source_url':'https://gss.norc.org/content/dam/gss/get-documentation/pdf/codebook/GSS%202024%20Codebook%20R3.pdf','claim':'NORC documents 2024 question wording, response codes, multi-mode changes, and variable universes.','status':'official-definition'}],'boundary':'This is a weighted cross-sectional GSS 2024 comparison. It does not establish that financial satisfaction or trajectory causes trust, fairness judgments, ideology, or vote intention; it does not measure a specific bill, local exposure, institutional remedy, cultural identity formation, or geopolitical action. The 2024 file has module-specific missingness and changed multi-mode design, so it should not be treated as a direct unadjusted continuation of earlier GSS years without a separate trend audit.','retrieval_hash':'sha256:'+hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'output':str(OUT),'rows':len(d),'observations':len(obs),'archive_sha256':record['retrieval_hash']},indent=2))
