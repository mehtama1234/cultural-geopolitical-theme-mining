#!/usr/bin/env python3
"""Condition MEPS Panel 27 paired health/work outcomes on baseline expenditure."""
import hashlib, json, re, zipfile
from pathlib import Path
import pandas as pd

ARCHIVE = Path('/tmp/meps_h252dat.zip')
SAS = Path('/tmp/h252su.txt')
OUT = Path('analysis/records/us-meps-panel27-baseline-expenditure-outcomes-2022-2023.json')
SOURCE = 'https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-252'

def positions():
    text = SAS.read_text(errors='replace')
    block = text[text.index('* INPUT STATEMENTS;'):text.index('* LABEL STATEMENTS;')]
    return {m.group(2): (int(m.group(1)) - 1, int(m.group(1)) - 1 + int(m.group(4)))
            for m in re.finditer(r'@\s*(\d+)\s+([A-Za-z][A-Za-z0-9_]*)\s+(\$?)(\d+)(?:\.(\d+))?', block)}

def read_fields(fields):
    pos = positions()
    missing = sorted(set(fields) - set(pos))
    if missing:
        raise ValueError(f'missing positions: {missing}')
    with zipfile.ZipFile(ARCHIVE) as z, z.open('h252.dat') as fh:
        frame = pd.read_fwf(fh, colspecs=[pos[x] for x in fields], names=fields, dtype=str, header=None)
    for c in fields:
        if c != 'DUPERSID':
            frame[c] = pd.to_numeric(frame[c].str.strip(), errors='coerce')
    return frame

def wmean(x, value):
    x = x[[value, 'LONGWT']].dropna()
    return float((x[value] * x.LONGWT).sum() / x.LONGWT.sum())

def wshare(x, indicator):
    x = x[['LONGWT']].copy()
    indicator = pd.Series(indicator, index=x.index).astype(float)
    return float((indicator * x.LONGWT).sum() / x.LONGWT.sum() * 100)

def taylor_se(base, valid, outcome):
    valid = pd.Series(valid, index=base.index).fillna(False).astype(bool)
    outcome = pd.Series(outcome, index=base.index)
    valid &= outcome.notna() & base.LONGWT.notna() & base.VARSTR.notna() & base.VARPSU.notna()
    if int(valid.sum()) < 2:
        return None
    w = base.LONGWT.astype(float)
    den = float(w[valid].sum())
    theta = float((w[valid] * outcome[valid].astype(float)).sum() / den)
    linear = pd.Series(0.0, index=base.index)
    linear.loc[valid] = w[valid] * (outcome[valid].astype(float) - theta) / den
    psu = linear.groupby([base.VARSTR, base.VARPSU]).sum()
    all_psus = base.loc[base.VARSTR.notna() & base.VARPSU.notna(), ['VARSTR','VARPSU']].drop_duplicates()
    psu = psu.reindex(all_psus.set_index(['VARSTR','VARPSU']).index, fill_value=0.0)
    variance = 0.0
    for _, values in psu.groupby(level=0):
        m = len(values)
        if m < 2:
            continue
        centered = values.to_numpy(dtype=float) - float(values.mean())
        variance += (m / (m - 1.0)) * float((centered ** 2).sum())
    return float(variance ** 0.5)

def estimate(base, valid, outcome, unit, percent=False):
    value = wshare(base[valid], outcome[valid]) if percent else wmean(base[valid].assign(_outcome=outcome[valid]), '_outcome')
    se = taylor_se(base, valid, outcome)
    if percent:
        se = se * 100 if se is not None else None
    out = {'value': round(value, 4), 'unit': unit, 'value_type': 'weighted_estimate'}
    if se is not None:
        out.update({'standard_error': round(se, 4), 'ci95_low': round(value - 1.96 * se, 4), 'ci95_high': round(value + 1.96 * se, 4), 'variance_method': 'Taylor linearization using LONGWT, VARSTR, and VARPSU'})
    return out

fields = ['DUPERSID','ALL5RDS','RTHLTH3','RTHLTH5','EMPST3','EMPST5','WAGEPY1X','WAGEPY2X','TOTEXPY1','TOTEXPY2','TOTSLFY1','TOTSLFY2','OBTOTVY1','OBTOTVY2','OPTOTVY1','OPTOTVY2','RXTOTY1','RXTOTY2','LONGWT','VARPSU','VARSTR']
d = read_fields(fields)
d = d[d.LONGWT.notna() & d.LONGWT.gt(0)].copy()

# Baseline expenditure quartiles are weighted population cut points among
# nonnegative 2022 expenditure records. They are descriptive conditioning
# bands, not treatment groups and not a proxy for illness severity.
base_valid = d.TOTEXPY1.ge(0)
ordered = d.loc[base_valid, ['TOTEXPY1','LONGWT']].sort_values('TOTEXPY1')
cum = ordered.LONGWT.cumsum()
total = float(ordered.LONGWT.sum())
cuts = [float(ordered.loc[cum.ge(total * q).idxmax(), 'TOTEXPY1']) for q in (.25, .50, .75)]
d['baseline_exp_band'] = pd.cut(d.TOTEXPY1, bins=[-float('inf'), *cuts, float('inf')], labels=['Q1 lowest','Q2','Q3','Q4 highest'], include_lowest=True, duplicates='drop')

paired_health = d.ALL5RDS.eq(1) & d[['TOTEXPY1','TOTEXPY2','RTHLTH3','RTHLTH5']].notna().all(axis=1) & d.TOTEXPY1.ge(0) & d.TOTEXPY2.ge(0)
improved = (d.RTHLTH5 < d.RTHLTH3).astype(float)
worsened = (d.RTHLTH5 > d.RTHLTH3).astype(float)
unchanged = (d.RTHLTH5 == d.RTHLTH3).astype(float)
status_valid = d.ALL5RDS.eq(1) & d.EMPST3.isin([1,2,3,4]) & d.EMPST5.isin([1,2,3,4]) & d.TOTEXPY1.ge(0)
emp3 = d.EMPST3.isin([1,2,3])
emp5 = d.EMPST5.isin([1,2,3])
employed_both = (emp3 & emp5).astype(float)
employed_to_not = (emp3 & ~emp5).astype(float)
not_to_employed = (~emp3 & emp5).astype(float)
wage_valid = d.ALL5RDS.eq(1) & d.WAGEPY1X.ge(0) & d.WAGEPY2X.ge(0) & d.TOTEXPY1.ge(0)
wage_change = d.WAGEPY2X - d.WAGEPY1X
util_valid = d.ALL5RDS.eq(1) & d.TOTEXPY1.ge(0) & d.OBTOTVY1.ge(0) & d.OBTOTVY2.ge(0) & d.OPTOTVY1.ge(0) & d.OPTOTVY2.ge(0) & d.RXTOTY1.ge(0) & d.RXTOTY2.ge(0)
office_visit_change = d.OBTOTVY2 - d.OBTOTVY1
outpatient_visit_change = d.OPTOTVY2 - d.OPTOTVY1
prescription_fill_change = d.RXTOTY2 - d.RXTOTY1
oop_valid = d.ALL5RDS.eq(1) & d.TOTEXPY1.gt(0) & d.TOTEXPY2.ge(0) & d.TOTSLFY1.ge(0) & d.TOTSLFY2.ge(0) & d.TOTEXPY1.ge(0)
oop_change = d.TOTSLFY2 - d.TOTSLFY1
oop_share_2022 = d.TOTSLFY1 / d.TOTEXPY1 * 100
oop_share_2023 = d.TOTSLFY2 / d.TOTEXPY2.where(d.TOTEXPY2.gt(0)) * 100

method = 'MEPS Panel 27 Longitudinal PUF; baseline 2022 total health expenditure quartiles are weighted cut points among nonnegative expenditure records; paired outcomes use ALL5RDS=1 and their own valid-field universes.'
uncertainty = 'Point estimates use LONGWT. Taylor-linearized standard errors and normal-approximation 95% intervals use LONGWT, VARSTR, and VARPSU. Quartile cells are descriptive and do not adjust for baseline health, age, insurance, income, service mix, or illness severity; expenditure is skewed and quartile cut points are sample-specific.'
boundary = 'This conditioning pass does not establish that health expenditure caused health or employment change. Baseline expenditure reflects need, prices, coverage, and treatment. The panel does not identify a dated bill, unpaid care hours, schedule control, treatment delay, household debt, trust, political action, or geopolitical consequence.'
obs = []
bands = [('All valid paired persons', pd.Series(True, index=d.index))] + [(str(label), d.baseline_exp_band.eq(label)) for label in ['Q1 lowest','Q2','Q3','Q4 highest']]
for label, band in bands:
    hvalid = paired_health & band
    evalid = status_valid & band
    vvalid = wage_valid & band
    frame = d[hvalid]
    measures = {
        'health_status_improved': estimate(d, hvalid, improved, 'percent of valid paired persons', True),
        'health_status_worsened': estimate(d, hvalid, worsened, 'percent of valid paired persons', True),
        'health_status_unchanged': estimate(d, hvalid, unchanged, 'percent of valid paired persons', True),
        'employed_both_rounds': estimate(d, evalid, employed_both, 'percent of valid employment-status pairs', True),
        'employed_to_not_employed': estimate(d, evalid, employed_to_not, 'percent of valid employment-status pairs', True),
        'not_employed_to_employed': estimate(d, evalid, not_to_employed, 'percent of valid employment-status pairs', True),
        'wage_income_change': estimate(d, vvalid, wage_change, '2023 minus 2022 dollars per person', False),
        'office_visit_change': estimate(d, util_valid & band, office_visit_change, '2023 minus 2022 visits per person', False),
        'outpatient_visit_change': estimate(d, util_valid & band, outpatient_visit_change, '2023 minus 2022 visits per person', False),
        'prescription_fill_change': estimate(d, util_valid & band, prescription_fill_change, '2023 minus 2022 fills per person', False),
        'out_of_pocket_change': estimate(d, oop_valid & band, oop_change, '2023 minus 2022 dollars per person', False),
        'out_of_pocket_share_2022': estimate(d, oop_valid & band, oop_share_2022, 'person-level out-of-pocket share of total expenditure, percent', False),
        'out_of_pocket_share_2023': estimate(d, oop_valid & band & d.TOTEXPY2.gt(0), oop_share_2023, 'person-level out-of-pocket share of total expenditure, percent', False),
    }
    obs.append({'period':'2022 baseline expenditure band: ' + label, 'denominator': {'value': int(frame.shape[0]), 'unit':'MEPS Panel 27 persons with valid paired expenditure and perceived-health fields', 'value_type':'unweighted_person_count'}, 'measures':measures, 'method':method, 'uncertainty':uncertainty, 'subgroup':label, 'counterinterpretation':boundary, 'source_url':SOURCE, 'retrieval_hash':'sha256:'+hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()+'; sas-layout:sha256:'+hashlib.sha256(SAS.read_bytes()).hexdigest(), 'status':'compared'})

record = {'format':'us-trend-observation-record-v1','trend_id':'us-meps-panel27-baseline-expenditure-outcomes-2022-2023','title':'Baseline health expenditure conditions paired health and work outcomes','theme_ids':['cost','work','time'],'program_theme_ids':['care_health_reproduction','household_room_consumption','work_control_bargaining','unequal_exposure_status'],'source_unit':'MEPS Panel 27 longitudinal person in the civilian noninstitutionalized US population','geography':'United States','observations':obs,'related_sources':[{'source_url':'https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252doc.pdf','claim':'Official Panel 27 documentation defines longitudinal weights, variance variables, field coding, and panel participation.','status':'official-method'},{'source_url':'https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252cb.pdf','claim':'Official codebook defines the expenditure, health, employment, and wage fields.','status':'official-definition'}],'boundary':boundary,'retrieval_hash':'sha256:'+hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({'output':str(OUT),'rows':len(d),'paired_health':int(paired_health.sum()),'cuts':cuts}, indent=2))
