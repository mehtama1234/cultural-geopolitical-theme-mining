#!/usr/bin/env python3
"""Extract a bounded MEPS Panel 27 health-cost longitudinal layer."""
import hashlib, json, re, zipfile
from pathlib import Path
import pandas as pd

ARCHIVE = Path('/tmp/meps_h252dat.zip')
SAS = Path('/tmp/h252su.txt')
OUT = Path('analysis/records/us-meps-panel27-health-cost-longitudinal-2022-2023.json')

def get_positions():
    text = SAS.read_text(errors='replace')
    block = text[text.index('* INPUT STATEMENTS;'):text.index('* LABEL STATEMENTS;')]
    out = {}
    for m in re.finditer(r'@\s*(\d+)\s+([A-Za-z][A-Za-z0-9_]*)\s+(\$?)(\d+)(?:\.(\d+))?', block):
        start, name, width = int(m.group(1)), m.group(2), int(m.group(4))
        out[name] = (start - 1, start - 1 + width)
    return out

def read_fields(fields):
    pos = get_positions()
    missing = sorted(set(fields) - set(pos))
    if missing: raise ValueError(f'missing positions: {missing}')
    with zipfile.ZipFile(ARCHIVE) as z:
        with z.open('h252.dat') as fh:
            d = pd.read_fwf(fh, colspecs=[pos[x] for x in fields], names=fields, dtype=str, header=None)
    for c in fields:
        if c != 'DUPERSID': d[c] = pd.to_numeric(d[c].str.strip(), errors='coerce')
    return d

def weighted_mean(frame, value):
    x = frame[[value, 'LONGWT']].dropna(); return float((x[value] * x.LONGWT).sum() / x.LONGWT.sum())

def weighted_share(frame, indicator):
    x = frame[['LONGWT']].dropna(); return float((indicator.loc[x.index] * x.LONGWT).sum() / x.LONGWT.sum() * 100)

def taylor_se(base, universe, outcome):
    """Taylor-linearized SE for a weighted mean over a MEPS domain.

    ``universe`` identifies valid records in the estimand's denominator and
    ``outcome`` is aligned to ``base``.  Non-domain records contribute zero
    to the linearized PSU total, which preserves the design information when
    estimating a subpopulation or a field-specific valid universe.
    """
    u = pd.Series(universe, index=base.index).fillna(False).astype(bool)
    y = pd.Series(outcome, index=base.index)
    valid = u & y.notna() & base.LONGWT.notna() & base.VARSTR.notna() & base.VARPSU.notna()
    if int(valid.sum()) < 2:
        return None
    w = base.LONGWT.astype(float)
    den = float(w[valid].sum())
    if den <= 0:
        return None
    theta = float((w[valid] * y[valid].astype(float)).sum() / den)
    linearized = pd.Series(0.0, index=base.index)
    linearized.loc[valid] = w[valid] * (y[valid].astype(float) - theta) / den
    # Keep zero-contribution PSUs in the stratum frame for domain estimates.
    psu = linearized.groupby([base.VARSTR, base.VARPSU]).sum()
    all_psus = base.loc[base.VARSTR.notna() & base.VARPSU.notna(), ['VARSTR', 'VARPSU']].drop_duplicates()
    all_psus = all_psus.set_index(['VARSTR', 'VARPSU']).index
    psu = psu.reindex(all_psus, fill_value=0.0)
    variance = 0.0
    strata = 0
    for _, values in psu.groupby(level=0):
        m = len(values)
        if m < 2:
            continue
        centered = values.to_numpy(dtype=float) - float(values.mean())
        variance += (m / (m - 1.0)) * float((centered ** 2).sum())
        strata += 1
    return float(variance ** 0.5) if strata and variance >= 0 else None

def precision(value, se, unit, scale=1.0):
    """Attach a normal-approximation SE and 95% interval in the same unit."""
    if se is None:
        return {'value': value, 'unit': unit, 'value_type': 'weighted_estimate'}
    se = float(se)
    return {'value': value, 'unit': unit, 'value_type': 'weighted_estimate',
            'standard_error': round(se, 4),
            'ci95_low': round(float(value) - 1.96 * se, 4),
            'ci95_high': round(float(value) + 1.96 * se, 4),
            'variance_method': 'Taylor linearization using LONGWT, VARSTR, and VARPSU'}

fields = ['DUPERSID','PANEL','ALL5RDS','AGEY1X','AGEY2X','RTHLTH3','RTHLTH5','EMPST3','EMPST5','WAGEPY1X','WAGEPY2X','TOTEXPY1','TOTEXPY2','TOTSLFY1','TOTSLFY2','FAMINCY1','FAMINCY2','POVCATY1','POVCATY2','UNINSY1','UNINSY2','INSURCY1','INSURCY2','LONGWT','VARPSU','VARSTR']
d = read_fields(fields)
d = d[d.LONGWT.notna() & (d.LONGWT > 0)].copy()
source_url = 'https://meps.ahrq.gov/mepsweb/data_stats/download_data_files_detail.jsp?cboPufNumber=HC-252'
hashes = 'sha256:' + hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() + '; sas-layout:sha256:' + hashlib.sha256(SAS.read_bytes()).hexdigest()
method = 'MEPS Panel 27 Longitudinal PUF; final LONGWT used for weighted person estimates; annual 2022 and 2023 fields are taken from the released longitudinal file.'
uncertainty = 'Taylor-linearized standard errors and normal-approximation 95% intervals use LONGWT, VARSTR, and VARPSU; AHRQ documents these as the longitudinal estimation variables. Estimates remain descriptive and retain valid-field denominators. Expenditure distributions are skewed, so intervals should not be read as a complete robustness analysis.'
counter = 'Medical expenditure and payment patterns reflect health need, age, insurance, employment, income, provider prices, and reporting; they do not identify a single bill, institutional decision, or cultural response.'

def make_obs(period, frame, measures, subgroup, meth=method, unc=uncertainty):
    return {'period': period, 'denominator': {'value': int(len(frame)), 'unit': 'MEPS Panel 27 persons with positive longitudinal weight', 'value_type': 'unweighted_person_count'}, 'measures': measures, 'method': meth, 'uncertainty': unc, 'subgroup': subgroup, 'counterinterpretation': counter, 'source_url': source_url, 'retrieval_hash': hashes, 'status': 'compared'}

observations = []
for year, exp, oop, unins, insur in [(2022,'TOTEXPY1','TOTSLFY1','UNINSY1','INSURCY1'), (2023,'TOTEXPY2','TOTSLFY2','UNINSY2','INSURCY2')]:
    x = d[d[exp].notna() & (d[exp] >= 0)].copy()
    observations.append(make_obs(str(year), x, {'total_health_expenditure': {'value': round(weighted_mean(x, exp),4), 'unit':'dollars per person in calendar year', 'value_type':'weighted_mean'}, 'out_of_pocket_expenditure': {'value': round(weighted_mean(x, oop),4), 'unit':'dollars per person in calendar year', 'value_type':'weighted_mean'}, 'uninsured_any_time': {'value': round(weighted_share(x, (x[unins] == 1).astype(float)),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}, 'continuous_coverage': {'value': round(weighted_share(x, (x[insur] == 1).astype(float)),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}}, 'Panel 27 persons with valid annual expenditure fields'))

x = d[(d.ALL5RDS == 1) & d[['TOTEXPY1','TOTEXPY2','TOTSLFY1','TOTSLFY2','RTHLTH3','RTHLTH5']].notna().all(axis=1)].copy()
x['exp_change'] = x.TOTEXPY2 - x.TOTEXPY1
x['oop_change'] = x.TOTSLFY2 - x.TOTSLFY1
health_change = pd.Series((x.RTHLTH5 < x.RTHLTH3).astype(float), index=x.index)
health_worse = pd.Series((x.RTHLTH5 > x.RTHLTH3).astype(float), index=x.index)
observations.append(make_obs('2022→2023; all-five-round participation and valid paired fields', x, {'total_health_expenditure_change': {'value': round(weighted_mean(x, 'exp_change'),4), 'unit':'2023 minus 2022 dollars per person', 'value_type':'weighted_mean_change'}, 'out_of_pocket_expenditure_change': {'value': round(weighted_mean(x, 'oop_change'),4), 'unit':'2023 minus 2022 dollars per person', 'value_type':'weighted_mean_change'}, 'health_status_improved': {'value': round(weighted_share(x, health_change),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}, 'health_status_worsened': {'value': round(weighted_share(x, health_worse),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}, 'health_status_unchanged': {'value': round(100 - weighted_share(x, health_change) - weighted_share(x, health_worse),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}}, 'Panel 27 longitudinal persons with ALL5RDS=1 and valid paired expenditure/health fields', method, uncertainty + ' The paired cell is conditional on valid fields and full-round participation; health direction uses ordinal perceived-health codes and is not a clinical outcome.'))

for code, label in [(1, 'poor/negative income'), (2, 'near-poor income'), (3, 'low income'), (4, 'middle income'), (5, 'high income')]:
    g = x[x.POVCATY1 == code]
    if len(g) < 10: continue
    observations.append(make_obs('2022→2023; baseline family income-to-poverty category: ' + label, g, {'total_health_expenditure_change': {'value': round(weighted_mean(g, 'exp_change'),4), 'unit':'2023 minus 2022 dollars per person', 'value_type':'weighted_mean_change'}, 'out_of_pocket_expenditure_change': {'value': round(weighted_mean(g, 'oop_change'),4), 'unit':'2023 minus 2022 dollars per person', 'value_type':'weighted_mean_change'}, 'health_status_improved': {'value': round(weighted_share(g, health_change.loc[g.index]),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}, 'health_status_worsened': {'value': round(weighted_share(g, health_worse.loc[g.index]),4), 'unit':'percent of valid persons', 'value_type':'weighted_share'}}, 'Panel 27 longitudinal persons with baseline 2022 poverty category ' + label, method + ' Baseline material position is the official five-category family income-to-poverty measure.', uncertainty + ' Poverty-category cells are descriptive and do not adjust for age, health, insurance, or composition.'))

# Employment and wage endpoints use their own valid universes. EMPST3 and
# EMPST5 are round-specific employment-status measures; WAGEPY1X/WAGEPY2X are
# annual person wage-income fields for 2022 and 2023. They extend the same
# panel arrow without treating employment continuity as a health-cost effect.
status_valid = d.ALL5RDS.eq(1) & d.EMPST3.isin([1, 2, 3, 4]) & d.EMPST5.isin([1, 2, 3, 4])
employed3 = d.EMPST3.isin([1, 2, 3]).astype(float)
employed5 = d.EMPST5.isin([1, 2, 3]).astype(float)
work = d[status_valid].copy()
work['employed_both'] = ((employed3 == 1) & (employed5 == 1)).astype(float)
work['employed_to_not'] = ((employed3 == 1) & (employed5 == 0)).astype(float)
work['not_to_employed'] = ((employed3 == 0) & (employed5 == 1)).astype(float)
def scaled_se(value, scale):
    return round(value * scale, 4) if value is not None else None

work_measures = {
    'employed_both_rounds': precision(round(weighted_share(work, work.employed_both), 4), scaled_se(taylor_se(d, status_valid, work.employed_both), 100), 'percent of valid persons'),
    'employed_to_not_employed': precision(round(weighted_share(work, work.employed_to_not), 4), scaled_se(taylor_se(d, status_valid, work.employed_to_not), 100), 'percent of valid persons'),
    'not_employed_to_employed': precision(round(weighted_share(work, work.not_to_employed), 4), scaled_se(taylor_se(d, status_valid, work.not_to_employed), 100), 'percent of valid persons'),
}
wage_valid = d.ALL5RDS.eq(1) & d.WAGEPY1X.ge(0) & d.WAGEPY2X.ge(0)
d['wage_change'] = d.WAGEPY2X - d.WAGEPY1X
wage = d[wage_valid].copy()
wage_se = taylor_se(d, wage_valid, d.wage_change)
work_measures['wage_income_change'] = precision(round(weighted_mean(wage, 'wage_change'), 4), round(wage_se, 4) if wage_se is not None else None, '2023 minus 2022 dollars per person')
observations.append(make_obs('2022→2023; employment status and wage-income continuity', work, work_measures, 'Panel 27 longitudinal persons with ALL5RDS=1 and valid EMPST3/EMPST5 status; wage-income change uses its separate valid paired wage universe', method + ' EMPST3/EMPST5 are round-specific employment-status fields; WAGEPY1X/WAGEPY2X are annual person wage-income fields. Employment and wage measures use distinct valid universes.', uncertainty + ' Employment status is not a job-quality, hours, schedule-control, or causal health-cost measure. Wage-income change is conditional on nonnegative paired wage fields and does not measure household income.',))

# Add design-based precision after the point-estimate table is assembled. The
# masks intentionally mirror each observation's valid-field denominator. This
# keeps a missing field out of the numerator and denominator while retaining
# zero-contribution PSUs for Taylor domain estimation.
for obs in observations:
    period = obs['period']
    subgroup_code = None
    if 'baseline family income-to-poverty category:' in period:
        subgroup_code = {
            'poor/negative income': 1, 'near-poor income': 2,
            'low income': 3, 'middle income': 4, 'high income': 5,
        }[period.split(': ', 1)[1]]
    base_mask = pd.Series(True, index=d.index)
    if subgroup_code is not None:
        base_mask &= d.POVCATY1.eq(subgroup_code)

    if period == '2022':
        specs = {
            'total_health_expenditure': ('TOTEXPY1', d.TOTEXPY1.ge(0), 'dollars per person in calendar year'),
            'out_of_pocket_expenditure': ('TOTSLFY1', d.TOTSLFY1.ge(0), 'dollars per person in calendar year'),
            'uninsured_any_time': ('UNINSY1', d.UNINSY1.eq(1), 'percent of valid persons'),
            'continuous_coverage': ('INSURCY1', d.INSURCY1.eq(1), 'percent of valid persons'),
        }
        universes = {
            'total_health_expenditure': d.TOTEXPY1.ge(0),
            'out_of_pocket_expenditure': d.TOTSLFY1.ge(0),
            'uninsured_any_time': d.UNINSY1.notna(),
            'continuous_coverage': d.INSURCY1.notna(),
        }
        for name, (field, _, unit) in specs.items():
            scale = 100 if name in ('uninsured_any_time', 'continuous_coverage') else 1
            outcome = d[field].eq(1).astype(float) if scale == 100 else d[field]
            se = taylor_se(d, universes[name], outcome)
            m = obs['measures'][name]
            obs['measures'][name] = precision(m['value'], round(se * scale, 4) if se is not None else None, unit)
    elif period == '2023':
        fields = {
            'total_health_expenditure': ('TOTEXPY2', d.TOTEXPY2.ge(0), 'dollars per person in calendar year'),
            'out_of_pocket_expenditure': ('TOTSLFY2', d.TOTSLFY2.ge(0), 'dollars per person in calendar year'),
            'uninsured_any_time': ('UNINSY2', d.UNINSY2.notna(), 'percent of valid persons'),
            'continuous_coverage': ('INSURCY2', d.INSURCY2.notna(), 'percent of valid persons'),
        }
        for name, (field, valid, unit) in fields.items():
            valid &= base_mask
            scale = 100 if name in ('uninsured_any_time', 'continuous_coverage') else 1
            outcome = d[field].eq(1).astype(float) if scale == 100 else d[field]
            se = taylor_se(d, valid, outcome)
            m = obs['measures'][name]
            obs['measures'][name] = precision(m['value'], round(se * scale, 4) if se is not None else None, unit)
    elif period.startswith('2022→2023'):
        valid = base_mask & d.ALL5RDS.eq(1) & d[['TOTEXPY1','TOTEXPY2','TOTSLFY1','TOTSLFY2','RTHLTH3','RTHLTH5']].notna().all(axis=1)
        specs = {
            'total_health_expenditure_change': (d.TOTEXPY2 - d.TOTEXPY1, '2023 minus 2022 dollars per person', 1),
            'out_of_pocket_expenditure_change': (d.TOTSLFY2 - d.TOTSLFY1, '2023 minus 2022 dollars per person', 1),
            'health_status_improved': ((d.RTHLTH5 < d.RTHLTH3).astype(float), 'percent of valid persons', 100),
            'health_status_worsened': ((d.RTHLTH5 > d.RTHLTH3).astype(float), 'percent of valid persons', 100),
            'health_status_unchanged': ((d.RTHLTH5 == d.RTHLTH3).astype(float), 'percent of valid persons', 100),
        }
        for name, (outcome, unit, scale) in specs.items():
            # The point estimate is a percent for indicators and dollars for
            # changes; the linearized mean is scaled only for percentages.
            se = taylor_se(d, valid, outcome)
            m = obs['measures'].get(name)
            if m is not None:
                obs['measures'][name] = precision(m['value'], round(se * scale, 4) if se is not None else None, unit)

record = {'format':'us-trend-observation-record-v1','trend_id':'us-meps-panel27-health-cost-longitudinal-2022-2023','title':'Health expenditure and out-of-pocket cost add a longitudinal material-pressure layer','theme_ids':['cost','work','time'],'program_theme_ids':['care_health_reproduction','household_room_consumption','unequal_exposure_status','work_control_bargaining','public_systems_feedback'],'source_unit':'MEPS Panel 27 longitudinal person in the civilian noninstitutionalized U.S. population','geography':'United States','observations':observations,'related_sources':[{'source_url':'https://meps.ahrq.gov/data_stats/download_data/pufs/h252/h252doc.shtml','claim':'AHRQ documents the Panel 27 longitudinal file, LONGWT, panel retention, annual expenditure and health fields, and the VARSTR/VARPSU variance structure for longitudinal estimates.','status':'official-method'},{'source_url':'https://meps.ahrq.gov/mepsweb/data_stats/download_data/pufs/h252/h252cb.pdf','claim':'The official codebook defines the longitudinal variables and valid coding.','status':'official-definition'}],'boundary':'This layer tests longitudinal health-cost and health-status co-movement for one MEPS panel. It does not establish that expenditure caused health change, identify a specific price or institutional actor, measure time/care allocation, or connect health costs to trust, politics, consumer exit, or geopolitical consequences. The paired analysis is conditional on valid fields and full-round participation. Taylor-linearized precision uses the released variance units; normal intervals do not resolve expenditure skewness, nonresponse, attrition, or subgroup composition.','retrieval_hash':'sha256:'+hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'output':str(OUT),'rows':len(d),'paired_rows':len(x),'archive_sha256':record['retrieval_hash']},indent=2))
