#!/usr/bin/env python3
"""Build a bounded, weighted 2020 RECS household energy-burden layer."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
import pandas as pd

RAW = Path("/tmp/recs2020_public_v7.csv")
OUT = Path("analysis/records/us-recs-energy-burden-income-assistance-2020.json")

cols = ["MONEYPY", "TOTALDOL", "NWEIGHT", "ENERGYASST", "ENERGYASST20",
        "PAYHELP", "NOHEATBROKE", "NOHEATHELP", "NOACBROKE", "NOACHELP",
        "KOWNRENT", "STATE_FIPS", "NHSLDMEM", "NUMCHILD"] + [f"NWEIGHT{i}" for i in range(1, 61)]
d = pd.read_csv(RAW, usecols=cols)
rw = [f"NWEIGHT{i}" for i in range(1, 61)]

# RECS publishes income bands, not continuous income. Midpoints make this an
# explicitly bounded affordability proxy, not an observed household ratio.
mid = {1:2500, 2:6249.5, 3:8749.5, 4:11249.5, 5:13749.5, 6:17499.5,
       7:22499.5, 8:27499.5, 9:32499.5, 10:37499.5, 11:44999.5,
       12:54999.5, 13:67499.5, 14:87499.5, 15:124999.5, 16:200000}
d["income_midpoint"] = d.MONEYPY.map(mid)
d["burden_proxy"] = d.TOTALDOL / d.income_midpoint
d["income_band"] = pd.cut(d.MONEYPY, [0, 5, 9, 13, 16], labels=["<$15k", "$15k-$35k", "$35k-$75k", "$75k+"])

def est(frame, col, predicate=None):
    x = frame.copy()
    if predicate is not None: x = x[predicate(x)]
    x = x[x[col].notna() & x.NWEIGHT.notna()]
    if len(x) == 0: return None
    y = x[col].astype(float).to_numpy(); w = x.NWEIGHT.to_numpy()
    den = w.sum(); theta = float((w*y).sum()/den)
    reps = []
    for c in rw:
        wr = x[c].to_numpy()
        reps.append(float((wr*y).sum()/wr.sum()) if wr.sum() else np.nan)
    reps = np.array(reps)
    se = float(np.sqrt((59/60)*np.nansum((reps-theta)**2)))
    return {"value": round(theta, 4), "approx_95_percent_ci": [round(theta-1.96*se,4), round(theta+1.96*se,4)],
            "standard_error": round(se,4), "n": int(len(x)), "weighted_denominator": round(float(den), 2)}

def share(frame, col, yes=1):
    return est(frame, "_indicator", lambda x: x[col].isin([0, 1]).to_numpy()) if False else None

observations = []
for band in ["<$15k", "$15k-$35k", "$35k-$75k", "$75k+"]:
    x = d[d.income_band == band]
    row = {"period": "2020 survey year", "denominator": {"value": int(len(x)), "unit": "RECS responding households in income band", "value_type": "unweighted household count"},
           "measures": {"mean_total_energy_expenditure": {**est(x, "TOTALDOL"), "unit": "2020 dollars", "value_type": "weighted_mean"},
                        "mean_energy_burden_proxy": {**est(x, "burden_proxy"), "unit": "share of income-band midpoint", "value_type": "weighted_mean_proxy"}},
           "method": "Final RECS analysis weight and 60 supplied Jackknife replicate weights; income-band midpoint used only as a bounded affordability proxy.",
           "uncertainty": "RECS recommends suppressing estimates with RSE above 50% or fewer than 10 sample households; the record retains n and replicate-weight intervals for review.",
           "subgroup": band, "counterinterpretation": "The midpoint proxy can overstate or understate the true burden, especially in the open-ended lowest and highest income bands; modeled energy expenditures are not bills observed at one moment.",
           "source_url": "https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata", "retrieval_hash": "sha256:" + hashlib.sha256(RAW.read_bytes()).hexdigest(), "status": "compared"}
    observations.append(row)

for field, label in [("ENERGYASST", "ever received home energy assistance"), ("ENERGYASST20", "received home energy assistance in 2020"),
                     ("PAYHELP", "received energy assistance after disconnection notice"), ("NOHEATBROKE", "could not use broken heating equipment because repair/replacement was unaffordable"),
                     ("NOHEATHELP", "received help after heating equipment was unaffordable to repair"), ("NOACBROKE", "air-conditioning equipment broke"), ("NOACHELP", "received help after air-conditioning equipment was unaffordable to repair")]:
    x = d[d[field].isin([0, 1])].copy(); x["_indicator"] = (x[field] == 1).astype(float)
    z = est(x, "_indicator")
    observations.append({"period": "2020 survey year", "denominator": {"value": int(len(x)), "unit": "RECS households with valid field", "value_type": "unweighted household count"},
      "measures": {"share": {**z, "unit": "percent", "value": round(z["value"]*100,4), "approx_95_percent_ci": [round(v*100,4) for v in z["approx_95_percent_ci"]], "standard_error": round(z["standard_error"]*100,4), "value_type": "weighted_share"}},
      "method": "Final RECS analysis weight and 60 supplied Jackknife replicate weights; field-specific valid universe retained.",
      "uncertainty": "Self-reported assistance and hardship measures; RECS imputation flags should be consulted for field-level sensitivity analysis.", "subgroup": label,
      "counterinterpretation": "Assistance receipt and equipment hardship are correlates of energy vulnerability, not a complete measure of energy insecurity or household welfare.",
      "source_url": "https://www.eia.gov/consumption/residential/data/2020/index.php?view=microdata", "retrieval_hash": "sha256:" + hashlib.sha256(RAW.read_bytes()).hexdigest(), "status": "compared"})

record = {"format":"us-trend-observation-record-v1", "trend_id":"us-recs-energy-burden-income-assistance-2020",
 "title":"Energy expenditure and assistance vulnerability vary sharply across household income bands", "theme_ids":["cost","energy"],
 "program_theme_ids":["household_room_consumption","unequal_exposure_status","care_health_reproduction","public_systems_feedback"],
 "source_unit":"occupied U.S. household responding to the 2020 Residential Energy Consumption Survey", "geography":"United States",
 "observations":observations, "related_sources":[{"source_url":"https://www.eia.gov/consumption/residential/data/2020/pdf/microdata-guide.pdf","claim":"EIA documents the final weight, 60 Jackknife replicate weights, and recommended reliability standards.","status":"official-method"}],
 "boundary":"This is a 2020 cross-sectional household energy-vulnerability layer. It does not establish causal effects, monthly payment shocks, health outcomes, political attitudes, or consumer behavior. The energy-burden measure is a midpoint-of-income-band proxy; modeled annual energy expenditures should not be read as observed bills.",
 "retrieval_hash":"sha256:" + hashlib.sha256(RAW.read_bytes()).hexdigest()}
OUT.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"output":str(OUT),"observations":len(observations),"raw_sha256":record["retrieval_hash"]}, indent=2))
